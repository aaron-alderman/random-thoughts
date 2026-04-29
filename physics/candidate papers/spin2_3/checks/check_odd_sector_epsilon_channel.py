def main() -> None:
    print("Odd-sector epsilon channel:")
    print("  On 2 tensor 2:")
    print("    symmetric part     -> 3")
    print("    antisymmetric part -> 1")
    print()
    print("  Swap operator tau has eigenvalues:")
    print("    tau = +1 on the triplet")
    print("    tau = -1 on the singlet")
    print()
    print("  So the antisymmetric singlet projector is")
    print("    P_eps = (1/2)(1 - tau)")
    print()
    print("  With total weak Casimir normalized by")
    print("    C_tot = 0 on the singlet")
    print("    C_tot = 2 on the triplet")
    print("  one has")
    print("    C_tot = 1 + tau")
    print("  and therefore")
    print("    P_eps = 1 - (1/2) C_tot")


if __name__ == "__main__":
    main()
