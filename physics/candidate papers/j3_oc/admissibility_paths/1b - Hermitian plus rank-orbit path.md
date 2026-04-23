# Hermitian Plus Rank-Orbit Path

## Purpose

This note records the Hermitian-plus-rank/orbit admissibility path for `j3_oc`.

Its core question is:

> what if admissibility is defined not only by Hermitian compatibility, but also by selecting particular rank or orbit sectors as physically meaningful?

---

## Core rule

Start from
$$
X \in J3(C \otimes O)
$$
and require both:
$$
X = X^\dagger,
\qquad
\mathrm{rank}(X) \in \mathcal{R}_*
$$
or, more generally,
$$
X \in \mathcal{O}_*
$$
for a chosen orbit class `O_*`.

In branch language, this is the path:

`X -> X_H -> X_{H,r}`

with `X_{H,r}` already more selective than the pure Hermitian-first path.

The current working interpretation is:

- `X_H` is the weak baseline
- `X_{H,r}` is the active strong admissible target

So this note should be read as the branch's current main admissibility candidate, not just one option among equals.

---

## Why it is attractive

- it is more selective than raw Hermitian restriction
- it gives the branch a more geometric way to talk about distinguished sectors
- it helps move admissibility from broad cleanup toward actual structure selection
- it gives the reduction map more content before stabilizer-sensitive conditions are introduced

---

## What it buys

- a cleaner basis for later reduction
- a more explicit way to discuss branch-relevant sectors
- a stronger comparison against `J3(O)` than Hermitian-first alone
- a better chance of making later `u` or `SU(3)` sharpening non-arbitrary

---

## Current working candidate

The strongest current non-overclaiming version of this path is:

1. first pass to a Hermitian or reality-compatible representative
2. then restrict to a chosen rank set `R_*` or orbit class `O_*`
3. only after that ask what residual structures survive into later reduction

In practical branch language:

- this path is trying to make `X_{H,r}` the first genuinely informative admissible object

That is stronger than a cleanup step and weaker than a full reduction theorem.

---

## Main decision questions

For this path to become operational, later work should ask:

1. which rank classes are serious candidates, and why?
2. which orbit classes are serious candidates, and why?
3. does the chosen class improve the `u` story at all?
4. does the chosen class preserve any candidate residual symmetry relevant to `SU(3)`?
5. does the chosen class make later reduction to a `Spin(2,3)`-type image any cleaner?

These questions are the real test of whether the path is informative rather than only narrower.

---

## Current explicit candidate

The current best provisional candidate for the main path is:

- Hermitian admissibility plus a distinguished low-rank sector
- most concretely, a rank-`1` Hermitian or projective-like orbit candidate

In shorthand:

$$
X = X^\dagger,
\qquad
\mathrm{rank}(X)=1
$$
or the corresponding admissible rank-`1` orbit class.

This should be read as:

- a working `Choice`
- not yet a theorem
- and not yet the only viable option

The reason to test rank `1` first is not that it is already known to be physically correct.

The reason is that it is the cleanest minimal candidate if the branch wants:

- a disciplined first distinguished sector
- a projective- or state-like interpretation
- a strong contrast with leaving the ambient arena too large

---

## Why rank `1` is the first test

Rank `1` is the best first explicit test candidate because it is:

- the minimal nontrivial rank choice
- the easiest way to make the admissibility path concrete
- the clearest place to ask whether the branch gains a projective or state-like geometry
- the least committal rank choice that still forces the branch to stop talking only schematically

This does **not** mean:

- rank `1` is already the physical answer
- higher-rank sectors are ruled out
- the branch has already earned a state-space interpretation

It only means rank `1` is the best first falsifiable test case.

---

## What rank `1` should change if it is useful

If rank `1` is the right first candidate, it should improve at least one of the following:

1. make the admissible sector more visibly projective or state-like
2. narrow the range of possible `u` behavior
3. preserve a cleaner candidate residual symmetry story for `SU(3)`
4. make later reduction to a smaller effective branch less arbitrary

If it does none of these, the rank-`1` test should be treated as a useful failure rather than a hidden premise.

---

## Rank-`1` test against `u`

The first question is whether a rank-`1` Hermitian sector does anything useful for the `u` story.

The strongest hope is not yet:

- that rank `1` fully derives `u`

The strongest reasonable test is:

- does rank `1` reduce the freedom in how `u` can appear?

The candidate gains would be:

1. rank `1` narrows the admissible sectors enough that `u` is no longer completely arbitrary
2. rank `1` makes it easier to talk about `u` up to the right orbit or stabilizer class
3. rank `1` makes the statement about `u^\perp` as residual internal carrier more disciplined

The main risk is:

- rank `1` may still leave `u` entirely external to the admissibility choice

So the actual test here is modest:

- does rank `1` improve the status of `u` from unconstrained insertion to at least constrained branch data?

If not, rank `1` is still usable, but weaker than hoped.

---

## Rank-`1` test against `SU(3)`

