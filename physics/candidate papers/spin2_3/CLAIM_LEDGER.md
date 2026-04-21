# Claim Ledger

This file indexes the current status of major claims in the Spin(2,3) programme.

Allowed statuses:

- `established`: mathematical fact, direct calculation, or stable repo result.
- `conditional`: valid under explicitly named assumptions or reduction regimes.
- `conjecture`: plausible research target with proof obligations.
- `speculative`: interpretive or exploratory direction.
- `retired`: no longer used as a live claim.

## Core Mathematical And Representation Claims

| Claim | Status | Notes |
| --- | --- | --- |
| `SO(2,3)` is the isometry group of `AdS_4` | established | Standard mathematical identification. |
| `Spin(2,3)` admits a four-component spinor representation | established | Framework input. |
| Choosing conventions/time orientation gives a `J^{01}` split into two two-component sectors | conditional | Clean after the reduced conventions are fixed. |
| Each `J^{01}` sector carries `SU(2)` doublet structure under the maximal compact subgroup | established | Standard representation result within the chosen setup. |
| The `J^{01}` split should be read as an effective reduced branch rather than a literal extra-time remnant | conditional | Current parent-reduction interpretation. |
| `Cl(2,3) ~= M4(C)` | established | Standard Clifford algebra fact used by the topology track. |
| `Sigma = 2J^{01}` is the chiral grading operator | conditional | Structural identification inside the reduced representation. |

## Parent Geometry And Static Claims

| Claim | Status | Notes |
| --- | --- | --- |
| Choosing an octonionic direction `e7` reduces `G2` to `SU(3)` | established | Standard octonionic stabilizer fact. |
| This `SU(3)` is physical color | conjecture | Strong physical identification, not just group theory. |
| The preferred octonionic direction aligns with the zero-mass traversal direction | conjecture | Central framework proposal; forcing mechanism still open. |
| `u^\perp ~= C^3` is the parent source of color, hidden planes, and generation structure | conjecture | Current strongest parent-geometry convergence point. |
| The hidden complement is carried locally by a quaternionic `H` slice as complex-plane data | conditional | Useful local reduction model; not yet canonical globally. |
| `J3(O)` naturally supplies three structural slots | established | Safe structural organizer claim. |
| `J3(C x O)` or a complexified ambient algebra may be the full ambient object | conjecture | Needs bridge to observable constraints. |
| `T1 tensor (3 + 1)` matches quark/lepton doublet slots | conditional | Derived inside the representation ansatz; physical identification remains stronger. |
| Hypercharge can be built from `J^{01}` and `Q7` inside the chosen ansatz | conditional | Useful constrained construction. |
| Hypercharge uniqueness is forced | conjecture | Needs sharper proof structure. |
| Exactly three physical generations are forced | conjecture | Strong proof burden remains. |
| A fourth generation is physically excluded | conjecture | Not publication-safe as a theorem. |
| `G2 cap Spin(2,3)` produces the phenomenologically relevant common symmetry | conjecture | Explicit calculation needed. |

## Reduction And Dynamics Claims

| Claim | Status | Notes |
| --- | --- | --- |
| The ambient-to-observable reduction can be modeled by the current toy intertwiner | conditional | Useful local scaffold; still owes canonical parent derivation. |
| Zero-mass direct traversal is supported on `T1` | conditional | Depends on reduction/intertwiner and orientation assumptions. |
| Observables are evaluated after projection onto `T1` | conditional | Effective rule downstream of channel selection. |
| `T2` is dynamically present but not directly observable through the zero-mass channel | conditional | Follows inside the current interaction/readout picture. |
| Sector mixing can be modeled by an off-diagonal block term | conditional | Minimal model choice, not unique. |
| The leading reduced correction is second order in `m` | conditional | Derived under weak coupling. |
| The reduced Markovian generator is trace preserving in the Lindblad regime | conditional | Depends on the Markovian reduction assumptions. |
| The reduced Markovian generator is completely positive in the Lindblad regime | conditional | Same regime caveat as trace preservation. |
| The reduced equation is Lindblad type in the Markov regime | conditional | Core reduced-dynamics claim under assumptions. |
| The long-scale density satisfies advection-diffusion under closure assumptions | conditional | Reduced transport result, not a full microscopic derivation. |
| `D ~ m^2 / gamma` | conditional | Clean reduced-model scaling law. |
| T1/T2 mixing functions as the reduced mass mechanism | conditional | Strong inside the reduced model; physical completion remains open. |
| Physical mass may be encoded by sector mixing after further identification | speculative | Central interpretation, not yet a field-theoretic derivation. |
| Higgs-mediated mass generation may be what opens the `T1/T2` channel | speculative | Promising but not established. |
| The hidden-sector correlator is derived from first principles | retired | Major missing dynamical input, not a live claim. |

