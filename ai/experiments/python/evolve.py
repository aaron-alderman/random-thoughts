"""
evolve.py — evolutionary search over Field Dynamics parameters.

Strategy: (B/2 + B/2) — keep top half, fill bottom half with mutated offspring.
Crossover: uniform (each parameter drawn from one of two parents at random).
Mutation:  Gaussian noise scaled to 15% of each parameter's range, then clamped.

Usage:
    python evolve.py                        # B=16, N=32, 40 generations, cuda
    python evolve.py --B 32 --gens 80       # larger population
    python evolve.py --device cpu           # CPU fallback
    python evolve.py --resume best_genome.json  # continue from saved best
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

BASE_DIR = Path(__file__).resolve().parent
GENOME_FILE = BASE_DIR / "best_genome.json"


# ── GA operators ──────────────────────────────────────────────────────────────

def clamp_params(arr: np.ndarray) -> np.ndarray:
    """Clamp each parameter column to its valid range."""
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
        arr[:, i] = np.clip(arr[:, i], lo, hi)
    return arr


def mutate(arr: np.ndarray, strength: float = 1.0) -> np.ndarray:
    """Gaussian mutation. strength scales sigma (1.0 = 15% of range)."""
    out = arr.copy()
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
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

def save_genome(path: str, params_row: np.ndarray, fitness: float, generation: int):
    genome = {
        "generation": generation,
        "fitness":    float(fitness),
        "params":     {name: float(params_row[i]) for i, name in enumerate(PARAM_NAMES)},
    }
    with open(path, "w") as f:
        json.dump(genome, f, indent=2)


def load_genome(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def ensure_genome_file(path: Path):
    if path.exists():
        return
    params_row = np.array([PARAM_DEFAULTS[name] for name in PARAM_NAMES], dtype=np.float32)
    save_genome(path, params_row, fitness=-1.0, generation=-1)


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
    print("  best genome:")
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
        normed = (best_p[i] - lo) / (hi - lo)
        print(f"    {name:>15s} = {best_p[i]:.5f}  [{_bar(normed, 15)}]")


# ── main ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--B",      type=int,   default=16,     help="Population size (default 16)")
    p.add_argument("--N",      type=int,   default=32,     help="Grid size (default 32)")
    p.add_argument("--gens",   type=int,   default=40,     help="Generations (default 40)")
    p.add_argument("--device", default="auto")
    p.add_argument("--resume", default=None,
                   help="Path to best_genome.json to seed the initial population")
    p.add_argument("--episodes", type=int, default=1,
                   help="Episodes per generation for fitness averaging (default 1)")
    p.add_argument("--seed_default", action="store_true",
                   help="Include one copy of the v7 default params in the initial population")
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
    device = pick_device(args.device)
    B      = args.B
    N      = args.N
    gens   = args.gens
    eps    = args.episodes
    ensure_genome_file(GENOME_FILE)

    print(f"Field Dynamics — Evolutionary Search")
    print(f"  population={B}  grid={N}x{N}  generations={gens}  "
          f"episodes/gen={eps}  device={device}\n")

    # ── initial population ────────────────────────────────────────────────────
    arr = np.zeros((B, len(PARAM_NAMES)), dtype=np.float32)
    for i, name in enumerate(PARAM_NAMES):
        lo, hi = PARAM_BOUNDS[name]
        arr[:, i] = np.random.uniform(lo, hi, B)

    if args.seed_default:
        # Slot 0: exact v7 defaults
        for i, name in enumerate(PARAM_NAMES):
            arr[0, i] = PARAM_DEFAULTS[name]

    if args.resume:
        resume_path = resolve_path(args.resume)
        genome = load_genome(resume_path)
        print(f"Resuming from {resume_path}  (gen {genome['generation']}, "
              f"fitness {genome['fitness']:.4f})")
        for i, name in enumerate(PARAM_NAMES):
            arr[0, i] = genome["params"][name]   # seed slot 0 with best known

    # ── build simulation ──────────────────────────────────────────────────────
    params_t = array_to_params(arr, device)
    field    = BatchedField(B=B, N=N, device=device, params=params_t)

    best_fitness_ever = -1.0
    best_arr_ever     = arr[0].copy()
    best_gen_ever     = 0

    mut_strength = 1.0   # annealed slowly

    for gen in range(gens):
        t0 = time.perf_counter()

        # Evaluate fitness — average over multiple episodes if requested
        fitness_acc = np.zeros(B, dtype=np.float32)
        for ep in range(eps):
            field.params = array_to_params(arr, device)
            f_t = field.run_episode()
            fitness_acc += f_t.cpu().numpy()
        fitness = fitness_acc / eps
        metrics = field.last_episode_metrics

        elapsed = time.perf_counter() - t0

        print_generation(gen, gens, fitness, arr, elapsed, metrics=metrics)

        best_idx = int(np.argmax(fitness))
        if fitness[best_idx] > best_fitness_ever:
            best_fitness_ever = fitness[best_idx]
            best_arr_ever     = arr[best_idx].copy()
            best_gen_ever     = gen
            save_genome(GENOME_FILE, best_arr_ever, best_fitness_ever, gen)
            print(f"  ** New best saved → {GENOME_FILE}")

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
    print(f"\nSaved to {GENOME_FILE}")
    print(f"\nTo visualise the best individual:")
    print(f"  python run.py --device {device} --load_genome {GENOME_FILE}")


if __name__ == "__main__":
    main()
