# `T1 tensor (3 + 1)`: Product Symmetry, Diagonal Overlap, and the Hypercharge Slot

## Purpose

This note sharpens the static matter ansatz

$$
\mathcal H_{\mathrm{matter}} = T1 \otimes (\mathbf 3 \oplus \mathbf 1)
$$

using the new compact-overlap result in `kernels/g2-spin23-intersection.md`.

The main outcome is a separation of three distinct structures that were easy to mix before:

1. the full product symmetry `SU(3) x K` acting on the ansatz;
2. the literal common compact overlap `K_cap ~= U(2)`;
3. the `Q7` grading slot relevant to hypercharge matching.

Once these are separated, one finite hypercharge result falls out immediately.

---

## Input data

The current corpus fixes the following compact data:

1. `T1` is the `J^{01}` eigenspace of eigenvalue `-1/2`, so as a `K = U(1) x SU(2)` module
   $$
   T1 = (\mathbf 2,-1/2).
   $$

2. The preferred-octonion stabilizer is
   $$
   \mathrm{Stab}_{G_2}(u) = SU(3).
   $$

3. The literal compact overlap between that octonionic structure and the reduced `Spin(2,3)` compact structure is only
   $$
   K_\cap = G_2 \cap \mathrm{Spin}(2,3) = U(1) x SU(2)
   $$
   in repo convention, equivalently `U(2)` up to common center.

4. Under this overlap, the octonionic color carrier restricts as
   $$
   \mathbf 3 \downarrow_{K_\cap} = \mathbf 2_{+1/2} \oplus \mathbf 1_{-1}.
   $$

The question is what these statements do to the matter ansatz.

---

## The full product action is still the right static organizer

Before restricting anything to the literal overlap, the natural static action on

$$
T1 \otimes (\mathbf 3 \oplus \mathbf 1)
$$

is the product action of:

- `K` on `T1`;
- `SU(3)` on `\mathbf 3 \oplus \mathbf 1`.

Under that product action one has

$$
T1 \otimes (\mathbf 3 \oplus \mathbf 1)
=
(\mathbf 3,\mathbf 2)_{-1/2} \oplus (\mathbf 1,\mathbf 2)_{-1/2}.
$$

This is the clean content of the existing static claim:

- one color-triplet weak doublet slot;
- one color-singlet weak doublet slot.

So the quark/lepton slot statement lives naturally at the level of the pair

$$
SU(3) \times K,
$$

not at the level of the literal intersection alone.

---

## Restriction to the literal compact overlap

Now restrict the same ansatz to the diagonal/common compact overlap `K_cap`.

Since

$$
T1 = \mathbf 2_{-1/2},
\qquad
\mathbf 3 \oplus \mathbf 1
\downarrow_{K_\cap}
=
\mathbf 2_{+1/2} \oplus \mathbf 1_{-1} \oplus \mathbf 1_0,
$$

one gets

$$
T1 \otimes (\mathbf 3 \oplus \mathbf 1)
\downarrow_{K_\cap}
=
\mathbf 2_{-1/2} \otimes
\big(
\mathbf 2_{+1/2} \oplus \mathbf 1_{-1} \oplus \mathbf 1_0
\big).
$$

Using `2 tensor 2 = 1 ⊕ 3` for the `SU(2)` factor and adding `U(1)` weights gives

$$
\mathcal H_{\mathrm{matter}}\downarrow_{K_\cap}
=
(\mathbf 1,0) \oplus (\mathbf 3,0) \oplus (\mathbf 2,-3/2) \oplus (\mathbf 2,-1/2).
$$

So the literal overlap reorganizes the ansatz into:

- one compact singlet of charge `0`;
- one compact triplet of charge `0`;
- one compact doublet of charge `-3/2`;
- one compact doublet of charge `-1/2`.

This is important because it shows exactly why the earlier `G2 cap Spin(2,3)` hope was too strong:

- the full quark/lepton slot structure is visible under `SU(3) x K`;
- the literal overlap only sees a repackaged `U(2)` spectrum.

So the matter ansatz is not controlled by the overlap alone.

---

## The natural `Q7` slot on `3 + 1`

The hypercharge ansatz elsewhere in the repo is

$$
Y = a J^{01} + b Q7.
$$

The overlap calculation helps clarify what `Q7` can mean safely on the bare static seed.

