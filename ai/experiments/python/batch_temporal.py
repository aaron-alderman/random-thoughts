"""
batch_temporal.py - batch-run temporal_v1 across deterministic seed slots.

This is a lightweight manual-validation script for the temporal-contiguity
experiment before porting it into batched evolutionary search.

Outputs:
  - per_seed_trace.csv    one row per seed slot per traced step
  - aggregate_trace.csv   step-wise mean/std/min/max across seed slots
  - seed_summary.csv      compact per-seed summary metrics
  - metadata.json         run arguments + optional genome source

Examples:
  python batch_temporal.py
  python batch_temporal.py --seeds 12 --seed_base 123 --trace_every 5
  python batch_temporal.py --cycles 3 --out_dir temporal_batch_runs\trial_01
  python batch_temporal.py --load_genome best_genome.json
"""

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
import torch

from field_dynamics import FieldDynamics

BASE_DIR = Path(__file__).resolve().parent
TRACE_METRICS = [
    "C_mean",
    "C_slow_mean",
    "R_mean",
    "S_mean",
    "dC_mean",
    "dC_pos_mean",
    "dC_neg_mean",
    "R_slow_mean",
    "retention_mean",
    "improve_mean",
    "degrade_mean",
    "surprise_gate_mean",
    "quiet_prune_mean",
    "S_growth_mean",
    "S_mass",
]
TRACE_FIELDS = [
    "seed_slot",
    "step",
    "cycle_mode",
    "cycle_count",
    "drive_env",
    "gate_value",
    "signal_phase",
    *TRACE_METRICS,
]
SUMMARY_FIELDS = [
    "seed_slot",
    "total_steps",
    "trace_samples",
    "peak_S_growth_mean",
    "peak_S_growth_step",
    "mean_S_growth_mean",
    "positive_growth_samples",
    "positive_growth_fraction",
    "growth_auc_pos",
    "final_retention_mean",
    "max_surprise_gate_mean",
    "max_improve_mean",
    "max_degrade_mean",
    "final_C_mean",
    "final_C_slow_mean",
    "final_S_mean",
    "final_S_mass",
    "final_R_slow_mean",
]


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
            print(f"GPU detected: {torch.cuda.get_device_name(0)} -> using CUDA")
            return "cuda"
        print("No CUDA GPU found -> using CPU")
        return "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        print("WARNING: --device cuda requested but CUDA not available. Falling back to CPU.")
        return "cpu"
    return requested


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--device", default="auto")
    p.add_argument("--N", type=int, default=32, help="Grid size (default: 32)")
    p.add_argument("--seeds", type=int, default=8,
                   help="Number of deterministic seed slots to run (default: 8)")
    p.add_argument("--seed_base", type=int, default=12345,
                   help="Base seed shared across seed slots (default: 12345)")
    p.add_argument("--cycles", type=int, default=2,
                   help="Number of task cycles to run (default: 2)")
    p.add_argument("--steps", type=int, default=None,
                   help="Override total simulation steps; default derives from warmup + cycles * cycleLen")
    p.add_argument("--trace_every", type=int, default=10,
                   help="Simulation-step cadence for trace rows (default: 10)")
    p.add_argument("--out_dir", default="temporal_batch_runs",
                   help="Output directory for CSV/JSON artifacts")
    p.add_argument("--load_genome", default=None,
                   help="Optional genome JSON whose params should seed temporal_v1")
    return p.parse_args()


