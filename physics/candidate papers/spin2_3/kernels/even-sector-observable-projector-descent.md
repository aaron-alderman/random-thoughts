# Even-Sector Observable Projector Descent

## Purpose

After the epsilon-channel refinement, the candidate physical-state rule has the form
$$
P_{\mathrm{phys}}
=
P_{\mathrm{obs}}P_{\mathrm{aux},0}
\;+\;
P_{\epsilon}P_{\mathrm{aux},1},
$$
where:

- `P_{\epsilon}` is now essentially fixed by ordinary `SU(2)` representation theory on the odd auxiliary sector;
- the real remaining ambiguity sits in the even-line selector `P_{\mathrm{obs}}`.

This note isolates the finite result already available in the corpus:

> the even-line selector is not a new static ad hoc rule. It is exactly the reduced observable-sector projector already required by the ambient/readout scaffold.

That does not finish the derivation. But it narrows the open burden substantially.

---

## The scaffold already contains `P_{\mathrm{obs}}`

The ambient-reduction scaffold introduces an observable-sector projector
$$
P_{\mathrm{obs}}
$$
selected by the forward readout orientation.

The key compatibility statement there is:
$$
\mathcal R_{\mathrm{op}}(P_{\Pi,-}) = P_{\mathrm{obs}},
\qquad
\mathcal R_{\mathrm{op}}(P_{\Pi,+}) = 1 - P_{\mathrm{obs}},
$$
with the sector named `T1` defined to be the reduced eigenspace selected by the physical orientation.

So once the global orientation is fixed, the static branch projector is not extra data. It is simply
$$
P_{\mathrm{obs}} = P_{T1}.
$$

In the chosen reduced convention,
$$
P_{T1}
=
\frac12(\mathbf 1 - 2J^{01}).
$$

---

## Why this matters for the hypercharge carrier

The minimal physical-subcarrier candidate used the even-line projector
$$
P_{T1}P_{\mathrm{aux},0}.
$$

Without the scaffold context, that can look like a local patch:

- keep `T1` on the even line because it gives the desired left-handed charges;
- discard `T2` because it gives exotic charges.

But the scaffold changes the interpretation:

> the physical even-line branch is whichever `J^{01}` eigenspace is selected by the forward observable/readout orientation, and in the current orientation that is exactly `T1`.

So the even half of the static subcarrier is not a new hypercharge-specific branch rule. It is the same observable-sector rule the reduction programme already needed for zero-mass support.

---

## Support preservation viewpoint

The scaffold's support-compatibility conditions say that if the parent direct/readout operator is already confined to the parent negative-charge sector,
$$
H_{\Pi}^{(0)} = P_{\Pi,-} H_{\Pi}^{(0)} P_{\Pi,-},
$$
then reduction should not create spurious support on the opposite reduced sector.

Transporting this through the reduction map gives
$$
H_0 = P_{\mathrm{obs}} H_0 P_{\mathrm{obs}},
$$
with
$$
(\mathbf 1 - P_{\mathrm{obs}}) H_0 = H_0 (\mathbf 1 - P_{\mathrm{obs}}) = 0.
$$

So the even-line branch selector can be read as a support-preservation consequence:

- parent direct/readout support is one-sided,
- reduction preserves that one-sided support,
- the reduced one-sided support is exactly the `P_{\mathrm{obs}}` sector.

This is the cleanest current reason the complementary even branch should be absent.

---

## Rewriting the static candidate one more time

Using the scaffold notation, the physical-state projector now reads
$$
P_{\mathrm{phys}}
=
P_{\mathrm{obs}}P_{\mathrm{aux},0}
\;+\;
P_{\epsilon}P_{\mathrm{aux},1},
$$
where:

- `P_{\mathrm{obs}}` comes from the ambient/readout orientation and reduced support-preservation rule,
- `P_{\epsilon}` comes from the unique antisymmetric invariant scalar channel on `\mathbf 2 \otimes \mathbf 2`.

This is better than the earlier wording because the two halves now have distinct and coherent roles:

- even line: observable/readout support selector,
- odd line: invariant antisymmetric scalar-pairing selector.

---

## What this does and does not close

This note **does** close the following finite point:

> in the current static carrier proposal, the even-line projector is not an independent new ingredient beyond the ambient scaffold. It is the reduced observable-sector projector already required by the zero-mass/readout descent programme.

This note does **not** yet derive:

1. why the ambient/readout selector picks one global orientation rather than the other;
2. whether the same parent mechanism that fixes `P_{\mathrm{obs}}` also explains the low-occupancy auxiliary structure;
3. whether the branch/readout selector and the odd `\epsilon` selector come from one common parent principle.

So the open burden is now mostly upstream of the static carrier, not inside it.

---

## Best current formulation

The cleanest current statement is:

> the candidate physical static subspace is selected by the observable/readout projector on the auxiliary even line and by the invariant antisymmetric `SU(2)` pairing projector on the auxiliary odd line.

This means the static problem has been reduced to two upstream questions:

1. what fixes the observable/readout orientation,
2. what justifies the auxiliary low-occupancy block if the Fock reading is used.

The carrier algebra itself is now comparatively disciplined.

---

## What is now established

The following statement is now finite:

> the even half of the current physical-subcarrier candidate,
> $$
> P_{\mathrm{obs}}P_{\mathrm{aux},0},
> $$
> is exactly the reduced observable-sector projector already built into the ambient/readout scaffold, not a separate hypercharge-specific branch rule.

That is a genuine narrowing of the remaining static ambiguity.

---

## What remains open

The next question is:

> can the same ambient/readout selector that fixes `P_{\mathrm{obs}}` also explain why the auxiliary odd sector should enter only through the invariant antisymmetric pairing channel, or are these two superselection inputs fundamentally separate?
