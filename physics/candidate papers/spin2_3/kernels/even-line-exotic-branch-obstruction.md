# Even-Line Exotic Branch Obstruction

## Purpose

The projector repair
$$
Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}
$$
solved a real algebraic problem:

- it fit the standard left-handed doublet charges;
- it fit the standard right-handed singlet charges;
- it gave the first working unified hypercharge operator on the small carrier.

But that fit was made on a **selected slot assignment** inside the carrier. The natural next question is:

> does the same carrier automatically avoid extra unwanted states, or was the fit only partial?

This note answers that question. The fit is only partial. Even before the top-wedge issue from the full Fock completion, the even auxiliary line already contains an unused exotic `T2` doublet sector.

---

## The even auxiliary line carries both `T1` and `T2`

In the projector-repair carrier
$$
(T1 \oplus T2)\otimes (\mathbf 1 \oplus S_{\mathrm{aux}})\otimes (\mathbf 3 \oplus \mathbf 1),
$$
the left-handed doublets were taken from:

- the `\mathbf 1` part of `\mathbf 1 \oplus S_{\mathrm{aux}}`,
- on the `T1` branch.

With the fitted coefficients
$$
a = 1,
\qquad
b = \frac12,
\qquad
c = \frac12,
$$
the hypercharge operator is
$$
Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}.
$$

On the auxiliary even line one has
$$
P_{\mathrm{aux},0} = 1.
$$

So both `T1` and `T2` branches on that line carry charges
$$
Y = J^{01} + \frac12 Q7 + \frac12.
$$

The earlier fit used only the `T1` part of this sector. But the `T2` part is still present unless an additional rule removes it.

---

## Charges on the even line

### `T1` even line

On `T1`, `J^{01} = -1/2`, so:

- on the color-triplet slot (`Q7 = 1/3`),
  $$
  Y = -\frac12 + \frac16 + \frac12 = \frac16;
  $$
- on the singlet slot (`Q7 = -1`),
  $$
  Y = -\frac12 - \frac12 + \frac12 = -\frac12.
  $$

So the `T1` even line gives the desired left-handed doublets
$$
(\mathbf 3,\mathbf 2)_{1/6}
\oplus
(\mathbf 1,\mathbf 2)_{-1/2}.
$$

### `T2` even line

On `T2`, `J^{01} = +1/2`, so:

- on the color-triplet slot (`Q7 = 1/3`),
  $$
  Y = \frac12 + \frac16 + \frac12 = \frac76;
  $$
- on the singlet slot (`Q7 = -1`),
  $$
  Y = \frac12 - \frac12 + \frac12 = \frac12.
  $$

So the complementary `T2` even line gives
$$
(\mathbf 3,\mathbf 2)_{7/6}
\oplus
(\mathbf 1,\mathbf 2)_{1/2}.
$$

These are exotic weak doublets, not part of the usual one-generation matter content.

---

## Why this matters

This is not the same problem as the later top-wedge obstruction.

The top-wedge obstruction appeared only after replacing the auxiliary `\mathbf 1 \oplus \mathbf 2` block by the full fermionic completion
$$
\mathbf 1 \oplus \mathbf 2 \oplus \mathbf 1.
$$

By contrast, the present obstruction already exists on the smaller auxiliary block itself:

- one even auxiliary line,
- one odd auxiliary doublet,
- but **two** branch choices on the even line.

So the low-occupancy vacuum-plus-doublet candidate does not yet solve the full spectrum problem by itself. It solves the slot-level hypercharge fit, but not the unwanted complementary even-branch sector.

---

## What this changes about the projector repair

The projector repair should now be read more carefully:

> it is a successful selected-slot fit, not yet a full-spectrum completion of the candidate carrier.

That is still useful. It means the operator itself is plausible.

But it also means a second mechanism is required:

> some rule must keep the `T1` even line and remove, identify, or decouple the `T2` even line.

Without that extra rule, the candidate carrier still contains exotic weak doublets.

---

## Best current escape routes

At the current kernel level, the live ways out are:

1. **Branch-selective even-sector rule.**
   Only one branch of the auxiliary even line is physical in the chosen orientation.

2. **Dynamical lifting or decoupling.**
   The complementary `T2` even-line doublets are massive, confined, or otherwise removed from the low-energy spectrum.

3. **Non-factorized carrier refinement.**
   The physical carrier is not the full tensor product
   $$
   (T1 \oplus T2)\otimes (\mathbf 1 \oplus \mathbf 2),
   $$
   but a smaller subcarrier that keeps the wanted even sector and odd singlet channels without keeping the complementary even branch.

4. **Orientation/readout-linked selection.**
   The same structure that eventually chooses the physical branch orientation may also choose which even-line branch survives.

None of these is closed yet. But the obstruction makes clear what the next mechanism must do.

---

## What is now established

The following statement is now finite:

> the minimal projector/vacuum repair is not yet a full carrier solution. On the auxiliary even line it produces both the desired `T1` left-handed doublets and an unwanted complementary `T2` doublet sector with charges `(\mathbf 3,\mathbf 2)_{7/6} \oplus (\mathbf 1,\mathbf 2)_{1/2}`.

So the current fit is a selected-slot success, not a closed static spectrum.

---

## What remains open

The next question is now:

> what principled mechanism removes, identifies, or dynamically neutralizes the complementary `T2` even-line sector while preserving the successful hypercharge fit on the selected slots?
