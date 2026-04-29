from fractions import Fraction


def fmt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    q7_triplet = Fraction(1, 3)
    q7_singlet = Fraction(-1, 1)

    print("Minimal physical subcarrier candidate:")
    print("  P_phys = P_T1 P_aux,0 + P_odd,0 P_aux,1")
    print("  where P_T1 = (1/2)(1 - 2 J01)")
    print("  and   P_odd,0 = 1 - (1/2) C_tot on 2 tensor 2 = 1 (+) 3")
    print()

    def charge(j: Fraction, q7: Fraction, p0: Fraction) -> Fraction:
        return j + Fraction(1, 2) * q7 + Fraction(1, 2) * p0

    kept = {
        "Q_L": charge(Fraction(-1, 2), q7_triplet, Fraction(1, 1)),
        "L_L": charge(Fraction(-1, 2), q7_singlet, Fraction(1, 1)),
        "d_R": charge(Fraction(-1, 2), q7_triplet, Fraction(0, 1)),
        "u_R": charge(Fraction(1, 2), q7_triplet, Fraction(0, 1)),
        "e_R": charge(Fraction(-1, 2), q7_singlet, Fraction(0, 1)),
        "nu_R": charge(Fraction(1, 2), q7_singlet, Fraction(0, 1)),
    }

    print("  Kept sectors:")
    for key, value in kept.items():
        print(f"    {key} = {fmt(value)}")
    print()

    exotic_even = {
        "T2 even x 3": charge(Fraction(1, 2), q7_triplet, Fraction(1, 1)),
        "T2 even x 1": charge(Fraction(1, 2), q7_singlet, Fraction(1, 1)),
    }

    print("  Removed by P_T1 on the even line:")
    for key, value in exotic_even.items():
        print(f"    {key} = {fmt(value)}")
    print()
    print("  Removed by P_odd,0 on the odd line:")
    print("    all weak-triplet channels inside 2 tensor 2")


if __name__ == "__main__":
    main()
