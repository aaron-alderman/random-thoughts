from __future__ import annotations

from pathlib import Path

from parameter_policy import EXPERIMENT_CONFIGS


SUPPORTED_EXPERIMENTS = tuple(EXPERIMENT_CONFIGS.keys())
SUPPORTED_SYMMETRY_BREAKS = ("spatial",)


def validate_experiment(experiment: str, symmetry_break: str | None = None):
    if experiment not in SUPPORTED_EXPERIMENTS:
        raise ValueError(f"Unsupported experiment: {experiment}")
    if experiment == "symmetry_v1":
        if symmetry_break not in SUPPORTED_SYMMETRY_BREAKS:
            raise ValueError(f"Unsupported symmetry break for {experiment}: {symmetry_break}")
    else:
        symmetry_break = None
    return experiment, symmetry_break


def genome_root(base_dir: Path) -> Path:
    return base_dir / "genomes"


def genome_dir(base_dir: Path, experiment: str) -> Path:
    return genome_root(base_dir) / experiment


def history_dir(base_dir: Path, experiment: str) -> Path:
    return genome_dir(base_dir, experiment) / "history"


def default_genome_path(base_dir: Path, experiment: str) -> Path:
    return genome_dir(base_dir, experiment) / "best_genome.json"


def search_state_root(base_dir: Path) -> Path:
    return base_dir / "search_state"


def search_state_dir(base_dir: Path, experiment: str) -> Path:
    return search_state_root(base_dir) / experiment


def default_cmaes_state_path(base_dir: Path, experiment: str, symmetry_break: str | None = None) -> Path:
    _ = symmetry_break
    return search_state_dir(base_dir, experiment) / "cmaes_state.pkl"


def default_cmaes_history_path(base_dir: Path, experiment: str, symmetry_break: str | None = None) -> Path:
    _ = symmetry_break
    return search_state_dir(base_dir, experiment) / "cmaes_history.json"
