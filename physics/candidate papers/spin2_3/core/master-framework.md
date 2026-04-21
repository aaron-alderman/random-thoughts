# Master Framework: Project Breakdown

## Purpose

This document applies the generic framework taxonomy to this specific research program.

The goal is to keep separate:

1. the mathematical structures being used
2. the dynamical assumptions being made
3. the observational postulates being introduced
4. the constraints that force or exclude certain outcomes
5. the physical interpretations being suggested
6. the phenomenological consequences that might follow
7. the parts of the program that are still incomplete

This is the project-facing map.

The reusable generic version lives outside this project folder as the earlier meta-framework note.

---

## One-sentence project spine

Start from `Spin(2,3)`, the octonions, and `J3(O)`; select the octonionic direction aligned with the channel of massless traversal; let that alignment define the effective observable sector; then ask how massive couplings depart from pure `T1` propagation and what representation structure, reduced dynamics, and interpretation follow.

Parent exploratory note:

- the current strongest parent branch now sits one level above this reduced spine and treats a selected imaginary octonionic direction `u` as the effective time anchor, with `u^\perp \cong \mathbf{C}^3` as the main hidden geometric remainder and a local quaternionic `H` slice as the carrier of the relevant hidden complex plane; the earlier `Spin(3,3)` lift is now read as a transitional calculation that revealed this fold rather than as a live parent branch; see `core/parent-inquiry-map.md`

---

## How claims should be read here

This document is allowed to make working choices. That is part of building the program.

But each major claim should be read in the following bounded way:

- what is already fixed by the lens being used here
- what live options remain within that lens
- which branch this project is currently running with
- whether that branch is an axiom, a choice, a derivation, an interpretation, or still missing

So when this document speaks firmly, it does not always mean the alternatives are dead. It may only mean:

- this is the current working branch
- this branch is coherent enough to build with
- the bridge must later explain why it is physically preferred, or why the nearby alternatives are not

Conversely, this document should not keep reopening what the lens has already chosen. If a structure is fixed by the lens, it is allowed to function as local starting data.

This matters especially in cases like:

- `J3(O)` versus `J3(C \otimes O)`
- primitive projection versus observability downstream of zero-mass exchange
- exact origin of the selected octonionic direction
- Higgs-mediated mass generation as the route to `T1/T2` coupling
- how the larger octonionic parent geometry folds into the effective `Spin(2,3)` branch without reifying extra timelike directions

---

## NS Programme cross-reference

A parallel programme in NS regularity via J3(O) has been independently developed. Its structural overlaps with this framework are treated as external context rather than live Spin(2,3) corpus material. The transfer summary:

- The NS programme has constructed an explicit full-rank embedding of local fluid variables into J3(H) and lifted it to J3(O) via 12 bilocal vorticity correlations, closing the dimensional count 15+12=27 exactly (maturity 3–4). This bears on the J3(O) vs J3(C⊗O) choice.
- G2 transitivity on S⁶ is proved, and the BKM blow-up rescaling group selects the vorticity direction ξ̂ as its unique fixed point (maturity 3). This provides a structural template for how the preferred octonionic direction might be forced rather than chosen.
- The strain-only blow-up attractor (1D ray in Q-R space with J̃ = 0) is structurally consistent with pure T1 propagation; transverse terms that prevent collapse onto the ray are structurally consistent with T2 mixing preventing T1 collapse (maturity 4 for the NS result; maturity 5 for the bridge identification).
- An exponent gap of 1/2 in the NS scaling contradiction is proposed to reflect the rigidity of the fermionic sector in Spin(2,3) representation theory (maturity 5 for bridge identification).

All bridge identifications between the two programmes are maturity 5 proposals. None substitute for independent derivation within the Spin(2,3) framework. The NS programme is most useful as a source of structural templates that reduce the search space for missing bridge arguments.

---

## Outstanding within the lens

The current lens fixes the broad starting structures, but some especially important questions remain live within it.

- `SU(3)`: the stabilizer isomorphism obtained from octonionic vector selection is mathematically standard; the live question is what formal treatment is still needed to realize that `SU(3)` as physical color within this lens
- `Mixing`: the current analysis gives conditional reduced dynamics once a privileged zero-mass channel and `T1` readout are specified; the live question is whether mixing does more than develop the consequences of that prior choice
- `Geometric mass`: the current formalism identifies `m` as the sector-mixing scale; the live question is whether that scale, or its spectrum, is geometrically derived rather than introduced as effective solution-level data

These are not objections to the lens. They are the main places where the lens is still doing active work.

---

## Top, Bottom, and Bridge

