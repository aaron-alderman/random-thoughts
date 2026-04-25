"""
Field Dynamics v7 — Python/PyTorch port of field-dynamics-v7-phasepersist-experiment.js

Faithful translation of the JS engine.  All field buffers are 2D tensors (N, N)
instead of flat Float32Arrays.  Indexing convention: tensor[row, col] == tensor[y, x].

Roll convention: _roll_neighbor(t, dx, dy)[y, x] == t[(y+dy)%N, (x+dx)%N]
  achieved by: torch.roll(torch.roll(t, -dy, 0), -dx, 1)
"""

import math
import torch
import numpy as np
from experiment_paths import validate_experiment

TWO_PI = 2.0 * math.pi

# 8-connected neighbours: (dx, dy) in (col, row) convention matching JS nb8
NB8 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
NB4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _wrap(d):
    """Wrap angle difference tensor to (-π, π]."""
    return (d + math.pi) % TWO_PI - math.pi


def _estimate_period(trace, min_amplitude=0.05):
    """Estimate period from positive-going zero crossings of a centered trace."""
    if len(trace) < 8:
        return math.nan

    arr = np.asarray(trace, dtype=np.float32)
    centered = arr - arr.mean()
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


class FieldDynamics:
    def __init__(self, N=32, device="cpu", **param_overrides):
        experiment = param_overrides.pop("experiment", "symmetry_v1")
        symmetry_break = param_overrides.pop("symmetry_break", "spatial")
        self.experiment, self.symmetry_break = validate_experiment(experiment, symmetry_break)
        self.N = N
        self.device = torch.device(device)

        self.P = {
            "alpha":        0.843,
            "W":            0.0325,
            "kAlign":       0.43,
            "edgeGain":     8.00,
            "retain":       0.60,
            "phaseInertia": 1.25,
            "persistAlpha": 0.28,
            "omegaLearn":   0.12,
            "edgeDecay":    0.0008,
            "beta":         0.485,
            "phi":          0.00,
            "triWeight":    0.52,
            "selfEx":       0.06,
            "epsilon":      0.035,
            "eta":          0.00,
            "tauC":         0.45,
            "driveAmp":     1.00,
            "drivePer":     80,
            "driveRamp":    32,
            "gatePer":      800,
            "signalPer":    80,
            "signalAmp":    1.00,
            "spatialBias":  1.06,
            "dayLen":       400,
            "nightLen":     400,
            "corrThr":      0.5,
            "warmup":       300,
        }
        self.P.update(param_overrides)
        self.reset()

    # ── helpers ──────────────────────────────────────────────────────────────

    def _z(self):
        return torch.zeros(self.N, self.N, device=self.device)

    def _roll(self, t, dx, dy):
        """t[y,x] → neighbour at (x+dx, y+dy) seen from each (y,x)."""
        return torch.roll(torch.roll(t, -dy, 0), -dx, 1)

    # ── initialisation ───────────────────────────────────────────────────────

    def reset(self):
        N, d = self.N, self.device
        P = self.P

        baseline = 0.035
        angles = torch.rand(N, N, device=d) * TWO_PI
        noise  = (torch.rand(N, N, device=d) - 0.5) * 0.01

        self.Xr = baseline * torch.cos(angles) + noise
        self.Xi = baseline * torch.sin(angles) + noise
        self.S  = 0.1 + torch.rand(N, N, device=d) * 0.05

        if self.symmetry_break == "spatial":
            # Match the search-time initialization so live runs and searched
            # genomes share the same built-in symmetry bias.
            self.S[:, :N//2] *= P["spatialBias"]

        self.R  = self._z()
        self.C  = self._z()

        self.AL = torch.full((N, N), P["alpha"], device=d)
        self.BL = torch.full((N, N), P["beta"],  device=d)

        self.ChF = self._z()   # fast coherence history  (τ ≈ 7 steps)
        self.ChS = self._z()   # slow coherence history  (τ ≈ 100 steps)

        self.Sedge = torch.zeros(N, N, 8, device=d)   # directional edge memory

        self.Omega     = self._z()                         # learned angular velocity
        self.PrevPhi   = torch.atan2(self.Xi, self.Xr)
        self.PhaseDelta = self._z()
        self.DriveLock  = self._z()
        self.ReplayMem  = self._z()
        self.ReplayGain = self._z()
        self.ReplayAdv  = self._z()

        self.DRIVE_R = self._z()
        self.DRIVE_I = self._z()

        # cycle state
        self.step                = 0
        self.drive_env           = 0.0
        self.cycle_mode          = "warmup"   # warmup | day | night | forceday | forcenight
        self.cycle_step_in_phase = 0
        self.cycle_count         = 0
        self.warmup_done         = False

        # node positions as (row, col) == (y, x)
        self._configure_nodes()

        # signal histories (Python lists)
        self.HIST_LEN             = 200
        self.input_history        = []
        self.output_history       = []
        self.output_imag_history  = []
        self.output_mag_history   = []
        self.output_day_history   = []
        self.output_day_imag_history = []
        self.output_day_mag_history  = []
        self.output_night_history = []
        self.output_night_imag_history = []
        self.output_night_mag_history  = []
        self.dwell_steps = 0
        self.best_dwell  = 0
        self.peak_corr   = 0.0
        self.corr_value  = 0.0
        self.day_period_est = math.nan
        self.night_period_est = math.nan
        self.replay_period_ratio = math.nan
        self.frequency_faithfulness = math.nan
        self.left_basin_history = []
        self.right_basin_history = []
        self.left_day_history = []
        self.right_day_history = []
        self.left_night_history = []
        self.right_night_history = []
        self.choice_strength = math.nan
        self.choice_consistency = math.nan
        self.overnight_persistence = math.nan
        self.switch_penalty = math.nan
        self.symmetry_fitness = math.nan
        self.chosen_basin = "none"
        self.current_dominance = 0.0
        self.gate_value = 0.0
        self.signal_phase = 0.0

    def _configure_nodes(self):
        N = self.N
        mid = N // 2
        input_col = N // 4
        recv_col = input_col + 6
        offset = max(2, N // 8)

        self.input_node = (mid, input_col)
        self.output_node = (mid, recv_col)
        self.left_input_node = (mid - offset, input_col)
        self.right_input_node = (mid + offset, input_col)
        self.left_receiver_node = (mid - offset, recv_col)
        self.right_receiver_node = (mid + offset, min(N - 2, recv_col + 1))

    # ── cycle ────────────────────────────────────────────────────────────────

    def is_day(self):
        m = self.cycle_mode
        if m == "warmup":     return False
        if m == "forceday":   return True
        if m == "forcenight": return False
        return m == "day"

    def is_warmup(self):
        return self.cycle_mode == "warmup"

    def advance_cycle(self):
        if self.cycle_mode in ("forceday", "forcenight"):
            return
        self.cycle_step_in_phase += 1

        if self.cycle_mode == "warmup":
            if self.cycle_step_in_phase >= self.P["warmup"]:
                self.cycle_mode = "day"
                self.cycle_step_in_phase = 0
                self.warmup_done = True
                self._on_day_start()
            return

        if self.cycle_mode == "day" and self.cycle_step_in_phase >= self.P["dayLen"]:
            self.cycle_mode = "night"
            self.cycle_step_in_phase = 0
            self._on_night_start()
        elif self.cycle_mode == "night" and self.cycle_step_in_phase >= self.P["nightLen"]:
            self.cycle_mode = "day"
            self.cycle_step_in_phase = 0
            self.cycle_count += 1
            self._on_day_start()

    def _on_day_start(self):
        self.output_day_history.clear()
        self.output_day_imag_history.clear()
        self.output_day_mag_history.clear()
        self.output_night_history.clear()
        self.output_night_imag_history.clear()
        self.output_night_mag_history.clear()
        self.left_basin_history.clear()
        self.right_basin_history.clear()
        self.left_day_history.clear()
        self.right_day_history.clear()
        self.left_night_history.clear()
        self.right_night_history.clear()
        self.dwell_steps = 0
        self.peak_corr   = 0.0
        self.corr_value  = 0.0
        self.choice_strength = math.nan
        self.choice_consistency = math.nan
        self.overnight_persistence = math.nan
        self.switch_penalty = math.nan
        self.symmetry_fitness = math.nan
        self.chosen_basin = "none"
        self.current_dominance = 0.0

    def _on_night_start(self):
        self.output_night_history.clear()
        self.output_night_imag_history.clear()
        self.output_night_mag_history.clear()
        self.left_night_history.clear()
        self.right_night_history.clear()
        self.dwell_steps = 0
        self.peak_corr   = 0.0
        self.corr_value  = 0.0

    # ── drive ─────────────────────────────────────────────────────────────────

    def _current_drive_phase(self):
        return TWO_PI * (self.step % self.P["drivePer"]) / self.P["drivePer"]

    def _current_signal_phase(self):
        return TWO_PI * (self.step % self.P["signalPer"]) / self.P["signalPer"]

    def _current_gate_value(self):
        if self.is_warmup():
            return 0.0
        total = max(1, self.P["dayLen"] + self.P["nightLen"])
        if self.cycle_mode in ("forceday", "day"):
            phase_step = self.cycle_step_in_phase
        elif self.cycle_mode in ("forcenight", "night"):
            phase_step = self.P["dayLen"] + self.cycle_step_in_phase
        else:
            phase_step = 0
        return max(0.0, math.sin(TWO_PI * phase_step / total))

    def _compute_drive(self):
        self.DRIVE_R.zero_()
        self.DRIVE_I.zero_()

        target_env = 1.0 if self.is_day() else 0.0
        if target_env == 0.0:
            self.drive_env = 0.0
        else:
            ramp = max(1, self.P.get("driveRamp", 1))
            self.drive_env += (1.0 - self.drive_env) / ramp
            if abs(self.drive_env - 1.0) < 1e-4:
                self.drive_env = 1.0

        phase = self._current_drive_phase()
        amp   = self.P["driveAmp"] * self.drive_env
        r, c  = self.input_node
        self.DRIVE_R[r, c] = amp * math.cos(phase)
        self.DRIVE_I[r, c] = amp * math.sin(phase)
        self.gate_value = self.drive_env
        self.signal_phase = phase

    # ── X update (every step) ─────────────────────────────────────────────────

    def _update_x(self):
        P   = self.P
        Xr  = self.Xr
        Xi  = self.Xi
        S   = self.S
        Sedge = self.Sedge

        sumR   = self._z(); sumI   = self._z()
        retR   = self._z(); retI   = self._z()
        memW   = self._z()
        alignR = self._z(); alignI = self._z()
        psR    = self._z(); psI    = self._z()

        ps   = P["phi"] * S          # (N, N) phase bias from structural field
        mi   = torch.sqrt(Xr**2 + Xi**2)

        for e, (dx, dy) in enumerate(NB8):
            Xr_j = self._roll(Xr, dx, dy)
            Xi_j = self._roll(Xi, dx, dy)

            se  = Sedge[:, :, e]
            wij = P["W"] * (1.0 + P["edgeGain"] * se)

            edgePhase = ps + P["phi"] * se
            cE = torch.cos(edgePhase)
            sE = torch.sin(edgePhase)

            eR = cE * Xr_j - sE * Xi_j
            eI = sE * Xr_j + cE * Xi_j

            sumR += wij * eR
            sumI += wij * eI
            retR += se * eR
            retI += se * eI
            memW += se

            # Kuramoto-style phase alignment
            mj       = torch.sqrt(Xr_j**2 + Xi_j**2)
            has_j    = mj > 1e-6
            mi_s     = mi.clamp(min=1e-6)
            mj_s     = mj.clamp(min=1e-6)
            uiR = torch.where(mi > 1e-6, Xr / mi_s, torch.ones_like(Xr))
            uiI = torch.where(mi > 1e-6, Xi / mi_s, torch.zeros_like(Xi))
            ujR = Xr_j / mj_s
            ujI = Xi_j / mj_s
            sinD     = uiR * ujI - uiI * ujR
            amp_node = mi.clamp(min=0.05)
            contrib  = has_j.float() * ((sinD * (-uiI) * amp_node + 0.35 * (Xr_j - Xr)) * (1.0 + se))
            alignR  += contrib
            alignI  += has_j.float() * ((sinD * uiR * amp_node + 0.35 * (Xi_j - Xi)) * (1.0 + se))

            # Phase-unit sum for coherence
            psR += torch.where(has_j, Xr_j / mj_s, torch.zeros_like(Xr_j))
            psI += torch.where(has_j, Xi_j / mj_s, torch.zeros_like(Xi_j))

        an = float(len(NB8))

        # Triadic remainder — discrete vortex detection.
        # Each edge phase difference is wrapped individually to (-π, π] before
        # summing; the sum then measures topological charge (0 = no vortex,
        # ±2π = full vortex).  Dividing by 2π and clamping gives [0, 1].
        # (The JS version wrapped the *sum*, which always telescopes to 0.)
        triRem = self._z()
        if P["triWeight"] > 0:
            j1r = torch.roll(Xr, -1, 1);  j1i = torch.roll(Xi, -1, 1)  # x+1
            j2r = torch.roll(Xr, -1, 0);  j2i = torch.roll(Xi, -1, 0)  # y+1
            j3r = torch.roll(torch.roll(Xr, -1, 0), -1, 1)              # x+1, y+1
            j3i = torch.roll(torch.roll(Xi, -1, 0), -1, 1)
            p0 = torch.atan2(Xi, Xr)
            p1 = torch.atan2(j1i, j1r)
            p2 = torch.atan2(j2i, j2r)
            p3 = torch.atan2(j3i, j3r)
            # Triangle 1: (i, x+1,y, x,y+1)
            l1 = (torch.abs(_wrap(p1-p0) + _wrap(p2-p1) + _wrap(p0-p2)) / TWO_PI).clamp(max=1.0)
            # Triangle 2: (x+1,y, x,y+1, x+1,y+1)
            l2 = (torch.abs(_wrap(p3-p1) + _wrap(p2-p3) + _wrap(p1-p2)) / TWO_PI).clamp(max=1.0)
            triRem = (l1 + l2) * 0.5

        coh = torch.sqrt(psR**2 + psI**2) / an
        self.C = coh
        self.R = 0.55 * (1.0 - coh) + 0.45 * triRem

        self.ChF = 0.85 * self.ChF + 0.15 * coh
        self.ChS = 0.99 * self.ChS + 0.01 * coh

        al = self.AL.clone()
        bl = self.BL

        # Night: memory-weighted damping relief
        if not self.is_day() and not self.is_warmup():
            memNode = Sedge.max(dim=2).values
            al = torch.clamp(al + P["persistAlpha"] * P["retain"] * memNode, max=0.999)

        selfBoost   = P["selfEx"] * coh
        alignScale  = P["kAlign"] / an
        retainScale = P["retain"] if (not self.is_day() and not self.is_warmup()) else 0.0

        nr = (al * Xr
              + sumR * (1.0 + selfBoost)
              + alignScale * alignR
              + retainScale * retR
              - bl * self.R * Xr
              + self.DRIVE_R)
        ni = (al * Xi
              + sumI * (1.0 + selfBoost)
              + alignScale * alignI
              + retainScale * retI
              - bl * self.R * Xi
              + self.DRIVE_I)

        # v7 night replay: rotate state by learned phase velocity
        replayMem = self._z(); replayGain = self._z(); replayAdv = self._z()
        if not self.is_day() and not self.is_warmup():
            memNode   = Sedge.max(dim=2).values
            memAvg    = torch.max(memNode, memW / an)
            replayMem = memAvg
            rg        = P["phaseInertia"] * P["retain"] * memAvg
            replayGain = rg
            # Preserve the learned angular velocity itself; memory strength should
            # gate whether replay is applied, not slow the replayed frequency.
            adv        = P["phaseInertia"] * self.Omega
            replayAdv  = adv
            significant = rg > 1e-6
            ca = torch.cos(adv); sa = torch.sin(adv)
            # Save originals before rotation (JS uses const tr=nr, ti=ni)
            tr = nr; ti = ni
            nr = torch.where(significant, ca * tr - sa * ti, tr)
            ni = torch.where(significant, sa * tr + ca * ti, ti)

        self.ReplayMem  = replayMem
        self.ReplayGain = replayGain
        self.ReplayAdv  = replayAdv

        # Clamp input node to drive frequency during day
        if self.is_day():
            clamp = self.P.get("driveClamp", 0.50)
            r, c = self.input_node
            nr[r, c] = (1.0 - clamp) * nr[r, c] + clamp * self.DRIVE_R[r, c]
            ni[r, c] = (1.0 - clamp) * ni[r, c] + clamp * self.DRIVE_I[r, c]

        # Amplitude cap
        m2 = nr**2 + ni**2
        sc = torch.where(m2 > 4.0, 2.0 / torch.sqrt(m2.clamp(min=1e-10)), torch.ones_like(m2))
        self.Xr = nr * sc
        self.Xi = ni * sc

    # ── phase memory (every step) ─────────────────────────────────────────────

    def _update_phase_memory(self):
        P  = self.P
        Xr = self.Xr; Xi = self.Xi

        ph  = torch.atan2(Xi, Xr)
        d   = ((ph - self.PrevPhi + math.pi) % TWO_PI) - math.pi   # wrapped diff
        self.PhaseDelta = d
        self.PrevPhi    = ph

        amp = torch.sqrt(Xr**2 + Xi**2)
        mem = self.Sedge.max(dim=2).values
        dph = self._current_drive_phase()
        drive_period = self.P["drivePer"]

        drive_lock = torch.where(
            amp > 1e-6,
            (Xr * math.cos(dph) + Xi * math.sin(dph)) / amp.clamp(min=1e-6),
            torch.zeros_like(Xr)
        )
        self.DriveLock = drive_lock

        learn       = max(0.0, P.get("omegaLearn", 0.0))
        forget_rate = 0.002

        if self.is_day() and not self.is_warmup():
            gate         = torch.clamp(amp / 0.12, max=1.0) * torch.max(torch.abs(drive_lock), mem)
            drive_omega  = TWO_PI / max(1, drive_period)
            target_omega = 0.55 * d + 0.45 * drive_omega
            self.Omega   = (1.0 - learn * gate) * self.Omega + (learn * gate) * target_omega
        elif not self.is_warmup():
            self.Omega = self.Omega * (1.0 - forget_rate)

    # ── S update (every 10 steps) ─────────────────────────────────────────────

    def _update_s(self):
        P = self.P; S = self.S; C = self.C; R = self.R

        maxC = torch.zeros_like(C)
        maxS = S.clone()
        for dx, dy in NB4:
            C_j = self._roll(C, dx, dy)
            S_j = self._roll(S, dx, dy)
            better = C_j > maxC
            maxC = torch.where(better, C_j, maxC)
            maxS = torch.where(better, S_j, maxS)

        self.S = torch.clamp(
            (1.0 - P["epsilon"]) * S + P["epsilon"] * (C - R) + 0.02 * (maxS - S),
            min=0.001, max=1.0
        )

    # ── Sedge update (every 10 steps) ─────────────────────────────────────────

    def _update_sedge(self):
        P   = self.P
        Xr  = self.Xr; Xi = self.Xi
        forgetting = P.get("edgeDecay", 0.0)
        train      = self.is_day() and not self.is_warmup() and P["epsilon"] > 0
        anneal     = 1.0 / (1.0 + self.cycle_count * 0.12)
        dph        = self._current_drive_phase()

        ai    = torch.sqrt(Xr**2 + Xi**2)
        pi_   = torch.atan2(Xi, Xr)
        driveI = torch.where(
            ai > 1e-6,
            torch.abs((Xr * math.cos(dph) + Xi * math.sin(dph)) / ai.clamp(min=1e-6)),
            torch.zeros_like(ai)
        )

        old      = self.Sedge.clone()       # pre-forgetting reference (matches JS `old`)
        new_edge = old * (1.0 - forgetting)

        if train:
            for e, (dx, dy) in enumerate(NB8):
                Xr_j = self._roll(Xr, dx, dy)
                Xi_j = self._roll(Xi, dx, dy)
                aj   = torch.sqrt(Xr_j**2 + Xi_j**2)
                pj   = torch.atan2(Xi_j, Xr_j)

                coh01   = 0.5 * (torch.cos(pj - pi_) + 1.0)
                driveJ  = torch.where(
                    aj > 1e-6,
                    torch.abs((Xr_j * math.cos(dph) + Xi_j * math.sin(dph)) / aj.clamp(min=1e-6)),
                    torch.zeros_like(aj)
                )
                ampGate   = torch.clamp((ai * aj) / 0.04, max=1.0)
                driveGate = driveI * driveJ * ampGate
                rem       = (1.0 - coh01) + 0.10 * torch.abs(ai - aj)
                plastic   = P["epsilon"] * anneal * (1.0 - old[:, :, e]) * driveGate
                new_edge[:, :, e] = torch.clamp(
                    new_edge[:, :, e] + plastic * (coh01 - rem - 0.03 * old[:, :, e]),
                    min=0.0, max=1.0
                )

        self.Sedge = new_edge

    # ── homeostasis (every 100 steps) ─────────────────────────────────────────

    def _update_homeostasis(self):
        P        = self.P
        fast_err = self.ChF - P["tauC"]
        slow_err = self.ChS - P["tauC"]
        agree    = fast_err * slow_err > 0

        err      = fast_err
        eta_eff  = P["eta"] * (1.0 + 5.0 * err**2)
        new_AL   = torch.clamp(self.AL - eta_eff * err * 0.5, min=0.88,  max=0.995)
        new_BL   = torch.clamp(self.BL + eta_eff * err * 1.0, min=0.02,  max=0.5)
        self.AL  = torch.where(agree, new_AL, self.AL)
        self.BL  = torch.where(agree, new_BL, self.BL)

    # ── cross-correlation ─────────────────────────────────────────────────────

    def _cross_corr(self, a, b):
        n = min(len(a), len(b), self.HIST_LEN)
        if n < 4:
            return 0.0
        a_t = torch.tensor(a[-n:], dtype=torch.float32)
        b_t = torch.tensor(b[-n:], dtype=torch.float32)
        da  = a_t - a_t.mean()
        db  = b_t - b_t.mean()
        num   = (da * db).sum()
        denom = torch.sqrt((da**2).sum() * (db**2).sum())
        return (num / denom).item() if denom > 1e-10 else 0.0

    def _update_symmetry_metrics(self):
        if len(self.left_day_history) < 4 or len(self.right_day_history) < 4:
            self.choice_strength = math.nan
            self.choice_consistency = math.nan
            self.overnight_persistence = math.nan
            self.switch_penalty = math.nan
            self.symmetry_fitness = math.nan
            self.chosen_basin = "none"
            return

        day_left = np.asarray(self.left_day_history, dtype=np.float32)
        day_right = np.asarray(self.right_day_history, dtype=np.float32)
        day_dom = (day_left - day_right) / np.maximum(day_left + day_right, 1e-6)
        mean_dom = float(np.mean(day_dom))
        chosen_sign = 1.0 if mean_dom >= 0.0 else -1.0
        self.chosen_basin = "left" if chosen_sign > 0 else "right"
        self.choice_strength = abs(mean_dom)
        self.choice_consistency = float(np.mean(np.sign(day_dom + 1e-6) == chosen_sign))

        if self.left_night_history and self.right_night_history:
            night_left = np.asarray(self.left_night_history, dtype=np.float32)
            night_right = np.asarray(self.right_night_history, dtype=np.float32)
            night_dom = (night_left - night_right) / np.maximum(night_left + night_right, 1e-6)
            self.overnight_persistence = float(np.mean(np.sign(night_dom + 1e-6) == chosen_sign))
            combined = np.concatenate([day_dom, night_dom])
        else:
            self.overnight_persistence = math.nan
            combined = day_dom

        signs = np.sign(combined)
        signs = signs[np.abs(combined) > 0.02]
        if len(signs) < 2:
            self.switch_penalty = 0.0
        else:
            flips = np.count_nonzero(signs[1:] != signs[:-1])
            self.switch_penalty = flips / max(1, len(signs) - 1)

        persistence = 0.0 if not np.isfinite(self.overnight_persistence) else self.overnight_persistence
        self.symmetry_fitness = (
            self.choice_strength
            * self.choice_consistency
            * persistence
            * max(0.0, 1.0 - self.switch_penalty)
        )

    # ── main tick ─────────────────────────────────────────────────────────────

    def update(self):
        was_day = self.is_day()
        was_warmup = self.is_warmup()

        self._compute_drive()
        self._update_x()
        self._update_phase_memory()

        if self.step % 10 == 0:
            self._update_s()
            self._update_sedge()

        if self.step % 100 == 0:
            self._update_homeostasis()

        # Record histories
        r, c = self.output_node
        ov   = self.Xr[r, c].item()
        oi   = self.Xi[r, c].item()
        om   = float(math.hypot(ov, oi))
        _append(self.output_history, ov, self.HIST_LEN)
        _append(self.output_imag_history, oi, self.HIST_LEN)
        _append(self.output_mag_history, om, self.HIST_LEN)

        if self.experiment == "symmetry_v1":
            lr, lc = self.left_receiver_node
            rr, rc = self.right_receiver_node
            left_mag = float(math.hypot(self.Xr[lr, lc].item(), self.Xi[lr, lc].item()))
            right_mag = float(math.hypot(self.Xr[rr, rc].item(), self.Xi[rr, rc].item()))
            _append(self.left_basin_history, left_mag, self.HIST_LEN)
            _append(self.right_basin_history, right_mag, self.HIST_LEN)
            self.current_dominance = (left_mag - right_mag) / max(left_mag + right_mag, 1e-6)

        if was_day and not was_warmup:
            _append(self.output_day_history, ov, self.HIST_LEN)
            _append(self.output_day_imag_history, oi, self.HIST_LEN)
            _append(self.output_day_mag_history, om, self.HIST_LEN)
            if self.experiment == "symmetry_v1":
                _append(self.left_day_history, left_mag, self.HIST_LEN)
                _append(self.right_day_history, right_mag, self.HIST_LEN)
        elif not was_day and not was_warmup:
            _append(self.output_night_history, ov, self.HIST_LEN)
            _append(self.output_night_imag_history, oi, self.HIST_LEN)
            _append(self.output_night_mag_history, om, self.HIST_LEN)
            if self.experiment == "symmetry_v1":
                _append(self.left_night_history, left_mag, self.HIST_LEN)
                _append(self.right_night_history, right_mag, self.HIST_LEN)

        # Memory scoring at night
        if not was_day and not was_warmup:
            self.corr_value = self._cross_corr(self.output_day_history, self.output_night_history)
            self.peak_corr  = max(self.peak_corr, self.corr_value)
            if self.corr_value > self.P["corrThr"]:
                self.dwell_steps += 1
                self.best_dwell   = max(self.best_dwell, self.dwell_steps)
            else:
                self.dwell_steps = 0

        self.day_period_est = _estimate_period(self.output_day_history)
        self.night_period_est = _estimate_period(self.output_night_history)
        if np.isfinite(self.day_period_est) and np.isfinite(self.night_period_est):
            ratio = self.night_period_est / max(self.day_period_est, 1e-6)
            self.replay_period_ratio = ratio
            self.frequency_faithfulness = min(ratio, 1.0 / max(ratio, 1e-6))
        else:
            self.replay_period_ratio = math.nan
            self.frequency_faithfulness = math.nan

        if self.experiment == "symmetry_v1":
            self._update_symmetry_metrics()

        self.advance_cycle()
        self.step += 1

    # ── state snapshot ────────────────────────────────────────────────────────

    def get_state(self):
        to_np = lambda t: t.cpu().numpy()
        or_, oc = self.output_node
        output_omega = float(self.Omega[or_, oc].item())
        output_adv = float(self.ReplayAdv[or_, oc].item())
        return {
            "Xr":        to_np(self.Xr),
            "Xi":        to_np(self.Xi),
            "S":         to_np(self.S),
            "R":         to_np(self.R),
            "C":         to_np(self.C),
            "Sedge_max": to_np(self.Sedge.max(dim=2).values),
            "Omega":     to_np(self.Omega),
            "magnitude": to_np(torch.sqrt(self.Xr**2 + self.Xi**2)),
            "phase":     to_np(torch.atan2(self.Xi, self.Xr)),
            "cycle_mode":   self.cycle_mode,
            "step":         self.step,
            "cycle_count":  self.cycle_count,
            "corr_value":   self.corr_value,
            "peak_corr":    self.peak_corr,
            "best_dwell":   self.best_dwell,
            "day_period_est": self.day_period_est,
            "night_period_est": self.night_period_est,
            "replay_period_ratio": self.replay_period_ratio,
            "frequency_faithfulness": self.frequency_faithfulness,
            "drive_env":    self.drive_env,
            "gate_value":   self.gate_value,
            "signal_phase": self.signal_phase,
            "experiment":   self.experiment,
            "symmetry_break": self.symmetry_break,
            "input_node":   self.input_node,
            "output_node":  self.output_node,
            "left_input_node": self.left_input_node,
            "right_input_node": self.right_input_node,
            "left_receiver_node": self.left_receiver_node,
            "right_receiver_node": self.right_receiver_node,
            "choice_strength": self.choice_strength,
            "choice_consistency": self.choice_consistency,
            "overnight_persistence": self.overnight_persistence,
            "switch_penalty": self.switch_penalty,
            "symmetry_fitness": self.symmetry_fitness,
            "chosen_basin": self.chosen_basin,
            "current_dominance": self.current_dominance,
            "output_omega": output_omega,
            "output_replay_adv": output_adv,
        }

    # ── persistence ───────────────────────────────────────────────────────────

    def save(self, path):
        """Save full field state to a .npz file."""
        tensors = {k: v.cpu().numpy() for k, v in vars(self).items()
                   if isinstance(v, torch.Tensor)}
        scalars = {k: v for k, v in vars(self).items()
                   if isinstance(v, (int, float, str, bool))}
        np.savez(path, **tensors, **{k: np.array(v) for k, v in scalars.items()})
        print(f"Saved → {path}")

    def load(self, path):
        """Restore field state from a .npz file (same N and device required)."""
        d = np.load(path, allow_pickle=True)
        for k, v in d.items():
            if hasattr(self, k):
                existing = getattr(self, k)
                if isinstance(existing, torch.Tensor):
                    setattr(self, k, torch.tensor(v, dtype=existing.dtype, device=self.device))
                else:
                    setattr(self, k, v.item() if v.ndim == 0 else v)
        print(f"Loaded ← {path}")


# ── tiny utility ─────────────────────────────────────────────────────────────

def _append(lst, val, max_len):
    lst.append(val)
    if len(lst) > max_len:
        del lst[0]
