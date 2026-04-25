"""
evolve_cmaes.py — CMA-ES search over Field Dynamics parameters.

AUTO-RESUME: if the experiment-specific CMA-ES state file exists beside this
script, the run continues from exactly where it left off — same covariance
matrix, same sigma, same iteration count. Run as many times as you like; it
always appends history for that experiment/symmetry-break pair.

Use --fresh to discard the saved state and start over.

Geometry readout is printed at the end of every run.
Add --plot for a matplotlib figure (covariance heatmap, eigenvalue spectrum,
fitness history).

Requires:  pip install cma matplotlib

From the repo root:
    python python/evolve_cmaes.py
        # auto-resume or start fresh for symmetry_v1/spatial
    python python/evolve_cmaes.py --gens 20
        # run 20 more iterations for the current experiment state
    python python/evolve_cmaes.py --fresh --seed_default
        # restart and initialize the mean at the default parameter set
    python python/evolve_cmaes.py --experiment replay --fresh
        # start a separate replay-mode CMA-ES run
    python python/evolve_cmaes.py --plot
        # show geometry and history figures after the run
    python python/evolve_cmaes.py --fresh --B 32 --sigma0 0.2
        # change popsize or sigma0 when starting a new CMA-ES state
    python python/evolve_cmaes.py --reset
        # delete best_genome.json before running (separate from --fresh)

State files written:
    cmaes_state.<suffix>.pkl   full CMA-ES object (pickled)
    cmaes_history.<suffix>.json
        fitness + sigma per iteration (appended)
    best_genome.json
        best params found so far (not written in replay mode)
"""

import argparse
import json
import os
import pickle
import time
from pathlib import Path
import numpy as np
import torch

try:
    import cma
except ImportError:
    raise SystemExit("cma not installed.  Run:  pip install cma")

from batched_field import (
    BatchedField, PARAM_NAMES, PARAM_BOUNDS, PARAM_DEFAULTS,
    array_to_params,
)
from experiment_paths import (
    SUPPORTED_EXPERIMENTS,
    SUPPORTED_SYMMETRY_BREAKS,
    default_cmaes_history_path,
    default_cmaes_state_path,
    default_genome_path,
)
from search_space import (
    clamp_physical_row,
    physical_to_search_value,
    search_to_physical_value,
    transform_bounds,
)

P = len(PARAM_NAMES)

BASE_DIR = Path(__file__).resolve().parent
SEARCH_BOUNDS = transform_bounds(PARAM_NAMES, PARAM_BOUNDS)
CANONICAL_EVAL_SLOT = 0
MIN_EARLY_STOP_ITERS = 8
DEFERRED_STOP_REASONS = {"tolfun", "tolflatfitness"}


# ── parameter space ↔ unit cube ───────────────────────────────────────────────

def to_unit(row: np.ndarray) -> np.ndarray:
    out = np.empty(P, dtype=np.float64)
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = SEARCH_BOUNDS[name]
        search_val = physical_to_search_value(name, float(row[i]))
        out[i] = (search_val - lo) / (hi - lo)
    return out


def from_unit(row) -> np.ndarray:
    out = np.empty(P, dtype=np.float64)
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = SEARCH_BOUNDS[name]
        search_val = float(np.clip(row[i] * (hi - lo) + lo, lo, hi))
        out[i] = search_to_physical_value(name, search_val)
    return out


def batch_from_unit(X) -> np.ndarray:
    return np.array([from_unit(x) for x in X], dtype=np.float64)


def find_unit_bound_violations(row, physical_row: np.ndarray | None = None) -> list[str]:
    row = np.asarray(row, dtype=np.float64)
    physical_row = None if physical_row is None else np.asarray(physical_row, dtype=np.float64)
    issues = []
    for i, name in enumerate(PARAM_NAMES):
        unit_val = float(row[i])
        if np.isfinite(unit_val) and 0.0 <= unit_val <= 1.0:
            continue
        search_lo, search_hi = SEARCH_BOUNDS[name]
        physical_lo, physical_hi = PARAM_BOUNDS[name]
        parts = [
            f"{name}: unit={unit_val:.12g}",
            "expected in [0, 1]",
            f"search_bounds=[{search_lo:.12g}, {search_hi:.12g}]",
            f"physical_bounds=[{physical_lo:.12g}, {physical_hi:.12g}]",
        ]
        if physical_row is not None:
            physical_val = float(physical_row[i])
            search_val = physical_to_search_value(name, physical_val)
            parts.insert(1, f"physical={physical_val:.12g}")
            parts.insert(2, f"search={search_val:.12g}")
        issues.append("  " + "  ".join(parts))
    return issues