def load_genome(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def build_param_overrides(args) -> tuple[dict, Path | None]:
    overrides = {"taskCycles": int(args.cycles)}
    genome_path = resolve_path(args.load_genome)
    if genome_path is None:
        return overrides, None

    genome = load_genome(genome_path)
    overrides.update(genome.get("params", {}))
    return overrides, genome_path


def make_trace_row(st: dict, seed_slot: int) -> dict:
    return {
        "seed_slot": seed_slot,
        "step": st["step"],
        "cycle_mode": st["cycle_mode"],
        "cycle_count": st["cycle_count"],
        "drive_env": st["drive_env"],
        "gate_value": st["gate_value"],
        "signal_phase": st["signal_phase"],
        "C_mean": float(np.mean(st["C"])),
        "C_slow_mean": st["C_slow_mean"],
        "R_mean": float(np.mean(st["R"])),
        "S_mean": float(np.mean(st["S"])),
        "dC_mean": st["dC_mean"],
        "dC_pos_mean": st["dC_pos_mean"],
        "dC_neg_mean": st["dC_neg_mean"],
        "R_slow_mean": st["R_slow_mean"],
        "retention_mean": st["retention_mean"],
        "improve_mean": st["improve_mean"],
        "degrade_mean": st["degrade_mean"],
        "surprise_gate_mean": st["surprise_gate_mean"],
        "quiet_prune_mean": st["quiet_prune_mean"],
        "S_growth_mean": st["S_growth_mean"],
        "S_mass": st["S_mass"],
    }


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize_seed(trace_rows: list[dict], trace_every: int, total_steps: int) -> dict:
    growth = np.asarray([float(row["S_growth_mean"]) for row in trace_rows], dtype=np.float64)
    surprise = np.asarray([float(row["surprise_gate_mean"]) for row in trace_rows], dtype=np.float64)
    improve = np.asarray([float(row["improve_mean"]) for row in trace_rows], dtype=np.float64)
    degrade = np.asarray([float(row["degrade_mean"]) for row in trace_rows], dtype=np.float64)

    peak_idx = int(np.argmax(growth)) if len(growth) else 0
    pos_mask = growth > 0.0
    final = trace_rows[-1]
    return {
        "seed_slot": final["seed_slot"],
        "total_steps": total_steps,
        "trace_samples": len(trace_rows),
        "peak_S_growth_mean": float(growth[peak_idx]) if len(growth) else math.nan,
        "peak_S_growth_step": int(trace_rows[peak_idx]["step"]) if trace_rows else 0,
        "mean_S_growth_mean": float(np.mean(growth)) if len(growth) else math.nan,
        "positive_growth_samples": int(np.count_nonzero(pos_mask)),
        "positive_growth_fraction": float(np.mean(pos_mask)) if len(growth) else math.nan,
        "growth_auc_pos": float(np.sum(np.clip(growth, a_min=0.0, a_max=None)) * trace_every),
        "final_retention_mean": float(final["retention_mean"]),
        "max_surprise_gate_mean": float(np.max(surprise)) if len(surprise) else math.nan,
        "max_improve_mean": float(np.max(improve)) if len(improve) else math.nan,
        "max_degrade_mean": float(np.max(degrade)) if len(degrade) else math.nan,
        "final_C_mean": float(final["C_mean"]),
        "final_C_slow_mean": float(final["C_slow_mean"]),
        "final_S_mean": float(final["S_mean"]),
        "final_S_mass": float(final["S_mass"]),
        "final_R_slow_mean": float(final["R_slow_mean"]),
    }


def aggregate_trace_rows(trace_rows: list[dict]) -> list[dict]:
    grouped: dict[int, list[dict]] = {}
    for row in trace_rows:
        grouped.setdefault(int(row["step"]), []).append(row)

    out = []
    for step in sorted(grouped):
        rows = grouped[step]
        agg = {
            "step": step,
            "trace_samples": len(rows),
            "cycle_mode": rows[0]["cycle_mode"],
            "cycle_count_mean": float(np.mean([float(row["cycle_count"]) for row in rows])),
        }
        for metric in TRACE_METRICS:
            vals = np.asarray([float(row[metric]) for row in rows], dtype=np.float64)
            agg[f"{metric}_mean"] = float(np.mean(vals))
            agg[f"{metric}_std"] = float(np.std(vals))
            agg[f"{metric}_min"] = float(np.min(vals))
            agg[f"{metric}_max"] = float(np.max(vals))
        out.append(agg)
    return out


def print_summary(summary_rows: list[dict]):
    peak = np.asarray([row["peak_S_growth_mean"] for row in summary_rows], dtype=np.float64)
    auc = np.asarray([row["growth_auc_pos"] for row in summary_rows], dtype=np.float64)
    frac = np.asarray([row["positive_growth_fraction"] for row in summary_rows], dtype=np.float64)
    hold = np.asarray([row["final_retention_mean"] for row in summary_rows], dtype=np.float64)
    final_s = np.asarray([row["final_S_mass"] for row in summary_rows], dtype=np.float64)
    final_r = np.asarray([row["final_R_slow_mean"] for row in summary_rows], dtype=np.float64)

    print("\nBatch summary:")
    print(f"  peak S_growth_mean  mean={peak.mean():.4f}  min={peak.min():.4f}  max={peak.max():.4f}")
    print(f"  growth_auc_pos      mean={auc.mean():.4f}  min={auc.min():.4f}  max={auc.max():.4f}")
    print(f"  positive fraction   mean={frac.mean():.4f}  min={frac.min():.4f}  max={frac.max():.4f}")
    print(f"  final retention     mean={hold.mean():.4f}  min={hold.min():.4f}  max={hold.max():.4f}")
    print(f"  final S_mass        mean={final_s.mean():.4f}  min={final_s.min():.4f}  max={final_s.max():.4f}")
    print(f"  final R_slow_mean   mean={final_r.mean():.4f}  min={final_r.min():.4f}  max={final_r.max():.4f}")


def main():
    args = parse_args()
    args.trace_every = max(1, int(args.trace_every))
    device = pick_device(args.device)
    param_overrides, genome_path = build_param_overrides(args)
    out_dir = resolve_path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    trace_rows: list[dict] = []
    summary_rows: list[dict] = []

    print("Temporal batch run")
    print(f"  device={device}  N={args.N}  seeds={args.seeds}  seed_base={args.seed_base}")
    print(f"  cycles={args.cycles}  trace_every={args.trace_every}")
    print(f"  out_dir={out_dir}")
    if genome_path is not None:
        print(f"  genome_params={genome_path}")

    for seed_slot in range(args.seeds):
        sim = FieldDynamics(
            N=args.N,
            device=device,
            experiment="temporal_v1",
            reset_seed=args.seed_base,
            reset_slot=seed_slot,
            **param_overrides,
        )
        total_steps = int(args.steps) if args.steps is not None else int(sim.P["warmup"] + args.cycles * sim.P["cycleLen"])
        seed_trace_rows = [make_trace_row(sim.get_state(), seed_slot)]

        for _ in range(total_steps):
            sim.update()
            if sim.step % args.trace_every == 0 or sim.step >= total_steps:
                seed_trace_rows.append(make_trace_row(sim.get_state(), seed_slot))

        trace_rows.extend(seed_trace_rows)
        summary_rows.append(summarize_seed(seed_trace_rows, args.trace_every, total_steps))

    aggregate_rows = aggregate_trace_rows(trace_rows)
    aggregate_fields = [
        "step",
        "trace_samples",
        "cycle_mode",
        "cycle_count_mean",
    ]
    for metric in TRACE_METRICS:
        aggregate_fields.extend([
            f"{metric}_mean",
            f"{metric}_std",
            f"{metric}_min",
            f"{metric}_max",
        ])

    trace_path = out_dir / "per_seed_trace.csv"
    aggregate_path = out_dir / "aggregate_trace.csv"
    summary_path = out_dir / "seed_summary.csv"
    metadata_path = out_dir / "metadata.json"

    write_csv(trace_path, TRACE_FIELDS, trace_rows)
    write_csv(aggregate_path, aggregate_fields, aggregate_rows)
    write_csv(summary_path, SUMMARY_FIELDS, summary_rows)

    metadata = {
        "experiment": "temporal_v1",
        "device": device,
        "N": args.N,
        "seeds": args.seeds,
        "seed_base": args.seed_base,
        "cycles": args.cycles,
        "steps": args.steps,
        "trace_every": args.trace_every,
        "out_dir": str(out_dir),
        "load_genome": None if genome_path is None else str(genome_path),
        "param_overrides": param_overrides,
    }
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print_summary(summary_rows)
    print("\nArtifacts:")
    print(f"  {trace_path}")
    print(f"  {aggregate_path}")
    print(f"  {summary_path}")
    print(f"  {metadata_path}")


if __name__ == "__main__":
    main()
