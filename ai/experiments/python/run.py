"""
run.py — interactive runner for Field Dynamics v7

Controls
  Space       pause / resume
  r           reset
  d           force day
  n           force night
  a           automatic cycle (default)
  q / Esc     quit
  s           save state to field_state.npz

Usage:
  python run.py                              # CPU
  python run.py --device cuda               # NVIDIA GPU
  python run.py --N 64                      # larger grid
  python run.py --load_genome best_genome.json  # visualise evolved params
"""

import argparse
import json
import sys
import time
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec
import torch

from field_dynamics import FieldDynamics

TWO_PI = 2 * math.pi


# ── argument parsing ─────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--device", default="auto",
                   help="'cpu', 'cuda', or 'auto' (default: auto-detect)")
    p.add_argument("--N", type=int, default=32, help="Grid size (default: 32)")
    p.add_argument("--steps_per_frame", type=int, default=4,
                   help="Simulation steps between display updates (default: 4)")
    p.add_argument("--load_genome", default=None,
                   help="Path to best_genome.json produced by evolve.py")
    return p.parse_args()


def pick_device(requested):
    if requested == "auto":
        if torch.cuda.is_available():
            name = torch.cuda.get_device_name(0)
            print(f"GPU detected: {name}  → using CUDA")
            return "cuda"
        else:
            print("No CUDA GPU found → using CPU")
            return "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        print("WARNING: --device cuda requested but CUDA not available. Falling back to CPU.")
        return "cpu"
    return requested


# ── phase → HSL colour (matches JS renderer) ─────────────────────────────────

def phase_to_rgb(phase, mag, S_val, drive_phase=0.0, is_day=True):
    """Vectorised: all inputs are (N,N) arrays, returns (N,N,3) float [0,1]."""
    angle = (phase - drive_phase) if is_day else phase
    hue   = ((angle / TWO_PI) * 360 + 360) % 360          # degrees
    sat   = (35 + np.clip(S_val * 120, 0, 55)) / 100
    lit   = (12 + np.clip(mag * 85,   0, 58)) / 100

    # HSL → RGB (vectorised)
    h = hue / 360
    c = (1 - np.abs(2 * lit - 1)) * sat
    x = c * (1 - np.abs((h * 6) % 2 - 1))
    m = lit - c / 2

    h6 = (h * 6).astype(int)
    r = np.select([h6==0, h6==1, h6==2, h6==3, h6==4, h6==5],
                  [c, x, 0*c, 0*c, x, c], default=0*c)
    g = np.select([h6==0, h6==1, h6==2, h6==3, h6==4, h6==5],
                  [x, c, c, x, 0*c, 0*c], default=0*c)
    b = np.select([h6==0, h6==1, h6==2, h6==3, h6==4, h6==5],
                  [0*c, 0*c, x, c, c, x], default=0*c)
    rgb = np.stack([r+m, g+m, b+m], axis=-1)
    return np.clip(rgb, 0, 1)


# ── figure setup ─────────────────────────────────────────────────────────────

