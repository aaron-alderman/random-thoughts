# Minimal Right-Handed Singlet Candidate and the `J^{01}` Tension

## Purpose

The previous screening note showed that

$$
(T1 \oplus T2) \otimes (\mathbf 3 \oplus \mathbf 1)
$$

is still too small:

- it contains only weak doublets;
- it cannot literally supply the right-handed singlet completion;
- it still leaves `J^{01}` invisible in hypercharge once the left-handed `T1` seed is fixed.

So the next finite question is:

> what is the smallest algebraic repair that can even produce weak singlets?

This note answers that question and then checks its hypercharge consequences.

---

## Minimal repair: add one more weak doublet factor

Under the current `K = U(1) x SU(2)` reading, the obstruction in the previous note came from one simple fact:

- `T1` and `T2` are both weak doublets;
- tensoring them only with color/internal factors on which the weak `SU(2)` acts trivially can never produce weak singlets.

So the smallest repair is to add one more `SU(2)` doublet factor, call it

$$
S_{\mathrm{aux}} \cong \mathbf 2.
$$

At the purely algebraic level this is the first place where

$$
\mathbf 2 \otimes \mathbf 2 = \mathbf 1 \oplus \mathbf 3
$$

can create weak singlets.

The current corpus already contains a natural parent-side source candidate for such a doublet factor: the visible quaternionic carrier `S_{\mathrm{vis}} \cong \mathbf C^2_u` inside the local slice `H(u,v)`. This note does **not** claim that a second such factor is already physically derived. It only uses the representation algebra.

---

## The candidate carrier

Take

$$
\mathcal H_{\mathrm{cand}}
=
(T1 \oplus T2) \otimes S_{\mathrm{aux}} \otimes (\mathbf 3 \oplus \mathbf 1),
$$

with `S_{\mathrm{aux}}` neutral under `J^{01}` and `Q7`, and transforming as a weak doublet under the same `SU(2)`.

Since

$$
T1 = (\mathbf 2,-1/2),
\qquad
T2 = (\mathbf 2,+1/2),
$$

one gets

$$
T1 \otimes S_{\mathrm{aux}} = (\mathbf 1,-1/2) \oplus (\mathbf 3,-1/2),
$$
$$
T2 \otimes S_{\mathrm{aux}} = (\mathbf 1,+1/2) \oplus (\mathbf 3,+1/2).
$$

So the weak-singlet part of `\mathcal H_{\mathrm{cand}}` is

$$
(\mathbf 3,\mathbf 1)_{-1/2}
\oplus
(\mathbf 3,\mathbf 1)_{+1/2}
\oplus
(\mathbf 1,\mathbf 1)_{-1/2}
\oplus
(\mathbf 1,\mathbf 1)_{+1/2}.
$$

This is the first carrier in the current static line that has the right color/weak shape for

- one down-type color singlet slot,
- one up-type color singlet slot,
- one charged lepton singlet slot,
- one neutral lepton singlet slot.

So one extra weak doublet factor is the minimal algebraic ingredient needed to create right-handed-style singlets at all.

---

## Hypercharge on the singlet candidate

Keep the same hypercharge ansatz

$$
Y = a J^{01} + b Q7,
$$

with the same natural `SU(3)`-invariant traceless grading on `\mathbf 3 \oplus \mathbf 1`,

$$
Q7 = \mathrm{diag}\!\left(\frac13,\frac13,\frac13,-1\right).
$$

On the weak-singlet sector of `\mathcal H_{\mathrm{cand}}`, the four charge values are:

$$
Y(\mathbf 3,\mathbf 1)_{-1/2} = -\frac a2 + \frac b3,
$$
$$
Y(\mathbf 3,\mathbf 1)_{+1/2} = +\frac a2 + \frac b3,
$$
$$
Y(\mathbf 1,\mathbf 1)_{-1/2} = -\frac a2 - b,
$$
$$
Y(\mathbf 1,\mathbf 1)_{+1/2} = +\frac a2 - b.
$$