The second question is whether a rank-`1` Hermitian sector sharpens the `SU(3)` story at all.

The strongest hope is:

- rank `1` leaves a cleaner residual internal geometry on which a candidate `SU(3)` action can later be tracked

That would still be only a structural gain, not physical color.

The key questions are:

1. does rank `1` preserve a cleaner candidate stabilizer picture than a looser admissible sector?
2. does rank `1` make it easier to state what symmetry survives after admissibility?
3. does rank `1` reduce the chance that `SU(3)` is being inserted only after the fact?

The main risk is:

- rank `1` may be too thin to do more than support a projective reading while leaving the `SU(3)` burden basically unchanged

So the real test is:

- does rank `1` help separate ambient stabilizer language from later reduced internal symmetry language?

If not, it remains admissible but not especially illuminating for color.

---

## Rank-`1` test against reduced `Spin(2,3)`

The third question is whether rank `1` helps the reduced-branch story.

The strongest claim available at this stage is not:

- rank `1` yields `Spin(2,3)`

The stronger available question is:

- does rank `1` make a later reduction to a `Spin(2,3)`-type image less arbitrary?

Possible gains would be:

1. a cleaner candidate reduced sector
2. a smaller set of admissible branch data to quotient or project
3. a clearer distinction between ambient data and effective reduced data

The main risk is:

- rank `1` may be helpful for state-like language without telling us much about the reduced spacetime branch

So the true test is:

- does rank `1` help identify a more disciplined `S_relevant -> S_reduced` step?

If not, then the path remains a good admissibility candidate but not yet a better reduction bridge.

---

## Provisional score of the rank-`1` test

At the current stage, the fairest provisional reading is:

- `u`: possible modest gain, but not yet strong
- `SU(3)`: possible structural gain, but not yet clearly strong
- reduced `Spin(2,3)`: still speculative

So rank `1` currently looks best as:

- a clean first falsifiable test case

not yet as:

- the obviously correct final admissible sector

That is still a useful outcome, because a good first test case should be strong enough to clarify the next move even if it does not win outright.

---

## Nearby alternative to keep in view

The nearest serious alternative is:

- a Hermitian rank-`2` or broader non-minimal orbit sector

That should remain in view for one specific reason:

- if rank `1` is too thin to sharpen `u`, `SU(3)`, or reduced-branch selection, then the next natural comparison is not "give up on rank/orbit control," but "ask whether a less minimal admissible sector is needed"

---

## Current comparison candidate

The nearest comparison case should now be treated explicitly as:

- Hermitian rank-`2` admissibility
- or, more cautiously, a non-minimal orbit sector whose first motivation is that rank `1` may be too thin

In shorthand:

$$
X = X^\dagger,
\qquad
\mathrm{rank}(X)=2
$$
or the corresponding admissible non-minimal orbit class.

This is not yet the new default.

It is the nearest serious comparison case because it changes only one thing:

- it relaxes the minimality of rank `1` without abandoning the rank/orbit strategy itself

---

## Why rank `2` is the right next comparison

Rank `2` is the cleanest next comparison because it may:

- preserve more internal structure than rank `1`
- leave more room for a nontrivial residual symmetry story
- give the branch a better chance of sharpening `u` or `SU(3)` without jumping all the way back to a broad admissible sector

The cost is:

- it also weakens the minimal, projective-like simplicity of rank `1`

So the actual comparison is not:

- minimal versus arbitrary

but:

- minimal rank `1` versus slightly richer rank `2`

---

## Rank-`2` test against `u`

If rank `1` is too thin, rank `2` may help by leaving a richer admissible carrier on which a preferred direction can become less arbitrary.

The candidate gain is:

- rank `2` may constrain `u` more effectively by retaining more internal geometric structure before reduction

The candidate risk is:

- rank `2` may add room without adding real selection

So the comparison question is:

- does rank `2` improve the `u` story in a way rank `1` cannot, or does it merely broaden the admissible arena again?

---

## Rank-`2` test against `SU(3)`

Rank `2` may be the stronger candidate if the `SU(3)` story needs a thicker residual internal geometry than the rank-`1` path preserves.

The candidate gain is:

- rank `2` may preserve a more robust candidate stabilizer or residual symmetry structure

The candidate risk is:

- rank `2` may look better only because it is looser, not because it is more disciplined

So the comparison question is:

- does rank `2` sharpen the staged `SU(3)` story, or does it only postpone the need to explain it?

---

## Rank-`2` test against reduced `Spin(2,3)`

Rank `2` may help the reduced-branch story if a less minimal admissible sector is actually needed before projection or quotient can produce a credible reduced image.

The candidate gain is:

- rank `2` may support a more informative `S_relevant -> S_reduced` step than rank `1`

The candidate risk is:

- rank `2` may simply carry more baggage into reduction without making the reduced image any cleaner

So the real question is:

- does rank `2` make the reduced branch less arbitrary than rank `1`, or only less sharp?

---

