#!/usr/bin/env python3
# Vacuum Impedance 2
# Extracted from relational ontology / physics exploration

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# === THE VACUUM SIMULATION ===
#
# Model: a lattice of three-node units (Feynman loops)
# Each unit: e⁻ node, e⁺ node, γ node
# Internal coupling: sqrt(alpha)
# Units interact with neighbors through shared photon field
#
# The Feynman path integral insight applied:
# Instead of tracking individual particles,
# track the RELATIONAL AMPLITUDE of each three-node closure
#
# Key difference from before:
# - Two types of nodes: FERMIONIC (e⁻, e⁺) and BOSONIC (γ)
# - Fermionic nodes: monogamy budget = 1 (Pauli exclusion - one state only)
# - Bosonic nodes: no monogamy budget (photons can stack - Bose-Einstein)
# - This asymmetry is new and fundamental

alpha = 1/137.036
hbar = 1.0  # natural units
e_charge = np.sqrt(4 * np.pi * alpha)  # coupling in natural units

print("=== VACUUM SIMULATION: SETUP ===")
print()
print(f"alpha = {alpha:.6f}")
print(f"Vertex coupling g = sqrt(4π·alpha) = {e_charge:.6f}")
print(f"This is the amplitude per three-node closure event")
print()

# === SINGLE THREE-NODE UNIT ===
# Nodes: 0=electron, 1=positron, 2=photon
# Relations: S_ep (e-p pair), S_eg (e-gamma), S_pg (p-gamma)
# 
# The asymmetry:
# Fermionic monogamy budget: 1 (hard - Pauli exclusion)
# Bosonic budget: unbounded (photons don't exclude)
#
# But the COUPLING is set by alpha, not by 1
# So the fermionic nodes couple to photon with strength sqrt(alpha)
# The fermionic pair couples to each other with strength alpha (two vertices)

def vacuum_unit_dynamics(state, t, alpha, beta_f):
    """
    Three-node vacuum unit: e⁻, e⁺, γ
    state = [S_ee (pair correlation), S_eg (e-gamma), S_pg (p-gamma)]
    
    Key physics:
    - S_ee: electron-positron correlation (fermionic, tends to annihilate)
    - S_eg, S_pg: fermion-boson coupling (set by sqrt(alpha))
    - Photon node has no monogamy constraint
    - Fermionic nodes have monogamy budget = 1
    """
    S_ee, S_eg, S_pg = state
    
    # Intrinsic dynamics for each relation
    # Cubic with critical point set by physics, not arbitrary
    # For vacuum: the critical threshold is related to alpha
    S_c = alpha  # threshold set by coupling strength - this is the key physical input
    
    def cubic(s, sc):
        return -s * (s - sc) * (s - 1)
    
    # Fermionic pair (e⁻ e⁺): 
    # Natural tendency to annihilate (S_ee → 0) unless stabilized by photon field
    f_ee = cubic(S_ee, S_c)
    
    # Fermion-boson coupling:
    # Vertex amplitude = sqrt(alpha), so coupling strength = alpha
    f_eg = cubic(S_eg, np.sqrt(S_c))
    f_pg = cubic(S_pg, np.sqrt(S_c))
    
    # Competition terms
    # Electron node: budget = 1, couples to positron AND photon
    # beta_f controls how strictly Pauli exclusion enforces monogamy
    electron_load = S_ee + S_eg
    positron_load = S_ee + S_pg
    # Photon node: NO monogamy constraint (bosonic)
    # So photon doesn't compete with itself
    
    comp_ee = beta_f * S_ee * ((electron_load - 1) + (positron_load - 1)) / 2
    comp_eg = beta_f * S_eg * (electron_load - 1) / 2  # only electron side constrained
    comp_pg = beta_f * S_pg * (positron_load - 1) / 2  # only positron side constrained
    
    dS_ee = f_ee - comp_ee
    dS_eg = f_eg - comp_eg
    dS_pg = f_pg - comp_pg
    
    return [dS_ee, dS_eg, dS_pg]

t = np.linspace(0, 500, 10000)

print("=== SINGLE VACUUM UNIT: FIXED POINT ANALYSIS ===")
print()

# Scan initial conditions
beta_f = 0.5  # Pauli exclusion strength

results = {}
for ic_name, ic in [
    ("Symmetric (0.5,0.5,0.5)", [0.5, 0.5, 0.5]),
    ("Pair dominant", [0.8, 0.1, 0.1]),
    ("Photon dominant", [0.1, 0.8, 0.8]),
    ("All weak", [0.05, 0.05, 0.05]),
    ("Just above alpha", [alpha*1.1, alpha*1.1, alpha*1.1]),
    ("At alpha", [alpha, alpha, alpha]),
]:
    sol = odeint(vacuum_unit_dynamics, ic, t, args=(alpha, beta_f))
    final = sol[-1]
    results[ic_name] = final
    print(f"IC: {ic_name}")
    print(f"  Final: S_ee={final[0]:.6f}, S_eg={final[1]:.6f}, S_pg={final[2]:.6f}")
    print(f"  Sum: {sum(final):.6f}")
    print()

