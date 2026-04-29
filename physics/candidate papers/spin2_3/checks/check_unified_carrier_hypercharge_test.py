from fractions import Fraction


def fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def solve_left(branch_sign: int) -> tuple[Fraction, Fraction]:
    # branch_sign = -1 for T1, +1 for T2
    # sign*a/2 + b/3 = 1/6
    # sign*a/2 - b   = -1/2
    b = Fraction(1, 2)
    a = Fraction(0, 1)
    return a, b


def solve_right(up_branch_sign: int) -> tuple[Fraction, Fraction]:
    # One branch carries d_R/e_R and the opposite branch carries u_R/nu_R.
    # If up_branch_sign = +1, then:
    #   +a/2 + b/3 = 2/3
    #   +a/2 - b   = 0
    # Otherwise signs flip.
    if up_branch_sign == 1:
        a = Fraction(1, 1)
    else:
        a = Fraction(-1, 1)
    b = Fraction(1, 2)
    return a, b


def main() -> None:
    print("Unified carrier:")
    print("  H_unif = (T1 (+) T2) tensor (1 (+) S_aux) tensor (3 (+) 1)")
    print("  with S_aux a weak SU(2) doublet, neutral under J^{01} and Q7")
    print()

    print("Left-handed fit from a pure J-branch doublet sector:")
    for sign, label in [(-1, "T1 branch"), (1, "T2 branch")]:
        a, b = solve_left(sign)
        print(f"  {label}: a = {fmt(a)}, b = {fmt(b)}")
    print()

    print("Right-handed singlet fit:")
    for sign, label in [(1, "T2 as up/nu branch"), (-1, "T1 as up/nu branch")]:
        a, b = solve_right(sign)
        print(f"  {label}: a = {fmt(a)}, b = {fmt(b)}")
    print()

    print("Conclusion:")
    print("  Left-handed fit always wants a = 0, b = 1/2.")
    print("  Right-handed fit always wants |a| = 1, b = 1/2.")
    print("  So neutral-S_aux unified carrier gives no single global Y = a J^{01} + b Q7.")


if __name__ == "__main__":
    main()
