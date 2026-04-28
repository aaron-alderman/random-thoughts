import matplotlib.pyplot as plt
import numpy as np

from paper3_qwz_common import (
    configure_matplotlib,
    finalize_figure,
    plateau_suppression_curves,
    sigma_xy_dissipative,
    sigma_xy_dissipative_curve,
    sigma_xy_thermal,
    sigma_xy_thermal_curve,
)


OUTFILE = "figure-5-thermal-comparison.png"


def main():
    configure_matplotlib()

    masses = np.linspace(-3.0, 3.0, 401)
    representative_scale = 0.35
    scale_values = np.linspace(0.2, 1.0, 20)

    dissipative_curve = sigma_xy_dissipative_curve(masses, representative_scale, n=210)
    thermal_curve = sigma_xy_thermal_curve(masses, representative_scale, n=210)

    diss_single_minus, _, diss_doubled = plateau_suppression_curves(
        scale_values, sigma_xy_dissipative, delta=0.12, n=210
    )
    therm_single_minus, _, therm_doubled = plateau_suppression_curves(
        scale_values, sigma_xy_thermal, delta=0.12, n=210
    )

    ratio_diss = diss_doubled / diss_single_minus
    ratio_therm = therm_doubled / therm_single_minus

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14.2, 5.5))
    fig.suptitle("Figure 5 - Dissipative and Thermal Broadening Compared", fontsize=16, y=0.98)

    ax_left.plot(masses, dissipative_curve, color="#2c7fb8", linewidth=2.5, label=r"Dissipative: $\gamma=0.35$")
    ax_left.plot(
        masses,
        thermal_curve,
        color="#d95f0e",
        linewidth=2.5,
        linestyle="--",
        label=r"Thermal: $T=0.35$",
    )
    ax_left.axvline(-2.0, color="0.65", linestyle=":", linewidth=1.0)
    ax_left.axvline(0.0, color="0.65", linestyle=":", linewidth=1.0)
    ax_left.axvline(2.0, color="0.65", linestyle=":", linewidth=1.0)
    ax_left.axhline(1.0, color="0.7", linestyle="--", linewidth=1.0)
    ax_left.axhline(-1.0, color="0.7", linestyle="--", linewidth=1.0)
    ax_left.set_title(r"(a) Matched broadening scale: line cuts in $M$", fontsize=13)
    ax_left.set_xlabel(r"Mass Parameter $M$")
    ax_left.set_ylabel(r"$\sigma_{xy}\ (e^2/h)$")
    ax_left.set_xlim(-3.0, 3.0)
    ax_left.set_ylim(-1.23, 1.23)
    ax_left.legend(frameon=True, loc="lower left")

    ax_right.plot(scale_values, ratio_diss, color="#2c7fb8", linewidth=2.5, label="Dissipative ratio")
    ax_right.plot(scale_values, ratio_therm, color="#d95f0e", linewidth=2.5, linestyle="--", label="Thermal ratio")
    ax_right.axhline(1.0, color="0.45", linestyle=":", linewidth=1.0)
    ax_right.annotate(
        "dissipative asymmetry\nstays stronger",
        xy=(0.7, ratio_diss[12]),
        xytext=(0.58, ratio_diss[12] + 0.16),
        color="#2c7fb8",
        fontsize=11,
        arrowprops={"arrowstyle": "->", "color": "#2c7fb8", "lw": 1.1},
    )
    ax_right.set_title(r"(b) Ratio $\delta\sigma(M \approx 0) / \delta\sigma(M \approx -2)$", fontsize=13)
    ax_right.set_xlabel("Broadening scale")
    ax_right.set_ylabel("Suppression ratio")
    ax_right.set_xlim(0.18, 1.02)
    ax_right.set_ylim(0.95, max(ratio_diss.max(), ratio_therm.max()) * 1.12)
    ax_right.legend(frameon=True, loc="upper right")

    fig.subplots_adjust(wspace=0.2, top=0.83)
    finalize_figure(fig, OUTFILE)


if __name__ == "__main__":
    main()
