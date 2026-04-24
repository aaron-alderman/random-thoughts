# Epistemics Kernel

## Purpose

This document is the epistemics source text for the project.

It is not a paper draft. It is the place where the framework's claims about observability, projection, coarse-graining, and hidden structure are kept coherent inside one domain. The goal is to say:

- what counts as observable in the framework
- what remains hidden but dynamically active
- how projection relates the full structure to accessible physics
- what is postulated, what is derived, and what is still only interpretation

This file sits between statics and dynamics. It is the bridge between what exists and what is seen.

---

## Scope

This file covers:

- the observable status of `T1`
- the hidden but dynamically real status of `T2`
- projection as the rule connecting full structure to observed physics
- coarse-graining as a map from full evolution to effective observables
- the epistemic reading of uncertainty and broadening

This file does not cover:

- the full static derivation of the sectors
- the microscopic derivation of the reduced generator
- particle-representation structure beyond what is needed to define observables
- experimental predictions in quantitative form

---

## Core epistemic question

The central epistemic question of the framework is:

> If the formal state space contains more structure than is directly observed, what rule determines the observable part of the theory?

The present framework no longer needs to answer that only with a bare projection principle. A stronger version is available:

- the observable channel is determined by the selected axis of zero-mass interaction
- projection onto the induced observable sector, currently named `T1`, is then the effective observable rule downstream of that interaction structure

This should now be read alongside the ambient-reduction scaffold:

- the `T1/T2` split is a reduced output of a deeper hidden complex-plane structure
- the remaining open question is not whether one may postulate projection, but whether the zero-mass readout projector can be dynamically or ambient-geometrically forced rather than only epistemically imposed

---

## Epistemic inputs

The epistemic layer assumes:

1. The static domain provides a sector split
   $$
   \mathcal{H}_{\mathrm{spin}} = T1 \oplus T2.
   $$
2. The dynamics domain allows evolution in the full space.
3. The static and interaction structure select a privileged channel for zero-mass traversal.
4. The framework is willing to distinguish between what exists dynamically and what is directly accessed observationally.

The decisive epistemic move is therefore not just "project onto `T1`," but:

- identify the observable channel with the channel used by zero-mass interaction

---

## Central epistemic principle

### Principle E1: observable access follows the zero-mass channel

The effective observable sector is the sector singled out by zero-mass traversal or interaction.

In the current framework, that channel is conventionally named `T1` after the readout orientation is fixed.

This is the deeper epistemic proposal. It explains why one sector matters observationally without needing to begin from an entirely separate visibility axiom.

At present, the cleanest reading is:

- the channel-selection story is more structured than a bare primitive axiom
- but the final derivation of that projector from bulk dynamics or ambient scale-flow geometry is not yet a full theorem

So Principle E1 should be treated as a sharpened framework principle, not as a closed derivation.

### Effective postulate E2: projected observables

Physical observables are evaluated after projection onto the induced observable sector.

At the operator level, if `O` is an observable acting on the accessible sector, then its physical expectation value is taken to be
$$
\langle O \rangle = \mathrm{Tr}(\rho P O P),
$$
or equivalently through the projected state
$$
\rho_1 = P \rho P.
$$

This is not yet a theorem in the current framework. But in the revised backbone it is best read as the effective observational rule induced by Principle E1.

In the current orientation convention, `P` is the projector onto the sector named `T1`. The projector is the invariant object; the sector name is bookkeeping.

---

## Meaning of the hidden sector

The framework does **not** treat `T2` as nonexistent.

Instead:

- `T2` is dynamically present
- `T2` can influence the evolution of `T1`
- `T2` is not directly read out in the observable algebra

So the hidden sector is:

- ontic within the model
- epistemically restricted

This distinction is central. The framework does not say "ignore `T2`." It says "`T2` is real in the evolution, but not directly visible in the final observational channel."

In the revised picture, `T2` is hidden specifically because zero-mass interactions do not use it directly.

---

## Projection versus elimination

It is important to distinguish two different operations.

### Projection

Projection is the observational rule:

- what is treated as visible
- what expectation values are formed from

### Elimination or coarse-graining

Elimination is the dynamical reduction:

- how hidden degrees of freedom are integrated out
- how their unresolved effect appears in the reduced law

These are related but not identical.

The framework is strongest when it keeps them separate:

- the zero-mass channel is the deeper epistemic principle
- projection is the effective observational rule
- elimination is a dynamical derivation under assumptions

---

## Observable algebra

At the kernel level, the observable algebra is taken to be the algebra generated on the induced observable sector, or equivalently the subalgebra selected by `P O P`.

Safe consequences:

- expectation values are determined by the projected state
- effective measured densities live in the sector named `T1` after orientation is fixed
- hidden-sector influence enters indirectly through the evolution of the projected state
- this algebra is physically privileged because it is the one reached by the selected zero-mass interaction channel