def validate_unit_seed(row, physical_row: np.ndarray | None = None, source: str = "initial mean"):
    issues = find_unit_bound_violations(row, physical_row=physical_row)
    if issues:
        raise SystemExit(f"{source} is out of CMA-ES bounds:\n" + "\n".join(issues))


def active_stop_reasons(stop_dict: dict, gen: int, best_fitness: float) -> dict:
    """Defer flat-objective stops until CMA-ES has had a few chances to explore."""
    if not stop_dict:
        return {}
    filtered = dict(stop_dict)
    if gen < MIN_EARLY_STOP_ITERS or best_fitness <= 0.0:
        for key in DEFERRED_STOP_REASONS:
            filtered.pop(key, None)
    return filtered


# ── genome I/O ────────────────────────────────────────────────────────────────

def save_genome(path, params_row, fitness, generation, experiment, symmetry_break,
                eval_episode_seeds: list[int] | None = None, eval_slot: int | None = None):
    genome = {
        "generation": generation,
        "fitness":    float(fitness),
        "experiment": experiment,
        "symmetry_break": symmetry_break,
        "params":     {n: float(params_row[i]) for i, n in enumerate(PARAM_NAMES)},
    }
    if eval_episode_seeds is not None:
        genome["eval_episode_seeds"] = [int(s) for s in eval_episode_seeds]
    if eval_slot is not None:
        genome["eval_slot"] = int(eval_slot)
    with open(path, "w") as f:
        json.dump(genome, f, indent=2)


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


def load_genome(path):
    with open(path) as f:
        return json.load(f)


def genome_param(genome: dict, name: str) -> float:
    return float(genome["params"].get(name, PARAM_DEFAULTS[name]))


def genome_matches_run(genome: dict, experiment: str, symmetry_break: str | None) -> bool:
    genome_experiment = genome.get("experiment", "replay")
    genome_break = genome.get("symmetry_break", None if genome_experiment == "replay" else "spatial")
    target_break = None if experiment == "replay" else symmetry_break
    return genome_experiment == experiment and genome_break == target_break


# ── history (appended across runs) ───────────────────────────────────────────

def load_history(history_file: Path):
    if history_file.exists():
        with open(history_file) as f:
            return json.load(f)
    return []


def append_history(history_file: Path, history, entry):
    history.append(entry)
    with open(history_file, "w") as f:
        json.dump(history, f, indent=1)


# ── state persistence ─────────────────────────────────────────────────────────

def save_state(state_file: Path, es, meta):
    with open(state_file, "wb") as f:
        pickle.dump({"es": es, "meta": meta}, f)


def load_state(state_file: Path):
    with open(state_file, "rb") as f:
        return pickle.load(f)


# ── display ───────────────────────────────────────────────────────────────────

def _bar(v, width=20):
    filled = int(round(max(0.0, min(1.0, float(v))) * width))
    return "#" * filled + "-" * (width - filled)


def print_iteration(gen, fitness, arr, elapsed, sigma, metrics=None):
    best_idx = int(np.argmax(fitness))
    best_f   = fitness[best_idx]
    mean_f   = float(fitness.mean())
    best_p   = arr[best_idx]
    print(f"\n=== Iteration {gen}  ({elapsed:.1f}s)  sigma={sigma:.4f} ===")
    print(f"  fitness  best={best_f:.4f}  mean={mean_f:.4f}  [{_bar(min(best_f,1.0))}]")
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
                  f"  eff = {_fmt(metrics.get('efficiency_reward'))}")
            cue_seq = metrics.get("cue_sequence", "--")
            print(f"        cueSeq = {cue_seq}")
        else:
            print(f"           corr = {_fmt(metrics.get('corr'))}"
                  f"  retention = {_fmt(metrics.get('retention'))}"
                  f"  faithful = {_fmt(metrics.get('frequency_faithfulness'))}"
                  f"  eff = {_fmt(metrics.get('efficiency_reward'))}")
            print(f"         dayT = {_fmt(metrics.get('day_period'))}"
                  f"  nightT = {_fmt(metrics.get('night_period'))}"
                  f"  ratio = {_fmt(metrics.get('period_ratio'))}")
    print("  best params:")
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = SEARCH_BOUNDS[name]
        search_val = physical_to_search_value(name, float(best_p[i]))
        normed = (search_val - lo) / (hi - lo)
        print(f"    {name:>15s} = {best_p[i]:.5f}  [{_bar(normed, 15)}]")


