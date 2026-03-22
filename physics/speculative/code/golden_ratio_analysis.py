#!/usr/bin/env python3
# Golden Ratio Analysis
# Extracted from relational ontology / physics exploration

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve

alpha = 1.0
S_c = 0.3
beta = 0.5

# First - is 0.622 related to golden ratio?
phi = (1 + np.sqrt(5)) / 2
print("=== GOLDEN RATIO CHECK ===")
print(f"phi = {phi:.6f}")
print(f"1/phi = {1/phi:.6f}")
print(f"phi - 1 = {phi-1:.6f}")
print(f"1/phi^2 = {1/phi**2:.6f}")
print(f"2 - phi = {2-phi:.6f}")
print(f"phi/e = {phi/np.e:.6f}")
print(f"Observed symmetric attractor = 0.6217")
print()

# Solve analytically for the symmetric fixed point
# At symmetric fixed point: S12 = S13 = S23 = S*
# dS/dt = 0
# -alpha * S*(S* - S_c)(S* - 1) - beta * S* * (2S* - 1) = 0
# S* [ -alpha(S* - S_c)(S* - 1) - beta(2S* - 1) ] = 0
# Non-trivial: -alpha(S* - S_c)(S* - 1) = beta(2S* - 1)

# Expand left: -alpha(S*^2 - (1+S_c)S* + S_c) = beta(2S* - 1)
# -alpha*S*^2 + alpha(1+S_c)S* - alpha*S_c = 2*beta*S* - beta
# -alpha*S*^2 + [alpha(1+S_c) - 2*beta]*S* + (beta - alpha*S_c) = 0
# alpha*S*^2 - [alpha(1+S_c) - 2*beta]*S* - (beta - alpha*S_c) = 0

a_coef = alpha
b_coef = -(alpha*(1+S_c) - 2*beta)
c_coef = -(beta - alpha*S_c)

discriminant = b_coef**2 - 4*a_coef*c_coef
S_star_1 = (-b_coef + np.sqrt(discriminant)) / (2*a_coef)
S_star_2 = (-b_coef - np.sqrt(discriminant)) / (2*a_coef)

print("=== ANALYTIC FIXED POINT ===")
print(f"Quadratic: {a_coef}*S^2 + {b_coef:.3f}*S + {c_coef:.3f} = 0")
print(f"S* solutions: {S_star_1:.6f} and {S_star_2:.6f}")
print(f"Observed: 0.621700")
print()

# So what IS the analytic form?
# S* = [alpha(1+S_c) - 2*beta + sqrt(D)] / (2*alpha)
# With alpha=1, S_c=0.3, beta=0.5:
# b_coef = -(1.3 - 1.0) = -0.3
# c_coef = -(0.5 - 0.3) = -0.2
# D = 0.09 + 0.8 = 0.89
# S* = (0.3 + sqrt(0.89)) / 2

print(f"Exact: S* = (0.3 + sqrt(0.89)) / 2 = {(0.3 + np.sqrt(0.89))/2:.6f}")
print(f"sqrt(0.89) = {np.sqrt(0.89):.6f}")
print()

# Now check if golden ratio appears when we tune parameters
# Golden ratio fixed point would require S* = 1/phi = 0.61803...
# (0.3 + sqrt(D)) / 2 = 0.61803
# sqrt(D) = 0.93606
# D = 0.87622
# b^2 - 4ac = 0.87622
# With b = alpha(1+S_c) - 2*beta, c = -(beta - alpha*S_c)
# Try to find S_c and beta that give golden ratio

print("=== PARAMETER SEARCH FOR GOLDEN RATIO FIXED POINT ===")
print("Looking for S_c, beta where symmetric attractor = 1/phi = 0.61803...")
print()

target = 1/phi
best_error = 1.0
best_params = None

for sc in np.linspace(0.1, 0.6, 100):
    for b in np.linspace(0.1, 2.0, 100):
        a_c = alpha
        b_c = -(alpha*(1+sc) - 2*b)
        c_c = -(b - alpha*sc)
        disc = b_c**2 - 4*a_c*c_c
        if disc >= 0:
            s_star = (-b_c + np.sqrt(disc)) / (2*a_c)
            if 0 < s_star < 1:
                error = abs(s_star - target)
                if error < best_error:
                    best_error = error
                    best_params = (sc, b, s_star)

print(f"Best match: S_c={best_params[0]:.3f}, beta={best_params[1]:.3f}")
print(f"S* = {best_params[2]:.6f} vs target {target:.6f}")
print(f"Error: {best_error:.6f}")
print()

# Check: is there a NATURAL parameterization that gives golden ratio?
# What if S_c = 1/phi^2 and beta = 1/phi?
sc_phi = 1/phi**2
beta_phi = 1/phi
a_c = 1.0
b_c = -(1*(1+sc_phi) - 2*beta_phi)
c_c = -(beta_phi - 1*sc_phi)
disc = b_c**2 - 4*a_c*c_c
if disc >= 0:
    s_star = (-b_c + np.sqrt(disc)) / (2*a_c)
    print(f"Natural phi parameterization:")
    print(f"S_c = 1/phi^2 = {sc_phi:.6f}, beta = 1/phi = {beta_phi:.6f}")
    print(f"S* = {s_star:.6f} vs 1/phi = {1/phi:.6f}")
    print()

# What about S_c = 1 - 1/phi, beta = 1/phi?
sc2 = 1 - 1/phi
beta2 = 1/phi
b_c2 = -(1*(1+sc2) - 2*beta2)
c_c2 = -(beta2 - 1*sc2)
disc2 = b_c2**2 - 4*1*c_c2
if disc2 >= 0:
    s_star2 = (-b_c2 + np.sqrt(disc2)) / (2*1)
    print(f"Alt phi parameterization:")
    print(f"S_c = 1-1/phi = {sc2:.6f}, beta = 1/phi = {beta2:.6f}")
    print(f"S* = {s_star2:.6f} vs 1/phi = {1/phi:.6f}")
