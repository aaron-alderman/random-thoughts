from pathlib import Path


SUPPORTED_EXPERIMENTS = ("symmetry_v1", "replay")
SUPPORTED_SYMMETRY_BREAKS = ("spatial",)


def validate_experiment(experiment: str, symmetry_break: str | None = None):
    if experiment not in SUPPORTED_EXPERIMENTS:
        raise ValueError(f"Unsupported experiment: {experiment}")
    if experiment == "symmetry_v1":
        if symmetry_break not in SUPPORTED_SYMMETRY_BREAKS:
            raise ValueError(f"Unsupported symmetry break for {experiment}: {symmetry_break}")
    return experiment, symmetry_break


def default_genome_path(base_dir: Path, *args, **kwargs) -> Path:
    """Single canonical genome file — always best_genome.json regardless of experiment."""
    return base_dir / "best_genome.json"


def default_cmaes_state_path(base_dir: Path, experiment: str, symmetry_break: str | None = None) -> Path:
    suffix = experiment if experiment == "replay" else f"{experiment}.{symmetry_break}"
    return base_dir / f"cmaes_state.{suffix}.pkl"


def default_cmaes_history_path(base_dir: Path, experiment: str, symmetry_break: str | None = None) -> Path:
    suffix = experiment if experiment == "replay" else f"{experiment}.{symmetry_break}"
    return base_dir / f"cmaes_history.{suffix}.json"
