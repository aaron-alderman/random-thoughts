from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any

import numpy as np


PARAM_NAMES = (
    "W",
    "alpha",
    "beta",
    "selfEx",
    "epsilon",
    "retain",
    "phaseInertia",
    "edgeGain",
    "driveAmp",
    "cueAmp",
    "cycleLen",
    "dayFrac",
    "kAlign",
    "persistAlpha",
    "omegaLearn",
    "edgeDecay",
    "driveRamp",
    "driveClamp",
    "tauC",
)

PARAM_BOUNDS = {
    "W":            (0.000005, 0.18),
    "alpha":        (0.5, 0.9999),
    "beta":         (0.000005, 0.80),
    "selfEx":       (0.0001, 0.90),
    "epsilon":      (0.0001, 0.50),
    "retain":       (0.20, 0.95),
    "phaseInertia": (0.30, 8.00),
    "edgeGain":     (0.0, 20.0),
    "driveAmp":     (0.2, 5.0),
    "cueAmp":       (0.0, 3.0),
    "cycleLen":     (200.0, 500.0),
    "dayFrac":      (0.49, 0.51),
    "kAlign":       (0.20, 0.80),
    "persistAlpha": (0.10, 0.50),
    "omegaLearn":   (0.03, 0.30),
    "edgeDecay":    (1e-5, 5e-3),
    "driveRamp":    (8.0, 64.0),
    "driveClamp":   (0.20, 0.80),
    "tauC":         (0.30, 0.60),
}

PARAM_DEFAULTS = {
    "W":            0.0325,
    "alpha":        0.843,
    "beta":         0.485,
    "selfEx":       0.06,
    "epsilon":      0.035,
    "retain":       0.60,
    "phaseInertia": 1.25,
    "edgeGain":     8.00,
    "driveAmp":     1.00,
    "cueAmp":       0.30,
    "cycleLen":     800.0,
    "dayFrac":      0.50,
    "kAlign":       0.43,
    "persistAlpha": 0.28,
    "omegaLearn":   0.12,
    "edgeDecay":    0.0008,
    "driveRamp":    32.0,
    "driveClamp":   0.50,
    "tauC":         0.45,
}

FIXED_PARAM_DEFAULTS = {
    "phi":          0.00,
    "triWeight":    0.52,
    "eta":          0.00,
    "drivePer":     80,
    "taskCycles":   2,
    "warmupFrac":   0.375,
    "spatialBias":  1.00,
}

FULL_RUNTIME_PARAM_NAMES = PARAM_NAMES + tuple(FIXED_PARAM_DEFAULTS.keys())

PARAM_METADATA = {
    "W":            {"group": "core_field", "search_default": True, "role": "backbone"},
    "alpha":        {"group": "core_field", "search_default": True, "role": "backbone"},
    "beta":         {"group": "core_field", "search_default": True, "role": "backbone"},
    "selfEx":       {"group": "core_field", "search_default": True, "role": "backbone"},
    "kAlign":       {"group": "core_field", "search_default": True, "role": "backbone"},
    "tauC":         {"group": "core_field", "search_default": True, "role": "backbone"},
    "epsilon":      {"group": "structural_plasticity", "search_default": True, "role": "backbone"},
    "retain":       {"group": "structural_plasticity", "search_default": True, "role": "backbone"},
    "edgeGain":     {"group": "structural_plasticity", "search_default": True, "role": "backbone"},
    "edgeDecay":    {"group": "structural_plasticity", "search_default": True, "role": "backbone"},
    "persistAlpha": {"group": "structural_plasticity", "search_default": True, "role": "backbone"},
    "omegaLearn":   {"group": "structural_plasticity", "search_default": True, "role": "backbone"},
    "driveAmp":     {"group": "drive_schedule", "search_default": True, "role": "backbone"},
    "cueAmp":       {"group": "drive_schedule", "search_default": True, "role": "backbone"},
    "cycleLen":     {"group": "drive_schedule", "search_default": True, "role": "backbone"},
    "dayFrac":      {"group": "drive_schedule", "search_default": True, "role": "backbone"},
    "driveRamp":    {"group": "drive_schedule", "search_default": True, "role": "backbone"},
    "driveClamp":   {"group": "drive_schedule", "search_default": True, "role": "backbone"},
    "phaseInertia": {"group": "phase_dynamics", "search_default": True, "role": "backbone"},
    "taskCycles":   {"group": "fixed_non_evolved", "search_default": False, "role": "derived"},
    "warmupFrac":   {"group": "fixed_non_evolved", "search_default": False, "role": "derived"},
    "drivePer":     {"group": "fixed_non_evolved", "search_default": False, "role": "derived"},
    "phi":          {"group": "fixed_non_evolved", "search_default": False, "role": "derived"},
    "triWeight":    {"group": "fixed_non_evolved", "search_default": False, "role": "derived"},
    "eta":          {"group": "fixed_non_evolved", "search_default": False, "role": "derived"},
    "spatialBias":  {"group": "fixed_non_evolved", "search_default": False, "role": "derived"},
}


@dataclass(frozen=True)
class ExperimentConfig:
    experiment: str
    active_params: tuple[str, ...]
    frozen_overrides: dict[str, float]
    fitness_profile: str
    symmetry_breaks: tuple[str, ...]
    notes: str = ""


