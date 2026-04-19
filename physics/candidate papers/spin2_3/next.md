# Next

This file is the current working todo list for the `Spin(2,3)` program.

It is organized by what should be done now, what should come next, and what is explicitly bracketed so it does not hold up the main line of work.

---

## Current Position

Already strong enough to build on:

- the local quaternionic reduction frame is explicit enough to use as bridge structure
- the reduced `T1/T2` grading story is explicit enough to support the next derivation steps
- the DIII topological classification is pinned and the natural gapped extension gives `|W_3| = 1`

Still missing at the core:

- a disciplined ambient-to-observable reduction
- a derivation of why the zero-mass operator lives on `T1`
- a bulk derivation of the two-branch dynamics

Working rule:

- do not hold up the rest of the project waiting for the quaternionic sector to become new physics

---

## Now

### N1. Close the Ambient-to-Observable Reduction Enough to Use It

Primary file:

- `0d - ambient reduction scaffold.md`

What to do:

- turn the current bridge into the cleanest possible reduction story
- keep only the parent structure needed for the main derivation chain
- state clearly what is established, what is toy-level, and what remains conjectural
- make the reduction explicit enough to intertwine the parent toy charge generator with `J^{01}`

Deliverable:

- a short reduction kernel that can be cited without dragging the whole scaffold behind it

Done enough when:

- the map from parent hidden-plane data to reduced `T1/T2` structure is stated sharply
- the quaternionic slice is explicitly treated as local reduction geometry, not a new interaction sector
- the reduction story is strong enough to support `N2`
- the basis-level intertwiner is explicit at least for the maximal compact subgroup
- the parent-adapted basis conditions are stated so the remaining ambiguity is only genuinely residual
- the residual stabilizer is identified explicitly, so the canonicity gap is small and named
- the last global `\mathbf Z_2` is located at the readout/time-orientation interface rather than left as a vague basis problem
- the last global `\mathbf Z_2` is sharpened into a forward-semigroup/readout alignment criterion

### N2. Derive the Zero-Mass / Mixing Split from the Reduction

Primary file:

- `2b - dynamics.md`

What to do:

- push the current operator split beyond ansatz level
- justify why `H_0` acts only on `T1`
- isolate exactly where mixing enters

Current sub-burdens:

1. keep the already-built charge-diagonality argument explicit: hidden-line phase covariance is the parent source of the zero-mass charge split
2. keep the intertwiner statement explicit: support preservation is now carried by `J_{\Pi,\mathrm{toy}} \to J^{01}` rather than by separate projector postulates
3. keep the one-sector traversal issue honest: the reduction isolates two oriented candidates, but only one may serve as the unique direct readout channel
4. live open step: derive, rather than merely impose, that the phase-normalized direct readout branch is the constructive/persistent one and therefore has `\kappa_u > 0`

Target identities:

- `H_0 = P H_0 P`
- `Q H_0 = 0`
- `H_0 Q = 0`

Deliverable:

- a clean derivation path, or an honest statement of the minimal extra assumption still required

Done enough when:

- these identities follow from the reduction map together with a derived parent selection principle
- or the project states explicitly that only one final operational axiom remains: direct readout uses the constructive/persistent branch (`\kappa_u > 0` in phase-normalized gauge)
- the status of `H_{\mathrm{mix}}` is separated cleanly from `H_0`

### N3. Derive the Two-Branch Dynamics from the Bulk Side

Primary files:

- `2b - dynamics.md`
- `0d - ambient reduction scaffold.md`

What to do:

- derive the two-branch transport equations from a bulk action, moment map, or equivalent Hamiltonian structure

Current sub-burdens:

1. identify the reduced branch state and the anti-linear branch-exchange operation `\mathcal C(A,B) = (\bar B,\bar A)`
   Current best route: derive `\mathcal C` as the reduced image of the parent charge flip `C_\Pi` combined with conjugation on the selected `u`-complex line
2. derive the `u`-adapted branch symplectic form that gives the exact effective Hamilton-Rayleigh system
3. realize the fixed exchange generator `\mathcal M_{\mathrm{ex}} = -\mathrm{Im}_u(AB)` as the reduced slot whose bulk coefficient is `\kappa_u`
   Best current symmetry route: compact-equivariant anti-linear maps swapping the two charge sectors are unique up to scalar, so any odd parent scalar moment can only land in this exchange slot
