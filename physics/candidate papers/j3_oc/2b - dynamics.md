# Dynamics Kernel

## Purpose

This document is the dynamics source text for the `j3_oc` branch.

Its job is to say:

- what kinds of dynamics genuinely belong to the complexified exceptional Jordan ambient branch
- what dynamic notions are only imported from reduced comparison branches
- how mixing should be framed if the branch is to add anything real

This file is deliberately narrower than the `spin2_3` dynamics file because the reduced transport story is not yet derived here.

---

## Scope

This file covers:

- ambient versus reduced dynamic roles
- what counts as a genuine `j3_oc` dynamic question
- the branch-specific status of mixing
- how reduced `spin2_3` dynamics should be used here

This file does not cover:

- a finished transport model
- Lindblad derivations
- advection-diffusion claims as if they already followed from `J3(C \otimes O)`

---

## Inputs from statics

The dynamical branch assumes:

1. `J3(C \otimes O)` is the ambient starting object
2. physically relevant sectors arise only after admissibility and reduction
3. the status of `u`, `SU(3)`, and the reduced branch is not yet fully settled

So the primary dynamical question becomes:

> what form of motion or interaction can be attributed to the ambient branch before one collapses back to reduced effective models?

---

## Ambient-versus-reduced dynamic distinction

The most important discipline in this file is:

- ambient dynamics are not the same thing as reduced `spin2_3` dynamics

The current reduced branch already contains useful material on:

- `T1/T2` sector evolution
- zero-mass channel privilege
- effective mixing
- reduced Markovian dynamics
- diffusion scaling

Those can be reused here only in one of three ways:

1. as downstream target behavior
2. as comparison material
3. as provisional effective image after reduction

They should **not** be stated here as already derived from `J3(C \otimes O)`.

---

## Main dynamical burdens of `j3_oc`

The ambient branch owes at least four dynamical clarifications.

### D1. What evolves?

The branch must say what the fundamental evolving objects are:

- Jordan elements
- selected orbit data
- reduced sector representatives
- expectation-type functionals on the admissible state space

This remains open.

### D2. What counts as interaction?

The branch must say what it means, internally, for sectors to interact.

Until that is defined, "mixing" remains imported vocabulary.

### D3. What is reduced and what is ambient?

The branch must distinguish:

- ambient motion
- reduction operations
- observable coarse-graining

If those are blurred, the branch will look physically richer than it really is.

### D4. What becomes the reduced effective image?

If the branch is to subsume `spin2_3`, it must eventually show how a reduced effective dynamic picture could emerge after the relevant reductions.

---

## Mixing in this branch

The feedback correctly raises mixing as a central unresolved issue.

Inside `j3_oc`, the branch should treat the word "mixing" as a placeholder until a geometric meaning is chosen.

The main candidate meanings are:

- departure from a preferred orbit or stabilizer-preserving sector
- failure of alignment with a selected direction `u`
- coupling between retained and discarded sectors under reduction
- motion between visible and hidden sectors after a chosen observable restriction

The safe current statement is:

- the branch does not yet have a uniquely settled geometric definition of mixing

That is a real open problem, not an embarrassment.

---

## Safe dynamic statements at present

The branch can safely say:

1. a genuine ambient branch must distinguish ambient evolution from reduction
2. current `spin2_3` mixing and transport results are usable as downstream comparison targets
3. the `j3_oc` branch still owes its own definition of mixing and interaction

The branch should not yet say:

- that Lindblad-type reduced dynamics follow from `J3(C \otimes O)`
- that the `T1/T2` block picture is already an ambient Jordan consequence
- that mass-like mixing has already been geometrically derived here

---

## Dynamic claim ledger

| Claim | Status | Maturity | Comment |
|---|---|---|---|
| reduced `spin2_3` dynamics can be used as downstream comparison data | working methodological rule | 4 | important separation principle |
| ambient motion, reduction, and observability must be distinguished | framework requirement | 4 | central bridge discipline |
| mixing should be given a geometric meaning inside the complexified branch | branch target | 5 | not yet complete |
| the reduced `T1/T2` transport story is already derived from `J3(C \otimes O)` | missing | 6 | not yet true |

---

## Interfaces to other domains

### From statics

- admissible sectors
- candidate stabilizers
- candidate selected directions

### To epistemics

- candidate distinction between ambient motion and observable access

### To consistency

- whether the proposed dynamics are genuinely ambient or only borrowed

### To interpretation

- what mixing is taken to mean physically

---

## Major unresolved issues

The dynamics domain still owes:

1. a statement of the fundamental evolving objects
2. a branch-internal definition of interaction
3. a branch-internal definition of mixing
4. a disciplined route from ambient motion to reduced effective dynamics

These are the main reasons this file must remain modest.

---

## Working bottom line

The dynamic spine of `j3_oc` is currently mostly a discipline statement:

1. do not overclaim reduced results as ambient derivations
2. use `spin2_3` as a target image where useful
3. make "mixing" geometric before making it physical
4. keep ambient evolution, reduction, and observability conceptually separate

That is the right starting point for this branch.
