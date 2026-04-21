# Claim Ledger

This file indexes the claim level of major claims in the Spin(2,3) programme.

## Scale

| Level | Name | Meaning |
| --- | --- | --- |
| 1 | Trivial | Immediate, definitional, or too elementary to need defense. |
| 2 | Solid established | Broadly accepted background that usually does not need citation. |
| 3 | Established | Known and defensible, but specialized enough that a paper should normally cite it. |
| 4 | Being established in this paper | A claim the current paper is actively deriving, proving, or defending. |
| 5 | Plausible but future work | A reasonable extension, interpretation, or conjectural consequence not yet fully established. |
| 6 | Significant issue | A genuine weakness, unresolved problem, or point where the framework does not yet support the claim. |

## Core Mathematical And Representation Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| `SO(2,3)` is the isometry group of `AdS_4` | 2 | Solid established | Standard mathematical identification. |
| `Spin(2,3)` admits a four-component spinor representation | 2 | Solid established | Framework input. |
| Choosing conventions/time orientation gives a `J^{01}` split into two two-component sectors | 3 | Established | Known once the reduced conventions are fixed. |
| Each `J^{01}` sector carries `SU(2)` doublet structure under the maximal compact subgroup | 3 | Established | Standard representation result within the chosen setup. |
| The `J^{01}` split should be read as an effective reduced branch rather than a literal extra-time remnant | 4 | Being established in this paper | Current parent-reduction interpretation. |
| `Cl(2,3) ~= M4(C)` | 3 | Established | Standard Clifford algebra fact used by the topology track. |
| `Sigma = 2J^{01}` is the chiral grading operator | 4 | Being established in this paper | Structural identification inside the reduced representation. |

## Parent Geometry And Static Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| Choosing an octonionic direction `e7` reduces `G2` to `SU(3)` | 3 | Established | Standard octonionic stabilizer fact. |
| This `SU(3)` is physical color | 5 | Plausible but future work | Strong physical identification, not just group theory. |
| The preferred octonionic direction aligns with the zero-mass traversal direction | 5 | Plausible but future work | Central framework proposal; forcing mechanism still open. |
| `u^\perp ~= C^3` is the parent source of color, hidden planes, and generation structure | 5 | Plausible but future work | Current strongest parent-geometry convergence point. |
| The hidden complement is carried locally by a quaternionic `H` slice as complex-plane data | 4 | Being established in this paper | Useful local reduction model; not yet canonical globally. |
| `J3(O)` naturally supplies three structural slots | 3 | Established | Safe structural organizer claim. |
| `J3(C x O)` or a complexified ambient algebra may be the full ambient object | 5 | Plausible but future work | Needs bridge to observable constraints. |
| `T1 tensor (3 + 1)` matches quark/lepton doublet slots | 4 | Being established in this paper | Derived inside the representation ansatz; physical identification remains stronger. |
| Hypercharge can be built from `J^{01}` and `Q7` inside the chosen ansatz | 4 | Being established in this paper | Useful constrained construction. |
| Hypercharge uniqueness is forced | 5 | Plausible but future work | Needs sharper proof structure. |
| Exactly three physical generations are forced | 5 | Plausible but future work | Strong proof burden remains. |
| A fourth generation is physically excluded | 5 | Plausible but future work | Not publication-safe as a theorem. |
| `G2 cap Spin(2,3)` produces the phenomenologically relevant common symmetry | 5 | Plausible but future work | Explicit calculation needed. |

