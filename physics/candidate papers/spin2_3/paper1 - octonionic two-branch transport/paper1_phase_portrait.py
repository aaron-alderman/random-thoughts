import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTFILE = Path(__file__).with_name("paper1_phase_portrait.png")


def classify(kappa, omega, gamma, rho, phi):
    locked = abs(omega) <= abs(kappa) * np.cosh(2.0 * rho)
    persistent = kappa * np.cosh(2.0 * rho) * np.cos(phi) > gamma

    out = np.full(rho.shape, 0, dtype=int)
    out[~locked] = 0
    out[locked & ~persistent] = 1
    if kappa > 0:
        out[locked & persistent] = 2
    else:
        out[locked & persistent] = 3
    return out


def vector_field(kappa, omega, rho, phi):
    drho = -kappa * np.sinh(2.0 * rho) * np.cos(phi)
    dphi = 2.0 * omega - 2.0 * kappa * np.cosh(2.0 * rho) * np.sin(phi)
    return drho, dphi


def draw_panel(ax, kappa, omega, gamma, rho_lim):
    rho = np.linspace(-rho_lim, rho_lim, 401)
    phi = np.linspace(0.0, 2.0 * math.pi, 401)
    RHO, PHI = np.meshgrid(rho, phi)

    classes = classify(kappa, omega, gamma, RHO, PHI)

    colors = ["#d9d9d9", "#f4a261", "#2a9d8f", "#457b9d"]
    labels = ["Dephased", "Frustrated", "Constructive", "Inverted"]
    cmap = plt.matplotlib.colors.ListedColormap(colors)

    ax.pcolormesh(RHO, PHI, classes, shading="auto", cmap=cmap, vmin=-0.5, vmax=3.5)

    drho, dphi = vector_field(kappa, omega, RHO, PHI)
    speed = np.hypot(drho, dphi)
    drho = drho / (speed + 1e-9)
    dphi = dphi / (speed + 1e-9)
    stride = 24
    ax.quiver(
        RHO[::stride, ::stride],
        PHI[::stride, ::stride],
        drho[::stride, ::stride],
        dphi[::stride, ::stride],
        color="black",
        alpha=0.4,
        scale=35,
        width=0.0022,
    )

    if abs(omega / kappa) >= 1.0:
        rho_lock = 0.5 * np.arccosh(abs(omega / kappa))
        for sign in (-1.0, 1.0):
            ax.axvline(sign * rho_lock, color="black", linestyle="--", linewidth=1.2, alpha=0.9)

    rho_curve = np.linspace(-rho_lim, rho_lim, 1200)
    rhs = gamma / (kappa * np.cosh(2.0 * rho_curve))
    mask = np.abs(rhs) <= 1.0
    phi_curve = np.arccos(np.clip(rhs[mask], -1.0, 1.0))
    ax.plot(rho_curve[mask], phi_curve, color="white", linewidth=1.7)
    ax.plot(rho_curve[mask], 2.0 * math.pi - phi_curve, color="white", linewidth=1.7)

    if abs(omega / kappa) <= 1.0:
        phi0 = math.asin(omega / kappa)
        node_pts = [(0.0, phi0), (0.0, math.pi - phi0)]
        for x, y in node_pts:
            ax.plot(x, y, "o", color="black", markersize=5)

    if abs(omega / kappa) >= 1.0:
        rho_c = 0.5 * math.acosh(abs(omega / kappa))
        center_pts = [
            (rho_c, math.pi / 2.0),
            (-rho_c, math.pi / 2.0),
            (rho_c, 3.0 * math.pi / 2.0),
            (-rho_c, 3.0 * math.pi / 2.0),
        ]
        for x, y in center_pts:
            ax.plot(x, y, marker="o", markerfacecolor="white", markeredgecolor="black", markersize=5)

    title = rf"$\kappa_u = {kappa:+.1f},\ \omega = {omega:.2f},\ \gamma = {gamma:.2f}$"
    ax.set_title(title, fontsize=11)
    ax.set_xlabel(r"$\rho$")
    ax.set_xlim(-rho_lim, rho_lim)
    ax.set_ylim(0.0, 2.0 * math.pi)
    ax.set_yticks([0.0, math.pi / 2.0, math.pi, 3.0 * math.pi / 2.0, 2.0 * math.pi])
    ax.set_yticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.grid(False)

    return colors, labels


def main():
    omega = 1.35
    gamma = 0.35
    rho_lim = 1.4

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.6), constrained_layout=True, sharey=True)

    colors, labels = draw_panel(axes[0], 1.0, omega, gamma, rho_lim)
    draw_panel(axes[1], -1.0, omega, gamma, rho_lim)
    axes[0].set_ylabel(r"$\Phi$")

    handles = [
        plt.matplotlib.patches.Patch(color=colors[i], label=labels[i])
        for i in range(len(labels))
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.03))
    fig.suptitle("Phase Portrait and Forced Transport Classes", fontsize=14)
    fig.savefig(OUTFILE, dpi=220, bbox_inches="tight")
    print(f"Wrote {OUTFILE}")


if __name__ == "__main__":
    main()
