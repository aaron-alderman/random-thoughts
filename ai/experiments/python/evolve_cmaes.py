"""
evolve_cmaes.py - CMA-ES search over experiment-scoped active parameter subsets.
"""

from __future__ import annotations

import argparse
import json
import pickle
import time
from pathlib import Path

import numpy as np
import torch

try:
    import cma
except ImportError:
    raise SystemExit("cma not installed. Run: pip install cma")

from batched_field import BatchedField, array_to_params
from experiment_paths import (
    SUPPORTED_EXPERIMENTS,
    SUPPORTED_SYMMETRY_BREAKS,
    default_cmaes_history_path,
    default_cmaes_state_path,
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
    search_to_physical_value,
    transform_bounds,
)

BASE_DIR = Path(__file__).resolve().parent
CANONICAL_EVAL_SLOT = 0
MIN_EARLY_STOP_ITERS = 8
DEFERRED_STOP_REASONS = {"tolfun", "tolflatfitness"}
ACTIVE_PARAM_NAMES: tuple[str, ...] = ()
ACTIVE_PARAM_BOUNDS: dict[str, tuple[float, float]] = {}
ACTIVE_SEARCH_BOUNDS: dict[str, tuple[float, float]] = {}
ACTIVE_DIMENSIONS = 0


def configure_active_search(experiment: str):
    global ACTIVE_PARAM_NAMES, ACTIVE_PARAM_BOUNDS, ACTIVE_SEARCH_BOUNDS, ACTIVE_DIMENSIONS
    ACTIVE_PARAM_NAMES = active_param_names(experiment)
    ACTIVE_PARAM_BOUNDS = active_param_bounds(experiment)
    ACTIVE_SEARCH_BOUNDS = transform_bounds(ACTIVE_PARAM_NAMES, ACTIVE_PARAM_BOUNDS)
    ACTIVE_DIMENSIONS = len(ACTIVE_PARAM_NAMES)


def to_unit(row: np.ndarray) -> np.ndarray:
    out = np.empty(ACTIVE_DIMENSIONS, dtype=np.float64)
    for i, name in enumerate(ACTIVE_PARAM_NAMES):
        lo, hi = ACTIVE_SEARCH_BOUNDS[name]
        search_val = physical_to_search_value(name, float(row[i]))
        out[i] = (search_val - lo) / (hi - lo)
    return out


def from_unit(row) -> np.ndarray:
    out = np.empty(ACTIVE_DIMENSIONS, dtype=np.float64)
    for i, name in enumerate(ACTIVE_PARAM_NAMES):
        lo, hi = ACTIVE_SEARCH_BOUNDS[name]
        search_val = float(np.clip(row[i] * (hi - lo) + lo, lo, hi))
        out[i] = search_to_physical_value(name, search_val)
    return out


def batch_from_unit(X) -> np.ndarray:
    return np.array([from_unit(x) for x in X], dtype=np.float64)


def validate_unit_seed(row, physical_row: np.ndarray | None = None, source: str = "initial mean"):
    row = np.asarray(row, dtype=np.float64)
    issues = []
    for i, name in enumerate(ACTIVE_PARAM_NAMES):
        unit_val = float(row[i])
        if np.isfinite(unit_val) and 0.0 <= unit_val <= 1.0:
            continue
        search_lo, search_hi = ACTIVE_SEARCH_BOUNDS[name]
        physical_lo, physical_hi = ACTIVE_PARAM_BOUNDS[name]
        parts = [
            f"{name}: unit={unit_val:.12g}",
            "expected in [0, 1]",
            f"search_bounds=[{search_lo:.12g}, {search_hi:.12g}]",
            f"physical_bounds=[{physical_lo:.12g}, {physical_hi:.12g}]",
        ]
        if physical_row is not None:
            parts.insert(1, f"physical={float(physical_row[i]):.12g}")
        issues.append("  " + "  ".join(parts))
    if issues:
        raise SystemExit(f"{source} is out of CMA-ES bounds:\n" + "\n".join(issues))


