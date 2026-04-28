from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from parameter_policy import (
    PARAM_NAMES,
    active_param_names,
    merged_genome_params,
    resolve_runtime_params,
    split_genome_params,
)


def save_genome(
    path: str | Path,
    *,
    experiment: str,
    symmetry_break: str | None,
    generation: int,
    fitness: float,
    resolved_params: dict[str, float],
    eval_episode_seeds: list[int] | None = None,
    eval_slot: int | None = None,
):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    active_params, frozen_params, full_params = split_genome_params(experiment, resolved_params)
    genome = {
        "generation": int(generation),
        "fitness": float(fitness),
        "experiment": experiment,
        "symmetry_break": symmetry_break,
        "active_param_names": list(active_param_names(experiment)),
        "active_params": active_params,
        "frozen_params": frozen_params,
        "resolved_params": full_params,
    }
    if eval_episode_seeds is not None:
        genome["eval_episode_seeds"] = [int(seed) for seed in eval_episode_seeds]
    if eval_slot is not None:
        genome["eval_slot"] = int(eval_slot)
    with open(path, "w") as f:
        json.dump(genome, f, indent=2)


def load_genome(path: str | Path) -> dict:
    with open(path) as f:
        return json.load(f)


def ensure_genome_file(path: Path, experiment: str, symmetry_break: str | None):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    save_genome(
        path,
        experiment=experiment,
        symmetry_break=symmetry_break,
        generation=-1,
        fitness=-1.0,
        resolved_params=resolve_runtime_params(experiment),
    )


def genome_matches_run(genome: dict, experiment: str, symmetry_break: str | None) -> bool:
    genome_experiment = genome.get("experiment")
    genome_break = genome.get("symmetry_break")
    return genome_experiment == experiment and genome_break == symmetry_break


def genome_active_row(genome: dict, experiment: str, active_names: tuple[str, ...] | None = None) -> np.ndarray:
    active_names = active_names or active_param_names(experiment)
    resolved = merged_genome_params(genome)
    return np.array([float(resolved[name]) for name in active_names], dtype=np.float64)


def genome_resolved_searchable_row(genome: dict) -> np.ndarray:
    resolved = merged_genome_params(genome)
    return np.array([float(resolved[name]) for name in PARAM_NAMES], dtype=np.float64)
