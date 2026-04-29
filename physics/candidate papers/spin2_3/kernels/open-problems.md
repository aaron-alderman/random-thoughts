# Open Problems Kernel

## Purpose

This document is the open-problems source text for the project.

It is not a paper draft. It is the place where the framework's debts are kept explicit and organized. The goal is to say:

- what the project still owes at a structural level
- which proof burdens are still heavy
- which missing pieces block publication at different levels
- how to prioritize future work

This file should be brutally honest. It is not a weakness to have it; it is a control system.

---

## Scope

This file covers:

- unresolved static issues
- unresolved dynamical issues
- unresolved epistemic and interpretive issues
- unresolved phenomenological issues
- publication blockers

---

## Why a dedicated open-problems file matters

Ambitious frameworks usually fail in one of two ways:

1. they do not know what they still owe
2. they know, but the gaps are scattered across too many drafts and discussions

This file prevents both failures.

---

## Tiered open problems

The project's open problems naturally fall into tiers.

### Tier 1: local strengthening problems

These do not change the framework, but they would make current claims cleaner.

- sharpen the proof burden for hypercharge uniqueness
- sharpen the proof burden for generation counting
- improve the derivation of the reduced Markov regime
- cleanly separate constrained fit from true derivation everywhere

### Tier 2: domain-completion problems

These complete major kernel domains.

- a first-principles model for the hidden-sector correlator
- a fully relativistic field-theoretic completion
- direct geometric derivation of all fermion sectors
- a sharper relation between the projection rule and standard measurement language
- a disciplined ambient-to-observable reduction map
- a sharper parent-level reduction from the octonionic hidden geometry to the `Spin(2,3)` effective branch
- a formal folding map from the exploratory `Spin(3,3)` lift into the effective `Spin(2,3)` branch plus hidden quaternionic complex-plane structure

### Tier 3: synthesis problems

These are the problems that would turn the project from a coherent framework into a more complete theory program.

- CKM and PMNS structure
- mass hierarchy
- neutrino masses
- experimental predictions or bounds
- a stronger unification of static, dynamical, and epistemic claims

---

## Open problems by domain

### Static / kinematic

- how strong is the argument that `T1 \otimes (3 + 1)` genuinely yields physical matter structure rather than a compelling matching pattern?
- is the hypercharge ansatz really canonical?
- how much of the generation story is structural and how much is interpretive?
- what exactly in the large ambient space is physical structure, and what is redundancy, gauge, or filtered-out data?
- can the octonionic remainder `u^\perp \cong \mathbf{C}^3` be shown to be the primary parent geometry from which color, wandering planes, and generation structure all descend?
- can the local quaternionic carrier of the hidden complex plane be identified canonically inside the broader octonionic parent?
  This is now best read as an important bridge-cleanup problem rather than a stop-everything blocker; the local quaternionic slice can be bracketed as a non-blocking reduction device unless later results force a stronger physical interpretation.

### Dynamics

- what microscopic dynamics produces the hidden-sector correlator?
- under exactly what assumptions is the reduced semigroup form valid?
- how should the framework be made relativistic beyond the current reduced model?
- can the `2/4/6` wandering-access ladder be made dynamical rather than merely kinematical?
- how exactly does the hidden internal `2`-plane feed the reduced kernel `G_{ab}` without being re-described as literal extra time?

### Epistemics

- what induces the observable projector, and does the induced sector match the current `T1` naming convention?
- is projection fundamental or emergent?
- what is the relation to standard quantum measurement theory?
- how does the ambient-to-observable reduction act on the full space before one reaches the final visible sector?
- can a hidden antisymmetric `2`-plane induce the effective observable symplectic structure needed for Heisenberg-type relations?
- how should the framework distinguish rigorously between literal spacetime directions, internal complex-plane structure, and reduced observable sectors?

### Consistency

- which strong uniqueness claims are actually proven?
- what exactly is excluded, and in what sense?

### Interpretation

- which conceptual readings are indispensable to the framework and which are optional?
- when does interpretation begin to outrun proof?
- is toric resolution the right language for how latent hidden `SU(3)` geometry becomes explicit under higher energy?

### Phenomenology

- what quantity should be compared with experiment first?
- how can the model parameters be constrained?
- what would count as a genuine falsifiable signature?
- how much of the large ambient space can be ruled out experimentally without thereby invalidating the larger framework?
- does the hydrogen hidden-symmetry split `SO(4) / SO(3,1)` admit a controlled reduction from the transport classification, and can the near-threshold `SO(2,1)` sector recover the Efimov exponent `s_0`?

---

## Publication blockers

These are the main blockers for different kinds of papers.

### For stronger static papers

