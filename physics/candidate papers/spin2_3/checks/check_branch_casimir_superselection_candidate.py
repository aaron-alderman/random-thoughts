def main() -> None:
    print("Branch-Casimir superselection candidate:")
    print("  Even line selector:")
    print("    P_obs = P_T1 = (1/2)(1 - 2 J01)")
    print("  Odd line selector:")
    print("    P_jmin = P_odd,0 = 1 - (1/2) C_tot on 2 tensor 2 = 1 (+) 3")
    print()
    print("  Proposed physical-state projector:")
    print("    P_phys = P_obs P_aux,0 + P_jmin P_aux,1")
    print()
    print("  Orientation partner under global reversal:")
    print("    P_phys' = (1 - P_obs) P_aux,0 + P_jmin P_aux,1")
    print()
    print("  Interpretation:")
    print("    even line  -> observable branch selected by orientation/readout")
    print("    odd sector -> minimal total weak-spin channel")


if __name__ == "__main__":
    main()
