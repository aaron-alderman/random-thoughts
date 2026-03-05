#!/usr/bin/env python3
# Three Node Attractors 2
# Extracted from relational ontology / physics exploration

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

t = np.linspace(0, 30, 2000)

fig = plt.figure(figsize=(16, 12))

# Plot 1: Phase space - the two main attractors
ax1 = fig.add_subplot(221, projection='3d')

test_cases = [
    ([0.8, 0.8, 0.8], 'blue', 'Symmetric high'),
    ([0.1, 0.1, 0.1], 'cyan', 'Symmetric low'),
    ([0.5, 0.5, 0.5], 'green', 'Midpoint'),
    ([0.8, 0.8, 0.1], 'red', 'Two high one low'),
    ([0.8, 0.1, 0.1], 'orange', 'One high two low'),
    ([1.0, 1.0, 0.0], 'purple', 'Max pair'),
    ([0.31, 0.31, 0.31], 'magenta', 'Just above S_c'),
    ([0.29, 0.29, 0.29], 'brown', 'Just below S_c'),
]

for ic, color, label in test_cases:
    sol = odeint(relational_dynamics, ic, t, args=(alpha, S_c, beta))
    ax1.plot(sol[:,0], sol[:,1], sol[:,2], color=color, alpha=0.7, linewidth=1.5, label=label)
    ax1.scatter(*sol[-1], color=color, s=50, zorder=5)

ax1.set_xlabel('S12')
ax1.set_ylabel('S13')
ax1.set_zlabel('S23')
ax1.set_title('Phase Space Trajectories')
ax1.legend(fontsize=6, loc='upper left')

# Plot 2: Time series showing attractor types
ax2 = fig.add_subplot(222)

attractor_examples = [
    ([0.5, 0.5, 0.5], 'blue', 'Symmetric attractor (0.62,0.62,0.62)'),
    ([0.8, 0.8, 0.1], 'red', 'Asymmetric attractor (0.8,0.8,0)'),
    ([0.8, 0.1, 0.1], 'orange', 'Single dominant (0.94,0.13,0.13)'),
]

for ic, color, label in attractor_examples:
    sol = odeint(relational_dynamics, ic, t, args=(alpha, S_c, beta))
    ax2.plot(t[:300], sol[:300,0], color=color, linewidth=2)
    ax2.plot(t[:300], sol[:300,1], color=color, linewidth=2, linestyle='--')
    ax2.plot(t[:300], sol[:300,2], color=color, linewidth=2, linestyle=':')
    ax2.axhline(y=sol[-1,0], color=color, alpha=0.3, linewidth=0.5)

ax2.set_xlabel('Time')
ax2.set_ylabel('S values')
ax2.set_title('Time Evolution - Three Attractor Types')
ax2.set_ylim(-0.05, 1.05)
ax2.grid(True, alpha=0.3)

# Plot 3: Scan beta (coupling strength) to find bifurcations
ax3 = fig.add_subplot(223)

betas = np.linspace(0, 2.0, 50)
sym_attractor = []
asym_attractor_high = []
asym_attractor_low = []

for b in betas:
    # Symmetric IC
    sol = odeint(relational_dynamics, [0.5, 0.5, 0.5], t, args=(alpha, S_c, b))
    sym_attractor.append(sol[-1, 0])
    
    # Asymmetric IC
    sol2 = odeint(relational_dynamics, [0.8, 0.8, 0.1], t, args=(alpha, S_c, b))
    asym_attractor_high.append(sol2[-1, 0])
    asym_attractor_low.append(sol2[-1, 2])

ax3.plot(betas, sym_attractor, 'b-', linewidth=2, label='Symmetric IC → S12')
ax3.plot(betas, asym_attractor_high, 'r-', linewidth=2, label='Asym IC → S12 (high pair)')
ax3.plot(betas, asym_attractor_low, 'r--', linewidth=2, label='Asym IC → S23 (excluded)')
ax3.axvline(x=0.5, color='gray', linestyle=':', alpha=0.7, label='Current beta')
ax3.set_xlabel('Beta (coupling strength)')
ax3.set_ylabel('Final S value')
ax3.set_title('Bifurcation with Coupling Strength')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Plot 4: Scan S_c to find phase transitions
ax4 = fig.add_subplot(224)

s_cs = np.linspace(0.1, 0.8, 60)
sym_finals = []
asym_finals_high = []
asym_finals_low = []

