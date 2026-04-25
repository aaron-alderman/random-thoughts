"""
run.py - canonical interactive runner for Field Dynamics v7

Focus:
  - compare spatial structure, replay, and symmetry behavior in one dashboard
  - inspect period/frequency using autocorrelation and unwrapped phase
  - load searched genomes into the same canonical live runner

Controls
  Space       pause / resume
  r           reset
  d           force day
  n           force night
  a           automatic cycle (default)
  q / Esc     quit
  s           save state to field_state.npz

Usage:
  python run.py
  python run.py --device cuda
  python run.py --load_genome best_genome.json
"""

import argparse
import json
import math
import time
from pathlib import Path

import matplotlib
import numpy as np
import torch
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

from experiment_paths import SUPPORTED_EXPERIMENTS, SUPPORTED_SYMMETRY_BREAKS
from field_dynamics import FieldDynamics

TWO_PI = 2 * math.pi
plt = None
BASE_DIR = Path(__file__).resolve().parent


def format_period(period):
    if period is None or not np.isfinite(period):
        return "--"
    return f"{period:.1f}"


def format_ratio(ratio):
    if ratio is None or not np.isfinite(ratio):
        return "--"
    return f"{ratio:.2f}x"


def format_score(score):
    if score is None or not np.isfinite(score):
        return "--"
    return f"{score:.2f}"


def resolve_path(path: str | None) -> Path | None:
    if path is None:
        return None
    p = Path(path)
    if p.is_absolute():
        return p
    if p.exists():
        return p.resolve()
    return BASE_DIR / p


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--device", default="auto",
                   help="'cpu', 'cuda', or 'auto' (default: auto-detect)")
    p.add_argument("--N", type=int, default=32, help="Grid size (default: 32)")
    p.add_argument("--steps_per_frame", type=int, default=4,
                   help="Simulation steps between display updates (default: 4)")
    p.add_argument("--experiment", choices=SUPPORTED_EXPERIMENTS, default="symmetry_v1",
                   help="Experiment family to run (default: symmetry_v1)")
    p.add_argument("--symmetry-break", choices=SUPPORTED_SYMMETRY_BREAKS, default="spatial",
                   help="Programmed symmetry break for symmetry_v1 (default: spatial)")
    p.add_argument("--load_genome", default=None,
                   help="Path to an experiment-scoped best_genome*.json produced by search")
    p.add_argument("--autocorr_lag", type=int, default=256,
                   help="Maximum lag shown in the autocorrelation panel")
    return p.parse_args()


def pick_device(requested):
    if requested == "auto":
        if torch.cuda.is_available():
            name = torch.cuda.get_device_name(0)
            print(f"GPU detected: {name} -> using CUDA")
            return "cuda"
        print("No CUDA GPU found -> using CPU")
        return "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        print("WARNING: --device cuda requested but CUDA not available. Falling back to CPU.")
        return "cpu"
    return requested


def phase_to_rgb(phase, mag, s_val, drive_phase=0.0, is_day=True):
    """Vectorized: all inputs are (N,N) arrays, returns (N,N,3) float [0,1]."""
    angle = (phase - drive_phase) if is_day else phase
    hue = ((angle / TWO_PI) * 360 + 360) % 360
    sat = (35 + np.clip(s_val * 120, 0, 55)) / 100
    lit = (12 + np.clip(mag * 85, 0, 58)) / 100

    h = hue / 360
    c = (1 - np.abs(2 * lit - 1)) * sat
    x = c * (1 - np.abs((h * 6) % 2 - 1))
    m = lit - c / 2

    h6 = (h * 6).astype(int)
    r = np.select([h6 == 0, h6 == 1, h6 == 2, h6 == 3, h6 == 4, h6 == 5],
                  [c, x, 0 * c, 0 * c, x, c], default=0 * c)
    g = np.select([h6 == 0, h6 == 1, h6 == 2, h6 == 3, h6 == 4, h6 == 5],
                  [x, c, c, x, 0 * c, 0 * c], default=0 * c)
    b = np.select([h6 == 0, h6 == 1, h6 == 2, h6 == 3, h6 == 4, h6 == 5],
                  [0 * c, 0 * c, x, c, c, x], default=0 * c)
    rgb = np.stack([r + m, g + m, b + m], axis=-1)
    return np.clip(rgb, 0, 1)


