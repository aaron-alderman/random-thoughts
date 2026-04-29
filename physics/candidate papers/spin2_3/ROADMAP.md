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

2. Make the upstream selector the active proof target.
   - Primary sources: `kernels/upstream-selector-program.md`, `kernels/orientation-rule-upgrades.md`, `kernels/epistemics.md`, and `kernels/conditional-static-spectrum-closure.md`.
   - Current status: the static carrier line is paused at conditional one-generation closure. The remaining burden is now upstream: justify the observable/readout projector `P_obs`, justify the auxiliary low-occupancy rule, and decide whether those come from one parent mechanism or two.
   - Highest-yield route: D2 ambient selector descent. D1 bulk/readout stability remains a valid side route for the orientation sign, but D2 is the only current route that might close both the observable branch and the auxiliary rule in one parent language.
   - Next calculations:
     - identify the minimal parent selector data (`D_amb`, `P_{Pi,-}`, or equivalent);
     - prove its reduced image is the even-line observable projector;
     - test whether the same parent object also induces the auxiliary even/odd or low-occupancy split.

3. Keep research tracks explicitly marked.
   - Spectral transition supplies general operator/projector language.
   - Faddeev/Efimov remains a quantitative test target for the threshold SO(2,1) idea.
   - Representation theory should now treat the literal `G2 cap Spin(2,3)` overlap as the compact `U(2)` sector and focus on how the full octonionic `SU(3)` stabilizer couples to the reduced `K = U(1) x SU(2)` action across the reduction map.
   - The topological/anomaly branch is still live, but it is no longer the default next move. Its current safe reading remains Scenario A as established and Scenario D as bridge extension until a larger boundary Hamiltonian is specified.

## Later

- Sharpen static uniqueness burdens: hypercharge, generation counting, fourth-generation exclusion.
- Strengthen the microscopic hidden-sector story: correlator, relativistic completion, and Heisenberg bridge.
- Push phenomenology only when there is a stable comparison target or falsifiable signature.

## Bracketed

- The quaternionic slice is useful local reduction data, not automatically new physics.
- The hydrogen/Efimov bridge is secondary until quantitative.
- Interpretation-heavy upgrades should remain downstream of explicit derivations.

## One-Line Rule

Keep the core spine disciplined; push the upstream selector before reopening local carrier bookkeeping.
