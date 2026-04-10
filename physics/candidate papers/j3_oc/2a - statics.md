# Statics Kernel

## Purpose

This document is the static or kinematic source text for the `j3_oc` branch.

Its job is to say:

- what the ambient mathematical objects are
- what substructures are being treated as admissible
- what stabilizers and distinguished directions may arise
- what is fixed by the branch choice and what remains open

This file is not the place to smuggle in reduced `spin2_3` conclusions as if they were already derived here.

---

## Scope

This file covers:

- the ambient role of `J3(C \otimes O)` / `H3(O_C)`
- candidate real, Hermitian, or positive substructures
- candidate stabilizers and symmetry reductions
- where a selected direction `u` could enter
- where `SU(3)` could arise in the complexified setting

This file does not cover:

- reduced transport equations
- coarse-grained observability
- the full phenomenology of color or generations

---

## Domain inputs

### Structural input

The branch starts from:

1. the complexified exceptional Jordan object `J3(C \otimes O)`
2. its role as a larger ambient alternative to `J3(O)`
3. the possibility that physically relevant sectors arise only after admissibility and reduction conditions are imposed

### Static branch choice

The working branch is:

- use `J3(C \otimes O)` as primary ambient structure
- treat `J3(O)` as a nearby comparator, not as the default base object
- ask what real or Hermitian slices matter only after starting from the complexified arena

---

## Minimal static setup

The safe static claim is:

- `J3(C \otimes O)` is a larger ambient Jordan arena than `J3(O)`

What that larger ambientity is meant to buy is not yet a theorem, but the branch is using it to ask for:

- more explicit phase-carrying structure
- a more flexible orbit language
- a clearer place for ambient state-space geometry
- a possible route to later observable reduction that is not already fixed by the real branch

At this level, the branch should resist overclaiming:

- larger ambient room does not by itself imply better physics

---

## Admissible substructures

The first static issue is not "what is everything in the ambient space?" but:

> what kind of substructure is even admissible as candidate physical data?

The main live candidates are:

- real slices inside the complexified ambient object
- Hermitian restrictions
- positivity-compatible sectors
- orbit classes stable under selected subgroup actions
- sectors singled out by a chosen stabilizer or preferred direction

The branch does not yet claim that one of these has been uniquely selected.

The safe static position is:

- admissibility itself is part of the bridge problem

The current branch default is:

1. begin with Hermitian or reality-compatible admissibility
2. sharpen with rank or orbit control
3. add stabilizer-sensitive refinement only when it constrains later `u` or `SU(3)` work rather than merely reproducing the desired answer

---

## Candidate role of `u`

Inside this branch, the selected direction `u` should not be treated as already settled.

The main static options are:

1. `u` is inserted as branch data
2. `u` is selected by a stabilizer condition
3. `u` is induced only after passing to an admissible real or Hermitian slice
4. `u` is not fundamental at the ambient level, but only appears in the reduced image

The branch is interested in options `2-4` more than option `1`, because those would actually improve on the reduced branch's present proof burden.

Safe statement:

- the status of `u` is unresolved inside the static ambient branch

The best current sharpening, without overclaiming, is:

- treat `u` as reduction-selected branch data constrained by admissibility
- require the branch to explain at least why `u` is selected up to the right orbit or stabilizer class
- use `u^\perp` as the candidate carrier of the residual `C^3`-type internal geometry if such a selection succeeds

---

## Candidate role of `SU(3)`

The branch also needs a disciplined static reading of `SU(3)`.

The main possibilities are:

1. `SU(3)` appears as stabilizer data of a selected direction or structure inside the ambient complexified arena
2. `SU(3)` appears only after restricting to a more controlled real or Hermitian sector
3. `SU(3)` survives as an effective reduced internal symmetry
4. `SU(3)` further survives as candidate physical color

The static domain can safely address `1-2`.

The move to `3-4` requires later reduction and consistency work.

So the safe static statement is:

- the branch is looking for a clean structural route to `SU(3)`, but physical color is not yet earned here

The best current sharpening is:

- once `u` is fixed or selected, the first useful `SU(3)` should be read as the stabilizer of the residual internal geometry associated with `u^\perp`
- only later reduction and observable survival tests can justify stronger color language

---

## `J3(O)` versus `J3(C \otimes O)` in static terms

The static comparison should be framed carefully.

### `J3(O)`

Strengths:

- simpler
- more controlled
- already natural for three-slot organization

Costs:

- may leave phase-rich or projective-like structure external to the organizer
- may not obviously carry the ambient room this branch wants

### `J3(C \otimes O)`

Strengths:

- ambient enlargement
- more natural place to ask for complex phase structure
- more obvious room for state-space style language

Costs:

- larger proof burden
- larger admissibility burden
- greater risk of importing physical claims without disciplined reduction

The static branch is therefore not claiming that complexification is automatically superior. It is claiming that it is worth testing as the primary ambient lens.

---

## Static claim ledger

| Claim | Status | Maturity | Comment |
|---|---|---|---|
| `J3(C \otimes O)` is a mathematically available complexified exceptional Jordan object | established input | 3 | ambient starting object |
| `J3(C \otimes O)` should be treated as primary in this branch | choice | 4 | local lens commitment |
| admissibility conditions are part of the static bridge burden | structural consequence of branch size | 4 | central for control |
| Hermitian-first then rank/orbit admissibility is the current branch default | choice | 4 | provisional but operational |
| a selected direction `u` may arise through ambient restriction rather than primitive insertion | plausible branch target | 5 | not yet derived |
| an `SU(3)`-type stabilizer pattern may emerge structurally inside the ambient branch | plausible structural target | 5 | not yet physical color |
| complexification is physically necessary | unresolved strong claim | 6 | not yet earned |

---

## Interfaces to other domains

### To dynamics

- admissible sectors on which ambient dynamics could act
- candidate distinguished directions or stabilizers
- possible reduced images to compare with `spin2_3`

### To epistemics

- candidate state-space objects after admissibility restriction
- candidate observables before final observable filtering

### To consistency

- whether the ambient enlargement earns anything over `J3(O)`
- whether the selected reductions are disciplined

---

## What this domain does not yet settle

The static domain does not yet settle:

- whether `u` is derived
- whether `SU(3)` is physical color
- whether `Spin(2,3)` is recoverable by a clean reduction
- whether three-generation interpretations survive unchanged from the real branch

Those remain cross-domain burdens.

---

## Working bottom line

The static spine of `j3_oc` is:

1. start from `J3(C \otimes O)` as ambient exceptional Jordan structure
2. treat admissibility as part of the problem, not a hidden convenience
3. look for a controlled route to `u` and `SU(3)` inside the complexified setting
4. refuse to treat reduced `spin2_3` structure as already inherited

That is enough to make the branch statically meaningful without overstating its achievements.