def configure_matplotlib():
    global plt
    if plt is not None:
        return plt

    for backend in ("TkAgg", "Qt5Agg", "WXAgg", "Agg"):
        try:
            matplotlib.use(backend, force=True)
            import matplotlib.pyplot as pyplot
            plt = pyplot
            return plt
        except Exception:
            continue

    raise RuntimeError("No usable matplotlib backend found.")


def build_figure():
    fig = plt.figure(figsize=(18, 9), facecolor="#0d0d14")
    gs = GridSpec(3, 6, figure=fig, hspace=0.42, wspace=0.32,
                  left=0.05, right=0.98, top=0.92, bottom=0.08)

    axes = {}
    axes["field"] = fig.add_subplot(gs[:2, :2])
    axes["C"] = fig.add_subplot(gs[0, 2])
    axes["S"] = fig.add_subplot(gs[0, 3])
    axes["portrait"] = fig.add_subplot(gs[0, 4])
    axes["autocorr"] = fig.add_subplot(gs[0, 5])
    axes["R"] = fig.add_subplot(gs[1, 2])
    axes["edge"] = fig.add_subplot(gs[1, 3])
    axes["omega"] = fig.add_subplot(gs[1, 4])
    axes["magmap"] = fig.add_subplot(gs[1, 5])
    axes["proj"] = fig.add_subplot(gs[2, :2])
    axes["phase"] = fig.add_subplot(gs[2, 2:4])
    axes["corr"] = fig.add_subplot(gs[2, 4:6])

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


def build_help_overlay(fig):
    help_text = (
        "Hotkeys\n"
        "space  pause / resume\n"
        "r      reset\n"
        "d      force day\n"
        "n      force night\n"
        "a      automatic cycle\n"
        "s      save field_state.npz\n"
        "h      toggle this help\n"
        "q/esc  quit"
    )
    text = fig.text(
        0.013, 0.987, help_text,
        ha="left", va="top",
        color="#ddd", fontsize=9, family="monospace",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#111722", edgecolor="#444", alpha=0.94),
        zorder=20,
    )
    text.set_visible(False)
    return text


