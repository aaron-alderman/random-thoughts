# Spin(2,3) Roadmap

This is the live work order for the Spin(2,3) programme. Strong bridges can be explored, but they should not steer the core until their assumptions and proof obligations are explicit.

## Current Basis

- The core programme lives in `core/` and `kernels/`.
- General mathematical tools live in `research/`.
- Draft papers live in `papers/`.
- Snapshots and overflow live in `archive/`.
- Claim status is indexed in `CLAIM_LEDGER.md`.

## Now

1. Preserve the core Spin(2,3) line.
   - Primary sources: `core/master-framework.md`, `core/spin23-compendium.md`, and the kernel files.
   - Main burden: sharpen the ambient-to-observable reduction and the reduced dynamics without letting secondary bridges inflate the claim level.

2. Advance the topological/anomaly calculation.
   - Primary sources: `kernels/topological.md`, `kernels/consistency.md`, and `kernels/open-problems.md`.
   - Current note: `kernels/diii-anomaly-bridge.md` shows that a direct 3d/4d coefficient identification is too strong as stated.
   - First bookkeeping pass: the reduced `T1` seed reproduces the even-doublet/global `SU(2)` shadow cleanly, while the color and `U(1)` parity data remain nontrivial.
   - Clarification now in place: the current `W_3` result is most safely a statement about one protected channel in the minimal reduced `Spin(2,3)` block, before color/generation factors are localized onto the boundary Hamiltonian.
   - Default corpus reading: Scenario A is the established topological statement; Scenario D is the leading bridge extension; Scenarios B/C require a new Hamiltonian-level calculation before they can be promoted.
   - Next calculation: use the Scenario A/B/C/D split in `kernels/diii-anomaly-bridge.md` to decide which extra internal sectors are actually present in the boundary Hamiltonian as spectator copies, localized protected channels, or non-topological bulk structure; then recompute the boundary parity data under that sharper rule.

3. Keep research tracks explicitly marked.
   - Spectral transition supplies general operator/projector language.
   - Faddeev/Efimov remains a quantitative test target for the threshold SO(2,1) idea.
   - Representation theory should now treat the literal `G2 cap Spin(2,3)` overlap as the compact `U(2)` sector and focus on how the full octonionic `SU(3)` stabilizer couples to the reduced `K = U(1) x SU(2)` action across the reduction map.

## Later

- Sharpen static uniqueness burdens: hypercharge, generation counting, fourth-generation exclusion.
- Strengthen the microscopic hidden-sector story: correlator, relativistic completion, and Heisenberg bridge.
- Push phenomenology only when there is a stable comparison target or falsifiable signature.

## Bracketed

- The quaternionic slice is useful local reduction data, not automatically new physics.
- The hydrogen/Efimov bridge is secondary until quantitative.
- Interpretation-heavy upgrades should remain downstream of explicit derivations.

## One-Line Rule

Keep the core spine disciplined; let research tracks explore, but make their assumptions visible.
