#!/usr/bin/env python3
# Four Node Dynamics
# Extracted from relational ontology / physics exploration

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from itertools import combinations

alpha = 1.0
S_c = 0.3
beta = 0.5

# FOUR NODE SYSTEM
# Nodes: 1,2,3,4
# Relations: S12, S13, S14, S23, S24, S34 - six pairwise relations
# Monogamy: each node has budget constraint
# Node 1: S12 + S13 + S14 <= 1
# Node 2: S12 + S23 + S24 <= 1
# Node 3: S13 + S23 + S34 <= 1
# Node 4: S14 + S24 + S34 <= 1

def four_node_dynamics(state, t, alpha, S_c, beta):
    S12, S13, S14, S23, S24, S34 = state
    
    # Intrinsic cubic for each
    def cubic(s):
        return -alpha * s * (s - S_c) * (s - 1)
    
    # Competition at each node
    # Node 1 owns: S12, S13, S14
    # Node 2 owns: S12, S23, S24  
    # Node 3 owns: S13, S23, S34
    # Node 4 owns: S14, S24, S34
    
    node1_load = S12 + S13 + S14
    node2_load = S12 + S23 + S24
    node3_load = S13 + S23 + S34
    node4_load = S14 + S24 + S34
    
    # Competition for S12: felt by node1 and node2
    comp12 = beta * S12 * ((node1_load - 1) + (node2_load - 1)) / 2
    comp13 = beta * S13 * ((node1_load - 1) + (node3_load - 1)) / 2
    comp14 = beta * S14 * ((node1_load - 1) + (node4_load - 1)) / 2
    comp23 = beta * S23 * ((node2_load - 1) + (node3_load - 1)) / 2
    comp24 = beta * S24 * ((node2_load - 1) + (node4_load - 1)) / 2
    comp34 = beta * S34 * ((node3_load - 1) + (node4_load - 1)) / 2
    
    dS12 = cubic(S12) - comp12
    dS13 = cubic(S13) - comp13
    dS14 = cubic(S14) - comp14
    dS23 = cubic(S23) - comp23
    dS24 = cubic(S24) - comp24
    dS34 = cubic(S34) - comp34
    
    return [dS12, dS13, dS14, dS23, dS24, dS34]

t = np.linspace(0, 50, 3000)

print("=== FOUR NODE SYSTEM ===")
print("6 pairwise relations, monogamy budget per node = 1")
print()

# Key structured initial conditions
test_cases = {
    "All symmetric": [0.5]*6,
    "All low": [0.1]*6,
    "All high": [0.9]*6,
    "Two pairs (12,34 high; 13,14,23,24 low)": [0.8, 0.1, 0.1, 0.1, 0.1, 0.8],
    "Triangle + isolated (123 high, node4 disconnected)": [0.8, 0.8, 0.1, 0.8, 0.1, 0.1],
    "One dominant relation": [0.9, 0.1, 0.1, 0.1, 0.1, 0.1],
    "Square (12,23,34,14 high; diagonals 13,24 low)": [0.8, 0.1, 0.8, 0.8, 0.8, 0.1],
    "Complete bipartite (14,24 high; rest low)": [0.1, 0.1, 0.8, 0.1, 0.8, 0.1],
    "Star from node1 (12,13,14 high)": [0.8, 0.8, 0.8, 0.1, 0.1, 0.1],
    "Random 1": [0.6, 0.3, 0.7, 0.2, 0.8, 0.4],
    "Random 2": [0.4, 0.7, 0.2, 0.6, 0.3, 0.8],
}

results_4 = {}
for name, ic in test_cases.items():
    sol = odeint(four_node_dynamics, ic, t, args=(alpha, S_c, beta))
    final = sol[-1]
    results_4[name] = final
    
    # Characterize
    active = sum(1 for s in final if s > 0.1)
    total = sum(final)
    max_s = max(final)
    min_s = min(final)
    spread = max_s - min_s
    
    print(f"{name}:")
    print(f"  Final: [{', '.join(f'{s:.3f}' for s in final)}]")
    print(f"  Active relations: {active}/6, Total: {total:.3f}, Spread: {spread:.3f}")
    print()

# Random scan to find all attractors
print("=== ATTRACTOR CENSUS (100 random ICs) ===")
np.random.seed(42)
random_ics = np.random.uniform(0, 1, (100, 6))
final_states = []
for ic in random_ics:
    sol = odeint(four_node_dynamics, ic, t, args=(alpha, S_c, beta))
    final_states.append(sol[-1])

