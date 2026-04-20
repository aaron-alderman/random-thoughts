# 🧭 Handoff Document — Phase II

## Relational Decomposition Framework → New Physics Program

---

# 1. Objective

Extend the **decomposition inconsistency framework** beyond Efimov physics to:

* identify **new universal regimes**
* classify **few-body systems structurally**
* generate **testable predictions**

---

## Core Principle (carry forward)

> Physical behavior emerges from **consistency constraints across competing decompositions**.
> Universality arises when a **scale-independent collective mode** forms.

---

# 2. What is Already Established (Do NOT redo)

* 3-body identical bosons → 3 decomposition charts
* Bethe–Peierls → cross-chart coupling
* symmetric collective mode → Efimov channel
* scale independence → (1/\rho^2)
* only invariant quantity:
  [
  \lambda_{\text{sym}} = -s_0^2 - \frac{1}{4}
  ]

---

# 3. New Program: General Method

## Step 1 — Identify decomposition space

For a given system:

* list all valid **factorizations / pairings / channels**
* treat them as basis states

---

## Step 2 — Build coupling graph

Construct:

* nodes = decompositions
* edges = coupling strength (from physics)

This replaces the simple 3×3 matrix.

---

## Step 3 — Apply constraints

From underlying physics:

* symmetry (bosonic, fermionic, mass imbalance)
* boundary conditions (zero-range, finite-range)
* kinematics

These determine:

* which couplings exist
* whether they are equal / suppressed

---

## Step 4 — Look for collective modes

Solve:

* eigenmodes of coupling structure
* identify **symmetric or dominant collective modes**

---

## Step 5 — Check scale structure

Key question:

> does the effective operator become **scale-independent** in some regime?

If yes:

* expect (1/\rho^2)-like behavior
* candidate for universality

---

## Step 6 — Check criticality

Determine if eigenvalue crosses:

[
\lambda = -\frac{1}{4}
]

If:

* above → no instability
* below → Efimov-like / new regime

---

# 4. First Target Systems (Priority Order)

---

## 🥇 Target 1 — Mass-imbalanced systems

### System:

* 2 heavy + 1 light (HHL)

### Known:

* Efimov scaling changes with mass ratio
* disappears below threshold

---

### Task

1. Build decomposition graph:

   * (HH)+L
   * (HL)+H (×2)

2. Note asymmetry:

   * couplings not equal

3. Compute:

   * how symmetry breaking affects eigenvalues

---

### Goal

> Derive **mass ratio threshold** for Efimov effect from decomposition asymmetry

---

### Expected payoff

* structural explanation of known threshold (~13.6 for fermions)
* possible prediction of new regimes

---

## 🥈 Target 2 — Fermionic systems

### System:

* identical fermions + one distinguishable particle

---

### Key effect:

* Pauli exclusion removes some channels

---

### Task

1. Remove forbidden decompositions
2. Build reduced coupling graph
3. Analyze eigenmodes

---

### Goal

> Show Efimov disappears because **symmetric mode is not allowed**

---

### Big insight

> universality requires **symmetry-compatible collective mode**

---

## 🥉 Target 3 — 2D vs 3D

### Known:

* Efimov exists in 3D, not 2D

---

### Task

1. Rebuild decomposition structure in 2D
2. Check:

   * scale invariance?
   * kernel structure?
   * eigenvalue behavior?

---

### Goal

> explain dimensional dependence via **decomposition structure collapse**

---

# 5. Second Layer (Harder, Higher Impact)

---

## Target 4 — 4-body systems

### System:

* 4 identical bosons

---

### Structure:

* many decompositions:

  * 2+2
  * 3+1
  * etc.

---

### Task

1. Enumerate decomposition graph
2. Identify dominant modes
3. Look for scale-independent sectors

---

### Goal

> explain tetramer states as higher-order collective modes

---

## Target 5 — Finite-range corrections

### System:

* real interactions with scale (r_0)

---

### Task

1. introduce scale into coupling
2. track breakdown of scale invariance

---

### Goal

> understand **how universality dies**

---

# 6. Deliverables for Each Case

Each system should produce:

---

## A. Decomposition graph

* nodes + couplings
* symmetry constraints

---

## B. Reduced operator

* matrix or integral form

---

## C. Eigenmode structure

* symmetric / broken modes

---

## D. Scaling behavior

* does (1/\rho^2) appear?

---

## E. Critical condition

* does eigenvalue cross (-1/4)?

---

## F. Physical prediction

* bound states?
* scaling law?
* absence of universality?

---

# 7. Minimal Working Example (Template)

For any system:

1. define decomposition basis
2. write coupling matrix (symbolic OK)
3. impose symmetry
4. diagonalize
5. identify dominant mode
6. check scaling
7. compare to known physics

---

# 8. What Counts as Success

You have real new physics if you can:

* predict when Efimov appears/disappears
* derive thresholds from structure
* explain known anomalies
* identify new scaling regimes

---

# 9. Biggest Pitfalls

Avoid:

* trying to define ε₀, W₀ uniquely
* overfitting to known results
* assuming symmetry where it doesn’t exist

Always:

* focus on eigenvalues, not components
* separate representation vs invariant

---

# 10. One-Line Program Summary

> Use decomposition graphs and their collective modes to identify when scale-independent physics — and therefore universality — must emerge.

---

# 11. Immediate Next Step

Start with:

👉 **mass-imbalanced 3-body system**

because:

* simplest deviation from known case
* already rich physics
* high chance of publishable result