def main():
    global plt
    args = parse_args()
    device = pick_device(args.device)
    plt = configure_matplotlib()

    genome_overrides = {}
    replay_episode_seeds = None
    replay_seed = None
    replay_slot = 0
    if args.load_genome:
        genome_path = resolve_path(args.load_genome)
        with open(genome_path) as f:
            genome = json.load(f)
        genome_overrides = genome["params"]
        replay_episode_seeds = genome.get("eval_episode_seeds")
        replay_slot = int(genome.get("eval_slot", 0))
        if replay_episode_seeds:
            replay_seed = int(replay_episode_seeds[0])
            genome_overrides["reset_seed"] = replay_seed
            genome_overrides["reset_slot"] = replay_slot
        args.experiment = genome.get("experiment", args.experiment)
        args.symmetry_break = genome.get("symmetry_break", args.symmetry_break) or args.symmetry_break
        print(f"Loaded genome from {genome_path}  "
              f"(gen {genome['generation']}, fitness {genome['fitness']:.4f}, "
              f"{args.experiment}:{args.symmetry_break if args.experiment != 'replay' else 'baseline'})")
        if replay_seed is not None:
            print(f"  replay seed = {replay_seed}  slot = {replay_slot}")
            if len(replay_episode_seeds) > 1:
                print(f"  note: saved fitness is averaged over {len(replay_episode_seeds)} episodes; live replay uses the first saved episode.")
        else:
            print("  note: genome has no saved replay seed, so exact fitness replay is unavailable for this file.")
        for k, v in genome_overrides.items():
            if k in ("reset_seed", "reset_slot"):
                continue
            print(f"  {k:>15s} = {v:.6f}")

    sim = FieldDynamics(
        N=args.N,
        device=device,
        experiment=args.experiment,
        symmetry_break=args.symmetry_break,
        **genome_overrides,
    )

    plt.ion()
    fig, ax = build_figure()
    fig.canvas.manager.set_window_title("Field Dynamics v7")
    help_overlay = build_help_overlay(fig)

    paused = False
    quit_flag = [False]
    show_help = [False]
    corr_history = []
    dominance_history = []

    def on_key(event):
        nonlocal paused
        if event.key in ("q", "escape"):
            quit_flag[0] = True
        elif event.key == " ":
            paused = not paused
        elif event.key == "r":
            sim.reset()
            corr_history.clear()
            dominance_history.clear()
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
        elif event.key in ("h", "H"):
            show_help[0] = not show_help[0]
            help_overlay.set_visible(show_help[0])
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("key_press_event", on_key)

    blank = np.zeros((args.N, args.N, 3))
    scalar_blank = blank[:, :, 0]

    im_field = ax["field"].imshow(blank, origin="lower", interpolation="nearest", aspect="equal")
    ax["field"].set_title("Phase Field  (spatial context)")

    def _node_box(r, c, color, lw=1.5):
        ax["field"].add_patch(Rectangle(
            (c - 0.5, r - 0.5), 1.0, 1.0,
            linewidth=lw, edgecolor=color, facecolor="none", zorder=5
        ))
    _node_box(*sim.input_node,  "#ff8c3d")   # main drive — orange
    _node_box(*sim.output_node, "#cccccc")   # main output — grey

    im_C = ax["C"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                          cmap="plasma", vmin=0, vmax=1, aspect="equal")
    im_S = ax["S"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                          cmap="viridis", vmin=0, vmax=1, aspect="equal")
    im_R = ax["R"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                          cmap="hot", vmin=0, vmax=1, aspect="equal")
    im_edge = ax["edge"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                                cmap="magma", vmin=0, vmax=1, aspect="equal")
    im_omega = ax["omega"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                                  cmap="coolwarm", vmin=-0.2, vmax=0.2, aspect="equal")
    im_magmap = ax["magmap"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                                    cmap="cividis", vmin=0, vmax=2.0, aspect="equal")
    ax["C"].set_title("Coherence C")
    ax["S"].set_title("Structural S")
    ax["R"].set_title("Remainder R")
    ax["edge"].set_title("Edge Memory")
    ax["omega"].set_title("Omega")
    ax["magmap"].set_title("Magnitude")

    line_xr, = ax["proj"].plot([], [], color="#4fc3f7", lw=0.9, label="Xr")
    line_xi, = ax["proj"].plot([], [], color="#f48fb1", lw=0.9, alpha=0.9, label="Xi")
    line_mag, = ax["proj"].plot([], [], color="#ffd54f", lw=0.9, alpha=0.85, label="|X|")
    ax["proj"].set_ylim(-2.2, 2.2)
    ax["proj"].set_title("Projection Components Vs Magnitude")
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
        rgb[ir, ic] = [1.0, 0.55, 0.24] if sim.is_day() else [0.6, 0.33, 0.14]
        if st["experiment"] == "symmetry_v1":
            ar, ac = st.get("probe_a_node", st["left_receiver_node"])
            br, bc = st.get("probe_b_node", st["right_receiver_node"])
            rgb[ar, ac] = [0.35, 1.0, 0.55]
            rgb[br, bc] = [0.55, 0.65, 1.0]
        if not sim.is_day() and not sim.is_warmup():
            alpha = min(sim.cycle_step_in_phase / 50, 1) * 0.22
            rgb = np.clip(rgb * (1 - alpha) + np.array([0.05, 0.13, 0.36]) * alpha, 0, 1)

        im_field.set_data(rgb)
        im_C.set_data(st["C"])
        im_S.set_data(st["S"])
        im_R.set_data(st["R"])
        im_edge.set_data(st["Sedge_max"])
        im_omega.set_data(np.clip(st["Omega"], -0.2, 0.2))
        im_magmap.set_data(np.clip(st["magnitude"], 0.0, 2.0))

        xs = list(range(len(sim.output_history)))
        line_xr.set_data(xs, sim.output_history)
        line_xi.set_data(xs, sim.output_imag_history)
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
        if len(phase_day) or len(phase_night):
            phase_all = np.concatenate([phase_day, phase_night])
            phase_min = np.nanmin(phase_all)
            phase_max = np.nanmax(phase_all)
        else:
            phase_min, phase_max = -1.0, 1.0
        if not np.isfinite(phase_min) or not np.isfinite(phase_max) or abs(phase_max - phase_min) < 1e-6:
            phase_min, phase_max = -1.0, 1.0
        pad = max(0.5, 0.08 * (phase_max - phase_min))
        ax["phase"].set_ylim(phase_min - pad, phase_max + pad)
        ax["phase"].set_xlim(0, max(hist, len(phase_day), len(phase_night)))

        corr_history.append(st["corr_value"])
        if len(corr_history) > hist:
            del corr_history[0]
        dominance_history.append(st.get("current_balance", st["current_dominance"]))
        if len(dominance_history) > hist:
            del dominance_history[0]

        if st["experiment"] == "symmetry_v1":
            ax["corr"].set_title("Probe Balance / Corr")
            ax["corr"].set_ylim(-1.1, 1.1)
            line_corr.set_data(np.arange(len(dominance_history)), dominance_history)
            ax["corr"].axhline(0, color="#333", lw=0.5)
        else:
            ax["corr"].set_title("Day/Night Corr")
            line_corr.set_data(np.arange(len(corr_history)), corr_history)
        ax["corr"].set_xlim(0, max(hist, len(corr_history), len(dominance_history)))

        fps = 1.0 / max(0.001, time.perf_counter() - frame_t)
        frame_t = time.perf_counter()
        if st["experiment"] == "symmetry_v1":
            title_text.set_text(
                f"Step {st['step']}  |  {st['cycle_mode'].upper()}  cycle {st['cycle_count']}"
                f"  |  {st['experiment']}:{st['symmetry_break']}"
                f"  |  cue {st.get('cue_label', '--')}"
                f"  |  choice {format_score(st['choice_strength'])}"
                f"  consistent {format_score(st['choice_consistency'])}"
                f"  persist {format_score(st['overnight_persistence'])}"
                f"  switch {format_score(st['switch_penalty'])}"
                f"  |  target {st.get('chosen_probe', st['chosen_basin'])}"
                f"  bal {st.get('current_balance', st['current_dominance']):.3f}"
                f"  |  dayT {format_period(st['day_period_est'])}"
                f"  nightT {format_period(st['night_period_est'])}"
                f"  ratio {format_ratio(st['replay_period_ratio'])}"
                f"  faithful {format_score(st['frequency_faithfulness'])}"
                f"  |  fit {format_score(st['symmetry_fitness'])}"
                f"  cycleFit {format_score(st['cycle_optimizer_fitness'])}"
                f"  optFit {format_score(st['optimizer_fitness'])}"
                f"  |  {fps:.0f} fps  device: {device}  N={args.N}"
            )
        else:
            title_text.set_text(
                f"Step {st['step']}  |  {st['cycle_mode'].upper()}  cycle {st['cycle_count']}"
                f"  |  dayT {format_period(st['day_period_est'])}"
                f"  nightT {format_period(st['night_period_est'])}"
                f"  |  ratio {format_ratio(st['replay_period_ratio'])}"
                f"  faithful {format_score(st['frequency_faithfulness'])}"
                f"  |  omega {st['output_omega']:.4f}"
                f"  replayAdv {st['output_replay_adv']:.4f}"
                f"  |  corr {st['corr_value']:.3f}  dwell {st['best_dwell']}"
                f"  optFit {format_score(st['optimizer_fitness'])}"
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
