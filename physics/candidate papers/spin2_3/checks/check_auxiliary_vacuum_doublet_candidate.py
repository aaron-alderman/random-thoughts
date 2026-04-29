def main() -> None:
    print("Auxiliary vacuum-plus-doublet candidate:")
    print("  Start with one quaternionic complex doublet mode V ~= 2.")
    print("  Fermionic completion gives")
    print("    Lambda^0 V ~= 1")
    print("    Lambda^1 V ~= 2")
    print("    Lambda^2 V ~= det(2) ~= 1")
    print("  So full auxiliary Fock space is")
    print("    Lambda^bullet V ~= 1 (+) 2 (+) 1")
    print()

    print("  Desired auxiliary block appears as the low-occupancy sector")
    print("    Lambda^{<=1} V = Lambda^0 V (+) Lambda^1 V ~= 1 (+) 2")
    print()

    print("  Number operator N has eigenvalues 0, 1, 2 on Lambda^0, Lambda^1, Lambda^2.")
    print("  Vacuum projector:")
    print("    on Lambda^{<=1}:  P_vac = 1 - N")
    print("    on full Lambda^bullet: P_vac = 1 - (3/2) N + (1/2) N^2")
    print()

    for n in (0, 1, 2):
        p = 1 - 1.5 * n + 0.5 * (n ** 2)
        print(f"  P_vac(N={n}) = {p:g}")


if __name__ == "__main__":
    main()