## Rank-`1` versus rank-`2` comparison

At the current stage, the cleanest comparison is:

| Candidate | Main strength | Main risk |
|---|---|---|
| rank `1` | minimal, falsifiable, projective-like | may be too thin |
| rank `2` | richer internal structure | may regain looseness too quickly |

The actual branch test should therefore be:

1. if rank `1` sharpens at least one major burden, keep it primary
2. if rank `1` is too thin across all major burdens, promote rank `2` as the next serious candidate
3. do not promote rank `2` merely because it is broader

---

## Comparative scorecard

The branch now needs a more explicit comparison than "minimal" versus "richer."

The best current scorecard is:

| Criterion | rank `1` | rank `2` | Current reading |
|---|---|---|---|
| `Discipline` | strong | medium | rank `1` wins because it makes the sharpest first admissibility cut |
| `u` leverage | low-to-medium | medium | rank `2` may carry more structure, but has not yet shown cleaner selection |
| `SU(3)` leverage | low-to-medium | medium | rank `2` may support a thicker residual symmetry story, but not yet in a disciplined way |
| `Reduction` leverage | medium | medium | neither candidate clearly wins yet |
| `Observable viability` | medium | medium | both are still provisional at this stage |
| `Ad hoc risk` | lower | higher | rank `2` is easier to justify only by breadth |
| `Comparative value against J3(O)` | medium | medium | both remain live, but neither has yet earned a decisive complexified advantage |

This scorecard is deliberately qualitative.

That is appropriate here because the branch is still comparing admissibility postures, not measuring a finished derived structure.

---

## Current reading of the scorecard

The fairest present reading is:

- rank `1` remains the primary test because it is the cleanest disciplined first cut
- rank `2` remains the nearest serious escalation because it may preserve more internal structure where rank `1` proves too thin
- the burden of proof currently lies with rank `2`, not rank `1`

So the question is no longer:

- which rank looks richer?

It is:

- which rank improves at least one bridge burden without paying too much in looseness?

On that standard, rank `1` still has the better current balance.

---

## Provisional decision rule

The current decision rule between rank `1` and rank `2` should be:

- prefer rank `1` if it gives any real gain in `u`, `SU(3)`, or reduction discipline
- move to rank `2` only if rank `1` repeatedly proves too thin rather than genuinely informative

That keeps the branch conservative without becoming rigid.

---

## Where it is weak

- it may still organize sectors without explaining which one is physically preferred
- it may improve geometric control without yet improving the status of `u`
- it may narrow the field without yet connecting structural `SU(3)` to anything physical
- the choice of rank or orbit class can become arbitrary if not motivated clearly

---

## Success condition

This path succeeds if the selected rank/orbit control does at least one of the following:

- narrows the admissible sectors enough to improve the `u` story
- preserves the right candidate residual symmetry for the `SU(3)` story
- makes the later reduction to a `Spin(2,3)`-type image more disciplined

The stronger version of success would be:

- one candidate rank/orbit class emerges as the current working default because it improves more than one bridge burden at once

---

## Failure condition

This path fails if:

- the chosen rank/orbit class is selected only because it gives the answer we wanted
- the extra control does not sharpen any of the branch burdens
- it produces a narrower admissible sector but no better bridge to reduced or observable structure

It also fails if:

- every plausible rank/orbit choice leaves `u`, `SU(3)`, and observable extraction equally unconstrained

In that case the path is still cleaner than Hermitian-first, but not yet stronger in a branch-defining sense.

---

## Minimum evidence this path should aim to produce

Before this path can count as more than a promising posture, it should be able to supply:

1. one explicit candidate `R_*` or `O_*`
2. one reason that candidate is preferred over a nearby alternative
3. one statement about what that choice changes for `u`, `SU(3)`, or later reduction

The current candidate proposed for this burden is:

- rank `1` Hermitian / projective-like admissibility
- with rank `2` retained as the nearest escalation test if rank `1` proves too thin in practice

That is a manageable proof burden for the next stage.

---

## Handoff to stabilizer-sensitive refinement

This path should remain primary unless and until a stabilizer-sensitive refinement can satisfy two conditions:

1. it acts on top of a grounded `X_{H,r}` sector rather than replacing it from scratch
2. it sharpens a real branch burden that `X_{H,r}` alone leaves underdetermined

This keeps the refinement path subordinate to the main path unless it earns more.

---

## Best current verdict

This is the strongest candidate for the main admissibility backbone.

It is still not sufficient by itself, but it is the best middle path between:

- a baseline that is too weak
- and a stabilizer-sensitive path that risks being too engineered

So the present branch should:

- work this path first
- measure explicitly where it succeeds and where it stalls
- only then decide whether the fallback or refinement paths need to take over

---

## Relation to the main branch

This path matches the current default ordering in:

- [0b - ambient-to-observable reduction.md](../0b%20-%20ambient-to-observable%20reduction.md)

and is the strongest candidate to become the branch's actual central admissibility rule if later work supports it.
