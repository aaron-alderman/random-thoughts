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
| `SO(2,4)` can serve as a conformal parent arena reducing to `SO(2,3)` after fixing a spacelike normal | 3 | Established structural input | Standard conformal-group geometry; physical role in this programme remains interpretive. |
| `Spin(2,3)` admits a four-component spinor representation | 2 | Solid established | Framework input. |
| Choosing conventions/time orientation gives a `J^{01}` split into two two-component sectors | 3 | Established | Known once the reduced conventions are fixed; the names `T1/T2` are labels after orientation is chosen. |
| Each `J^{01}` sector carries `SU(2)` doublet structure under the maximal compact subgroup | 3 | Established | Standard representation result within the chosen setup. |
| The `J^{01}` split should be read as an effective reduced branch rather than a literal extra-time remnant | 4 | Being established in this paper | Current parent-reduction interpretation. |
| `Cl(2,3) ~= M4(C)` | 3 | Established | Standard Clifford algebra fact used by the topology track. |
| `Sigma = 2J^{01}` is the chiral grading operator | 4 | Being established in this paper | Structural identification inside the reduced representation. |

## Parent Geometry And Static Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| Choosing an octonionic direction `e7` reduces `G2` to `SU(3)` | 3 | Established | Standard octonionic stabilizer fact. |
| This `SU(3)` is physical color | 5 | Plausible but future work | Strong physical identification, not just group theory. |
| The preferred octonionic direction aligns with the zero-mass traversal direction | 5 | Plausible but future work | [K/D] Central framework proposal; forcing mechanism still open (alignment may be taken as pointwise-in-`u`, but any derivation of why this `u` is selected is a [D] upgrade). |
| `u^\perp ~= C^3` is the parent source of color, hidden planes, and generation structure | 5 | Plausible but future work | Current strongest parent-geometry convergence point. |
| The hidden complement is carried locally by a quaternionic `H` slice as complex-plane data | 4 | Being established in this paper | Useful local reduction model; not yet canonical globally. |
| `J3(O)` naturally supplies three structural slots | 3 | Established | Safe structural organizer claim. |
| `J3(C x O)` or a complexified ambient algebra may be the full ambient object | 5 | Plausible but future work | Needs bridge to observable constraints. |
| `T1 tensor (3 + 1)` matches quark/lepton doublet slots | 4 | Being established in this paper | Derived inside the representation ansatz; physical identification remains stronger. |
| Restricting `T1 tensor (3 + 1)` to the literal common compact overlap repackages it as `(\mathbf 1,0) \oplus (\mathbf 3,0) \oplus (\mathbf 2,-3/2) \oplus (\mathbf 2,-1/2)` | 4 | Being established in this paper | Shows explicitly that the quark/lepton slot structure lives at the `SU(3) x K` level, not in the literal overlap alone. See `kernels/t1-3plus1-branching.md`. |
| Hypercharge can be built from `J^{01}` and `Q7` inside the chosen ansatz | 4 | Being established in this paper | Useful constrained construction. |
| On the bare left-handed seed `T1 tensor (3 + 1)`, the natural `SU(3)`-invariant traceless grading gives `Y = (1/2) Q7`, so any nontrivial `J^{01}` contribution must enter only beyond that seed | 4 | Being established in this paper | Finite within the current normalization of `Q7`; this sharpens rather than closes the full hypercharge problem. See `kernels/t1-3plus1-branching.md`. |
| The naive enlargement `(T1 + T2) tensor (3 + 1)` cannot supply the right-handed weak-singlet completion and still leaves `J^{01}` invisible in hypercharge once the left-handed `T1` seed is fixed | 4 | Being established in this paper | Every state remains a weak doublet under the current `SU(3) x K` reading, and matching the left-handed seed still forces `a = 0`, `b = 1/2`. See `kernels/right-handed-completion-screening.md`. |
| Adding one extra weak doublet factor is enough to create right-handed-style weak singlets, and on that minimal singlet candidate the standard one-generation singlet charges are reproduced by `Y = J^{01} + (1/2)Q7` up to the global orientation flip | 4 | Being established in this paper | This is the first place where `J^{01}` becomes genuinely useful in the hypercharge fit. See `kernels/minimal-right-handed-singlet-candidate.md`. |
| No single global coefficient pair `(a,b)` yet fits both the naive bare left-handed seed and the minimal right-handed singlet candidate inside the current `Y = a J^{01} + b Q7` ansatz | 4 | Being established in this paper | Left-handed bare seed wants `a=0`, `b=1/2`; minimal singlet candidate wants `|a|=1`, `b=1/2`. This localizes the next obstruction to the unified embedding problem. |
| Even the smallest natural unified carrier `(T1 + T2) tensor (1 + S_aux) tensor (3 + 1)` fails for one global `Y = a J^{01} + b Q7` when `S_aux` is neutral under `J^{01}` and `Q7` | 4 | Being established in this paper | The carrier contains both doublet and singlet slots, but the left-handed fit still forces `a=0` while the right-handed fit forces `|a|=1`. See `kernels/unified-carrier-hypercharge-test.md`. |
| On the same unified carrier, the minimal three-term enlargement `Y = J^{01} + (1/2)Q7 + (1/2)P_aux,0` reproduces the standard one-generation left-handed and right-handed charges exactly on a selected slot assignment in the current orientation | 4 | Being established in this paper | `P_aux,0` is the projector onto the trivial summand of `1 + S_aux`. This removes the smallest unified-carrier no-go algebraically at the slot level, though the projector still needs geometric justification and the full carrier spectrum remains open. See `kernels/unified-carrier-projector-fix.md`. |
| The same even auxiliary line still carries an unwanted complementary `T2` weak-doublet sector with charges `(\mathbf 3,\mathbf 2)_{7/6} \oplus (\mathbf 1,\mathbf 2)_{1/2}` | 4 | Being established in this paper | This sharpens the projector/vacuum repair into a selected-slot fit rather than a finished spectrum: a further branch-selection, quotient, or decoupling mechanism is required. See `kernels/even-line-exotic-branch-obstruction.md`. |
| If the auxiliary block is the reducible `SU(2)` module `1 + 2`, then `P_aux,0` is the Casimir-zero projector `1 - (4/3)C_aux` | 4 | Being established in this paper | This rewrites the projector repair in basis-independent representation-theoretic language and narrows the burden to deriving the auxiliary reducible block itself. See `kernels/auxiliary-projector-casimir-rewrite.md`. |
| The current quaternionic slice `H(u,v)` does not itself realize the auxiliary reducible complex `SU(2)` module `1 + 2` under its natural visible action; it gives the irreducible complex doublet, while the scalar-plus-triplet split belongs to a different real adjoint action | 4 | Being established in this paper | This is a useful negative screen: the projector/Casimir repair is not yet derived from the existing quaternionic carrier alone. See `kernels/quaternionic-auxiliary-block-screening.md`. |
| A standard fermionic completion of the existing quaternionic doublet supplies a concrete candidate auxiliary block `Lambda^0 V + Lambda^1 V ~= 1 + 2`, with the fitted projector re-read as the vacuum projector | 5 | Plausible but future work | This is the best current positive candidate after the negative screen on bare `H(u,v)`, but it still needs a principled rule removing the complementary `T2` vacuum branch and a reason for the low-occupancy truncation or the fate of the top wedge singlet `Lambda^2 V ~= 1`. See `kernels/auxiliary-vacuum-doublet-candidate.md`. |
| The first explicit operator-level candidate for the physical static space is the correlated subcarrier cut out by `P_phys = P_{T1} P_aux,0 + P_{odd,0} P_aux,1`, which keeps the `T1` even line and the odd weak-singlet channel | 4 | Being established in this paper | This is the first candidate that removes both the complementary even-branch doublets and the odd weak-triplet sectors at the representation level, though its physical origin is still open. See `kernels/minimal-physical-subcarrier-candidate.md`. |
| The same physical-subcarrier projector can be rewritten structurally as observable-branch selection on the auxiliary even line plus minimal total weak-spin selection on the auxiliary odd line | 4 | Being established in this paper | This tightens the carrier proposal into a candidate superselection rule and aligns it with the existing orientation/readout programme and Casimir language. See `kernels/branch-casimir-superselection-candidate.md`. |
| The odd-sector selector in that superselection rule is exactly the antisymmetric `SU(2)`-invariant `epsilon` channel, equivalently the projector `(1/2)(1-tau) = 1 - (1/2) C_tot` on `2 tensor 2` | 4 | Being established in this paper | This makes the odd half of the superselection rule essentially canonical at the representation-theory level and localizes the harder ambiguity to the even observable branch. See `kernels/odd-sector-epsilon-channel.md`. |
| The even-sector selector in that superselection rule is exactly the reduced observable/readout-sector projector already built into the ambient scaffold, i.e. `P_obs = P_T1` after orientation is fixed | 4 | Being established in this paper | This means the even half is not a new hypercharge-specific branch rule; the remaining burden is to derive or justify the ambient/readout selector itself. See `kernels/even-sector-observable-projector-descent.md`. |
| Conditional on the current observable-branch rule and auxiliary-sector rule, the reduced static spectrum on `P_phys` reproduces exactly the standard one-generation charge pattern | 4 | Being established in this paper | This packages the current static line into one explicit conditional proposition and localizes the remaining burden to the upstream selector inputs rather than the carrier algebra itself. See `kernels/conditional-static-spectrum-closure.md`. |
| After the current carrier cleanup, the remaining one-generation static burden is primarily upstream selector justification rather than further local carrier fitting | 4 | Being established in this paper | The main open inputs are now the observable/readout selector on the even line and the auxiliary low-occupancy rule; nearby local carrier variants are secondary unless they test those inputs directly. See `kernels/upstream-selector-program.md`. |
| The full fermionic completion `Lambda^bullet V ~= 1 + 2 + 1` is not by itself a clean replacement for the low-occupancy auxiliary block in the current hypercharge fit, because the top wedge produces extra weak doublets carrying right-handed-style hypercharge values on the wrong `SU(2)` type | 4 | Being established in this paper | This sharpens the positive candidate into a real truncation/identification problem rather than a loose choice. See `kernels/full-fock-auxiliary-obstruction.md`. |
| Hypercharge uniqueness is forced | 5 | Plausible but future work | Needs sharper proof structure. |
| Exactly three physical generations are forced | 5 | Plausible but future work | Strong proof burden remains. |
| A fourth generation is physically excluded | 5 | Plausible but future work | Not publication-safe as a theorem. |
| Under the current compact-level bridge assumptions, `G2 cap Spin(2,3)` is the compact overlap `K = U(1) x SU(2)` in repo convention, equivalently `U(2)` up to common center | 4 | Being established in this paper | Follows because the intersection is compact, contains the reduced maximal compact subgroup `K`, and `K` is maximal compact in `Spin(2,3)`. See `kernels/g2-spin23-intersection.md`. |
| The useful representation structure must be read from the pair `Stab_{G2}(u)=SU(3)` and `K`, not from the literal intersection alone | 4 | Being established in this paper | The literal overlap only sees the compact `U(2)` restriction of the octonionic carrier; it does not itself contain an independent `SU(3) x SU(2) x U(1)`. |