- overclaiming uniqueness or exclusion without a tighter proof chain
- failing to explain how the large ambient space reduces to the physically relevant static sector

### For stronger dynamics papers

- insufficient microscopic control of the hidden-sector assumptions
- failing to explain how the dynamical variables sit inside the ambient-to-observable reduction

### For interpretation-heavy papers

- drifting into philosophical overstatement without enough formal support

### For phenomenology papers

- lack of sharp predictions or bounds

---

## Priority ordering

If the goal is to build the framework in the most efficient order, the current priorities appear to be:

1. sharpen the parent octonionic geometry and its reduction to the effective `Spin(2,3)` branch
2. formalize the folding of the exploratory `Spin(3,3)` lift into hidden quaternionic complex-plane data
3. tighten the static and consistency proof burdens inside the reduced branch
4. define the ambient-to-observable reduction more sharply
5. strengthen the microscopic basis of the reduced dynamics, especially the hidden antisymmetric sector needed for a Heisenberg bridge
6. complete the epistemic story around projection
7. only then push toward mature phenomenology

This priority order matches the current level of the project.

---

## Open-problem ledger

| Problem | Domain | Severity | Comment |
|---|---|---|---|
| hidden-sector correlator lacks first-principles derivation | dynamics | high | major blocker for stronger dynamical claims |
| hypercharge uniqueness still needs a sharper proof structure | consistency | high | important for static papers |
| generation-counting and fourth-generation exclusion remain heavy proof burdens | statics / consistency | high | one of the biggest weak spots |
| ambient-to-observable reduction is not yet sharply defined | cross-domain | high | central missing-middle object |
| projection onto the sector named `T1` lacks a deeper justification | epistemics | medium-high | now reduced to one final issue: either justify the physical readout functional that selects the constructive/persistent branch (`Psi_rd = A + bar(B)` is the leading D1 candidate), or show that an ambient scale-flow selector induces the same observable projector. The D1 sign implication itself is conditionally closed once the conjugate-sum readout is granted; see `kernels/orientation-d1-bulk-stability.md`. |
| parent octonionic geometry has not yet been rigorously reduced to the effective `Spin(2,3)` branch | statics / cross-domain | high | now a central parent-program task |
| folded `Spin(3,3)` insight has not yet been formalized as a precise reduction map into hidden quaternionic complex-plane structure | statics / cross-domain | high | new central bridge task |
| Heisenberg-type structure is not yet derived from a hidden antisymmetric sector | dynamics / epistemics | high | requires more than diffusion |
| full field-theoretic completion is missing | dynamics / completion | high | major long-term gap |
| no sharp experimental predictions yet | phenomenology | high | blocks PRD-style work |
| interpretation can still outrun proof if not carefully disciplined | interpretation | medium | recurring writing risk |

### Two-branch transport tasks (added from octonionic transport coherence framework)

