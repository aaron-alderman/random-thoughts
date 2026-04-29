def main() -> None:
    print("Quaternionic auxiliary-block screening:")
    print("  Current parent slice: H(u,v) as a complex carrier over C_u with visible SU(2) from left multiplication.")
    print("  Use scaled generators")
    print("    Lu = diag(1,-1)")
    print("    Lv = [[0,1],[-1,0]]")
    print()

    print("  Let X = [[a,b],[c,d]].")
    print("  [X,Lu] = 0 forces b = c = 0, so X is diagonal.")
    print("  [X,Lv] = 0 then forces a = d.")
    print("  Therefore every SU(2)-equivariant endomorphism is scalar:")
    print("    X = lambda I_2")
    print()

    print("  Consequence:")
    print("    H(u,v) is the irreducible complex doublet 2 under the natural left action.")
    print("    So it contains no nontrivial equivariant projector and does not realize 1 (+) 2.")
    print()

    print("  Distinct real decomposition under quaternionic conjugation / adjoint action:")
    print(f"    dim_R(H)      = {4}")
    print(f"    dim_R(R*1)    = {1}")
    print(f"    dim_R(Im(H))  = {3}")
    print("    so H = 1 (+) 3 as a real adjoint-type package, not as the visible complex doublet carrier.")


if __name__ == "__main__":
    main()
