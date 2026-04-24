"""
Phase-portrait helper for the reduced two-branch system in kernels/dynamics.md.

We plot the (rho, Phi) dynamics:
  dot(rho) = -kappa * sinh(2 rho) * cos(Phi)
  dot(Phi) =  2 omega - 2 kappa * cosh(2 rho) * sin(Phi)

And overlay the two organizing boundaries:
  Locking boundary:      |omega| = |kappa| cosh(2 rho)
  Persistence boundary:  kappa cosh(2 rho) cos(Phi) = gamma
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--omega", type=float, required=True)
    ap.add_argument("--kappa", type=float, required=True)
    ap.add_argument("--gamma", type=float, required=True)
    ap.add_argument("--rho-max", type=float, default=2.0)
    ap.add_argument("--n", type=int, default=80, help="Grid size per axis for the vector field.")
    ap.add_argument("--out", type=str, default="checks/phase_portrait.png")
    args = ap.parse_args()

    omega = float(args.omega)
    kappa = float(args.kappa)
    gamma = float(args.gamma)
    rho_max = float(args.rho_max)
    n = int(args.n)

    if n < 10:
        raise SystemExit("--n must be >= 10")
    if rho_max <= 0:
        raise SystemExit("--rho-max must be > 0")

    # Grid: rho in [-rho_max, rho_max], Phi in [-pi, pi].
    rhos = np.linspace(-rho_max, rho_max, n)
    phis = np.linspace(-math.pi, math.pi, n)
    RHO, PHI = np.meshgrid(rhos, phis, indexing="xy")

    # Vector field.
    drho = -kappa * np.sinh(2 * RHO) * np.cos(PHI)
    dphi = 2 * omega - 2 * kappa * np.cosh(2 * RHO) * np.sin(PHI)

    speed = np.hypot(drho, dphi)
    # Avoid division by 0 in the color normalization; keep a little floor.
    speed = np.maximum(speed, 1e-12)

    fig, ax = plt.subplots(figsize=(10.5, 6.0), dpi=140)

    ax.streamplot(
        RHO,
        PHI,
        drho,
        dphi,
        density=1.25,
        color=np.log10(speed),
        linewidth=0.9,
        cmap="viridis",
        arrowsize=1.0,
    )

    # Overlay locking boundary: |omega| = |kappa| cosh(2 rho).
    # If |omega| < |kappa|, the equality cannot be met (cosh >= 1), so the system is
    # locked for all rho in the reduced criterion.
    kk = abs(kappa)
    ww = abs(omega)
    if kk > 0 and ww >= kk:
        rho_lock = 0.5 * math.acosh(ww / kk)
        if rho_lock <= rho_max:
            ax.axvline(+rho_lock, color="white", lw=1.0, ls="--", alpha=0.8, label="locking boundary")
            ax.axvline(-rho_lock, color="white", lw=1.0, ls="--", alpha=0.8)
        else:
            # Boundary exists but lies outside view.
            pass

    # Overlay persistence boundary: kappa cosh(2 rho) cos(Phi) = gamma.
    # Solve for Phi(rho): cos(Phi) = gamma / (kappa cosh(2 rho)).
    # Draw where |rhs| <= 1.
    if kappa != 0:
        rho_curve = np.linspace(-rho_max, rho_max, 600)
        rhs = gamma / (kappa * np.cosh(2 * rho_curve))
        ok = np.abs(rhs) <= 1.0
        if np.any(ok):
            phi0 = np.arccos(np.clip(rhs[ok], -1.0, 1.0))
            # Two branches in [-pi, pi]: +phi0 and -phi0
            ax.plot(rho_curve[ok], +phi0, color="tomato", lw=1.2, alpha=0.95, label="persistence boundary")
            ax.plot(rho_curve[ok], -phi0, color="tomato", lw=1.2, alpha=0.95)

    ax.set_title(r"Reduced $(\rho,\Phi)$ Phase Portrait")
    ax.set_xlabel(r"$\rho$")
    ax.set_ylabel(r"$\Phi$")
    ax.set_xlim(-rho_max, rho_max)
    ax.set_ylim(-math.pi, math.pi)
    ax.set_yticks([-math.pi, -math.pi / 2, 0, math.pi / 2, math.pi])
    ax.set_yticklabels([r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$"])

    # Lightweight legend: only show once per label.
    handles, labels = ax.get_legend_handles_labels()
    if labels:
        uniq = {}
        for h, lab in zip(handles, labels):
            uniq.setdefault(lab, h)
        ax.legend(uniq.values(), uniq.keys(), loc="upper right", framealpha=0.85)

    txt = f"omega={omega:g}, kappa={kappa:g}, gamma={gamma:g}"
    ax.text(
        0.01,
        0.99,
        txt,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=9,
        color="black",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white", alpha=0.85, edgecolor="none"),
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out)
    print(str(out))


if __name__ == "__main__":
    main()