| Problem | Domain | Severity | Comment |
|---|---|---|---|
| derive the two-branch evolution equations $\dot{A} = (u\omega-\gamma)A + \kappa_u\bar{B}$ from a variational principle on the octonionic bulk | dynamics | high | [D] upgrade: the equations now admit an explicit Hamiltonian-plus-Rayleigh scaffold on the selected `u`-complex line; the remaining task is to derive its ingredients from the parent bulk: branch symplectic form, charge-flip/conjugation exchange, odd moment `\kappa_u`, and positive leakage term `\gamma` |
| express $\kappa_u$ as a genuine Sp(4,ℝ) moment map of the associator — show it is the Hamiltonian generator of branch rotations, not merely an invariant projection | dynamics / statics | medium | **substantially closed at the symmetry level**: $\kappa_u$ is $K$-invariant by $K \subset \mathrm{Stab}_{G_2}(u)$, and exchange-odd by $\mathfrak K_u: u \mapsto -u$; the uniqueness argument then forces descent as $\kappa_u \mathcal M_{\mathrm{ex}}$ (formal lemma note: `kernels/kappa_u-moment-map-lemma.md`); remaining open: variational origin of the coupling from a parent action, and orientation ($\kappa_u > 0$ criterion) |
| determine how the full octonionic `SU(3)` stabilizer and the reduced compact `K = U(1) x SU(2)` action fit together beyond their literal overlap | statics | medium | **substantially closed at the literal-intersection level**: `kernels/g2-spin23-intersection.md` shows that `G_2 cap Spin(2,3)` is only the compact `U(2)` sector (repo convention: `U(1) x SU(2)` up to common center), so the overlap does not itself contain `SU(3) x SU(2) x U(1)`; the remaining task is to organize the joint irrep data of `Stab_{G_2}(u)=SU(3)` and the reduced transport action across the reduction map |
| determine where a genuinely nontrivial `J^{01}` contribution to hypercharge first enters beyond the bare left-handed `T1 tensor (3 + 1)` seed | statics / consistency | medium | **sharpened substantially**: `kernels/t1-3plus1-branching.md` shows that with the natural `SU(3)`-invariant traceless grading `Q7 = diag(1/3,1/3,1/3,-1)`, matching the left-handed quark/lepton doublet charges gives `Y = (1/2)Q7` on the bare seed, so `J^{01}` can only become an independent hypercharge ingredient after enlarging the representation content |
| identify the smallest enlarged static carrier that can realize the right-handed singlet completion | statics / consistency | medium | **advanced one step further**: `kernels/right-handed-completion-screening.md` rules out `(T1 \oplus T2) tensor (3 \oplus 1)`, while `kernels/minimal-right-handed-singlet-candidate.md` shows that adding one extra weak doublet factor is the first algebraic repair that creates weak singlets and yields the standard right-handed charges with `Y = J^{01} + (1/2)Q7`; the remaining task is to justify the extra factor and unify it with the left-handed embedding |
| find a single unified static carrier on which one global `Y = a J^{01} + b Q7` fits both the left-handed doublet seed and the right-handed singlet sector | statics / consistency | high | **now sharper still**: `kernels/unified-carrier-hypercharge-test.md` shows that even the smallest natural unified carrier `(T1 \oplus T2) tensor (1 \oplus S_aux) tensor (3 \oplus 1)` fails if `S_aux` is neutral under `J^{01}` and `Q7`, because the left-handed fit still wants `a=0`, `b=1/2` while the right-handed fit wants `a=\pm1`, `b=1/2` |
| derive or justify the projector term `P_{\mathrm{aux},0}` in the successful three-term fit `Y = J^{01} + (1/2)Q7 + (1/2)P_{\mathrm{aux},0}` | statics / consistency | high | **narrowed further**: `kernels/unified-carrier-projector-fix.md` and `kernels/auxiliary-projector-casimir-rewrite.md` reduce the burden to explaining why the physical charge operator should see the auxiliary `j=0` sector at all; `kernels/even-line-exotic-branch-obstruction.md` shows that the repair is only a selected-slot fit unless the complementary `T2` even branch is removed; `kernels/minimal-physical-subcarrier-candidate.md` packages the current best repair as a genuine subcarrier projector; `kernels/quaternionic-auxiliary-block-screening.md` shows that this term is not already inherited from the current bare quaternionic visible carrier; `kernels/auxiliary-vacuum-doublet-candidate.md` gives the best current positive source reading; and `kernels/full-fock-auxiliary-obstruction.md` shows that the corresponding low-occupancy restriction is not optional in the present fit |
| derive or justify the auxiliary reducible `SU(2)` block `1 \oplus 2` whose Casimir-zero projector equals `P_{\mathrm{aux},0}` | statics / consistency | high | **sharpened again**: `kernels/auxiliary-projector-casimir-rewrite.md` shows that the projector term is canonically `1 - (4/3)C_aux` once such a block exists; `kernels/quaternionic-auxiliary-block-screening.md` shows that the present local slice `H(u,v)` does not itself provide that module under its natural visible action; `kernels/auxiliary-vacuum-doublet-candidate.md` identifies the low-occupancy sector `Lambda^0 V \oplus Lambda^1 V` of a fermionic completion of that doublet as the first concrete positive candidate; `kernels/minimal-physical-subcarrier-candidate.md` shows how that block would have to enter a correlated physical subspace; `kernels/even-line-exotic-branch-obstruction.md` shows that even this low-occupancy candidate still needs a rule removing the complementary `T2` even branch; and `kernels/full-fock-auxiliary-obstruction.md` shows that the full `1 \oplus 2 \oplus 1` completion adds a wrong-type top-wedge doublet sector |
| determine whether the projector/Casimir fix is canonical or whether a larger left-handed embedding / different operator-level completion is preferable | statics / consistency | medium-high | the algebraic obstruction is gone, the projector has a canonical rewrite, the bare quaternionic slice has been screened negatively as its direct source, the best current positive candidate is now an explicit correlated subcarrier rather than a raw tensor-product carrier, `kernels/branch-casimir-superselection-candidate.md` rewrites that subcarrier as observable-branch plus minimal weak-spin selection, `kernels/odd-sector-epsilon-channel.md` sharpens the odd half into the unique antisymmetric invariant scalar channel, and the larger completions fail in specific ways; the live options are therefore derivation of the remaining superselection rule from branch/orientation/dynamics, explicit parent-carrier enlargement, or a different left-handed / operator-level completion |
| render the explicit $(\rho,\Phi)$ phase portrait: locking boundary $\lvert\omega\rvert = \lvert\kappa_u\rvert\cosh(2\rho)$, persistence boundary $\mathcal{O}\cosh(2\rho) = \gamma$, four transport class regions, Branch 1 nodes, Branch 2 centers, flow arrows | dynamics | medium | makes the classification theorem visually transparent; needed for any publication on the two-branch system (plot helper: `checks/plot_phase_portrait.py`) |
| promote parameters to momentum-dependent functions $\omega(p)$, $\gamma(m,p)$, $\kappa_u(a,b,c;p,s)$; determine the locking boundary as a curve in momentum space | dynamics / phenomenology | medium | where kinematic regime structure appears — why some states are long-lived only at certain momenta |
| derive the connection between the two-branch amplitude picture and the Lindblad-Markov density-matrix reduction | dynamics | high | the two pictures are complementary levels; how coarse-graining recovers the Lindblad equation with $D \sim m^2/\gamma$ from the incoherent (dephased) branch is the key link |
| derive the hydrogen/Efimov bridge: identify the `SO(4)`, `SO(3,1)`, and `SO(2,1)` subgroup data of the transport classification and test whether the Efimov exponent `s_0` is a function of `\omega/\kappa_u` at the persistence threshold | dynamics / phenomenology / interpretation | high | strongest check is quantitative: either recover or fail to recover `s_0 \approx 1.00624`; until then the bridge remains interpretive |
| identify physically meaningful Hamiltonians or material realizations exhibiting the Spin(2,3) topological class structure | topological / phenomenology | medium | the class assignment is now much sharper, but the physical realization problem remains open |
| identify what observable probes the DIII `\mathbb{Z}` invariant of the massless `T1` sector | topological / phenomenology | medium | **substantially advanced**: `W_3 = 1` implies one protected massless T1 channel in the minimal reduced block at the mass-transition surface; observable candidates identified: (1) protected critical point, (2) quantized topological response coefficient, (3) half-integer parity anomaly shift on transition surface; the relative sign-tracking with `\kappa_u` is now closed at the convention level, while physical orientation selection remains open |
| determine whether the DIII topological structure participates in anomaly inflow and links to the anomaly-cancellation constraints | topological / consistency | medium-low | **sharpened bridge candidate**: `kernels/diii-anomaly-bridge.md` now shows that the weak/global `SU(2)` shadow works cleanly, but the color and `U(1)` parity data remain localization-dependent; the current corpus default is Scenario A for established claims and Scenario D for the bridge hypothesis, while Scenarios B/C require a new boundary-Hamiltonian calculation |

