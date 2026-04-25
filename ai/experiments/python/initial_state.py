import numpy as np


def build_initial_fields(n: int, base_seed: int, slot: int):
    """Deterministic per-slot initial state shared by search and live replay."""
    seed = np.random.SeedSequence([int(base_seed), int(slot)])
    rng = np.random.default_rng(seed)
    angles = rng.random((n, n), dtype=np.float32) * (2.0 * np.pi)
    noise = (rng.random((n, n), dtype=np.float32) - 0.5) * 0.01
    structural = 0.1 + rng.random((n, n), dtype=np.float32) * 0.05
    return angles, noise, structural
