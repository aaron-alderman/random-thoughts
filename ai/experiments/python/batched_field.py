"""
batched_field.py — B instances of Field Dynamics v7 running in parallel.

All field tensors are (B, N, N) instead of (N, N).
Sedge is (B, N, N, 8).
Evolved parameters are (B, 1, 1) tensors so they broadcast over the grid.

All instances share the same input/output node positions, but cycle timing can
now vary per candidate via evolved schedule parameters. The batch dimension is
still population-level parallelism, but each individual can run on its own
warmup/day/night clock.

Fitness returned by run_episode():
    fitness = peak_corr
              * clamp(night_rms / (day_rms + 1e-4), max=2)
              * frequency_faithfulness
              * efficiency_reward

  peak_corr : best Pearson r between last-HIST day output and first-HIST night output
  night_rms / day_rms : signal-retention ratio — rewards keeping amplitude alive at night
  frequency_faithfulness : min(night_period / day_period, day_period / night_period)
                           in [0, 1] when both periods are measurable, else 0
"""

import math
import torch
import numpy as np
from experiment_paths import validate_experiment
from initial_state import build_initial_fields

TWO_PI = 2.0 * math.pi

NB8 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
NB4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _wrap(d):
    """Wrap angle difference tensor to (-π, π]."""
    return (d + math.pi) % TWO_PI - math.pi


def estimate_period_np(trace, min_amplitude=0.05):
    """Estimate period from positive-going zero crossings of a centered trace."""
    if len(trace) < 8:
        return math.nan

    centered = trace.astype(np.float32, copy=False) - float(np.mean(trace))
    if np.max(np.abs(centered)) < min_amplitude:
        return math.nan

    crossings = []
    for i in range(1, len(centered)):
        prev = float(centered[i - 1])
        cur = float(centered[i])
        if prev <= 0.0 < cur and cur != prev:
            frac = -prev / (cur - prev)
            crossings.append((i - 1) + frac)

    if len(crossings) < 2:
        return math.nan

    diffs = np.diff(crossings)
    diffs = diffs[np.isfinite(diffs) & (diffs >= 2.0)]
    if len(diffs) == 0:
        return math.nan

    return float(np.median(diffs))


def batch_estimate_periods(arr: np.ndarray) -> np.ndarray:
    """Per-row period estimate for a (B, T) trace matrix."""
    return np.array([estimate_period_np(row) for row in arr], dtype=np.float32)


def ordered_trace_np(buf: np.ndarray, ptr: int) -> np.ndarray:
    """Recover chronological order from a fixed-size circular buffer."""
    if ptr <= 0:
        return np.array([], dtype=np.float32)
    if ptr >= HIST:
        start = ptr % HIST
        return np.concatenate([buf[start:], buf[:start]]).astype(np.float32, copy=False)
    return np.asarray(buf[:ptr], dtype=np.float32)


def cross_corr_np(a: np.ndarray, b: np.ndarray) -> float:
    n = min(len(a), len(b))
    if n < 4:
        return 0.0
    a = np.asarray(a[:n], dtype=np.float32)
    b = np.asarray(b[:n], dtype=np.float32)
    da = a - float(np.mean(a))
    db = b - float(np.mean(b))
    denom = float(np.sqrt(np.sum(da ** 2) * np.sum(db ** 2)))
    if denom <= 1e-10:
        return 0.0
    return float(np.sum(da * db) / denom)


def signed_match_fraction_np(trace: np.ndarray, cue_sign: float, tol: float = 0.02) -> float:
    """Fraction of decisive samples whose sign matches the target cue."""
    arr = np.asarray(trace, dtype=np.float32)
    decisive = np.abs(arr) > tol
    if not np.any(decisive):
        return 0.0
    return float(np.mean(np.sign(arr[decisive]) == cue_sign))

# ── parameter catalogue ───────────────────────────────────────────────────────

PARAM_NAMES = [
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
]