print("=== THE IMPEDANCE CALCULATION ===")
print()

# The bulk impedance of the vacuum emerges from how the network
# responds to an applied electromagnetic perturbation
#
# In our model:
# - Apply a small perturbation to the photon field (S_eg, S_pg)
# - Measure the induced current (change in S_ee)
# - Impedance = perturbation / induced current
#
# This is the network analog of Z = V/I
#
# For a network of N three-node units:
# The photon field couples to all units simultaneously
# Each unit responds according to its alpha-weighted dynamics
# The collective response is the bulk impedance

def vacuum_network_dynamics(state, t, alpha, beta_f, N, J_ext):
    """
    N three-node vacuum units on a lattice
    state: [S_ee_0, S_eg_0, S_pg_0, S_ee_1, S_eg_1, S_pg_1, ...]
    J_ext: external photon field perturbation
    """
    ds = np.zeros(3*N)
    S_c = alpha
    
    def cubic(s, sc):
        return -s * (s - sc) * (s - 1)
    
    for i in range(N):
        S_ee = state[3*i]
        S_eg = state[3*i + 1]
        S_pg = state[3*i + 2]
        
        # Add external photon field to boson coupling
        S_eg_eff = S_eg + J_ext
        S_pg_eff = S_pg + J_ext
        
        f_ee = cubic(S_ee, S_c)
        f_eg = cubic(S_eg_eff, np.sqrt(S_c))
        f_pg = cubic(S_pg_eff, np.sqrt(S_c))
        
        electron_load = S_ee + S_eg
        positron_load = S_ee + S_pg
        
        comp_ee = beta_f * S_ee * ((electron_load - 1) + (positron_load - 1)) / 2
        comp_eg = beta_f * S_eg * (electron_load - 1) / 2
        comp_pg = beta_f * S_pg * (positron_load - 1) / 2
        
        # Nearest-neighbor photon coupling
        # Photons from adjacent units can interact
        if i > 0:
            neighbor_photon = (state[3*(i-1)+1] + state[3*(i-1)+2]) / 2
        else:
            neighbor_photon = 0
        if i < N-1:
            neighbor_photon += (state[3*(i+1)+1] + state[3*(i+1)+2]) / 2
        else:
            neighbor_photon += 0
            
        photon_coupling = alpha * neighbor_photon
        
        ds[3*i] = f_ee - comp_ee
        ds[3*i + 1] = f_eg - comp_eg + photon_coupling
        ds[3*i + 2] = f_pg - comp_pg + photon_coupling
    
    return ds

# Run network to ground state first (no external field)
N = 10
ic_network = [alpha] * (3*N)  # start near vacuum coupling strength
t_relax = np.linspace(0, 1000, 5000)

ground_state = odeint(vacuum_network_dynamics, ic_network, t_relax, 
                       args=(alpha, beta_f, N, 0.0))[-1]

print(f"Network of N={N} vacuum units")
print(f"Ground state (averaged):")
S_ee_gs = np.mean([ground_state[3*i] for i in range(N)])
S_eg_gs = np.mean([ground_state[3*i+1] for i in range(N)])
S_pg_gs = np.mean([ground_state[3*i+2] for i in range(N)])
print(f"  <S_ee> = {S_ee_gs:.6f}  (pair correlation)")
print(f"  <S_eg> = {S_eg_gs:.6f}  (e-photon coupling)")
print(f"  <S_pg> = {S_pg_gs:.6f}  (p-photon coupling)")
print()

# Apply perturbation and measure response
J_values = np.linspace(0, 0.01, 20)
responses = []

for J in J_values:
    perturbed = odeint(vacuum_network_dynamics, ground_state.copy(), 
                       np.linspace(0, 100, 1000),
                       args=(alpha, beta_f, N, J))[-1]
    
    # Induced current = change in pair correlation (S_ee)
    delta_S_ee = np.mean([perturbed[3*i] - ground_state[3*i] for i in range(N)])
    responses.append(delta_S_ee)

responses = np.array(responses)

# Impedance = J / delta_S_ee (analog of V/I)
# Use linear regime (small J)
linear_mask = J_values > 0.0001
if np.any(linear_mask) and np.any(responses[linear_mask] != 0):
    Z_ratio = np.mean(J_values[linear_mask] / (responses[linear_mask] + 1e-10))
    print(f"Simulated impedance ratio (J/delta_S_ee): {Z_ratio:.4f}")
else:
    Z_ratio = None
    print("Response too small to measure impedance directly")

print()
print(f"Target: Z₀ = 2α × R_K")
print(f"In natural units (R_K = 1): Z₀_natural = 2α = {2*alpha:.6f}")
print(f"Ground state photon coupling: {S_eg_gs:.6f}")
print(f"Ratio: {S_eg_gs/(2*alpha):.4f}")
print()
