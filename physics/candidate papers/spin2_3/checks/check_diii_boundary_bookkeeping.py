from __future__ import annotations

from fractions import Fraction


def fmt(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def parity_shift(sum_value: Fraction) -> Fraction:
    return Fraction(1, 2) * sum_value


def print_scenario(name: str, sum_t_su2: Fraction, sum_t_su3: Fraction, sum_q2: Fraction, n_doublets: int) -> None:
    print(f"Scenario: {name}")
    print(f"  SU(2) doublets: {n_doublets} ({'even' if n_doublets % 2 == 0 else 'odd'})")
    print(f"  sum T_SU(2): {fmt(sum_t_su2)}")
    print(f"  Delta k_SU(2): {fmt(parity_shift(sum_t_su2))}")
    print(f"  sum T_SU(3): {fmt(sum_t_su3)}")
    print(f"  Delta k_SU(3): {fmt(parity_shift(sum_t_su3))}")
    print(f"  sum q^2: {fmt(sum_q2)}")
    print(f"  Delta k_U(1): {fmt(parity_shift(sum_q2))}")
    print()


def print_copy_scaling(name: str, copies: int, base_w3: int) -> None:
    print(f"Copy-scaling scenario: {name}")
    print(f"  spectator copies: {copies}")
    print(f"  base W3: {base_w3}")
    print(f"  total W3 if copies are uncoupled spectators: {copies * base_w3}")
    print()


def main() -> None:
    t2_fund = Fraction(1, 2)
    t3_fund = Fraction(1, 2)

    # Left-handed T1 seed only: Q_L + L_L.
    sum_t_su2_left = 3 * t2_fund + t2_fund
    sum_t_su3_left = 2 * t3_fund
    sum_q2_left_sm = 6 * Fraction(1, 6) ** 2 + 2 * Fraction(-1, 2) ** 2
    print_scenario(
        "left-handed T1 seed (Q_L + L_L), SM-like target charges",
        sum_t_su2_left,
        sum_t_su3_left,
        sum_q2_left_sm,
        n_doublets=4,
    )

    # Full one-generation SM-like completion, included only as an illustrative target.
    sum_t_su2_full = sum_t_su2_left
    sum_t_su3_full = 2 * t3_fund + t3_fund + t3_fund
    sum_q2_full_sm = (
        6 * Fraction(1, 6) ** 2
        + 3 * Fraction(2, 3) ** 2
        + 3 * Fraction(-1, 3) ** 2
        + 2 * Fraction(-1, 2) ** 2
        + Fraction(-1, 1) ** 2
    )
    print_scenario(
        "full one-generation SM-like completion without nu_R",
        sum_t_su2_full,
        sum_t_su3_full,
        sum_q2_full_sm,
        n_doublets=4,
    )

    print_copy_scaling("minimal reduced block only", copies=1, base_w3=1)
    print_copy_scaling("one generation of color/lepton spectator slots", copies=4, base_w3=1)
    print_copy_scaling("three such generations as uncoupled spectators", copies=12, base_w3=1)

    print("Scenario status:")
    print("  - Scenario A: established reading for the current W3 result.")
    print("  - Scenario D: leading bridge hypothesis consistent with the current corpus.")
    print("  - Scenarios B/C: require an enlarged boundary Hamiltonian and a new W3/inflow calculation.")
    print()

    print("Notes:")
    print("  - Delta k values are the raw 2+1d parity-anomaly half-index sums.")
    print("  - The SM-like charges are an illustrative target, not a derived Spin(2,3) result.")
    print("  - The SU(2) even-doublet check is the cleanest common shadow with the 4d global constraint.")
    print("  - The current W3 calculation in the corpus is on the minimal reduced Spin(2,3) block;")
    print("    these boundary sums become directly comparable only after a localization rule for")
    print("    color/generation/right-handed sectors is chosen.")
    print("  - If extra sectors enter as uncoupled spectator copies, the protected-mode count")
    print("    and additive parity data scale with the copy number.")


if __name__ == "__main__":
    main()
