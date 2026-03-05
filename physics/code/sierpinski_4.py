#!/usr/bin/env python3
# Sierpinski 4
# Extracted from relational ontology / physics exploration

import numpy as np
import matplotlib.pyplot as plt

# Rule 90 is a cellular automaton
# Each cell's next state = XOR of its two neighbors
# Binary: 0 or 1
# Rule 90 produces Sierpinski triangle from a single cell

# The connection to check:
# Rule 90 over GF(2) (binary field)
# Our system: continuous dynamics over [0,1]
# 
# Rule 90 generates Sierpinski because XOR = addition mod 2
# Which is the same as Pascal's triangle mod 2
# Which IS Sierpinski
#
# Question: is our dynamics secretly implementing Rule 90?
# Or something analogous in continuous space?

print("=== RULE 90 CONNECTION ===")
print()
print("Rule 90: next_state[i] = state[i-1] XOR state[i+1]")
print("       = (state[i-1] + state[i+1]) mod 2")
print()
print("This generates Sierpinski from a single 'on' cell")
print("because Pascal's triangle mod 2 = Sierpinski")
print()

# Generate Rule 90 Sierpinski
def rule90(n_cells, n_steps):
    grid = np.zeros((n_steps, n_cells), dtype=int)
    grid[0, n_cells//2] = 1  # single cell
    for t in range(1, n_steps):
        for i in range(n_cells):
            left = grid[t-1, (i-1) % n_cells]
            right = grid[t-1, (i+1) % n_cells]
            grid[t, i] = (left + right) % 2
    return grid

grid_r90 = rule90(63, 32)

print("Rule 90 output (first 8 steps, center 15 cells):")
for row in grid_r90[:8, 24:39]:
    print('  ' + ''.join('█' if x else '.' for x in row))

print()
print("=== THE DEEP CONNECTION ===")
print()
print("Rule 90 over GF(2): next[i] = left XOR right")
print("Our dynamics over R: the COHERENT edges form a pattern")
print("  where junction edges (connecting shared nodes) collapse")
print("  and internal edges survive")
print()
print("The structural parallel:")
print()

# What IS the update rule our dynamics implements at the edge level?
# At level n of Sierpinski construction:
# Edge survives if it's in EXACTLY ONE triangle (internal)
# Edge dies if it connects two junction nodes (inter-triangle)
#
# A junction node is one shared by multiple triangles
# The edge between two junction nodes connects two overloaded nodes
# -> gets squeezed to zero
#
# This is equivalent to:
# edge_survives = (node_i_degree == 2) OR (node_j_degree == 2)
# i.e., at least one endpoint is a "corner" node (degree 2 in triangle network)

print("Edge survival rule in our dynamics:")
print("  edge(i,j) survives iff at least one of i,j is a 'corner' node")
print("  'corner' = connects to exactly 2 edges (one triangle only)")
print("  'junction' = connects to 4+ edges (multiple triangles)")
print()
print("Rule 90 survival rule:")
print("  cell survives iff exactly one neighbor is 'on'")
print("  cell[t+1] = left XOR right = left + right mod 2")
print()
print("Both are XOR-like: survive if boundary, die if interior")
print("Both produce Sierpinski for the same topological reason")
print()

# Now the deeper question:
# Is Rule 90 the CONTINUOUS LIMIT of our dynamics?
# 
# Rule 90 in continuous form:
# ds/dt = s(i-1) + s(i+1) - 2*s(i)  <- diffusion (heat equation)
# 
# But that gives smooth solutions, not Sierpinski
# 
# The key is NONLINEARITY
# Our cubic has a threshold - below S_c, falls to zero
# This threshold is what converts continuous dynamics into binary-like behavior
# The edge either survives (above threshold) or dies (below threshold)
# 
# With threshold, continuous Rule-90-like dynamics DOES produce Sierpinski

print("=== CONTINUOUS RULE 90 ===")
print()
print("Standard Rule 90 continuous analog:")
print("  ds_i/dt = s_{i-1} + s_{i+1} - 2*s_i  (diffusion)")
print("  -> smooth, no Sierpinski")
print()
print("With threshold nonlinearity (like our cubic):")
print("  ds_i/dt = [s_{i-1} + s_{i+1} - 2*s_i] * Θ(s_i - S_c)")
print("  -> binary-like output, Sierpinski emerges")
print()
print("Our dynamics implements this through:")
print("  1. Intrinsic cubic: drives to 0 or 1 (binary attractor)")
print("  2. Monogamy competition: implements the 'neighbor sum' constraint")
print("  3. Together: continuous Rule 90 with threshold")
print()

# Check: is there a direct correspondence?
# Rule 90: cell i gets contribution from neighbors i-1 and i+1
# Our system: edge (i,j) gets competition from all OTHER edges at nodes i and j
# 
# For a linear chain of triangles (degenerate case):
# Triangle 1: nodes 0,1,2 with shared node 1
# Triangle 2: nodes 1,2,3 with shared node 2  
# etc.
# This IS a 1D cellular structure where the "cells" are triangles
# and the "neighbors" are the triangles sharing a node

print("=== 1D CHAIN OF TRIANGLES ===")
print("Building a linear chain and checking for Rule 90 behavior")
print()

# Chain of 5 triangles sharing nodes
# Nodes: 0-1-2-3-4-5-6-7-8-9-10 (11 nodes)
# Triangle i uses nodes: i, i+1, i+2... no
# Actually: triangle i = (2i, 2i+1, 2i+2) sharing nodes 2i+1, 2i+2 with neighbors

# Simpler: linear chain
# T0: 0,1,2
# T1: 2,3,4  (shares node 2 with T0)
# T2: 4,5,6  (shares node 4 with T1)
# T3: 6,7,8
# T4: 8,9,10

chain_edges = []
for k in range(5):
    base = 2*k
    i,j,l = base, base+1, base+2
    chain_edges.extend([(min(i,j),max(i,j)),(min(i,l),max(i,l)),(min(j,l),max(j,l))])
chain_edges = list(set(chain_edges))
n_chain = 11

from scipy.integrate import odeint

def build_network_dynamics(n_nodes, edges):
    n_edges = len(edges)
    node_edges = {n: [] for n in range(n_nodes)}
    for idx, (i,j) in enumerate(edges):
        node_edges[i].append(idx)
        node_edges[j].append(idx)
    def dynamics(state, t, alpha, S_c, beta):
        ds = np.zeros(n_edges)
        loads = np.zeros(n_nodes)
        for n in range(n_nodes):
            loads[n] = sum(state[idx] for idx in node_edges[n])
        for idx, (i,j) in enumerate(edges):
            s = state[idx]
            f = -alpha * s * (s - S_c) * (s - 1)
            comp = beta * s * ((loads[i] - 1) + (loads[j] - 1)) / 2
            ds[idx] = f - comp
        return ds
    return dynamics, node_edges, n_edges

alpha, S_c, beta = 1.0, 0.3, 0.5
t = np.linspace(0, 100, 5000)

dyn_chain, ne_chain, _ = build_network_dynamics(n_chain, chain_edges)
ic_chain = [0.5]*len(chain_edges)
sol_chain = odeint(dyn_chain, ic_chain, t, args=(alpha, S_c, beta))

print("Chain of 5 triangles, symmetric IC:")
final_chain = sol_chain[-1]
print(f"Edges: {chain_edges}")
print(f"Values: {[f'{v:.3f}' for v in final_chain]}")
print()

# Which are junction edges (connecting shared nodes)?
# Shared nodes in chain: 2,4,6,8 (each connects 2 triangles)
shared_chain = {2,4,6,8}
for idx, (i,j) in enumerate(chain_edges):
    is_junction = i in shared_chain and j in shared_chain
    print(f"  {(i,j)}: {final_chain[idx]:.4f} {'JUNCTION' if is_junction else 'internal'}")

print()

# Now run with different initial "patterns" to test Rule 90 analog
# In Rule 90: which triangles start "on" determines evolution
# Let's seed specific triangles and see if Rule 90 XOR logic applies

print("=== SEEDING SPECIFIC TRIANGLES ===")
print("Testing if triangle activation follows Rule 90 XOR logic")
print()

def triangle_edges_in_chain(k):
    """Return edge indices for triangle k in chain"""
    base = 2*k
    i,j,l = base, base+1, base+2
    needed = [(min(i,j),max(i,j)),(min(i,l),max(i,l)),(min(j,l),max(j,l))]
    return [chain_edges.index(e) for e in needed if e in chain_edges]

def seed_triangles(active_triangles, n_triangles=5, high=0.8, low=0.1):
    ic = [low]*len(chain_edges)
    for k in active_triangles:
        for idx in triangle_edges_in_chain(k):
            ic[idx] = high
    return ic

def get_active_triangles(final, threshold=0.3):
    active = []
    for k in range(5):
        idxs = triangle_edges_in_chain(k)
        avg = np.mean([final[i] for i in idxs])
        active.append(avg > threshold)
    return active

# Test Rule 90 predictions
# Rule 90: if T0 on, T1 off, T2 on...
# After one step: T1 = T0 XOR T2 = 1, etc.

test_patterns = [
    ([0], "Only T0"),
    ([2], "Only T2 (middle)"),
    ([0,2], "T0 and T2"),
    ([0,4], "T0 and T4 (ends)"),
    ([1,3], "T1 and T3"),
    ([0,1,2,3,4], "All on"),
]

for seed, label in test_patterns:
    ic = seed_triangles(seed)
    sol = odeint(dyn_chain, ic, t, args=(alpha, S_c, beta))
    final = sol[-1]
    active = get_active_triangles(final)
    active_str = ''.join('█' if a else '.' for a in active)
    seed_str = ''.join('█' if k in seed else '.' for k in range(5))
    print(f"  Seed: {seed_str}  ->  Final: {active_str}  ({label})")

print()
print("Rule 90 XOR prediction (T_i_new = T_{i-1} XOR T_{i+1}):")
for seed, label in test_patterns:
    seed_binary = [1 if k in seed else 0 for k in range(5)]
    next_gen = [(seed_binary[(i-1)%5] + seed_binary[(i+1)%5]) % 2 for i in range(5)]
    seed_str = ''.join('█' if x else '.' for x in seed_binary)
    next_str = ''.join('█' if x else '.' for x in next_gen)
    print(f"  Rule90: {seed_str}  ->  Predict: {next_str}  ({label})")
