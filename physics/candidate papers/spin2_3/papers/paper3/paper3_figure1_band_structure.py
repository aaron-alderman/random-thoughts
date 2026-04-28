from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

import matplotlib.pyplot as plt
import numpy as np

from paper3_qwz_common import band_energy, configure_matplotlib, finalize_figure, pi_tick_data


OUTFILE = "figure-1-energy-band-structure.png"


def draw_panel(ax, mass, subtitle):
    kx, ky, energy = band_energy(mass, n=121)
    ax.plot_surface(kx, ky, energy, cmap="Blues", linewidth=0, antialiased=True, alpha=0.85)
    ax.plot_surface(kx, ky, -energy, cmap="Reds", linewidth=0, antialiased=True, alpha=0.78)

    ticks, labels = pi_tick_data()
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels)
    ax.set_yticks(ticks)
    ax.set_yticklabels(labels)
    ax.set_xlabel(r"$k_x$")
    ax.set_ylabel(r"$k_y$")
    ax.set_zlabel(r"$E(k)$")
    ax.set_title(subtitle, fontsize=11, pad=10)
    ax.view_init(elev=28, azim=-55)
    ax.set_box_aspect((1, 1, 0.65))


def main():
    configure_matplotlib()

    fig = plt.figure(figsize=(15.5, 5.3))
    fig.suptitle("Figure 1 - QWZ Band Structure at Topological Phase Boundaries", fontsize=16, y=0.97)

    masses = [-2.0, 0.0, 2.0]
    subtitles = [
        r"$M=-2$: gap closure at $\Gamma=(0,0)$",
        r"$M=0$: closure at $X=(\pi,0)$ and $Y=(0,\pi)$",
        r"$M=+2$: gap closure at $(\pi,\pi)$",
    ]

    for index, (mass, subtitle) in enumerate(zip(masses, subtitles), start=1):
        ax = fig.add_subplot(1, 3, index, projection="3d")
        draw_panel(ax, mass, subtitle)

    fig.subplots_adjust(top=0.83, wspace=0.08)
    finalize_figure(fig, OUTFILE)


if __name__ == "__main__":
    main()
