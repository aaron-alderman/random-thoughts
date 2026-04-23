# Master Framework: `j3_oc`

## Purpose

This document applies the generic framework taxonomy to the stand-alone `j3_oc` branch.

It is the project-facing map for the branch built around the complexified exceptional Jordan object:

- `J3(C \otimes O)`
- `H3(O_C)`

For the reusable generic framework, see [0 - meta.md](../../meta/0%20-%20meta.md).

---

## One-sentence project spine

Start from `J3(C \otimes O)` as the primary ambient exceptional Jordan arena; identify what admissible sectors, stabilizers, and reduction operations it naturally carries; then ask whether a disciplined ambient-to-observable map can produce a reduced branch comparable to `spin2_3` without inserting `u`, `SU(3)`, mixing, or observability by hand.

Comparison branch:

- [1 - master framework.md](1%20-%20master%20framework.md)

---

## How claims should be read here

This branch is allowed to make a deliberate lens choice:

- use `J3(C \otimes O)` as primary

But each major claim should still be read under bounded discipline:

- what is fixed by the lens
- what options remain live nearby
- whether the branch is claiming axiom, choice, derivation, interpretation, or missing structure
- whether the maturity level of the claim is really earned

This matters especially for:

- `J3(O)` versus `J3(C \otimes O)`
- the status of the selected direction `u`
- the status of `SU(3)` inside the complexified setting
- the relation between structural ambient richness and actual observables
- the question of whether reduced `Spin(2,3)` data are obtained or merely compared against

---

## Top-down summary

The top-down reading of this branch is:

1. begin with a large exceptional Jordan ambient arena
2. use complexification to allow phase-rich and projective-like structure not already present in the minimal real branch
3. ask what substructures, orbit types, stabilizers, and admissibility conditions can live there
4. force the branch to explain how an observable reduced slice is extracted

In this reading:

- `J3(C \otimes O)` is not decoration
- it is the primary ambient candidate
- the main question is not whether the space is large, but whether it reduces in a disciplined way

---

## Bottom-up relation to `spin2_3`

The branch does not start from the reduced `Spin(2,3)` kernel, but it must still respect it as a major comparison target.

So the bottom-up relation is:

- `spin2_3` already defines a sharp reduced working branch
- `j3_oc` asks whether that type of branch can be obtained from a complexified exceptional Jordan ambient space
- until that is shown, `spin2_3` remains a target image rather than a derived consequence

The safe language is therefore:

- `spin2_3` is downstream
- `spin2_3` is not assumed as the hidden premise of this folder

---

## Bridge burden

The central task of the branch is the missing middle:

> how does one pass from `J3(C \otimes O)` to an observable reduced sector?

This burden includes at least:

1. admissibility inside the ambient Jordan arena
2. reduction to a physically relevant sector
3. reduction to an effective branch
4. extraction of an observable sector

This is formalized in:

- [0b - ambient-to-observable reduction.md](0b%20-%20ambient-to-observable%20reduction.md)

---

## Three pressure points that remain burdens unless earned

### Selected direction `u`

The branch must say whether `u` is:

- ambiently available
- induced by a stabilizer or orbit condition
- chosen as branch data
- or only imported from reduced analysis

Until that is sharpened, `u` remains a bridge burden.

### `SU(3)`

The branch must distinguish:

- ambient stabilizer structure
- reduced internal symmetry
- physical color

Until those are linked by a real reduction argument, `SU(3)` remains a bridge burden.

### Observable reduction

The branch must define where states, observables, and measurement live after reduction.

Until that is made explicit, the branch remains structurally rich but physically underdetermined.

---

## Ambient-to-observable reduction

The branch uses the schematic chain:

`A_ambient -> S_relevant -> S_reduced -> S_observable`

where the main intended operations include:

- orbit restriction
- stabilizer selection
- reality / Hermiticity condition
- quotient
- rank restriction
- positivity condition
- effective coarse-graining

The branch is not yet claiming that the exact map is derived. It is claiming that the map must exist if the branch is to count as physics rather than architecture.

---

## Methodological placement in the seven domains

### Statics / Kinematics

Primary ambient object:

- `J3(C \otimes O)` / `H3(O_C)`

Main questions:

- what substructures are admissible
- what stabilizers and orbit types exist
- how `u` and `SU(3)` could arise in the complexified setting

### Dynamics

Main questions:

- what dynamics genuinely belong to the ambient complexified Jordan branch
- what dynamics are only inherited from reduced comparison branches
- how mixing should be defined geometrically rather than only effectively

### Epistemics / Observables

Main questions:

- what counts as a state
- what counts as an observable
- what the measurement or access rule is after reduction

### Consistency / Selection

Main questions:

- what the complexified branch earns over `J3(O)`
- what reductions are disciplined rather than ad hoc
- whether a reduced `Spin(2,3)` slice can be obtained without selective matching

### Interpretation

Main questions:

- what physical meaning complexification is supposed to carry
- whether `u`, color, and mixing are structural, interpretive, or derived
- whether the ambient object is ontic, generative, or partly redundant

### Phenomenology

Main questions:

- what survives the new reduction map
- what, if anything, becomes a genuine phenomenological difference from the reduced branches

### Completion / Open Problems

Main questions:

- where the branch still lacks derivations
- what would keep `J3(O)` competitive
- what would count as branch failure

---

## Priority ordering

The most useful next tasks for this branch are:

1. make the reduction map explicit
2. define the status of `u`
3. distinguish structural `SU(3)` from physical color
4. define mixing geometrically inside the complexified branch
5. state where observables and measurement live
6. keep falsification and branch-control criteria visible

This ordering follows the external feedback and matches the branch's largest current debts.

---

## Bottom line

The `j3_oc` branch is best read as:

1. a stand-alone ambient investigation centered on `J3(C \otimes O)`
2. a deliberate reversal of the reduced-first `spin2_3` perspective
3. a test of whether the complexified exceptional Jordan setting can earn a better missing-middle story
4. a branch whose strongest open burdens are still `u`, `SU(3)`, and observable reduction

If those burdens are not improved, then the branch may stay valuable without becoming the preferred physical backbone.
