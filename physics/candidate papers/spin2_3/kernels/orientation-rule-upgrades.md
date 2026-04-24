# Upgrading The Orientation Rule (`\kappa_u > 0`) From Operational To Derived

The programme currently uses the condition `\kappa_u > 0` as an **operational rule** to fix the physical forward/readout orientation (the remaining global `\mathbf Z_2`). This is compatible with both brackets for the selector `u` (kinematic or dynamical).

Separately, the programme keeps a **derivation target**: explain why the physical readout must land on the constructive/persistent branch, i.e. why the forward/readout choice should coincide with `\kappa_u > 0`.

This note lists the clean upgrade routes and what they would have to assume.

See also:

- `kernels/dynamics.md` (orientation rule and its geometric content)
- `kernels/epistemics.md` (operational readout rule and the remaining burden)
- `kernels/discrete-symmetries.md` (disambiguates the different `Z2` flips)
- `kernels/u-selector-bracketing.md` (the [K]/[D] fork map and no-go statements)
- `kernels/orientation-d1-bulk-stability.md` (a focused D1 attempt and its minimal gate)

## Route D1: Bulk Stability / Attractor Principle

Assume there exists a bulk functional (energy, Lyapunov, entropy production, or equivalent) whose extremum/monotonicity selects the long-lived readout channel.

Target form:

- show that for the readout-relevant family of bulk states, the long-time attractor/fixed point must satisfy `Re_u(AB)|_* > 0`
- conclude `\kappa_u > 0` for the physically realized direct readout branch

What this would buy:

- turns `\kappa_u > 0` into a bulk stability consequence rather than a named convention

What it must overcome:

- symmetry and linearized branch-space stability do not fix the sign (see `u-selector-bracketing.md`)

One concrete candidate for the missing sign-sensitive stability functional is the conjugate-sum readout intensity `|A+\bar B|^2`, whose interference term is `2 Re_u(AB)`; see `kernels/orientation-d1-bulk-stability.md`.

If EM/readout coupling is taken to be axis-aligned (defined only after `u` is selected, e.g. gauge-fix `u=e1`) and to sample the conjugate-sum channel, then the D1 gate reduces to `Re_u(AB)|_*>0` and the orientation rule `\kappa_u>0` follows immediately from the fixed-point identity in `kernels/dynamics.md`.

## Route D2: Ambient Scale/Readout Selector Descent

Assume there is an ambient selector (scale-flow / readout generator) upstream of the reduced slice (for example in `SO(2,4)`), whose induced reduced image fixes the forward/readout orientation.

Target form:

- identify `D_amb` (or a flow field)
- show that its induced orientation agrees with the constructive/persistent branch convention
- read `\kappa_u > 0` as the sign alignment between the ambient forward arrow and the odd bulk scalar

What this would buy:

- makes the forward/readout arrow an induced geometric object rather than an epistemic postulate

What it must specify:

- what data selects `D_amb` in the first place, and why it is physical rather than gauge

## Route D3: Observer Coupling / Readout Arrow As A Physical Input

Assume that the observer/readout mechanism is itself a physical coupling that breaks the `Z2` degeneracy (for example, a semigroup arrow `t>=0` plus a coupling that requires persistence rather than inversion).

Target form:

- model the readout coupling so that the only stable, consistently readable branch is the constructive/persistent one
- show that this physical readout coupling forces `\kappa_u > 0` in the phase-normalized gauge

What this would buy:

- admits that "observability" is not purely kinematic, while still turning the rule into a consequence of the readout mechanism

What it concedes:

- the sign is not fixed by the bare transport algebra; it is fixed at the interface of dynamics and epistemics

## Minimal Writing Rule

Until one of D1–D3 is completed, statements should be written in one of two explicit forms:

- **Operational rule:** "we adopt `\kappa_u > 0` to fix the forward/readout orientation."
- **Derivation target:** "we aim to derive `\kappa_u > 0` from {bulk stability / ambient selector / readout coupling}."
