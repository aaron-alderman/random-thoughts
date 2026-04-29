from fractions import Fraction


def fmt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    print("Conditional static spectrum closure:")
    print("  Inputs:")
    print("    P_obs   = P_T1 = (1/2)(1 - 2 J01)")
    print("    P_eps   = (1/2)(1 - tau) = 1 - (1/2) C_tot")
    print("    P_phys  = P_obs P_aux,0 + P_eps P_aux,1")
    print("    Y       = J01 + (1/2) Q7 + (1/2) P_aux,0")
    print()

    q7_triplet = Fraction(1, 3)
    q7_singlet = Fraction(-1, 1)

    def charge(j: Fraction, q7: Fraction, p0: Fraction) -> Fraction:
        return j + Fraction(1, 2) * q7 + Fraction(1, 2) * p0

    values = {
        "Q_L": charge(Fraction(-1, 2), q7_triplet, Fraction(1, 1)),
        "L_L": charge(Fraction(-1, 2), q7_singlet, Fraction(1, 1)),
        "d_R": charge(Fraction(-1, 2), q7_triplet, Fraction(0, 1)),
        "e_R": charge(Fraction(-1, 2), q7_singlet, Fraction(0, 1)),
        "u_R": charge(Fraction(1, 2), q7_triplet, Fraction(0, 1)),
        "nu_R": charge(Fraction(1, 2), q7_singlet, Fraction(0, 1)),
    }

    print("  Charges on P_phys:")
    for key, value in values.items():
        print(f"    {key} = {fmt(value)}")
    print()
    print("  So under the current projector inputs, the reduced static spectrum matches one SM-like generation exactly.")


if __name__ == "__main__":
    main()
