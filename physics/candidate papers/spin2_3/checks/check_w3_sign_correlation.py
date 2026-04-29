from __future__ import annotations

import numpy as np


sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def qmat(chi: float, theta: float, phi: float) -> np.ndarray:
    x0 = np.cos(chi)
    s = np.sin(chi)
    x1 = s * np.cos(theta)
    x2 = s * np.sin(theta) * np.cos(phi)
    x3 = s * np.sin(theta) * np.sin(phi)
    return x0 * I2 - 1j * (x1 * sx + x2 * sy + x3 * sz)


def qmat_dagger(chi: float, theta: float, phi: float) -> np.ndarray:
    return qmat(chi, theta, phi).conj().T


def deriv(f, chi: float, theta: float, phi: float, idx: int, h: float = 1e-5) -> np.ndarray:
    args = [chi, theta, phi]
    args[idx] += h
    qp = f(*args)
    args[idx] -= 2 * h
    qm = f(*args)
    return (qp - qm) / (2 * h)


def compute_w3(f, n: int = 28) -> complex:
    chis = np.linspace(1e-4, np.pi - 1e-4, n)
    thetas = np.linspace(1e-4, np.pi - 1e-4, n)
    phis = np.linspace(0, 2 * np.pi, n, endpoint=False)
    dchi = chis[1] - chis[0]
    dtheta = thetas[1] - thetas[0]
    dphi = phis[1] - phis[0]

    total = 0.0 + 0.0j
    for chi in chis:
        for theta in thetas:
            for phi in phis:
                q = f(chi, theta, phi)
                qinv = q.conj().T
                a = qinv @ deriv(f, chi, theta, phi, 0)
                b = qinv @ deriv(f, chi, theta, phi, 1)
                c = qinv @ deriv(f, chi, theta, phi, 2)
                dens = np.trace(
                    a @ b @ c
                    - a @ c @ b
                    + b @ c @ a
                    - b @ a @ c
                    + c @ a @ b
                    - c @ b @ a
                )
                total += dens * dchi * dtheta * dphi

    return total / (24 * np.pi**2)


def main() -> None:
    w_q = compute_w3(qmat)
    w_qdag = compute_w3(qmat_dagger)

    print(f"W3[q]      ~= {w_q.real:.6f} {w_q.imag:+.6e}i")
    print(f"W3[q^dag]  ~= {w_qdag.real:.6f} {w_qdag.imag:+.6e}i")
    print(f"sum        ~= {(w_q + w_qdag).real:.6f} {(w_q + w_qdag).imag:+.6e}i")
    print()
    print("Expected sign relation:")
    print("  - q -> q^dagger flips the winding sign in the current convention.")
    print("  - Under the corpus orientation dictionary, the same global reversal flips kappa_u.")


if __name__ == "__main__":
    main()