## Reduction And Dynamics Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| The ambient-to-observable reduction can be modeled by the current toy intertwiner | 4 | Being established in this paper | Useful local scaffold; still owes canonical parent derivation. |
| The observable projector may be induced by an ambient scale/readout flow above the reduced `Spin(2,3)` slice | 5 | Plausible but future work | [K/D] New sharper selector target; would make `T1` a reduced label rather than an intrinsic preference (becomes [D] only if the programme claims to derive this flow/selector dynamically). |
| A single upstream selector principle may be able to induce both the even observable projector and the auxiliary-sector rule used by the current static conditional closure | 5 | Plausible but future work | This is now the main synthesis target, especially along the D2 ambient-selector route; if it fails, the repo should separate the observable projector from the auxiliary rule as distinct principles. See `kernels/upstream-selector-program.md`. |
| Zero-mass direct traversal is supported on the sector named `T1` | 4 | Being established in this paper | [K/D] Depends on reduction/intertwiner and orientation assumptions; `T1` is the label for the sector selected by the forward readout/scale-flow orientation (pointwise support/readout rule is [K/D]; forcing it from bulk is [D]). |
| Observables are evaluated after projection onto the sector named `T1` | 4 | Being established in this paper | [K/D] Effective rule downstream of channel selection; invariant content should be the induced observable projector, not the bare label. |
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
| `kappa_u > 0` is the orientation rule (operational axiom) with geometric content | 4 | Being established in this paper | [K/D] Final operational sign rule unless derived from the bulk (deriving the sign is a [D] upgrade; using it as a named readout orientation rule is [K/D]). |
| Under the conjugate-sum readout assumption `Psi_rd = A + bar(B)`, constructive persistent readout implies `kappa_u > 0` | 4 | Being established in this paper | [D1] Conditional algebraic closure: once the readout functional is fixed, the sign implication follows immediately from `Re_u(AB)|_* = R^2 gamma / kappa_u`. See `kernels/orientation-d1-bulk-stability.md`. |
| The physical readout channel is the conjugate-sum `Psi_rd = A + bar(B)` aligned with `u` (or an equivalent sign-sensitive observable) | 5 | Plausible but future work | This is now the remaining D1 burden. If justified, the conditional D1 implication upgrades to a physical sign-selection argument. |
| The two-branch evolution equations are the minimal Spin(2,3)-compatible ansatz | 4 | Being established in this paper | Coupling term is symmetry-constrained; full parent action remains open. |
| Exact reduction to `(R, rho, Phi)` and effective coupling `kappa_eff = kappa_u cosh(2rho)` | 4 | Being established in this paper | Exact once the two-branch equations are adopted. |
| Four transport classes are forced by locking and persistence boundaries | 4 | Being established in this paper | Paper-local theorem imported as framework-level claim. |
| Particle-like states satisfy locking plus persistence conditions | 4 | Being established in this paper | Derived consequence of the two-branch classification. |
| The two-branch equations are derived from a first-principles octonionic variational principle | 5 | Plausible but future work | [D] Partially constrained, but full parent action is open (this is a dynamical-upgrade claim, not pointwise-in-`u`). |
| The two-branch amplitude picture has been derived into the Lindblad-Markov density-matrix picture | 5 | Plausible but future work | Coarse-graining bridge remains open. |

