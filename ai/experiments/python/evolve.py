"""
evolve.py - evolutionary search over experiment-scoped active parameter subsets.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
import torch

from batched_field import BatchedField, array_to_params
from experiment_paths import (
    SUPPORTED_EXPERIMENTS,
    SUPPORTED_SYMMETRY_BREAKS,
    default_genome_path,
)
from genome_io import (
    ensure_genome_file,
    genome_active_row,
    genome_matches_run,
    load_genome,
    save_genome,
)
from parameter_policy import (
    active_param_bounds,
    active_param_defaults,
    active_param_names,
    experiment_dimension_count,
    parameter_summary_lines,
    resolve_runtime_params,
    resolved_searchable_matrix,
)
from search_space import (
    clamp_physical_row,
    physical_to_search_value,
    physical_matrix_to_search,
    search_matrix_to_physical,
    transform_bounds,
)

BASE_DIR = Path(__file__).resolve().parent
CANONICAL_EVAL_SLOT = 0


def clamp_params(arr: np.ndarray, active_names: tuple[str, ...], search_bounds: dict[str, tuple[float, float]]) -> np.ndarray:
    for i, name in enumerate(active_names):
        lo, hi = search_bounds[name]
        arr[:, i] = np.clip(arr[:, i], lo, hi)
    return arr


def mutate(arr: np.ndarray, active_names: tuple[str, ...], search_bounds: dict[str, tuple[float, float]], strength: float = 1.0) -> np.ndarray:
    out = arr.copy()
    for i, name in enumerate(active_names):
        lo, hi = search_bounds[name]
        sigma = strength * 0.15 * (hi - lo)
        out[:, i] += np.random.randn(len(arr)) * sigma
    return clamp_params(out, active_names, search_bounds)


def crossover(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    mask = np.random.rand(*a.shape) < 0.5
    return np.where(mask, a, b)


def evolve_population(
    arr: np.ndarray,
    fitness: np.ndarray,
    active_names: tuple[str, ...],
    search_bounds: dict[str, tuple[float, float]],
    mutation_strength: float = 1.0,
) -> np.ndarray:
    pop_size = len(arr)
    elite_n = pop_size // 2
    ranked = np.argsort(fitness)[::-1]
    elite = arr[ranked[:elite_n]]

    children = []
    while len(children) < pop_size - elite_n:
        i, j = np.random.choice(elite_n, size=2, replace=False)
        child = crossover(elite[i:i + 1], elite[j:j + 1])
        child = mutate(child, active_names, search_bounds, strength=mutation_strength)
        children.append(child[0])
    return np.vstack([elite, np.array(children)])


def resolve_path(path: str | None) -> Path | None:
    if path is None:
        return None
    p = Path(path)
    if p.is_absolute():
        return p
    if p.exists():
        return p.resolve()
    return BASE_DIR / p


def _bar(v: float, width: int = 20) -> str:
    filled = int(round(max(0.0, min(1.0, float(v))) * width))
    return "#" * filled + "-" * (width - filled)


def print_generation(
    gen: int,
    gens: int,
    fitness: np.ndarray,
    active_arr: np.ndarray,
    elapsed: float,
    metrics: dict | None,
    *,
    experiment: str,
    active_names: tuple[str, ...],
    search_bounds: dict[str, tuple[float, float]],
):
    best_idx = int(np.argmax(fitness))
    best_f = fitness[best_idx]
    mean_f = fitness.mean()
    best_active = active_arr[best_idx]
    resolved_best = resolve_runtime_params(
        experiment,
        active_values={name: float(best_active[i]) for i, name in enumerate(active_names)},
    )
    active_lines, frozen_lines = parameter_summary_lines(experiment, resolved_best)

    print(f"\n=== Generation {gen + 1}/{gens}  ({elapsed:.1f}s) ===")
    print(f"  fitness  best={best_f:.4f}  mean={mean_f:.4f}  [{_bar(min(best_f, 1.0))}]")
    print(f"  active_dims={len(active_names)}")
    if metrics:
        def _fmt(arr_):
            if arr_ is None:
                return "--"
            val = arr_[best_idx]
            return f"{val:.3f}" if np.isfinite(val) else "--"

        print("  best metrics:")
        if "choice_strength" in metrics:
            print(f"         choice = {_fmt(metrics.get('choice_strength'))}  consistent = {_fmt(metrics.get('choice_consistency'))}")
            print(f"        persist = {_fmt(metrics.get('overnight_persistence'))}  switch = {_fmt(metrics.get('switch_penalty'))}")
            print(f"        parity = {_fmt(metrics.get('cue_parity'))}  eff = {_fmt(metrics.get('efficiency_reward'))}  A = {_fmt(metrics.get('a_mean'))}  B = {_fmt(metrics.get('b_mean'))}")
            print(f"        cueSeq = {metrics.get('cue_sequence', '--')}")
        elif "peak_S_growth_mean" in metrics:
            print(f"          peak = {_fmt(metrics.get('peak_S_growth_mean'))}  grow+ = {_fmt(metrics.get('positive_growth_mean'))}  frac+ = {_fmt(metrics.get('positive_growth_fraction'))}  frac* = {_fmt(metrics.get('positive_growth_fraction_score'))}")
            print(f"        Sfinal = {_fmt(metrics.get('final_S_mass'))}  Sstd = {_fmt(metrics.get('final_S_std'))}  Sstd^ = {_fmt(metrics.get('peak_S_std'))}")
            print(f"           Sf* = {_fmt(metrics.get('final_structure_score'))}  Sp* = {_fmt(metrics.get('peak_structure_score'))}  S* = {_fmt(metrics.get('structure_score'))}")
            print(f"         hold = {_fmt(metrics.get('final_retention_mean'))}  Rslow = {_fmt(metrics.get('final_R_slow_mean'))}")
            print(f"         Cslow = {_fmt(metrics.get('final_C_slow_mean'))}  nS = {_fmt(metrics.get('temporal_structural_samples'))}  eff = {_fmt(metrics.get('efficiency_reward'))}")
        else:
            print(f"           corr = {_fmt(metrics.get('corr'))}  retention = {_fmt(metrics.get('retention'))}  faithful = {_fmt(metrics.get('frequency_faithfulness'))}  eff = {_fmt(metrics.get('efficiency_reward'))}")
            print(f"         dayT = {_fmt(metrics.get('day_period'))}  nightT = {_fmt(metrics.get('night_period'))}  ratio = {_fmt(metrics.get('period_ratio'))}")

    print("  active params:")
    for i, name in enumerate(active_names):
        lo, hi = search_bounds[name]
        search_val = physical_to_search_value(name, float(best_active[i]))
        normed = (search_val - lo) / (hi - lo)
        print(f"    {name:>15s} = {best_active[i]:.5f}  [{_bar(normed, 15)}]")
    print("  frozen searchable params:")
    for name, value in frozen_lines:
        print(f"    {name:>15s} = {value:.5f}")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--B", type=int, default=16, help="Population size (default 16)")
    p.add_argument("--N", type=int, default=32, help="Grid size (default 32)")
    p.add_argument("--gens", type=int, default=40, help="Generations (default 40)")
    p.add_argument("--device", default="auto")
    p.add_argument("--experiment", choices=SUPPORTED_EXPERIMENTS, default="symmetry_v1")
    p.add_argument("--symmetry-break", choices=SUPPORTED_SYMMETRY_BREAKS, default="spatial")
    p.add_argument("--resume", default=None, help="Path to an experiment-scoped genome to seed slot 0")
    p.add_argument("--episodes", type=int, default=1, help="Episodes per generation for fitness averaging (default 1)")
    p.add_argument("--seed", type=int, default=None, help="Random seed for reproducible search and replay")
    p.add_argument("--seed_default", action="store_true", help="Include one copy of the experiment default active set in slot 0")
    p.add_argument("--reset", action="store_true", help="Delete the experiment-scoped best genome and start from scratch")
    return p.parse_args()


def pick_device(requested: str) -> str:
    if requested == "auto":
        if torch.cuda.is_available():
            print(f"GPU: {torch.cuda.get_device_name(0)}")
            return "cuda"
        print("No CUDA GPU - using CPU")
        return "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, falling back to CPU")
        return "cpu"
    return requested


def main():
    args = parse_args()
    if args.experiment != "symmetry_v1":
        args.symmetry_break = None
    if args.seed is not None:
        np.random.seed(args.seed)
        torch.manual_seed(args.seed)

    device = pick_device(args.device)
    pop_size = args.B
    grid_size = args.N
    gens = args.gens
    episodes = args.episodes
    active_names = active_param_names(args.experiment)
    active_bounds = active_param_bounds(args.experiment)
    search_bounds = transform_bounds(active_names, active_bounds)
    genome_file = default_genome_path(BASE_DIR, args.experiment)
    if args.reset and genome_file.exists():
        genome_file.unlink()
        print(f"Reset: deleted {genome_file}")
    ensure_genome_file(genome_file, args.experiment, args.symmetry_break)

    print("Field Dynamics - Evolutionary Search")
    print(f"  population={pop_size}  grid={grid_size}x{grid_size}  generations={gens}  episodes/gen={episodes}  device={device}")
    print(f"  experiment={args.experiment}  symmetry_break={args.symmetry_break}  active_dims={experiment_dimension_count(args.experiment)}")
    print(f"  genome_path={genome_file}")
    print()

    active_init = np.zeros((pop_size, len(active_names)), dtype=np.float32)
    for i, name in enumerate(active_names):
        lo, hi = active_bounds[name]
        active_init[:, i] = np.random.uniform(lo, hi, pop_size)

    default_active_row = clamp_physical_row(
        active_names,
        np.array([active_param_defaults(args.experiment)[name] for name in active_names], dtype=np.float32),
        active_bounds,
    ).astype(np.float32, copy=False)
    if args.seed_default:
        active_init[0] = default_active_row

    seed_genome = None
    if args.resume:
        resume_path = resolve_path(args.resume)
        seed_genome = load_genome(resume_path)
        if not genome_matches_run(seed_genome, args.experiment, args.symmetry_break):
            raise SystemExit(
                f"{resume_path} targets {seed_genome.get('experiment')}:{seed_genome.get('symmetry_break')}, "
                f"not {args.experiment}:{args.symmetry_break}"
            )
        print(f"Resuming from {resume_path}  (gen {seed_genome['generation']}, fitness {seed_genome['fitness']:.4f})")
        active_init[0] = clamp_physical_row(
            active_names,
            genome_active_row(seed_genome, args.experiment, active_names).astype(np.float32, copy=False),
            active_bounds,
        ).astype(np.float32, copy=False)
    elif genome_file.exists():
        genome = load_genome(genome_file)
        if genome_matches_run(genome, args.experiment, args.symmetry_break):
            seed_genome = genome
            print(f"Seeding slot 0 from {genome_file}  (gen {genome['generation']}, fitness {genome['fitness']:.4f})")
            active_init[0] = clamp_physical_row(
                active_names,
                genome_active_row(genome, args.experiment, active_names).astype(np.float32, copy=False),
                active_bounds,
            ).astype(np.float32, copy=False)

    search_arr = physical_matrix_to_search(active_names, active_init)
    full_physical_arr = resolved_searchable_matrix(args.experiment, active_names, search_matrix_to_physical(active_names, search_arr))
    field = BatchedField(
        B=pop_size,
        N=grid_size,
        device=device,
        params=array_to_params(full_physical_arr, device),
        experiment=args.experiment,
        symmetry_break=args.symmetry_break,
    )

    if seed_genome is not None:
        best_fitness_ever = float(seed_genome.get("fitness", -1.0))
        best_active_ever = clamp_physical_row(
            active_names,
            genome_active_row(seed_genome, args.experiment, active_names),
            active_bounds,
        ).astype(np.float32, copy=False)
        best_gen_ever = int(seed_genome.get("generation", -1))
    else:
        best_fitness_ever = -1.0
        best_active_ever = search_matrix_to_physical(active_names, search_arr)[0].copy()
        best_gen_ever = 0

    mutation_strength = 1.0
    for gen in range(gens):
        t0 = time.perf_counter()
        fitness_acc = np.zeros(pop_size, dtype=np.float32)
        episode_seeds = []
        slot_ids = np.full(pop_size, CANONICAL_EVAL_SLOT, dtype=np.int64)
        active_physical_arr = search_matrix_to_physical(active_names, search_arr)
        full_physical_arr = resolved_searchable_matrix(args.experiment, active_names, active_physical_arr)
        for _ in range(episodes):
            episode_seed = int(np.random.randint(0, 2**31 - 1))
            episode_seeds.append(episode_seed)
            field.params = array_to_params(full_physical_arr, device)
            fitness_acc += field.run_episode(base_seed=episode_seed, slot_ids=slot_ids).cpu().numpy()
        fitness = fitness_acc / episodes
        metrics = field.last_episode_metrics
        elapsed = time.perf_counter() - t0

        print_generation(
            gen,
            gens,
            fitness,
            active_physical_arr,
            elapsed,
            metrics,
            experiment=args.experiment,
            active_names=active_names,
            search_bounds=search_bounds,
        )

        best_idx = int(np.argmax(fitness))
        if fitness[best_idx] > best_fitness_ever:
            best_fitness_ever = float(fitness[best_idx])
            best_active_ever = active_physical_arr[best_idx].copy()
            best_gen_ever = gen
            resolved_best = resolve_runtime_params(
                args.experiment,
                active_values={name: float(best_active_ever[i]) for i, name in enumerate(active_names)},
            )
            save_genome(
                genome_file,
                experiment=args.experiment,
                symmetry_break=args.symmetry_break,
                generation=gen,
                fitness=best_fitness_ever,
                resolved_params=resolved_best,
                eval_episode_seeds=episode_seeds,
                eval_slot=CANONICAL_EVAL_SLOT,
            )
            print(f"  ** New best saved -> {genome_file}")

        mutation_strength = max(0.2, 1.0 - (gen / gens) * 0.7)
        search_arr = evolve_population(search_arr, fitness, active_names, search_bounds, mutation_strength=mutation_strength)

    print(f"\n{'=' * 60}")
    print(f"Search complete.  Best fitness: {best_fitness_ever:.4f}  (generation {best_gen_ever + 1})")
    resolved_best = resolve_runtime_params(
        args.experiment,
        active_values={name: float(best_active_ever[i]) for i, name in enumerate(active_names)},
    )
    active_lines, frozen_lines = parameter_summary_lines(args.experiment, resolved_best)
    print("Best active parameters:")
    for name, value in active_lines:
        print(f"  {name:>15s} = {value:.6f}")
    print("Frozen searchable parameters:")
    for name, value in frozen_lines:
        print(f"  {name:>15s} = {value:.6f}")
    print(f"\nSaved to {genome_file}")
    viz_cmd = f"python run.py --device {device} --experiment {args.experiment}"
    if args.symmetry_break is not None:
        viz_cmd += f" --symmetry-break {args.symmetry_break}"
    viz_cmd += f" --load_genome {genome_file}"
    print("\nTo visualise the best individual:")
    print(f"  {viz_cmd}")


if __name__ == "__main__":
    main()
