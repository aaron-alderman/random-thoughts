# Full Fock Auxiliary Completion and the Top-Wedge Obstruction

## Purpose

The vacuum-plus-doublet candidate improved the auxiliary `\mathbf 1 \oplus \mathbf 2` story substantially:

$$
\Lambda^0 V \oplus \Lambda^1 V \cong \mathbf 1 \oplus \mathbf 2
$$

for the existing quaternionic doublet `V \cong \mathbf 2`.

But that candidate left one immediate question open:

> is the low-occupancy truncation really necessary, or could one simply use the full fermionic completion
> $$
> \Lambda^\bullet V \cong \mathbf 1 \oplus \mathbf 2 \oplus \mathbf 1
> $$
> without harm?

This note answers that question. The truncation is not optional if the current hypercharge fit is kept. The full Fock completion introduces an extra top-wedge weak-doublet sector with the wrong representation type. This is an additional obstruction on top of the already-existing complementary even-branch problem recorded in `kernels/even-line-exotic-branch-obstruction.md`.

---

## Full auxiliary completion

Start with the same quaternionic doublet
$$
V \cong \mathbf 2.
$$

Its full fermionic completion is
$$
\Lambda^\bullet V
=
\Lambda^0 V \oplus \Lambda^1 V \oplus \Lambda^2 V
\cong
\mathbf 1_{\mathrm{vac}} \oplus \mathbf 2_{\mathrm{1p}} \oplus \mathbf 1_{\mathrm{top}}.
$$

If one feeds this into the previously successful unified carrier, the natural full candidate is
$$
\mathcal H_{\mathrm{full}}
=
(T1 \oplus T2)\otimes \Lambda^\bullet V \otimes (\mathbf 3 \oplus \mathbf 1).
$$

Keep the same hypercharge operator as before, now written with the vacuum projector:
$$
Y
=
J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{vac}}.
$$

On the full Fock space, `P_{\mathrm{vac}}` acts by:

- `1` on `\Lambda^0 V`,
- `0` on `\Lambda^1 V`,
- `0` on `\Lambda^2 V`.

So the vacuum and one-particle sectors behave exactly as in the previous note. The new issue is entirely the top wedge `\Lambda^2 V`.

---

## The top wedge does not create singlets; it creates extra doublets

The crucial point is that
$$
\Lambda^2 V \cong \mathbf 1
$$
is a weak singlet **as an auxiliary factor**.

Therefore tensoring it with `T1` or `T2` does **not** create right-handed weak singlets. It leaves the reduced `Spin(2,3)` branch type unchanged:
$$
T1 \otimes \Lambda^2 V \cong T1 \cong (\mathbf 2,-1/2),
$$
$$
T2 \otimes \Lambda^2 V \cong T2 \cong (\mathbf 2,+1/2).
$$

So the top wedge sector contributes **another pair of weak doublet carriers**, not another pair of singlet carriers.

That is already enough to show that the full Fock completion is structurally different from the low-occupancy candidate.

---

## Hypercharges on the top-wedge doublets

Because `P_{\mathrm{vac}} = 0` on `\Lambda^2 V`, the top-wedge charges are simply
$$
Y = J^{01} + \frac12 Q7
$$
on that sector.

### `T1` top wedge

On the `T1` branch, `J^{01} = -1/2`. Therefore:

- on the color-triplet slot (`Q7 = 1/3`),
  $$
  Y = -\frac12 + \frac16 = -\frac13;
  $$
- on the singlet slot (`Q7 = -1`),
  $$
  Y = -\frac12 - \frac12 = -1.
  $$

So the `T1` top wedge carries weak doublets with hypercharges
$$
(\mathbf 3,\mathbf 2)_{-1/3}
\oplus
(\mathbf 1,\mathbf 2)_{-1}.
$$

### `T2` top wedge

On the `T2` branch, `J^{01} = +1/2`. Therefore:

- on the color-triplet slot (`Q7 = 1/3`),
  $$
  Y = \frac12 + \frac16 = \frac23;
  $$
- on the singlet slot (`Q7 = -1`),
  $$
  Y = \frac12 - \frac12 = 0.
  $$

So the `T2` top wedge carries weak doublets with hypercharges
$$
(\mathbf 3,\mathbf 2)_{2/3}
\oplus
(\mathbf 1,\mathbf 2)_0.
$$

---

## Why this is an obstruction

These top-wedge sectors are not innocuous duplicates of the ordinary left-handed seed.

They are stranger than that:

- the `T1` top wedge carries the **right-handed-style hypercharge values**
  `-1/3` and `-1`,
  but on weak doublets rather than weak singlets;
- the `T2` top wedge carries the **right-handed-style hypercharge values**
  `2/3` and `0`,
  again on weak doublets rather than weak singlets.

So the full Fock completion does not merely overcount states. It puts the right hypercharge values on the wrong `SU(2)` representation type.

That is a real obstruction, not just cosmetic redundancy.

---

## What this means for the vacuum-plus-doublet candidate

The previous note suggested that
$$
\Lambda^{\le 1} V = \Lambda^0 V \oplus \Lambda^1 V
$$
is the best current candidate auxiliary block.

The present calculation sharpens that claim:

> if the current hypercharge operator is kept, then some mechanism removing or neutralizing the top wedge `\Lambda^2 V` is necessary.

So the low-occupancy truncation is not merely a convenient reading. It is the minimal way to avoid the extra wrong-type doublet sector.

---

## Best current escape routes

At the current kernel level there are three clear ways one could try to save the vacuum-plus-doublet idea:

1. **Literal low-occupancy truncation.**
   Keep only `\Lambda^0 V \oplus \Lambda^1 V` as the physical auxiliary carrier.

2. **Even-sector identification or quotient.**
   Use some particle-hole, Hodge-dual, or other constraint to identify or remove the top wedge singlet `\Lambda^2 V` relative to the vacuum singlet `\Lambda^0 V`.

3. **Hidden decoupling / reinterpretation.**
   Keep the full Fock space but show that the top-wedge doublets are projected out dynamically, lifted to a very high scale, or reinterpreted as a separate unobserved sector.

None of these is established yet. But the current note tells us exactly what any successful mechanism has to accomplish.

---

## What is now established

The following point is now closed:

> the full fermionic completion `\Lambda^\bullet V \cong \mathbf 1 \oplus \mathbf 2 \oplus \mathbf 1` is not by itself a clean replacement for the low-occupancy auxiliary block in the present hypercharge construction, because the top wedge `\Lambda^2 V` generates extra weak doublets carrying right-handed-style hypercharge values on the wrong `SU(2)` representation type.

That is a finite and useful obstruction.

---

## What remains open

The next question is now sharper than before:

> what mechanism, if any, removes, identifies, or dynamically neutralizes the top-wedge sector `\Lambda^2 V` so that the vacuum-plus-doublet auxiliary candidate can survive as a physical construction?
