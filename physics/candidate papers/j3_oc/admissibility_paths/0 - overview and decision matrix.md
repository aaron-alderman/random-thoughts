# Admissibility Paths Overview

## Purpose

This folder compares the main admissibility paths currently available to the `j3_oc` branch.

Its purpose is not to declare a winner too early.

Its purpose is to:

- separate the genuinely different admissibility strategies
- make their strengths and risks explicit
- compare them against the real burdens of the branch
- leave a clear record of why one path may later be preferred

This is a comparison pack, but it now also records the current working investigation strategy.

Related notes:

- [0b - ambient-to-observable reduction.md](../0b%20-%20ambient-to-observable%20reduction.md)
- [0c - falsification and decision criteria.md](../0c%20-%20falsification%20and%20decision%20criteria.md)
- [2a - statics.md](../2a%20-%20statics.md)
- [2d - consistency.md](../2d%20-%20consistency.md)

---

## Candidate paths

The current comparison pack treats four paths as the main serious candidates:

1. `Hermitian-first`
2. `Hermitian + rank/orbit`
3. `Stabilizer-sensitive`
4. `Observable-viability first`

These are not four different theory programs.

They are four different ways to define the first serious admissibility cut on
$$
X \in J3(C \otimes O).
$$

---

## Evaluation criteria

The paths should be compared against the actual burdens of the branch, not only by elegance.

The main tests are:

1. `Discipline`
   Does the path give a real admissibility rule rather than vague cleanup?
2. `u`
   Does the path improve the status of `u`, even if only up to orbit or stabilizer class?
3. `SU(3)`
   Does the path help distinguish ambient stabilizer from reduced internal symmetry and possible color?
4. `Reduction`
   Does the path support a credible later route to a reduced `Spin(2,3)`-type image?
5. `Observable viability`
   Does the path help later observable extraction rather than leaving it fully unstructured?
6. `Ad hoc risk`
   Does the path risk reverse-engineering the answer?
7. `Comparative value against J3(O)`
   Does the path help explain why the complexified branch earns something over the real branch?

---

## Quick matrix

| Path | Strength | Main risk | Provisional role |
|---|---|---|---|
| Hermitian-first | safest baseline control | too weak by itself | likely stage one, not whole answer |
| Hermitian + rank/orbit | more selective and geometric | may still not sharpen `u` or `SU(3)` enough | strongest middle candidate |
| Stabilizer-sensitive | directly targets branch burdens | highest ad hoc danger | strong but risky refinement stage |
| Observable-viability first | ties ambient branch to physics early | may start too far downstream | useful check, weak as first cut |

---

## Current working strategy

The current working strategy is:

- treat `Hermitian + rank/orbit` as the active strong path
- keep `Hermitian-first` alive as a weaker fallback, not as an equal competitor
- return to the weaker path only if the stronger path hits a real roadblock and that fallback clarifies where the difficulty actually lies
- keep `Stabilizer-sensitive` alive in parallel as a high-upside refinement track
- treat `Observable-viability first` mainly as a pressure test rather than a primary backbone

This means the branch is no longer merely comparing paths in the abstract.

It is running:

1. one main strong path
2. one weaker fallback path
3. one parallel high-upside refinement path

That is the most disciplined way to explore multiple admissibility options without multiplying the whole branch.

---

## Provisional reading

The current best non-overclaiming picture is:

- `Hermitian-first` is the safest weak baseline
- `Hermitian + rank/orbit` is the strongest candidate for the main admissibility backbone and should now be treated as the active strong path
- `Stabilizer-sensitive` should remain alive in parallel as a refinement track unless it can later justify becoming part of the main backbone
- `Observable-viability first` is more useful as a screening or comparison criterion than as the very first cut

That is not a final victory claim. It is the current investigative posture.

The first explicit test candidate inside the strong path is now:

- Hermitian rank-`1` / projective-like admissibility

This is a provisional working choice meant to make the strong path falsifiable, not a declaration that rank `1` is already the correct physical sector.

The nearest comparison case inside that same strong path is now:

- Hermitian rank-`2` or a corresponding non-minimal orbit sector

So the current strong-path investigation is no longer only:

- "is rank `1` good?"

It is now:

- "is rank `1` informative enough to keep, or is rank `2` the first admissible sector that actually sharpens the branch burdens?"

---

## What would count as a winner

A path should count as the current preferred admissibility path only if it does at least one of the following better than the others:

1. improves the `u` story
2. improves the `SU(3)` story
3. sharpens the reduction map
4. helps explain why `J3(C \otimes O)` earns more than `J3(O)`

If no path clearly does that, the right conclusion is:

- keep multiple paths alive
- treat one as the active strong path
- keep one weaker fallback available
- do not pretend the branch decision is settled

---

## Current decision matrix inside the strong path

The active strong path now contains its own internal comparison:

| Candidate inside `Hermitian + rank/orbit` | Present role | Reason |
|---|---|---|
| rank `1` | primary test case | strongest first cut, lowest ad hoc risk, best falsifiability |
| rank `2` | nearest escalation test | richer internal structure if rank `1` proves too thin |

The current working verdict is:

- keep rank `1` as the main live candidate
- keep rank `2` close at hand as the first serious escalation
- do not promote rank `2` merely because it carries more room

This means the branch now has a clearer nested strategy:

1. main strong path = `Hermitian + rank/orbit`
2. internal primary test = rank `1`
3. internal escalation test = rank `2`
4. parallel refinement track = stabilizer-sensitive admissibility

The stabilizer-sensitive track is now concrete enough to have its own ordered probes:

1. `u`-compatibility probe
2. residual-internal-symmetry probe
3. joint `u` / `SU(3)` probe

That is helpful because it keeps the refinement track from sounding stronger than it is.

---

## File map

- [1a - Hermitian-first path.md](1a%20-%20Hermitian-first%20path.md)
- [1b - Hermitian plus rank-orbit path.md](1b%20-%20Hermitian%20plus%20rank-orbit%20path.md)
- [1c - Stabilizer-sensitive path.md](1c%20-%20Stabilizer-sensitive%20path.md)
- [1d - Observable-viability path.md](1d%20-%20Observable-viability%20path.md)

---

## Working bottom line

This pack exists so the branch can investigate several admissibility paths in parallel without multiplying the whole framework.

That is the right level of branching for now.
