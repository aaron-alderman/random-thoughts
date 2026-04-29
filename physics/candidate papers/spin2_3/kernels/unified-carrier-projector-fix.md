# Unified Carrier Projector Fix: The Minimal Three-Term Hypercharge Operator

## Purpose

The last note proved a clean no-go:

$$
(T1 \oplus T2) \otimes (\mathbf 1 \oplus S_{\mathrm{aux}}) \otimes (\mathbf 3 \oplus \mathbf 1)
$$

cannot support one global

$$
Y = a J^{01} + b Q7
$$

if `S_{\mathrm{aux}}` is neutral under both `J^{01}` and `Q7`.

The natural next question is:

> what is the smallest algebraic enlargement of the hypercharge operator that removes this conflict while preserving the successful `Q7` normalization and `J^{01}` branch splitting?

This note gives that enlargement explicitly.

---

## Why the extra operator cannot live on `S_aux` alone

The auxiliary factor `S_{\mathrm{aux}}` is a weak `SU(2)` doublet:

$$
S_{\mathrm{aux}} \cong \mathbf 2.
$$

If we insist that any extra term in `Y` commute with the weak `SU(2)`, then by Schur's lemma any operator on the irreducible doublet `\mathbf 2` is a scalar multiple of the identity.

So there is no nontrivial `SU(2)`-commuting grading living on `S_{\mathrm{aux}}` alone.

The first place a nontrivial commuting operator can appear is on the reducible auxiliary block

$$
\mathbf 1 \oplus S_{\mathrm{aux}},
$$

where one may distinguish the trivial summand from the doublet summand.

That is exactly the minimal new ingredient.

---

## The auxiliary projector

Let

$$
P_{\mathrm{aux},0}
$$

denote the projector onto the trivial summand `\mathbf 1` inside

$$
\mathbf 1 \oplus S_{\mathrm{aux}}.
$$

So:

- `P_{\mathrm{aux},0} = 1` on the `\mathbf 1` summand;
- `P_{\mathrm{aux},0} = 0` on the `S_{\mathrm{aux}}` summand.

This operator commutes with the weak `SU(2)` action, because it acts as a scalar on each irreducible summand of `\mathbf 1 \oplus \mathbf 2`.

Now enlarge the hypercharge ansatz to

$$
Y = a J^{01} + b Q7 + c P_{\mathrm{aux},0}.
$$

This is the minimal three-term candidate.

---

## Charges on the unified carrier

Keep the same unified carrier

$$
\mathcal H_{\mathrm{unif}}
=
(T1 \oplus T2) \otimes (\mathbf 1 \oplus S_{\mathrm{aux}}) \otimes (\mathbf 3 \oplus \mathbf 1),
$$

with the same `Q7` normalization

$$
Q7 = \mathrm{diag}\!\left(\frac13,\frac13,\frac13,-1\right).
$$

### Left-handed doublet sector

Take the visible left-handed doublets from the `\mathbf 1` part of `\mathbf 1 \oplus S_{\mathrm{aux}}` on the `T1` branch. Then

$$
Q_L : -\frac a2 + \frac b3 + c,
$$
$$
L_L : -\frac a2 - b + c.
$$

Matching the standard left-handed values

$$
Q_L = \frac16,
\qquad
L_L = -\frac12
$$

gives

$$
b = \frac12,
$$

and then

$$
-\frac a2 + c = 0
\qquad\Longrightarrow\qquad
c = \frac a2.
$$

So the projector term compensates exactly the `J^{01}` shift on the left-handed doublet sector.

### Right-handed singlet sector

Take the right-handed singlets from the `S_{\mathrm{aux}}` singlet channel. Since `P_{\mathrm{aux},0}=0` there, their charges are:

$$
d_R : -\frac a2 + \frac b3,
$$
$$
u_R : +\frac a2 + \frac b3,
$$
$$
e_R : -\frac a2 - b,
$$
$$
\nu_R : +\frac a2 - b.
$$

Matching the standard values

$$
d_R = -\frac13,
\qquad
u_R = \frac23,
\qquad
e_R = -1,
\qquad
\nu_R = 0
$$

gives

