# Meta Framework

## Purpose

This document gives a reusable way to organize a research program in mathematical physics.

It separates seven orthogonal layers:

1. statics / kinematics
2. dynamics
3. epistemics / observables
4. consistency / selection
5. interpretation
6. phenomenology
7. completion / open problems

This is the generic version, independent of any one project.

For a project-specific application, see [00 - master framework.md](C:/Users/aaron/Desktop/liberalism/god-thoughts/kenosis/random-thoughts/physics/candidate%20papers/00%20-%20master%20framework.md).

---

## 1. Statics / Kinematics

This layer answers:

- what are the fundamental mathematical objects
- what spaces, algebras, groups, and representations exist
- how those objects decompose before time evolution is introduced

Typical examples:

- symmetry groups
- representation theory
- internal spaces
- algebraic decompositions
- geometric background structure

This is the layer of form.

---

## 2. Dynamics

This layer answers:

- how the objects evolve
- what equations of motion, actions, or generators are assumed
- how different sectors interact

Typical examples:

- Hamiltonians
- field equations
- transport laws
- interaction terms
- effective reduced equations

This is the layer of motion.

---

## 3. Epistemics / Observables

This layer answers:

- what is physically observable
- what is hidden, coarse-grained, or inaccessible
- how formal structure is related to measurement or interaction

Typical examples:

- observable algebras
- projection rules
- measurement postulates
- coarse-graining maps
- effective observer-dependent descriptions

This is the layer of access.

It is often neglected, but it is conceptually distinct from both kinematics and dynamics.

---

## 4. Consistency / Selection

This layer answers:

- what the framework allows
- what it forbids
- what becomes forced once the setup is fixed

Typical examples:

- anomaly cancellation
- positivity
- stability
- compatibility of symmetries
- uniqueness statements
- no-go theorems

This is the layer of constraints.

---

## 5. Interpretation

This layer answers:

- what the mathematics is taken to mean physically
- what conceptual reading is given to the formal structures

Typical examples:

- identifying a parameter with mass
- reading hidden structure as uncertainty
- treating a symmetry-breaking choice as physically meaningful

This is the layer of meaning.

Interpretation is essential, but it should not be confused with derivation.

---

## 6. Phenomenology

This layer answers:

- what the framework predicts
- what observable consequences could follow
- how the framework might touch experiment or established physics

Typical examples:

- scaling laws
- effective coefficients
- particle content
- deviations from standard theories
- bounds and signatures

This is the layer of empirical contact.

---

## 7. Completion / Open problems

This layer answers:

- what remains missing
- what has not yet been derived
- where the current framework is still incomplete

Typical examples:

- missing derivations
- absent field-theoretic completion
- unresolved uniqueness questions
- uncomputed observables
- lack of empirical bounds

This is the layer of honest incompleteness.

---

## The second axis: logical status

Every claim in a framework should also be tagged by status.

### Main statuses

- `Axiom/Postulate`
- `Choice`
- `Derived`
- `Interpretation`
- `Missing`

These statuses cut across all seven categories.

For example:

- a symmetry group may be an `Axiom` inside `Statics`
- a preferred direction may be a `Choice` inside `Statics`
- a reduced equation may be `Derived` inside `Dynamics`
- an identification of a parameter with mass may be `Interpretation`
- an experimental bound may still be `Missing` inside `Phenomenology`

So every serious framework can be organized by two axes:

1. category
2. logical status

---

## The third axis: claim maturity

Every claim should also be tagged by how mature or defensible it currently is.

### Claim maturity scale

| Level | Name | Meaning |
|---|---|---|
| 1 | Trivial | Immediate, definitional, or too elementary to need defense. |
| 2 | Solid established | Broadly accepted background that usually does not need citation. |
| 3 | Established | Known and defensible, but specialized enough that a paper should normally cite it. |
| 4 | Being established in this paper | A claim the current paper is actively deriving, proving, or defending. |
| 5 | Plausible but future work | A reasonable extension, interpretation, or conjectural consequence not yet fully established. |
| 6 | Significant issue | A genuine weakness, unresolved problem, or point where the framework does not yet support the claim. |

### Why this matters

This scale is not the same as logical status.

- A claim can be `Derived` in status and still be level `4` if the current paper is the one establishing it.
- A claim can be an `Interpretation` and still be level `5` if it is plausible but not yet demonstrated.
- A claim that is `Missing` will often sit naturally at level `6`.

This gives a practical writing rule:

- levels `1-3` are safe inputs
- level `4` is what the present paper must actually earn
- level `5` belongs in discussion, outlook, or future work
- level `6` must be acknowledged honestly as a real issue

So the full framework has three axes:

1. category
2. logical status
3. claim maturity

---

## The generic matrix

| Category | Main question |
|---|---|
| Statics / Kinematics | What exists? |
| Dynamics | How does it evolve? |
| Epistemics / Observables | What is seen or accessible? |
| Consistency / Selection | What is allowed, forbidden, or forced? |
| Interpretation | What does it mean physically? |
| Phenomenology | What does it predict? |
| Completion / Open problems | What is still missing? |

| Status | Meaning |
|---|---|
| Axiom/Postulate | Assumed at the start |
| Choice | Selected inside the framework |
| Derived | Forced by the setup |
| Interpretation | Physical reading of the result |
| Missing | Not yet established |

| Maturity level | Meaning |
|---|---|
| 1 | Trivial |
| 2 | Solid established |
| 3 | Established and typically cited |
| 4 | Being established in this paper |
| 5 | Plausible but future work |
| 6 | Significant issue |

---

## Practical use

This taxonomy is useful for at least four tasks:

