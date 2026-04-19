# Next

This file is the current working todo list for the `Spin(2,3)` program.

It is organized by what should be done now, what should come next, and what is explicitly bracketed so it does not hold up the main line of work.

---

## Current Position

Already strong enough to build on:

- the ambient-to-observable reduction is closed at the toy level: explicit basis-level intertwiner, full maximal compact and noncompact extension, residual ambiguity reduced to one `\mathbf Z_2` fixed by the forward-semigroup / readout alignment criterion
- the reduced `T1/T2` grading story, exchange structure, and scalar damping argument are explicit in `2b - dynamics.md`
- the DIII topological classification is pinned and the natural gapped extension gives `|W_3| = 1`
- the associator moment descent is established: `\kappa_u` is `K`-invariant by `K \subset \mathrm{Stab}_{G_2}(u)` and exchange-odd by `\mathfrak K_u : u \mapsto -u`, forcing it to descend as the unique coefficient of `\mathcal M_{\mathrm{ex}}`; the coupling term in the two-branch equations is no longer a structural ansatz

Still open, but no longer blocking:

- **orientation axiom**: `\kappa_u > 0` is named as the explicit final axiom — the constructive readout branch has `\mathrm{Re}_u(AB)|_* > 0` at the transport fixed point; bulk derivation of the sign is a sharpening task, not a programme blocker
- **parent action**: `\kappa_u \mathcal M_{\mathrm{ex}}` (coupling) and `\omega\,\mu_{U(1)}` (rotation) are now symmetry-derived; `\gamma > 0` is established by K-injectivity + Γ > 0; deriving all three from a single parent octonionic action simultaneously remains open but is not needed to proceed

Working rule:

- do not hold up the rest of the project waiting for the quaternionic sector to become new physics

---

## Now

**N2 and N3 are conditionally closed.** The programme can proceed.

### N2. Derive the Zero-Mass / Mixing Split from the Reduction — Closed

Primary file: `2b - dynamics.md`

Closed under the orientation axiom. In place:

- charge-diagonality, support preservation via `J_{\Pi,\mathrm{toy}} \to J^{01}` intertwiner, one-sector traversal
- `\kappa_u \mathcal M_{\mathrm{ex}}` coupling term symmetry-forced (associator descent)
- orientation axiom named: `\kappa_u > 0` iff `\mathrm{Re}_u(AB)|_* > 0` (constructive branch interference)
- conditionally: `H_0 = PH_0P`, `QH_0 = 0`, `H_0Q = 0`

Sharpening task (non-blocking): derive `\kappa_u > 0` from the parent octonionic geometry rather than the readout alignment criterion.

### N3. Derive the Two-Branch Dynamics from the Bulk Side — Conditionally Closed

Primary files: `2b - dynamics.md`, `0d - ambient reduction scaffold.md`

Closed with named residuals. In place:

- exchange map `\mathcal C(A,B) = (\bar B,\bar A)` and `\mathcal M_{\mathrm{ex}} = -\mathrm{Im}_u(AB)` explicit; `\mathcal C` unique as compact-equivariant anti-linear exchange
- `\kappa_u \mathcal M_{\mathrm{ex}}` forced by symmetry descent (K-invariance + exchange-odd character)
- `\omega\,\mu_{U(1)} = \frac{\omega}{2}(|A|^2+|B|^2)` identified as the `U(1)` moment map term
- scalar `\gamma > 0` established by admissibility + K-injectivity + `\Gamma > 0`

Named open residuals (sharpening tasks, not blockers):

- single parent action from which `\omega`, `\kappa_u`, and `\gamma` all descend simultaneously
- bulk derivation of the orientation sign `\kappa_u > 0`

---

## Next

### X1. Topological Observable / Anomaly Bridge — Substantially Advanced

Primary files: `2h - topological.md`, `2g - open problems.md`

In place:

- `W_3 = 1` implies exactly one topologically protected massless T1 mode at the T1/T2 mass-transition surface (DIII d=3 bulk-boundary correspondence)
- observable candidates identified: (1) protected critical point, (2) quantized topological response coefficient, (3) half-integer parity anomaly shift on transition surface
- sign of `W_3` correlates with sign of `\kappa_u`: W_3 = +1 selects the constructive (κ_u > 0) branch — if confirmed, the orientation axiom follows from the DIII sign
- DIII anomaly inflow identified as the structural mechanism connecting the bulk topological term to the T1-sector boundary anomaly; bridge conjecture formulated: DIII inflow condition = matter-content anomaly cancellation (2d) in different language

Remaining calculation (specific, identified):

- compute the T₀ anomaly coefficient of the massless T1-sector boundary theory from the DIII bulk data
- compute the gauge anomaly coefficient of the T1 matter content from 2a/2d
- check whether they match (closes the bridge) or diverge (identifies an independent constraint)

### X2. Render the Explicit Phase Portrait — Done

Primary context: two-branch transport system in `(\rho,\Phi)`

Deliverable: `all/phase-portrait.html` — interactive canvas figure with:

- background shaded by transport class (Constructive / Frustrated / Inverted / Dephased)
- vector field arrows (`\dot\rho`, `\dot\Phi`) at each grid point
- persistence boundary (dashed teal): `\kappa_u\cosh(2\rho)\cos\Phi = \gamma`
- locking boundary (solid red): appears as vertical lines `\rho = \pm\rho_L` when `\omega > \kappa_u`; invisible when `\omega \leq \kappa_u`
- stable node (filled, green) and saddle (open, amber) fixed points with live labels
- sliders for `\kappa_u`, `\omega`, `\gamma`: drag `\omega` above `\kappa_u` to open the dephased band

Explanatory note is embedded in the HTML page itself.

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

1. ~~`N2` / `N3` κ_u / associator derivation~~ — conditionally closed
2. ~~`X1` topological observable / anomaly bridge~~ — substantially advanced; one calculation remaining (T₀ anomaly coefficient matching)
3. ~~`X2` phase portrait~~ — done; `all/phase-portrait.html`
4. `X3` hydrogen / Efimov bridge
5. `X4` representation-theory track

---

## One-Line Rule

Use the quaternionic slice where it helps the reduction; bracket the question of whether it is deeper physics.