The project is best understood as having three methodological levels.

### Top down

Start from the largest plausible ambient structure and ask:

- what symmetries exist
- what sectors are available
- what gauge, family, and dynamical structures are even possible

In this spirit, a large `RCHO`-type ambient fiber or related enlarged space is not a problem in itself. It is the possibility space.

### Bottom up

Start from the experimentally constrained Standard Model world and ask:

- what must be preserved
- what minimal low-energy structure is already known
- what cannot be violated

### Bridge or missing middle

The distinctive task of this series is to build the bridge between those two ends:

- enough structure to explain why Standard-Model-like physics emerges from the top space
- enough constraint to reduce the ambient space without pretending it was never there

This bridge is the real identity of the project.

---

## Ambient-to-observable reduction

One useful way to name the bridge object is:

> **ambient-to-observable reduction**

This means the framework should eventually specify how a large ambient space is reduced to:

1. the physically relevant sector
2. the gauge-reduced or constraint-reduced sector
3. the actually observable sector

This matters because a large ambient space can contain:

- redundant information
- zero directions
- gauge-equivalent structure
- sectors that are dynamically present but not directly observed

That does **not** make the ambient space invalid. It only means that the reduction map has to be understood.

At the project level, the safe position is:

- the full ambient space may be real and generative
- the Standard Model may be a reduced visible slice of that larger structure
- the framework owes a disciplined account of how that reduction happens

This same bridge discipline also applies when there is more than one mathematically valid high-level organizing object. For example:

- `J3(O)` is a standard real exceptional Jordan object
- `J3(C \otimes O)` or `H_3(O_C)` is also a mathematically valid complexified exceptional Jordan object

The framework should not treat that choice as already settled unless a bridge argument settles it. In the language of this project:

- the mathematics may permit both
- the bottom-up constraints may not yet distinguish them
- the bridge must explain which one is physically relevant, or whether one is ambient and the other effective

So this is not a defect. It is exactly the kind of choice the missing middle is supposed to discipline.

In practice, this means that when the project says "use `J3(O)`" it should often be read as:

- live options: `J3(O)`, `J3(C \otimes O)`, or a relation between them
- working branch: start with `J3(O)` because it is the simpler real exceptional object
- status: choice
- bridge burden: explain why this is the physically relevant branch, or why the larger complexified object is only ambient

---

## 1. Statics / Kinematics

This is the layer of mathematical structure before effective dynamics is reduced.

### Core objects

- `Spin(2,3)` and its four-component spinor representation
- the generator `J^{01}` and the induced effective sector split
- the octonions `O` with automorphism group `G2`
- the reduction to `SU(3)` after fixing a preferred imaginary direction
- the exceptional Jordan algebra `J3(O)` as the organizing space for generations
- the possible complexified exceptional Jordan algebra `J3(C \otimes O)` as a larger ambient alternative
- the selected direction associated with massless traversal or zero-mass interaction
- a local quaternionic `H` slice inside `O` carrying the hidden complex-plane data relevant to the reduced branch
- the larger ambient space within which these selected structures live

### Project-specific structural claims

- The spinor decomposes into two two-component sectors, `T1` and `T2`, once a time orientation is chosen.
- In the current reading, this `T1/T2` split is the effective reduced image of a deeper hidden complex-plane structure rather than evidence that literal extra time directions remain fundamental.
- The `SU(2)` structure comes from the maximal compact subgroup acting on the spinor blocks.
- The octonionic sector supplies the color structure through `G2 -> SU(3)`, but only after a direction in `O` is selected.
- The physically relevant octonionic direction should be aligned with the direction associated with zero-mass traversal.
- The relevant hidden two-plane is carried locally by a quaternionic slice inside `O`, while the broader parent remainder remains `u^\perp \cong \mathbf{C}^3`.
- `J3(O)` supplies a natural three-slot structure relevant to generation organization.
- `J3(C \otimes O)` is also mathematically available as a larger complexified organizing object, but its physical role is not yet fixed.
- The `T1/T2` split is kinematically present before it is physically interpreted.

### Status

- `Spin(2,3)` spinor structure: derived mathematics once the group is chosen
- `T1/T2` split: derived once time orientation is chosen, then read as the effective branch of a deeper hidden complex-plane structure
- preferred octonion direction: choice
- alignment between the preferred octonion direction and the massless-traversal direction: central framework proposal
- local quaternionic carrier of the hidden complex plane: working proposal suggested by the folded `Spin(3,3)` analysis, not yet a theorem
- hidden-line phase covariance forcing charge-diagonality of the parent zero-mass operator: sharpened bridge result
- charge-generator intertwiner `J_{\Pi,\mathrm{toy}} \to J^{01}` as the cleanest route to support preservation: current reduction target
- use of `J3(O)` for generations: structural proposal, partly derived and partly interpretive depending on claim strength
- choice between `J3(O)` and `J3(C \otimes O)`: bridge-level choice not yet physically settled

