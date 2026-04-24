"""
batched_field.py — B instances of Field Dynamics v7 running in parallel.

All field tensors are (B, N, N) instead of (N, N).
Sedge is (B, N, N, 8).
Evolved parameters are (B, 1, 1) tensors so they broadcast over the grid.

All instances share the same cycle phase (warmup → day → night) and the
same input/output node positions, so the batch dimension is purely a
population-level parallelism — every individual sees the same task.

Fitness returned by run_episode():
    fitness = peak_corr * clamp(night_rms / (day_rms + 1e-4), max=2)

  peak_corr : best Pearson r between last-HIST day output and first-HIST night output
  night_rms / day_rms : signal-retention ratio — rewards keeping amplitude alive at night
"""

import math
import torch
import numpy as np

TWO_PI = 2.0 * math.pi

NB8 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
NB4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _wrap(d):
    """Wrap angle difference tensor to (-π, π]."""
    return (d + math.pi) % TWO_PI - math.pi

# ── parameter catalogue ───────────────────────────────────────────────────────

PARAM_NAMES = ["W", "alpha", "beta", "selfEx", "epsilon", "retain", "phaseInertia"]

PARAM_BOUNDS = {
    "W":            (0.010, 0.18),
    "alpha":        (0.82,  0.97),
    "beta":         (0.10,  0.80),
    "selfEx":       (0.01,  0.20),
    "epsilon":      (0.005, 0.10),
    "retain":       (0.20,  0.95),
    "phaseInertia": (0.30,  3.50),
}

PARAM_DEFAULTS = {
    "W":            0.0325,
    "alpha":        0.843,
    "beta":         0.485,
    "selfEx":       0.06,
    "epsilon":      0.035,
    "retain":       0.60,
    "phaseInertia": 1.25,
}

# Fixed hyperparameters — not evolved
FIXED = {
    "kAlign":       0.43,
    "edgeGain":     8.00,
    "persistAlpha": 0.28,
    "omegaLearn":   0.12,
    "edgeDecay":    0.0008,
    "phi":          0.00,
    "triWeight":    0.52,
    "eta":          0.00,
    "tauC":         0.45,
    "driveAmp":     1.00,
    "drivePer":     80,
    "driveRamp":    32,
    "dayLen":       400,
    "nightLen":     400,
    "warmup":       300,
}

HIST = 200   # trace length used for fitness correlation


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


# ── main class ────────────────────────────────────────────────────────────────

