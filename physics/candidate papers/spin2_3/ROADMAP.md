# Spin(2,3) Roadmap

This is the live work order for the Spin(2,3) programme after the recovery reorganization. It is intentionally conservative: strong bridges can be explored, but they do not steer the core until their proof obligations are met.

## Current Basis

- The core programme lives in `core/` and `kernels/`.
- General mathematical tools live in `research/`.
- Draft papers live in `papers/`.
- Snapshots and overflow live in `archive/`.
- Claim status is governed by `CLAIM_LEDGER.md`.

## Now

1. Stabilize the reorganized corpus.
   - Keep root navigation current.
   - Keep internal links pointed at the new directory structure.
   - Keep strong claims routed through the claim ledger before they enter papers.

2. Preserve the core Spin(2,3) line.
   - Primary sources: `core/master-framework.md`, `core/spin23-compendium.md`, and the kernel files.
   - Main burden: sharpen the ambient-to-observable reduction and the reduced dynamics without letting secondary bridges inflate the claim level.

3. Maintain the topological/anomaly track as the next mature calculation.
   - Primary sources: `kernels/topological.md`, `kernels/consistency.md`, and `kernels/open-problems.md`.
   - Next calculation: compare the DIII boundary anomaly data with the matter-content anomaly constraints.

## Research Tracks

### Spectral Transition

Home: `research/spectral-transition/`

Use this as a general mathematical toolkit for parametrized symmetric operators, spectral gaps, projectors, transition geometry, and boundary observables. It can support the main programme only through explicit interface notes, not by implication.

### Faddeev / Efimov Bridge

Home: `research/faddeev-efimov/`

This is a conjectural bridge track. The working rule is:

> test the bridge; do not let it steer the core.

The bridge may feed back into the core only after the proof obligations in `research/faddeev-efimov/proof-obligations.md` are completed or partially completed with stated limits. Until then, Efimov scaling remains an open conjectural application of the Spin(2,3) threshold story.

### Representation Theory

Primary context: `Spin(2,3) ~= Sp(4,R)`.

Keep this track focused on classifying relevant irreps, transport classes, and possible `G_2 cap Spin(2,3)` structure. It becomes more valuable once the core reduction story is cleaner.

## Later

- Sharpen static uniqueness burdens: hypercharge, generation counting, fourth-generation exclusion.
- Strengthen the microscopic hidden-sector story: correlator, relativistic completion, and Heisenberg bridge.
- Push phenomenology only when there is a stable comparison target or falsifiable signature.

## Bracketed

- The quaternionic slice is useful local reduction data, not automatically new physics.
- The hydrogen/Efimov bridge is interesting but secondary until quantitative.
- Interpretation-heavy upgrades should remain downstream of the proof ledger.

## One-Line Rule

Keep the core spine disciplined; let research tracks explore, but make them earn their way back into the framework.
