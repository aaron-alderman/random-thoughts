#!/usr/bin/env python3
# Sierpinski
# Extracted from relational ontology / physics exploration

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from itertools import combinations

alpha = 1.0
S_c = 0.3
beta = 0.5

def build_network_dynamics(n_nodes, edges):
    """
    Build dynamics for arbitrary network topology.
    edges: list of (i,j) pairs, 0-indexed
    Returns dynamics function
    """
    n_edges = len(edges)
    edge_index = {e: i for i, e in enumerate(edges)}
    edge_index.update({(j,i): idx for (i,j), idx in edge_index.items()})
    
    # For each node, which edge indices connect to it?
    node_edges = {n: [] for n in range(n_nodes)}
    for idx, (i,j) in enumerate(edges):
        node_edges[i].append(idx)
        node_edges[j].append(idx)
    
    def dynamics(state, t, alpha, S_c, beta):
        ds = np.zeros(n_edges)
        
        # Node loads
        loads = np.zeros(n_nodes)
        for n in range(n_nodes):
            loads[n] = sum(state[idx] for idx in node_edges[n])
        
        for idx, (i,j) in enumerate(edges):
            s = state[idx]
            # Cubic intrinsic
            f = -alpha * s * (s - S_c) * (s - 1)
            # Competition from both endpoint nodes
            comp = beta * s * ((loads[i] - 1) + (loads[j] - 1)) / 2
            ds[idx] = f - comp
        
        return ds
    
    return dynamics, node_edges, n_edges

def run_network(n_nodes, edges, ic, t):
    dyn, node_edges, n_edges = build_network_dynamics(n_nodes, edges)
    sol = odeint(dyn, ic, t, args=(alpha, S_c, beta))
    return sol

t = np.linspace(0, 80, 4000)

# ============================================================
# BUILD SIERPINSKI TRIANGLE LEVELS
# ============================================================

print("=== SIERPINSKI TRIANGLE NETWORKS ===")
print()

# Level 0: Single triangle (3 nodes, 3 edges)
# Level 1: 3 triangles sharing corners (6 nodes, 9 edges) 
# Level 2: 9 triangles (15 nodes, 27 edges... actually less due to sharing)

# Let's build them carefully

# LEVEL 0: Triangle
# Nodes: 0,1,2
# Edges: (0,1),(0,2),(1,2)
l0_nodes = 3
l0_edges = [(0,1),(0,2),(1,2)]

# LEVEL 1: Sierpinski - 3 triangles joined at corners
# Take triangle and subdivide: add midpoints
# Nodes: 0(top), 1(bot-left), 2(bot-right), 3(mid-top-left), 4(mid-top-right), 5(mid-bottom)
# Actually let's think of it as 3 triangles:
# Triangle A: 0,1,2 (original scaled down, top)
# Triangle B: 3,4,5 but sharing corners
# Sierpinski level 1 has 6 nodes, 9 edges

# Standard Sierpinski level 1:
# Top triangle: nodes 0,1,2
# Bottom-left triangle: nodes 3,4,5 where 3 shares with 0, etc.
# Let me use coordinates to be precise

def sierpinski_coords(level):
    """Generate node positions for Sierpinski triangle at given level"""
    if level == 0:
        return np.array([[0.5, 1.0], [0.0, 0.0], [1.0, 0.0]])
    
    # Iterative: take previous and create 3 scaled copies
    prev = sierpinski_coords(level - 1)
    scale = 0.5
    
    top = prev * scale + np.array([0.25, 0.5])
    bot_left = prev * scale
    bot_right = prev * scale + np.array([0.5, 0.0])
    
    return np.vstack([top, bot_left, bot_right])