class BatchedField:
    """
    B instances of the v7 field running in a single batched GPU pass.

    params: dict {name: (B,1,1) tensor} for the 7 evolved parameters.
            Use random_params() or default_params() to construct.
    """

    def __init__(self, B: int, N: int = 32, device: str = "cuda", params: dict = None):
        self.B = B
        self.N = N
        self.device = torch.device(device)
        self.params = params if params is not None else default_params(B, self.device)
        self.input_node  = (N // 2, N // 4)
        self.output_node = (N // 2, N // 4 + 4)
        self.reset()

    # ── init ─────────────────────────────────────────────────────────────────

    def _z(self):
        return torch.zeros(self.B, self.N, self.N, device=self.device)

    def reset(self):
        B, N, d = self.B, self.N, self.device
        F = FIXED
        p = self.params

        baseline = 0.035
        angles = torch.rand(B, N, N, device=d) * TWO_PI
        noise  = (torch.rand(B, N, N, device=d) - 0.5) * 0.01
        self.Xr = baseline * torch.cos(angles) + noise
        self.Xi = baseline * torch.sin(angles) + noise
        self.S   = 0.1 + torch.rand(B, N, N, device=d) * 0.05

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

        # cycle state — scalar, shared across all B instances
        self.step_count          = 0
        self.drive_env           = 0.0
        self.cycle_mode          = "warmup"
        self.cycle_step_in_phase = 0
        self.cycle_count         = 0

    # ── cycle ─────────────────────────────────────────────────────────────────

    def is_day(self):
        m = self.cycle_mode
        return m not in ("warmup", "night", "forcenight")

    def is_warmup(self):
        return self.cycle_mode == "warmup"

    def _advance_cycle(self):
        F = FIXED
        self.cycle_step_in_phase += 1
        if self.cycle_mode == "warmup":
            if self.cycle_step_in_phase >= F["warmup"]:
                self.cycle_mode = "day"; self.cycle_step_in_phase = 0
        elif self.cycle_mode == "day":
            if self.cycle_step_in_phase >= F["dayLen"]:
                self.cycle_mode = "night"; self.cycle_step_in_phase = 0
        elif self.cycle_mode == "night":
            if self.cycle_step_in_phase >= F["nightLen"]:
                self.cycle_mode = "day"; self.cycle_step_in_phase = 0
                self.cycle_count += 1

    # ── roll ──────────────────────────────────────────────────────────────────

    def _roll(self, t, dx, dy):
        """t: (B,N,N) → shifted so result[b,y,x] == t[b,(y+dy)%N,(x+dx)%N]."""
        return torch.roll(torch.roll(t, -dy, 1), -dx, 2)

    # ── drive ─────────────────────────────────────────────────────────────────

    def _drive_phase(self):
        return TWO_PI * (self.step_count % FIXED["drivePer"]) / FIXED["drivePer"]

    def _compute_drive(self):
        self.DRIVE_R.zero_()
        self.DRIVE_I.zero_()
        if self.is_day():
            ramp = max(1, FIXED["driveRamp"])
            self.drive_env += (1.0 - self.drive_env) / ramp
        else:
            self.drive_env = 0.0
        phase = self._drive_phase()
        amp   = FIXED["driveAmp"] * self.drive_env
        r, c  = self.input_node
        self.DRIVE_R[:, r, c] = amp * math.cos(phase)
        self.DRIVE_I[:, r, c] = amp * math.sin(phase)

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
            wij  = p["W"] * (1.0 + F["edgeGain"] * se)

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
        night = not self.is_day() and not self.is_warmup()

        if night:
            memNode = Sedge.max(dim=3).values   # (B,N,N)
            al = torch.clamp(al + F["persistAlpha"] * p["retain"] * memNode, max=0.999)

        selfBoost   = p["selfEx"] * coh
        alignScale  = F["kAlign"] / an
        retainScale = p["retain"] if night else 0.0

        nr = (al * Xr + sumR * (1.0 + selfBoost)
              + alignScale * alignR + retainScale * retR
              - bl * self.R * Xr + self.DRIVE_R)
        ni = (al * Xi + sumI * (1.0 + selfBoost)
              + alignScale * alignI + retainScale * retI
              - bl * self.R * Xi + self.DRIVE_I)

        if night:
            memNode = Sedge.max(dim=3).values
            memAvg  = torch.maximum(memNode, memW / an)
            rg      = p["phaseInertia"] * p["retain"] * memAvg
            adv     = rg * self.Omega
            sig     = torch.abs(adv) > 1e-6
            ca = torch.cos(adv); sa = torch.sin(adv)
            tr = nr; ti = ni
            nr = torch.where(sig, ca * tr - sa * ti, tr)
            ni = torch.where(sig, sa * tr + ca * ti, ti)

        if self.is_day():
            r, c = self.input_node
            nr[:, r, c] = 0.15 * nr[:, r, c] + 0.85 * self.DRIVE_R[:, r, c]
            ni[:, r, c] = 0.15 * ni[:, r, c] + 0.85 * self.DRIVE_I[:, r, c]

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
        drive_lock = torch.where(
            amp > 1e-6,
            (Xr * math.cos(dph) + Xi * math.sin(dph)) / amp.clamp(min=1e-6),
            torch.zeros_like(Xr)
        )
        learn = max(0.0, F["omegaLearn"])
        if self.is_day() and not self.is_warmup():
            gate         = torch.clamp(amp / 0.12, max=1.0) * torch.maximum(torch.abs(drive_lock), mem)
            drive_omega  = TWO_PI / max(1, F["drivePer"])
            target_omega = 0.55 * d + 0.45 * drive_omega
            self.Omega   = (1.0 - learn * gate) * self.Omega + (learn * gate) * target_omega
        elif not self.is_warmup():
            self.Omega = self.Omega * 0.998

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
        forgetting = F["edgeDecay"]
        train      = self.is_day() and not self.is_warmup() and True
        anneal     = 1.0 / (1.0 + self.cycle_count * 0.12)
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

        if train:
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
                plastic   = p["epsilon"] * anneal * (1.0 - old[:, :, :, e]) * driveGate
                new_edge[:, :, :, e] = torch.clamp(
                    new_edge[:, :, :, e] + plastic * (coh01 - rem - 0.03 * old[:, :, :, e]),
                    min=0.0, max=1.0
                )
        self.Sedge = new_edge

    # ── homeostasis ───────────────────────────────────────────────────────────

    def _update_homeostasis(self):
        F = FIXED; p = self.params
        fast_err = self.ChF - F["tauC"]
        slow_err = self.ChS - F["tauC"]
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
    def run_episode(self) -> torch.Tensor:
        """
        Reset → warmup → day → night.
        Returns fitness: (B,) tensor on self.device.
        """
        F = FIXED
        self.reset()
        B = self.B; d = self.device

        # Buffers for correlation: last HIST steps of day, first HIST of night
        day_buf   = torch.zeros(B, HIST, device=d)
        night_buf = torch.zeros(B, HIST, device=d)
        day_ptr   = 0    # circular write pointer into day_buf
        night_ptr = 0    # linear write pointer into night_buf
        or_, oc   = self.output_node

        total = F["warmup"] + F["dayLen"] + F["nightLen"]

        for _ in range(total):
            self.step()
            ov = self.Xr[:, or_, oc]   # (B,)

            if self.cycle_mode == "day":
                day_buf[:, day_ptr % HIST] = ov
                day_ptr += 1

            elif self.cycle_mode == "night" and night_ptr < HIST:
                night_buf[:, night_ptr] = ov
                night_ptr += 1

        # Re-order day_buf so newest entry is at index HIST-1
        if day_ptr >= HIST:
            start = day_ptr % HIST
            day_ordered = torch.cat([day_buf[:, start:], day_buf[:, :start]], dim=1)
        else:
            day_ordered = day_buf[:, :day_ptr] if day_ptr > 0 else day_buf

        night_filled = night_buf[:, :max(night_ptr, 1)]

        corr     = batch_cross_corr(day_ordered, night_filled).clamp(min=0.0)
        day_rms  = day_ordered.pow(2).mean(dim=1).sqrt()
        night_rms = night_filled.pow(2).mean(dim=1).sqrt()
        retention = (night_rms / (day_rms + 1e-4)).clamp(max=2.0)
        fitness   = corr * retention

        return fitness
