from fractions import Fraction


def fmt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    q7_triplet = Fraction(1, 3)
    q7_singlet = Fraction(-1, 1)

    print("Full Fock auxiliary obstruction:")
    print("  H_full = (T1 (+) T2) tensor (Lambda^0 V (+) Lambda^1 V (+) Lambda^2 V) tensor (3 (+) 1)")
    print("  Y = J01 + (1/2) Q7 + (1/2) P_vac")
    print("  On Lambda^2 V, P_vac = 0, so Y = J01 + (1/2) Q7.")
    print()

    t1_triplet = Fraction(-1, 2) + Fraction(1, 2) * q7_triplet
    t1_singlet = Fraction(-1, 2) + Fraction(1, 2) * q7_singlet
    t2_triplet = Fraction(1, 2) + Fraction(1, 2) * q7_triplet
    t2_singlet = Fraction(1, 2) + Fraction(1, 2) * q7_singlet

    print("  Top-wedge weak-doublet hypercharges:")
    print(f"    T1 x Lambda^2 x 3 : Y = {fmt(t1_triplet)}")
    print(f"    T1 x Lambda^2 x 1 : Y = {fmt(t1_singlet)}")
    print(f"    T2 x Lambda^2 x 3 : Y = {fmt(t2_triplet)}")
    print(f"    T2 x Lambda^2 x 1 : Y = {fmt(t2_singlet)}")
    print()
    print("  So the full Fock completion adds extra weak doublets with right-handed-style hypercharge values.")


if __name__ == "__main__":
    main()
