import matplotlib.pyplot as plt
import numpy as np

from paper3_qwz_common import (
    configure_matplotlib,
    finalize_figure,
    plateau_suppression_curves,
    sigma_xy_dissipative,
    sigma_xy_dissipative_curve,
)


OUTFILE = "figure-3-line-cuts.png"


def main():
    configure_matplotlib()

    masses = np.linspace(-3.0, 3.0, 401)
    gammas = [0.05, 0.15, 0.35, 0.7, 1.0]
    colors = plt.cm.viridis(np.linspace(0.15, 0.85, len(gammas)))

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14.2, 5.5))
    fig.suptitle("Figure 3 - Line Cuts and Cusp Enhancement", fontsize=16, y=0.98)

    for color, gamma in zip(colors, gammas):
        curve = sigma_xy_dissipative_curve(masses, gamma, n=210)
        ax_left.plot(masses, curve, color=color, linewidth=2.2, label=rf"$\gamma={gamma:.2f}$")

    ax_left.axhline(1.0, color="0.7", linestyle="--", linewidth=1.1)
    ax_left.axhline(-1.0, color="0.7", linestyle="--", linewidth=1.1)
    ax_left.axvline(-2.0, color="0.65", linestyle=":", linewidth=1.0)
    ax_left.axvline(0.0, color="0.65", linestyle=":", linewidth=1.0)
    ax_left.axvline(2.0, color="0.65", linestyle=":", linewidth=1.0)
    ax_left.set_title(r"(a) $\sigma_{xy}^{\mathrm{eff}}$ vs. $M$ at fixed $\gamma$", fontsize=13)
    ax_left.set_xlabel(r"Mass Parameter $M$")
    ax_left.set_ylabel(r"$\sigma_{xy}^{\mathrm{eff}}\ (e^2/h)$")
    ax_left.set_xlim(-3.0, 3.0)
    ax_left.set_ylim(-1.23, 1.23)
    ax_left.legend(frameon=True, loc="lower left")

    scale_values = np.linspace(0.05, 1.0, 26)
    single_minus, single_plus, doubled = plateau_suppression_curves(
        scale_values, sigma_xy_dissipative, delta=0.1, n=210
    )

    ax_right.plot(scale_values, single_minus, color="#356da6", linewidth=2.3, label=r"Near $M=-2$ (single)")
    ax_right.plot(
        scale_values,
        single_plus,
        color="#356da6",
        linewidth=2.3,
        linestyle="--",
        label=r"Near $M=+2$ (single)",
    )
    ax_right.plot(scale_values, doubled, color="#c0392b", linewidth=2.5, label=r"Near $M=0$ (doubled)")
    ax_right.annotate(
        "doubled cusp\nsuppresses more strongly",
        xy=(0.55, doubled[13]),
        xytext=(0.47, doubled[13] + 0.085),
        color="#c0392b",
        fontsize=11,
        arrowprops={"arrowstyle": "->", "color": "#c0392b", "lw": 1.1},
    )

    ax_right.set_title(r"(b) Plateau suppression: $M=0$ vs. $M=\pm 2$", fontsize=13)
    ax_right.set_xlabel(r"Dephasing Rate $\gamma$")
    ax_right.set_ylabel(r"Plateau suppression $\delta \sigma_{xy}\ (e^2/h)$")
    ax_right.set_xlim(0.0, 1.02)
    ax_right.set_ylim(0.0, max(doubled) * 1.18)
    ax_right.legend(frameon=True, loc="upper left")

    fig.subplots_adjust(wspace=0.18, top=0.83)
    finalize_figure(fig, OUTFILE)


if __name__ == "__main__":
    main()