What this does **not** yet settle:

- whether the full observable algebra should be exactly `P A P` in every formulation
- whether there are contexts in which mixed `T1/T2` observables should count as indirectly measurable
- whether the projection rule has a deeper derivation

Those remain open.

---

## Two routes for `T1` observability

The framework should keep two possible justifications distinct.

### Route A: dynamical or ambient selection

The strongest route would derive that zero-mass interaction acts directly only on one reduced charge sector, and that this sector is the reduced image of the forward readout or scale-flow selector.

If that route succeeds, then:

- the observable projector is dynamically or ambient-geometrically selected
- projection onto the sector named `T1` is derivative rather than primitive

This route is not yet complete.

### Route B: epistemic selection

The weaker but currently cleaner route is:

- the reduction produces `T1 \oplus T2`
- the framework identifies one reduced sector as the zero-mass readout channel and names it `T1`
- projection onto that induced sector is then the effective observational rule

This route is already coherent with the present kernel, as long as the naming of the readout channel as `T1` is tracked explicitly as an orientation convention rather than smuggled in as a theorem.

### Present status

The current project sits between these routes:

- stronger than a bare projection axiom
- weaker than a fully forced dynamical selection theorem

That middle position is acceptable, but it should be named clearly.

The recent reduction sharpening improves this picture slightly. If hidden-line phase covariance is granted, then the zero-mass channel is already forced to be charge-diagonal before reduction. The remaining epistemic burden is narrower:

- not "why project at all from an arbitrary split?"
- but "why does direct zero-mass readout use only one of the two oriented charge sectors?"

That does not finish Route A, but it does make Route B less ad hoc. The projection rule is no longer floating over a completely unexplained decomposition; it sits downstream of a hidden charge split and a still-open one-sector traversal principle.

There is now a further consistency pressure in the same direction. If the two hidden charge sectors are the two orientations of a single hidden line, and if the observable channel is supposed to be unique, then allowing both sectors to serve as direct zero-mass readout channels would undercut the uniqueness of the observable rule. So the epistemic layer now has a cleaner remaining burden:

- justify why the chosen oriented direction yields one direct readout channel rather than two

That is still not a theorem, but it is a much narrower target than the older demand to justify projection from scratch.

The residual `\mathbf Z_2` ambiguity now also has a cleaner location. It should not be thought of as a large hidden ambiguity in the algebra. The reduction fixes the structure almost completely, and the last global reversal is best read as the choice of which orientation counts as the physical forward/readout orientation. In that sense, the remaining sign is not primarily a static representation issue; it sits at the interface of epistemics and dynamics.

**Concept hygiene.** The programme contains several distinct `\mathbf Z_2` operations (axis reversal `u\mapsto -u`, reduced naming swap `J^{01}\mapsto -J^{01}`, branch exchange/conjugation, and reduced-variable sign flips). When epistemics refers to the "last sign" or "global reversal" it means the physical forward/readout orientation choice, not an arbitrary reduced relabeling. See `kernels/discrete-symmetries.md`.

So the strongest clean formulation currently available is:

- the parent reduction fixes the two oriented candidate readout sectors
- consistency and uniqueness force direct readout to use only one of them
- the final `T1` label is fixed by the orientation chosen, or derived from an ambient scale-flow selector, as the forward observable/readout arrow

This means `T1` should not be treated as intrinsically preferred by its name. The name is conventional after the orientation is fixed. The invariant object is the reduced projector onto the sector selected by the forward readout or scale-flow direction.

This can now be stated a little more operationally. The observable arrow is not just a philosophical preference; it is the same arrow used when the reduced theory is written as a forward semigroup for `t \ge 0`. So the last global sign is best read as the requirement that:

- the sector used for direct zero-mass readout
- the sector used for projected observables
- the sector carrying forward reduced evolution

are all the same sector.

At the current stage there is also a more dynamical version of the same idea: in the phase convention where the direct locked readout branch is normalized to `\Phi_*=0`, that branch must lie on the constructive/persistent side of the transport dynamics and therefore has `\kappa_u > 0`. So the observable arrow is starting to look less like a free epistemic label and more like the readout sector singled out by the constructive branch of the reduced dynamics.

There is also a possible ambient version of the same point. If the scale/readout selector lives above the reduced `Spin(2,3)` slice, for example in a larger conformal or `AdS_5`/`SO(2,4)`-type setting, then epistemics should not demand an internal proof that `Spin(2,3)` prefers `T1`. It should demand a descent statement: the larger ambient flow induces the reduced observable projector, and the sector named `T1` is the reduced label for that induced projector.

