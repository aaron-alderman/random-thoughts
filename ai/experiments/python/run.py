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
  python run.py --load_genome genomes/symmetry_v1/best_genome.json
  python run.py --experiment temporal_v1 --trace_csv temporal_trace.csv
"""

import argparse
import csv
import math
import time
from pathlib import Path

import matplotlib
import numpy as np
import torch
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch, Rectangle

from experiment_paths import SUPPORTED_EXPERIMENTS, SUPPORTED_SYMMETRY_BREAKS
from field_dynamics import FieldDynamics
from genome_io import load_genome
from parameter_policy import merged_genome_params

TWO_PI = 2 * math.pi
plt = None
BASE_DIR = Path(__file__).resolve().parent
THEME = {
    "bg": "#080b14",
    "panel": "#101826",
    "panel_soft": "#0d1522",
    "card_edge": "#26354c",
    "spine": "#31445f",
    "tick": "#93a4bf",
    "title": "#f4f7fb",
    "muted": "#a8b6cc",
    "grid": "#243246",
    "text": "#eef4ff",
    "accent": "#6fd3ff",
    "accent2": "#ffd166",
    "accent3": "#8ce99a",
    "danger": "#ff9f68",
}
DAY_THEME = {
    "bg": "#f1d48a",
    "panel": "#16293d",
    "panel_soft": "#132437",
    "card_edge": "#4d7398",
    "spine": "#6189af",
    "tick": "#b4cee6",
    "title": "#f7fbff",
    "muted": "#c6d9ea",
    "grid": "#3b5873",
    "text": "#f4f9ff",
    "accent": "#64d9ff",
    "accent2": "#ffd980",
    "accent3": "#98efb0",
    "danger": "#ffb36d",
}
IMAGE_PANELS = {"field", "C", "S", "R", "edge", "omega", "magmap"}


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
    p.add_argument("--trace_csv", default=None,
                   help="Optional CSV path for per-step metric logging")
    p.add_argument("--trace_every", type=int, default=10,
                   help="Simulation-step cadence for CSV tracing when --trace_csv is set (default: 10)")
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


def blend_color(night, day, mix):
    a = np.asarray(matplotlib.colors.to_rgb(night), dtype=np.float32)
    b = np.asarray(matplotlib.colors.to_rgb(day), dtype=np.float32)
    return tuple(a * (1.0 - mix) + b * mix)


def themed_color(key, mix):
    return blend_color(THEME[key], DAY_THEME[key], mix)


def add_figure_background(fig):
    bg_ax = fig.add_axes([0, 0, 1, 1], zorder=-3)
    bg_ax.set_axis_off()

    x = np.linspace(-1.0, 1.0, 700, dtype=np.float32)
    y = np.linspace(-1.0, 1.0, 420, dtype=np.float32)
    xx, yy = np.meshgrid(x, y)
    radial = np.sqrt((xx + 0.42) ** 2 + (yy + 0.18) ** 2)
    swirl = np.clip(1.15 - radial, 0.0, 1.0)
    glow = np.clip(1.0 - np.sqrt((xx - 0.55) ** 2 + (yy + 0.5) ** 2) * 1.35, 0.0, 1.0)

    rgb = np.zeros((y.size, x.size, 3), dtype=np.float32)
    rgb[..., 0] = 0.03 + 0.11 * swirl + 0.07 * glow
    rgb[..., 1] = 0.05 + 0.08 * swirl + 0.03 * glow
    rgb[..., 2] = 0.09 + 0.22 * swirl + 0.12 * glow
    bg_ax.imshow(np.clip(rgb, 0.0, 1.0), extent=[0, 1, 0, 1], origin="lower",
                 interpolation="bicubic", aspect="auto")
    tint_ax = fig.add_axes([0, 0, 1, 1], zorder=-2.5)
    tint_ax.set_axis_off()
    tx = np.linspace(0.0, 1.0, 700, dtype=np.float32)
    ty = np.linspace(0.0, 1.0, 420, dtype=np.float32)
    txx, tyy = np.meshgrid(tx, ty)
    sun = np.clip(1.0 - np.sqrt((txx - 0.18) ** 2 + (tyy - 0.9) ** 2) * 1.6, 0.0, 1.0)
    haze = np.clip(1.0 - np.sqrt((txx - 0.55) ** 2 + (tyy - 0.82) ** 2) * 1.25, 0.0, 1.0)
    warm = np.clip(0.18 + 0.82 * np.maximum(sun, haze * 0.7), 0.0, 1.0)

    tint_rgb = np.zeros((ty.size, tx.size, 4), dtype=np.float32)
    tint_rgb[..., 0] = 0.98
    tint_rgb[..., 1] = 0.84
    tint_rgb[..., 2] = 0.45
    tint_rgb[..., 3] = warm * 0.55
    tint_img = tint_ax.imshow(tint_rgb, extent=[0, 1, 0, 1], origin="lower",
                              interpolation="bicubic", aspect="auto", alpha=0.0)
    return tint_ax, tint_img


def style_axis(ax, *, image=False):
    ax.set_facecolor(THEME["panel"])
    for spine in ax.spines.values():
        spine.set_edgecolor(THEME["spine"])
        spine.set_linewidth(1.0)
    ax.tick_params(colors=THEME["tick"], labelsize=7, length=0)
    for title_artist in (ax.title, getattr(ax, "_left_title", None), getattr(ax, "_right_title", None)):
        if title_artist is not None:
            title_artist.set_color(THEME["title"])
            title_artist.set_fontsize(10)
    if image:
        ax.set_xticks([])
        ax.set_yticks([])
    else:
        ax.grid(True, color=THEME["grid"], linewidth=0.6, alpha=0.7)
        ax.set_axisbelow(True)
        ax.margins(x=0)


def add_panel_cards(fig, axes):
    cards = []
    for ax in axes.values():
        bbox = ax.get_position()
        pad_x = 0.006
        pad_y = 0.014
        card = FancyBboxPatch(
            (bbox.x0 - pad_x, bbox.y0 - pad_y),
            bbox.width + pad_x * 2,
            bbox.height + pad_y * 2,
            boxstyle="round,pad=0.008,rounding_size=0.015",
            transform=fig.transFigure,
            linewidth=1.0,
            edgecolor=THEME["card_edge"],
            facecolor=THEME["panel_soft"],
            alpha=0.96,
            zorder=-2,
        )
        fig.add_artist(card)
        cards.append(card)
    return cards


def make_axis_badge(ax, x=0.02, y=0.98):
    return ax.text(
        x, y, "",
        transform=ax.transAxes,
        ha="left", va="top",
        color=THEME["text"], fontsize=7.5, family="monospace",
        bbox=dict(
            boxstyle="round,pad=0.28",
            facecolor="#0a111d",
            edgecolor=THEME["card_edge"],
            alpha=0.92,
        ),
        zorder=15,
    )


def apply_theme(fig, tint_ax, axes, cards, legends, text_roles, mix):
    fig.patch.set_facecolor(blend_color(THEME["bg"], "#3b2d11", mix * 0.45))
    tint_img = text_roles["bg_tint"]
    tint_img.set_alpha(0.7 * mix)


def build_figure():
    fig = plt.figure(figsize=(18.5, 10.2), facecolor=THEME["bg"])
    tint_ax, tint_img = add_figure_background(fig)
    gs = GridSpec(3, 6, figure=fig, hspace=0.42, wspace=0.32,
                  left=0.045, right=0.98, top=0.86, bottom=0.07)

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

    for name, axis in axes.items():
        style_axis(axis, image=name in IMAGE_PANELS)

    cards = add_panel_cards(fig, axes)

    return fig, axes, tint_ax, tint_img, cards


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


TRACE_FIELDNAMES = [
    "wall_seconds",
    "reset_count",
    "step",
    "cycle_mode",
    "cycle_count",
    "experiment",
    "symmetry_break",
    "drive_env",
    "gate_value",
    "signal_phase",
    "corr_value",
    "replay_period_ratio",
    "frequency_faithfulness",
    "output_omega",
    "output_replay_adv",
    "current_balance",
    "C_mean",
    "C_slow_mean",
    "R_mean",
    "S_mean",
    "dC_mean",
    "dC_pos_mean",
    "dC_neg_mean",
    "R_slow_mean",
    "retention_mean",
    "improve_mean",
    "degrade_mean",
    "surprise_gate_mean",
    "quiet_prune_mean",
    "S_growth_mean",
    "S_mass",
]


def make_trace_row(st, *, wall_seconds: float, reset_count: int):
    return {
        "wall_seconds": wall_seconds,
        "reset_count": reset_count,
        "step": st["step"],
        "cycle_mode": st["cycle_mode"],
        "cycle_count": st["cycle_count"],
        "experiment": st["experiment"],
        "symmetry_break": st["symmetry_break"],
        "drive_env": st["drive_env"],
        "gate_value": st["gate_value"],
        "signal_phase": st["signal_phase"],
        "corr_value": st["corr_value"],
        "replay_period_ratio": st["replay_period_ratio"],
        "frequency_faithfulness": st["frequency_faithfulness"],
        "output_omega": st["output_omega"],
        "output_replay_adv": st["output_replay_adv"],
        "current_balance": st.get("current_balance", math.nan),
        "C_mean": float(np.mean(st["C"])),
        "C_slow_mean": st["C_slow_mean"],
        "R_mean": float(np.mean(st["R"])),
        "S_mean": float(np.mean(st["S"])),
        "dC_mean": st["dC_mean"],
        "dC_pos_mean": st["dC_pos_mean"],
        "dC_neg_mean": st["dC_neg_mean"],
        "R_slow_mean": st["R_slow_mean"],
        "retention_mean": st["retention_mean"],
        "improve_mean": st["improve_mean"],
        "degrade_mean": st["degrade_mean"],
        "surprise_gate_mean": st["surprise_gate_mean"],
        "quiet_prune_mean": st["quiet_prune_mean"],
        "S_growth_mean": st["S_growth_mean"],
        "S_mass": st["S_mass"],
    }


def is_temporal_structural_snapshot(step: int) -> bool:
    return step > 0 and ((step - 1) % 10 == 0)


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
        color=THEME["text"], fontsize=9, family="monospace",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#0a111d", edgecolor=THEME["card_edge"], alpha=0.95),
        zorder=20,
    )
    text.set_visible(False)
    return text


def main():
    global plt
    args = parse_args()
    args.trace_every = max(1, int(args.trace_every))
    device = pick_device(args.device)
    plt = configure_matplotlib()

    genome_overrides = {}
    replay_episode_seeds = None
    replay_seed = None
    replay_slot = 0
    if args.load_genome:
        genome_path = resolve_path(args.load_genome)
        genome = load_genome(genome_path)
        genome_overrides = merged_genome_params(genome)
        replay_episode_seeds = genome.get("eval_episode_seeds")
        replay_slot = int(genome.get("eval_slot", 0))
        if replay_episode_seeds:
            replay_seed = int(replay_episode_seeds[0])
            genome_overrides["reset_seed"] = replay_seed
            genome_overrides["reset_slot"] = replay_slot
        args.experiment = genome.get("experiment", args.experiment)
        args.symmetry_break = genome.get("symmetry_break", args.symmetry_break)
        print(f"Loaded genome from {genome_path}  "
              f"(gen {genome['generation']}, fitness {genome['fitness']:.4f}, "
              f"{args.experiment}:{args.symmetry_break if args.symmetry_break is not None else 'baseline'})")
        if replay_seed is not None:
            print(f"  replay seed = {replay_seed}  slot = {replay_slot}")
            if len(replay_episode_seeds) > 1:
                print(f"  note: saved fitness is averaged over {len(replay_episode_seeds)} episodes; live replay uses the first saved episode.")
        else:
            print("  note: genome has no saved replay seed, so exact fitness replay is unavailable for this file.")
        for k, v in genome_overrides.items():
            if k in ("reset_seed", "reset_slot"):
                continue
            print(f"  {k:>15s} = {float(v):.6f}")

    sim = FieldDynamics(
        N=args.N,
        device=device,
        experiment=args.experiment,
        symmetry_break=args.symmetry_break,
        **genome_overrides,
    )

    trace_file = None
    trace_writer = None
    trace_path = resolve_path(args.trace_csv)
    next_trace_step = 1 if sim.experiment == "temporal_v1" else 0
    reset_count = 0
    trace_start_time = time.perf_counter()
    if trace_path is not None:
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        trace_file = open(trace_path, "w", newline="")
        trace_writer = csv.DictWriter(trace_file, fieldnames=TRACE_FIELDNAMES)
        trace_writer.writeheader()
        print(f"Tracing metrics to {trace_path} every {args.trace_every} simulation steps")

    plt.ion()
    fig, ax, tint_ax, tint_img, cards = build_figure()
    fig.canvas.manager.set_window_title("Field Dynamics v7")
    help_overlay = build_help_overlay(fig)
    header_text = fig.text(0.05, 0.955, "Field Dynamics v7",
                           ha="left", va="top", color=THEME["title"],
                           fontsize=20, fontweight="bold")
    subtitle_text = fig.text(0.05, 0.928,
                             "Live phase-space dashboard for structure, replay, and symmetry behavior",
                             ha="left", va="top", color=THEME["muted"], fontsize=10)
    status_text = fig.text(
        0.98, 0.956, "",
        ha="right", va="top",
        color=THEME["text"], fontsize=10.2, family="monospace",
        bbox=dict(boxstyle="round,pad=0.38", facecolor="#0a111d", edgecolor=THEME["card_edge"], alpha=0.95),
    )
    detail_text = fig.text(
        0.98, 0.925, "",
        ha="right", va="top",
        color=THEME["muted"], fontsize=8.5, family="monospace",
    )

    paused = False
    quit_flag = [False]
    show_help = [False]
    corr_history = []
    dominance_history = []

    def on_key(event):
        nonlocal paused, next_trace_step, reset_count
        if event.key in ("q", "escape"):
            quit_flag[0] = True
        elif event.key == " ":
            paused = not paused
        elif event.key == "r":
            sim.reset()
            corr_history.clear()
            dominance_history.clear()
            reset_count += 1
            next_trace_step = 1 if sim.experiment == "temporal_v1" else 0
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
    ax["field"].set_title("Phase Field", loc="left", pad=10)

    def _node_box(r, c, color, lw=1.5):
        ax["field"].add_patch(Rectangle(
            (c - 0.5, r - 0.5), 1.0, 1.0,
            linewidth=lw, edgecolor=color, facecolor="none", zorder=5
        ))
    _node_box(*sim.input_node, THEME["danger"], lw=1.8)
    _node_box(*sim.output_node, THEME["text"], lw=1.6)

    im_C = ax["C"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                          cmap="magma", vmin=0, vmax=1, aspect="equal")
    im_S = ax["S"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                          cmap="viridis", vmin=0, vmax=1, aspect="equal")
    im_R = ax["R"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                          cmap="inferno", vmin=0, vmax=1, aspect="equal")
    im_edge = ax["edge"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                                cmap="magma", vmin=0, vmax=1, aspect="equal")
    im_omega = ax["omega"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                                  cmap="coolwarm", vmin=-0.2, vmax=0.2, aspect="equal")
    im_magmap = ax["magmap"].imshow(scalar_blank, origin="lower", interpolation="nearest",
                                    cmap="cividis", vmin=0, vmax=2.0, aspect="equal")
    ax["C"].set_title("Coherence C", loc="left", pad=10)
    ax["S"].set_title("Structure S", loc="left", pad=10)
    ax["R"].set_title("Residual R", loc="left", pad=10)
    ax["edge"].set_title("Edge Memory", loc="left", pad=10)
    ax["omega"].set_title("Omega", loc="left", pad=10)
    ax["magmap"].set_title("Magnitude", loc="left", pad=10)

    line_xr, = ax["proj"].plot([], [], color=THEME["accent"], lw=1.25, label="Xr")
    line_xi, = ax["proj"].plot([], [], color="#ff8fb3", lw=1.15, alpha=0.95, label="Xi")
    line_mag, = ax["proj"].plot([], [], color=THEME["accent2"], lw=1.15, alpha=0.9, label="|X|")
    ax["proj"].set_ylim(-2.2, 2.2)
    ax["proj"].set_title("Projection History", loc="left", pad=10)
    ax["proj"].axhline(0, color=THEME["grid"], lw=0.7)
    proj_legend = ax["proj"].legend(fontsize=7, facecolor=THEME["panel"], edgecolor=THEME["card_edge"],
                                    labelcolor=THEME["muted"], loc="upper right")

    line_day_portrait, = ax["portrait"].plot([], [], color=THEME["accent3"], lw=1.1, alpha=0.95, label="day")
    line_night_portrait, = ax["portrait"].plot([], [], color=THEME["accent2"], lw=1.1, alpha=0.95, label="night")
    dot_current, = ax["portrait"].plot([], [], marker="o", ms=4.5, color=THEME["accent"], lw=0)
    ax["portrait"].set_xlim(-2.2, 2.2)
    ax["portrait"].set_ylim(-2.2, 2.2)
    ax["portrait"].set_title("Phase Portrait", loc="left", pad=10)
    ax["portrait"].axhline(0, color=THEME["grid"], lw=0.7)
    ax["portrait"].axvline(0, color=THEME["grid"], lw=0.7)
    portrait_legend = ax["portrait"].legend(fontsize=7, facecolor=THEME["panel"], edgecolor=THEME["card_edge"],
                                            labelcolor=THEME["muted"], loc="upper right")

    line_day_auto, = ax["autocorr"].plot([], [], color=THEME["accent3"], lw=1.2, label="day")
    line_night_auto, = ax["autocorr"].plot([], [], color=THEME["accent2"], lw=1.2, label="night")
    vline_day = ax["autocorr"].axvline(np.nan, color=THEME["accent3"], lw=1.0, ls="--", alpha=0.8)
    vline_night = ax["autocorr"].axvline(np.nan, color=THEME["accent2"], lw=1.0, ls="--", alpha=0.8)
    ax["autocorr"].set_ylim(-1.05, 1.05)
    ax["autocorr"].set_xlim(0, args.autocorr_lag)
    ax["autocorr"].set_title("Autocorrelation", loc="left", pad=10)
    ax["autocorr"].axhline(0, color=THEME["grid"], lw=0.7)
    autocorr_legend = ax["autocorr"].legend(fontsize=7, facecolor=THEME["panel"], edgecolor=THEME["card_edge"],
                                            labelcolor=THEME["muted"], loc="upper right")

    line_day_phase, = ax["phase"].plot([], [], color=THEME["accent3"], lw=1.2, label="day")
    line_night_phase, = ax["phase"].plot([], [], color=THEME["accent2"], lw=1.2, label="night")
    ax["phase"].set_title("Unwrapped Phase", loc="left", pad=10)
    ax["phase"].axhline(0, color=THEME["grid"], lw=0.7)
    phase_legend = ax["phase"].legend(fontsize=7, facecolor=THEME["panel"], edgecolor=THEME["card_edge"],
                                      labelcolor=THEME["muted"], loc="upper left")

    line_corr, = ax["corr"].plot([], [], color=THEME["accent2"], lw=1.2)
    ax["corr"].set_ylim(-1.1, 1.1)
    ax["corr"].set_title("Day / Night Corr", loc="left", pad=10)
    ax["corr"].axhline(sim.P["corrThr"], color=THEME["muted"], lw=0.9, ls="--", alpha=0.7)
    corr_zero = ax["corr"].axhline(0, color=THEME["grid"], lw=0.7, alpha=0.0)

    field_badge = make_axis_badge(ax["field"])
    portrait_badge = make_axis_badge(ax["portrait"])
    autocorr_badge = make_axis_badge(ax["autocorr"])
    phase_badge = make_axis_badge(ax["phase"])
    corr_badge = make_axis_badge(ax["corr"])
    legends = [proj_legend, portrait_legend, autocorr_legend, phase_legend]
    text_roles = {
        "title": header_text,
        "subtitle": subtitle_text,
        "status": status_text,
        "detail": detail_text,
        "help": help_overlay,
        "bg_tint": tint_img,
        "field_badge": field_badge,
        "portrait_badge": portrait_badge,
        "autocorr_badge": autocorr_badge,
        "phase_badge": phase_badge,
        "corr_badge": corr_badge,
    }
    theme_mix = 1.0 if sim.is_day() else 0.45 if sim.is_warmup() else 0.0
    apply_theme(fig, tint_ax, ax, cards, legends, text_roles, theme_mix)
    frame_t = time.perf_counter()
    hist = sim.HIST_LEN

    while not quit_flag[0]:
        if not paused:
            for _ in range(args.steps_per_frame):
                sim.update()
                if trace_writer is not None:
                    trace_state = sim.get_state()
                    trace_ready = trace_state["step"] >= next_trace_step
                    trace_aligned = (
                        trace_state["experiment"] != "temporal_v1"
                        or is_temporal_structural_snapshot(int(trace_state["step"]))
                    )
                    if trace_ready and trace_aligned:
                        trace_writer.writerow(
                            make_trace_row(
                                trace_state,
                                wall_seconds=time.perf_counter() - trace_start_time,
                                reset_count=reset_count,
                            )
                        )
                        trace_file.flush()
                        while next_trace_step <= trace_state["step"]:
                            next_trace_step += args.trace_every

        st = sim.get_state()
        mag = st["magnitude"]
        phase = st["phase"]
        dph = sim._current_drive_phase()
        target_theme_mix = 1.0 if sim.is_day() else 0.45 if sim.is_warmup() else 0.0
        theme_mix += (target_theme_mix - theme_mix) * 0.08
        apply_theme(fig, tint_ax, ax, cards, legends, text_roles, theme_mix)

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
            ax["corr"].set_title("Probe Balance / Corr", loc="left", pad=10)
            ax["corr"].set_ylim(-1.1, 1.1)
            line_corr.set_data(np.arange(len(dominance_history)), dominance_history)
            corr_zero.set_alpha(1.0)
        else:
            ax["corr"].set_title("Day / Night Corr", loc="left", pad=10)
            line_corr.set_data(np.arange(len(corr_history)), corr_history)
            corr_zero.set_alpha(0.0)
        ax["corr"].set_xlim(0, max(hist, len(corr_history), len(dominance_history)))

        fps = 1.0 / max(0.001, time.perf_counter() - frame_t)
        frame_t = time.perf_counter()
        if st["experiment"] == "symmetry_v1":
            status_text.set_text(
                f"step {st['step']:>6}   {st['cycle_mode'].upper():<8}   cycle {st['cycle_count']:>3}"
                f"   cue {st.get('cue_label', '--'):<2}   fps {fps:>3.0f}   {device}   N={args.N}"
            )
            detail_text.set_text(
                f"{st['experiment']}:{st['symmetry_break']}   target {st.get('chosen_probe', st['chosen_basin'])}"
                f"   balance {st.get('current_balance', st['current_dominance']): .3f}"
                f"   choice {format_score(st['choice_strength'])}   persist {format_score(st['overnight_persistence'])}"
                f"   dayT {format_period(st['day_period_est'])}   nightT {format_period(st['night_period_est'])}"
                f"   ratio {format_ratio(st['replay_period_ratio'])}   fit {format_score(st['optimizer_fitness'])}"
            )
        elif st["experiment"] == "temporal_v1":
            status_text.set_text(
                f"step {st['step']:>6}   {st['cycle_mode'].upper():<8}   cycle {st['cycle_count']:>3}"
                f"   temporal_v1   fps {fps:>3.0f}   {device}   N={args.N}"
            )
            detail_text.set_text(
                f"C {float(np.mean(st['C'])):.4f}   Cslow {st['C_slow_mean']:.4f}"
                f"   dC {st['dC_mean']:+.4f}   dC+ {st['dC_pos_mean']:.4f}   dC- {st['dC_neg_mean']:.4f}"
                f"   Rslow {st['R_slow_mean']:.4f}   Sgrow {st['S_growth_mean']:+.4f}"
                f"   hold {st['retention_mean']:.4f}   imp {st['improve_mean']:.4f}   deg {st['degrade_mean']:.4f}"
                f"   gate {st['surprise_gate_mean']:.4f}   prune {st['quiet_prune_mean']:.4f}"
            )
        else:
            status_text.set_text(
                f"step {st['step']:>6}   {st['cycle_mode'].upper():<8}   cycle {st['cycle_count']:>3}"
                f"   fps {fps:>3.0f}   {device}   N={args.N}"
            )
            detail_text.set_text(
                f"dayT {format_period(st['day_period_est'])}   nightT {format_period(st['night_period_est'])}"
                f"   ratio {format_ratio(st['replay_period_ratio'])}   omega {st['output_omega']:.4f}"
                f"   corr {st['corr_value']:.3f}   replayAdv {st['output_replay_adv']:.4f}"
                f"   optFit {format_score(st['optimizer_fitness'])}"
            )

        field_badge.set_text(
            f"{st['cycle_mode'].upper():<8}  step {st['step']}\n"
            f"drive {dph: .2f} rad\n"
            f"cue {st.get('cue_label', '--')}"
        )
        portrait_badge.set_text(
            f"Xr {sim.output_history[-1]: .3f}\n"
            f"Xi {sim.output_imag_history[-1]: .3f}\n"
            f"|X| {sim.output_mag_history[-1]: .3f}"
            if sim.output_history and sim.output_imag_history and sim.output_mag_history
            else "Awaiting history"
        )
        autocorr_badge.set_text(
            f"dayT   {format_period(st['day_period_est'])}\n"
            f"nightT {format_period(st['night_period_est'])}\n"
            f"ratio  {format_ratio(st['replay_period_ratio'])}"
        )
        phase_badge.set_text(
            f"faith {format_score(st['frequency_faithfulness'])}\n"
            f"omega {st['output_omega']: .4f}\n"
            f"replay {st.get('output_replay_adv', 0.0): .4f}"
        )
        if st["experiment"] == "symmetry_v1":
            corr_badge.set_text(
                f"balance {st.get('current_balance', st['current_dominance']): .3f}\n"
                f"choice  {format_score(st['choice_strength'])}\n"
                f"fit     {format_score(st['optimizer_fitness'])}"
            )
        elif st["experiment"] == "temporal_v1":
            corr_badge.set_text(
                f"hold   {st['retention_mean']:.4f}\n"
                f"imp    {st['improve_mean']:.4f}\n"
                f"gate   {st['surprise_gate_mean']:.4f}\n"
                f"prune  {st['quiet_prune_mean']:.4f}"
            )
        else:
            corr_badge.set_text(
                f"corr  {st['corr_value']: .3f}\n"
                f"dwell {st['best_dwell']}\n"
                f"fit   {format_score(st['optimizer_fitness'])}"
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
    if trace_file is not None:
        trace_file.close()
    print("Done.")


if __name__ == "__main__":
    main()
