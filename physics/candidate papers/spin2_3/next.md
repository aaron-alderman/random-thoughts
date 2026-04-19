# Next

This file is the current working todo list for the `Spin(2,3)` program.

It is organized by what should be done now, what should come next, and what is explicitly bracketed so it does not hold up the main line of work.

---

## Current Position

Already strong enough to build on:

- the ambient-to-observable reduction is closed at the toy level: explicit basis-level intertwiner, full maximal compact and noncompact extension, residual ambiguity reduced to one `\mathbf Z_2` fixed by the forward-semigroup / readout alignment criterion
- the reduced `T1/T2` grading story, exchange structure, and scalar damping argument are explicit in `2b - dynamics.md`
- the DIII topological classification is pinned and the natural gapped extension gives `|W_3| = 1`

Still missing at the core:

- a derivation that the direct readout branch is constructive/persistent (`\kappa_u > 0`) from the octonionic bulk — this closes both the zero-mass support question and the bulk origin of the two-branch dynamics

Working rule:

- do not hold up the rest of the project waiting for the quaternionic sector to become new physics

---

## Now

Shared live blocker for N2 and N3: derive that the direct readout branch is constructive/persistent (`\kappa_u > 0`) from the octonionic associator moment rather than accepting it as the final operational axiom.

### N2. Derive the Zero-Mass / Mixing Split from the Reduction

Primary file:

- `2b - dynamics.md`

What to do:

- push the current operator split beyond ansatz level
- justify why `H_0` acts only on `T1`
- isolate exactly where mixing enters

Status:

- charge-diagonality (hidden-line phase covariance), support preservation (charge-generator intertwiner `J_{\Pi,\mathrm{toy}} \to J^{01}`), and one-sector traversal are all conditionally in place via the reduction map
- live open step: derive that the phase-normalized direct readout branch is the constructive/persistent one and therefore has `\kappa_u > 0`

Target identities:

- `H_0 = P H_0 P`
- `Q H_0 = 0`
- `H_0 Q = 0`

Deliverable:

- a clean derivation path, or an honest statement of the minimal extra assumption still required

Done enough when:

- the constructive/persistent branch condition (`\kappa_u > 0`) is derived from the octonionic bulk rather than stated as a final operational rule, or the project names it explicitly as the one remaining axiom
- the status of `H_{\mathrm{mix}}` is separated cleanly from `H_0`

### N3. Derive the Two-Branch Dynamics from the Bulk Side

Primary files:

- `2b - dynamics.md`
- `0d - ambient reduction scaffold.md`

What to do:

- derive the two-branch transport equations from a bulk action, moment map, or equivalent Hamiltonian structure

Status:

- the exchange map `\mathcal C(A,B) = (\bar B,\bar A)`, the symplectic form, and the exchange generator `\mathcal M_{\mathrm{ex}} = -\mathrm{Im}_u(AB)` are all explicit in 2b; the uniqueness of `\mathcal C` as the compact-equivariant anti-linear exchange is established
- scalar `\gamma` from compact-equivariant, charge-exchange-symmetric hidden elimination is substantially addressed (see 2b admissibility criterion)
- live proof target: show the octonionic associator moment projected onto `u` is compact-equivariant and anti-linear-exchange odd, forcing it to descend as `\kappa_u \mathcal M_{\mathrm{ex}}`

Deliverable:

- a first derivation draft of the transport equations with the minimal generator split made explicit

Done enough when:

- the associator moment's compact-equivariance and exchange-odd character are established, so `\kappa_u \mathcal M_{\mathrm{ex}}` is the forced reduced form rather than a structural ansatz
- the remaining gap, if any, is named at the level of a single identified missing ingredient rather than at the whole-system level

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

1. `N2` / `N3` κ_u / associator derivation (shared live blocker)
2. `X1` topological observable / anomaly bridge
3. `X2` phase portrait
4. `X3` hydrogen / Efimov bridge
5. `X4` representation-theory track

---

## One-Line Rule

Use the quaternionic slice where it helps the reduction; bracket the question of whether it is deeper physics.