Now match the standard one-generation right-handed target

$$
d_R : (\mathbf 3,\mathbf 1)_{-1/3},
\qquad
u_R : (\mathbf 3,\mathbf 1)_{+2/3},
$$
$$
e_R : (\mathbf 1,\mathbf 1)_{-1},
\qquad
\nu_R : (\mathbf 1,\mathbf 1)_0.
$$

If we identify the `-1/2` singlet branch with `(d_R,e_R)` and the `+1/2` branch with `(u_R,\nu_R)`, the equations are

$$
-\frac a2 + \frac b3 = -\frac13,
\qquad
+\frac a2 + \frac b3 = \frac23.
$$

Subtracting gives

$$
a = 1,
$$

and then averaging gives

$$
\frac b3 = \frac16
\qquad\Longrightarrow\qquad
b = \frac12.
$$

The lepton singlets then come out automatically:

$$
-\frac12 - \frac12 = -1,
\qquad
\frac12 - \frac12 = 0.
$$

So this candidate does exactly realize the standard right-handed singlet hypercharges with

$$
a = 1,
\qquad
b = \frac12.
$$

Up to the global orientation reversal swapping `T1 <-> T2`, this is the unique fit.

This is the first place in the static line where `J^{01}` becomes genuinely nontrivial and useful.

---

## Comparison with the left-handed seed

This is where the next obstruction appears.

The earlier left-handed calculation on the bare seed

$$
T1 \otimes (\mathbf 3 \oplus \mathbf 1)
$$

forced

$$
a = 0,
\qquad
b = \frac12.
$$

But the minimal right-handed singlet candidate forces

$$
a = 1,
\qquad
b = \frac12
$$

up to the same global sign flip on `a`.

So:

- the `Q7` normalization is stable;
- the `J^{01}` coefficient is not.

Therefore a single global coefficient pair `(a,b)` cannot simultaneously fit:

1. the naive bare left-handed seed `T1 \otimes (\mathbf 3 \oplus \mathbf 1)`, and
2. the minimal singlet candidate `(T1 \oplus T2) \otimes S_{\mathrm{aux}} \otimes (\mathbf 3 \oplus \mathbf 1)`.

That is the new tension.

---

## What this means

The result is narrower than "the hypercharge ansatz fails." In fact it shows something better:

1. the right-handed singlet sector is no longer mysterious at the representation-theory level;
2. one extra weak doublet factor is enough to make `J^{01}` enter with exactly the right charge splitting;
3. the real problem has moved to **unifying** the left-handed and right-handed embeddings under one global hypercharge operator.

So the live structural alternatives are now clear:

- the left-handed seed should also be embedded in a larger carrier before matching;
- or the hypercharge ansatz must be enlarged beyond `a J^{01} + b Q7`;
- or the present identification of the bare left-handed seed is only a partial projection of a larger static object.

---

## What is now established

The following points are now closed within the current algebraic line:

1. one extra weak doublet factor is the minimal algebraic ingredient needed to produce weak singlets from the present `T1/T2` framework;
2. on that minimal singlet candidate, the standard right-handed one-generation charges are reproduced exactly by
   $$
   Y = J^{01} + \frac12\,Q7
   $$
   up to the global orientation reversal `J^{01} -> -J^{01}`;
3. the coefficient `b = 1/2` is consistent with the earlier left-handed fit, but the coefficient of `J^{01}` is not;
4. so the first serious hypercharge problem is no longer "can `J^{01}` ever matter?" It can. The real problem is "how are the left-handed and right-handed sectors embedded so that one global `Y` works?"

---

## What remains open

This note does **not** prove that `S_{\mathrm{aux}}` is already physically present in the framework. It only identifies the smallest kind of extra structure that would work algebraically.

So the next static/consistency question is now:

> what is the smallest unified carrier containing both the left-handed doublet seed and the right-handed singlet candidate on which one global hypercharge operator is well defined?

That is the right next blocker.
