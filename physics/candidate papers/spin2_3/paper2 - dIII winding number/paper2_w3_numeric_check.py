import numpy as np


sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
Id = np.eye(2, dtype=complex)


def qmat(chi, theta, phi):
    x0 = np.cos(chi)
    s = np.sin(chi)
    x1 = s * np.cos(theta)
    x2 = s * np.sin(theta) * np.cos(phi)
    x3 = s * np.sin(theta) * np.sin(phi)
    return x0 * Id - 1j * (x1 * sx + x2 * sy + x3 * sz)


def deriv(f, chi, theta, phi, idx, h=1e-5):
    args = [chi, theta, phi]
    args[idx] += h
    qp = f(*args)
    args[idx] -= 2 * h
    qm = f(*args)
    return (qp - qm) / (2 * h)


def compute_w3(n=28):
    chis = np.linspace(1e-4, np.pi - 1e-4, n)
    thetas = np.linspace(1e-4, np.pi - 1e-4, n)
    phis = np.linspace(0, 2 * np.pi, n, endpoint=False)
    dchi = chis[1] - chis[0]
    dtheta = thetas[1] - thetas[0]
    dphi = phis[1] - phis[0]

    W = 0.0 + 0.0j
    for chi in chis:
        for theta in thetas:
            for phi in phis:
                q = qmat(chi, theta, phi)
                qinv = q.conj().T
                a = qinv @ deriv(qmat, chi, theta, phi, 0)
                b = qinv @ deriv(qmat, chi, theta, phi, 1)
                c = qinv @ deriv(qmat, chi, theta, phi, 2)
                dens = np.trace(
                    a @ b @ c
                    - a @ c @ b
                    + b @ c @ a
                    - b @ a @ c
                    + c @ a @ b
                    - c @ b @ a
                )
                W += dens * dchi * dtheta * dphi

    return W / (24 * np.pi**2)


if __name__ == "__main__":
    W3 = compute_w3()
    print(f"W3 ~= {W3.real:.6f} {W3.imag:+.6e}i")
