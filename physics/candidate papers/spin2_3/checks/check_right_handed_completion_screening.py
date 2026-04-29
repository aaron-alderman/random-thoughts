from fractions import Fraction


def fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    y_q = Fraction(1, 6)
    y_l = Fraction(-1, 2)

    print("Fixed left-handed seed:")
    print(f"  y_Q = {fmt(y_q)}")
    print(f"  y_L = {fmt(y_l)}")
    print()

    y_u_plus_y_d = 2 * y_q
    y_e_plus_y_nu = Fraction(-1, 1)
    p_minus_q = Fraction(-2, 9)

    print("Anomaly target relations for the right-handed completion:")
    print(f"  y_u + y_d = {fmt(y_u_plus_y_d)}")
    print(f"  y_e + y_nu = {fmt(y_e_plus_y_nu)}")
    print(f"  y_u*y_d - y_e*y_nu = {fmt(p_minus_q)}")
    print()

    y_nu = Fraction(0, 1)
    y_e = y_e_plus_y_nu - y_nu
    y_u_times_y_d = p_minus_q + y_e * y_nu
    disc = y_u_plus_y_d * y_u_plus_y_d - 4 * y_u_times_y_d
    y_u_root_1 = (y_u_plus_y_d + 1) / 2
    y_u_root_2 = (y_u_plus_y_d - 1) / 2

    print("Special case y_nu = 0:")
    print(f"  y_e = {fmt(y_e)}")
    print(f"  y_u*y_d = {fmt(y_u_times_y_d)}")
    print(f"  discriminant = {fmt(disc)}")
    print(
        "  {y_u, y_d} = "
        f"{{{fmt(y_u_root_1)}, {fmt(y_u_root_2)}}}"
    )
    print()

    print("Trial enlargement:")
    print("  H_trial = (T1 (+) T2) tensor (3 (+) 1)")
    print("  Product-level SU(3) x K content:")
    print("    (3,2)_(-1/2) (+) (1,2)_(-1/2) (+) (3,2)_(+1/2) (+) (1,2)_(+1/2)")
    print("  Every state is still a weak doublet under the current K reading.")
    print()

    # Match the left-handed T1 charges:
    #   -a/2 + b/3 = 1/6
    #   -a/2 - b   = -1/2
    b = Fraction(1, 2)
    a = Fraction(0, 1)

    def charge(j01: Fraction, q7: Fraction) -> Fraction:
        return a * j01 + b * q7

    charges = {
        "Y(T1,3)": charge(Fraction(-1, 2), Fraction(1, 3)),
        "Y(T1,1)": charge(Fraction(-1, 2), Fraction(-1, 1)),
        "Y(T2,3)": charge(Fraction(1, 2), Fraction(1, 3)),
        "Y(T2,1)": charge(Fraction(1, 2), Fraction(-1, 1)),
    }

    print("Hypercharge fit on the doubled trial space after fixing the T1 seed:")
    print(f"  a = {fmt(a)}")
    print(f"  b = {fmt(b)}")
    for key, value in charges.items():
        print(f"  {key} = {fmt(value)}")
    print()

    print("Conclusion:")
    print("  T2 duplication alone does not create right-handed weak singlets.")
    print("  Once the T1 seed is fixed, it also does not make J^{01} visible in Y.")


if __name__ == "__main__":
    main()
