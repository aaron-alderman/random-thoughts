from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


FIGURE_DIR = Path(__file__).with_name("figures")


def configure_matplotlib():
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 240,
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "legend.fontsize": 10,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "mathtext.fontset": "dejavusans",
        }
    )


def output_path(filename):
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    return FIGURE_DIR / filename


def finalize_figure(fig, filename):
    outfile = output_path(filename)
    fig.savefig(outfile, bbox_inches="tight", facecolor="white")
    print(f"Wrote {outfile}")


def pi_tick_data():
    return [-np.pi, 0.0, np.pi], [r"$-\pi$", "0", r"$\pi$"]


def qzw_grid(n):
    k = np.linspace(-np.pi, np.pi, n, endpoint=False)
    kx, ky = np.meshgrid(k, k, indexing="xy")
    sinx = np.sin(kx)
    siny = np.sin(ky)
    cosx = np.cos(kx)
    cosy = np.cos(ky)
    return k, kx, ky, sinx, siny, cosx, cosy


def qzw_fields(mass, n):
    _, kx, ky, sinx, siny, cosx, cosy = qzw_grid(n)
    dz = mass + cosx + cosy
    d2 = sinx**2 + siny**2 + dz**2
    d = np.sqrt(d2)
    cross_x = sinx * cosy
    cross_y = cosx * siny
    cross_z = cosx * cosy
    omega = 0.5 * (sinx * cross_x + siny * cross_y + dz * cross_z) / (d**3 + 1e-12)
    return {
        "kx": kx,
        "ky": ky,
        "dz": dz,
        "d2": d2,
        "d": d,
        "omega": omega,
    }


def band_energy(mass, n=121):
    fields = qzw_fields(mass, n)
    return fields["kx"], fields["ky"], np.sqrt(fields["d2"])


def sigma_xy_dissipative(mass, gamma, n=220):
    fields = qzw_fields(mass, n)
    f_gamma = (4.0 * fields["d2"]) / (4.0 * fields["d2"] + gamma**2)
    dk = 2.0 * np.pi / n
    return np.sum(fields["omega"] * f_gamma) * dk**2 / (2.0 * np.pi)


def sigma_xy_thermal(mass, temperature, n=220):
    fields = qzw_fields(mass, n)
    occupation_weight = np.tanh(fields["d"] / (2.0 * temperature + 1e-12))
    dk = 2.0 * np.pi / n
    return np.sum(fields["omega"] * occupation_weight) * dk**2 / (2.0 * np.pi)


def sigma_xy_dissipative_curve(masses, gamma, n=220):
    return np.array([sigma_xy_dissipative(mass, gamma, n=n) for mass in masses], dtype=float)


def sigma_xy_thermal_curve(masses, temperature, n=220):
    return np.array([sigma_xy_thermal(mass, temperature, n=n) for mass in masses], dtype=float)


def sigma_xy_dissipative_phase_map(masses, gammas, n=160):
    _, _, _, sinx, siny, cosx, cosy = qzw_grid(n)
    cross_x = sinx * cosy
    cross_y = cosx * siny
    cross_z = cosx * cosy
    dk = 2.0 * np.pi / n
    out = np.empty((len(gammas), len(masses)), dtype=float)

    for idx, mass in enumerate(masses):
        dz = mass + cosx + cosy
        d2 = sinx**2 + siny**2 + dz**2
        d = np.sqrt(d2)
        omega = 0.5 * (sinx * cross_x + siny * cross_y + dz * cross_z) / (d**3 + 1e-12)
        f_gamma = (4.0 * d2)[None, :, :] / (4.0 * d2[None, :, :] + gammas[:, None, None] ** 2)
        out[:, idx] = np.sum(omega[None, :, :] * f_gamma, axis=(1, 2)) * dk**2 / (2.0 * np.pi)

    return out


def plateau_suppression_curves(scale_values, sigma_fn, delta=0.1, n=220):
    single_minus = np.array(
        [1.0 - abs(sigma_fn(-2.0 + delta, scale, n=n)) for scale in scale_values], dtype=float
    )
    single_plus = np.array(
        [1.0 - abs(sigma_fn(2.0 - delta, scale, n=n)) for scale in scale_values], dtype=float
    )
    doubled = np.array(
        [
            0.5
            * (
                1.0 - abs(sigma_fn(-delta, scale, n=n))
                + 1.0 - abs(sigma_fn(delta, scale, n=n))
            )
            for scale in scale_values
        ],
        dtype=float,
    )
    return single_minus, single_plus, doubled