$$
a = 1,
\qquad
b = \frac12.
$$

Then the left-handed relation above forces

$$
c = \frac12.
$$

So the unified carrier admits the exact fit

$$
Y = J^{01} + \frac12\,Q7 + \frac12\,P_{\mathrm{aux},0}.
$$

That is the minimal algebraic repair.

---

## What this fit does not yet remove

The calculation above matches the desired charges on a selected slot assignment:

- left-handed doublets from the `T1` branch of the auxiliary `\mathbf 1`;
- right-handed singlets from the singlet channel inside `T1 \otimes S_{\mathrm{aux}}` and `T2 \otimes S_{\mathrm{aux}}`.

But the same auxiliary `\mathbf 1` also carries the complementary `T2` branch. On that branch,
$$
Y = \frac12 + \frac12 Q7 + \frac12,
$$
so one gets the extra weak-doublet charges
$$
(\mathbf 3,\mathbf 2)_{7/6}
\oplus
(\mathbf 1,\mathbf 2)_{1/2}.
$$

So this note closes the **slot-level** hypercharge fit, but not yet the full carrier spectrum. The residual even-line obstruction is recorded separately in `kernels/even-line-exotic-branch-obstruction.md`.

---

## Orientation partner

Under the common global orientation reversal that swaps `T1` and `T2`,

$$
J^{01} \mapsto -J^{01},
$$

while `Q7` and `P_{\mathrm{aux},0}` are unchanged as operators on the internal and auxiliary blocks.

So the orientation-partner fit is

$$
Y = -J^{01} + \frac12\,Q7 - \frac12\,P_{\mathrm{aux},0}
$$

if one simultaneously swaps which branch carries the left-handed and right-handed assignments.

So, up to the same global orientation flip already present elsewhere in the corpus, the coefficient pattern is fixed.

---

## What this resolves

This solves the finite algebraic problem left open by the previous notes.

The successful pattern is now:

- `Q7` carries the stable color-triplet versus singlet split with coefficient `1/2`;
- `J^{01}` carries the branch-odd up/down and charged/neutral splitting with coefficient `\pm 1`;
- `P_{\mathrm{aux},0}` corrects the left-handed doublet sector so that the same nonzero `J^{01}` coefficient no longer over-shifts it.

So the previous conflict

$$
a=0 \quad \text{vs} \quad a=\pm 1
$$

is not a proof that the framework needs a completely different charge story. It is only a proof that the two-term ansatz was too small on the unified carrier.

---

## What remains nontrivial

This note is algebraically clean, but it does not yet make the projector term physically safe.

The real remaining question is:

> why should the projector onto the trivial auxiliary summand be part of the physical hypercharge operator?

That is not answered just by matching charges.

So the burden has shifted again:

- the representation-theory obstruction is removed;
- the new issue is geometric or dynamical justification of `P_{\mathrm{aux},0}`.

---

## What is now established

The following points are now closed:

1. no nontrivial weak-`SU(2)`-commuting grading exists on the irreducible auxiliary doublet `S_{\mathrm{aux}}` alone;
2. the first nontrivial commuting auxiliary operator lives on the reducible block `\mathbf 1 \oplus S_{\mathrm{aux}}`, namely the projector `P_{\mathrm{aux},0}`;
3. on the unified carrier
   $$
   (T1 \oplus T2) \otimes (\mathbf 1 \oplus S_{\mathrm{aux}}) \otimes (\mathbf 3 \oplus \mathbf 1),
   $$
   the minimal three-term operator
   $$
   Y = J^{01} + \frac12\,Q7 + \frac12\,P_{\mathrm{aux},0}
   $$
   reproduces the standard one-generation left-handed and right-handed charges exactly on the selected slot assignment in the current orientation;
4. therefore the smallest unified-carrier obstruction is not fatal at the slot level: it is repaired by one projector term, though later notes show that extra complementary sectors still remain in the full carrier.

---

## What remains open

The next blocker is now much narrower:

> derive or justify `P_{\mathrm{aux},0}` from the parent geometry, the quaternionic reduction, or a principled operator-level selection rule, rather than treating it as a fitted bookkeeping term.

That is the right next task if the project stays on hypercharge.
