"""
run-phase.py - phase-oriented runner for Field Dynamics v7

Focus:
  - distinguish projection effects from genuine replay slowdown
  - compare day vs night phase geometry directly
  - inspect period/frequency using autocorrelation and unwrapped phase

Controls
  Space       pause / resume
  r           reset
  d           force day
  n           force night
  a           automatic cycle (default)
  q / Esc     quit
  s           save state to field_state.npz

Usage:
  python run-phase.py
  python run-phase.py --device cuda
  python run-phase.py --load_genome best_genome.json
"""

import argparse
import json
import time
from pathlib import Path
import numpy as np
from matplotlib.gridspec import GridSpec

from field_dynamics import FieldDynamics
from run import (
    configure_matplotlib,
    format_period,
    format_ratio,
    format_score,
    phase_to_rgb,
    pick_device,
)

BASE_DIR = Path(__file__).resolve().parent


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--device", default="auto",
                   help="'cpu', 'cuda', or 'auto' (default: auto-detect)")
    p.add_argument("--N", type=int, default=32, help="Grid size (default: 32)")
    p.add_argument("--steps_per_frame", type=int, default=4,
                   help="Simulation steps between display updates (default: 4)")
    p.add_argument("--load_genome", default=None,
                   help="Path to best_genome.json produced by evolve.py")
    p.add_argument("--autocorr_lag", type=int, default=96,
                   help="Maximum lag shown in the autocorrelation panel")
    return p.parse_args()


def resolve_path(path: str | None) -> Path | None:
    if path is None:
        return None
    p = Path(path)
    if p.is_absolute():
        return p
    if p.exists():
        return p.resolve()
    return BASE_DIR / p


def build_figure(plt):
    fig = plt.figure(figsize=(15, 8.5), facecolor="#0d0d14")
    gs = GridSpec(2, 4, figure=fig, hspace=0.42, wspace=0.32,
                  left=0.05, right=0.98, top=0.92, bottom=0.08)

    axes = {}
    axes["field"] = fig.add_subplot(gs[0, :2])
    axes["proj"] = fig.add_subplot(gs[1, :2])
    axes["portrait"] = fig.add_subplot(gs[0, 2])
    axes["autocorr"] = fig.add_subplot(gs[0, 3])
    axes["phase"] = fig.add_subplot(gs[1, 2])
    axes["corr"] = fig.add_subplot(gs[1, 3])

    for ax in axes.values():
        ax.set_facecolor("#0d0d14")
        for spine in ax.spines.values():
            spine.set_edgecolor("#333")
        ax.tick_params(colors="#666", labelsize=7)
        ax.title.set_color("#aaa")
        ax.title.set_fontsize(8)

    return fig, axes


def autocorr_curve(trace, max_lag):
    lags = np.arange(max_lag + 1, dtype=np.float32)
    vals = np.full(max_lag + 1, np.nan, dtype=np.float32)

    if len(trace) < 4:
        return lags, vals

    arr = np.asarray(trace, dtype=np.float32)
    centered = arr - arr.mean()
    denom = float(np.dot(centered, centered))
    if denom <= 1e-8:
        return lags, vals

    vals[0] = 1.0
    upper = min(max_lag + 1, len(arr))
    for lag in range(1, upper):
        vals[lag] = float(np.dot(centered[:-lag], centered[lag:]) / denom)
    return lags, vals


def unwrapped_phase(real_hist, imag_hist):
    if len(real_hist) == 0 or len(real_hist) != len(imag_hist):
        return np.array([], dtype=np.float32)
    return np.unwrap(np.arctan2(np.asarray(imag_hist, dtype=np.float32),
                                np.asarray(real_hist, dtype=np.float32)))


def set_vline(line, x):
    if x is None or not np.isfinite(x):
        line.set_xdata([np.nan, np.nan])
    else:
        line.set_xdata([x, x])