## Two-Branch Transport Claims

| Claim | Status | Notes |
| --- | --- | --- |
| The transport-coherence invariant `I = A bar(B)` is the `Sp(4,R)`-compatible symplectic pairing of branch amplitudes | conditional | Structural identification in the reduced two-branch language. |
| `kappa_u` is the Spin(2,3)-compatible projection of the associator onto the transport axis | conditional | Structural associator-projection claim. |
| `kappa_u` is compact-equivariant and exchange-odd, forcing its coupling slot | conditional | Symmetry-descent result; variational origin remains open. |
| `omega` is the `U(1)` moment-map value on branch space | conditional | Reduced Hamiltonian/moment-map identification. |
| `gamma > 0` is conditionally forced by full hidden-sector coupling under `Gamma > 0` and injective `K` | conditional | Sign result; magnitude still needs hidden correlator derivation. |
| `kappa_u > 0` is the named orientation axiom with geometric content | conditional | Final operational sign axiom unless derived from the bulk. |
| The two-branch evolution equations are the minimal Spin(2,3)-compatible ansatz | conditional | Coupling term is symmetry-constrained; full parent action remains open. |
| Exact reduction to `(R, rho, Phi)` and effective coupling `kappa_eff = kappa_u cosh(2rho)` | conditional | Exact once the two-branch equations are adopted. |
| Four transport classes are forced by locking and persistence boundaries | conditional | Paper-local theorem imported as framework-level conditional claim. |
| Particle-like states satisfy locking plus persistence conditions | conditional | Derived consequence of the two-branch classification. |
| The two-branch equations are derived from a first-principles octonionic variational principle | conjecture | Partially constrained, but full parent action is open. |
| The two-branch amplitude picture has been derived into the Lindblad-Markov density-matrix picture | conjecture | Coarse-graining bridge remains open. |

## Epistemic Claims

| Claim | Status | Notes |
| --- | --- | --- |
| The effective observable channel is determined by zero-mass interaction | conjecture | Central epistemic proposal; still needs deeper derivation. |
| Projection and coarse-graining are distinct operations | established | Conceptual hygiene statement used across the kernels. |
| The effective observable description loses full microscopic information | conditional | Safe at the reduced-description level. |
| Uncertainty-like broadening can arise from unresolved hidden-sector excursions | speculative | Grounded in reduced dynamics but stronger than a theorem. |
| Full quantum measurement theory follows from this projection rule | retired | Unsupported overreach at present. |

## Consistency Claims

| Claim | Status | Notes |
| --- | --- | --- |
| Anomaly cancellation constrains completion of the matter content | established | Standard consistency condition. |
| Coefficients in `Y = a J^{01} + b Q7` can be fixed inside the chosen ansatz | conditional | Constrained fit, not full uniqueness. |
| Reduced positivity/complete positivity holds in the Lindblad regime | conditional | Covered dynamically; consistency layer records the same regime caveat. |
| Strong uniqueness/exclusion claims must be separated from constrained fits | established | Writing rule for static and paper-facing claims. |

## Topological Claims

