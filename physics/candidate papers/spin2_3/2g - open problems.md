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

- why is `T1` the observable sector rather than `T2` or some other subspace?
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

This priority order matches the current maturity of the project.

---

## Open-problem ledger

| Problem | Domain | Severity | Comment |
|---|---|---|---|
| hidden-sector correlator lacks first-principles derivation | dynamics | high | major blocker for stronger dynamical claims |
| hypercharge uniqueness still needs a sharper proof structure | consistency | high | important for static papers |
| generation-counting and fourth-generation exclusion remain heavy proof burdens | statics / consistency | high | one of the biggest weak spots |
| ambient-to-observable reduction is not yet sharply defined | cross-domain | high | central missing-middle object |
| projection onto `T1` lacks a deeper justification | epistemics | medium-high | now reduced to one final issue: derive why the unique direct readout branch must be the constructive/persistent one (`\kappa_u > 0` in phase-normalized gauge); with that rule, the support-preserving reduction to `T1` is conditionally closed |
| parent octonionic geometry has not yet been rigorously reduced to the effective `Spin(2,3)` branch | statics / cross-domain | high | now a central parent-program task |
| folded `Spin(3,3)` insight has not yet been formalized as a precise reduction map into hidden quaternionic complex-plane structure | statics / cross-domain | high | new central bridge task |
| Heisenberg-type structure is not yet derived from a hidden antisymmetric sector | dynamics / epistemics | high | requires more than diffusion |
| full field-theoretic completion is missing | dynamics / completion | high | major long-term gap |
| no sharp experimental predictions yet | phenomenology | high | blocks PRD-style work |
| interpretation can still outrun proof if not carefully disciplined | interpretation | medium | recurring writing risk |

### Two-branch transport tasks (added from octonionic transport coherence framework)

| Problem | Domain | Severity | Comment |
|---|---|---|---|
| derive the two-branch evolution equations $\dot{A} = (u\omega-\gamma)A + \kappa_u\bar{B}$ from a variational principle on the octonionic bulk | dynamics | high | the equations now admit an explicit Hamiltonian-plus-Rayleigh scaffold on the selected `u`-complex line; the remaining task is to derive its ingredients from the parent bulk: branch symplectic form, charge-flip/conjugation exchange, odd moment `\kappa_u`, and positive leakage term `\gamma` |
| express $\kappa_u$ as a genuine Sp(4,ℝ) moment map of the associator — show it is the Hamiltonian generator of branch rotations, not merely an invariant projection | dynamics / statics | medium | **substantially closed at the symmetry level**: $\kappa_u$ is $K$-invariant by $K \subset \mathrm{Stab}_{G_2}(u)$, and exchange-odd by $\mathfrak K_u: u \mapsto -u$; the uniqueness argument then forces descent as $\kappa_u \mathcal M_{\mathrm{ex}}$; remaining open: variational origin of the coupling from a parent action, and orientation ($\kappa_u > 0$ criterion) |
| compute $G_2 \cap \mathrm{Spin}(2,3)$ and determine its irrep content | statics | high | the intersection is the symmetry seeing both octonionic structure and transport projection simultaneously; if it contains $SU(3) \times SU(2) \times U(1)$ the framework has direct phenomenological potential |
| render the explicit $(\rho,\Phi)$ phase portrait: locking boundary $\lvert\omega\rvert = \lvert\kappa_u\rvert\cosh(2\rho)$, persistence boundary $\mathcal{O}\cosh(2\rho) = \gamma$, four transport class regions, Branch 1 nodes, Branch 2 centers, flow arrows | dynamics | medium | makes the classification theorem visually transparent; needed for any publication on the two-branch system |
| promote parameters to momentum-dependent functions $\omega(p)$, $\gamma(m,p)$, $\kappa_u(a,b,c;p,s)$; determine the locking boundary as a curve in momentum space | dynamics / phenomenology | medium | where kinematic regime structure appears — why some states are long-lived only at certain momenta |
| derive the connection between the two-branch amplitude picture and the Lindblad-Markov density-matrix reduction | dynamics | high | the two pictures are complementary levels; how coarse-graining recovers the Lindblad equation with $D \sim m^2/\gamma$ from the incoherent (dephased) branch is the key link |
| derive the hydrogen/Efimov bridge: identify the `SO(4)`, `SO(3,1)`, and `SO(2,1)` subgroup data of the transport classification and test whether the Efimov exponent `s_0` is a function of `\omega/\kappa_u` at the persistence threshold | dynamics / phenomenology / interpretation | high | strongest check is quantitative: either recover or fail to recover `s_0 \approx 1.00624`; until then the bridge remains interpretive |
| identify physically meaningful Hamiltonians or material realizations exhibiting the Spin(2,3) topological class structure | topological / phenomenology | medium | the class assignment is now much sharper, but the physical realization problem remains open |
| identify what observable probes the DIII `\mathbb{Z}` invariant of the massless `T1` sector | topological / phenomenology | medium | **substantially advanced**: `W_3 = 1` implies one protected massless T1 mode at the mass-transition surface; observable candidates identified: (1) protected critical point, (2) quantized topological response coefficient, (3) half-integer parity anomaly shift on transition surface; sign of `W_3` may correlate with `\kappa_u > 0` — specific calculation identified |
| determine whether the DIII topological structure participates in anomaly inflow and links to the anomaly-cancellation constraints | topological / consistency | medium-low | **advanced to bridge candidate**: DIII bulk produces a T₀ anomaly inflow; conjecture that this matches the gauge anomaly conditions in 2d; requires explicit coefficient matching — identified as a concrete next calculation |

### NS programme bridge tasks (added from ns_to_spin23_integration.md)

The NS/J3(O) regularity programme has identified several structural parallels with the Spin(2,3) framework. The following bridge arguments are required before any NS-derived structure can function as more than corroborating evidence.

| Bridge task | Domain | Severity | Comment |
|---|---|---|---|
| find a rescaling group in the Spin(2,3) setting for which the preferred octonionic direction is the unique fixed point, analogous to BKM scale-invariance of s* | statics | high | would promote the octonionic alignment claim from maturity 4 to derived |
| count the independent gauge-invariant nonlocal observables of the theory and compare to 12 | statics / consistency | medium | decides J3(O) vs J3(C⊗O) from the observable-algebra side |
| establish that T1-pure propagation is dynamically unstable in the Spin(2,3) setting, or that γ > 0 is forced by the dynamics | dynamics | high | Spin(2,3) analogue of NS Gap A |
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