# ── geometry ──────────────────────────────────────────────────────────────────

def get_covariance(es):
    """Return the normalised covariance matrix C from the CMA-ES object."""
    # cma stores it on es.sm.C; fall back to reconstructing from B and D
    try:
        return np.array(es.sm.C)
    except AttributeError:
        pass
    try:
        B = np.array(es.B); D = np.array(es.D)
        return (B * D**2) @ B.T
    except AttributeError:
        return None


def print_geometry(es, sigma):
    C = get_covariance(es)
    if C is None:
        print("  (covariance not accessible on this cma version)")
        return

    vals, vecs = np.linalg.eigh(C)       # ascending order
    vals = vals[::-1]; vecs = vecs[:, ::-1]   # descending

    cond   = vals[0] / max(vals[-1], 1e-12)
    # participation ratio: how many effective dimensions
    eff_d  = (vals.sum()**2) / max((vals**2).sum(), 1e-12)
    # per-parameter 1-sigma uncertainty in normalised space
    sensitivity = sigma * np.sqrt(np.diag(C))

    print(f"\n{'─'*58}")
    print(f"  Geometry of fitness landscape (normalised parameter space)")
    print(f"{'─'*58}")
    print(f"  Step size σ          = {sigma:.5f}")
    print(f"  Condition number     = {cond:.1f}  "
          f"({'sharp ridge' if cond > 20 else 'moderate ridge' if cond > 5 else 'round bowl'})")
    print(f"  Effective dimensions = {eff_d:.1f} / {P}")

    print(f"\n  Eigenvalue spectrum  (large = flat/insensitive, small = sharp/critical)")
    for k in range(P):
        # Top-3 loading parameters on this axis
        loading = sorted(zip(np.abs(vecs[:, k]), PARAM_NAMES), reverse=True)
        top = "  ".join(
            f"{nm}({'+'if vecs[PARAM_NAMES.index(nm),k]>=0 else '-'}{abs(vecs[PARAM_NAMES.index(nm),k]):.2f})"
            for _, nm in loading[:3]
        )
        rel = vals[k] / vals[0]
        print(f"    PC{k+1}  {vals[k]:.4f}  [{_bar(rel, 18)}]  {top}")

    print(f"\n  Per-parameter uncertainty  (σ × √C_ii, in normalised space)")
    order = np.argsort(sensitivity)
    for i in order:
        name = PARAM_NAMES[i]
        lo, hi = PARAM_BOUNDS[name]
        abs_uncertainty = sensitivity[i] * (hi - lo)
        label = "constrained" if sensitivity[i] < 0.05 else \
                "moderate"    if sensitivity[i] < 0.15 else "free"
        print(f"    {name:>15s}  ±{abs_uncertainty:.5f}  ({label})")

    print(f"{'─'*58}")


