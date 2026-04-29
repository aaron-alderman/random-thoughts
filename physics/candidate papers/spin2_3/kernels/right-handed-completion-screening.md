# Right-Handed Completion: Why `T2` Duplication Is Not Enough

## Purpose

The last branching note closed the bare left-handed seed:

$$
T1 \otimes (\mathbf 3 \oplus \mathbf 1).
$$

On that seed, matching the usual quark/lepton doublet charges forces

$$
Y = \frac12 Q7
$$

and leaves no independent visible role for `J^{01}`.

So the next finite question is:

> what is the first enlargement on which `J^{01}` could become nontrivial, and can that enlargement already supply the right-handed completion?

This note answers the first obvious trial case. The answer is no.

---

## The consistency target

Take the left-handed seed as fixed:

$$
Q_L : (\mathbf 3,\mathbf 2)_{1/6},
\qquad
L_L : (\mathbf 1,\mathbf 2)_{-1/2}.
$$

The anomaly-cancellation equations for a one-generation completion with singlets

$$
u_R : (\mathbf 3,\mathbf 1)_{y_u},
\qquad
d_R : (\mathbf 3,\mathbf 1)_{y_d},
\qquad
e_R : (\mathbf 1,\mathbf 1)_{y_e},
\qquad
\nu_R : (\mathbf 1,\mathbf 1)_{y_\nu}
$$

imply:

$$
y_u + y_d = \frac13,
$$
$$
y_e + y_\nu = -1,
$$

and, after combining the cubic condition with the two linear ones,

$$
y_u y_d - y_e y_\nu = -\frac29.
$$

So anomaly cancellation does not yet prove a unique completion in full generality, but it does sharply constrain the target.

In the special case

$$
y_\nu = 0,
$$

one gets

$$
y_e = -1,
\qquad
y_u y_d = -\frac29,
\qquad
y_u + y_d = \frac13,
$$

which forces

$$
\{y_u,y_d\} = \left\{\frac23,-\frac13\right\}.
$$

So the usual Standard-Model-shaped right-handed completion is recovered, up to exchanging `u_R` and `d_R`.

That is the consistency target the geometry must eventually meet.

---

## The first obvious trial enlargement

The smallest static enlargement beyond the bare left-handed seed is the naive sector doubling

$$
\mathcal H_{\mathrm{trial}}
=
(T1 \oplus T2) \otimes (\mathbf 3 \oplus \mathbf 1).
$$

This is the first place where `J^{01}` could in principle matter, because it takes values `-1/2` on `T1` and `+1/2` on `T2`.

Under the product action of `SU(3) x K`, one gets

$$
\mathcal H_{\mathrm{trial}}
=
(\mathbf 3,\mathbf 2)_{-1/2}
\oplus
(\mathbf 1,\mathbf 2)_{-1/2}
\oplus
(\mathbf 3,\mathbf 2)_{+1/2}
\oplus
(\mathbf 1,\mathbf 2)_{+1/2}.
$$

This already gives the first obstruction:

- every state is still a weak `SU(2)` doublet;
- there are no `(\mathbf 3,\mathbf 1)` slots;
- there are no `(\mathbf 1,\mathbf 1)` slots.

So if the `SU(2)` factor in `K = U(1) x SU(2)` is the physical weak group, then `T2` duplication alone cannot literally be the right-handed singlet completion.

That failure occurs before hypercharge is even discussed.

---

## Hypercharge on the doubled trial space

Now keep the same hypercharge ansatz

$$
Y = a J^{01} + b Q7
$$

with the same natural `SU(3)`-invariant traceless grading on `\mathbf 3 \oplus \mathbf 1`,

$$
Q7 = \mathrm{diag}\!\left(\frac13,\frac13,\frac13,-1\right).
$$

Then the four charge values on `\mathcal H_{\mathrm{trial}}` are:

$$
Y(T1,\mathbf 3) = -\frac a2 + \frac b3,
$$
$$
Y(T1,\mathbf 1) = -\frac a2 - b,
$$
$$
Y(T2,\mathbf 3) = +\frac a2 + \frac b3,
$$
$$
Y(T2,\mathbf 1) = +\frac a2 - b.
$$

If we insist that the `T1` states remain the usual left-handed quark and lepton doublets,

$$
Y(T1,\mathbf 3) = \frac16,
\qquad
Y(T1,\mathbf 1) = -\frac12,
$$

then the same two equations as before immediately give

$$
a = 0,
\qquad
b = \frac12.
$$

So the `T2` charges become

$$
Y(T2,\mathbf 3) = \frac16,
\qquad
Y(T2,\mathbf 1) = -\frac12.
$$

This is the second obstruction:

- once the left-handed seed is fixed, the naive doubled space still does not make `J^{01}` visible as an independent hypercharge ingredient;
- the `T2` copy inherits the same charge values as `T1`;
- so the doubled trial space fails not only at the weak-representation level, but also at the charge-splitting level.

---

## What this means for `J^{01}`

The result is narrower than "the hypercharge ansatz fails."

What it actually says is:

> the first obvious place where `J^{01}` could matter, namely `(T1 \oplus T2) \otimes (\mathbf 3 \oplus \mathbf 1)`, is still too small.

So the first genuinely nontrivial `J^{01}` role must enter only after a larger enlargement, for example one that adds:

- distinct color-triplet singlet slots for the up-type and down-type completion;
- distinct lepton singlet slots for charged and neutral completion;
- or another mechanism that converts the current doublet-level static carrier into weak singlets.

Under the current product reading `SU(3) x K`, that extra structure cannot be supplied by `T2` duplication alone.

---

## What is now established

The following points are now closed within the present static framework:

1. the minimal right-handed consistency target is sharply constrained by anomaly cancellation, and with `y_\nu = 0` it reproduces the usual
   $$
   \left(\frac23,-\frac13,-1,0\right)
   $$
   hypercharge pattern up to the `u/d` swap;
2. the naive enlargement
   $$
   (T1 \oplus T2) \otimes (\mathbf 3 \oplus \mathbf 1)
   $$
   contains only weak doublets under the current `SU(3) x K` reading, so it cannot literally be the right-handed singlet completion;
3. matching the left-handed `T1` charges on that doubled space still forces
   $$
   a = 0,
   \qquad
   b = \frac12,
   $$
   so `J^{01}` remains invisible there as an independent hypercharge parameter.

---

## What remains open

This note does **not** construct the correct enlarged static carrier. It only rules out the first obvious one.

So the next representation-theory problem is now precise:

> find the smallest enlargement beyond `(T1 \oplus T2) \otimes (\mathbf 3 \oplus \mathbf 1)` that
> 1. produces weak singlet slots,
> 2. distinguishes up-type from down-type color triplets,
> 3. distinguishes charged from neutral lepton singlets,
> 4. and makes `J^{01}` enter nontrivially in the hypercharge assignment.

That is the right next blocker on the static side.