EXPERIMENT_CONFIGS: dict[str, ExperimentConfig] = {
    "symmetry_v1": ExperimentConfig(
        experiment="symmetry_v1",
        active_params=(
            "driveAmp",
            "cueAmp",
            "cycleLen",
            "kAlign",
            "persistAlpha",
            "omegaLearn",
            "edgeDecay",
            "driveRamp",
            "driveClamp",
            "tauC",
        ),
        frozen_overrides={},
        fitness_profile="symmetry_v1",
        symmetry_breaks=("spatial",),
        notes="Research branch kept above the 8-parameter guideline because cue and schedule tuning are still core to the symmetry task.",
    ),
    "replay": ExperimentConfig(
        experiment="replay",
        active_params=(
            "driveAmp",
            "cycleLen",
            "phaseInertia",
            "persistAlpha",
            "omegaLearn",
            "edgeDecay",
            "tauC",
        ),
        frozen_overrides={},
        fitness_profile="replay",
        symmetry_breaks=(),
    ),
    "temporal_v1": ExperimentConfig(
        experiment="temporal_v1",
        active_params=(
            "epsilon",
            "beta",
            "driveAmp",
            "cycleLen",
            "kAlign",
            "tauC",
        ),
        frozen_overrides={},
        fitness_profile="temporal_v1",
        symmetry_breaks=(),
    ),
}


def backbone_defaults() -> dict[str, float]:
    return {name: float(PARAM_DEFAULTS[name]) for name in PARAM_NAMES}


def full_runtime_defaults() -> dict[str, float]:
    merged = backbone_defaults()
    merged.update({name: float(val) for name, val in FIXED_PARAM_DEFAULTS.items()})
    return merged


def get_experiment_config(experiment: str) -> ExperimentConfig:
    try:
        return EXPERIMENT_CONFIGS[experiment]
    except KeyError as exc:
        raise ValueError(f"Unsupported experiment config: {experiment}") from exc


def active_param_names(experiment: str) -> tuple[str, ...]:
    return get_experiment_config(experiment).active_params


def searchable_frozen_param_names(experiment: str) -> tuple[str, ...]:
    active = set(active_param_names(experiment))
    return tuple(name for name in PARAM_NAMES if name not in active)


def active_param_defaults(experiment: str) -> dict[str, float]:
    resolved = resolve_runtime_params(experiment)
    return {name: float(resolved[name]) for name in active_param_names(experiment)}


def active_param_bounds(experiment: str) -> dict[str, tuple[float, float]]:
    return {name: PARAM_BOUNDS[name] for name in active_param_names(experiment)}


def resolve_runtime_params(
    experiment: str,
    active_values: dict[str, float] | None = None,
    extra_overrides: dict[str, float] | None = None,
) -> dict[str, float]:
    cfg = get_experiment_config(experiment)
    resolved = full_runtime_defaults()
    resolved.update({name: float(val) for name, val in cfg.frozen_overrides.items()})
    if active_values:
        for name, value in active_values.items():
            resolved[name] = float(value)
    if extra_overrides:
        for name, value in extra_overrides.items():
            resolved[name] = float(value)
    return resolved


def resolved_searchable_params(experiment: str, active_values: dict[str, float] | None = None) -> dict[str, float]:
    resolved = resolve_runtime_params(experiment, active_values=active_values)
    return {name: float(resolved[name]) for name in PARAM_NAMES}


def active_values_from_row(active_names: tuple[str, ...], row: np.ndarray | list[float]) -> dict[str, float]:
    return {name: float(row[i]) for i, name in enumerate(active_names)}


def resolved_searchable_row(experiment: str, active_names: tuple[str, ...], row: np.ndarray | list[float]) -> np.ndarray:
    active_values = active_values_from_row(active_names, row)
    resolved = resolved_searchable_params(experiment, active_values=active_values)
    return np.array([resolved[name] for name in PARAM_NAMES], dtype=np.float32)


def resolved_searchable_matrix(experiment: str, active_names: tuple[str, ...], arr: np.ndarray) -> np.ndarray:
    return np.stack([resolved_searchable_row(experiment, active_names, row) for row in arr], axis=0)


def split_genome_params(experiment: str, resolved_params: dict[str, Any]) -> tuple[dict[str, float], dict[str, float], dict[str, float]]:
    cfg = get_experiment_config(experiment)
    active = {name: float(resolved_params[name]) for name in cfg.active_params}
    frozen = {
        name: float(resolved_params[name])
        for name in FULL_RUNTIME_PARAM_NAMES
        if name not in cfg.active_params
    }
    full = {name: float(resolved_params[name]) for name in FULL_RUNTIME_PARAM_NAMES}
    return active, frozen, full


def merged_genome_params(genome: dict[str, Any]) -> dict[str, float]:
    if "resolved_params" in genome:
        return {name: float(val) for name, val in genome["resolved_params"].items()}
    experiment = genome["experiment"]
    active_values = genome.get("active_params", {})
    frozen_values = genome.get("frozen_params", {})
    return resolve_runtime_params(
        experiment,
        active_values={name: float(val) for name, val in active_values.items()},
        extra_overrides={name: float(val) for name, val in frozen_values.items()},
    )


def experiment_dimension_count(experiment: str) -> int:
    return len(active_param_names(experiment))


def parameter_summary_lines(experiment: str, resolved_params: dict[str, float]) -> tuple[list[tuple[str, float]], list[tuple[str, float]]]:
    active_names = active_param_names(experiment)
    active_lines = [(name, float(resolved_params[name])) for name in active_names]
    frozen_lines = [(name, float(resolved_params[name])) for name in searchable_frozen_param_names(experiment)]
    return active_lines, frozen_lines


def parameter_note_lines() -> list[str]:
    lines = []
    for experiment, cfg in EXPERIMENT_CONFIGS.items():
        if len(cfg.active_params) > 8 and cfg.notes:
            lines.append(f"{experiment}: {cfg.notes}")
    return lines
