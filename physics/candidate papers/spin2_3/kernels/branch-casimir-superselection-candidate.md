# Branch-Casimir Superselection Candidate

## Purpose

The minimal physical-subcarrier note gave the first fully explicit operator-level candidate:
$$
P_{\mathrm{phys}}
=
P_{T1}P_{\mathrm{aux},0}
\;+\;
P_{\mathrm{odd},0}P_{\mathrm{aux},1}.
$$

That was progress, but it still looked like a local repair assembled from several pieces.

This note reorganizes the same projector into two selectors the corpus already treats as structurally meaningful:

1. an **observable branch selector** on the auxiliary even line,
2. a **minimal total weak-spin selector** on the auxiliary odd sector.

This does not fully derive the subcarrier. But it changes the status of the proposal from "slot-fixing patch" to a concrete superselection candidate.

---

## Even line: the observable branch selector is already in the scaffold

The ambient-reduction scaffold already isolates an observable-sector projector
$$
P_{\mathrm{obs}}
$$
selected by the forward readout orientation.

In the current reduced orientation convention, that observable sector is named `T1`. So
$$
P_{\mathrm{obs}} = P_{T1}
=
\frac12\bigl(\mathbf 1 - 2J^{01}\bigr).
$$

This matters because the even-line choice in the minimal subcarrier is no longer a random branch deletion. It is exactly the same branch-selection problem the repo already had elsewhere:

> which `J^{01}` eigenspace is the forward observable sector once the global orientation is fixed?

So the even-line piece of the subcarrier can be read as:
$$
P_{\mathrm{obs}}\,P_{\mathrm{aux},0}.
$$

That ties it directly to the existing orientation/readout programme rather than introducing a separate branch rule just for the hypercharge carrier.

---

## Odd line: the weak-singlet selector is a total-Casimir minimum

On the auxiliary odd sector the weak content is
$$
\mathbf 2 \otimes \mathbf 2 = \mathbf 1 \oplus \mathbf 3.
$$

The previous note used the projector
$$
P_{\mathrm{odd},0}
=
\mathbf 1 - \frac12 C_{\mathrm{tot}},
$$
where `C_{\mathrm{tot}}` is the total weak `SU(2)` Casimir.

This is exactly the projector onto the **minimal total weak-spin sector**:

- `j_{\mathrm{tot}} = 0` on the singlet,
- `j_{\mathrm{tot}} = 1` on the triplet.

So the odd-sector choice can be read as:

> keep only the minimal total weak-spin channel on the odd auxiliary sector.

This is better than saying "keep the slot that happened to work." It makes the odd-sector rule a standard spectral choice.

---

## Rewriting the physical subcarrier

With that language, the physical-subcarrier projector becomes
$$
P_{\mathrm{phys}}
=
P_{\mathrm{obs}}\,P_{\mathrm{aux},0}
\;+\;
P_{j_{\min}}\,P_{\mathrm{aux},1},
$$
where:

- `P_{\mathrm{obs}}` is the observable-branch projector chosen by orientation/readout,
- `P_{j_{\min}}` is the spectral projector onto the minimal total weak-spin sector on the odd auxiliary block.

So the whole carrier proposal can be read in one sentence:

> physical static states lie in the observable branch on the auxiliary even line, and in the minimal total weak-spin channel on the auxiliary odd line.

That is the cleanest conceptual packaging reached so far.

---

## Why this is a real simplification

Before this reformulation, the project seemed to need three separate ad hoc instructions:

1. keep `T1` on the even line,
2. keep the odd singlet channel,
3. drop the rest.

After the reformulation, those become two existing structural ideas:

1. **observable-sector selection** from the orientation/readout programme;
2. **minimal Casimir-sector selection** on the odd weak sector.

This does not make the proposal true. But it does make it much more coherent.

---

## Orientation partner

Under the common global orientation reversal,
$$
P_{\mathrm{obs}} \leftrightarrow \mathbf 1 - P_{\mathrm{obs}},
$$
while the odd-sector Casimir projector is unchanged.

So the orientation partner of the candidate is
$$
P_{\mathrm{phys}}'
=
(\mathbf 1 - P_{\mathrm{obs}})\,P_{\mathrm{aux},0}
\;+\;
P_{j_{\min}}\,P_{\mathrm{aux},1}.
$$

This is exactly what one should expect:

- the even-line physical branch swaps under orientation reversal,
- the odd weak-singlet selection does not.

So the new packaging is compatible with the existing global-orientation dictionary.

---

## What this still does not derive

The superselection interpretation is tighter, but it is still not a theorem.

What remains open is not the formula. The formula is clear.

What remains open is:

1. why physical observable states should obey `P_{\mathrm{obs}}` on the even auxiliary line;
2. why physical odd auxiliary states should minimize the total weak Casimir rather than populate the triplet channel;
3. whether both rules arise from one deeper parent statement or from two separate mechanisms.

So the proposal is best read as a **candidate superselection rule**, not yet as a derived consequence.

---

## Best current formulation

The safest strong statement now available is:

> the best current candidate for the physical static space is the subcarrier selected by observable-branch projection on the auxiliary even line and minimal total weak-spin projection on the auxiliary odd line.

This is stronger than "we found some slots that work," and weaker than "the parent geometry has proved this uniquely."

That is exactly the right level for the repo at present.

---

## What is now established

The following point is now finite:

> the explicit subcarrier projector
> $$
> P_{\mathrm{phys}}
> =
> P_{T1}P_{\mathrm{aux},0}
> +
> P_{\mathrm{odd},0}P_{\mathrm{aux},1}
> $$
> can be rewritten structurally as
> $$
> P_{\mathrm{phys}}
> =
> P_{\mathrm{obs}}P_{\mathrm{aux},0}
> +
> P_{j_{\min}}P_{\mathrm{aux},1},
> $$
> i.e. as observable-branch selection on the even line plus minimal total weak-spin selection on the odd line.

That is a genuine conceptual tightening of the static proposal.

---

## What remains open

The next question is:

> can the branch/Casimir superselection rule be derived from the parent reduction or eventual orientation selector, or must it be postulated as part of the reduced physical state definition?
