def main() -> None:
    print("Even-sector observable-projector descent:")
    print("  Ambient scaffold compatibility:")
    print("    R_op(P_Pi,-) = P_obs")
    print("    R_op(P_Pi,+) = 1 - P_obs")
    print()
    print("  In the current reduced orientation convention:")
    print("    P_obs = P_T1 = (1/2)(1 - 2 J01)")
    print()
    print("  So the even half of the static subcarrier")
    print("    P_obs P_aux,0")
    print("  is the reduced observable/readout-sector projector,")
    print("  not a new hypercharge-specific branch rule.")


if __name__ == "__main__":
    main()
