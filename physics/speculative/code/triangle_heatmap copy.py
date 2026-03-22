#!/usr/bin/env python3
"""
Triangle (ternary) heatmap showing attractor basins for three-node relational dynamics.
Initial conditions are scanned across the simplex S12 + S13 + S23 = 1,
colored by which attractor the system reaches.
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

alpha = 1.0
S_c = 0.3
beta = 0.5

def relational_dynamics(state, t, alpha, S_c, beta):
    S12, S13, S23 = state
    f12 = -alpha * S12 * (S12 - S_c) * (S12 - 1)
    f13 = -alpha * S13 * (S13 - S_c) * (S13 - 1)
    f23 = -alpha * S23 * (S23 - S_c) * (S23 - 1)
    competition_12 = beta * S12 * ((S12 + S13 - 1) + (S12 + S23 - 1)) / 2
    competition_13 = beta * S13 * ((S12 + S13 - 1) + (S13 + S23 - 1)) / 2
    competition_23 = beta * S23 * ((S12 + S23 - 1) + (S13 + S23 - 1)) / 2
    dS12 = f12 - competition_12
    dS13 = f13 - competition_13
    dS23 = f23 - competition_23
    return [dS12, dS13, dS23]

def classify_attractor(final_state):
    """0 = symmetric, 1 = paired, 2 = single dominant."""
    s = sorted(final_state, reverse=True)
    if s[0] - s[2] < 0.15:
        return 0  # all values similar
    elif s[0] - s[1] < 0.15:
        return 1  # top two similar, bottom suppressed
    else:
        return 2  # one clearly dominates

def ternary_to_cart(a, b, c):
    """Convert ternary coords to 2D Cartesian.
    a (S12) -> bottom-left corner (0, 0)
    b (S13) -> bottom-right corner (1, 0)
    c (S23) -> top corner (0.5, sqrt(3)/2)
    """
    x = b + c * 0.5
    y = c * np.sqrt(3) / 2
    return x, y

t = np.linspace(0, 40, 2000)
n = 300  # grid resolution (n+1 points per side, (n+1)(n+2)/2 total)
total_points = (n + 1) * (n + 2) // 2
print(f"Running {total_points} simulations on {n}-resolution ternary grid...")

xs, ys, zs = [], [], []

for i in range(n + 1):
    for j in range(n + 1 - i):
        k = n - i - j
        a, b, c = i / n, j / n, k / n  # S12, S13, S23 on simplex (sum=1)

        sol = odeint(relational_dynamics, [a, b, c], t, args=(alpha, S_c, beta))
        attractor = classify_attractor(sol[-1])

        x, y = ternary_to_cart(a, b, c)
        xs.append(x)
        ys.append(y)
        zs.append(attractor)

    if i % 10 == 0:
        done = sum(n + 1 - ii for ii in range(i + 1))
        print(f"  {done}/{total_points} points done")

xs = np.array(xs)
ys = np.array(ys)
zs = np.array(zs)

print("Rendering plot...")

fig, ax = plt.subplots(figsize=(9, 8))

# --- Filled heatmap via triangulation ---
triang = mtri.Triangulation(xs, ys)
cmap = ListedColormap(['#4a90d9', '#d9534f', '#5cb85c'])  # blue, red, green
ax.tripcolor(triang, zs, cmap=cmap, vmin=-0.5, vmax=2.5, alpha=0.9)

# --- Ternary gridlines at 0.25, 0.5, 0.75 ---
for val in [0.25, 0.5, 0.75]:
    # constant a lines (parallel to b-c edge)
    p1 = ternary_to_cart(val, 1 - val, 0)
    p2 = ternary_to_cart(val, 0, 1 - val)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'w-', alpha=0.35, linewidth=0.9, zorder=2)

    # constant b lines (parallel to a-c edge)
    p1 = ternary_to_cart(1 - val, val, 0)
    p2 = ternary_to_cart(0, val, 1 - val)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'w-', alpha=0.35, linewidth=0.9, zorder=2)

    # constant c lines (parallel to a-b edge)
    p1 = ternary_to_cart(1 - val, 0, val)
    p2 = ternary_to_cart(0, 1 - val, val)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'w-', alpha=0.35, linewidth=0.9, zorder=2)

# --- Triangle outline ---
h = np.sqrt(3) / 2
ax.plot([0, 1, 0.5, 0], [0, 0, h, 0], 'k-', linewidth=2, zorder=3)

# --- Corner labels ---
ax.text(0.00, -0.05, 'S₁₂ = 1\n(S₁₃ = S₂₃ = 0)', ha='center', va='top',
        fontsize=11, fontweight='bold')
ax.text(1.00, -0.05, 'S₁₃ = 1\n(S₁₂ = S₂₃ = 0)', ha='center', va='top',
        fontsize=11, fontweight='bold')
ax.text(0.50, h + 0.04, 'S₂₃ = 1\n(S₁₂ = S₁₃ = 0)', ha='center', va='bottom',
        fontsize=11, fontweight='bold')

# --- Edge midpoint labels ---
ax.text(0.50, -0.05, 'S₂₃ = 0', ha='center', va='top', fontsize=9, color='#555')
ax.text(0.77, h / 2 + 0.02, 'S₁₂ = 0', ha='left', va='center', fontsize=9,
        color='#555', rotation=-60)
ax.text(0.23, h / 2 + 0.02, 'S₁₃ = 0', ha='right', va='center', fontsize=9,
        color='#555', rotation=60)

# --- Mark center (equal split) ---
cx, cy = ternary_to_cart(1/3, 1/3, 1/3)
ax.plot(cx, cy, 'k+', markersize=12, markeredgewidth=2, zorder=4)
ax.text(cx, cy - 0.06, '(⅓, ⅓, ⅓)', ha='center', fontsize=8, color='k', zorder=4)

# --- Mark S_c boundary: each axis > S_c=0.3 region ---
# On the simplex sum=1, the region where all three > 0.3 forms a small inner triangle
sc = S_c  # 0.3
inner_verts = [
    ternary_to_cart(1 - 2*sc, sc, sc),
    ternary_to_cart(sc, 1 - 2*sc, sc),
    ternary_to_cart(sc, sc, 1 - 2*sc),
    ternary_to_cart(1 - 2*sc, sc, sc),
]
ax.plot([v[0] for v in inner_verts], [v[1] for v in inner_verts],
        'k--', linewidth=1.2, alpha=0.6, zorder=4, label=f'All S > S_c ({S_c})')
ax.text(cx, cy + 0.09, f'All > S_c', ha='center', fontsize=8, color='k',
        style='italic', zorder=4)

# --- Legend ---
legend_elements = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#4a90d9', markersize=14,
           label='Symmetric  (≈ 0.62, 0.62, 0.62)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#d9534f', markersize=14,
           label='Paired  (≈ 0.80, 0.80, 0.00)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#5cb85c', markersize=14,
           label='Single dominant  (≈ 0.94, 0.13, 0.13)'),
    Line2D([0], [0], color='k', linestyle='--', linewidth=1.5,
           label=f'S_c = {S_c} boundary'),
]
ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.20),
          ncol=2, fontsize=10, framealpha=0.95, title='Attractor type')

ax.set_xlim(-0.12, 1.12)
ax.set_ylim(-0.22, h + 0.12)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(
    f'Attractor Basin Boundaries — Ternary Diagram\n'
    f'α = {alpha},  S_c = {S_c},  β = {beta}  |  '
    f'Initial conditions on simplex  S₁₂ + S₁₃ + S₂₃ = 1',
    fontsize=12, pad=15
)

plt.tight_layout()
plt.savefig('triangle_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: triangle_heatmap.png")
