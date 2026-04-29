from fractions import Fraction


def fmt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    q7_triplet = Fraction(1, 3)
    q7_singlet = Fraction(-1, 1)
    p0 = Fraction(1, 1)

    print("Even-line exotic branch obstruction:")
    print("  Y = J01 + (1/2) Q7 + (1/2) P_aux,0 with P_aux,0 = 1 on the even line.")
    print()

    def charge(j: Fraction, q7: Fraction) -> Fraction:
        return j + Fraction(1, 2) * q7 + Fraction(1, 2) * p0

    t1_triplet = charge(Fraction(-1, 2), q7_triplet)
    t1_singlet = charge(Fraction(-1, 2), q7_singlet)
    t2_triplet = charge(Fraction(1, 2), q7_triplet)
    t2_singlet = charge(Fraction(1, 2), q7_singlet)

    print(f"  T1 even x 3 : Y = {fmt(t1_triplet)}")
    print(f"  T1 even x 1 : Y = {fmt(t1_singlet)}")
    print(f"  T2 even x 3 : Y = {fmt(t2_triplet)}")
    print(f"  T2 even x 1 : Y = {fmt(t2_singlet)}")
    print()
    print("  So the same even auxiliary line carries:")
    print("    desired left-handed doublets on T1")
    print("    exotic extra doublets on T2 with charges 7/6 and 1/2")


if __name__ == "__main__":
    main()