# Classify by number of active relations and total
from collections import Counter

def classify(state, threshold=0.1):
    active = sum(1 for s in state if s > threshold)
    total = round(sum(state), 1)
    sym = np.std(state)
    if sym < 0.05:
        return f"SYMMETRIC({active}active,sum={total})"
    elif active <= 2:
        return f"SPARSE({active}active,sum={total})"
    elif active >= 5:
        return f"DENSE({active}active,sum={total})"
    else:
        return f"MIXED({active}active,sum={total})"

classifications = Counter([classify(s) for s in final_states])
print("Attractor classes:")
for cls, count in sorted(classifications.items(), key=lambda x: -x[1]):
    print(f"  {cls}: {count}/100")

print()

# Find the symmetric fixed point analytically for 4 nodes
# Each node has 3 relations, budget = 1
# At symmetric fixed point all S = S*
# Each node load = 3*S*
# Competition term = beta * S* * (3*S* - 1)   [each relation shared by 2 nodes, both with same load]
# cubic + competition = 0:
# -alpha*S*(S-S_c)(S-1) - beta*S*(3S-1) = 0
# S[-alpha(S-S_c)(S-1) - beta(3S-1)] = 0
# Non-trivial:
# -alpha(S^2 - (1+S_c)S + S_c) - beta(3S-1) = 0
# -alpha*S^2 + alpha(1+S_c)S - alpha*S_c - 3*beta*S + beta = 0
# alpha*S^2 + (3*beta - alpha(1+S_c))S + (alpha*S_c - beta) = 0

a_c = alpha
b_c = 3*beta - alpha*(1+S_c)
c_c = alpha*S_c - beta

disc = b_c**2 - 4*a_c*c_c
S_star = (-b_c + np.sqrt(disc)) / (2*a_c) if disc >= 0 else None
S_star2 = (-b_c - np.sqrt(disc)) / (2*a_c) if disc >= 0 else None

print(f"=== ANALYTIC 4-NODE SYMMETRIC FIXED POINT ===")
print(f"Equation: {a_c}*S^2 + {b_c:.3f}*S + {c_c:.3f} = 0")
print(f"Solutions: {S_star:.6f} and {S_star2:.6f}")
print()

phi = (1 + np.sqrt(5)) / 2
print(f"Comparison:")
print(f"  3-node S* = 0.621699")
print(f"  4-node S* = {S_star:.6f}")
print(f"  1/phi     = {1/phi:.6f}")
print(f"  1/phi^2   = {1/phi**2:.6f}")
print(f"  3-node S* * 3 = {0.621699*3:.6f} (total relational load per node)")
print(f"  4-node S* * 3 = {S_star*3:.6f} (total relational load per node)")
print()

# General n-node formula
print("=== N-NODE SYMMETRIC FIXED POINT ===")
print("Each node connects to (n-1) others, so load = (n-1)*S*")
print("Competition = beta*S*((n-1)*S* - 1)")
print()
for n in range(2, 9):
    k = n - 1  # connections per node
    # -alpha(S-S_c)(S-1) - beta(k*S - 1) = 0 ... but wait
    # Each relation is SHARED between 2 nodes
    # competition_ij = beta * S_ij * ((load_i - 1) + (load_j - 1)) / 2
    # At symmetric: = beta * S* * (k*S* - 1)
    a_c = alpha
    b_c = k*beta - alpha*(1+S_c)
    c_c = alpha*S_c - beta  # Note: beta term is -beta * (-1) = +beta... wait
    # Let me redo:
    # -alpha(S^2 - (1+S_c)S + S_c) - beta(k*S - 1) = 0
    # -alpha*S^2 + alpha(1+S_c)*S - alpha*S_c - k*beta*S + beta = 0
    # alpha*S^2 + (k*beta - alpha(1+S_c))*S + (alpha*S_c - beta) = 0
    a_c = alpha
    b_c = k*beta - alpha*(1+S_c)
    c_c = alpha*S_c - beta
    disc = b_c**2 - 4*a_c*c_c
    if disc >= 0:
        s = (-b_c + np.sqrt(disc))/(2*a_c)
        s2 = (-b_c - np.sqrt(disc))/(2*a_c)
        load = k * s
        print(f"  n={n} (k={k} connections): S* = {s:.6f}, per-node load = {load:.6f}")
    else:
        print(f"  n={n}: No real fixed point (disc={disc:.4f})")
