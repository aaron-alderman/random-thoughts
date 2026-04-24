# Bracketing The Octonionic Selector `u` (Kinematic vs Dynamical)

This note records an intentional open fork in the programme.

We do not yet know which "part of the universe" we live in with respect to the preferred octonionic direction `u` (the zero-mass traversal/readout direction). Two semantics are therefore bracketed:

- **[K] Kinematic `u`.** `u` is treated as fixed upstream structure. Local geometry is adapted to `u` and all downstream constructions are pointwise in that fixed choice.
- **[D] Dynamical `u`.** `u` is treated as a field/flow variable (possibly RG/scale-flow coupled). The preferred direction may be selected dynamically, may run, and may pass through threshold regimes.

The point of bracketing is not to avoid committing forever. It is to (i) keep both readings available, and (ii) track exactly where each reading is required so we can later identify impossibility or necessity cleanly.

## Claims That Are Pointwise In `u` (Compatible With [K] And [D])

These claims may be used without deciding whether `u` is kinematic or dynamical.

1. **Stabilizer/adaptation facts.** Given a local choice of `u`, the local remainder and stabilizer structure can be described (e.g. `G2 -> SU(3)`, `u^\perp ~= C^3`, local `H(u,v)` slices).
2. **Gauge-fixing logic.** Reduced basis choices are downstream representatives of `u`-adapted data. Axis labels `2/3/4` are not intrinsic unless upstream data breaks the `SO(3)` conjugacy.
3. **Massless observability as support/readout rule.** In the direct readout regime, the observable sector should be stated as a support/orientation principle tied to the forward/readout convention induced by `u`, not as an internal `Spin(2,3)` preference.
4. **Massive regime bookkeeping.** Once there is genuine mixing, an effective reduced symmetry such as `Spin(2,3)` can package the two-sector dynamics without claiming it is the fundamental kinematics of the massless channel.
5. **Existence of a threshold `SO(2,1)` sector.** A local `SO(2,1)` subsector can be identified as a threshold arena in the effective dynamics (useful for Efimov-class comparisons) without asserting that `u` itself runs.

## Claims That Require `u` To Be Dynamical (Or At Least Coupled To Dynamics)

The following are upgrades that cannot be asserted from pointwise-in-`u` reasoning alone.

1. **Derivation of selection.** A mechanism that derives why *this* `u` is selected (rather than taking it as background).
2. **Forced observability (Route A strength).** Any statement that the observable channel is uniquely forced by dynamics rather than postulated as a readout rule.
3. **Generic threshold crossing.** Any statement that the system naturally flows across elliptic/hyperbolic/parabolic threshold types as part of evolution, rather than being tuned into those regimes.
4. **RG/scale-flow identification.** Any statement that identifies `u` with a running scale-flow vector in a way that changes the effective sector selection.

## "Impossibility" Tests (How A Bracket Could Fail)

This section lists the kinds of checks that can, in principle, rule one bracket out in a given model realization.

1. **Gauge invariance obstruction.** If a proposed dynamical evolution of `u` depends on gauge-fixed representatives rather than invariant data, the [D] reading is inconsistent as stated.
2. **No-go from symmetry.** If the reduced theory plus couplings is strictly invariant under the full transverse `SO(3)` with no upstream symmetry breaking, then an intrinsic local axis in the reduced slice cannot be physical (any axis dependence must be upstream, pushing back toward [K] or to an explicitly dynamical symmetry-breaking field).
3. **No-go for the sign from symmetry alone.** In the current two-branch setup there is an explicit exchange-odd structure tied to `u -> -u` that swaps constructive/inverted classes (equivalently flips the sign of `\kappa_u`). Moreover, at the level of the linear Hamiltonian-Rayleigh generator on branch space, `\kappa_u` and `-\kappa_u` are related by a similarity transformation (flip the sign of `B`, i.e. `(A,B)\mapsto(A,-B)`), so the spectrum and linear stability depend only on `\kappa_u^2`. Therefore the sign choice `\kappa_u > 0` cannot be derived from symmetry or linear stability constraints alone. Any upgrade from "named orientation axiom" to a derived statement must introduce extra structure: a bulk stability principle beyond the linearized generator, a dissipation/readout arrow, or an ambient selector whose reduced image fixes the orientation.
4. **Well-posed observable rule at threshold.** If the programme insists that observability is defined by a spectral projector of an induced selector, then parabolic/null regimes require a limiting/filtration prescription. If no such prescription is available or stable, then the observable rule cannot be taken to live at that selector level.
5. **Efimov gate.** If the Efimov/Faddeev bridge is pursued quantitatively, failure to reproduce the exponent `s_0` under a fixed normalization is evidence against a strong [D]-style identification of the running selector with the threshold `SO(2,1)` Casimir (it does not rule out [K], only the strong dynamical upgrade).

## Minimal Usage Rule

When writing a claim that touches `u`:

- If it holds "given a fixed `u`", label it as pointwise-in-`u` and do not imply a selection mechanism.
- If it asserts selection, flow, or forcing, label it explicitly as requiring the [D] upgrade (or list the extra assumptions needed).
- The orientation condition `\kappa_u > 0` is allowed to appear in two roles: as an operational readout-orientation rule ([K/D]) and as a derivation target to be justified from bulk/ambient structure ([D]). Do not use it as both an input and a proven output within the same argument.