1. writing papers without overclaiming
2. separating strong results from suggestive ideas
3. deciding which journal fits which piece of work
4. tracking what the framework still owes

The most common mistake in ambitious programs is to blur:

- assumptions and theorems
- choices and necessities
- interpretation and proof
- suggestive consequences and actual predictions

This framework exists to prevent that.

---

## From framework to paper

The framework becomes practically useful when it is turned into a paper kernel.

The paper kernel is the minimal logical structure that must be clear before drafting begins.

Before writing a paper, identify:

1. which layer the paper belongs to
2. which claims are being established in this paper
3. which claims are only background inputs
4. which claims are interpretation only
5. which claims belong to future work
6. which unresolved issues must be acknowledged

If these are not clear, the paper is not ready.

### Step 1. Choose the paper's home layer

Every paper should have a primary home:

- `Statics / Kinematics`
- `Dynamics`
- `Epistemics / Observables`
- `Consistency / Selection`
- `Interpretation`
- `Phenomenology`

It may touch adjacent layers, but only one or two should be central.

Rule:

- the title, abstract, and main theorem or result should all live in the same home layer

If they do not, the paper is probably trying to do too much.

### Step 2. Build the claim list

List every meaningful claim in the draft and tag each one by:

- `Category`
- `Logical status`
- `Maturity`

Rule:

- only level `4` claims are what the paper must truly earn

Everything else must be treated differently.

### Step 3. Sort the claims into paper roles

#### Background / setup

Use:

- level `1`
- level `2`
- level `3`

These belong in setup, notation, and literature-supported background.

#### Core result

Use:

- level `4`

These belong in the main derivation, theorem, proposition, and headline abstract claim.

#### Interpretation

Use:

- claims with logical status `Interpretation`

These belong in discussion and concluding interpretation. They should not carry the proof burden of the paper.

#### Future work / plausible extensions

Use:

- level `5`

These belong in discussion, outlook, and the end of the conclusion. They should not be sold as established outcomes.

#### Limitations / issues

Use:

- level `6`

These belong in assumptions, limitations, and conclusion. They must be stated honestly.

### Step 4. Define the proof burden

For each level `4` claim, specify:

1. exact statement
2. assumptions needed
3. derivation or proof path
4. what would count as establishing it
5. what still remains unproved even after success

Rule:

- if a claim cannot be written this way, it is probably not yet level `4`

It is probably level `5`.

### Step 5. Write the abstract from the kernel

A clean abstract usually has five moves:

1. one-sentence problem statement
2. one-sentence setup
3. one-sentence central level `4` result
4. one-sentence conditions or regime of validity
5. one-sentence interpretation or consequence

Discipline:

- background claims should be brief
- level `4` claims should be explicit
- level `5` claims should not be sold as results
- level `6` issues should not be hidden if they materially limit the result

### Step 6. Write the introduction from the kernel

The introduction should answer:

1. what problem is being addressed
2. what layer the paper belongs to
3. what is assumed as background
4. what exact result is established here
5. what is not established here

A good default structure is:

- paragraph 1: problem and motivation
- paragraph 2: setup and scope
- paragraph 3: exact contribution
- paragraph 4: what remains outside scope

### Step 7. Write the body in proof order

The body should follow the dependency structure of the level `4` claims.

Typical order:

1. setup and notation
2. assumptions or postulates
3. intermediate lemmas or reductions
4. main derivation or theorem
5. regime of validity
6. interpretation

Rule:

- write in the order required to make the result checkable, not in the order of what sounds most exciting

### Step 8. Write the discussion properly

The discussion is where different claim types are separated cleanly.

It should usually contain:

- what was established
- what it suggests
- what remains open
- how it relates to the larger program

The discussion is the right home for:

- interpretation
- plausible extension
- broader synthesis

It is the wrong home for pretending something was derived when it was not.

### Step 9. Match the paper to the venue

Different venues tolerate different kernels.

Short conceptual letter:

- one narrow level `4` claim
- minimal setup
- clear limitations

Mathematical physics paper:

- sharper assumptions
- more explicit derivation
- careful operator or structural control

Phenomenology paper:

- actual predictions or bounds
- not just suggestive interpretation

Rule:

- a paper should only be sent to a venue whose standards match the maturity of its core claim

### Step 10. Final pre-writing checklist

Before drafting, confirm:

- the home layer is clear
- the level `4` claims are explicit
- the proof burden for each level `4` claim is known
- level `1-3` claims are separated as background
- level `5` claims are moved to future work
- level `6` issues are acknowledged
- the venue matches the maturity of the result

If any of these fail, do not write the paper yet. Fix the kernel first.

### Minimal kernel worksheet

Use this block before writing any paper:

- working title:
- primary layer:
- secondary layer if any:
- level `4` claim 1:
- level `4` claim 2:
- level `4` claim 3:
- level `1-3` background claims:
- level `5` discussion claims:
- level `6` issues to acknowledge:
- assumptions:
- main derivation path:
- regime of validity:
- what is not proved:
- target venue:
- why this kernel matches that venue:

---

## Crisp summary

The shortest reusable version is:

1. `Statics` says what structures exist.
2. `Dynamics` says how they evolve.
3. `Epistemics` says what is observed.
4. `Consistency` says what is allowed or forced.
5. `Interpretation` says what it means.
6. `Phenomenology` says what it predicts.
7. `Completion` says what is missing.

That is a fuller and cleaner map than a simple split between statics and dynamics.

To turn that framework into a paper:

1. choose the paper's home layer
2. identify the level `4` claims it must earn
3. move level `1-3` claims to background
4. move level `5` claims to discussion and future work
5. state level `6` issues honestly

Once that is done, writing becomes mostly a matter of execution and presentation.