def plot_geometry(es, sigma, history):
    try:
        import matplotlib.pyplot as plt
        import matplotlib.gridspec as gridspec
    except ImportError:
        print("matplotlib not available — skipping plot")
        return

    C = get_covariance(es)
    vals, vecs = np.linalg.eigh(C)
    vals = vals[::-1]; vecs = vecs[:, ::-1]

    fig = plt.figure(figsize=(14, 9), facecolor="#0d0d14")
    gs  = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.38,
                            left=0.07, right=0.97, top=0.92, bottom=0.08)

    kw = dict(facecolor="#0d0d14")
    ax_cov  = fig.add_subplot(gs[0, 0], **kw)
    ax_vec  = fig.add_subplot(gs[0, 1], **kw)
    ax_eig  = fig.add_subplot(gs[0, 2], **kw)
    ax_fit  = fig.add_subplot(gs[1, :2], **kw)
    ax_sig  = fig.add_subplot(gs[1, 2], **kw)

    tc = "#aaa"
    for ax in (ax_cov, ax_vec, ax_eig, ax_fit, ax_sig):
        ax.tick_params(colors="#666", labelsize=7)
        ax.title.set_color(tc)
        for sp in ax.spines.values(): sp.set_edgecolor("#333")

    labels = [n[:6] for n in PARAM_NAMES]

    # Covariance heatmap
    im = ax_cov.imshow(C, cmap="RdBu_r", vmin=-np.abs(C).max(), vmax=np.abs(C).max(),
                        aspect="auto")
    ax_cov.set_xticks(range(P)); ax_cov.set_xticklabels(labels, rotation=45, ha="right", fontsize=6)
    ax_cov.set_yticks(range(P)); ax_cov.set_yticklabels(labels, fontsize=6)
    ax_cov.set_title("Covariance C")
    plt.colorbar(im, ax=ax_cov, fraction=0.046)

    # Eigenvector heatmap  (rows=params, cols=PCs)
    vmax = np.abs(vecs).max()
    im2 = ax_vec.imshow(vecs, cmap="RdBu_r", vmin=-vmax, vmax=vmax, aspect="auto")
    ax_vec.set_xticks(range(P)); ax_vec.set_xticklabels([f"PC{k+1}" for k in range(P)],
                                                          rotation=45, fontsize=6)
    ax_vec.set_yticks(range(P)); ax_vec.set_yticklabels(labels, fontsize=6)
    ax_vec.set_title("Eigenvectors  (rows=params, cols=PCs)")
    plt.colorbar(im2, ax=ax_vec, fraction=0.046)

    # Eigenvalue spectrum
    ax_eig.barh(range(P)[::-1], vals, color="#4fc3f7", alpha=0.8)
    ax_eig.set_yticks(range(P)); ax_eig.set_yticklabels([f"PC{k+1}" for k in range(1, P+1)],
                                                          fontsize=7)
    ax_eig.set_xlabel("eigenvalue", color="#888", fontsize=7)
    ax_eig.set_title("Eigenvalue spectrum")
    ax_eig.axvline(0, color="#444")

    # Fitness history
    if history:
        gens      = [h["gen"]          for h in history]
        bests     = [h["best_fitness"] for h in history]
        means     = [h["mean_fitness"] for h in history]
        ax_fit.plot(gens, bests, color="#81c784", lw=1.2, label="best")
        ax_fit.plot(gens, means, color="#4fc3f7", lw=0.8, alpha=0.7, label="mean")
        ax_fit.set_xlabel("iteration", color="#888", fontsize=7)
        ax_fit.set_title("Fitness history")
        ax_fit.legend(fontsize=7, labelcolor="#aaa",
                      facecolor="#0d0d14", edgecolor="#333")
        ax_fit.axhline(0, color="#333", lw=0.5)

    # Sigma history
    if history and "sigma" in history[0]:
        sigmas = [h["sigma"] for h in history]
        ax_sig.plot(gens, sigmas, color="#ffb74d", lw=1.0)
        ax_sig.set_xlabel("iteration", color="#888", fontsize=7)
        ax_sig.set_title("Step size σ  (should shrink as it converges)")
        ax_sig.axhline(0, color="#333", lw=0.5)

    fig.suptitle("CMA-ES Landscape Geometry", color="#ccc", fontsize=10)
    plt.show()


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--B",       type=int,   default=16)
    p.add_argument("--N",       type=int,   default=32)
    p.add_argument("--gens",    type=int,   default=20,
                   help="Iterations to run this session (default 20, appended to previous)")
    p.add_argument("--sigma0",  type=float, default=0.3)
    p.add_argument("--device",  default="auto")
    p.add_argument("--experiment", choices=SUPPORTED_EXPERIMENTS, default="symmetry_v1")
    p.add_argument("--symmetry-break", choices=SUPPORTED_SYMMETRY_BREAKS, default="spatial")
    p.add_argument("--episodes", type=int,  default=1)
    p.add_argument("--seed", type=int, default=None,
                   help="Random seed for reproducible search and saved-genome replay")
    p.add_argument("--fresh",   action="store_true",
                   help="Discard saved state and start over")
    p.add_argument("--seed_default", action="store_true",
                   help="(fresh only) start mean at v7 default parameters")
    p.add_argument("--plot",    action="store_true",
                   help="Show geometry + history figure after run")
    p.add_argument("--reset",   action="store_true",
                   help="Delete best_genome.json and start from scratch (separate from --fresh)")
    return p.parse_args()


