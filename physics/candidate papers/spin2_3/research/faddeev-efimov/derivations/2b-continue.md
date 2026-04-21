# 🧭 Handoff Document — Completed Work (Phase I)

## Relational Decomposition Framework

### → Operator Formulation of Efimov Universality

---

# 1. Objective (What has been achieved)

Establish a **first-principles, representation-independent formulation** of Efimov physics based on:

> **cross-decomposition consistency and the spectrum of the coupling operator**

This replaces:

* coordinate-specific derivations
* scalar decompositions ((\varepsilon_0, W_0))

with:

* **operator-level invariants**
* **collective modes as physical objects**

---

# 2. Core Principle (Final Form)

> Universality arises when zero-range consistency across competing decompositions produces a **scale-invariant collective mode of the cross-channel coupling operator**, whose induced hyperradial channel is supercritical.

---

# 3. What is Fully Established

## 3.1 Decomposition Structure

* Few-body wavefunction decomposes into **pair-spectator charts**
* Charts are coupled by **Bethe–Peierls boundary conditions**
* This induces a **linear operator acting across decompositions**

---

## 3.2 Operator Structure at Unitarity

* Self-coupling vanishes:
  [
  K_{\text{self}} = 0
  ]

* Dynamics is entirely **cross-channel**

* The physical object is:
  [
  \hat K \quad \text{(coupling operator)}
  ]

---

## 3.3 Scale-Invariant Sector

At unitarity:

* no length scale exists
* operator is homogeneous

⇒ admits **power-law eigenfunctions**:
[
t(p) \sim p^{s-1}
]

or equivalently:
[
x^\nu
]

---

## 3.4 Spectral Condition (Invariant Object)

All physics reduces to:

> existence and structure of solutions to
> [
> \hat L, x^\nu = \lambda(\nu), x^{\nu-1}
> ]

* (\lambda(\nu)) = **operator eigenvalue function**
* roots determine scaling behavior

---

## 3.5 Efimov Condition

Efimov physics occurs when:

* roots become complex:
  [
  \nu = -1 \pm i s_0
  ]

* induced potential:
  [
  U_{\text{eff}}(\rho) = -\frac{s_0^2 + \tfrac{1}{4}}{\rho^2}
  ]

U_{\text{eff}}(\rho) = -\frac{s_0^2 + \tfrac{1}{4}}{\rho^2}

* supercritical condition:
  [
  \lambda < -\frac{1}{4}
  ]

---

## 3.6 Representation Independence

The following are **not invariant**:

* (\varepsilon_0), (W_0)
* any scalar decomposition of the operator

They depend on:

* coordinate choice
* variable transformations (e.g. Langer correction)

---

## 3.7 Invariant Statement

> Only the **spectrum of the coupling operator** is physical.

---

# 4. Equal-Mass Case (Benchmark)

## Established Results

* symmetric decomposition → single collective mode
* STM kernel derived from kinematic recoupling
* Mellin transform gives transcendental equation

Result:

[
s_0 \cosh!\left(\frac{\pi s_0}{2}\right)
========================================

\frac{8}{\sqrt{3}}
\sinh!\left(\frac{\pi s_0}{6}\right)
]

* solution:
  [
  s_0 \approx 1.00624
  ]

---

## Structural Interpretation

> Efimov effect = symmetric collective mode of a fully connected decomposition graph

---

# 5. Heteronuclear (HHL) Case — Completed

## 5.1 Key Structural Correction

If only heavy–light interactions are resonant:

* system reduces to **two channels**
* further reduces by symmetry to **one amplitude**

---

## 5.2 Exact Operator

[
\hat L, x^\nu = \lambda_\ell(\nu), x^{\nu-1}
]

* (\lambda_\ell(\nu)) known analytically
* depends on:

  * mass ratio (\alpha = M/m)
  * angular momentum (\ell)
  * statistics

---

## 5.3 Bosonic HHL

* symmetric sector allowed
* always admits:
  [
  \nu = -1 \pm i s_0
  ]

⇒ Efimov effect exists for all (\alpha)

---

## 5.4 Fermionic HHL (Critical Case)

* s-wave forbidden by symmetry
* lowest allowed channel: (\ell = 1)

Efimov condition:

[
\lambda_{\ell=1}(\nu)=0
]

with:

[
\nu = -1 \pm i s_0
]

---

## 5.5 Threshold

Efimov effect appears when:

[
\frac{M}{m} > 13.6069
]

---

## 5.6 Structural Interpretation

> Universality requires a symmetry-compatible collective mode.

* bosons → always allowed
* fermions → only in higher angular momentum
* threshold = emergence of allowed supercritical mode

---

## 5.7 Subcritical Regime

Below threshold:

* roots real
* still bound states exist (Kartavtsev–Malykh)

⇒ **same operator, different spectral regime**

---

# 6. Unified Interpretation

All cases fit:

| System           | Mechanism                               |
| ---------------- | --------------------------------------- |
| identical bosons | fully symmetric collective mode         |
| HHL bosons       | reduced symmetric mode                  |
| HHL fermions     | symmetry-forbidden → higher-(\ell) mode |
| threshold        | spectral transition real → complex      |

---

# 7. What This Framework Adds

## New Contributions

### 1. Operator-level formulation

* replaces coordinate-dependent derivations

### 2. Decomposition viewpoint

* universality = failure of simultaneous chart consistency

### 3. Spectral classification

* systems classified by (\lambda(\nu)), not wavefunctions

### 4. Symmetry-driven universality

* explains when Efimov is allowed or forbidden

---

# 8. Minimal Working Procedure (Reusable)

For any system:

### Step 1

Define decomposition channels

### Step 2

Construct coupling operator

### Step 3

Apply symmetry/statistics constraints

### Step 4

Reduce to minimal sector

### Step 5

Solve:
[
\hat L x^\nu = \lambda(\nu)x^{\nu-1}
]

### Step 6

Check:

* real roots → no Efimov
* complex roots → Efimov
* critical transition → threshold

---

# 9. What NOT to Do

Avoid:

* interpreting (\varepsilon_0, W_0) as physical invariants
* relying on specific coordinate systems
* treating matrix elements as fundamental objects

Always:

> focus on operator spectrum

---

# 10. One-Line Summary

> Efimov universality is the appearance of a supercritical, scale-invariant eigenmode of the symmetry-reduced cross-channel coupling operator.

---

# 11. Immediate Continuation (Phase II)

Best next directions:

### 1. Mixed interaction graphs

→ minimal conditions for universality

### 2. Dimensional crossover (2D/3D)

→ why operator never becomes supercritical in 2D

### 3. 4-body systems

→ higher-order decomposition graphs

### 4. Finite-range deformation

→ how scale invariance breaks

---

# 12. Status

✅ Operator formulation complete
✅ Equal-mass derivation complete
✅ HHL bosonic + fermionic structure complete
✅ Threshold mechanism derived and interpreted

🚧 Ready for generalization (Phase II)