def sierpinski_network(level):
    """Build Sierpinski triangle network at given level"""
    if level == 0:
        nodes = [(0.5, 1.0), (0.0, 0.0), (1.0, 0.0)]
        edges = [(0,1),(0,2),(1,2)]
        return nodes, edges
    
    # Build by recursive construction
    # Level 1: 6 unique nodes (corners of 3 triangles, with shared corners)
    
    if level == 1:
        # Top triangle: 0,1,2
        # Bottom-left: 3=1(shared), 4, 5=2_shared
        # Actually Sierpinski shares the TOUCHING corners
        # 
        # Layout:    0
        #           / \
        #          1---2
        #         / \ / \
        #        3---4---5
        # But Sierpinski REMOVES the middle:
        #    0
        #   / \
        #  1---2
        # /     \
        # 3---  ---5
        # Wait, let me be precise about Sierpinski level 1
        # 
        # 6 nodes: top(0), mid-left(1), mid-right(2), bot-left(3), bot-mid(4), bot-right(5)
        # Three triangles: (0,1,2), (1,3,4), (2,4,5)
        # Shared nodes: 1 between top and bot-left, 2 between top and bot-right, 4 between bot-left and bot-right
        
        nodes = [
            (0.5, 1.0),   # 0: apex
            (0.25, 0.5),  # 1: mid-left  
            (0.75, 0.5),  # 2: mid-right
            (0.0, 0.0),   # 3: bot-left
            (0.5, 0.0),   # 4: bot-mid
            (1.0, 0.0),   # 5: bot-right
        ]
        # Triangle 1: (0,1,2) - top
        # Triangle 2: (1,3,4) - bottom left
        # Triangle 3: (2,4,5) - bottom right
        edges = [(0,1),(0,2),(1,2),  # top triangle
                 (1,3),(1,4),(3,4),  # bottom-left triangle
                 (2,4),(2,5),(4,5)]  # bottom-right triangle
        return nodes, edges
    
    if level == 2:
        # 15 nodes, each of the 3 sub-triangles is itself a level-1 Sierpinski
        # This gets complex - let me build it systematically
        # 
        # Level 2 has 9 triangles, 15 nodes
        # 
        # Node layout (row by row, left to right):
        # Row 0: 0
        # Row 1: 1, 2
        # Row 2: 3, 4, 5
        # Row 3: 6, 7, 8, 9
        # Row 4: 10, 11, 12, 13, 14
        
        nodes = []
        for row in range(5):
            for col in range(row + 1):
                x = 0.5 - row * 0.25 + col * 0.5
                y = 1.0 - row * 0.25
                nodes.append((x, y))
        
        # Sierpinski level 2: which edges exist?
        # All upward-pointing triangles at this resolution
        # Upward triangles: (row,col) -> (row,col), (row+1,col), (row+1,col+1)
        # But Sierpinski removes downward triangles at each level
        
        # Node numbering: node at (row, col) = sum(range(row+1)) + col = row*(row+1)/2 + col
        def node_idx(row, col):
            return row*(row+1)//2 + col
        
        edges = set()
        # Level 2 Sierpinski: upward triangles at scale 1 (finest)
        # but only those NOT in the removed central triangles
        
        # The removed triangles at level 2 are the central triangles of each level-1 sub-triangle
        # Let me just enumerate valid upward triangles
        
        # All upward triangles in a 4-row grid:
        upward_triangles = []
        for row in range(4):
            for col in range(row + 1):
                upward_triangles.append((row, col))
        
        # Sierpinski removes the "central" downward triangles
        # At level 2, removed downward triangles are at:
        # (row=1, between (1,0) and (1,1)) -> center between rows 1-2
        # (row=3, between (3,0)-(3,1)), (3,1)-(3,2)), (3,2)-(3,3)) -> but only some
        
        # Easier: define Sierpinski by which upward triangles to INCLUDE
        # Level 2: 9 upward triangles
        # Think of it as 3x3 grid of sub-triangles
        # Sub-triangle (i,j) at scale 2 contains nodes at rows 2i to 2i+2
        
        # Valid upward unit triangles (at finest scale):
        # Top sub-triangle (rows 0-2): upward triangles at (0,0), (1,0), (1,1)
        # Bottom-left sub-triangle (rows 2-4): (2,0),(3,0),(3,1) 
        # Bottom-right sub-triangle (rows 2-4): (2,2),(3,2),(3,3)
        # Wait, this isn't quite right for Sierpinski level 2
        
        # Let me just hardcode level 2 Sierpinski edges
        # 9 triangles, 3 per sub-triangle
        
        # Top sub (Sierpinski level 1 scaled to top):
        # nodes: 0,1,2,3,4,5 (rows 0-2 but only outer)
        # Actually let me use a different approach
        
        # Sierpinski level 2 = take level 1 and replace each triangle with level 1
        # Level 1 nodes: 0,1,2,3,4,5 (6 nodes)
        # Each triangle in level 1 becomes a level-0 Sierpinski (single triangle)
        # with its 3 corners
        
        # I'll build it as explicit triangles
        # Using the row/col layout above (15 nodes total)
        
        def ni(r,c): return r*(r+1)//2 + c
        
        # All upward-pointing unit triangles in full grid:
        all_up = [(r,c) for r in range(4) for c in range(r+1)]
        
        # Sierpinski level 2 removes the "central" unit triangles
        # At level 2, central triangles of each quadrant are removed:
        # Quadrant top (rows 0-2): central is downward at row 1
        # The downward triangle between (1,0),(1,1),(2,1) is removed
        # But we only add upward triangle edges, so:
        
        # Valid upward triangles for Sierpinski level 2:
        # (these are all upward triangles EXCEPT those inside removed regions)
        # Removed upward triangles: those that would fill the central holes
        # Central hole of top quadrant: upward triangle at (2,1) - row2, col1
        # Central hole of bottom-left: upward at (4,1)  
        # Central hole of bottom-right: upward at (4,3)
        # Plus the big central hole: upward triangles at rows 2-4 middle
        
        # Actually for level 2 Sierpinski the removed upward triangles are:
        # The "central" triangle of the whole figure (rows 2, cols 1): node (2,1)
        # And within each sub-triangle, its central removal
        
        # Let me just list the 9 valid triangles explicitly:
        valid_triangles = [
            # Top sub-triangle (level 1 in top):
            (ni(0,0), ni(1,0), ni(1,1)),  # apex triangle
            (ni(1,0), ni(2,0), ni(2,1)),   # bot-left of top sub
            (ni(1,1), ni(2,1), ni(2,2)),   # bot-right of top sub
            # Bottom-left sub-triangle:
            (ni(2,0), ni(3,0), ni(3,1)),   # apex of bot-left sub
            (ni(3,0), ni(4,0), ni(4,1)),   # bot-left of bot-left sub
            (ni(3,1), ni(4,1), ni(4,2)),   # bot-right of bot-left sub
            # Bottom-right sub-triangle:
            (ni(2,2), ni(3,2), ni(3,3)),   # apex of bot-right sub
            (ni(3,2), ni(4,2), ni(4,3)),   # bot-left of bot-right sub
            (ni(3,3), ni(4,3), ni(4,4)),   # bot-right of bot-right sub
        ]
        
        edges = set()
        for (a,b,c) in valid_triangles:
            edges.add((min(a,b), max(a,b)))
            edges.add((min(a,c), max(a,c)))
            edges.add((min(b,c), max(b,c)))
        
        return nodes, list(edges), valid_triangles