---

## 2. Dynamics

This is the layer describing how the state evolves.

### Core dynamical ingredients

- evolution in the full space `T1 (+) T2`
- transport operator acting in `T1`
- off-diagonal coupling between `T1` and `T2`
- reduced evolution for the projected sector
- effective transport-diffusion after coarse-graining
- hidden oriented two-plane data feeding the reduced correction terms
- a distinguished role for zero-mass propagation in defining the effective observable channel

### Project-specific dynamical claims

- Zero-mass interactions or traversal propagate only on the selected `T1` channel.
- The microscopic model is a block Hamiltonian or generator with transport in `T1` and mixing between sectors once mass is present.
- The hidden structure needed for richer corrections is interpreted as an internal complex `2`-plane, locally carried by a quaternionic slice inside `O`, rather than as literal extra time directions.
- The leading observable correction from sector mixing enters at second order in the coupling.
- Under weak coupling, fast hidden-sector relaxation, and Markov coarse-graining, the reduced evolution is time-local.
- In the long-wavelength limit, the observable density satisfies an advection-diffusion equation with `D ~ m^2 / gamma`.
- Massive or Higgs-mediated structure is the natural place where access to `T2` can enter.

### Status

- zero-mass propagation on `T1`: central framework proposal
- one-sector zero-mass traversal: now narrowed to an oriented-direction plus unique-channel consistency burden
- support preservation of `H_0` on `T1`: best current route is through a charge-generator intertwiner in the reduction map
- remaining global `\mathbf Z_2` orientation: best current route is to tie it to the forward observable/readout arrow rather than treat it as a large unresolved basis freedom
- strongest current sharpening: the physical orientation is the one aligning direct zero-mass support, observable readout, and forward reduced evolution on the same sector
- best current bulk forcing candidate for that alignment: the sign of the odd transport scalar `\kappa_u`
- strongest current operational version: in the readout-phase normalization, the direct observable branch should be constructive/persistent, hence `\kappa_u > 0`
- current blocker status: `N2` is conditionally closed once that constructive-readout rule is adopted; the live burden is to derive it from the bulk rather than leave it as the final operational axiom
- `N3` derivation target is now sharper: derive `\dot\Psi = u\omega\,\Psi - \gamma\,\Psi + \kappa_u\,\mathcal C\Psi` from a parent branch state, an anti-linear exchange operation, an odd moment map, and controlled hidden-sector leakage
- stronger `N3` scaffold: the branch equations already form an exact Hamiltonian-plus-Rayleigh system on the selected `u`-complex line, so the bulk task is to derive that specific generator rather than guess one
- reduced coupling structure is now explicit: `\kappa_u` multiplies the fixed exchange generator `\mathcal M_{\mathrm{ex}} = -\mathrm{Im}_u(AB)`
- parent source for the exchange structure is now explicit: the anti-linear map `\mathfrak C_u = (C_\Pi \otimes 1)\circ \mathfrak K_u` descends to `\mathcal C(A,B) = (\bar B,\bar A)`
- symmetry slot for `\kappa_u` is now explicit: compact-equivariant anti-linear exchange maps are unique up to scalar, so an odd parent moment can only descend into the coefficient of `\mathcal M_{\mathrm{ex}}`
- reduced damping structure is now explicit: `\gamma` can arise as a positive hidden-sector elimination term of Schur-complement type
- symmetry route for scalar damping is now explicit: compact-equivariant elimination gives sectorwise scalars, and charge-exchange symmetry collapses them to `\gamma I_4`
- minimal admissible hidden coupling class is now explicit: compact-equivariant, charge-exchange-symmetric elimination is enough to force scalar damping
- current `N3` descent criteria are now explicit: the parent odd moment must be compact-equivariant and exchange-odd to force `\kappa_u \mathcal M_{\mathrm{ex}}`, while hidden elimination must be compact-equivariant and charge-exchange symmetric to force scalar `\gamma`
- full-space evolution: postulated model choice
- reduced Markovian equation: derived under assumptions
- diffusion law: derived under additional closure assumptions
- identification of `m` as a mass scale: interpretation of the derived parameter role

---

## 3. Epistemics / Observables

This is the layer of what is visible, measurable, or retained after coarse-graining.

