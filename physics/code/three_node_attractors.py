#!/usr/bin/env python3
# Three Node Attractors
# Extracted from relational ontology / physics exploration

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Three node relational system
# Nodes: 1, 2, 3
# Relations: S_12, S_13, S_23
# Each S in [0,1]
# 
# Basic equation for each relation:
# dS_ij/dt = -alpha * S_ij * (S_ij - S_c) * (S_ij - 1)
#
# But now add the constraint term - monogamy of entanglement
# If S_12 is high and S_13 is high, that costs S_23 (and vice versa)
# The constraint: each node has a total entanglement budget of 1
# So S_12 + S_13 <= 1 for node 1
#    S_12 + S_23 <= 1 for node 2  
#    S_13 + S_23 <= 1 for node 3
#
# Implement as a coupling term:
# dS_12/dt = intrinsic dynamics - beta * S_12 * (S_13 + S_23 - 1)  [competition from other relations at each node]

alpha = 1.0
S_c = 0.3  # critical threshold
beta = 0.5  # coupling strength between relations

def relational_dynamics(state, t, alpha, S_c, beta):
    S12, S13, S23 = state
    
    # Intrinsic cubic dynamics for each relation
    f12 = -alpha * S12 * (S12 - S_c) * (S12 - 1)
    f13 = -alpha * S13 * (S13 - S_c) * (S13 - 1)
    f23 = -alpha * S23 * (S23 - S_c) * (S23 - 1)
    
    # Monogamy constraint coupling
    # Node 1 couples S12 and S13
    # Node 2 couples S12 and S23
    # Node 3 couples S13 and S23
    
    competition_12 = beta * S12 * ((S12 + S13 - 1) + (S12 + S23 - 1)) / 2
    competition_13 = beta * S13 * ((S12 + S13 - 1) + (S13 + S23 - 1)) / 2
    competition_23 = beta * S23 * ((S12 + S23 - 1) + (S13 + S23 - 1)) / 2
    
    dS12 = f12 - competition_12
    dS13 = f13 - competition_13
    dS23 = f23 - competition_23
    
    return [dS12, dS13, dS23]

t = np.linspace(0, 20, 1000)

# Try many different initial conditions
np.random.seed(42)
n_trajectories = 50
initial_conditions = np.random.uniform(0.0, 1.0, (n_trajectories, 3))

# Also add some structured initial conditions
structured = [
    [0.8, 0.8, 0.8],  # all high
    [0.1, 0.1, 0.1],  # all low
    [0.8, 0.1, 0.1],  # one high
    [0.5, 0.5, 0.5],  # all at midpoint
    [0.31, 0.31, 0.31],  # just above critical
    [0.29, 0.29, 0.29],  # just below critical
    [0.8, 0.8, 0.1],  # two high one low
    [1.0, 1.0, 0.0],  # two maximal one zero
    [0.33, 0.33, 0.33],  # equal distribution at 1/3
]

all_initial = np.vstack([initial_conditions, structured])

results = []
final_states = []

for ic in all_initial:
    sol = odeint(relational_dynamics, ic, t, args=(alpha, S_c, beta))
    results.append(sol)
    final_states.append(sol[-1])

final_states = np.array(final_states)

print("=== FIXED POINT ANALYSIS ===")
print(f"Parameters: alpha={alpha}, S_c={S_c}, beta={beta}")
print()

# Cluster final states
from collections import Counter

def round_state(s, decimals=2):
    return tuple(np.round(sorted(s), decimals))

clusters = Counter([round_state(s) for s in final_states])
print("Attractor states (rounded, sorted):")
for state, count in sorted(clusters.items(), key=lambda x: -x[1]):
    total = sum(state)
    print(f"  {state} | count={count} | sum={total:.3f}")

print()
print("=== DETAILED FINAL STATES ===")
for i, (ic, fs) in enumerate(zip(all_initial, final_states)):
    print(f"IC: [{ic[0]:.2f}, {ic[1]:.2f}, {ic[2]:.2f}] -> Final: [{fs[0]:.3f}, {fs[1]:.3f}, {fs[2]:.3f}] sum={sum(fs):.3f}")