PARAM_BOUNDS = {
    "W":            (0.000005, 0.18),
    "alpha":        (0.5,   0.9999),
    "beta":         (0.000005,  0.80),
    "selfEx":       (0.0001,  0.90),
    "epsilon":      (0.0001, 0.50),
    "retain":       (0.20,  0.95),
    "phaseInertia": (0.30,  8.00),
    "edgeGain":     (0.0, 20.0),
    "driveAmp":     (0.2, 5),
    "cueAmp":       (0.0, 3),
    "cycleLen":     (200.0, 500),
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

# Fixed hyperparameters — not evolved. Candidate-specific task-strength knobs
# live in PARAM_* above so search can move them per individual.
FIXED = {
    "phi":          0.00,
    "triWeight":    0.52,
    "eta":          0.00,
    "drivePer":     80,
    # Disabled for now: keep the hook but make it a no-op until we decide
    # whether programmed asymmetry is actually part of the canonical task.
    "spatialBias":  1.00,
    "warmupFrac":   0.375,
    "taskCycles":   2,
}

HIST = 200   # trace length used for fitness correlation
EFFICIENCY_WEIGHT = 0.10


# ── helpers ───────────────────────────────────────────────────────────────────

def random_params(B: int, device) -> dict:
    """Draw B random parameter vectors uniformly within PARAM_BOUNDS."""
    p = {}
    for name in PARAM_NAMES:
        lo, hi = PARAM_BOUNDS[name]
        vals = torch.rand(B, device=device) * (hi - lo) + lo
        p[name] = vals.view(B, 1, 1)
    return p


def default_params(B: int, device) -> dict:
    """B copies of the v7 default parameters."""
    p = {}
    for name in PARAM_NAMES:
        p[name] = torch.full((B, 1, 1), PARAM_DEFAULTS[name],
                             dtype=torch.float32, device=device)
    return p


def params_to_array(params: dict) -> np.ndarray:
    """(B, len(PARAM_NAMES)) numpy array from a params dict."""
    cols = [params[n].view(-1).cpu().numpy() for n in PARAM_NAMES]
    return np.stack(cols, axis=1)


def array_to_params(arr: np.ndarray, device) -> dict:
    """Inverse of params_to_array. arr: (B, len(PARAM_NAMES))."""
    p = {}
    for i, name in enumerate(PARAM_NAMES):
        p[name] = torch.tensor(arr[:, i], dtype=torch.float32,
                               device=device).view(-1, 1, 1)
    return p


def batch_cross_corr(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Pearson r between a[:,i] and b[:,i] for each batch element. Returns (B,)."""
    n = min(a.shape[1], b.shape[1])
    a = a[:, :n]; b = b[:, :n]
    ma = a.mean(dim=1, keepdim=True)
    mb = b.mean(dim=1, keepdim=True)
    da = a - ma; db = b - mb
    num   = (da * db).sum(dim=1)
    denom = torch.sqrt((da**2).sum(dim=1) * (db**2).sum(dim=1))
    return torch.where(denom > 1e-10, num / denom, torch.zeros_like(num))


def efficiency_reward_np(total_steps: np.ndarray, task_cycles: int) -> tuple[np.ndarray, np.ndarray]:
    """Softly prefer shorter simulated schedules without dominating behavior."""
    lo_cycle = max(2, int(round(PARAM_BOUNDS["cycleLen"][0])))
    hi_cycle = max(lo_cycle, int(round(PARAM_BOUNDS["cycleLen"][1])))
    lo_warmup = max(1, int(round(lo_cycle * FIXED["warmupFrac"])))
    hi_warmup = max(1, int(round(hi_cycle * FIXED["warmupFrac"])))
    lo_total = float(lo_warmup + task_cycles * lo_cycle)
    hi_total = float(hi_warmup + task_cycles * hi_cycle)
    if hi_total <= lo_total:
        norm = np.zeros_like(total_steps, dtype=np.float32)
    else:
        norm = np.clip((total_steps.astype(np.float32) - lo_total) / (hi_total - lo_total), 0.0, 1.0)
    reward = 1.0 - EFFICIENCY_WEIGHT * norm
    return reward.astype(np.float32), norm.astype(np.float32)


# ── main class ────────────────────────────────────────────────────────────────

class BatchedField:
    """
    B instances of the v7 field running in a single batched GPU pass.

    params: dict {name: (B,1,1) tensor} for the evolved parameters.
            Use random_params() or default_params() to construct.
    """

    def __init__(self, B: int, N: int = 32, device: str = "cuda", params: dict = None,
                 experiment: str = "symmetry_v1", symmetry_break: str = "spatial"):
        self.experiment, self.symmetry_break = validate_experiment(experiment, symmetry_break)
        self.B = B
        self.N = N
        self.device = torch.device(device)
        self.params = params if params is not None else default_params(B, self.device)
        self._configure_nodes()
        self.last_episode_metrics = None
        self.reset()

    def _configure_nodes(self):
        N = self.N
        mid = N // 2
        input_col = N // 4
        recv_col = input_col + 6
        offset = max(2, N // 8)
        self.input_node = (mid, input_col)
        self.output_node = (mid, recv_col)
        # These are just two fixed probe locations offset around the driven
        # column. Their historical "left/right" names are geometric only.
        self.left_input_node = (mid - offset, input_col)
        self.right_input_node = (mid + offset, input_col)
        self.left_receiver_node = (mid - offset, recv_col)
        self.right_receiver_node = (mid + offset, recv_col)
        self.probe_a_node = self.left_input_node
        self.probe_b_node = self.right_input_node

    # ── init ─────────────────────────────────────────────────────────────────

    def _z(self):
        return torch.zeros(self.B, self.N, self.N, device=self.device)

    def reset(self, base_seed: int | None = None, slot_ids: np.ndarray | None = None):
        B, N, d = self.B, self.N, self.device
        F = FIXED
        p = self.params

        baseline = 0.035
        if base_seed is None:
            angles = torch.rand(B, N, N, device=d) * TWO_PI
            noise = (torch.rand(B, N, N, device=d) - 0.5) * 0.01
            structural = 0.1 + torch.rand(B, N, N, device=d) * 0.05
        else:
            if slot_ids is None:
                slot_ids = np.arange(B, dtype=np.int64)
            angle_rows = []
            noise_rows = []
            structural_rows = []
            for slot in slot_ids:
                angle_np, noise_np, structural_np = build_initial_fields(N, base_seed, int(slot))
                angle_rows.append(angle_np)
                noise_rows.append(noise_np)
                structural_rows.append(structural_np)
            angles = torch.tensor(np.stack(angle_rows, axis=0), dtype=torch.float32, device=d)
            noise = torch.tensor(np.stack(noise_rows, axis=0), dtype=torch.float32, device=d)
            structural = torch.tensor(np.stack(structural_rows, axis=0), dtype=torch.float32, device=d)
        self.Xr = baseline * torch.cos(angles) + noise
        self.Xi = baseline * torch.sin(angles) + noise
        self.S = structural

        if self.symmetry_break == "spatial":
            # No-op while the programmed spatial asymmetry is disabled.
            self.S[:, :, :N//2] *= F["spatialBias"]

        self.R  = self._z()
        self.C  = self.R.clone()
        self.AL = p["alpha"].expand(B, N, N).clone()
        self.BL = p["beta"].expand(B, N, N).clone()
        self.ChF = self._z()
        self.ChS = self._z()
        self.Sedge   = torch.zeros(B, N, N, 8, device=d)
        self.Omega   = self._z()
        self.PrevPhi = torch.atan2(self.Xi, self.Xr)
        self.DRIVE_R = self._z()
        self.DRIVE_I = self._z()

        cycle_len = torch.round(p["cycleLen"].view(B)).to(torch.int64)
        cycle_len = torch.clamp(cycle_len, min=2)
        day_frac = torch.clamp(p["dayFrac"].view(B), min=0.05, max=0.95)
        day_len = torch.round(cycle_len.float() * day_frac).to(torch.int64)
        day_len = torch.clamp(day_len, min=1)
        day_len = torch.minimum(day_len, cycle_len - 1)
        night_len = cycle_len - day_len
        warmup_len = torch.round(cycle_len.float() * F["warmupFrac"]).to(torch.int64)
        warmup_len = torch.clamp(warmup_len, min=1)

        self.cycle_len_steps = cycle_len
        self.day_len_steps = day_len
        self.night_len_steps = night_len
        self.warmup_steps = warmup_len

        # Per-candidate cycle state.
        self.step_count          = 0
        self.drive_env           = torch.zeros(B, device=d)
        self.cycle_phase         = torch.zeros(B, dtype=torch.int64, device=d)  # 0 warmup, 1 day, 2 night
        self.cycle_step_in_phase = torch.zeros(B, dtype=torch.int64, device=d)
        self.cycle_count         = torch.zeros(B, dtype=torch.int64, device=d)

    # ── cycle ─────────────────────────────────────────────────────────────────

    def is_day(self):
        return self.cycle_phase == 1

    def is_warmup(self):
        return self.cycle_phase == 0

    def _advance_cycle(self):
        self.cycle_step_in_phase += 1
        warmup_done = (self.cycle_phase == 0) & (self.cycle_step_in_phase >= self.warmup_steps)
        self.cycle_phase = torch.where(warmup_done, torch.ones_like(self.cycle_phase), self.cycle_phase)
        self.cycle_step_in_phase = torch.where(
            warmup_done, torch.zeros_like(self.cycle_step_in_phase), self.cycle_step_in_phase
        )

        day_done = (self.cycle_phase == 1) & (self.cycle_step_in_phase >= self.day_len_steps)
        self.cycle_phase = torch.where(day_done, torch.full_like(self.cycle_phase, 2), self.cycle_phase)
        self.cycle_step_in_phase = torch.where(
            day_done, torch.zeros_like(self.cycle_step_in_phase), self.cycle_step_in_phase
        )

        night_done = (self.cycle_phase == 2) & (self.cycle_step_in_phase >= self.night_len_steps)
        self.cycle_phase = torch.where(night_done, torch.ones_like(self.cycle_phase), self.cycle_phase)
        self.cycle_step_in_phase = torch.where(
            night_done, torch.zeros_like(self.cycle_step_in_phase), self.cycle_step_in_phase
        )
        self.cycle_count = torch.where(night_done, self.cycle_count + 1, self.cycle_count)

    # ── roll ──────────────────────────────────────────────────────────────────

    def _roll(self, t, dx, dy):
        """t: (B,N,N) → shifted so result[b,y,x] == t[b,(y+dy)%N,(x+dx)%N]."""
        return torch.roll(torch.roll(t, -dy, 1), -dx, 2)

    # ── drive ─────────────────────────────────────────────────────────────────

    def _drive_phase(self):
        return TWO_PI * (self.step_count % FIXED["drivePer"]) / FIXED["drivePer"]

    def _cue_label_for_cycle(self, cycle_idx: int) -> str:
        return "A" if (cycle_idx % 2) == 0 else "B"

    def _cue_sign_for_cycle(self, cycle_idx: int) -> float:
        return 1.0 if self._cue_label_for_cycle(cycle_idx) == "A" else -1.0

    def _signal_phase(self):
        return TWO_PI * (self.step_count % FIXED["drivePer"]) / FIXED["drivePer"]

    def _gate_value(self):
        warmup = self.is_warmup()
        phase_step = self.cycle_step_in_phase.clone()
        night = self.cycle_phase == 2
        phase_step = torch.where(night, self.day_len_steps + phase_step, phase_step)
        gate = torch.sin(TWO_PI * phase_step.float() / self.cycle_len_steps.float()).clamp(min=0.0)
        return torch.where(warmup, torch.zeros_like(gate), gate)

    def _compute_drive(self):
        self.DRIVE_R.zero_()
        self.DRIVE_I.zero_()
        day_mask = self.is_day()
        ramp = torch.clamp(self.params["driveRamp"].view(self.B), min=1.0)
        ramp_update = self.drive_env + (1.0 - self.drive_env) / ramp
        self.drive_env = torch.where(day_mask, ramp_update, torch.zeros_like(self.drive_env))
        phase = self._drive_phase()
        amp   = self.params["driveAmp"].view(self.B) * self.drive_env
        r, c  = self.input_node
        self.DRIVE_R[:, r, c] = amp * math.cos(phase)
        self.DRIVE_I[:, r, c] = amp * math.sin(phase)
        if torch.any(day_mask):
            cue_amp = self.params["cueAmp"].view(self.B) * self.drive_env
            probe_a = (self.cycle_count % 2) == 0
            probe_b = ~probe_a
            ar, ac = self.probe_a_node
            br, bc = self.probe_b_node
            mask_a = day_mask & probe_a
            mask_b = day_mask & probe_b
            if torch.any(mask_a):
                self.DRIVE_R[mask_a, ar, ac] += cue_amp[mask_a] * math.cos(phase)
                self.DRIVE_I[mask_a, ar, ac] += cue_amp[mask_a] * math.sin(phase)
            if torch.any(mask_b):
                self.DRIVE_R[mask_b, br, bc] += cue_amp[mask_b] * math.cos(phase)
                self.DRIVE_I[mask_b, br, bc] += cue_amp[mask_b] * math.sin(phase)

    # ── X update ──────────────────────────────────────────────────────────────

    def _update_x(self):
        F = FIXED; p = self.params
        Xr = self.Xr; Xi = self.Xi; S = self.S; Sedge = self.Sedge

        sumR = self._z(); sumI = self._z()
        retR = self._z(); retI = self._z()
        memW = self._z()
        alignR = self._z(); alignI = self._z()
        psR = self._z();  psI = self._z()

        phi = F["phi"]
        ps  = phi * S                    # (B,N,N)
        mi  = torch.sqrt(Xr**2 + Xi**2)

        for e, (dx, dy) in enumerate(NB8):
            Xr_j = self._roll(Xr, dx, dy)
            Xi_j = self._roll(Xi, dx, dy)
            se   = Sedge[:, :, :, e]    # (B,N,N)
            wij  = p["W"] * (1.0 + p["edgeGain"] * se)

            edgePhase = ps + phi * se
            cE = torch.cos(edgePhase); sE = torch.sin(edgePhase)
            eR = cE * Xr_j - sE * Xi_j
            eI = sE * Xr_j + cE * Xi_j
            sumR += wij * eR; sumI += wij * eI
            retR += se * eR;  retI += se * eI
            memW += se

            mj   = torch.sqrt(Xr_j**2 + Xi_j**2)
            has_j = mj > 1e-6
            mi_s  = mi.clamp(min=1e-6); mj_s = mj.clamp(min=1e-6)
            uiR = torch.where(mi > 1e-6, Xr / mi_s, torch.ones_like(Xr))
            uiI = torch.where(mi > 1e-6, Xi / mi_s, torch.zeros_like(Xi))
            ujR = Xr_j / mj_s; ujI = Xi_j / mj_s
            sinD     = uiR * ujI - uiI * ujR
            amp_node = mi.clamp(min=0.05)
            w_se = (1.0 + se) * has_j.float()
            alignR += w_se * (sinD * (-uiI) * amp_node + 0.35 * (Xr_j - Xr))
            alignI += w_se * (sinD *   uiR  * amp_node + 0.35 * (Xi_j - Xi))

            psR += torch.where(has_j, Xr_j / mj_s, torch.zeros_like(Xr_j))
            psI += torch.where(has_j, Xi_j / mj_s, torch.zeros_like(Xi_j))

        an = float(len(NB8))

        # Triadic remainder — discrete vortex detection (batch version).
        # Wrap each edge difference individually; sum measures topological charge.
        triRem = self._z()
        if F["triWeight"] > 0:
            j1r = torch.roll(Xr, -1, 2); j1i = torch.roll(Xi, -1, 2)   # x+1
            j2r = torch.roll(Xr, -1, 1); j2i = torch.roll(Xi, -1, 1)   # y+1
            j3r = torch.roll(torch.roll(Xr, -1, 1), -1, 2)              # x+1,y+1
            j3i = torch.roll(torch.roll(Xi, -1, 1), -1, 2)
            p0 = torch.atan2(Xi, Xr); p1 = torch.atan2(j1i, j1r)
            p2 = torch.atan2(j2i, j2r); p3 = torch.atan2(j3i, j3r)
            l1 = (torch.abs(_wrap(p1-p0) + _wrap(p2-p1) + _wrap(p0-p2)) / TWO_PI).clamp(max=1.0)
            l2 = (torch.abs(_wrap(p3-p1) + _wrap(p2-p3) + _wrap(p1-p2)) / TWO_PI).clamp(max=1.0)
            triRem = (l1 + l2) * 0.5

        coh = torch.sqrt(psR**2 + psI**2) / an
        self.C = coh
        self.R = 0.55 * (1.0 - coh) + 0.45 * triRem
        self.ChF = 0.85 * self.ChF + 0.15 * coh
        self.ChS = 0.99 * self.ChS + 0.01 * coh

        al = self.AL.clone(); bl = self.BL
        night_mask = (~self.is_day()) & (~self.is_warmup())
        night = night_mask.view(self.B, 1, 1)

        if torch.any(night_mask):
            memNode = Sedge.max(dim=3).values   # (B,N,N)
            boosted = torch.clamp(al + p["persistAlpha"] * p["retain"] * memNode, max=0.999)
            al = torch.where(night, boosted, al)

        selfBoost   = p["selfEx"] * coh
        alignScale  = p["kAlign"] / an
        retainScale = torch.where(night, p["retain"], torch.zeros_like(p["retain"]))

        nr = (al * Xr + sumR * (1.0 + selfBoost)
              + alignScale * alignR + retainScale * retR
              - bl * self.R * Xr + self.DRIVE_R)
        ni = (al * Xi + sumI * (1.0 + selfBoost)
              + alignScale * alignI + retainScale * retI
              - bl * self.R * Xi + self.DRIVE_I)

        if torch.any(night_mask):
            memNode = Sedge.max(dim=3).values
            memAvg  = torch.maximum(memNode, memW / an)
            rg      = p["phaseInertia"] * p["retain"] * memAvg
            # Preserve learned angular velocity; memory strength gates replay
            # participation instead of scaling the frequency itself.
            adv     = p["phaseInertia"] * self.Omega
            sig     = rg > 1e-6
            ca = torch.cos(adv); sa = torch.sin(adv)
            tr = nr; ti = ni
            nr = torch.where(sig, ca * tr - sa * ti, tr)
            ni = torch.where(sig, sa * tr + ca * ti, ti)

        day_mask = self.is_day()
        if torch.any(day_mask):
            clamp = p["driveClamp"].view(self.B)
            r, c = self.input_node
            day_nr = (1.0 - clamp) * nr[:, r, c] + clamp * self.DRIVE_R[:, r, c]
            day_ni = (1.0 - clamp) * ni[:, r, c] + clamp * self.DRIVE_I[:, r, c]
            nr[:, r, c] = torch.where(day_mask, day_nr, nr[:, r, c])
            ni[:, r, c] = torch.where(day_mask, day_ni, ni[:, r, c])

        m2 = nr**2 + ni**2
        sc = torch.where(m2 > 4.0, 2.0 / torch.sqrt(m2.clamp(min=1e-10)),
                         torch.ones_like(m2))
        self.Xr = nr * sc; self.Xi = ni * sc

    # ── phase memory ──────────────────────────────────────────────────────────

    def _update_phase_memory(self):
        F = FIXED; p = self.params
        Xr = self.Xr; Xi = self.Xi
        ph  = torch.atan2(Xi, Xr)
        d   = ((ph - self.PrevPhi + math.pi) % TWO_PI) - math.pi
        self.PrevPhi = ph
        amp = torch.sqrt(Xr**2 + Xi**2)
        mem = self.Sedge.max(dim=3).values
        dph = self._drive_phase()
        drive_period = FIXED["drivePer"]
        drive_lock = torch.where(
            amp > 1e-6,
            (Xr * math.cos(dph) + Xi * math.sin(dph)) / amp.clamp(min=1e-6),
            torch.zeros_like(Xr)
        )
        learn = torch.clamp(p["omegaLearn"], min=0.0)
        day_mask = self.is_day().view(self.B, 1, 1)
        warmup_mask = self.is_warmup().view(self.B, 1, 1)
        active_day = day_mask & (~warmup_mask)
        night_mask = (~day_mask) & (~warmup_mask)
        gate         = torch.clamp(amp / 0.12, max=1.0) * torch.maximum(torch.abs(drive_lock), mem)
        drive_omega  = TWO_PI / max(1, drive_period)
        target_omega = 0.55 * d + 0.45 * drive_omega
        learned = (1.0 - learn * gate) * self.Omega + (learn * gate) * target_omega
        self.Omega = torch.where(active_day, learned, self.Omega)
        self.Omega = torch.where(night_mask, self.Omega * 0.998, self.Omega)

    # ── S update ──────────────────────────────────────────────────────────────

    def _update_s(self):
        F = FIXED; p = self.params
        S = self.S; C = self.C; R = self.R
        maxC = torch.zeros_like(C); maxS = S.clone()
        for dx, dy in NB4:
            C_j = self._roll(C, dx, dy); S_j = self._roll(S, dx, dy)
            better = C_j > maxC
            maxC = torch.where(better, C_j, maxC)
            maxS = torch.where(better, S_j, maxS)
        self.S = torch.clamp(
            (1.0 - p["epsilon"]) * S + p["epsilon"] * (C - R) + 0.02 * (maxS - S),
            min=0.001, max=1.0
        )

    # ── Sedge update ──────────────────────────────────────────────────────────

    def _update_sedge(self):
        F = FIXED; p = self.params
        Xr = self.Xr; Xi = self.Xi
        forgetting = p["edgeDecay"].view(self.B, 1, 1, 1)
        day_mask = self.is_day().view(self.B, 1, 1)
        anneal     = (1.0 / (1.0 + self.cycle_count.float() * 0.12)).view(self.B, 1, 1)
        dph        = self._drive_phase()

        ai = torch.sqrt(Xr**2 + Xi**2)
        pi_ = torch.atan2(Xi, Xr)
        driveI = torch.where(
            ai > 1e-6,
            torch.abs((Xr * math.cos(dph) + Xi * math.sin(dph)) / ai.clamp(min=1e-6)),
            torch.zeros_like(ai)
        )
        old      = self.Sedge.clone()
        new_edge = old * (1.0 - forgetting)

        for e, (dx, dy) in enumerate(NB8):
            Xr_j = self._roll(Xr, dx, dy); Xi_j = self._roll(Xi, dx, dy)
            aj   = torch.sqrt(Xr_j**2 + Xi_j**2)
            pj   = torch.atan2(Xi_j, Xr_j)
            coh01    = 0.5 * (torch.cos(pj - pi_) + 1.0)
            driveJ   = torch.where(
                aj > 1e-6,
                torch.abs((Xr_j * math.cos(dph) + Xi_j * math.sin(dph)) / aj.clamp(min=1e-6)),
                torch.zeros_like(aj)
            )
            ampGate   = torch.clamp((ai * aj) / 0.04, max=1.0)
            driveGate = driveI * driveJ * ampGate
            rem       = (1.0 - coh01) + 0.10 * torch.abs(ai - aj)
            plastic   = p["epsilon"] * anneal * day_mask.float() * (1.0 - old[:, :, :, e]) * driveGate
            new_edge[:, :, :, e] = torch.clamp(
                new_edge[:, :, :, e] + plastic * (coh01 - rem - 0.03 * old[:, :, :, e]),
                min=0.0, max=1.0
            )
        self.Sedge = new_edge

    # ── homeostasis ───────────────────────────────────────────────────────────

    def _update_homeostasis(self):
        F = FIXED; p = self.params
        tau_c = p["tauC"]
        fast_err = self.ChF - tau_c
        slow_err = self.ChS - tau_c
        agree    = fast_err * slow_err > 0
        eta_eff  = F["eta"] * (1.0 + 5.0 * fast_err**2)
        self.AL = torch.where(agree,
                              torch.clamp(self.AL - eta_eff * fast_err * 0.5, min=0.88, max=0.995),
                              self.AL)
        self.BL = torch.where(agree,
                              torch.clamp(self.BL + eta_eff * fast_err * 1.0, min=0.02, max=0.5),
                              self.BL)

    # ── single step ───────────────────────────────────────────────────────────

    def step(self):
        self._compute_drive()
        self._update_x()
        self._update_phase_memory()
        if self.step_count % 10 == 0:
            self._update_s()
            self._update_sedge()
        if self.step_count % 100 == 0:
            self._update_homeostasis()
        self._advance_cycle()
        self.step_count += 1

    # ── episode runner ────────────────────────────────────────────────────────

    @torch.no_grad()
    def run_episode(self, base_seed: int | None = None, slot_ids: np.ndarray | None = None,
                    task_cycles: int | None = None) -> torch.Tensor:
        """
        Reset → warmup → day → night.
        Returns fitness: (B,) tensor on self.device.
        """
        F = FIXED
        self.reset(base_seed=base_seed, slot_ids=slot_ids)
        B = self.B; d = self.device
        task_cycles = int(F.get("taskCycles", 1) if task_cycles is None else task_cycles)

        # Buffers for replay and symmetry diagnostics.
        or_, oc = self.output_node
        lr, lc = self.left_receiver_node
        rr, rc = self.right_receiver_node
        day_buf = torch.zeros(B, task_cycles, HIST, device=d)
        night_buf = torch.zeros(B, task_cycles, HIST, device=d)
        left_day = torch.zeros(B, task_cycles, HIST, device=d)
        right_day = torch.zeros(B, task_cycles, HIST, device=d)
        left_night = torch.zeros(B, task_cycles, HIST, device=d)
        right_night = torch.zeros(B, task_cycles, HIST, device=d)
        day_ptr = torch.zeros(B, task_cycles, dtype=torch.int64, device=d)
        night_ptr = torch.zeros(B, task_cycles, dtype=torch.int64, device=d)

        total_steps = self.warmup_steps + task_cycles * self.cycle_len_steps
        max_total = int(total_steps.max().item())
        total_steps_np = total_steps.cpu().numpy().astype(np.float32, copy=False)
        efficiency_reward, step_cost = efficiency_reward_np(total_steps_np, task_cycles)

        for _ in range(max_total):
            active = self.cycle_count < task_cycles
            if not torch.any(active):
                break

            was_day = self.is_day()
            was_warmup = self.is_warmup()
            cycle_idx = torch.clamp(self.cycle_count, max=task_cycles - 1)
            self.step()
            ov = self.Xr[:, or_, oc]   # (B,)
            left_mag = torch.sqrt(self.Xr[:, lr, lc] ** 2 + self.Xi[:, lr, lc] ** 2)
            right_mag = torch.sqrt(self.Xr[:, rr, rc] ** 2 + self.Xi[:, rr, rc] ** 2)

            for cycle in range(task_cycles):
                day_mask = active & was_day & (~was_warmup) & (cycle_idx == cycle)
                if torch.any(day_mask):
                    idxs = torch.nonzero(day_mask, as_tuple=False).squeeze(1)
                    ptrs = torch.remainder(day_ptr[idxs, cycle], HIST)
                    day_buf[idxs, cycle, ptrs] = ov[idxs]
                    left_day[idxs, cycle, ptrs] = left_mag[idxs]
                    right_day[idxs, cycle, ptrs] = right_mag[idxs]
                    day_ptr[idxs, cycle] += 1

                night_mask = (
                    active
                    & (~was_day)
                    & (~was_warmup)
                    & (cycle_idx == cycle)
                    & (night_ptr[:, cycle] < HIST)
                )
                if torch.any(night_mask):
                    idxs = torch.nonzero(night_mask, as_tuple=False).squeeze(1)
                    ptrs = night_ptr[idxs, cycle]
                    night_buf[idxs, cycle, ptrs] = ov[idxs]
                    left_night[idxs, cycle, ptrs] = left_mag[idxs]
                    right_night[idxs, cycle, ptrs] = right_mag[idxs]
                    night_ptr[idxs, cycle] += 1

        day_buf_np = day_buf.cpu().numpy()
        night_buf_np = night_buf.cpu().numpy()
        left_day_np = left_day.cpu().numpy()
        right_day_np = right_day.cpu().numpy()
        left_night_np = left_night.cpu().numpy()
        right_night_np = right_night.cpu().numpy()
        day_ptr_np = day_ptr.cpu().numpy()
        night_ptr_np = night_ptr.cpu().numpy()

        if self.experiment == "symmetry_v1":
            cycle_scores = np.zeros((task_cycles, B), dtype=np.float32)
            cycle_choice_strength = np.full((task_cycles, B), np.nan, dtype=np.float32)
            cycle_choice_consistency = np.full((task_cycles, B), np.nan, dtype=np.float32)
            cycle_overnight_persistence = np.zeros((task_cycles, B), dtype=np.float32)
            cycle_switch_penalty = np.full((task_cycles, B), np.nan, dtype=np.float32)

            for b in range(B):
                for cycle_idx in range(task_cycles):
                    left_day_ordered = ordered_trace_np(left_day_np[b, cycle_idx], int(day_ptr_np[b, cycle_idx]))
                    right_day_ordered = ordered_trace_np(right_day_np[b, cycle_idx], int(day_ptr_np[b, cycle_idx]))
                    left_night_filled = np.asarray(
                        left_night_np[b, cycle_idx, :int(min(night_ptr_np[b, cycle_idx], HIST))], dtype=np.float32
                    )
                    right_night_filled = np.asarray(
                        right_night_np[b, cycle_idx, :int(min(night_ptr_np[b, cycle_idx], HIST))], dtype=np.float32
                    )

                    if len(left_day_ordered) < 4 or len(right_day_ordered) < 4:
                        cycle_scores[cycle_idx, b] = 0.0
                        continue

                    cue_sign = self._cue_sign_for_cycle(cycle_idx)
                    day_dom = (left_day_ordered - right_day_ordered) / np.maximum(
                        left_day_ordered + right_day_ordered, 1e-6
                    )
                    mean_dom = float(np.mean(day_dom))
                    choice_strength = max(0.0, cue_sign * mean_dom)
                    choice_consistency = signed_match_fraction_np(day_dom, cue_sign)

                    if len(left_night_filled) > 0 and len(right_night_filled) > 0:
                        night_dom = (left_night_filled - right_night_filled) / np.maximum(
                            left_night_filled + right_night_filled, 1e-6
                        )
                        overnight_persistence = signed_match_fraction_np(night_dom, cue_sign)
                        combined = np.concatenate([day_dom, night_dom])
                    else:
                        overnight_persistence = 0.0
                        combined = day_dom

                    signs = np.sign(combined)
                    signs = signs[np.abs(combined) > 0.02]
                    if len(signs) < 2:
                        switch_penalty = 0.0
                    else:
                        switch_penalty = float(np.mean(signs[1:] != signs[:-1]))

                    cycle_choice_strength[cycle_idx, b] = choice_strength
                    cycle_choice_consistency[cycle_idx, b] = choice_consistency
                    cycle_overnight_persistence[cycle_idx, b] = overnight_persistence
                    cycle_switch_penalty[cycle_idx, b] = switch_penalty
                    cycle_scores[cycle_idx, b] = (
                        choice_strength
                        * choice_consistency
                        * overnight_persistence
                        * max(0.0, 1.0 - switch_penalty)
                    )

            base_fitness = cycle_scores.mean(axis=0)
            a_mask = np.array([self._cue_label_for_cycle(i) == "A" for i in range(task_cycles)], dtype=bool)
            b_mask = ~a_mask
            if np.any(a_mask) and np.any(b_mask):
                a_mean = cycle_scores[a_mask].mean(axis=0)
                b_mean = cycle_scores[b_mask].mean(axis=0)
                denom = np.maximum(a_mean + b_mean, 1e-6)
                parity = np.clip(2.0 * np.minimum(a_mean, b_mean) / denom, 0.0, 1.0)
                parity_fitness = base_fitness * parity
            else:
                a_mean = np.ones(B, dtype=np.float32)
                b_mean = np.ones(B, dtype=np.float32)
                parity = np.ones(B, dtype=np.float32)
                parity_fitness = base_fitness

            fitness = parity_fitness * efficiency_reward

            fitness_t = torch.tensor(fitness, dtype=torch.float32, device=d)
            self.last_episode_metrics = {
                "choice_strength": cycle_choice_strength[-1],
                "choice_consistency": cycle_choice_consistency[-1],
                "overnight_persistence": cycle_overnight_persistence[-1],
                "switch_penalty": cycle_switch_penalty[-1],
                "cue_label": self._cue_label_for_cycle(task_cycles - 1),
                "cue_sequence": " -> ".join(self._cue_label_for_cycle(i) for i in range(task_cycles)),
                "cycle_scores": cycle_scores,
                "cue_parity": parity,
                "a_mean": a_mean,
                "b_mean": b_mean,
                "behavior_fitness": base_fitness,
                "parity_fitness": parity_fitness,
                "efficiency_reward": efficiency_reward,
                "normalized_step_cost": step_cost,
                "total_steps": total_steps_np,
                "fitness": fitness,
            }
            return fitness_t

        corr = np.zeros(B, dtype=np.float32)
        retention = np.zeros(B, dtype=np.float32)
        day_period = np.full(B, np.nan, dtype=np.float32)
        night_period = np.full(B, np.nan, dtype=np.float32)
        ratio = np.full(B, np.nan, dtype=np.float32)
        faithfulness = np.full(B, np.nan, dtype=np.float32)

        for b in range(B):
            day_ordered = np.array([], dtype=np.float32)
            night_filled = np.array([], dtype=np.float32)
            for cycle_idx in range(task_cycles):
                if day_ptr_np[b, cycle_idx] > 0:
                    day_ordered = ordered_trace_np(day_buf_np[b, cycle_idx], int(day_ptr_np[b, cycle_idx]))
                    night_filled = np.asarray(
                        night_buf_np[b, cycle_idx, :int(min(night_ptr_np[b, cycle_idx], HIST))],
                        dtype=np.float32,
                    )
                    break

            corr[b] = max(0.0, cross_corr_np(day_ordered, night_filled))
            if len(day_ordered) > 0:
                day_rms = float(np.sqrt(np.mean(day_ordered ** 2)))
            else:
                day_rms = 0.0
            if len(night_filled) > 0:
                night_rms = float(np.sqrt(np.mean(night_filled ** 2)))
            else:
                night_rms = 0.0
            retention[b] = min(2.0, night_rms / (day_rms + 1e-4))

            day_period[b] = estimate_period_np(day_ordered)
            night_period[b] = estimate_period_np(night_filled)
            if np.isfinite(day_period[b]) and np.isfinite(night_period[b]) and day_period[b] > 0:
                ratio[b] = night_period[b] / day_period[b]
                faithfulness[b] = min(ratio[b], 1.0 / max(ratio[b], 1e-6))

        faithfulness_reward = np.nan_to_num(faithfulness, nan=0.0, posinf=0.0, neginf=0.0)
        behavior_fitness = corr * retention * faithfulness_reward
        fitness = behavior_fitness * efficiency_reward
        fitness_t = torch.tensor(fitness, dtype=torch.float32, device=d)
        self.last_episode_metrics = {
            "corr": corr,
            "retention": retention,
            "day_period": day_period,
            "night_period": night_period,
            "period_ratio": ratio,
            "frequency_faithfulness": faithfulness,
            "frequency_reward": faithfulness_reward,
            "behavior_fitness": behavior_fitness,
            "efficiency_reward": efficiency_reward,
            "normalized_step_cost": step_cost,
            "total_steps": total_steps_np,
            "fitness": fitness,
        }

        return fitness_t
