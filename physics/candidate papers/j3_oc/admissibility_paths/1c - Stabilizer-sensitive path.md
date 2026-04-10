# Stabilizer-Sensitive Path

## Purpose

This note records the stabilizer-sensitive admissibility path for `j3_oc`.

Its core question is:

> what if admissibility is defined partly by whether a candidate sector preserves or exposes the stabilizer structure needed for the `u` and `SU(3)` story?

---

## Core rule

Start from an ambient candidate
$$
X \in J3(C \otimes O)
$$
and keep it only if the admissible sector retains the right kind of stabilizer data for later branch burdens.

In practical language:

- admissibility is not only about reality or rank
- it is also about whether the sector can support the relevant `u` and `SU(3)` geometry

This path is best read as a refinement stage after more conservative admissibility cuts, not as a free-floating first move.

Its present role is:

- parallel live refinement

not:

- primary backbone

The current branch posture is therefore:

- keep this path alive in parallel
- do not let it replace the main `Hermitian + rank/orbit` path without earning that promotion

---

## Why it is attractive

- it directly targets the real burdens of the branch
- it gives `F_adm` a chance to do physical work rather than only cleanup
- it offers the clearest route to linking admissibility with both `u` and `SU(3)` at once

---

## What it buys

- a more branch-relevant notion of admissibility
- a better chance of making the same reduction step sharpen multiple burdens at once
- a natural route to asking whether `u` and the relevant `SU(3)` emerge together

---

## Control rules

This path should stay alive only under explicit discipline.

The current control rules are:

1. it must act on top of an already grounded admissible sector
2. it must not introduce a preferred `u` or `SU(3)` choice with no independent reason
3. it must sharpen at least one live bridge burden
4. it must not merely rename the desired conclusion in stabilizer language

Its value is conditional:

- it is allowed to sharpen the main branch
- it is not allowed to silently redefine the main branch

---

## Gating conditions

This path should only be allowed to influence the main line if at least one of the following happens:

1. the `Hermitian + rank/orbit` path leaves `u` underdetermined
2. the `Hermitian + rank/orbit` path leaves the candidate `SU(3)` story too weak
3. the same stabilizer-sensitive refinement plausibly sharpens both at once
4. the refinement can be stated without already assuming the reduced answer

If these conditions are not met, the path should remain live but not branch-directing.

---

## Interaction with the strong path

Because the main branch is now testing rank `1` against rank `2`, the stabilizer-sensitive path should not act on an abstract admissible sector.

It should act on that explicit comparison.

The practical question is:

> does the same stabilizer-sensitive refinement discriminate between rank `1` and rank `2` in a way that improves a real bridge burden?

The best current uses of this path are therefore:

1. test whether a stabilizer-sensitive condition makes rank `1` less thin without becoming engineered
2. test whether the same condition makes rank `2` genuinely more informative rather than merely broader
3. test whether the same refinement sharpens both `u` and `SU(3)` together

This is an important discipline point:

- the refinement path should not escape the rank comparison
- it should deepen the rank comparison

---

## First refinement probes

To stay disciplined, this path should not speak only in generalities.

The first useful refinement probes are:

### Probe S1: `u`-compatibility probe

Ask whether the admissible sector preserves a distinguished-direction structure strongly enough that `u` becomes less arbitrary.

This is still weaker than a derivation of `u`.

The test is only:

- does the refinement reduce the freedom in the allowed `u` data?

### Probe S2: residual-internal-symmetry probe

Ask whether the admissible sector preserves a candidate residual internal geometry on which a later `SU(3)` story is more than decorative.

This is still weaker than physical color.

The test is only:

- does the refinement preserve a cleaner candidate internal symmetry than the unrefined rank sector alone?

### Probe S3: joint `u` / `SU(3)` probe

Ask whether the same refinement step improves both burdens together.

This is the highest-value probe, because it is the clearest sign that the refinement is doing real bridge work rather than adding separate auxiliary choices.

The test is:

- does one refinement sharpen the preferred-direction story and the residual-symmetry story at the same time?

---

## Probe use against rank `1` and rank `2`

The probes should now be used comparatively.

| Probe | rank `1` question | rank `2` question | What would count as progress |
|---|---|---|---|
| `S1` | does refinement stop rank `1` from being too thin for `u`? | does refinement make rank `2` genuinely selective rather than merely broader? | one rank becomes clearly better for `u` without extra arbitrary input |
| `S2` | does refinement preserve enough internal structure for a disciplined symmetry story? | does refinement prevent rank `2` from just carrying loose extra symmetry? | one rank supports a cleaner residual `SU(3)` candidate |
| `S3` | can rank `1` support both burdens through one refinement? | can rank `2` support both burdens without over-broadening? | one rank supports a shared refinement of `u` and `SU(3)` |

This table gives the stabilizer-sensitive path a real job:

- not to invent a preferred answer
- but to test whether one rank candidate can support a non-arbitrary shared refinement

---

## Provisional comparison verdict

At the current stage, the fairest expectation is:

- `S1` is the first probe to try on rank `1`
- `S2` is the first probe most likely to tempt premature promotion of rank `2`
- `S3` is the real promotion test for the whole stabilizer-sensitive track

That means the path should mature in the following order:

1. test whether rank `1` can survive a mild `u`-compatibility refinement
2. test whether rank `2` earns its extra room by supporting a cleaner residual symmetry story
3. only then ask whether one shared refinement improves both burdens together

If step `3` fails across both ranks, this path remains useful diagnostically but should not become branch-directing.

---

## Where it is weak

- it has the highest ad hoc risk
- it can easily become reverse-engineered if the stabilizer requirement is chosen only to recover the desired answer
- it can blur the line between admissibility and later reduction

---

## Success condition

This path succeeds only if the stabilizer-sensitive condition can be defended independently of the result it produces.

The strongest version would be:

- the admissible sector naturally determines `u` up to the right orbit or stabilizer class
- the same admissible sector preserves the candidate `SU(3)` structure

That would be a real branch gain.

The strongest version of success is:

- the refinement sharpens both `u` and `SU(3)` through the same step, without needing a separate compensating choice afterward

---

## Failure condition

This path fails if:

- the stabilizer criterion is only reverse-engineered from the preferred reduced answer
- it adds complexity without improving the `u` or `SU(3)` bridge
- it cannot be stated without already assuming what later notes are supposed to derive

It should also be treated as failing if:

- it influences the branch before the main admissibility path has identified a grounded candidate sector to refine

That would mean the refinement is trying to do the work of the main path rather than refine it.

---

## Allowed influence on the main branch

At the present stage, this path is allowed to do three things:

1. propose refinement questions for the main path
2. identify where the rank `1` and rank `2` tests each leave `u` or `SU(3)` too loose
3. supply a candidate extra condition that can later be tested for independence

It is **not** yet allowed to:

1. replace the main admissibility backbone
2. decide the branch's preferred `u`
3. treat structural `SU(3)` as already physically realized

---

## Best current verdict

This is the most promising high-upside refinement path, but also the riskiest.

The safest use of it right now is:

- not as the first admissibility cut
- but as a later refinement imposed only if Hermitian and rank/orbit control have already done enough grounding

That means:

- keep it alive
- keep it separate
- promote it only if it earns a genuine bridge gain

The clearest promotion trigger would be:

- one stabilizer-sensitive refinement improves the `u` and `SU(3)` burden for the same rank candidate without simply broadening that candidate again

---

## Relation to the main branch

This path is already implicit in the current reduction note, but this separate file makes the central danger explicit:

- if stabilizer-sensitive admissibility cannot be defended independently, it weakens rather than strengthens the branch
