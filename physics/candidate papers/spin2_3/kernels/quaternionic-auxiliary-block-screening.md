# Quaternionic Slice Screening for the Auxiliary `1 + 2` Block

## Purpose

The previous two notes isolated the remaining hypercharge burden very sharply:

- the smallest unified carrier works algebraically once one allows
  $$
  Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0},
  $$
- and that projector can be rewritten canonically as the Casimir-zero projector if the auxiliary block is the reducible `SU(2)` module
  $$
  \mathbf 1 \oplus \mathbf 2.
  $$

So the live question is no longer whether the projector repair is algebraically available. It is:

> does the current parent-side quaternionic slice already contain the needed auxiliary `\mathbf 1 \oplus \mathbf 2` block?

This note gives the answer under the present scaffold: not yet.

---

## The natural `SU(2)` action already in the scaffold

The ambient-reduction scaffold already identifies the local quaternionic slice
$$
H(u,v) = \mathrm{span}_{\mathbf R}\{1,u,v,uv\}
$$
as the parent-side source of the visible `SU(2)` structure.

The key point there is:

- regard `H(u,v)` as a complex vector space over `\mathbf C_u` using right multiplication by `u`;
- let the visible `SU(2)` act by left multiplication with the imaginary quaternion units.

With the complex basis
$$
e_1 = 1,
\qquad
e_2 = v,
$$
the three left-multiplication generators act, up to the standard `i` convention from right multiplication by `u`, as the Pauli triplet:
$$
L_u \sim
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix},
\qquad
L_v \sim
\begin{pmatrix}
0 & 1\\
-1 & 0
\end{pmatrix},
\qquad
L_{uv} \sim
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}.
$$

So under the current natural action, `H(u,v)` is exactly the usual complex `SU(2)` doublet:
$$
H(u,v) \cong \mathbf 2
\qquad
\text{(as a complex `SU(2)` module over `\mathbf C_u`).}
$$

That is already valuable. It explains the visible weak-doublet carrier internally.

But it also means something restrictive:

> the current quaternionic slice gives an irreducible complex doublet, not a reducible complex `\mathbf 1 \oplus \mathbf 2`.

---

## Why no `\mathbf 1 \oplus \mathbf 2` appears under this action

On the complex carrier `H(u,v) \cong \mathbf 2`, any operator commuting with the full visible `SU(2)` action must commute with `L_u`, `L_v`, and `L_{uv}`.

Write a general complex-linear endomorphism as
$$
X =
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}.
$$

Then:

- commuting with `L_u` forces `b=c=0`, so `X` is diagonal;
- commuting with `L_v` then forces `a=d`.

Therefore
$$
X = \lambda\,\mathbf 1.
$$

So the commutant is scalar only. Equivalently, the current visible action on `H(u,v)` is irreducible.

This has an immediate consequence for the hypercharge problem:

> there is no nontrivial `SU(2)`-equivariant projector inside the current complex quaternionic carrier itself.

In particular, the auxiliary projector `P_{\mathrm{aux},0}` from the unified-carrier fit cannot be identified with a projector already present on `H(u,v)` under this natural left action.

---

## The tempting scalar-plus-triplet split is a different action

There is another familiar decomposition of quaternions:
$$
H(u,v) = \mathbf R\cdot 1 \oplus \mathrm{Im}\,H(u,v),
$$
with
$$
\mathrm{Im}\,H(u,v) = \mathrm{span}_{\mathbf R}\{u,v,uv\}.
$$

Under quaternionic conjugation or the adjoint `SU(2)` action, this gives the real decomposition
$$
\mathbf 1 \oplus \mathbf 3.
$$

But that is **not** the same module used elsewhere in the scaffold:

- it is a real scalar-plus-triplet package;
- it comes from the adjoint/conjugation action, not from the left-multiplication action that supplies the visible weak doublet;
- it does not produce the required complex reducible module `\mathbf 1 \oplus \mathbf 2`.

So the scalar-plus-triplet split does not solve the present problem. It belongs to a different representation package.

---

## What the screen closes

The current parent-side quaternionic story now has a clean status:

1. the local slice `H(u,v)` does supply a natural visible `SU(2)` doublet carrier;
2. under that same natural action, `H(u,v)` is irreducible as a complex module and therefore contains no nontrivial equivariant projector;
3. the familiar scalar/imaginative split of quaternions belongs to a different real adjoint action and gives `\mathbf 1 \oplus \mathbf 3`, not the needed complex `\mathbf 1 \oplus \mathbf 2`.

So the current scaffold does **not** yet derive the auxiliary reducible block required by the projector/Casimir hypercharge repair.

---

## Best current interpretation

The disciplined reading is now:

- the quaternionic slice still explains why a weak-doublet factor was the first natural place to look;
- the successful three-term hypercharge fit remains algebraically valid;
- but the present quaternionic parent geometry does not by itself justify identifying the auxiliary block with `H(u,v)`.

So the live options are narrower than before.

Either:

1. the auxiliary `\mathbf 1 \oplus \mathbf 2` block is a genuinely larger carrier than the bare quaternionic visible slice;
2. the left-handed embedding should be enlarged or repackaged so that the current projector fix is replaced by a different global operator;
3. or a new parent-side selection rule / auxiliary sector must be added beyond the current `H(u,v)` scaffold.

---

## What is now established

The following statement is now closed at the current kernel level:

> under the present ambient-reduction scaffold, the natural quaternionic slice `H(u,v)` furnishes the visible irreducible complex `SU(2)` doublet, but it does not itself realize the reducible complex auxiliary module `\mathbf 1 \oplus \mathbf 2` whose Casimir-zero projector appears in the successful hypercharge repair.

That is a useful negative result. It tells us exactly what the current parent-side geometry does **not** yet provide.

---

## What remains open

The next question is no longer "does the existing quaternionic slice already contain the right auxiliary module?" It does not.

The next question is:

> what is the smallest principled enlargement or reinterpretation of the parent-side carrier that can produce the auxiliary `\mathbf 1 \oplus \mathbf 2` block, or else remove the need for it?
