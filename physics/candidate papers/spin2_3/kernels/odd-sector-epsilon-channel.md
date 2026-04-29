# Odd-Sector Epsilon Channel

## Purpose

The branch/Casimir superselection note repackaged the candidate physical subspace as:
$$
P_{\mathrm{phys}}
=
P_{\mathrm{obs}}P_{\mathrm{aux},0}
\;+\;
P_{j_{\min}}P_{\mathrm{aux},1}.
$$

That was already cleaner than the earlier slot language. But the odd-sector projector can be sharpened one step further.

On
$$
\mathbf 2 \otimes \mathbf 2,
$$
the weak singlet is not merely the minimal-Casimir channel. It is exactly the unique `SU(2)`-invariant antisymmetric `epsilon` channel.

This note records that refinement.

---

## Standard `SU(2)` decomposition

For the defining weak doublet,
$$
\mathbf 2 \otimes \mathbf 2
=
\mathrm{Sym}^2(\mathbf 2) \oplus \wedge^2(\mathbf 2)
=
\mathbf 3 \oplus \mathbf 1.
$$

So:

- the triplet is the symmetric part;
- the singlet is the antisymmetric part.

Equivalently, the singlet is the image of the unique `SU(2)`-invariant alternating tensor
$$
\epsilon_{ab}.
$$

This means the odd weak-singlet channel can be characterized in three equivalent ways:

1. as the `j_{\mathrm{tot}}=0` channel;
2. as the antisymmetric channel;
3. as the `\epsilon`-contraction channel.

---

## Projector formulas

Let `\tau` denote the swap operator exchanging the two weak-doublet factors in
$$
\mathbf 2 \otimes \mathbf 2.
$$

Then:

- `\tau = +1` on the symmetric triplet,
- `\tau = -1` on the antisymmetric singlet.

So the singlet projector is exactly
$$
P_{\epsilon}
=
\frac12(\mathbf 1 - \tau).
$$

Now compare this with the total weak Casimir.

If `C_{\mathrm{tot}}` is normalized so that:

- `C_{\mathrm{tot}} = 0` on the singlet,
- `C_{\mathrm{tot}} = 2` on the triplet,

then on these two eigenspaces one has
$$
C_{\mathrm{tot}} = \mathbf 1 + \tau.
$$

Therefore
$$
P_{\epsilon}
=
\frac12(\mathbf 1 - \tau)
=
\mathbf 1 - \frac12 C_{\mathrm{tot}}.
$$

So the odd-sector projector used earlier,
$$
P_{\mathrm{odd},0}
=
\mathbf 1 - \frac12 C_{\mathrm{tot}},
$$
is exactly the antisymmetric `\epsilon`-channel projector.

---

## Why this is better than the Casimir-only reading

The Casimir reading said:

> keep the minimal total weak-spin channel.

That was already structural, but it still sounded somewhat spectral and abstract.

The `\epsilon`-channel reading is tighter:

> keep the unique `SU(2)`-invariant antisymmetric scalar pairing between the two doublets.

This matters because it makes the odd-sector choice look less like a minimization convention and more like the standard invariant scalar contraction.

In the present carrier language:

- the even auxiliary line is governed by observable-branch selection;
- the odd auxiliary line is governed by invariant antisymmetric scalar pairing.

That is a cleaner split of roles.

---

## Relation to the repo's antisymmetric-structure theme

The broader repo already treats antisymmetric `2`-plane structure as an important hidden motif in other branches of the programme.

This note does **not** claim that the odd auxiliary selector is already derived from that larger hidden antisymmetric story.

It does show something narrower:

> the odd-sector choice in the static carrier is already the unique antisymmetric scalar channel available in ordinary `SU(2)` representation theory.

So if a later parent derivation privileges antisymmetric pairings or oriented `2`-plane structure, it would align naturally with the present odd-sector selector rather than having to replace it.

---

## Rewriting the superselection rule

With this refinement, the candidate physical-subspace projector becomes
$$
P_{\mathrm{phys}}
=
P_{\mathrm{obs}}P_{\mathrm{aux},0}
\;+\;
P_{\epsilon}P_{\mathrm{aux},1},
$$
where:

- `P_{\mathrm{obs}}` is the observable-branch projector on the auxiliary even line,
- `P_{\epsilon}` is the antisymmetric `SU(2)`-invariant scalar-pairing projector on the auxiliary odd line.

This is the cleanest statement so far.

---

## What this changes conceptually

After this refinement, the candidate physical-state rule is no longer best described as:

- branch selection plus minimal Casimir selection.

It is better described as:

- observable-branch selection on the even line,
- invariant antisymmetric scalar-pairing selection on the odd line.

That is a more concrete and more standard representation-theoretic formulation.

---

## What remains open

This note still does not finish the derivation.

The remaining burden is now very localized:

1. why the even auxiliary line should obey the observable-branch selector `P_{\mathrm{obs}}`;
2. why the physical odd sector should be built through the invariant `\epsilon` pairing rather than through the symmetric triplet channel;
3. whether those two rules arise from one common parent statement.

But the odd part is now much less mysterious than before.

---

## Best current formulation

The strongest safe statement now available is:

> the best current candidate for the physical static subspace is selected by observable-branch projection on the auxiliary even line and by the unique antisymmetric `SU(2)`-invariant scalar-pairing channel on the auxiliary odd line.

That is more precise than the earlier branch/Casimir wording.

---

## What is now established

The following point is now finite:

> the odd-sector projector in the current physical-subcarrier candidate is not only the minimal total weak-spin projector; it is exactly the antisymmetric `\epsilon`-channel projector
> $$
> P_{\epsilon}
> =
> \frac12(\mathbf 1 - \tau)
> =
> \mathbf 1 - \frac12 C_{\mathrm{tot}}
> $$
> on `\mathbf 2 \otimes \mathbf 2`.

This is a genuine structural tightening of the odd-sector selection rule.

---

## What remains open

The next question is:

> can the full physical-subspace projector be derived as "observable branch plus invariant antisymmetric pairing" from the parent reduction, or must that rule be taken as part of the reduced state definition?