| Claim | Status | Notes |
| --- | --- | --- |
| Spin(2,3) representations live in the complex tenfold-way sector before anti-unitary refinement | established | Consequence of the Clifford algebra. |
| Massless `m = 0` limit gives class AIII before anti-unitary refinement | conditional | Uses `Sigma` as exact chiral symmetry. |
| Massive `m != 0` limit breaks `Sigma` and gives class A before anti-unitary refinement | conditional | Direct reduced topological reading. |
| Corrected anti-unitary structure gives DIII for the massless sector | conditional | Based on explicit `T0`, `C`, and `Sigma = C T0` calculation. |
| Massive limit gives class D after chiral symmetry is broken | conditional | DIII to D under mass/mixing. |
| Mass generation, chiral symmetry breaking, and topological gap opening are the same mathematical event in the reduced model | conditional | Structural identification, not yet a material realization. |
| `W3 = 1` implies one protected massless T1 mode at the transition surface | conditional | Uses DIII bulk-boundary correspondence and the proposed transition-surface reading. |
| Sign of `W3` correlates with sign of `kappa_u` | conjecture | Concrete calculation pending. |
| DIII anomaly inflow cancels the boundary `T0` anomaly of the massless T1 sector | conjecture | Structural bridge candidate; coefficient matching not done. |
| DIII anomaly inflow and matter-content anomaly cancellation are the same constraint | conjecture | Requires explicit anomaly coefficient matching. |
| A physical material Hamiltonian realizing the Spin(2,3) topological class is known | retired | Material realization remains open. |

## Research Track Claims

| Claim | Status | Notes |
| --- | --- | --- |
| Parametrized symmetric operators exhibit gap-amplified projector sensitivity | established | General spectral mathematics in `research/spectral-transition/`. |
| Boundary-restricted projectors inherit inverse-gap sensitivity | conditional | Depends on the chosen bulk-boundary splitting. |
| Efimov scaling may be governed by a threshold SO(2,1) Casimir in the Spin(2,3) dephased sector | conjecture | Lives in `research/faddeev-efimov/`; not core until proof obligations are met. |
| The Faddeev 3x3 channel matrix is the restricted Spin-derived SO(2,1) Casimir | conjecture | Target theorem only after normalization and explicit `s_0` calculation. |
| The Faddeev/Casimir bridge has theorem-level status | retired | Replaced by the conjectural bridge track and proof-obligation gate. |
| The Efimov bridge is closed at matrix level | retired | Requires explicit Spin-derived operator and normalization match. |

## Interpretation And Phenomenology Guardrails

| Claim | Status | Notes |
| --- | --- | --- |
| Chirality follows from T1/T2 sector asymmetry | speculative | Promising interpretive route; asymmetry is not yet forced. |
| Spin as branch-pair holonomy around the transport axis | speculative | Structural reading; connection to full spin-statistics story remains open. |
| Interference is branch phase between bracket completions | speculative | Non-associative phase reading; field-theoretic derivation absent. |
| Dark matter as primarily T2-sector matter | speculative | Structural idea, not a model. |
| Hydrogen bound/free threshold symmetry directly realizes the transport classification | speculative | Useful analogy; quantitative derivation absent. |
| Quaternionic local reduction data is new fundamental physics | speculative | Use the slice as a tool unless forced otherwise. |
| Stronger mixing predicts stronger reduced broadening | speculative | Plausible model-facing phenomenology, not yet experimentally controlled. |
| Hidden-sector effects produce observable deviations from standard unitary evolution | speculative | Qualitative direction only. |
| The framework currently makes sharp numerical predictions | retired | Not yet true. |
| The framework is ready for a PRD-level phenomenology paper | retired | Premature until phenomenology is sharper. |
| The framework already constitutes a full interpretation of quantum mechanics | retired | Overreach at present. |

## Use

When a document introduces a strong claim, list it here before treating it as framework content. Use the lowest defensible status first, then strengthen the status only after the needed derivation, calculation, or proof obligation is recorded.

Paper-local theorems may remain in paper drafts when their assumptions are stated inside the paper. They become framework-level claims only after they appear in this ledger.
