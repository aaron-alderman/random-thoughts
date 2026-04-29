from fractions import Fraction


def fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    a = Fraction(1, 1)
    b = Fraction(1, 2)
    c = Fraction(1, 2)

    print("Unified carrier projector fix:")
    print("  H_unif = (T1 (+) T2) tensor (1 (+) S_aux) tensor (3 (+) 1)")
    print("  Y = a J^{01} + b Q7 + c P_aux,0")
    print()
    print(f"  a = {fmt(a)}")
    print(f"  b = {fmt(b)}")
    print(f"  c = {fmt(c)}")
    print()

    def charge(j: Fraction, q7: Fraction, p0: Fraction) -> Fraction:
        return a * j + b * q7 + c * p0

    values = {
        "Q_L": charge(Fraction(-1, 2), Fraction(1, 3), Fraction(1, 1)),
        "L_L": charge(Fraction(-1, 2), Fraction(-1, 1), Fraction(1, 1)),
        "d_R": charge(Fraction(-1, 2), Fraction(1, 3), Fraction(0, 1)),
        "u_R": charge(Fraction(1, 2), Fraction(1, 3), Fraction(0, 1)),
        "e_R": charge(Fraction(-1, 2), Fraction(-1, 1), Fraction(0, 1)),
        "nu_R": charge(Fraction(1, 2), Fraction(-1, 1), Fraction(0, 1)),
    }

    for key, value in values.items():
        print(f"  {key} = {fmt(value)}")
    print()

    print("Conclusion:")
    print("  The projector term shifts only the left-handed doublet sector.")
    print("  This removes the a=0 versus |a|=1 conflict from the neutral unified carrier.")
    print("  It is a selected-slot fit only; complementary even-line sectors are screened separately.")


if __name__ == "__main__":
    main()