On the `\mathbf 3 \oplus \mathbf 1` carrier, any operator commuting with the full `SU(3)` action must be of the form

$$
\alpha \,\mathbf 1_{\mathbf 3} \oplus \beta \,\mathbf 1_{\mathbf 1}.
$$

If one also imposes tracelessness, there is only one nontrivial such grading direction up to scale. A convenient normalization is

$$
Q7 =
\mathrm{diag}\!\left(
\frac13,\frac13,\frac13,-1
\right)
$$

on `\mathbf 3 \oplus \mathbf 1`.

This is the unique `SU(3)`-invariant traceless grading that separates the color triplet from the singlet.

That is a cleaner characterization of `Q7` than trying to identify it with the `U(1)` generator inside the literal `U(2)` overlap. The overlap `U(1)` splits the `\mathbf 3` itself as `2 + 1`; the grading above instead separates `\mathbf 3` from the extra `\mathbf 1`.

---

## What the hypercharge ansatz does on the bare `T1` seed

On the bare left-handed seed `T1 \otimes (\mathbf 3 \oplus \mathbf 1)`, the `Spin(2,3)` generator `J^{01}` acts as the constant value

$$
J^{01}|_{T1} = -\frac12.
$$

So inside this seed,

$$
Y = a J^{01} + b Q7
$$

gives:

- quark-doublet slot:
  $$
  Y_Q = -\frac a2 + \frac b3;
  $$
- lepton-doublet slot:
  $$
  Y_L = -\frac a2 - b.
  $$

If one matches the usual left-handed target values

$$
Y_Q = \frac16,
\qquad
Y_L = -\frac12,
$$

then one gets the finite linear system

$$
-\frac a2 + \frac b3 = \frac16,
\qquad
-\frac a2 - b = -\frac12.
$$

Subtracting gives

$$
\frac{4b}{3} = \frac23
\qquad\Longrightarrow\qquad
b = \frac12,
$$

and then the second equation gives

$$
a = 0.
$$

So, on the bare left-handed static seed,

$$
Y\big|_{T1 \otimes (\mathbf 3 \oplus \mathbf 1)}
=
\frac12\,Q7.
$$

That is the finite result.

---

## Interpretation of the result

This does **not** mean `J^{01}` is irrelevant to the full framework. It means something narrower:

> on the unreduced left-handed `T1` seed alone, the `J^{01}` term is invisible as an independent fit parameter because it is constant across the whole seed.

So any genuinely nontrivial role for the `J^{01}` contribution to hypercharge must enter only after enlarging beyond the bare left-handed seed, for example by including:

- right-handed singlet completion;
- `T2`-related sectors;
- a larger ambient representation in which the `J^{01}` eigenvalue is not constant across all states being matched.

This is actually useful. It narrows the open problem:

- the left-handed quark/lepton doublet split is already captured by the octonionic grading slot;
- the real burden on `J^{01}` is to distinguish sectors that the bare `T1` seed cannot distinguish by itself.

---

## What is now established

The following points are now closed within the present ansatz:

1. the quark/lepton slot statement belongs naturally to the product structure `SU(3) x K`, not to the literal overlap;
2. the literal compact overlap only repackages the matter seed into a `U(2)` spectrum
   $$
   (\mathbf 1,0) \oplus (\mathbf 3,0) \oplus (\mathbf 2,-3/2) \oplus (\mathbf 2,-1/2);
   $$
3. on `\mathbf 3 \oplus \mathbf 1`, the `SU(3)`-invariant traceless grading is unique up to scale;
4. with the natural normalization `Q7 = diag(1/3,1/3,1/3,-1)`, matching the left-handed doublet charges forces
   $$
   Y = \frac12 Q7
   $$
   on the bare `T1` seed.

---

## What remains open

This note does **not** prove:

- that the full hypercharge embedding is uniquely canonical;
- that the same coefficient choice survives the right-handed completion unchanged;
- that `Q7` has been derived from a unique ambient operator rather than identified as the natural grading slot on `\mathbf 3 \oplus \mathbf 1`.

So the next hypercharge question is now much sharper:

> where does the `J^{01}` contribution first become genuinely necessary, and can that extension still be made canonical?

That is a better-posed problem than the previous generic "fix `a` and `b`" wording.
