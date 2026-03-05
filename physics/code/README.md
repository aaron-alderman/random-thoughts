# Relational Ontology Physics — All Programs

## Python Simulation Scripts

### Three-Node Dynamics
- `three_node_attractors.py` — Initial 3-node relational dynamics: fixed-point analysis, attractor census across 59 initial conditions
- `three_node_attractors_2.py` — Extended 3-node analysis: phase space visualisation, bifurcation scans (varying β and S_c), attractor taxonomy

### Golden Ratio Analysis
- `golden_ratio_analysis.py` — Analytic fixed-point derivation, golden ratio proximity check (S* ≈ 0.622 vs 1/φ ≈ 0.618), parameter search for exact φ match

### Four-Node Dynamics
- `four_node_dynamics.py` — 4-node system: 6 pairwise relations, structured IC tests, attractor census (100 random ICs), analytic fixed point
- `four_node_dynamics_2.py` — Per-node load analysis, n-node scaling law, ratio of successive S*, stability analysis
- `four_node_dynamics_3.py` — Full visualisation: 3-node vs 4-node comparison, basin maps, attractor census bar chart, n-node scaling plot

### Sierpinski / Fractal Emergence
- `sierpinski.py` — Sierpinski triangle emergence from monogamy constraints, scaling law (2/3)^n, Hausdorff dimension calculation
- `sierpinski_2.py` — Rule 90 connection, boundary-selection parallel
- `sierpinski_3.py` — Extended Sierpinski analysis with visualisations
- `sierpinski_4.py` — Coherence propagation along Sierpinski skeleton
- `sierpinski_5.py` — Full Sierpinski visualisation suite

### Vacuum / QED / Impedance
- `vacuum_impedance.py` — Feynman connections, Z₀ = 2αR_K identity verification, QED vertex as 3-node closure
- `vacuum_impedance_2.py` — Vacuum simulation with S_c = α, asymmetric bosonic/fermionic monogamy, ground state verification
- `vacuum_impedance_3.py` — Full vacuum polarisation analysis, β_QED = α²/(3π) derivation, energy landscape
- `vacuum_impedance_4.py` — Derivation analysis: what is solid vs gestured at
- `vacuum_impedance_5.py` — Extended vacuum impedance with linear response, Z₀ calculation attempt

## Running the Python scripts
```bash
pip install numpy scipy matplotlib
python3 <script_name>.py
```
