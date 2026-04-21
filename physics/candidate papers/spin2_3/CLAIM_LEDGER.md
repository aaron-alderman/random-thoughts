# Claim Ledger

This file is the global claim-control surface for the Spin(2,3) programme.

Allowed statuses:

- `established`: mathematical fact, direct calculation, or stable repo result.
- `conditional`: valid under explicitly named assumptions or reduction regimes.
- `conjecture`: plausible research target with proof obligations.
- `speculative`: interpretive or exploratory direction.
- `retired`: no longer used as a live claim.

## Core Claims

| Claim | Status | Notes |
| --- | --- | --- |
| `SO(2,3)` is the isometry group of `AdS_4` | established | Standard mathematical identification. |
| Spin(2,3) admits a four-component spinor representation with a `T1 + T2` split under `J^{01}` | established | Used as framework input. |
| The ambient-to-observable reduction can be modeled by the current toy intertwiner | conditional | Useful local scaffold; still owes canonical parent derivation. |
| Zero-mass direct traversal is supported on `T1` | conditional | Depends on the reduction/intertwiner and orientation assumptions. |
| T1/T2 mixing functions as the reduced mass mechanism | conditional | Strong inside the reduced model; physical completion remains open. |
| DIII/topological structure organizes the massless T1 sector | conditional | Substantially developed, still subject to coefficient matching and realization questions. |

## Open Strong Claims

| Claim | Status | Notes |
| --- | --- | --- |
| Hypercharge uniqueness is forced | conjecture | Needs sharper proof structure. |
| Exactly three generations are forced | conjecture | Strong proof burden remains. |
| A fourth generation is physically excluded | conjecture | Not publication-safe as a theorem. |
| `G_2 cap Spin(2,3)` produces the phenomenologically relevant common symmetry | conjecture | Explicit calculation needed. |

## Research Track Claims

| Claim | Status | Notes |
| --- | --- | --- |
| Parametrized symmetric operators exhibit gap-amplified projector sensitivity | established | General spectral mathematics in `research/spectral-transition/`. |
| Boundary-restricted projectors inherit inverse-gap sensitivity | conditional | Depends on the chosen bulk-boundary splitting. |
| Efimov scaling may be governed by a threshold SO(2,1) Casimir in the Spin(2,3) dephased sector | conjecture | Lives in `research/faddeev-efimov/`; not core until proof obligations are met. |
| The Faddeev 3x3 channel matrix is the restricted Spin-derived SO(2,1) Casimir | conjecture | Target theorem only after normalization and `s_0` recovery are explicit. |

## Speculative Directions

| Claim | Status | Notes |
| --- | --- | --- |
| Dark matter as primarily T2-sector matter | speculative | Structural idea, not a model. |
| Hydrogen bound/free threshold symmetry directly realizes the transport classification | speculative | Useful analogy; quantitative derivation absent. |
| Quaternionic local reduction data is new fundamental physics | speculative | Use the slice as a tool unless forced otherwise. |

## Retired Or Demoted

| Claim | Status | Notes |
| --- | --- | --- |
| The Faddeev/Casimir bridge has theorem-level status | retired | Replaced by the conjectural bridge track and proof-obligation gate. |
| The Efimov bridge is closed at matrix level | retired | Requires explicit Spin-derived operator and normalization match. |