def active_stop_reasons(stop_dict: dict, gen: int, best_fitness: float) -> dict:
    if not stop_dict:
        return {}
    filtered = dict(stop_dict)
    if gen < MIN_EARLY_STOP_ITERS or best_fitness <= 0.0:
        for key in DEFERRED_STOP_REASONS:
            filtered.pop(key, None)
    return filtered


def load_history(history_file: Path):
    if history_file.exists():
        with open(history_file) as f:
            return json.load(f)
    return []


def append_history(history_file: Path, history, entry):
    history.append(entry)
    history_file.parent.mkdir(parents=True, exist_ok=True)
    with open(history_file, "w") as f:
        json.dump(history, f, indent=1)


def save_state(state_file: Path, es, meta):
    state_file.parent.mkdir(parents=True, exist_ok=True)
    with open(state_file, "wb") as f:
        pickle.dump({"es": es, "meta": meta}, f)


def load_state(state_file: Path):
    with open(state_file, "rb") as f:
        return pickle.load(f)


def _bar(v, width=20):
    filled = int(round(max(0.0, min(1.0, float(v))) * width))
    return "#" * filled + "-" * (width - filled)


def print_iteration(gen, fitness, active_arr, elapsed, sigma, metrics=None, *, experiment: str):
    best_idx = int(np.argmax(fitness))
    best_f = fitness[best_idx]
    mean_f = float(fitness.mean())
    best_active = active_arr[best_idx]
    resolved_best = resolve_runtime_params(
        experiment,
        active_values={name: float(best_active[i]) for i, name in enumerate(ACTIVE_PARAM_NAMES)},
    )
    _, frozen_lines = parameter_summary_lines(experiment, resolved_best)

    print(f"\n=== Iteration {gen}  ({elapsed:.1f}s)  sigma={sigma:.4f} ===")
    print(f"  fitness  best={best_f:.4f}  mean={mean_f:.4f}  [{_bar(min(best_f, 1.0))}]")
    print(f"  active_dims={ACTIVE_DIMENSIONS}")
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
            print(f"        parity = {_fmt(metrics.get('cue_parity'))}  eff = {_fmt(metrics.get('efficiency_reward'))}")
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
    for i, name in enumerate(ACTIVE_PARAM_NAMES):
        lo, hi = ACTIVE_SEARCH_BOUNDS[name]
        search_val = physical_to_search_value(name, float(best_active[i]))
        normed = (search_val - lo) / (hi - lo)
        print(f"    {name:>15s} = {best_active[i]:.5f}  [{_bar(normed, 15)}]")
    print("  frozen searchable params:")
    for name, value in frozen_lines:
        print(f"    {name:>15s} = {value:.5f}")


def get_covariance(es):
    try:
        return np.array(es.sm.C)
    except AttributeError:
        pass
    try:
        B = np.array(es.B)
        D = np.array(es.D)
        return (B * D**2) @ B.T
    except AttributeError:
        return None


def print_geometry(es, sigma):
    C = get_covariance(es)
    if C is None:
        print("  (covariance not accessible on this cma version)")
        return
    vals, vecs = np.linalg.eigh(C)
    vals = vals[::-1]
    vecs = vecs[:, ::-1]
    cond = vals[0] / max(vals[-1], 1e-12)
    eff_d = (vals.sum() ** 2) / max((vals**2).sum(), 1e-12)
    sensitivity = sigma * np.sqrt(np.diag(C))

    print(f"\n{'-' * 58}")
    print("  Geometry of fitness landscape (normalised active parameter space)")
    print(f"{'-' * 58}")
    print(f"  Step size σ          = {sigma:.5f}")
    print(f"  Condition number     = {cond:.1f}")
    print(f"  Effective dimensions = {eff_d:.1f} / {ACTIVE_DIMENSIONS}")
    print("\n  Per-parameter uncertainty")
    order = np.argsort(sensitivity)
    for i in order:
        name = ACTIVE_PARAM_NAMES[i]
        lo, hi = ACTIVE_PARAM_BOUNDS[name]
        abs_uncertainty = sensitivity[i] * (hi - lo)
        print(f"    {name:>15s}  ±{abs_uncertainty:.5f}")
    print(f"{'-' * 58}")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--B", type=int, default=16)
    p.add_argument("--N", type=int, default=32)
    p.add_argument("--gens", type=int, default=20, help="Iterations to run this session")
    p.add_argument("--sigma0", type=float, default=0.3)
    p.add_argument("--device", default="auto")
    p.add_argument("--experiment", choices=SUPPORTED_EXPERIMENTS, default="symmetry_v1")
    p.add_argument("--symmetry-break", choices=SUPPORTED_SYMMETRY_BREAKS, default="spatial")
    p.add_argument("--episodes", type=int, default=1)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--fresh", action="store_true", help="Discard saved state and start over")
    p.add_argument("--seed_default", action="store_true", help="Start mean at experiment defaults")
    p.add_argument("--plot", action="store_true", help="Reserved for future use")
    p.add_argument("--reset", action="store_true", help="Delete the experiment-scoped best genome before running")
    return p.parse_args()


