import matplotlib.pyplot as plt
import numpy as np

from paper3_qwz_common import configure_matplotlib, finalize_figure, sigma_xy_dissipative_phase_map


OUTFILE = "figure-2-phase-map.png"


def main():
    configure_matplotlib()

    masses = np.linspace(-3.0, 3.0, 80)
    gammas = np.linspace(0.0, 1.1, 50)
    sigma = sigma_xy_dissipative_phase_map(masses, gammas, n=150)
    mass_grid, gamma_grid = np.meshgrid(masses, gammas)

    fig, ax = plt.subplots(figsize=(10.6, 6.2))
    levels = np.linspace(-1.0, 1.0, 33)
    contour = ax.contourf(mass_grid, gamma_grid, sigma, levels=levels, cmap="RdBu_r", extend="both")

    for location in (-2.0, 0.0, 2.0):
        ax.axvline(location, color="0.25", linestyle="--", linewidth=1.2, alpha=0.8)

    ax.annotate(
        "single\ncusp",
        xy=(-2.0, 0.14),
        xytext=(-2.18, 0.55),
        color="#c63d2f",
        ha="center",
        fontsize=11,
        arrowprops={"arrowstyle": "->", "color": "#c63d2f", "lw": 1.2},
    )
    ax.annotate(
        "doubled\ncusp",
        xy=(0.0, 0.14),
        xytext=(0.0, 0.55),
        color="#c63d2f",
        ha="center",
        fontsize=11,
        arrowprops={"arrowstyle": "->", "color": "#c63d2f", "lw": 1.2},
    )
    ax.annotate(
        "single\ncusp",
        xy=(2.0, 0.14),
        xytext=(2.02, 0.55),
        color="#c63d2f",
        ha="center",
        fontsize=11,
        arrowprops={"arrowstyle": "->", "color": "#c63d2f", "lw": 1.2},
    )

    box = {"boxstyle": "round,pad=0.18", "facecolor": "#34495e", "edgecolor": "none", "alpha": 0.6}
    ax.text(-2.7, 0.055, r"$C=0$", color="white", fontsize=12, bbox=box)
    ax.text(-1.18, 0.055, r"$C=+1$", color="white", fontsize=12, bbox=box)
    ax.text(0.76, 0.055, r"$C=-1$", color="white", fontsize=12, bbox=box)
    ax.text(2.53, 0.055, r"$C=0$", color="white", fontsize=12, bbox=box)

    cbar = fig.colorbar(contour, ax=ax, pad=0.02)
    cbar.set_label(r"$\sigma_{xy}^{\mathrm{eff}}\ (e^2/h)$")

    ax.set_title(r"Figure 2 - Dissipative Hall Phase Map $\sigma_{xy}^{\mathrm{eff}}(M,\gamma)$", fontsize=16)
    ax.set_xlabel(r"Mass Parameter $M$")
    ax.set_ylabel(r"Dephasing Rate $\gamma$")
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(0.0, 1.1)
    ax.set_xticks(np.arange(-3, 4, 1))

    finalize_figure(fig, OUTFILE)


if __name__ == "__main__":
    main()
