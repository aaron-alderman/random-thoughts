from fractions import Fraction


def fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    print("Minimal singlet candidate:")
    print("  H_cand = (T1 (+) T2) tensor S_aux tensor (3 (+) 1)")
    print("  with S_aux a weak SU(2) doublet")
    print()
    print("Weak decomposition:")
    print("  T1 tensor S_aux = 1_(-1/2) (+) 3_(-1/2)")
    print("  T2 tensor S_aux = 1_(+1/2) (+) 3_(+1/2)")
    print()

    # Solve the right-handed singlet fit
    # -a/2 + b/3 = -1/3
    # +a/2 + b/3 = +2/3
    a = Fraction(1, 1)
    b = Fraction(1, 2)

    def charge(j01: Fraction, q7: Fraction) -> Fraction:
        return a * j01 + b * q7

    values = {
        "Y((3,1)_(-1/2))": charge(Fraction(-1, 2), Fraction(1, 3)),
        "Y((3,1)_(+1/2))": charge(Fraction(1, 2), Fraction(1, 3)),
        "Y((1,1)_(-1/2))": charge(Fraction(-1, 2), Fraction(-1, 1)),
        "Y((1,1)_(+1/2))": charge(Fraction(1, 2), Fraction(-1, 1)),
    }

    print("Right-handed singlet fit:")
    print(f"  a = {fmt(a)}")
    print(f"  b = {fmt(b)}")
    for key, value in values.items():
        print(f"  {key} = {fmt(value)}")
    print()

    print("Earlier left-handed bare-seed fit:")
    print("  a = 0")
    print("  b = 1/2")
    print()

    print("Comparison:")
    print("  b is stable across both fits.")
    print("  a is not: left-handed bare seed wants 0, singlet candidate wants 1.")
    print("  So one global Y = a J^{01} + b Q7 does not yet fit both naive embeddings.")


if __name__ == "__main__":
    main()