def main():
    args = parse_args()
    device = pick_device(args.device)
    plt = configure_matplotlib()

    genome_overrides = {}
    if args.load_genome:
        genome_path = resolve_path(args.load_genome)
        with open(genome_path) as f:
            genome = json.load(f)
        genome_overrides = genome["params"]
        print(f"Loaded genome from {genome_path}  "
              f"(gen {genome['generation']}, fitness {genome['fitness']:.4f})")

    sim = FieldDynamics(N=args.N, device=device, **genome_overrides)

    plt.ion()
    fig, ax = build_figure(plt)
    fig.canvas.manager.set_window_title("Field Dynamics v7 - run-phase")

    paused = False
    quit_flag = [False]
    corr_history = []

    def on_key(event):
        nonlocal paused
        if event.key in ("q", "escape"):
            quit_flag[0] = True
        elif event.key == " ":
            paused = not paused
        elif event.key == "r":
            sim.reset()
            corr_history.clear()
        elif event.key == "d":
            sim.cycle_mode = "forceday"
            sim.cycle_step_in_phase = 0
        elif event.key == "n":
            sim.cycle_mode = "forcenight"
            sim.cycle_step_in_phase = 0
        elif event.key == "a":
            sim.cycle_mode = "day" if sim.is_day() else "warmup"
            sim.cycle_step_in_phase = 0
        elif event.key == "s":
            sim.save("field_state.npz")

    fig.canvas.mpl_connect("key_press_event", on_key)

    blank = np.zeros((args.N, args.N, 3))
    im_field = ax["field"].imshow(blank, origin="lower", interpolation="nearest", aspect="equal")
    ax["field"].set_title("Phase Field  (spatial context)")

    line_xr, = ax["proj"].plot([], [], color="#4fc3f7", lw=0.9, label="Xr")
    line_mag, = ax["proj"].plot([], [], color="#ffd54f", lw=0.9, alpha=0.85, label="|X|")
    ax["proj"].set_ylim(-2.2, 2.2)
    ax["proj"].set_title("Projection Vs Magnitude")
    ax["proj"].axhline(0, color="#333", lw=0.5)
    ax["proj"].legend(fontsize=7, facecolor="#0d0d14", edgecolor="#333",
                      labelcolor="#aaa", loc="upper right")

    line_day_portrait, = ax["portrait"].plot([], [], color="#81c784", lw=1.0, alpha=0.9, label="day")
    line_night_portrait, = ax["portrait"].plot([], [], color="#ffb74d", lw=1.0, alpha=0.9, label="night")
    dot_current, = ax["portrait"].plot([], [], marker="o", ms=4, color="#4dd0e1", lw=0)
    ax["portrait"].set_xlim(-2.2, 2.2)
    ax["portrait"].set_ylim(-2.2, 2.2)
    ax["portrait"].set_title("Phase Portrait  (Xi vs Xr)")
    ax["portrait"].axhline(0, color="#333", lw=0.5)
    ax["portrait"].axvline(0, color="#333", lw=0.5)
    ax["portrait"].legend(fontsize=7, facecolor="#0d0d14", edgecolor="#333",
                          labelcolor="#aaa", loc="upper right")

    line_day_auto, = ax["autocorr"].plot([], [], color="#81c784", lw=1.0, label="day")
    line_night_auto, = ax["autocorr"].plot([], [], color="#ffb74d", lw=1.0, label="night")
    vline_day = ax["autocorr"].axvline(np.nan, color="#81c784", lw=0.8, ls="--", alpha=0.8)
    vline_night = ax["autocorr"].axvline(np.nan, color="#ffb74d", lw=0.8, ls="--", alpha=0.8)
    ax["autocorr"].set_ylim(-1.05, 1.05)
    ax["autocorr"].set_xlim(0, args.autocorr_lag)
    ax["autocorr"].set_title("Autocorrelation  (period cue)")
    ax["autocorr"].axhline(0, color="#333", lw=0.5)
    ax["autocorr"].legend(fontsize=7, facecolor="#0d0d14", edgecolor="#333",
                          labelcolor="#aaa", loc="upper right")

    line_day_phase, = ax["phase"].plot([], [], color="#81c784", lw=1.0, label="day")
    line_night_phase, = ax["phase"].plot([], [], color="#ffb74d", lw=1.0, label="night")
    ax["phase"].set_title("Unwrapped Phase  (slope = frequency)")
    ax["phase"].axhline(0, color="#333", lw=0.5)
    ax["phase"].legend(fontsize=7, facecolor="#0d0d14", edgecolor="#333",
                       labelcolor="#aaa", loc="upper left")

    line_corr, = ax["corr"].plot([], [], color="#ffb74d", lw=0.9)
    ax["corr"].set_ylim(-1.1, 1.1)
    ax["corr"].set_title("Day/Night Corr")
    ax["corr"].axhline(sim.P["corrThr"], color="#555", lw=0.5, ls="--")

    title_text = fig.suptitle("", color="#bbb", fontsize=9)
    frame_t = time.perf_counter()
    hist = sim.HIST_LEN

    while not quit_flag[0]:
        if not paused:
            for _ in range(args.steps_per_frame):
                sim.update()

        st = sim.get_state()
        mag = st["magnitude"]
        phase = st["phase"]
        dph = sim._current_drive_phase()

        rgb = phase_to_rgb(phase, mag, st["S"], drive_phase=dph, is_day=sim.is_day())
        ir, ic = sim.input_node
        or_, oc = sim.output_node
        rgb[ir, ic] = [1.0, 0.55, 0.24] if sim.is_day() else [0.6, 0.33, 0.14]
        rgb[or_, oc] = [0.24, 0.9, 0.9]
        if not sim.is_day() and not sim.is_warmup():
            alpha = min(sim.cycle_step_in_phase / 50, 1) * 0.22
            rgb = np.clip(rgb * (1 - alpha) + np.array([0.05, 0.13, 0.36]) * alpha, 0, 1)
        im_field.set_data(rgb)

        xs = list(range(len(sim.output_history)))
        line_xr.set_data(xs, sim.output_history)
        line_mag.set_data(xs, sim.output_mag_history)
        ax["proj"].set_xlim(0, max(hist, len(sim.output_history)))

        day_r = np.asarray(sim.output_day_history, dtype=np.float32)
        day_i = np.asarray(sim.output_day_imag_history, dtype=np.float32)
        night_r = np.asarray(sim.output_night_history, dtype=np.float32)
        night_i = np.asarray(sim.output_night_imag_history, dtype=np.float32)
        line_day_portrait.set_data(day_r, day_i)
        line_night_portrait.set_data(night_r, night_i)
        dot_current.set_data([sim.output_history[-1]] if sim.output_history else [],
                             [sim.output_imag_history[-1]] if sim.output_imag_history else [])

        lags_day, ac_day = autocorr_curve(sim.output_day_history, args.autocorr_lag)
        lags_night, ac_night = autocorr_curve(sim.output_night_history, args.autocorr_lag)
        line_day_auto.set_data(lags_day, ac_day)
        line_night_auto.set_data(lags_night, ac_night)
        set_vline(vline_day, st["day_period_est"])
        set_vline(vline_night, st["night_period_est"])

        phase_day = unwrapped_phase(sim.output_day_history, sim.output_day_imag_history)
        phase_night = unwrapped_phase(sim.output_night_history, sim.output_night_imag_history)
        line_day_phase.set_data(np.arange(len(phase_day)), phase_day)
        line_night_phase.set_data(np.arange(len(phase_night)), phase_night)
        phase_min = np.nanmin(np.concatenate([phase_day, phase_night])) if (len(phase_day) or len(phase_night)) else -1.0
        phase_max = np.nanmax(np.concatenate([phase_day, phase_night])) if (len(phase_day) or len(phase_night)) else 1.0
        if not np.isfinite(phase_min) or not np.isfinite(phase_max) or abs(phase_max - phase_min) < 1e-6:
            phase_min, phase_max = -1.0, 1.0
        pad = max(0.5, 0.08 * (phase_max - phase_min))
        ax["phase"].set_ylim(phase_min - pad, phase_max + pad)
        ax["phase"].set_xlim(0, max(hist, len(phase_day), len(phase_night)))

        corr_history.append(st["corr_value"])
        if len(corr_history) > hist:
            del corr_history[0]
        line_corr.set_data(np.arange(len(corr_history)), corr_history)
        ax["corr"].set_xlim(0, max(hist, len(corr_history)))

        fps = 1.0 / max(0.001, time.perf_counter() - frame_t)
        frame_t = time.perf_counter()
        title_text.set_text(
            f"Step {st['step']}  |  {st['cycle_mode'].upper()}  cycle {st['cycle_count']}"
            f"  |  dayT {format_period(st['day_period_est'])}"
            f"  nightT {format_period(st['night_period_est'])}"
            f"  |  ratio {format_ratio(st['replay_period_ratio'])}"
            f"  faithful {format_score(st['frequency_faithfulness'])}"
            f"  |  omega {st['output_omega']:.4f}"
            f"  replayAdv {st['output_replay_adv']:.4f}"
            f"  |  corr {st['corr_value']:.3f}  dwell {st['best_dwell']}"
            f"  |  {fps:.0f} fps  device: {device}  N={args.N}"
        )

        try:
            fig.canvas.draw_idle()
            fig.canvas.flush_events()
        except Exception:
            break

        if paused:
            plt.pause(0.05)

    plt.ioff()
    plt.close("all")
    print("Done.")


if __name__ == "__main__":
    main()
