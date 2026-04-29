# `W3` / `kappa_u` Sign Correlation

## Purpose

This note closes the finite calculation that was left open in the topological kernel:

- how the sign of the DIII winding number `W3` tracks the sign of the transport coupling `kappa_u`.

The result is narrower than "topology derives `kappa_u > 0`." What it establishes is:

> `W3` and `kappa_u` flip under the same global orientation reversal, so their **relative sign convention** is fixed once one physical orientation is chosen.

That is enough to remove the sign-correlation item as a free ambiguity. It is **not** enough to derive which orientation is physically selected.

---

## Input 1: the DIII winding sign flips under `q -> q^\dagger`

In the DIII paper, the reduced chiral Hamiltonian is

$$
Q(X)=
\begin{pmatrix}
0 & q(X) \\
q(X)^\dagger & 0
\end{pmatrix},
$$

with

$$
q(X)=X_0\mathbf{1}_2-i(X_1\sigma^1+X_2\sigma^2+X_3\sigma^3).
$$

The paper already proves that, in the current winding convention,

$$
W_3[q] = -1,
$$

and also records that:

- replacing `q` by `q^\dagger` flips the sign;
- reversing the orientation on `S^3` flips the sign.

So

$$
W_3[q^\dagger] = +1
$$

in the same convention.

This is the topological `Z2` we need.

---

## Input 2: the transport sign flips under `u -> -u`

The discrete-symmetry ledger already records:

$$
u \mapsto -u
\qquad \Longrightarrow \qquad
\kappa_u \mapsto -\kappa_u.
$$

This is the transport-side `Z2`.

So the remaining issue is whether the topological sign flip and the transport sign flip are the same global orientation reversal in the corpus sign dictionary.

---

## Reduced orientation flip sends `q` to `q^\dagger`

The reduced sector split is the `J^{01}` decomposition

$$
\mathbf 4 = T1 \oplus T2.
$$

In the chiral basis used in the DIII paper, the Hamiltonian is off-diagonal with upper-right block `q` and lower-left block `q^\dagger`.

Now swap the two chiral sectors by the permutation matrix

$$
P =
\begin{pmatrix}
0 & \mathbf 1_2 \\
\mathbf 1_2 & 0
\end{pmatrix}.
$$

Then

$$
P^{-1}Q(X)P
=
\begin{pmatrix}
0 & q(X)^\dagger \\
q(X) & 0
\end{pmatrix}.
$$

So the reduced orientation flip that swaps the two `J^{01}` sectors sends the topological block

$$
q \longleftrightarrow q^\dagger.
$$

Because `W_3[q^\dagger] = -W_3[q]`, the reduced orientation flip reverses the winding sign.

---

## Global orientation dictionary

The corpus already treats the remaining sign ambiguity as a **common global orientation issue** involving:

1. the upstream orientation of `u`,
2. the reduced sector naming / orientation,
3. the readout arrow.

Within that dictionary:

- `u -> -u` flips `kappa_u`;
- the induced reduced orientation flip swaps `T1 <-> T2`;
- the reduced topological block changes `q <-> q^\dagger`;
- therefore the winding sign flips `W3 -> -W3`.

So under the common global orientation reversal,

$$
(W_3,\kappa_u) \mapsto (-W_3,-\kappa_u).
$$

This is the precise sign-correlation statement.

---

## What is now established

The following statement is now closed:

> once the corpus fixes a physical orientation convention, the sign of `W3` and the sign of `kappa_u` are no longer independent; they track the same global `Z2`.

Equivalently:

- constructive and inverted transport are exchanged by the same global reversal that exchanges `W3 = +1` and `W3 = -1`;
- the relative sign convention between topology and transport is fixed.

In particular, if one adopts the operational orientation rule

$$
\kappa_u > 0
$$

for the physical readout branch, then one should normalize the topological sign so that the same physical branch is assigned

$$
W_3 = +1
$$

even though the current paper’s raw convention gives `W_3[q] = -1` for the un-reoriented block.

This is not a contradiction. It is just the statement that the paper’s raw winding convention and the physical readout orientation need one common sign choice.

---

## What is not established

This note does **not** prove:

- that topology alone derives `kappa_u > 0`;
- that the constructive branch is physically selected without extra readout / ambient / stability input;
- that the operational orientation rule has become a theorem.

Those stronger statements still belong to the orientation-upgrade files.

So the clean division is:

- **closed here:** relative sign tracking `W3 <-> kappa_u`;
- **still open elsewhere:** why the physical branch must be the constructive one.

---

## Bottom line

The sign-correlation problem is now reduced to a convention-matching statement rather than a missing calculation.

- `W3[q] = -1` and `W3[q^\dagger] = +1` in the current winding convention.
- `u -> -u` sends `kappa_u -> -kappa_u`.
- the reduced orientation flip swaps `q <-> q^\dagger`.
- therefore the common global orientation reversal sends
  $$
  (W_3,\kappa_u) \mapsto (-W_3,-\kappa_u).
  $$

So the repo can now safely say: the sign of `W3` tracks the sign of `kappa_u` once the physical orientation is fixed, but topology does not yet determine which orientation is physical.
