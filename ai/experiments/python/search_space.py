import math
import numpy as np


LOG_PARAMS = {"W", "beta", "epsilon"}
ALPHA_GAP_PARAM = "alpha"


def physical_to_search_value(name: str, value: float) -> float:
    if name in LOG_PARAMS:
        return math.log10(max(value, 1e-12))
    if name == ALPHA_GAP_PARAM:
        return math.log10(max(1.0 - value, 1e-12))
    return float(value)


def search_to_physical_value(name: str, value: float) -> float:
    if name in LOG_PARAMS:
        return float(10.0 ** value)
    if name == ALPHA_GAP_PARAM:
        return float(1.0 - (10.0 ** value))
    return float(value)


def transform_bounds(param_names, param_bounds) -> dict:
    out = {}
    for name in param_names:
        lo, hi = param_bounds[name]
        search_lo = physical_to_search_value(name, lo)
        search_hi = physical_to_search_value(name, hi)
        # Some transforms (for example alpha -> log10(1 - alpha)) reverse the
        # ordering, so clamp/mapping code needs bounds in search-space order.
        out[name] = tuple(sorted((search_lo, search_hi)))
    return out


def physical_row_to_search(param_names, row: np.ndarray) -> np.ndarray:
    return np.array(
        [physical_to_search_value(name, float(row[i])) for i, name in enumerate(param_names)],
        dtype=np.float64,
    )


def search_row_to_physical(param_names, row: np.ndarray) -> np.ndarray:
    return np.array(
        [search_to_physical_value(name, float(row[i])) for i, name in enumerate(param_names)],
        dtype=np.float64,
    )


def physical_matrix_to_search(param_names, arr: np.ndarray) -> np.ndarray:
    return np.stack([physical_row_to_search(param_names, row) for row in arr], axis=0)


def search_matrix_to_physical(param_names, arr: np.ndarray) -> np.ndarray:
    return np.stack([search_row_to_physical(param_names, row) for row in arr], axis=0)