def pick_device(requested):
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


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    args   = parse_args()
    if args.seed is not None:
        np.random.seed(args.seed)
        torch.manual_seed(args.seed)
    device = pick_device(args.device)
    state_file = default_cmaes_state_path(BASE_DIR, args.experiment, args.symmetry_break)
    history_file = default_cmaes_history_path(BASE_DIR, args.experiment, args.symmetry_break)
    genome_file = default_genome_path(BASE_DIR)
    save_genome_enabled = args.experiment != "replay"
    if args.reset and genome_file.exists():
        genome_file.unlink()
        print(f"Reset: deleted {genome_file}")
    if save_genome_enabled:
        ensure_genome_file(genome_file, args.experiment, args.symmetry_break)

    history = load_history(history_file)

    # ── load or create CMA-ES state ──────────────────────────────────────────
    if not args.fresh and state_file.exists():
        saved = load_state(state_file)
        es    = saved["es"]
        meta  = saved["meta"]
        B     = meta["B"]; N = meta["N"]
        meta_experiment = meta.get("experiment", "replay")
        meta_break = meta.get("symmetry_break", None if meta_experiment == "replay" else "spatial")
        target_break = None if args.experiment == "replay" else args.symmetry_break
        if meta_experiment != args.experiment or meta_break != target_break:
            print(f"Warning: resuming CMA-ES state from {meta_experiment}:{meta_break} "
                  f"into {args.experiment}:{target_break}. Use --fresh to start clean.")
        print(f"Resuming from {state_file}  "
              f"(iteration {meta['gen']}, best fitness {meta['best_fitness']:.4f})")
    else:
        if not args.fresh and not state_file.exists():
            print("No saved CMA-ES state found — starting a new CMA-ES run.")
        else:
            print("--fresh: discarding saved state.")

        B = args.B; N = args.N
        seeded_from_genome = False
        genome = None
        x0_physical = None
        clamped_default_row = clamp_physical_row(
            PARAM_NAMES,
            np.array([PARAM_DEFAULTS[name] for name in PARAM_NAMES], dtype=np.float64),
            PARAM_BOUNDS,
        )

        if save_genome_enabled and genome_file.exists():
            genome = load_genome(genome_file)
            if genome_matches_run(genome, args.experiment, args.symmetry_break):
                if args.seed_default:
                    print("Existing best_genome.json found, but --seed_default overrides it for the initial mean.")
                else:
                    x0_physical = clamp_physical_row(
                        PARAM_NAMES,
                        np.array([genome_param(genome, n) for n in PARAM_NAMES], dtype=np.float64),
                        PARAM_BOUNDS,
                    )
                    x0 = to_unit(x0_physical)
                    seeded_from_genome = True
                    print(f"Starting mean from {genome_file}  "
                          f"(gen {genome['generation']}, fitness {genome['fitness']:.4f})")
            else:
                print(f"Ignoring {genome_file} because it targets "
                      f"{genome.get('experiment')}:{genome.get('symmetry_break')} "
                      f"instead of {args.experiment}:{args.symmetry_break}.")

        if args.seed_default:
            x0_physical = clamped_default_row.copy()
            x0 = to_unit(x0_physical)
            print("Starting mean at search-clamped default parameters.")
        elif not seeded_from_genome:
            x0 = [0.5] * P
            x0_physical = None

        validate_unit_seed(x0, physical_row=x0_physical, source="Initial CMA-ES mean")

        es = cma.CMAEvolutionStrategy(
            x0, args.sigma0,
            {"popsize": B, "bounds": [[0.0]*P, [1.0]*P], "verbose": -9},
        )
        initial_best_fitness = -1.0
        initial_best_params = clamped_default_row.tolist()
        if genome is not None and genome_matches_run(genome, args.experiment, args.symmetry_break):
            initial_best_fitness = float(genome.get("fitness", -1.0))
            initial_best_params = clamp_physical_row(
                PARAM_NAMES,
                np.array([genome_param(genome, n) for n in PARAM_NAMES], dtype=np.float64),
                PARAM_BOUNDS,
            ).tolist()
        meta = {
            "B": B, "N": N, "gen": 0,
            "best_fitness": initial_best_fitness,
            "best_params":  initial_best_params,
            "experiment": args.experiment,
            "symmetry_break": None if args.experiment == "replay" else args.symmetry_break,
        }

    print(f"\nField Dynamics — CMA-ES  "
          f"popsize={B}  grid={N}x{N}  running {args.gens} iterations  "
          f"device={device}")
    print(f"  experiment={args.experiment}  symmetry_break={args.symmetry_break}")
    print(f"  state_path={state_file}")
    print(f"  history_path={history_file}")
    if save_genome_enabled:
        print(f"  genome_path={genome_file}")
    else:
        print(f"  genome_path=none (replay mode — not saving)")
    print()

    field = BatchedField(
        B=B,
        N=N,
        device=device,
        experiment=args.experiment,
        symmetry_break=args.symmetry_break,
    )

    for _ in range(args.gens):
        stop_reasons = active_stop_reasons(es.stop(), meta["gen"], float(meta["best_fitness"]))
        if stop_reasons:
            print("CMA-ES convergence criterion met — stopping early.")
            print(f"  Reason: {stop_reasons}")
            break

        t0  = time.perf_counter()
        X   = es.ask()
        arr = batch_from_unit(X)

        fitness_acc = np.zeros(B, dtype=np.float32)
        episode_seeds = []
        # CMA-ES also needs a shared evaluation seed within each episode;
        # otherwise the optimizer learns slot-specific reset luck.
        slot_ids = np.full(B, CANONICAL_EVAL_SLOT, dtype=np.int64)
        for _ in range(args.episodes):
            episode_seed = int(np.random.randint(0, 2**31 - 1))
            episode_seeds.append(episode_seed)
            field.params = array_to_params(arr, device)
            fitness_acc += field.run_episode(base_seed=episode_seed, slot_ids=slot_ids).cpu().numpy()
        fitness = fitness_acc / args.episodes
        metrics = field.last_episode_metrics

        es.tell(X, (-fitness).tolist())

        elapsed  = time.perf_counter() - t0
        meta["gen"] += 1
        gen = meta["gen"]

        print_iteration(gen, fitness, arr, elapsed, es.sigma, metrics=metrics)

        best_idx = int(np.argmax(fitness))
        best_f   = float(fitness[best_idx])

        append_history(history_file, history, {
            "gen":          gen,
            "best_fitness": best_f,
            "mean_fitness": float(fitness.mean()),
            "sigma":        float(es.sigma),
        })

        if best_f > meta["best_fitness"]:
            meta["best_fitness"] = best_f
            meta["best_params"]  = arr[best_idx].tolist()
            if save_genome_enabled:
                save_genome(
                    genome_file,
                    arr[best_idx],
                    best_f,
                    gen,
                    experiment=args.experiment,
                    symmetry_break=args.symmetry_break,
                    eval_episode_seeds=episode_seeds,
                    eval_slot=CANONICAL_EVAL_SLOT,
                )
                print(f"  ** New best → {genome_file}")

        save_state(state_file, es, meta)

    # ── geometry readout ─────────────────────────────────────────────────────
    print_geometry(es, es.sigma)

    print(f"\nTotal iterations so far: {meta['gen']}")
    print(f"Best fitness:            {meta['best_fitness']:.4f}")
    print(f"\nTo visualise best individual:")
    print(
        f"  python run.py --device {device} --experiment {args.experiment}"
        f" --symmetry-break {args.symmetry_break} --load_genome {genome_file}"
    )
    print(f"To continue search:")
    print(
        f"  python evolve_cmaes.py --experiment {args.experiment}"
        f" --symmetry-break {args.symmetry_break} --gens {args.gens}"
    )

    if args.plot:
        plot_geometry(es, es.sigma, history)


if __name__ == "__main__":
    main()
