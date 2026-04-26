"""
evolve.py — evolutionary search over Field Dynamics parameters.

Strategy: (B/2 + B/2) — keep top half, fill bottom half with mutated offspring.
Crossover: uniform (each parameter drawn from one of two parents at random).
Mutation: Gaussian noise scaled to 15% of each parameter's range, then clamped.

From the repo root:
    python python/evolve.py
        # B=16, N=32, 40 generations, device=auto
    python python/evolve.py --B 32 --gens 80
        # larger population, longer run
    python python/evolve.py --device cpu
        # force CPU instead of auto-selecting CUDA
    python python/evolve.py --resume python/best_genome.json
        # seed slot 0 from a saved genome
    python python/evolve.py --experiment replay --episodes 4
        # replay mode, average fitness over 4 episodes, no genome file saved
    python python/evolve.py --seed_default --reset
        # reset best_genome.json and include the default parameter set in slot 0
"""

import argparse
import json
import math
import time
from pathlib import Path
import numpy as np
import torch

from batched_field import (
    BatchedField, PARAM_NAMES, PARAM_BOUNDS, PARAM_DEFAULTS,
    random_params, default_params, params_to_array, array_to_params
)
from experiment_paths import (
    SUPPORTED_EXPERIMENTS,
    SUPPORTED_SYMMETRY_BREAKS,
    default_genome_path,
)
from search_space import (
    clamp_physical_row,
    physical_to_search_value,
    physical_matrix_to_search,
    search_matrix_to_physical,
    transform_bounds,
)

BASE_DIR = Path(__file__).resolve().parent
SEARCH_BOUNDS = transform_bounds(PARAM_NAMES, PARAM_BOUNDS)
CANONICAL_EVAL_SLOT = 0


# ── GA operators ──────────────────────────────────────────────────────────────

def clamp_params(arr: np.ndarray) -> np.ndarray:
    """Clamp each parameter column to its valid range."""
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = SEARCH_BOUNDS[name]
        arr[:, i] = np.clip(arr[:, i], lo, hi)
    return arr


def mutate(arr: np.ndarray, strength: float = 1.0) -> np.ndarray:
    """Gaussian mutation. strength scales sigma (1.0 = 15% of range)."""
    out = arr.copy()
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = SEARCH_BOUNDS[name]
        sigma = strength * 0.15 * (hi - lo)
        out[:, i] += np.random.randn(len(arr)) * sigma
    return clamp_params(out)