def pick_device(requested):
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
    configure_active_search(args.experiment)
    if args.seed is not None:
        np.random.seed(args.seed)
        torch.manual_seed(args.seed)

    device = pick_device(args.device)
    state_file = default_cmaes_state_path(BASE_DIR, args.experiment, args.symmetry_break)
    history_file = default_cmaes_history_path(BASE_DIR, args.experiment, args.symmetry_break)
    genome_file = default_genome_path(BASE_DIR, args.experiment)
    if args.reset and genome_file.exists():
        genome_file.unlink()
        print(f"Reset: deleted {genome_file}")
    ensure_genome_file(genome_file, args.experiment, args.symmetry_break)
    history = load_history(history_file)

    if not args.fresh and state_file.exists():
        saved = load_state(state_file)
        es = saved["es"]
        meta = saved["meta"]
        pop_size = meta["B"]
        grid_size = meta["N"]
        print(f"Resuming from {state_file}  (iteration {meta['gen']}, best fitness {meta['best_fitness']:.4f})")
    else:
        if args.fresh:
            print("--fresh: discarding saved state.")
        else:
            print("No saved CMA-ES state found - starting a new run.")
        pop_size = args.B
        grid_size = args.N
        genome = None
        x0_physical = None
        default_row = clamp_physical_row(
            ACTIVE_PARAM_NAMES,
            np.array([active_param_defaults(args.experiment)[name] for name in ACTIVE_PARAM_NAMES], dtype=np.float64),
            ACTIVE_PARAM_BOUNDS,
        )
        if genome_file.exists():
            genome = load_genome(genome_file)
            if genome_matches_run(genome, args.experiment, args.symmetry_break) and not args.seed_default:
                x0_physical = clamp_physical_row(
                    ACTIVE_PARAM_NAMES,
                    genome_active_row(genome, args.experiment, ACTIVE_PARAM_NAMES),
                    ACTIVE_PARAM_BOUNDS,
                )
                print(f"Starting mean from {genome_file}  (gen {genome['generation']}, fitness {genome['fitness']:.4f})")
        if args.seed_default:
            x0_physical = default_row.copy()
            print("Starting mean at experiment default active parameters.")
        x0 = [0.5] * ACTIVE_DIMENSIONS if x0_physical is None else to_unit(x0_physical)
        validate_unit_seed(x0, physical_row=x0_physical, source="Initial CMA-ES mean")
        es = cma.CMAEvolutionStrategy(
            x0,
            args.sigma0,
            {"popsize": pop_size, "bounds": [[0.0] * ACTIVE_DIMENSIONS, [1.0] * ACTIVE_DIMENSIONS], "verbose": -9},
        )
        matched_seed_genome = genome if genome is not None and genome_matches_run(genome, args.experiment, args.symmetry_break) else None
        initial_best_fitness = float(matched_seed_genome.get("fitness", -1.0)) if matched_seed_genome is not None else -1.0
        initial_best_params = (
            clamp_physical_row(ACTIVE_PARAM_NAMES, genome_active_row(matched_seed_genome, args.experiment, ACTIVE_PARAM_NAMES), ACTIVE_PARAM_BOUNDS).tolist()
            if matched_seed_genome is not None
            else default_row.tolist()
        )
        meta = {
            "B": pop_size,
            "N": grid_size,
            "gen": 0,
            "best_fitness": initial_best_fitness,
            "best_params": initial_best_params,
            "experiment": args.experiment,
            "symmetry_break": args.symmetry_break,
        }

    print(f"\nField Dynamics - CMA-ES  popsize={pop_size}  grid={grid_size}x{grid_size}  running {args.gens} iterations  device={device}")
    print(f"  experiment={args.experiment}  symmetry_break={args.symmetry_break}  active_dims={experiment_dimension_count(args.experiment)}")
    print(f"  state_path={state_file}")
    print(f"  history_path={history_file}")
    print(f"  genome_path={genome_file}")
    print()

    field = BatchedField(
        B=pop_size,
        N=grid_size,
        device=device,
        experiment=args.experiment,
        symmetry_break=args.symmetry_break,
    )

    for _ in range(args.gens):
        stop_reasons = active_stop_reasons(es.stop(), meta["gen"], float(meta["best_fitness"]))
        if stop_reasons:
            print("CMA-ES convergence criterion met - stopping early.")
            print(f"  Reason: {stop_reasons}")
            break

        t0 = time.perf_counter()
        X = es.ask()
        active_arr = batch_from_unit(X)
        full_arr = resolved_searchable_matrix(args.experiment, ACTIVE_PARAM_NAMES, active_arr)

        fitness_acc = np.zeros(pop_size, dtype=np.float32)
        episode_seeds = []
        slot_ids = np.full(pop_size, CANONICAL_EVAL_SLOT, dtype=np.int64)
        for _ in range(args.episodes):
            episode_seed = int(np.random.randint(0, 2**31 - 1))
            episode_seeds.append(episode_seed)
            field.params = array_to_params(full_arr, device)
            fitness_acc += field.run_episode(base_seed=episode_seed, slot_ids=slot_ids).cpu().numpy()
        fitness = fitness_acc / args.episodes
        metrics = field.last_episode_metrics

        es.tell(X, (-fitness).tolist())
        elapsed = time.perf_counter() - t0
        meta["gen"] += 1
        gen = meta["gen"]

        print_iteration(gen, fitness, active_arr, elapsed, es.sigma, metrics=metrics, experiment=args.experiment)

        best_idx = int(np.argmax(fitness))
        best_f = float(fitness[best_idx])
        append_history(
            history_file,
            history,
            {"gen": gen, "best_fitness": best_f, "mean_fitness": float(fitness.mean()), "sigma": float(es.sigma)},
        )

        if best_f > meta["best_fitness"]:
            meta["best_fitness"] = best_f
            meta["best_params"] = active_arr[best_idx].tolist()
            resolved_best = resolve_runtime_params(
                args.experiment,
                active_values={name: float(active_arr[best_idx][i]) for i, name in enumerate(ACTIVE_PARAM_NAMES)},
            )
            save_genome(
                genome_file,
                experiment=args.experiment,
                symmetry_break=args.symmetry_break,
                generation=gen,
                fitness=best_f,
                resolved_params=resolved_best,
                eval_episode_seeds=episode_seeds,
                eval_slot=CANONICAL_EVAL_SLOT,
            )
            print(f"  ** New best -> {genome_file}")

        save_state(state_file, es, meta)

    print_geometry(es, es.sigma)
    print(f"\nTotal iterations so far: {meta['gen']}")
    print(f"Best fitness:            {meta['best_fitness']:.4f}")
    viz_cmd = f"python run.py --device {device} --experiment {args.experiment}"
    if args.symmetry_break is not None:
        viz_cmd += f" --symmetry-break {args.symmetry_break}"
    viz_cmd += f" --load_genome {genome_file}"
    print("\nTo visualise best individual:")
    print(f"  {viz_cmd}")
    print("To continue search:")
    cont_cmd = f"python evolve_cmaes.py --experiment {args.experiment} --gens {args.gens}"
    if args.symmetry_break is not None:
        cont_cmd += f" --symmetry-break {args.symmetry_break}"
    print(f"  {cont_cmd}")
    if args.plot:
        print("Plotting is not yet implemented for the active-subset refactor.")


if __name__ == "__main__":
    main()