This also shrinks the remaining epistemic burden. Route B no longer has to justify projection onto `T1` from scratch. It only has to justify one final operational rule:

- the unique direct readout channel is the constructive/persistent locked branch, hence the one with `\kappa_u > 0` in the phase-normalized gauge

If that rule is accepted, the `T1` identification is conditionally fixed by the reduction kernel already in hand. If it can be derived from the bulk, then the remaining gap between Route B and Route A largely disappears.

In other words, the same statement can be used in two roles: as an operational rule that fixes the readout orientation now, and as a derivation target that the bulk/ambient selector story may later justify.

That does not yet derive the observable arrow from pure kinematics. But it does show exactly where the last sign choice lives: at the interface between reduction, observability, forward effective evolution, and possibly a larger ambient scale-flow geometry.

---

## Coarse-graining and effective access

The epistemic role of coarse-graining is:

- the observer does not track the full microscopic excursion history through `T2`
- only projected, effective information remains available

This means that reduced dynamics is not only a technical step. It also has epistemic content:

- information is lost from the observable description
- the lost information lives in unresolved sector structure

At the kernel level, the safe claim is:

- effective observable physics is poorer than full microscopic evolution because the observational rule and coarse-graining do not retain full sector information

That is stronger and cleaner than saying "quantum uncertainty is derived."

---

## Epistemic reading of uncertainty

The framework strongly suggests the following idea:

- uncertainty-like behaviour reflects incomplete access to the full state-space dynamics

This is attractive, but the kernel should distinguish two versions.

### Safe version

Projected and coarse-grained observables inherit effective broadening or diffusion because the observer does not resolve hidden-sector excursions.

### Stronger version

Quantum uncertainty in general is nothing but hidden-sector epistemic limitation.

The second statement is much stronger and is not established by the current framework. It should therefore remain interpretive or aspirational.

---

## Epistemic claim ledger

| Claim | Role | Level | Comment |
|---|---|---|---|
| the effective observable channel is determined by zero-mass interaction | central framework proposal | 4 | new epistemic center |
| observable quantities are evaluated after projection onto the sector named `T1` | effective postulate downstream of channel selection | 4 | still central, but not necessarily primitive; invariant object is the induced projector |
| the observable projector is dynamically or ambient-geometrically forced | missing | 5 | now reduced to one final issue: derive why the unique direct readout branch must be the constructive/persistent one (`\kappa_u > 0` in phase-normalized gauge), or show that a larger ambient scale-flow selector induces the same reduced projector; with either rule, the sector may be named `T1` conditionally |
| `T2` is dynamically present but not directly observable through the zero-mass channel | framework consequence of interaction rule plus dynamics | 4 | core hidden-sector claim |
| projection and coarse-graining are distinct operations | conceptual clarification | 4 | important for logical hygiene |
| the effective observable description loses full microscopic information | derived at the reduced-description level | 4 | safe and useful |
| uncertainty-like broadening can arise from unresolved hidden-sector excursions | interpretation grounded in reduced dynamics | 5 | plausible but still broader than theorem |
| full quantum measurement theory follows from this projection rule | missing | 6 | not yet supported |

---

## Interfaces to other domains

### From statics

- the `T1/T2` split
- the projector structure
- the selected octonionic direction aligned with the massless channel

### From dynamics

- the fact that evolution occurs in the full space
- the reduced observable law after elimination of unresolved structure

### To consistency

- questions about positivity of the projected description
- questions about whether the projection rule is stable and self-consistent

### To interpretation

- the reading of hidden structure as uncertainty
- the reading of projection as limited access rather than ontic collapse

### To phenomenology

- the possibility that limited access could leave observable imprints in transport or decoherence-like behaviour

---

## Major unresolved issues

The epistemic domain still owes:

1. a deeper justification for what induces the observable projector, whether bulk dynamics or an ambient scale-flow selector
2. a sharper account of whether projection is fundamental, emergent, or only effective downstream of channel selection
3. a relation to standard quantum measurement theory
4. a more careful treatment of whether any indirect observables of `T2` exist
5. a cleaner bridge between epistemic coarse-graining and experimentally meaningful uncertainty relations

These are major conceptual obligations of the framework.

---

## Working bottom line

The epistemic spine of the project is meaningful and central.

At its safest level, it says:

1. the full model evolves in a larger space than the one directly observed
2. a selected zero-mass interaction channel defines the effective observable sector
3. in the present framework that channel is named `T1` after the readout orientation is fixed
4. the hidden sector `T2` remains dynamically active but not directly visible through that channel
5. coarse-graining over that hidden structure reduces accessible information
6. the resulting observable theory can display broadening not present in the purely projected transport law

The strongest philosophical reading, that uncertainty in general is nothing but hidden-sector epistemics, remains one layer above what the current kernel strictly establishes.