def crossover(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Uniform crossover: each parameter drawn from a or b with equal probability."""
    mask = np.random.rand(*a.shape) < 0.5
    return np.where(mask, a, b)


def evolve_population(arr: np.ndarray, fitness: np.ndarray,
                      mutation_strength: float = 1.0) -> np.ndarray:
    """
    One generation step.
      arr:     (B, P) parameter array
      fitness: (B,)   fitness scores
    Returns new (B, P) array.
    """
    B = len(arr)
    elite_n = B // 2

    # Rank by fitness descending
    ranked = np.argsort(fitness)[::-1]
    elite  = arr[ranked[:elite_n]]   # top half survive

    # Fill bottom half: random pairs from elite, crossover + mutate
    children = []
    while len(children) < B - elite_n:
        i, j = np.random.choice(elite_n, size=2, replace=False)
        child = crossover(elite[i:i+1], elite[j:j+1])
        child = mutate(child, strength=mutation_strength)
        children.append(child[0])

    return np.vstack([elite, np.array(children)])


# ── genome I/O ────────────────────────────────────────────────────────────────

def save_genome(path: str | Path, params_row: np.ndarray, fitness: float, generation: int,
                experiment: str, symmetry_break: str | None,
                eval_episode_seeds: list[int] | None = None, eval_slot: int | None = None):
    genome = {
        "generation": generation,
        "fitness":    float(fitness),
        "experiment": experiment,
        "symmetry_break": symmetry_break,
        "params":     {name: float(params_row[i]) for i, name in enumerate(PARAM_NAMES)},
    }
    if eval_episode_seeds is not None:
        genome["eval_episode_seeds"] = [int(s) for s in eval_episode_seeds]
    if eval_slot is not None:
        genome["eval_slot"] = int(eval_slot)
    with open(path, "w") as f:
        json.dump(genome, f, indent=2)


def load_genome(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def genome_param(genome: dict, name: str) -> float:
    return float(genome["params"].get(name, PARAM_DEFAULTS[name]))


def genome_matches_run(genome: dict, experiment: str, symmetry_break: str | None) -> bool:
    genome_experiment = genome.get("experiment", "replay")
    genome_break = genome.get("symmetry_break", None if genome_experiment in ("replay", "temporal_v1") else "spatial")
    target_break = None if experiment in ("replay", "temporal_v1") else symmetry_break
    return genome_experiment == experiment and genome_break == target_break


def ensure_genome_file(path: Path, experiment: str, symmetry_break: str | None):
    if path.exists():
        return
    params_row = clamp_physical_row(
        PARAM_NAMES,
        np.array([PARAM_DEFAULTS[name] for name in PARAM_NAMES], dtype=np.float32),
        PARAM_BOUNDS,
    ).astype(np.float32, copy=False)
    save_genome(path, params_row, fitness=-1.0, generation=-1,
                experiment=experiment, symmetry_break=symmetry_break)


def resolve_path(path: str | None) -> Path | None:
    if path is None:
        return None
    p = Path(path)
    if p.is_absolute():
        return p
    if p.exists():
        return p.resolve()
    return BASE_DIR / p


# ── display ───────────────────────────────────────────────────────────────────

def _bar(v, width=20):
    filled = int(round(v * width))
    return "#" * filled + "-" * (width - filled)


def print_generation(gen: int, gens: int, fitness: np.ndarray,
                     arr: np.ndarray, elapsed: float, metrics: dict | None = None):
    best_idx = int(np.argmax(fitness))
    best_f   = fitness[best_idx]
    mean_f   = fitness.mean()
    best_p   = arr[best_idx]

    print(f"\n=== Generation {gen+1}/{gens}  ({elapsed:.1f}s) ===")
    print(f"  fitness  best={best_f:.4f}  mean={mean_f:.4f}  "
          f"[{_bar(min(best_f, 1.0))}]")
    if metrics:
        def _fmt(arr_):
            if arr_ is None:
                return "--"
            val = arr_[best_idx]
            return f"{val:.3f}" if np.isfinite(val) else "--"

        print("  best metrics:")
        if "choice_strength" in metrics:
            print(f"         choice = {_fmt(metrics.get('choice_strength'))}"
                  f"  consistent = {_fmt(metrics.get('choice_consistency'))}")
            print(f"        persist = {_fmt(metrics.get('overnight_persistence'))}"
                  f"  switch = {_fmt(metrics.get('switch_penalty'))}")
            print(f"        parity = {_fmt(metrics.get('cue_parity'))}"
                  f"  eff = {_fmt(metrics.get('efficiency_reward'))}"
                  f"  A = {_fmt(metrics.get('a_mean'))}"
                  f"  B = {_fmt(metrics.get('b_mean'))}")
            cue_seq = metrics.get("cue_sequence", "--")
            print(f"        cueSeq = {cue_seq}")
        elif "peak_S_growth_mean" in metrics:
            print(f"          peak = {_fmt(metrics.get('peak_S_growth_mean'))}"
                  f"  grow+ = {_fmt(metrics.get('positive_growth_mean'))}"
                  f"  frac+ = {_fmt(metrics.get('positive_growth_fraction'))}"
                  f"  frac* = {_fmt(metrics.get('positive_growth_fraction_score'))}")
            print(f"        Sfinal = {_fmt(metrics.get('final_S_mass'))}"
                  f"  Sstd = {_fmt(metrics.get('final_S_std'))}"
                  f"  Sstd^ = {_fmt(metrics.get('peak_S_std'))}")
            print(f"           Sf* = {_fmt(metrics.get('final_structure_score'))}"
                  f"  Sp* = {_fmt(metrics.get('peak_structure_score'))}"
                  f"  S* = {_fmt(metrics.get('structure_score'))}")
            print(f"         hold = {_fmt(metrics.get('final_retention_mean'))}"
                  f"  Rslow = {_fmt(metrics.get('final_R_slow_mean'))}")
            print(f"         Cslow = {_fmt(metrics.get('final_C_slow_mean'))}"
                  f"  nS = {_fmt(metrics.get('temporal_structural_samples'))}"
                  f"  eff = {_fmt(metrics.get('efficiency_reward'))}")
        else:
            print(f"           corr = {_fmt(metrics.get('corr'))}"
                  f"  retention = {_fmt(metrics.get('retention'))}"
                  f"  faithful = {_fmt(metrics.get('frequency_faithfulness'))}"
                  f"  eff = {_fmt(metrics.get('efficiency_reward'))}")
            print(f"         dayT = {_fmt(metrics.get('day_period'))}"
                  f"  nightT = {_fmt(metrics.get('night_period'))}"
                  f"  ratio = {_fmt(metrics.get('period_ratio'))}")
    print("  best genome:")
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = SEARCH_BOUNDS[name]
        search_val = physical_to_search_value(name, float(best_p[i]))
        normed = (search_val - lo) / (hi - lo)
        print(f"    {name:>15s} = {best_p[i]:.5f}  [{_bar(normed, 15)}]")


# ── main ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--B",      type=int,   default=16,     help="Population size (default 16)")
    p.add_argument("--N",      type=int,   default=32,     help="Grid size (default 32)")
    p.add_argument("--gens",   type=int,   default=40,     help="Generations (default 40)")
    p.add_argument("--device", default="auto")
    p.add_argument("--experiment", choices=SUPPORTED_EXPERIMENTS, default="symmetry_v1")
    p.add_argument("--symmetry-break", choices=SUPPORTED_SYMMETRY_BREAKS, default="spatial")
    p.add_argument("--resume", default=None,
                   help="Path to best_genome.json to seed the initial population")
    p.add_argument("--episodes", type=int, default=1,
                   help="Episodes per generation for fitness averaging (default 1)")
    p.add_argument("--seed", type=int, default=None,
                   help="Random seed for reproducible search and saved-genome replay")
    p.add_argument("--seed_default", action="store_true",
                   help="Include one copy of the v7 default params in the initial population")
    p.add_argument("--reset", action="store_true",
                   help="Delete best_genome.json and start from scratch")
    return p.parse_args()


def pick_device(requested: str) -> str:
    if requested == "auto":
        if torch.cuda.is_available():
            print(f"GPU: {torch.cuda.get_device_name(0)}")
            return "cuda"
        print("No CUDA GPU — using CPU")
        return "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, falling back to CPU")
        return "cpu"
    return requested


def main():
    args   = parse_args()
    if args.experiment == "temporal_v1":
        args.symmetry_break = None
    if args.seed is not None:
        np.random.seed(args.seed)
        torch.manual_seed(args.seed)
    device = pick_device(args.device)
    B      = args.B
    N      = args.N
    gens   = args.gens
    eps    = args.episodes
    genome_file = default_genome_path(BASE_DIR)
    if args.reset and genome_file.exists():
        genome_file.unlink()
        print(f"Reset: deleted {genome_file}")
    save_genome_enabled = args.experiment != "replay"
    if save_genome_enabled:
        ensure_genome_file(genome_file, args.experiment,
                           None if args.experiment == "replay" else args.symmetry_break)

    print(f"Field Dynamics — Evolutionary Search")
    print(f"  population={B}  grid={N}x{N}  generations={gens}  "
          f"episodes/gen={eps}  device={device}")
    print(f"  experiment={args.experiment}  symmetry_break={args.symmetry_break}")
    if save_genome_enabled:
        print(f"  genome_path={genome_file}")
    else:
        print(f"  genome_path=none (replay mode — not saving)")
    print()

    # ── initial population ────────────────────────────────────────────────────
    physical_init = np.zeros((B, len(PARAM_NAMES)), dtype=np.float32)
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
        physical_init[:, i] = np.random.uniform(lo, hi, B)

    clamped_default_row = clamp_physical_row(
        PARAM_NAMES,
        np.array([PARAM_DEFAULTS[name] for name in PARAM_NAMES], dtype=np.float32),
        PARAM_BOUNDS,
    ).astype(np.float32, copy=False)

    if args.seed_default:
        # Slot 0: defaults clamped into the active search space
        physical_init[0] = clamped_default_row

    seed_genome = None
    if args.resume:
        resume_path = resolve_path(args.resume)
        seed_genome = load_genome(resume_path)
        print(f"Resuming from {resume_path}  (gen {seed_genome['generation']}, "
              f"fitness {seed_genome['fitness']:.4f})")
        seed_row = clamp_physical_row(
            PARAM_NAMES,
            np.array([genome_param(seed_genome, name) for name in PARAM_NAMES], dtype=np.float32),
            PARAM_BOUNDS,
        ).astype(np.float32, copy=False)
        physical_init[0] = seed_row   # seed slot 0 with best known
    elif save_genome_enabled and genome_file.exists():
        genome = load_genome(genome_file)
        if genome_matches_run(genome, args.experiment, args.symmetry_break):
            seed_genome = genome
            print(f"Seeding slot 0 from {genome_file}  (gen {genome['generation']}, "
                  f"fitness {genome['fitness']:.4f})")
            seed_row = clamp_physical_row(
                PARAM_NAMES,
                np.array([genome_param(genome, name) for name in PARAM_NAMES], dtype=np.float32),
                PARAM_BOUNDS,
            ).astype(np.float32, copy=False)
            physical_init[0] = seed_row
        else:
            print(f"Ignoring {genome_file} because it targets "
                  f"{genome.get('experiment')}:{genome.get('symmetry_break')} "
                  f"instead of {args.experiment}:{args.symmetry_break}.")

    arr = physical_matrix_to_search(PARAM_NAMES, physical_init)

    # ── build simulation ──────────────────────────────────────────────────────
    physical_arr = search_matrix_to_physical(PARAM_NAMES, arr)
    params_t = array_to_params(physical_arr, device)
    field    = BatchedField(
        B=B,
        N=N,
        device=device,
        params=params_t,
        experiment=args.experiment,
        symmetry_break=args.symmetry_break,
    )

    if seed_genome is not None:
        best_fitness_ever = float(seed_genome.get("fitness", -1.0))
        best_arr_ever = clamp_physical_row(
            PARAM_NAMES,
            np.array([genome_param(seed_genome, name) for name in PARAM_NAMES], dtype=np.float32),
            PARAM_BOUNDS,
        ).astype(np.float32, copy=False)
        best_gen_ever = int(seed_genome.get("generation", -1))
    else:
        best_fitness_ever = -1.0
        best_arr_ever     = physical_arr[0].copy()
        best_gen_ever     = 0

    mut_strength = 1.0   # annealed slowly

    for gen in range(gens):
        t0 = time.perf_counter()

        # Evaluate fitness — average over multiple episodes if requested
        fitness_acc = np.zeros(B, dtype=np.float32)
        episode_seeds = []
        # Evaluate every candidate on the same deterministic reset for this
        # episode so selection pressure tracks genome quality, not batch slot.
        slot_ids = np.full(B, CANONICAL_EVAL_SLOT, dtype=np.int64)
        for ep in range(eps):
            episode_seed = int(np.random.randint(0, 2**31 - 1))
            episode_seeds.append(episode_seed)
            physical_arr = search_matrix_to_physical(PARAM_NAMES, arr)
            field.params = array_to_params(physical_arr, device)
            f_t = field.run_episode(base_seed=episode_seed, slot_ids=slot_ids)
            fitness_acc += f_t.cpu().numpy()
        fitness = fitness_acc / eps
        metrics = field.last_episode_metrics

        elapsed = time.perf_counter() - t0

        print_generation(gen, gens, fitness, physical_arr, elapsed, metrics=metrics)

        best_idx = int(np.argmax(fitness))
        if fitness[best_idx] > best_fitness_ever:
            best_fitness_ever = fitness[best_idx]
            best_arr_ever     = physical_arr[best_idx].copy()
            best_gen_ever     = gen
            if save_genome_enabled:
                save_genome(
                    genome_file,
                    best_arr_ever,
                    best_fitness_ever,
                    gen,
                    experiment=args.experiment,
                    symmetry_break=args.symmetry_break,
                    eval_episode_seeds=episode_seeds,
                    eval_slot=CANONICAL_EVAL_SLOT,
                )
                print(f"  ** New best saved → {genome_file}")

        # Slow annealing: reduce mutation strength as search converges
        mut_strength = max(0.2, 1.0 - (gen / gens) * 0.7)

        arr = evolve_population(arr, fitness, mutation_strength=mut_strength)

    # ── final report ──────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"Search complete.  Best fitness: {best_fitness_ever:.4f}  "
          f"(generation {best_gen_ever + 1})")
    print("Best parameters:")
    for i, name in enumerate(PARAM_NAMES):
        print(f"  {name:>15s} = {best_arr_ever[i]:.6f}")
    if save_genome_enabled:
        print(f"\nSaved to {genome_file}")
    print(f"\nTo visualise the best individual:")
    viz_cmd = f"python run.py --device {device} --experiment {args.experiment}"
    if args.symmetry_break is not None:
        viz_cmd += f" --symmetry-break {args.symmetry_break}"
    viz_cmd += f" --load_genome {genome_file}"
    print(f"  {viz_cmd}")


if __name__ == "__main__":
    main()
