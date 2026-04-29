# Auxiliary Vacuum-Plus-Doublet Candidate

## Purpose

The previous screening note closed one obvious route:

- the current quaternionic slice `H(u,v)` does supply the visible irreducible complex doublet `\mathbf 2`;
- but under that natural visible `SU(2)` action it does **not** itself contain the reducible auxiliary block `\mathbf 1 \oplus \mathbf 2`.

So the next reasonable question is:

> can the required auxiliary `\mathbf 1 \oplus \mathbf 2` block arise from a standard completion of the existing quaternionic doublet, rather than from a completely unrelated new module?

This note records the cleanest current candidate: a vacuum-plus-single-occupancy completion of the quaternionic doublet.

---

## Start from the existing quaternionic doublet

Let
$$
V := H(u,v)
$$
viewed as a complex vector space over `\mathbf C_u` with the natural visible `SU(2)` action from left multiplication.

From the previous note:
$$
V \cong \mathbf 2
$$
as a complex `SU(2)` module.

So the existing parent geometry already gives exactly one complex weak doublet mode.

---

## Standard fermionic completion

Given any complex `SU(2)` module `V`, its fermionic Fock completion is the exterior algebra
$$
\Lambda^\bullet V
=
\Lambda^0 V \oplus \Lambda^1 V \oplus \Lambda^2 V.
$$

For `V \cong \mathbf 2`, one has the standard `SU(2)` decomposition
$$
\Lambda^0 \mathbf 2 \cong \mathbf 1,
\qquad
\Lambda^1 \mathbf 2 \cong \mathbf 2,
\qquad
\Lambda^2 \mathbf 2 \cong \det(\mathbf 2) \cong \mathbf 1.
$$

Therefore
$$
\Lambda^\bullet V \cong \mathbf 1 \oplus \mathbf 2 \oplus \mathbf 1.
$$

This is important because the desired auxiliary block already appears inside the first two sectors:
$$
\Lambda^{\le 1} V
:=
\Lambda^0 V \oplus \Lambda^1 V
\cong
\mathbf 1 \oplus \mathbf 2.
$$

So the existing quaternionic doublet does admit a standard enlargement whose low-occupancy sector is exactly the auxiliary representation needed by the projector/Casimir repair.

---

## Why this is structurally better than a bare direct sum

The abstract successful fit only needed a reducible auxiliary block
$$
\mathbf 1 \oplus \mathbf 2
$$
and the projector onto its trivial summand.

The vacuum-plus-doublet completion improves that picture in two ways:

1. the `\mathbf 2` part is no longer a free extra module; it is the existing quaternionic visible doublet `V`;
2. the `\mathbf 1` part is no longer an unrelated spectator line; it is the vacuum sector `\Lambda^0 V`.

So the candidate auxiliary block is not
$$
\text{arbitrary scalar line} \oplus \text{arbitrary doublet},
$$
but rather
$$
\text{vacuum of one quaternionic doublet mode}
\oplus
\text{single-occupancy sector of the same mode}.
$$

That is a materially stronger interpretation.

---

## Canonical projector from the number operator

Let `N` denote the fermion-number operator on `\Lambda^\bullet V`.

Its eigenvalues are:

- `0` on `\Lambda^0 V`;
- `1` on `\Lambda^1 V`;
- `2` on `\Lambda^2 V`.

So:

- on the truncated low-occupancy sector `\Lambda^{\le 1} V`, the vacuum projector is simply
  $$
  P_{\mathrm{vac}} = \mathbf 1 - N;
  $$
- on the full Fock space `\Lambda^\bullet V`, the projector onto `\Lambda^0 V` is the polynomial
  $$
  P_{\mathrm{vac}}
  =
  \mathbf 1 - \frac32 N + \frac12 N^2,
  $$
  since this equals `1` at `N=0` and `0` at `N=1,2`.

So if the physical auxiliary block is the low-occupancy part of a quaternionic-doublet completion, then the fitted projector
$$
P_{\mathrm{aux},0}
$$
can be read as a canonical vacuum projector.

That is another real improvement:

> the projector term becomes vacuum-versus-single-occupancy selection for one quaternionic doublet mode.

---

## Hypercharge reading under this candidate

On the successful unified carrier, the fitted operator was
$$
Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}.
$$

Under the present candidate, this becomes
$$
Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{vac}}
$$
on the low-occupancy auxiliary completion.

Then the previous slot assignment acquires a concrete interpretation:

- the left-handed doublet sector sits in the auxiliary vacuum sector;
- the right-handed singlet sector sits in the auxiliary one-particle sector;
- the projector term shifts only the vacuum sector.

So the earlier algebraic fit can now be read as:

> left-handed states are "no auxiliary excitation" states, while right-handed singlets are "one auxiliary quaternionic-doublet excitation" states.

This is not yet a theorem, and it is not yet a full spectrum closure. The later screen `kernels/even-line-exotic-branch-obstruction.md` shows that the auxiliary vacuum line still carries an unwanted complementary `T2` doublet sector with exotic charges unless an extra branch-selection or decoupling rule is added. So this note should be read as a candidate **source mechanism** for the auxiliary `\mathbf 1 \oplus \mathbf 2`, not as a finished physical spectrum.

---

## What still has to be explained

This candidate does **not** finish the job.

The main remaining burden is now precise:

1. why the physical auxiliary carrier should be the truncated sector
   $$
   \Lambda^{\le 1} V = \Lambda^0 V \oplus \Lambda^1 V
   $$
   rather than the full Fock space
   $$
   \Lambda^\bullet V = \mathbf 1 \oplus \mathbf 2 \oplus \mathbf 1;
   $$
2. what becomes of the top wedge sector
   $$
   \Lambda^2 V \cong \mathbf 1;
   $$
3. whether that extra singlet is projected out, decoupled, already identified with another scalar sector, or physically forbidden by some selection rule.

So this note does not close the auxiliary problem. It changes it from

> where could `\mathbf 1 \oplus \mathbf 2` come from at all?

to

> can the auxiliary block be identified with the vacuum-plus-single-occupancy sector of the existing quaternionic doublet, and if so, what controls the fate of the top wedge singlet?

That is a narrower and more structured problem.

---

## Best current status

This is the best concrete candidate now on the table for the auxiliary block:

$$
\mathbf 1 \oplus \mathbf 2
\cong
\Lambda^0 H(u,v) \oplus \Lambda^1 H(u,v)
$$
with
$$
P_{\mathrm{aux},0} = P_{\mathrm{vac}}.
$$

It has three advantages over the previous abstract repair:

1. it reuses the existing quaternionic doublet rather than inventing a new `\mathbf 2`;
2. it gives the trivial summand a canonical interpretation as a vacuum sector;
3. it replaces the raw projector by a standard number-operator projector.

Its costs are equally clear:

- one must justify why the complementary `T2` vacuum branch is removed, identified, or decoupled;
- one must justify the low-occupancy truncation or explain the fate of the top wedge singlet.

---

## What is now established

At the current kernel level, the following statement is now finite:

> the smallest standard fermionic completion of the existing quaternionic doublet contains a canonical low-occupancy sector `\Lambda^0 V \oplus \Lambda^1 V \cong \mathbf 1 \oplus \mathbf 2`, and on that candidate auxiliary block the projector term may be re-read as the vacuum projector.

This is a real candidate mechanism, not merely a symbolic relabeling.

---

## What remains open

The next question is:

> is there a principled reason, internal to the `Spin(2,3)` / octonionic reduction story, to keep the vacuum-plus-single-occupancy sector and discard or neutralize the top wedge singlet?

That is the sharpest next task if this candidate is pursued.