## Epistemic Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| The effective observable channel is determined by zero-mass interaction | 5 | Plausible but future work | [K/D] Central epistemic proposal; can be adopted as a pointwise-in-`u` readout rule, but upgrading to "dynamically forced" is [D]. |
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
| `W3 = 1` implies one protected massless T1 channel in the minimal reduced Spin(2,3) block at the transition surface | 4 | Being established in this paper | Uses DIII bulk-boundary correspondence on the bare four-component block; extra color/generation multiplicities are not yet included. |
| Sign of `W3` tracks sign of `kappa_u` under the common global orientation reversal once the reduced orientation dictionary is fixed | 4 | Being established in this paper | Closed at the convention/equivariance level; this does not yet derive which orientation is physically selected. See `kernels/w3-kappa-sign-correlation.md`. |
| DIII anomaly inflow cancels the boundary `T0` anomaly of the massless T1 sector | 5 | Plausible but future work | Structural bridge candidate; coefficient matching not done. |
| DIII inflow may encode a parity/global shadow of the matter-content anomaly constraints after reduction to the T1 transition surface | 5 | Plausible but future work | Stronger literal-identity wording is too strong; the live task is the reduced boundary-spectrum comparison in `kernels/diii-anomaly-bridge.md`. |
| A physical material Hamiltonian realizing the Spin(2,3) topological class is known | 6 | Significant issue | Material realization remains open; not a live claim. |

## Research Track Claims

| Claim | Level | Name | Notes |
| --- | --- | --- | --- |
| Parametrized symmetric operators exhibit gap-amplified projector sensitivity | 3 | Established | General spectral mathematics in `research/spectral-transition/`. |
| Boundary-restricted projectors inherit inverse-gap sensitivity | 4 | Being established in this paper | Depends on the chosen bulk-boundary splitting. |
| Efimov scaling may be governed by a threshold SO(2,1) Casimir in the Spin(2,3) dephased sector | 5 | Plausible but future work | [K/D] Lives in `research/faddeev-efimov/`; not core until proof obligations are met (does not require `u` to run, but a strong "selector flow = RG flow" identification would be [D]). |
| The Faddeev 3x3 channel matrix is the restricted Spin-derived SO(2,1) Casimir | 5 | Plausible but future work | [K/D] Target theorem only after normalization and explicit `s_0` calculation. |
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

### Bracketed assumptions

The status of the preferred octonionic selector direction `u` is intentionally bracketed (kinematic vs dynamical). See `kernels/u-selector-bracketing.md` for the fork map and "impossibility tests" that would rule one bracket out in a given realization.