for sc in s_cs:
    sol = odeint(relational_dynamics, [0.5, 0.5, 0.5], t, args=(alpha, sc, beta))
    sym_finals.append(sol[-1, 0])
    
    sol2 = odeint(relational_dynamics, [0.8, 0.8, 0.1], t, args=(alpha, sc, beta))
    asym_finals_high.append(sol2[-1, 0])
    asym_finals_low.append(sol2[-1, 2])

ax4.plot(s_cs, sym_finals, 'b-', linewidth=2, label='Symmetric IC final S')
ax4.plot(s_cs, asym_finals_high, 'r-', linewidth=2, label='High pair final S')
ax4.plot(s_cs, asym_finals_low, 'r--', linewidth=2, label='Excluded relation final S')
ax4.plot(s_cs, s_cs, 'k:', alpha=0.5, label='S_c line')
ax4.axvline(x=0.3, color='gray', linestyle=':', alpha=0.7, label='Current S_c')
ax4.set_xlabel('S_c (critical threshold)')
ax4.set_ylabel('Final S value')
ax4.set_title('Phase Transitions with Critical Threshold')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('relational_dynamics.png', dpi=150, bbox_inches='tight')
plt.close()

# Now let's identify the attractor types clearly
print("=== ATTRACTOR TAXONOMY ===")
print()
print("TYPE 1: SYMMETRIC ATTRACTOR")
print("IC: any symmetric (0.5,0.5,0.5) or (0.1,0.1,0.1) or (0.8,0.8,0.8)")
sol = odeint(relational_dynamics, [0.5,0.5,0.5], t, args=(alpha,S_c,beta))
print(f"Final: ({sol[-1,0]:.4f}, {sol[-1,1]:.4f}, {sol[-1,2]:.4f})")
print(f"Sum: {sum(sol[-1]):.4f}")
print(f"Character: all three relations stable at ~0.622")
print()

print("TYPE 2: PAIRED ATTRACTOR") 
print("IC: two high, one low e.g. (0.8,0.8,0.1)")
sol = odeint(relational_dynamics, [0.8,0.8,0.1], t, args=(alpha,S_c,beta))
print(f"Final: ({sol[-1,0]:.4f}, {sol[-1,1]:.4f}, {sol[-1,2]:.4f})")
print(f"Sum: {sum(sol[-1]):.4f}")
print(f"Character: two relations maximize, one collapses to zero")
print()

print("TYPE 3: SINGLE DOMINANT")
print("IC: one high, two low e.g. (0.8,0.1,0.1)")
sol = odeint(relational_dynamics, [0.8,0.1,0.1], t, args=(alpha,S_c,beta))
print(f"Final: ({sol[-1,0]:.4f}, {sol[-1,1]:.4f}, {sol[-1,2]:.4f})")
print(f"Sum: {sum(sol[-1]):.4f}")
print(f"Character: one relation dominates, others suppressed")
print()

print("=== THE INTERESTING FINDING ===")
print()
print("Just above S_c (0.31,0.31,0.31):")
sol = odeint(relational_dynamics, [0.31,0.31,0.31], t, args=(alpha,S_c,beta))
print(f"Final: ({sol[-1,0]:.4f}, {sol[-1,1]:.4f}, {sol[-1,2]:.4f}) - goes SYMMETRIC")
print()
print("Just below S_c (0.29,0.29,0.29):")
sol = odeint(relational_dynamics, [0.29,0.29,0.29], t, args=(alpha,S_c,beta))
print(f"Final: ({sol[-1,0]:.4f}, {sol[-1,1]:.4f}, {sol[-1,2]:.4f}) - also goes SYMMETRIC")
print()
print("Why? Because symmetric perturbations stay symmetric.")
print("The basin of attraction for symmetric vs paired depends on ASYMMETRY not magnitude.")
print()

print("=== BASIN OF ATTRACTION BOUNDARY ===")
print("Scanning IC = (x, x, 0.1) to find where paired vs symmetric transition occurs:")
for x in np.arange(0.2, 0.9, 0.05):
    sol = odeint(relational_dynamics, [x, x, 0.1], t, args=(alpha,S_c,beta))
    diff = abs(sol[-1,0] - sol[-1,2])
    attractor_type = "PAIRED" if diff > 0.3 else "SYMMETRIC"
    print(f"  IC=({x:.2f},{x:.2f},0.10) -> ({sol[-1,0]:.3f},{sol[-1,1]:.3f},{sol[-1,2]:.3f}) [{attractor_type}]")