### Core epistemic postulates

- the effective observable channel is determined by the selected direction of zero-mass interaction
- `T2` is not directly observed through that zero-mass channel, but can affect the observable sector indirectly
- reduced physics arises from this interaction selection together with coarse-graining

### Project-specific epistemic claims

- The observable algebra is effectively filtered through `T1` because zero-mass interactions travel on that channel.
- The hidden sector is not discarded dynamically; it is only hidden observationally.
- Effective uncertainty and diffusion appear because the observer does not resolve `T2` excursions.
- The projection onto `T1` may be downstream of the interaction structure rather than an absolutely primitive axiom.

### Status

- `T1` as the effective observable channel for zero-mass interactions: central proposal
- projection onto `T1`: possibly effective rather than primitive; the remaining burden is now the uniqueness of one-sector readout
- hidden-sector influence on visible dynamics: derived once the interaction rule and dynamics are combined
- reading coarse-graining as epistemic limitation: interpretation

This is one of the most distinctive parts of the project. It is not reducible to pure statics or pure dynamics.

---

## 4. Consistency / Selection

This is the layer of constraints, exclusions, and things that become forced once the setup is fixed.

### Core consistency questions

- which structures are choices and which are fixed by the framework
- whether the reduced dynamics is positive and stable
- whether representation content is anomaly free
- whether generation counting is forced or only suggestive
- whether the real or complexified exceptional Jordan organizing space is the physically correct bridge object

### Project-specific consistency claims

- The reduced projected dynamics should preserve trace and positivity in the appropriate regime.
- If the selected direction is physically oriented and the zero-mass readout channel is unique, then one-sector traversal is the minimal selection-consistent realization.
- Anomaly cancellation constrains the allowed right-handed matter content once the left-handed content is fixed.
- Some hypercharge coefficients may be uniquely fixed by the charge-matching and anomaly conditions.
- A fourth generation may be excluded if the `J3(O)` argument is mathematically sound in the intended form.
- Gauge invariance should constrain the alignment between the selected octonionic direction and the massless-interaction direction rather than allowing unrelated choices.
- If both `J3(O)` and `J3(C \otimes O)` are mathematically available, the framework should explain whether one is fundamental, one is effective, or one is ruled out by the bridge to observed physics.

### Status

- positivity / complete positivity in reduced dynamics: derived under reduction assumptions
- anomaly constraints: standard derived consistency condition
- uniqueness of hypercharge embedding: partly derived, needs careful wording in paper form
- exact three-generation exclusion: strong claim, needs especially careful proof burden
- `J3(O)` versus `J3(C \otimes O)`: significant unresolved bridge choice unless a future argument resolves it

This is the layer where "natural" should be replaced by "forced by these constraints."

---

## 5. Interpretation

This is the layer of physical meaning assigned to the structure.

### Core interpretive ideas

- mass as sector mixing
- uncertainty as unresolved hidden-sector motion
- chirality as a consequence of sector asymmetry
- multiple observed structures as reflections of one common geometry
- the selected octonionic direction and the observable time-oriented channel are aspects of the same physical choice
- the Standard Model may be the reduced visible face of a larger ambient space rather than the whole ontological structure

### Project-specific interpretation claims

- `m` is read as an effective mass parameter because it controls the first departure from purely ballistic visible transport.
- Diffusion is read as the observable shadow of hidden-sector excursions.
- The asymmetry between `T1` and `T2` is read as physically meaningful rather than merely representational.
- The same geometric choices may underlie time orientation, color structure, and charge structure.
- An early selection of direction may fix the later observable channel for zero-mass interactions.
- Higgs-mediated mass generation may be what opens access away from pure `T1` propagation.
- Much of the ambient space may be physically redundant, gauge-reduced, or observationally filtered without thereby being meaningless.

### Status

- all items in this section are interpretation unless a given paper explicitly proves more than that

This category is valuable, but it should not be allowed to masquerade as theorem-level derivation.

---

## 6. Phenomenology

This is the layer of empirical or quasi-empirical implications.

### Core phenomenological directions

- scaling laws for effective coefficients
- deviations from standard unitary evolution
- particle-structure consequences of the static sector
- possible hidden-sector signatures

### Project-specific phenomenological claims

- In the reduced-dynamics regime, `D ~ m^2 / gamma`.
- Stronger sector mixing corresponds to stronger effective observable broadening.
- If the representation-theoretic sector survives scrutiny, it may organize quark, lepton, and generation structure.
- Hidden-sector effects might produce small deviations from idealized unitary behavior at short scales.
- If Higgs-mediated mass generation is the route to `T1/T2` coupling, then the framework should eventually tie mass generation to departure from pure observable-channel transport.

