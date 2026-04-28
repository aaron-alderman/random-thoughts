import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np

from paper3_qwz_common import configure_matplotlib, finalize_figure, pi_tick_data, qzw_fields


OUTFILE = "figure-4-berry-curvature.png"


def main():
    configure_matplotlib()

    masses = [-1.0, 0.0, 2.0]
    titles = [
        r"$M=-1$: plateau interior",
        r"$M=0$: doubled closure",
        r"$M=+2$: single closure",
    ]

    fig, axes = plt.subplots(1, 3, figsize=(15.2, 4.8), constrained_layout=True)
    fig.suptitle(r"Figure 4 - Berry Curvature $\Omega(k)$ Across the Brillouin Zone", fontsize=16, y=1.04)

    ticks, labels = pi_tick_data()
    norm = colors.SymLogNorm(linthresh=0.05, linscale=1.0, vmin=-3.0, vmax=3.0, base=10)
    image = None

    for ax, mass, title in zip(axes, masses, titles):
        fields = qzw_fields(mass, n=251)
        image = ax.pcolormesh(
            fields["kx"],
            fields["ky"],
            fields["omega"],
            cmap="coolwarm",
            shading="auto",
            norm=norm,
        )
        ax.set_title(title, fontsize=12)
        ax.set_xlabel(r"$k_x$")
        ax.set_ylabel(r"$k_y$")
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
        ax.set_yticks(ticks)
        ax.set_yticklabels(labels)

        if mass == 0.0:
            ax.plot([np.pi, 0.0], [0.0, np.pi], "^", ms=8, mfc="none", mec="black", mew=1.2)
        elif mass == 2.0:
            ax.plot(np.pi, np.pi, "^", ms=8, mfc="none", mec="black", mew=1.2)

    cbar = fig.colorbar(image, ax=axes, shrink=0.92, pad=0.02)
    cbar.set_label(r"$\Omega(k)$")
    finalize_figure(fig, OUTFILE)


if __name__ == "__main__":
    main()
