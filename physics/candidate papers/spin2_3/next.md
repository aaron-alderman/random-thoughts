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

Deliverable:

- a short reduction kernel that can be cited without dragging the whole scaffold behind it

Done enough when:

- the map from parent hidden-plane data to reduced `T1/T2` structure is stated sharply
- the quaternionic slice is explicitly treated as local reduction geometry, not a new interaction sector
- the reduction story is strong enough to support `N2`

### N2. Derive the Zero-Mass / Mixing Split from the Reduction

Primary file:

- `2b - dynamics.md`

What to do:

- push the current operator split beyond ansatz level
- justify why `H_0` acts only on `T1`
- isolate exactly where mixing enters

Current sub-burdens:

1. derive charge-diagonality of the parent zero-mass operator from hidden-line phase covariance
2. justify the one-sector traversal principle under the selected zero-mass channel
3. show that the reduction map preserves that support into `T1/T2`

Target identities:

- `H_0 = P H_0 P`
- `Q H_0 = 0`
- `H_0 Q = 0`

Deliverable:

- a clean derivation path, or an honest statement of the minimal extra assumption still required

Done enough when:

- these identities follow from the reduction map or from a clearly stated parent selection principle
- the status of `H_{\mathrm{mix}}` is separated cleanly from `H_0`

### N3. Derive the Two-Branch Dynamics from the Bulk Side

Primary files:

- `2b - dynamics.md`
- `0d - ambient reduction scaffold.md`

What to do:

- derive the two-branch transport equations from a bulk action, moment map, or equivalent Hamiltonian structure

Deliverable:

- a first derivation draft of the transport equations

Done enough when:

- the equations no longer stand only as a strong structural ansatz
- the role of `\kappa_u`, damping, and branch mixing is tied back to bulk structure

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
