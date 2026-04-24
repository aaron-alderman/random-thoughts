"""
evolve_cmaes.py — CMA-ES search over Field Dynamics parameters.

AUTO-RESUME: if cmaes_state.pkl exists in the working directory the run
continues from exactly where it left off — same covariance matrix, same sigma,
same iteration count.  Run as many times as you like; it always appends.

Use --fresh to discard the saved state and start over.

Geometry readout is printed at the end of every run.
Add --plot for a matplotlib figure (covariance heatmap, eigenvalue spectrum,
fitness history).

Requires:  pip install cma matplotlib

Usage:
    python evolve_cmaes.py                     # auto-resume or start fresh
    python evolve_cmaes.py --gens 20           # run 20 more iterations
    python evolve_cmaes.py --fresh             # ignore saved state, restart
    python evolve_cmaes.py --fresh --seed_default   # restart at v7 defaults
    python evolve_cmaes.py --plot              # show geometry figure after run
    python evolve_cmaes.py --B 32              # larger population (first run only)

State files written:
    cmaes_state.pkl        full CMA-ES object (pickled)
    cmaes_history.json     fitness + sigma per iteration (appended)
    best_genome_cmaes.json best params found so far
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

P = len(PARAM_NAMES)

BASE_DIR = Path(__file__).resolve().parent
STATE_FILE   = BASE_DIR / "cmaes_state.pkl"
HISTORY_FILE = BASE_DIR / "cmaes_history.json"
GENOME_FILE  = BASE_DIR / "best_genome_cmaes.json"


# ── parameter space ↔ unit cube ───────────────────────────────────────────────

def to_unit(row: np.ndarray) -> np.ndarray:
    out = np.empty(P, dtype=np.float64)
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
        out[i] = (row[i] - lo) / (hi - lo)
    return out


def from_unit(row) -> np.ndarray:
    out = np.empty(P, dtype=np.float32)
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
        out[i] = float(np.clip(row[i] * (hi - lo) + lo, lo, hi))
    return out


def batch_from_unit(X) -> np.ndarray:
    return np.array([from_unit(x) for x in X], dtype=np.float32)


# ── genome I/O ────────────────────────────────────────────────────────────────

def save_genome(path, params_row, fitness, generation):
    with open(path, "w") as f:
        json.dump({
            "generation": generation,
            "fitness":    float(fitness),
            "params":     {n: float(params_row[i]) for i, n in enumerate(PARAM_NAMES)},
        }, f, indent=2)


def ensure_genome_file(path: Path):
    if path.exists():
        return
    params_row = np.array([PARAM_DEFAULTS[name] for name in PARAM_NAMES], dtype=np.float32)
    save_genome(path, params_row, fitness=-1.0, generation=-1)


def load_genome(path):
    with open(path) as f:
        return json.load(f)


# ── history (appended across runs) ───────────────────────────────────────────

def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return []


def append_history(history, entry):
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=1)


# ── state persistence ─────────────────────────────────────────────────────────

def save_state(es, meta):
    with open(STATE_FILE, "wb") as f:
        pickle.dump({"es": es, "meta": meta}, f)


def load_state():
    with open(STATE_FILE, "rb") as f:
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
        corr = metrics.get("corr")
        retention = metrics.get("retention")
        faith = metrics.get("frequency_faithfulness")
        day_p = metrics.get("day_period")
        night_p = metrics.get("night_period")
        ratio = metrics.get("period_ratio")

        def _fmt(arr_):
            if arr_ is None:
                return "--"
            val = arr_[best_idx]
            return f"{val:.3f}" if np.isfinite(val) else "--"

        print("  best metrics:")
        print(f"           corr = {_fmt(corr)}"
              f"  retention = {_fmt(retention)}"
              f"  faithful = {_fmt(faith)}")
        print(f"         dayT = {_fmt(day_p)}"
              f"  nightT = {_fmt(night_p)}"
              f"  ratio = {_fmt(ratio)}")
    print("  best params:")
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
        normed = (best_p[i] - lo) / (hi - lo)
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
    p.add_argument("--episodes", type=int,  default=1)
    p.add_argument("--fresh",   action="store_true",
                   help="Discard saved state and start over")
    p.add_argument("--seed_default", action="store_true",
                   help="(fresh only) start mean at v7 default parameters")
    p.add_argument("--plot",    action="store_true",
                   help="Show geometry + history figure after run")
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
    device = pick_device(args.device)
    ensure_genome_file(GENOME_FILE)

    history = load_history()

    # ── load or create CMA-ES state ──────────────────────────────────────────
    if not args.fresh and STATE_FILE.exists():
        saved = load_state()
        es    = saved["es"]
        meta  = saved["meta"]
        B     = meta["B"]; N = meta["N"]
        print(f"Resuming from {STATE_FILE}  "
              f"(iteration {meta['gen']}, best fitness {meta['best_fitness']:.4f})")
    else:
        if not args.fresh and not STATE_FILE.exists():
            print("No saved state found — starting fresh.")
        else:
            print("--fresh: discarding saved state.")

        B = args.B; N = args.N

        if args.seed_default:
            x0 = to_unit(np.array([PARAM_DEFAULTS[n] for n in PARAM_NAMES],
                                   dtype=np.float64))
            print("Starting mean at v7 default parameters.")
        else:
            x0 = [0.5] * P

        es = cma.CMAEvolutionStrategy(
            x0, args.sigma0,
            {"popsize": B, "bounds": [[0.0]*P, [1.0]*P], "verbose": -9},
        )
        meta = {
            "B": B, "N": N, "gen": 0,
            "best_fitness": -1.0,
            "best_params":  [PARAM_DEFAULTS[n] for n in PARAM_NAMES],
        }

    print(f"\nField Dynamics — CMA-ES  "
          f"popsize={B}  grid={N}x{N}  running {args.gens} iterations  "
          f"device={device}\n")

    field = BatchedField(B=B, N=N, device=device)

    for _ in range(args.gens):
        if es.stop():
            print("CMA-ES convergence criterion met — stopping early.")
            print(f"  Reason: {es.stop()}")
            break

        t0  = time.perf_counter()
        X   = es.ask()
        arr = batch_from_unit(X)

        fitness_acc = np.zeros(B, dtype=np.float32)
        for _ in range(args.episodes):
            field.params = array_to_params(arr, device)
            fitness_acc += field.run_episode().cpu().numpy()
        fitness = fitness_acc / args.episodes
        metrics = field.last_episode_metrics

        es.tell(X, (-fitness).tolist())

        elapsed  = time.perf_counter() - t0
        meta["gen"] += 1
        gen = meta["gen"]

        print_iteration(gen, fitness, arr, elapsed, es.sigma, metrics=metrics)

        best_idx = int(np.argmax(fitness))
        best_f   = float(fitness[best_idx])

        append_history(history, {
            "gen":          gen,
            "best_fitness": best_f,
            "mean_fitness": float(fitness.mean()),
            "sigma":        float(es.sigma),
        })

        if best_f > meta["best_fitness"]:
            meta["best_fitness"] = best_f
            meta["best_params"]  = arr[best_idx].tolist()
            save_genome(GENOME_FILE, arr[best_idx], best_f, gen)
            print(f"  ** New best → {GENOME_FILE}")

        save_state(es, meta)

    # ── geometry readout ─────────────────────────────────────────────────────
    print_geometry(es, es.sigma)

    print(f"\nTotal iterations so far: {meta['gen']}")
    print(f"Best fitness:            {meta['best_fitness']:.4f}")
    print(f"\nTo visualise best individual:")
    print(f"  python run.py --device {device} --load_genome {GENOME_FILE}")
    print(f"To continue search:")
    print(f"  python evolve_cmaes.py --gens {args.gens}")

    if args.plot:
        plot_geometry(es, es.sigma, history)


if __name__ == "__main__":
    main()