4. explain the Rayleigh term `\frac{\gamma}{2}(|A|^2+|B|^2)` as hidden-sector leakage or elimination, ideally through a positive Schur-complement term `K^T\Gamma^{-1}K`
   Best current symmetry route: compact-equivariant elimination gives `\gamma_- I_2 \oplus \gamma_+ I_2`, and charge-exchange symmetry collapses this to scalar `\gamma I_4`

Immediate proof targets:

1. show the reduced odd associator moment is compact-equivariant and anti-linear-exchange odd, so it must descend as `\kappa_u \mathcal M_{\mathrm{ex}}`
2. identify a parent hidden coupling class `(K,\Gamma)` with compact equivariance and charge-exchange symmetry, so scalar `\gamma` is forced

Deliverable:

- a first derivation draft of the transport equations with the minimal generator split made explicit

Done enough when:

- the equations no longer stand only as a strong structural ansatz
- the Hamiltonian-plus-Rayleigh scaffold is derived rather than merely written down
- the role of `\kappa_u`, damping, and branch mixing is tied back to bulk structure
- the remaining open gap is localized to one of the ingredients above rather than to the whole transport system at once

---

## Next

### X1. Topological Observable / Anomaly Bridge

Primary files:

- `2h - topological.md`
- `2g - open problems.md`

What to do:

- identify the observable meaning of the DIII invariant
- test whether anomaly inflow connects the topological and consistency stories

Reason to do this after `Now`:

- the classification is already sharp, but the observable bridge should rest on the stronger reduction/dynamics spine

### X2. Render the Explicit Phase Portrait

Primary context:

- two-branch transport system in `(\rho,\Phi)`

What to do:

- render the locking boundary
- render the persistence boundary
- mark the transport classes, fixed points, and flow directions

Deliverable:

- one clear figure and a short explanatory note

### X3. Hydrogen / Efimov Bridge

Primary context:

- structural threshold analogy already recorded in the current notes

What to do:

- test whether there is a clean `SO(4) / SO(3,1) / SO(2,1)` subgroup bridge
- check whether the Efimov exponent `s_0` can be tied to threshold data such as `\omega/\kappa_u`

Working rule:

- keep this secondary unless it becomes quantitatively predictive

### X4. Representation-Theory Track

Primary context:

- `Spin(2,3) \cong Sp(4,\mathbf{R})`

What to do:

- classify the relevant irreps and relate them to transport classes
- sharpen the `G_2 \cap Spin(2,3)` story if possible

Reason to defer:

- this gets more valuable once the reduction story is cleaner

---

## Later

### L1. Sharpen Static Uniqueness Burdens

- hypercharge uniqueness
- generation counting
- fourth-generation exclusion

### L2. Strengthen the Microscopic Hidden-Sector Story

- first-principles correlator
- relativistic completion
- Heisenberg bridge from the hidden antisymmetric sector

### L3. Push Mature Phenomenology

- parameter constraints
- falsifiable signatures
- direct comparison targets

---

## Bracketed

These are real gaps, but they are not allowed to stop the main program.

### B1. Canonical Quaternionic Slice

Current reading:

- useful local reduction frame
- not yet canonically selected
- not required to be new physics right now

### B2. Strong Interpretation Upgrades

Examples:

- promoting the quaternionic `SU(2)` into a new fundamental interaction sector
- treating the reduction story as fully derived before `N2` and `N3` are done
- making the hydrogen/Efimov bridge carry more weight than the framework has earned

Working rule:

- record the hole honestly
- do not block on it

---

## Practical Order

If working sequentially, use this order:

1. `N1` ambient-to-observable reduction
2. `N2` zero-mass / mixing split
3. `N3` bulk derivation of the two-branch dynamics
4. `X1` topological observable / anomaly bridge
5. `X2` phase portrait
6. `X3` hydrogen / Efimov bridge
7. `X4` representation-theory track

---

## One-Line Rule

Use the quaternionic slice where it helps the reduction; bracket the question of whether it is deeper physics.
