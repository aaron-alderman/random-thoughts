import sympy as sp
from sympy import N, pi, cosh, sinh, sqrt, nsolve

s = sp.symbols('s', real=True, positive=True)

# Exact transcendental equation for s0 (three identical bosons, unitarity limit)
trans_eq = -s * cosh(pi * s / 2) + (8 / sqrt(3)) * sinh(pi * s / 6)

print("Transcendental equation:")
sp.pprint(trans_eq)

# Numerical solution near the known root (guess ≈1.0)
s0_solved = nsolve(trans_eq, s, 1.0)
print(f"\nSolved s0 ≈ {N(s0_solved, 8)}")

# Casimir effective strength from SO(2,1) in radial QM
# lambda_eff = 1/2 + i s   →  Re[lambda(lambda-1)] = - (s**2 + 1/4)
eff_strength = - (s0_solved**2 + sp.Rational(1,4))
print(f"Effective λ_sym from Casimir = {N(eff_strength, 8)}")

# Scaling ratio check
scaling_ratio = sp.exp(-2 * pi / s0_solved)
print(f"Energy ratio E_{{n+1}}/E_n ≈ {N(scaling_ratio, 6)}")
print(f"Size ratio ρ_{{n+1}}/ρ_n ≈ {N(1/scaling_ratio, 6)}")  # ≈22.7