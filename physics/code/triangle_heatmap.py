#!/usr/bin/env python3
"""
Triangle (ternary) heatmap showing attractor basins for three-node relational dynamics.
Fits three circles (enforcing exact 3-fold symmetry) to the basin boundaries.
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

alpha = 2.0
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
        return 0
    elif s[0] - s[1] < 0.15:
        return 1
    else:
        return 2

def ternary_to_cart(a, b, c):
    """a=S12 -> bottom-left, b=S13 -> bottom-right, c=S23 -> top."""
    x = b + c * 0.5
    y = c * np.sqrt(3) / 2
    return x, y

def fit_circle_algebraic(points):
    """Algebraic least-squares circle fit. Returns (cx, cy, r)."""
    pts = np.array(points)
    x, y = pts[:, 0], pts[:, 1]
    A = np.column_stack([x, y, np.ones(len(x))])
    b = -(x**2 + y**2)
    result = np.linalg.lstsq(A, b, rcond=None)
    D, E, F = result[0]
    cx = -D / 2
    cy = -E / 2
    r = np.sqrt(max(cx**2 + cy**2 - F, 0))
    return cx, cy, r

def symmetry_enforced_fit(boundary_pts, centroid):
    """
    Fit three circles enforcing exact 3-fold symmetry:
    - All three circles have the same radius
    - Centers are exact 120-degree rotations of each other around the centroid
    Strategy: map all boundary points into the first 120-degree sector,
    fit one circle, then rotate to get the other two.
    """
    cx0, cy0 = centroid
    pts = np.array(boundary_pts)

    # Polar coords relative to centroid
    angles   = np.arctan2(pts[:, 1] - cy0, pts[:, 0] - cx0)
    distances = np.hypot(pts[:, 0] - cx0, pts[:, 1] - cy0)

    # Map all angles into the first sector [0, 2pi/3)
    sector = 2 * np.pi / 3
    angles_mapped = angles % (2 * np.pi)   # [0, 2pi)
    angles_mapped = angles_mapped % sector  # [0, 2pi/3)

    x_mapped = cx0 + distances * np.cos(angles_mapped)
    y_mapped = cy0 + distances * np.sin(angles_mapped)

    # Fit one circle to all mapped points
    cx1, cy1, r = fit_circle_algebraic(list(zip(x_mapped, y_mapped)))

    # Generate the other two by rotating 120 and 240 degrees around centroid
    circles = []
    dx, dy = cx1 - cx0, cy1 - cy0
    for k in range(3):
        theta = k * sector
        rx = dx * np.cos(theta) - dy * np.sin(theta)
        ry = dx * np.sin(theta) + dy * np.cos(theta)
        circles.append((cx0 + rx, cy0 + ry, r))

    return circles

def point_in_triangle(x, y):
    """Check if (x,y) is inside the ternary triangle."""
    h = np.sqrt(3) / 2
    c = y / h
    b = x - c / 2
    a = 1 - b - c
    return a >= -1e-9 and b >= -1e-9 and c >= -1e-9

# ── Run simulations ──────────────────────────────────────────────────────────
t_span = np.linspace(0, 40, 2000)
n = 150
total_points = (n + 1) * (n + 2) // 2
print(f"Running {total_points} simulations (n={n})...")

grid_lookup = {}
xs, ys, zs = [], [], []

for i in range(n + 1):
    for j in range(n + 1 - i):
        k = n - i - j
        a, b, c = i / n, j / n, k / n
        sol = odeint(relational_dynamics, [a, b, c], t_span, args=(alpha, S_c, beta))
        att = classify_attractor(sol[-1])
        x, y = ternary_to_cart(a, b, c)
        grid_lookup[(i, j)] = att
        xs.append(x)
        ys.append(y)
        zs.append(att)

    if i % 10 == 0:
        done = sum(n + 1 - ii for ii in range(i + 1))
        print(f"  {done}/{total_points}")

xs = np.array(xs)
ys = np.array(ys)
zs = np.array(zs)

# ── Find boundary points between symmetric (0) and non-symmetric ─────────────
sym_bdy = []

for i in range(n + 1):
    for j in range(n + 1 - i):
        k = n - i - j
        t1 = grid_lookup[(i, j)]
        x1, y1 = ternary_to_cart(i/n, j/n, k/n)

        for di, dj in [(1, 0), (0, 1), (1, -1)]:
            ni, nj = i + di, j + dj
            nk = n - ni - nj
            if nk < 0 or (ni, nj) not in grid_lookup:
                continue
            t2 = grid_lookup[(ni, nj)]
            if t1 == t2:
                continue
            if 0 not in (t1, t2):
                continue  # only care about sym boundary

            x2, y2 = ternary_to_cart(ni/n, nj/n, nk/n)
            sym_bdy.append(((x1 + x2) / 2, (y1 + y2) / 2))

# ── Fit circles with enforced 3-fold symmetry ─────────────────────────────────
h = np.sqrt(3) / 2
centroid = (0.5, h / 3)
dist_centroid_to_corner = np.hypot(0.5, h / 3)          # ≈ 0.577
dist_centroid_to_edge   = h / 3 * np.sqrt(3) / np.sqrt(3)  # = h/3 * 1...
# Simpler: for equilateral triangle with side 1:
#   inradius  (centroid to edge midpoint) = 1 / (2*sqrt(3)) ≈ 0.289
#   circumradius (centroid to corner)     = 1 / sqrt(3)     ≈ 0.577
inradius      = 1 / (2 * np.sqrt(3))
circumradius  = 1 / np.sqrt(3)

print(f"\nTriangle geometry:")
print(f"  Inradius  (centroid -> edge midpoint): {inradius:.3f}")
print(f"  Circumradius (centroid -> corner):     {circumradius:.3f}")

print("\nFitting circles (3-fold symmetry enforced)...")
#circles = symmetry_enforced_fit(sym_bdy, centroid)

#r = circles[0][2]
#print(f"  Radius: {r:.4f}")
#for i, (cx, cy, _) in enumerate(circles):
#    d_from_centroid = np.hypot(cx - centroid[0], cy - centroid[1])
#    inside = point_in_triangle(cx, cy)
#    angle_deg = np.degrees(np.arctan2(cy - centroid[1], cx - centroid[0]))
#    print(f"  Circle {i+1}: center=({cx:.4f}, {cy:.4f}), "
#          f"dist_from_centroid={d_from_centroid:.4f}, "
#          f"angle={angle_deg:.1f}°, "
#          f"{'INSIDE' if inside else 'OUTSIDE'} triangle")

# ── Plot ──────────────────────────────────────────────────────────────────────
print("\nRendering plot...")
fig, ax = plt.subplots(figsize=(9, 8))

triang = mtri.Triangulation(xs, ys)
cmap = ListedColormap(['#4a90d9', '#d9534f', '#5cb85c'])
ax.tripcolor(triang, zs, cmap=cmap, vmin=-0.5, vmax=2.5, alpha=0.88)

# Ternary gridlines
for val in [0.25, 0.5, 0.75]:
    p1 = ternary_to_cart(val, 1-val, 0);  p2 = ternary_to_cart(val, 0, 1-val)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'w-', alpha=0.3, linewidth=0.8)
    p1 = ternary_to_cart(1-val, val, 0);  p2 = ternary_to_cart(0, val, 1-val)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'w-', alpha=0.3, linewidth=0.8)
    p1 = ternary_to_cart(1-val, 0, val);  p2 = ternary_to_cart(0, 1-val, val)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'w-', alpha=0.3, linewidth=0.8)

# Triangle outline
ax.plot([0, 1, 0.5, 0], [0, 0, h, 0], 'k-', linewidth=2, zorder=3)

# Overlay fitted circles (full circles so we can see where the centers are)
# theta = np.linspace(0, 2 * np.pi, 600)
# for cx, cy, r in circles:
#     ax.plot(cx + r*np.cos(theta), cy + r*np.sin(theta),
#             '-', color='#ffe066', linewidth=2.0, alpha=0.9, zorder=4)
#     ax.plot(cx, cy, '+', color='#ffe066', markersize=10,
#             markeredgewidth=2.2, zorder=5)

# Corner labels
ax.text(0.00, -0.05, 'S₁₂ = 1\n(S₁₃ = S₂₃ = 0)', ha='center', va='top',
        fontsize=11, fontweight='bold')
ax.text(1.00, -0.05, 'S₁₃ = 1\n(S₁₂ = S₂₃ = 0)', ha='center', va='top',
        fontsize=11, fontweight='bold')
ax.text(0.50, h + 0.04, 'S₂₃ = 1\n(S₁₂ = S₁₃ = 0)', ha='center', va='bottom',
        fontsize=11, fontweight='bold')

# Mark centroid and circle centers
ax.plot(*centroid, 'k+', markersize=12, markeredgewidth=2, zorder=6)

# Legend
# r_val = circles[0][2]
# cx0, cy0 = circles[0][0], circles[0][1]
# d_val = np.hypot(cx0 - centroid[0], cy0 - centroid[1])
# inside_str = "inside" if point_in_triangle(cx0, cy0) else "outside"

legend_elements = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#4a90d9', markersize=14,
           label='Symmetric  (≈ 0.62, 0.62, 0.62)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#d9534f', markersize=14,
           label='Paired  (≈ 0.80, 0.80, 0.00)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#5cb85c', markersize=14,
           label='Single dominant  (≈ 0.94, 0.13, 0.13)'),
    # Line2D([0], [0], color='#ffe066', linewidth=2,
    #        label=f'Fitted circles  r={r_val:.3f}, '
    #              f'd={d_val:.3f} ({inside_str} triangle)'),
]
ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.18),
          ncol=2, fontsize=9.5, framealpha=0.95)

ax.set_xlim(-0.22, 1.22)
ax.set_ylim(-0.22, h + 0.12)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(
    f'Attractor Basin Boundaries — Ternary Diagram\n'
    f'α = {alpha},  S_c = {S_c},  β = {beta}  |  '
    f'Initial conditions: S₁₂ + S₁₃ + S₂₃ = 1',
    fontsize=12, pad=15
)

plt.tight_layout()
plt.savefig('triangle_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: triangle_heatmap.png")
