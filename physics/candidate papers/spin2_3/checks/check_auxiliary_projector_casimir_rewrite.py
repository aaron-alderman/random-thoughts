from fractions import Fraction


def fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    c_singlet = Fraction(0, 1)
    c_doublet = Fraction(3, 4)

    def p0(casimir: Fraction) -> Fraction:
        return Fraction(1, 1) - Fraction(4, 3) * casimir

    print("Auxiliary Casimir rewrite:")
    print("  C_aux eigenvalue on j=0 singlet = 0")
    print("  C_aux eigenvalue on j=1/2 doublet = 3/4")
    print()
    print(f"  P_aux,0(j=0)   = {fmt(p0(c_singlet))}")
    print(f"  P_aux,0(j=1/2) = {fmt(p0(c_doublet))}")
    print()
    print("Conclusion:")
    print("  P_aux,0 = 1 - (4/3) C_aux is exactly the projector onto the trivial summand of 1 (+) 2.")


if __name__ == "__main__":
    main()