## Reduction And Dynamics Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| The ambient-to-observable reduction can be modeled by the current toy intertwiner | 4 | Being established in this paper | Useful local scaffold; still owes canonical parent derivation. |
| Zero-mass direct traversal is supported on `T1` | 4 | Being established in this paper | Depends on reduction/intertwiner and orientation assumptions. |
| Observables are evaluated after projection onto `T1` | 4 | Being established in this paper | Effective rule downstream of channel selection. |
| `T2` is dynamically present but not directly observable through the zero-mass channel | 4 | Being established in this paper | Follows inside the current interaction/readout picture. |
| Sector mixing can be modeled by an off-diagonal block term | 4 | Being established in this paper | Minimal model choice, not unique. |
| The leading reduced correction is second order in `m` | 4 | Being established in this paper | Derived under weak coupling. |
| The reduced Markovian generator is trace preserving in the Lindblad regime | 4 | Being established in this paper | Depends on the Markovian reduction assumptions. |
| The reduced Markovian generator is completely positive in the Lindblad regime | 4 | Being established in this paper | Same regime caveat as trace preservation. |
| The reduced equation is Lindblad type in the Markov regime | 4 | Being established in this paper | Core reduced-dynamics claim under assumptions. |
| The long-scale density satisfies advection-diffusion under closure assumptions | 4 | Being established in this paper | Reduced transport result, not a full microscopic derivation. |
| `D ~ m^2 / gamma` | 4 | Being established in this paper | Clean reduced-model scaling law. |
| T1/T2 mixing functions as the reduced mass mechanism | 4 | Being established in this paper | Strong inside the reduced model; physical completion remains open. |
| Physical mass may be encoded by sector mixing after further identification | 5 | Plausible but future work | Central interpretation, not yet a field-theoretic derivation. |
| Higgs-mediated mass generation may be what opens the `T1/T2` channel | 5 | Plausible but future work | Promising but not established. |
| The hidden-sector correlator is derived from first principles | 6 | Significant issue | Major missing dynamical input; not a live claim. |

## Two-Branch Transport Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| The transport-coherence invariant `I = A bar(B)` is the `Sp(4,R)`-compatible symplectic pairing of branch amplitudes | 4 | Being established in this paper | Structural identification in the reduced two-branch language. |
| `kappa_u` is the Spin(2,3)-compatible projection of the associator onto the transport axis | 4 | Being established in this paper | Structural associator-projection claim. |
| `kappa_u` is compact-equivariant and exchange-odd, forcing its coupling slot | 4 | Being established in this paper | Symmetry-descent result; variational origin remains open. |
| `omega` is the `U(1)` moment-map value on branch space | 4 | Being established in this paper | Reduced Hamiltonian/moment-map identification. |
| `gamma > 0` is forced by full hidden-sector coupling under `Gamma > 0` and injective `K` | 4 | Being established in this paper | Sign result; magnitude still needs hidden correlator derivation. |
| `kappa_u > 0` is the named orientation axiom with geometric content | 4 | Being established in this paper | Final operational sign axiom unless derived from the bulk. |
| The two-branch evolution equations are the minimal Spin(2,3)-compatible ansatz | 4 | Being established in this paper | Coupling term is symmetry-constrained; full parent action remains open. |
| Exact reduction to `(R, rho, Phi)` and effective coupling `kappa_eff = kappa_u cosh(2rho)` | 4 | Being established in this paper | Exact once the two-branch equations are adopted. |
| Four transport classes are forced by locking and persistence boundaries | 4 | Being established in this paper | Paper-local theorem imported as framework-level claim. |
| Particle-like states satisfy locking plus persistence conditions | 4 | Being established in this paper | Derived consequence of the two-branch classification. |
| The two-branch equations are derived from a first-principles octonionic variational principle | 5 | Plausible but future work | Partially constrained, but full parent action is open. |
| The two-branch amplitude picture has been derived into the Lindblad-Markov density-matrix picture | 5 | Plausible but future work | Coarse-graining bridge remains open. |

## Epistemic Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| The effective observable channel is determined by zero-mass interaction | 5 | Plausible but future work | Central epistemic proposal; still needs deeper derivation. |
| Projection and coarse-graining are distinct operations | 1 | Trivial | Conceptual hygiene statement used across the kernels. |
| The effective observable description loses full microscopic information | 4 | Being established in this paper | Safe at the reduced-description level. |
| Uncertainty-like broadening can arise from unresolved hidden-sector excursions | 5 | Plausible but future work | Grounded in reduced dynamics but stronger than a theorem. |
| Full quantum measurement theory follows from this projection rule | 6 | Significant issue | Unsupported overreach at present; not a live claim. |

## Consistency Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| Anomaly cancellation constrains completion of the matter content | 3 | Established | Standard consistency condition. |
| Coefficients in `Y = a J^{01} + b Q7` can be fixed inside the chosen ansatz | 4 | Being established in this paper | Constrained fit, not full uniqueness. |
| Reduced positivity/complete positivity holds in the Lindblad regime | 4 | Being established in this paper | Covered dynamically; consistency layer records the same regime caveat. |
| Strong uniqueness/exclusion claims must be separated from constrained fits | 1 | Trivial | Writing rule for static and paper-facing claims. |