def build_figure():
    fig = plt.figure(figsize=(14, 8), facecolor="#0d0d14")
    gs  = GridSpec(3, 4, figure=fig, hspace=0.45, wspace=0.35,
                   left=0.05, right=0.97, top=0.93, bottom=0.07)

    axes = {}
    axes["field"] = fig.add_subplot(gs[:2, :2])
    axes["C"]     = fig.add_subplot(gs[0, 2])
    axes["S"]     = fig.add_subplot(gs[0, 3])
    axes["R"]     = fig.add_subplot(gs[1, 2])
    axes["edge"]  = fig.add_subplot(gs[1, 3])
    axes["out"]   = fig.add_subplot(gs[2, :2])
    axes["omega"] = fig.add_subplot(gs[2, 2])
    axes["corr"]  = fig.add_subplot(gs[2, 3])

    style = dict(facecolor="#0d0d14", labelcolor="#888", titlecolor="#ccc",
                 tick_params=dict(colors="#666"))
    for name, ax in axes.items():
        ax.set_facecolor("#0d0d14")
        for spine in ax.spines.values():
            spine.set_edgecolor("#333")
        ax.tick_params(colors="#666", labelsize=7)
        ax.title.set_color("#aaa")
        ax.title.set_fontsize(8)

    return fig, axes


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    args   = parse_args()
    device = pick_device(args.device)
    N      = args.N
    spf    = args.steps_per_frame

    genome_overrides = {}
    if args.load_genome:
        with open(args.load_genome) as f:
            genome = json.load(f)
        genome_overrides = genome["params"]
        print(f"Loaded genome from {args.load_genome}  "
              f"(gen {genome['generation']}, fitness {genome['fitness']:.4f})")
        for k, v in genome_overrides.items():
            print(f"  {k:>15s} = {v:.6f}")

    sim = FieldDynamics(N=N, device=device, **genome_overrides)

    # ── matplotlib interactive mode ──────────────────────────────────────────
    # Try backends in order until one works
    for _backend in ("TkAgg", "Qt5Agg", "WXAgg", "Agg"):
        try:
            matplotlib.use(_backend)
            break
        except Exception:
            continue
    plt.ion()
    fig, ax = build_figure()
    fig.canvas.manager.set_window_title("Field Dynamics v7 — Python/PyTorch")

    paused    = False
    quit_flag = [False]

    def on_key(event):
        nonlocal paused
        if event.key in ("q", "escape"):
            quit_flag[0] = True
        elif event.key == " ":
            paused = not paused
        elif event.key == "r":
            sim.reset()
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

    # ── initial images (filled with zeros so imshow handles shape) ───────────
    blank = np.zeros((N, N, 3))
    im_field = ax["field"].imshow(blank, origin="lower", interpolation="nearest", aspect="equal")
    im_C     = ax["C"].imshow(blank[:,:,0], origin="lower", interpolation="nearest",
                               cmap="plasma", vmin=0, vmax=1, aspect="equal")
    im_S     = ax["S"].imshow(blank[:,:,0], origin="lower", interpolation="nearest",
                               cmap="viridis", vmin=0, vmax=1, aspect="equal")
    im_R     = ax["R"].imshow(blank[:,:,0], origin="lower", interpolation="nearest",
                               cmap="hot",    vmin=0, vmax=1, aspect="equal")
    im_edge  = ax["edge"].imshow(blank[:,:,0], origin="lower", interpolation="nearest",
                                  cmap="magma", vmin=0, vmax=1, aspect="equal")
    im_omega = ax["omega"].imshow(blank[:,:,0], origin="lower", interpolation="nearest",
                                   cmap="coolwarm", vmin=-0.2, vmax=0.2, aspect="equal")

    ax["field"].set_title("Phase field  (hue=phase, bright=mag)")
    ax["C"].set_title("Coherence C"); ax["S"].set_title("Structural S")
    ax["R"].set_title("Remainder R"); ax["edge"].set_title("Edge memory (max)")
    ax["omega"].set_title("Omega (learned ω)")

    line_out,  = ax["out"].plot([], [], color="#4fc3f7", lw=0.8)
    line_day,  = ax["out"].plot([], [], color="#81c784", lw=0.8, alpha=0.6)
    ax["out"].set_ylim(-2.2, 2.2)
    ax["out"].set_title("Output Xr  (blue=all  green=day history)")
    ax["out"].axhline(0, color="#333", lw=0.5)

    line_corr, = ax["corr"].plot([], [], color="#ffb74d", lw=0.9)
    ax["corr"].set_ylim(-1.1, 1.1)
    ax["corr"].set_title("Day/Night corr")
    ax["corr"].axhline(sim.P["corrThr"], color="#555", lw=0.5, ls="--")

    title_text = fig.suptitle("", color="#bbb", fontsize=9)

    corr_history = []

    HIST = sim.HIST_LEN
    frame_t = time.perf_counter()

    while not quit_flag[0]:
        if not paused:
            for _ in range(spf):
                sim.update()

        # ── gather state ─────────────────────────────────────────────────────
        st = sim.get_state()
        mag   = st["magnitude"]
        phase = st["phase"]
        S     = st["S"]
        dph   = sim._current_drive_phase()

        # Field image
        rgb = phase_to_rgb(phase, mag, S, drive_phase=dph, is_day=sim.is_day())
        # Mark input node (orange tint)
        ir, ic = sim.input_node
        if sim.is_day():
            rgb[ir, ic] = [1.0, 0.55, 0.24]
        else:
            rgb[ir, ic] = [0.6, 0.33, 0.14]
        # Mark output node (cyan tint)
        or_, oc = sim.output_node
        rgb[or_, oc] = [0.24, 0.9, 0.9]

        # Night overlay (dark blue tint)
        if not sim.is_day() and not sim.is_warmup():
            alpha = min(sim.cycle_step_in_phase / 50, 1) * 0.22
            rgb = np.clip(rgb * (1 - alpha) + np.array([0.05, 0.13, 0.36]) * alpha, 0, 1)

        im_field.set_data(rgb)
        im_C.set_data(st["C"])
        im_S.set_data(st["S"])
        im_R.set_data(st["R"])
        im_edge.set_data(st["Sedge_max"])
        im_omega.set_data(np.clip(st["Omega"], -0.2, 0.2))

        # Output trace
        oh = sim.output_history
        xs = list(range(len(oh)))
        line_out.set_data(xs, oh)
        dh = sim.output_day_history
        dx = list(range(len(dh)))
        line_day.set_data(dx, dh)
        ax["out"].set_xlim(0, max(HIST, len(oh)))

        # Correlation history
        corr_history.append(st["corr_value"])
        if len(corr_history) > HIST:
            del corr_history[0]
        cx = list(range(len(corr_history)))
        line_corr.set_data(cx, corr_history)
        ax["corr"].set_xlim(0, max(HIST, len(corr_history)))

        # Title bar
        mode_str = st["cycle_mode"].upper()
        fps = 1.0 / max(0.001, time.perf_counter() - frame_t)
        frame_t = time.perf_counter()
        title_text.set_text(
            f"Step {st['step']}  |  {mode_str}  cycle {st['cycle_count']}"
            f"  |  corr {st['corr_value']:.3f}  peak {st['peak_corr']:.3f}"
            f"  |  dwell {st['best_dwell']}  |  {fps:.0f} fps"
            f"  |  device: {device}  N={N}"
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
