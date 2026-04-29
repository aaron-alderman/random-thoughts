# `G2 cap Spin(2,3)` and Its Compact Irrep Content

## Purpose

This note closes the literal group-intersection task from the roadmap:

- compute `G2 cap Spin(2,3)`;
- determine the compact irrep content relevant to the current reduction picture.

The result is narrower than the earlier hope. Under the current corpus assumptions, the literal common subgroup is only the compact overlap

$$
G_2 \cap \mathrm{Spin}(2,3) = K = U(1) \times SU(2)
$$

in the repo's working convention, with Lie algebra

$$
\mathfrak g_2 \cap \mathfrak{spin}(2,3) = \mathfrak u(2) = \mathfrak{su}(2) \oplus \mathfrak u(1).
$$

So the literal intersection does **not** itself contain an independent `SU(3) x SU(2) x U(1)`.

---

## Inputs already live in the corpus

Three ingredients are already in place elsewhere in the repo:

1. Fixing the preferred imaginary octonionic direction `u` reduces `G2` to its stabilizer
   $$
   \mathrm{Stab}_{G_2}(u) = SU(3).
   $$

2. On the reduced `Spin(2,3)` spinor, the maximal compact subgroup is
   $$
   K = U(1) \times SU(2),
   $$
   with decomposition
   $$
   \mathbf 4 = (\mathbf 2,-1/2) \oplus (\mathbf 2,+1/2).
   $$

3. The current compact-level bridge already identifies this reduced `K` action with parent-side data preserving the chosen `u`, so in the working corpus language
   $$
   K \subset \mathrm{Stab}_{G_2}(u) \subset G_2.
   $$

The third item is not a background theorem about arbitrary embeddings; it is the current bridge assumption/result of the repo. Under that assumption, the intersection calculation is finite.

---

## Compact-overlap argument

Let

$$
H := G_2 \cap \mathrm{Spin}(2,3).
$$

Then:

- `H` is compact, because it is a subgroup of the compact group `G2`;
- `K \subset H`, because the current corpus already places `K` inside both `G2` and `Spin(2,3)`;
- `K` is a maximal compact subgroup of `Spin(2,3)`.

Therefore a compact subgroup of `Spin(2,3)` containing `K` cannot be larger than `K`. So

$$
H = K.
$$

At Lie algebra level this gives

$$
\mathfrak g_2 \cap \mathfrak{spin}(2,3) = \mathfrak k = \mathfrak u(2).
$$

This is the clean structural answer.

---

## Global-form caveat

The repo usually writes the compact subgroup as

$$
K = U(1) \times SU(2)
$$

because that is the representation language used for the reduced spinor block split.

If one instead passes to the faithful compact image, there can be a common central `Z2` quotient:

$$
(U(1) \times SU(2))/\{(-1,-1)\} \cong U(2).
$$

So the safest global statement is:

- repo convention: `G2 cap Spin(2,3) = U(1) x SU(2)`;
- faithful compact image: the same overlap is effectively `U(2)`.

Nothing below depends on which of these equivalent compact forms one prefers; the local weight data is the same.

---

## Irrep content on the reduced spinor

On the reduced `Spin(2,3)` spinor, the common compact subgroup acts exactly as already recorded elsewhere:

$$
\mathbf 4 = (\mathbf 2,-1/2) \oplus (\mathbf 2,+1/2).
$$

So the literal overlap sees:

- one `SU(2)` doublet with `U(1)` charge `-1/2`;
- one `SU(2)` doublet with `U(1)` charge `+1/2`.

This is the whole compact content on the reduced spinor side.

---

## Irrep content inside the octonionic `SU(3)` carrier

After fixing `u`, the hidden remainder is

$$
u^\perp \cong \mathbf C^3,
$$

carrying the fundamental `\mathbf 3` of `SU(3) = \mathrm{Stab}_{G_2}(u)`.

The common compact subgroup is the standard `U(2)` inside `SU(3)`, embedded as block-diagonal matrices

$$
A \mapsto
\begin{pmatrix}
A & 0 \\
0 & (\det A)^{-1}
\end{pmatrix},
\qquad A \in U(2).
$$

So the `SU(3)` fundamental restricts as

$$
\mathbf 3 \downarrow_{U(2)} = \mathbf 2_{+1} \oplus \mathbf 1_{-2}.
$$

If one rescales the `U(1)` generator by `1/2` to match the reduced spinor convention used elsewhere in the repo, this becomes

$$
\mathbf 3 \downarrow_K = \mathbf 2_{+1/2} \oplus \mathbf 1_{-1}.
$$

Correspondingly,

$$
\bar{\mathbf 3} \downarrow_K = \mathbf 2_{-1/2} \oplus \mathbf 1_{+1},
$$

and the fixed octonionic direction gives an additional singlet

$$
\mathbf 1 \downarrow_K = \mathbf 1_0.
$$

So, under the literal compact overlap, the octonionic carrier decomposes only into:

- a doublet plus singlet from `\mathbf 3`,
- a doublet plus singlet from `\bar{\mathbf 3}`,
- one neutral singlet from the fixed `u` direction.

The full `SU(3)` symmetry is not visible inside the overlap; only its `U(2)` restriction is.

---

## What this closes

The following point is now closed:

> the literal common symmetry seen simultaneously by the current octonionic stabilizer and the reduced `Spin(2,3)` compact transport structure is only the compact `U(2)` sector.

Equivalently:

- the intersection is `U(1) x SU(2)` in repo convention;
- at Lie algebra level it is `u(2)`;
- the `SU(3)` carrier restricts to `2 + 1`, not to a fresh independent color-times-electroweak product inside the overlap.

So the earlier hope

> maybe the literal intersection already contains something like `SU(3) x SU(2) x U(1)`

should be retired in its current form.

---

## What remains open

This does **not** weaken the broader parent-geometry programme. It only clarifies where the useful structure can live.

What remains open is:

1. how the full octonionic stabilizer `SU(3) = \mathrm{Stab}_{G_2}(u)` couples to the reduced compact subgroup `K = U(1) x SU(2)` across the reduction map;
2. whether the noncompact part of `Spin(2,3)` also admits a canonical parent-side realization beyond the compact overlap;
3. whether the joint data `(SU(3), K, \mathcal R)` can organize the static matter ansatz without pretending that all of it sits inside one literal common subgroup.

So the correct structural picture is now:

- `SU(3)` comes from the full octonionic stabilizer of `u`;
- `U(1) x SU(2)` comes from the reduced compact transport symmetry;
- their literal overlap is only `U(2)`;
- phenomenological structure, if real, must come from the pair together with the reduction map, not from the intersection alone.

---

## Bottom line

The `G2 cap Spin(2,3)` task is straightforward only once one stops asking the intersection to do too much.

- Literal compact overlap: `U(1) x SU(2)` in repo convention, equivalently `U(2)` up to common center.
- Lie algebra overlap: `u(2)`.
- Reduced spinor content: `(\mathbf 2,-1/2) \oplus (\mathbf 2,+1/2)`.
- Octonionic `SU(3)` carrier under the overlap: `\mathbf 3 -> \mathbf 2_{+1/2} \oplus \mathbf 1_{-1}` up to the same `U(1)` normalization.

That is enough to remove the literal-intersection ambiguity. The next representation-theory question is no longer "does the overlap already contain the full gauge structure?" It is "how do the full `SU(3)` parent stabilizer and the reduced `K` action fit together across the reduction?"