### Status

- diffusion scaling: semi-derived within the reduced model
- broader particle-physics implications: not yet quantitative
- direct experimental predictions: still missing

At present, this layer is promising but immature.

---

## 7. Completion / Open problems

This is the layer of what the framework still owes.

### Major open problems

- first-principles derivation of hidden-sector relaxation and the scale `gamma`
- fully relativistic field-theoretic completion
- explicit gauge dynamics
- direct geometric derivation of all fermion sectors
- robust derivation of CKM and PMNS structure
- mass hierarchy
- neutrino masses
- experimentally usable predictions or bounds
- a sharper derivation of why the selected octonionic direction should align with the massless-interaction channel
- a sharper account of the relation between Higgs-mediated mass generation and `T1/T2` coupling
- a clear ambient-to-observable reduction map from the large space to the Standard-Model-like visible sector
- a bridge argument for whether the physically relevant exceptional Jordan object is `J3(O)`, `J3(C \otimes O)`, or a relation between them; the NS programme suggests this can be resolved by counting independent gauge-invariant nonlocal observables
- an independent argument that the preferred octonionic direction is the unique fixed point of a rescaling group analogous to BKM, which would promote the alignment claim from a central proposal to a derived result
- a derivation that T1-pure propagation is dynamically unstable or that hidden-sector relaxation γ > 0 is forced, which is the Spin(2,3) analogue of NS Gap A

### Project-specific publication lesson

Different papers should stop at different layers:

- Paper 1, PLA-style target: mostly Dynamics plus Epistemics
- Paper 2, JMP-style target: Dynamics plus Consistency
- Paper 3, EPJC-style target: Statics plus Consistency
- Paper 4, PRD-style target: only after Phenomenology is stronger

---

## Logical status and claim maturity matrix

The project is easiest to manage if each claim is tagged by category, logical status, and claim maturity.

### Main statuses

- `Axiom/Postulate`
- `Choice`
- `Derived`
- `Interpretation`
- `Missing`

### Claim maturity levels

- `1`: trivial
- `2`: solid established
- `3`: established and normally cited
- `4`: being established in this paper
- `5`: plausible but future work
- `6`: significant issue

### Examples from this project

| Claim | Category | Status | Maturity |
|---|---|---|---|
| `Spin(2,3)` has a four-component spinor representation | Statics | Axiom/input to framework | 2 |
| Choosing a time orientation induces a `T1/T2` split through `J^{01}` | Statics | Choice plus derived consequence | 3 |
| A preferred octonionic direction must be selected to recover the framework's `SU(3)` color slot | Statics | Established structural fact inside the framework | 3 |
| The selected octonionic direction should align with the zero-mass interaction channel | Statics / Epistemics | Central proposal | 4 |
| Zero-mass interactions define the effective observable channel `T1` | Epistemics / Dynamics | Central proposal | 4 |
| Off-diagonal `T1/T2` mixing can be used in the microscopic generator | Dynamics | Choice | 4 |
| Weak-coupling reduction yields a reduced Markovian equation | Dynamics | Derived under assumptions | 4 |
| The long-scale observable dynamics has `D ~ m^2 / gamma` in the reduced model | Phenomenology | Derived within model | 4 |
| Anomaly cancellation constrains the allowed right-handed content | Consistency | Derived consistency condition | 3 |
| The sector-mixing scale may encode physical mass after further identification | Interpretation | Interpretation | 5 |
| Higgs-mediated mass generation may be the route by which `T2` becomes dynamically accessible | Interpretation / Phenomenology | Plausible future direction | 5 |
| The framework may organize CKM / PMNS structure | Phenomenology | Missing / future development | 5 |
| The framework currently lacks sharp experimental bounds | Completion | Missing | 6 |

### Practical reading rule

- `1-3` can be used as input or background
- `4` is what the current paper or draft must explicitly earn
- `5` belongs in discussion and future work
- `6` must be stated as a real weakness or unresolved issue

---

## Bottom line

The project is not just a split between statics and dynamics.

Its more complete structure is:

1. `Statics`: what structures exist
2. `Dynamics`: how they evolve
3. `Epistemics`: what is seen
4. `Consistency`: what is forced or forbidden
5. `Interpretation`: what it means
6. `Phenomenology`: what it predicts
7. `Completion`: what remains unfinished

For this program, the especially important extra axis is `Epistemics`, because the observable sector may be determined by the selected massless-interaction channel rather than by a purely separate projection rule.