# Run all three levels
print("Building Sierpinski networks...")

# Level 0
l0_nodes, l0_edges = sierpinski_network(0)
print(f"Level 0: {len(l0_nodes)} nodes, {len(l0_edges)} edges")

# Level 1  
l1_nodes, l1_edges = sierpinski_network(1)
print(f"Level 1: {len(l1_nodes)} nodes, {len(l1_edges)} edges")

# Level 2
result = sierpinski_network(2)
l2_nodes, l2_edges = result[0], result[1]
print(f"Level 2: {len(l2_nodes)} nodes, {len(l2_edges)} edges")
print()

# Run dynamics on each
def run_network_general(n_nodes, edges, ic=None, symmetric=True):
    n_edges = len(edges)
    if ic is None:
        if symmetric:
            ic = [0.5] * n_edges
        else:
            ic = np.random.uniform(0.1, 0.9, n_edges)
    
    dyn, node_edges, _ = build_network_dynamics(n_nodes, edges)
    sol = odeint(dyn, ic, t, args=(alpha, S_c, beta))
    return sol, node_edges

print("=== SYMMETRIC IC RESULTS ===")
for level, (n_nodes, edges, name) in enumerate([
    (len(l0_nodes), l0_edges, "Level 0 (triangle)"),
    (len(l1_nodes), l1_edges, "Level 1 (3 triangles)"),
    (len(l2_nodes), l2_edges, "Level 2 (9 triangles)"),
]):
    sol, node_edges = run_network_general(n_nodes, edges, symmetric=True)
    final = sol[-1]
    active = sum(1 for s in final if s > 0.1)
    unique_vals = np.unique(np.round(final, 3))
    print(f"{name}:")
    print(f"  Final active: {active}/{len(edges)}")
    print(f"  Unique values: {unique_vals}")
    print(f"  Mean: {np.mean(final):.4f}, Std: {np.std(final):.4f}")
    print(f"  Total relational coherence: {sum(final):.4f}")
    print()