## Topological Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| Spin(2,3) representations live in the complex tenfold-way sector before anti-unitary refinement | 3 | Established | Consequence of the Clifford algebra. |
| Massless `m = 0` limit gives class AIII before anti-unitary refinement | 4 | Being established in this paper | Uses `Sigma` as exact chiral symmetry. |
| Massive `m != 0` limit breaks `Sigma` and gives class A before anti-unitary refinement | 4 | Being established in this paper | Direct reduced topological reading. |
| Corrected anti-unitary structure gives DIII for the massless sector | 4 | Being established in this paper | Based on explicit `T0`, `C`, and `Sigma = C T0` calculation. |
| Massive limit gives class D after chiral symmetry is broken | 4 | Being established in this paper | DIII to D under mass/mixing. |
| Mass generation, chiral symmetry breaking, and topological gap opening are the same mathematical event in the reduced model | 4 | Being established in this paper | Structural identification, not yet a material realization. |
| `W3 = 1` implies one protected massless T1 mode at the transition surface | 4 | Being established in this paper | Uses DIII bulk-boundary correspondence and the proposed transition-surface reading. |
| Sign of `W3` correlates with sign of `kappa_u` | 5 | Plausible but future work | Concrete calculation pending. |
| DIII anomaly inflow cancels the boundary `T0` anomaly of the massless T1 sector | 5 | Plausible but future work | Structural bridge candidate; coefficient matching not done. |
| DIII anomaly inflow and matter-content anomaly cancellation are the same constraint | 5 | Plausible but future work | Requires explicit anomaly coefficient matching. |
| A physical material Hamiltonian realizing the Spin(2,3) topological class is known | 6 | Significant issue | Material realization remains open; not a live claim. |

## Research Track Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| Parametrized symmetric operators exhibit gap-amplified projector sensitivity | 3 | Established | General spectral mathematics in `research/spectral-transition/`. |
| Boundary-restricted projectors inherit inverse-gap sensitivity | 4 | Being established in this paper | Depends on the chosen bulk-boundary splitting. |
| Efimov scaling may be governed by a threshold SO(2,1) Casimir in the Spin(2,3) dephased sector | 5 | Plausible but future work | Lives in `research/faddeev-efimov/`; not core until proof obligations are met. |
| The Faddeev 3x3 channel matrix is the restricted Spin-derived SO(2,1) Casimir | 5 | Plausible but future work | Target theorem only after normalization and explicit `s_0` calculation. |
| The Faddeev/Casimir bridge has theorem-level status | 6 | Significant issue | The framework does not support this yet. |
| The Efimov bridge is closed at matrix level | 6 | Significant issue | Requires explicit Spin-derived operator and normalization match. |

## Interpretation And Phenomenology Guardrails

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| Chirality follows from T1/T2 sector asymmetry | 5 | Plausible but future work | Promising interpretive route; asymmetry is not yet forced. |
| Spin as branch-pair holonomy around the transport axis | 5 | Plausible but future work | Structural reading; connection to full spin-statistics story remains open. |
| Interference is branch phase between bracket completions | 5 | Plausible but future work | Non-associative phase reading; field-theoretic derivation absent. |
| Dark matter as primarily T2-sector matter | 5 | Plausible but future work | Structural idea, not a model. |
| Hydrogen bound/free threshold symmetry directly realizes the transport classification | 5 | Plausible but future work | Useful analogy; quantitative derivation absent. |
| Quaternionic local reduction data is new fundamental physics | 5 | Plausible but future work | Use the slice as a tool unless forced otherwise. |
| Stronger mixing predicts stronger reduced broadening | 5 | Plausible but future work | Plausible model-facing phenomenology, not yet experimentally controlled. |
| Hidden-sector effects produce observable deviations from standard unitary evolution | 5 | Plausible but future work | Qualitative direction only. |
| The framework currently makes sharp numerical predictions | 6 | Significant issue | Not yet true. |
| The framework is ready for a PRD-level phenomenology paper | 6 | Significant issue | Premature until phenomenology is sharper. |
| The framework already constitutes a full interpretation of quantum mechanics | 6 | Significant issue | Overreach at present. |

## Use

When a document introduces a strong claim, list it here before treating it as framework content. Use the lowest defensible level first, then lower the number only after the needed derivation, calculation, citation, or proof obligation is recorded.

Paper-local theorems may remain in paper drafts when their assumptions are stated inside the paper. They become framework-level claims only after they appear in this ledger.