### NS programme bridge tasks (added from ns_to_spin23_integration.md)

The NS/J3(O) regularity programme has identified several structural parallels with the Spin(2,3) framework. The following bridge arguments are required before any NS-derived structure can function as more than corroborating evidence.

| Bridge task | Domain | Severity | Comment |
|---|---|---|---|
| find a rescaling group in the Spin(2,3) setting for which the preferred octonionic direction is the unique fixed point, analogous to BKM scale-invariance of s* | statics | high | would promote the octonionic alignment claim from Level 4 to derived |
| count the independent gauge-invariant nonlocal observables of the theory and compare to 12 | statics / consistency | medium | decides J3(O) vs J3(C⊗O) from the observable-algebra side |
| establish that pure observable-sector propagation is dynamically unstable in the Spin(2,3) setting, or that γ > 0 is forced by the dynamics | dynamics | high | Spin(2,3) analogue of NS Gap A |
| derive from Spin(2,3) representation theory that the relevant scaling exponents are forced to differ by 1/2 | dynamics / consistency | medium | would independently verify the NS exponent gap |
| prove or disprove that Jordan algebra positivity N_lifted ≥ 0 is inconsistent with violation of reflection positivity in the dual theory | consistency | medium | potential route to close Gap A from the gauge-theory side |
| physically justify the identification m ~ strain rate a(t) and γ ~ vorticity correlation |b_ij| in the NS/Spin(2,3) parameter mapping | dynamics | medium-low | dimensional analogy only at present; needs an independent physical argument |

---

## Working bottom line

The project already has a coherent spine, but coherence is not completion.

The main open problems are not random loose ends. They cluster around a few deep tasks:

1. stronger uniqueness and exclusion proofs
2. a sharper ambient-to-observable reduction map
3. stronger microscopic control of the reduced dynamics
4. stronger justification of the projection rule
5. stronger bridge to observable physics

This file should be updated as the project matures. It is the record of what still has to be earned.
