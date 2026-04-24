"""
Small helper for the "ambient selector" question in core/ambient-reduction-scaffold.md.

Goal:
  Given a candidate D_amb in so(2,4), project to the stabilizer of a fixed spacelike
  normal n = e5, obtaining D_red in so(2,3), then test whether D_red selects the same
  compact U(1) generator as J^{01} (up to sign).

This is intentionally minimal: it uses the vector representation and commutator tests.

Notes:
  - If you do *not* want to pick a definite spatial axis inside Spin(2,3) (because it is
    conjugate under SO(3)), use `--axis any`. This tests whether D_red lies in some axis
    so(2,1) block up to SO(3) relabeling.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
from typing import Dict, List, Tuple


Matrix = List[List[int]]


def zeros(n: int) -> Matrix:
    return [[0 for _ in range(n)] for _ in range(n)]


def mat_copy(a: Matrix) -> Matrix:
    return [row[:] for row in a]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for j in range(n):
            out[i][j] = a[i][j] + b[i][j]
    return out


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for j in range(n):
            out[i][j] = a[i][j] - b[i][j]
    return out


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for k in range(n):
            aik = a[i][k]
            if aik == 0:
                continue
            for j in range(n):
                out[i][j] += aik * b[k][j]
    return out


def mat_comm(a: Matrix, b: Matrix) -> Matrix:
    return mat_sub(mat_mul(a, b), mat_mul(b, a))


def mat_is_zero(a: Matrix) -> bool:
    for row in a:
        for v in row:
            if v != 0:
                return False
    return True


def mat_l1_norm(a: Matrix) -> int:
    s = 0
    for row in a:
        for v in row:
            s += abs(v)
    return s


def mat_trace(a: Matrix) -> int:
    return sum(a[i][i] for i in range(len(a)))


def mat_det3(a: Matrix) -> int:
    if len(a) != 3 or len(a[0]) != 3:
        raise ValueError("mat_det3 expects 3x3")
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def mat_slice(a: Matrix, keep: List[int]) -> Matrix:
    """Extract a principal submatrix a[keep, keep]."""
    out = zeros(len(keep))
    for i, ii in enumerate(keep):
        for j, jj in enumerate(keep):
            out[i][j] = a[ii][jj]
    return out


def so_generator(eta_diag: List[int], a: int, b: int) -> Matrix:
    """
    Build the standard so(p,q) generator J^{ab} in the vector rep:
      (J^{ab})^c_d = delta^a_d eta^{bc} - delta^b_d eta^{ac}
    For diagonal eta, eta^{ii} == eta_{ii} == eta_diag[i] (up to sign conventions).
    """
    n = len(eta_diag)
    if a == b:
        raise ValueError("a and b must differ")
    g = zeros(n)
    for c in range(n):
        # column d=a contributes + eta^{bc} at row c
        g[c][a] += (1 if b == c else 0) * eta_diag[b]
        # column d=b contributes - eta^{ac} at row c
        g[c][b] -= (1 if a == c else 0) * eta_diag[a]
    return g


def project_to_stabilizer_fixed_index(x: Matrix, fixed_idx: int) -> Matrix:
    """
    Projection to the slice-preserving component that fixes e_fixed_idx:
    drop the parts that mix fixed_idx with the other directions.
    """
    n = len(x)
    out = mat_copy(x)
    for i in range(n):
        if i == fixed_idx:
            continue
        out[i][fixed_idx] = 0
        out[fixed_idx][i] = 0
    out[fixed_idx][fixed_idx] = 0
    return out


@dataclass(frozen=True)
class SelectorResult:
    commutes_with_so3: bool
    proportional_to_j01: bool
    j01_sign: int  # -1, 0, +1 (0 means inconclusive)
    red_is_zero: bool
    commutes_with_so2: bool
    in_axis_so21: bool


def classify_in_so23(d_red_5x5: Matrix, eta_diag_5: List[int]) -> SelectorResult:
    """
    In so(2,3), the maximal compact is so(2) + so(3).
    In the standard index split (0,1) timelike; (2,3,4) spacelike:
      so(3) = span{J^{23}, J^{34}, J^{42}}
      so(2) = span{J^{01}}

    We test whether d_red commutes with the so(3) generators; if so, it is forced
    to act only in the (0,1) plane, hence proportional to J^{01}.
    """
    j23 = so_generator(eta_diag_5, 2, 3)
    j34 = so_generator(eta_diag_5, 3, 4)
    j42 = so_generator(eta_diag_5, 4, 2)

    commutes_so3 = (
        mat_is_zero(mat_comm(d_red_5x5, j23))
        and mat_is_zero(mat_comm(d_red_5x5, j34))
        and mat_is_zero(mat_comm(d_red_5x5, j42))
    )

    j01 = so_generator(eta_diag_5, 0, 1)

    # If commutes, we can compare a single entry for proportionality/sign.
    # For our generator convention, J^{01} has a nonzero entry at (0,1) and (1,0).
    sign = 0
    prop = False
    if commutes_so3:
        a01 = d_red_5x5[0][1]
        b01 = j01[0][1]
        if b01 != 0 and a01 != 0 and a01 % b01 == 0:
            k = a01 // b01
            prop = mat_sub(d_red_5x5, [[k * v for v in row] for row in j01]) == zeros(5)
            if k > 0:
                sign = +1
            elif k < 0:
                sign = -1
        elif a01 == 0:
            # Could still be zero; treat as inconclusive
            sign = 0
            prop = False

    # "Local axis" variant:
    # Preserve only rotations in the plane orthogonal to a chosen spatial axis.
    # For axis=4, the stabilizer is generated by J^{23}.
    # For axis=2, stabilizer generator is J^{34}.
    # For axis=3, stabilizer generator is J^{42}.
    # Here we compute commutation with each of these and let main() choose.
    commutes_j23 = mat_is_zero(mat_comm(d_red_5x5, j23))
    commutes_j34 = mat_is_zero(mat_comm(d_red_5x5, j34))
    commutes_j42 = mat_is_zero(mat_comm(d_red_5x5, j42))

    return SelectorResult(
        commutes_with_so3=commutes_so3,
        proportional_to_j01=prop,
        j01_sign=sign,
        red_is_zero=mat_is_zero(d_red_5x5),
        # placeholders; filled/selected in main
        commutes_with_so2=False,
        in_axis_so21=False,
    )


def pretty_name(a: int, b: int) -> str:
    return f"J^{a}{b}"


def main() -> None:
    # Convention: so(2,4) on R^6 with eta = diag(-1,-1,+1,+1,+1,+1).
    # Indices 0,1 are timelike; indices 2,3,4,5 spacelike.
    eta6 = [-1, -1, +1, +1, +1, +1]
    fixed = 5  # n = e5 (spacelike normal)
    keep5 = [0, 1, 2, 3, 4]  # orthogonal complement n^perp
    eta5 = [eta6[i] for i in keep5]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--combo",
        default="",
        help="Linear combination like '01:1,04:2,14:-1' meaning sum c*J^ab in so(2,4).",
    )
    parser.add_argument(
        "--bruteforce",
        default="",
        help="Comma list of ab generators to brute force with coeffs in {-1,0,1}, e.g. '01,04,14,05,15,45'.",
    )
    parser.add_argument(
        "--axis",
        choices=["2", "3", "4", "any", "none"],
        default="none",
        help="Assume a local preferred spatial axis (2,3,4). Tests commutation with the SO(2) stabilizer of that axis.",
    )
    args = parser.parse_args()

    basis: Dict[str, Matrix] = {}
    for a in range(6):
        for b in range(a + 1, 6):
            basis[f"{a}{b}"] = so_generator(eta6, a, b)

    candidates: Dict[str, Matrix] = {}
    if args.combo.strip():
        damb = zeros(6)
        for term in args.combo.split(","):
            term = term.strip()
            if not term:
                continue
            if ":" not in term:
                raise SystemExit(f"Bad term '{term}'. Expected ab:coef, e.g. 01:1")
            ab, coef_s = term.split(":", 1)
            ab = ab.strip()
            coef = int(coef_s.strip())
            if ab not in basis:
                raise SystemExit(f"Unknown generator '{ab}'. Expected like 01, 04, 45, etc.")
            if coef == 0:
                continue
            part = [[coef * v for v in row] for row in basis[ab]]
            damb = mat_add(damb, part)
        candidates[f"combo({args.combo})"] = damb
    elif args.bruteforce.strip():
        gens = [g.strip() for g in args.bruteforce.split(",") if g.strip()]
        for g in gens:
            if g not in basis:
                raise SystemExit(f"Unknown generator '{g}' in --bruteforce")

        # Brute force all combinations with coeffs in {-1,0,1}.
        # Summarize by reduced classification bucket.
        buckets: Dict[str, List[str]] = {"zero": [], "+J01": [], "-J01": [], "other": []}

        def rec(i: int, current: Matrix, label_parts: List[str]) -> None:
            if i == len(gens):
                label = ",".join(label_parts) if label_parts else "0"
                dred6 = project_to_stabilizer_fixed_index(current, fixed)
                dred5 = mat_slice(dred6, keep5)
                cls = classify_in_so23(dred5, eta5)
                if cls.red_is_zero:
                    buckets["zero"].append(label)
                elif cls.proportional_to_j01 and cls.j01_sign == 1:
                    buckets["+J01"].append(label)
                elif cls.proportional_to_j01 and cls.j01_sign == -1:
                    buckets["-J01"].append(label)
                else:
                    buckets["other"].append(label)
                return

            ab = gens[i]
            for coef in (-1, 0, 1):
                if coef == 0:
                    rec(i + 1, current, label_parts)
                else:
                    part = [[coef * v for v in row] for row in basis[ab]]
                    rec(i + 1, mat_add(current, part), label_parts + [f"{ab}:{coef}"])

        rec(0, zeros(6), [])

        total = sum(len(v) for v in buckets.values())
        print("Ambient-selector brute force (vector rep)")
        print(f"eta6 = {eta6}, fixed index = {fixed}, keep = {keep5}")
        print(f"generators = {gens}, coeffs in {{-1,0,1}}, total combos = {total}")
        print("")
        for key in ("zero", "+J01", "-J01", "other"):
            ex = buckets[key][:8]
            more = "" if len(buckets[key]) <= 8 else f" (+{len(buckets[key]) - 8} more)"
            print(f"{key}: {len(buckets[key])} examples={ex}{more}")
        return
    else:
        # Sanity-check candidates. Extend these with your proposed selector.
        candidates = {
            pretty_name(0, 1): basis["01"],
            pretty_name(4, 5): basis["45"],
            pretty_name(0, 5): basis["05"],
            pretty_name(1, 5): basis["15"],
            pretty_name(0, 4): basis["04"],
            pretty_name(1, 4): basis["14"],
        }

    print("Ambient-selector check (vector rep)")
    print(f"eta6 = {eta6}, fixed index = {fixed}, keep = {keep5}")
    print("")

    for name, damb in candidates.items():
        dred6 = project_to_stabilizer_fixed_index(damb, fixed)
        dred5 = mat_slice(dred6, keep5)
        cls0 = classify_in_so23(dred5, eta5)
        red_norm = mat_l1_norm(dred5)

        def axis_checks(axis_s: str) -> Tuple[bool, bool]:
            # axis=4 => rotations in (2,3) plane: J^{23}
            # axis=2 => rotations in (3,4) plane: J^{34}
            # axis=3 => rotations in (4,2) plane: J^{42}
            if axis_s == "4":
                j_so2_local = so_generator(eta5, 2, 3)
                axis_idx_local = 4
            elif axis_s == "2":
                j_so2_local = so_generator(eta5, 3, 4)
                axis_idx_local = 2
            elif axis_s == "3":
                j_so2_local = so_generator(eta5, 4, 2)
                axis_idx_local = 3
            else:
                raise ValueError("axis_checks expects 2,3,4")

            commutes_so2_local = mat_is_zero(mat_comm(dred5, j_so2_local))

            # Axis so(2,1) subalgebra test: support only in indices {0,1,axis}.
            allowed = {0, 1, axis_idx_local}
            ok = True
            for i in range(5):
                for j in range(5):
                    if i in allowed and j in allowed:
                        continue
                    if dred5[i][j] != 0:
                        ok = False
                        break
                if not ok:
                    break
            return commutes_so2_local, ok

        def axis_invariants(axis_s: str) -> Tuple[int, int]:
            if axis_s == "4":
                idx = [0, 1, 4]
            elif axis_s == "2":
                idx = [0, 1, 2]
            elif axis_s == "3":
                idx = [0, 1, 3]
            else:
                raise ValueError("axis_invariants expects 2,3,4")
            m = mat_slice(dred5, idx)
            tr2 = mat_trace(mat_mul(m, m))
            det = mat_det3(m)
            return tr2, det

        def axis_type_from_invariants(tr2: int, det: int, is_zero: bool) -> str:
            """
            Coarse conjugacy-type label inside the axis block so(2,1)_{â}.

            For elements of so(2,1) (viewed as 3x3 matrices preserving diag(-1,-1,+1)),
            the sign of a quadratic invariant distinguishes the standard types:
              - elliptic  (compact-like)   : tr(M^2) < 0
              - hyperbolic (boost-like)    : tr(M^2) > 0
              - parabolic (null-like)      : tr(M^2) = 0, M != 0
            This is the exact analogue of the usual classification of Lorentz generators.

            det is reported for debugging; for a genuine so(2,1) element it is typically 0.
            """
            if is_zero:
                return "zero"
            if tr2 < 0:
                return "elliptic"
            if tr2 > 0:
                return "hyperbolic"
            # tr2 == 0 and nonzero
            return "parabolic"

        axis_summary = ""
        commutes_so2 = True
        in_so21 = True
        if args.axis == "any":
            hits = []
            for axis_s in ("2", "3", "4"):
                c2, s21 = axis_checks(axis_s)
                if c2 and s21:
                    hits.append(axis_s)
            invs = {}
            for axis_s in hits:
                tr2, det = axis_invariants(axis_s)
                invs[axis_s] = (tr2, det, axis_type_from_invariants(tr2, det, cls0.red_is_zero))
            axis_summary = f"  axis=any: hits={hits} inv(tr(M^2),det,type)={invs}"
            commutes_so2 = len(hits) > 0
            in_so21 = len(hits) > 0
        elif args.axis in ("2", "3", "4"):
            commutes_so2, in_so21 = axis_checks(args.axis)
            tr2, det = axis_invariants(args.axis)
            typ = axis_type_from_invariants(tr2, det, cls0.red_is_zero)
            axis_summary = (
                f"  axis={args.axis}: commutes_with_so2={commutes_so2}, in_axis_so21={in_so21}, "
                f"inv(tr(M^2),det,type)=({tr2},{det},{typ})"
            )
        else:
            axis_summary = ""
            commutes_so2 = False
            in_so21 = False

        cls = SelectorResult(
            commutes_with_so3=cls0.commutes_with_so3,
            proportional_to_j01=cls0.proportional_to_j01,
            j01_sign=cls0.j01_sign,
            red_is_zero=cls0.red_is_zero,
            commutes_with_so2=commutes_so2,
            in_axis_so21=in_so21,
        )

        print(
            f"{name}: red_L1={red_norm}, red_is_zero={cls.red_is_zero}, "
            f"commutes_with_so3={cls.commutes_with_so3}, "
            f"proportional_to_J01={cls.proportional_to_j01}, J01_sign={cls.j01_sign}"
        )

        if axis_summary:
            print(axis_summary)


if __name__ == "__main__":
    main()
