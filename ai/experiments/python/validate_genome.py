"""
validate_genome.py - validate a saved genome across many deterministic seeds.

This is a lightweight robustness check for the current symmetry_v1 task.
It loads one genome, replays it over multiple deterministic initial states,
prints summary statistics, and can optionally show a compact heatmap.

Examples:
  python validate_genome.py
  python validate_genome.py --genome best_genome.json --seeds 24 --seed_base 123
  python validate_genome.py --cycles 4
  python validate_genome.py --plot
"""

import argparse
import json
from pathlib import Path

import numpy as np
import torch

from batched_field import BatchedField, PARAM_NAMES, array_to_params

BASE_DIR = Path(__file__).resolve().parent


def resolve_path(path: str | None) -> Path | None:
    if path is None:
        return None
    p = Path(path)
    if p.is_absolute():
        return p
    if p.exists():
        return p.resolve()
    return BASE_DIR / p


def pick_device(requested: str) -> str:
    if requested == "auto":
        if torch.cuda.is_available():
            print(f"GPU: {torch.cuda.get_device_name(0)}")
            return "cuda"
        print("No CUDA GPU found -> using CPU")
        return "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        print("CUDA not available, falling back to CPU")
        return "cpu"
    return requested


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--genome", default="best_genome.json",
                   help="Path to a saved genome JSON (default: best_genome.json)")
    p.add_argument("--device", default="auto")
    p.add_argument("--N", type=int, default=32, help="Grid size (default: 32)")
    p.add_argument("--seeds", type=int, default=16,
                   help="Number of deterministic seed slots to validate (default: 16)")
    p.add_argument("--seed_base", type=int, default=12345,
                   help="Base seed used to generate deterministic initial states")
    p.add_argument("--cycles", type=int, default=4,
                   help="Number of day/night task cycles to validate (default: 4)")
    p.add_argument("--plot", action="store_true",
                   help="Show a compact validation heatmap if matplotlib is available")
    return p.parse_args()


def load_genome(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def format_score(score):
    if score is None or not np.isfinite(score):
        return "--"
    return f"{float(score):.4f}"


def summarize_cycle_scores(cycle_scores: np.ndarray, cue_labels: list[str]):
    cycle_mean = cycle_scores.mean(axis=1)
    cycle_min = cycle_scores.min(axis=1)
    cycle_max = cycle_scores.max(axis=1)

    print("\nPer-cycle:")
    for idx, cue in enumerate(cue_labels):
        print(
            f"  cycle {idx+1:>2d}  cue {cue}  "
            f"mean={cycle_mean[idx]:.4f}  min={cycle_min[idx]:.4f}  max={cycle_max[idx]:.4f}"
        )

    print("\nPer-cue:")
    for cue in sorted(set(cue_labels)):
        mask = np.array([label == cue for label in cue_labels], dtype=bool)
        cue_vals = cycle_scores[mask].reshape(-1)
        print(
            f"  cue {cue}  mean={cue_vals.mean():.4f}  "
            f"min={cue_vals.min():.4f}  max={cue_vals.max():.4f}"
        )

    seed_mean = cycle_scores.mean(axis=0)
    seed_min = cycle_scores.min(axis=0)
    worst_seed = int(np.argmin(seed_mean))
    best_seed = int(np.argmax(seed_mean))

    print("\nPer-seed:")
    print(
        f"  mean(score over cycles): mean={seed_mean.mean():.4f}  "
        f"min={seed_mean.min():.4f}  max={seed_mean.max():.4f}"
    )
    print(
        f"  min(score over cycles):  mean={seed_min.mean():.4f}  "
        f"min={seed_min.min():.4f}  max={seed_min.max():.4f}"
    )
    print(f"  worst seed slot = {worst_seed}  mean={seed_mean[worst_seed]:.4f}")
    print(f"  best  seed slot = {best_seed}  mean={seed_mean[best_seed]:.4f}")


def maybe_plot(cycle_scores: np.ndarray, cue_labels: list[str], genome_name: str):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nmatplotlib not available -> skipping plot")
        return

    fig, (ax_heat, ax_seed) = plt.subplots(1, 2, figsize=(12, 4.5))

    im = ax_heat.imshow(cycle_scores, aspect="auto", cmap="viridis", vmin=0.0, vmax=1.0)
    ax_heat.set_title("Cycle x Seed Score")
    ax_heat.set_xlabel("Seed Slot")
    ax_heat.set_ylabel("Cycle")
    ax_heat.set_yticks(range(len(cue_labels)))
    ax_heat.set_yticklabels([f"{idx+1}:{cue}" for idx, cue in enumerate(cue_labels)])
    fig.colorbar(im, ax=ax_heat, fraction=0.046)

    seed_mean = cycle_scores.mean(axis=0)
    seed_min = cycle_scores.min(axis=0)
    x = np.arange(len(seed_mean))
    ax_seed.plot(x, seed_mean, label="seed mean", color="#4fc3f7", lw=1.2)
    ax_seed.plot(x, seed_min, label="seed min", color="#ffb74d", lw=1.0)
    ax_seed.set_ylim(0.0, 1.0)
    ax_seed.set_title("Per-seed Robustness")
    ax_seed.set_xlabel("Seed Slot")
    ax_seed.legend()

    fig.suptitle(f"Genome Validation: {genome_name}")
    plt.tight_layout()
    plt.show()


def main():
    args = parse_args()
    device = pick_device(args.device)
    genome_path = resolve_path(args.genome)
    genome = load_genome(genome_path)

    params_row = np.array([float(genome["params"][name]) for name in PARAM_NAMES], dtype=np.float32)
    arr = np.repeat(params_row[None, :], args.seeds, axis=0)
    params_t = array_to_params(arr, device)

    experiment = genome.get("experiment", "symmetry_v1")
    symmetry_break = genome.get("symmetry_break", "spatial")

    field = BatchedField(
        B=args.seeds,
        N=args.N,
        device=device,
        params=params_t,
        experiment=experiment,
        symmetry_break=symmetry_break,
    )
    slot_ids = np.arange(args.seeds, dtype=np.int64)
    fitness = field.run_episode(
        base_seed=args.seed_base,
        slot_ids=slot_ids,
        task_cycles=args.cycles,
    ).cpu().numpy()
    metrics = field.last_episode_metrics or {}

    print(f"Genome:      {genome_path}")
    print(f"Experiment:  {experiment}:{symmetry_break}")
    print(f"Saved fit:   {format_score(genome.get('fitness'))}")
    print(f"Seeds:       {args.seeds}  (base_seed={args.seed_base})")
    print(f"Cycles:      {args.cycles}")
    print("\nOverall:")
    print(f"  mean={fitness.mean():.4f}  std={fitness.std():.4f}")
    print(f"  min ={fitness.min():.4f}  max={fitness.max():.4f}")

    cycle_scores = metrics.get("cycle_scores")
    if cycle_scores is not None:
        cycle_scores = np.asarray(cycle_scores, dtype=np.float32)
        cue_labels = [field._cue_label_for_cycle(i) for i in range(cycle_scores.shape[0])]
        summarize_cycle_scores(cycle_scores, cue_labels)
        if args.plot:
            maybe_plot(cycle_scores, cue_labels, genome_path.name)
    elif args.plot:
        print("\nNo cycle_scores available for this experiment -> skipping plot")


if __name__ == "__main__":
    main()
