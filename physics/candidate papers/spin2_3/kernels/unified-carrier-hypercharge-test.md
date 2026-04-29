# Unified Carrier Test: The Neutral-`S_aux` No-Go

## Purpose

The previous note identified the first algebraic carrier that can host right-handed-style weak singlets:

$$
(T1 \oplus T2) \otimes S_{\mathrm{aux}} \otimes (\mathbf 3 \oplus \mathbf 1),
$$

with `S_{\mathrm{aux}} \cong \mathbf 2`.

But that still left the real question open:

> can one embed both the left-handed doublet seed and the right-handed singlet sector into one small unified carrier so that a single global
> $$
> Y = a J^{01} + b Q7
> $$
> works on all of them at once?

The first obvious unified test carrier is

$$
\mathcal H_{\mathrm{unif}}
=
(T1 \oplus T2) \otimes (\mathbf 1 \oplus S_{\mathrm{aux}}) \otimes (\mathbf 3 \oplus \mathbf 1).
$$

This note computes that case exactly.

---

## Assumptions of the test

This test uses the smallest natural extension of the previous notes:

1. `T1` and `T2` carry the usual `J^{01}` eigenvalues `-1/2` and `+1/2`;
2. `Q7` is the same `SU(3)`-invariant traceless grading on `\mathbf 3 \oplus \mathbf 1`,
   $$
   Q7 = \mathrm{diag}\!\left(\frac13,\frac13,\frac13,-1\right);
   $$
3. `S_{\mathrm{aux}}` is a weak `SU(2)` doublet;
4. `S_{\mathrm{aux}}` is neutral under `J^{01}` and `Q7`.

The fourth point is the crucial test assumption. If the no-go below appears, that is where the next modification must enter.

---

## Decomposition of the unified carrier

Because

$$
\mathbf 2 \otimes (\mathbf 1 \oplus \mathbf 2)
=
\mathbf 2 \oplus \mathbf 1 \oplus \mathbf 3,
$$

each `T` sector contributes:

$$
T1 \otimes (\mathbf 1 \oplus S_{\mathrm{aux}})
=
(\mathbf 2,-1/2) \oplus (\mathbf 1,-1/2) \oplus (\mathbf 3,-1/2),
$$
$$
T2 \otimes (\mathbf 1 \oplus S_{\mathrm{aux}})
=
(\mathbf 2,+1/2) \oplus (\mathbf 1,+1/2) \oplus (\mathbf 3,+1/2).
$$

So `\mathcal H_{\mathrm{unif}}` contains:

- left-handed-shaped weak doublets from the `\mathbf 1` part of `\mathbf 1 \oplus S_{\mathrm{aux}}`,
- right-handed-shaped weak singlets from the `S_{\mathrm{aux}}` singlet channel,
- and extra weak triplets as spectators.

At the level of representation shape alone, this is the first small carrier that contains both types of slots simultaneously.

---

## Left-handed equations

If the left-handed quark/lepton doublets are taken from one fixed `J^{01}` branch, their charges are either

$$
Y_L^{(-)}(\mathbf 3,\mathbf 2) = -\frac a2 + \frac b3,
\qquad
Y_L^{(-)}(\mathbf 1,\mathbf 2) = -\frac a2 - b,
$$

or

$$
Y_L^{(+)}(\mathbf 3,\mathbf 2) = +\frac a2 + \frac b3,
\qquad
Y_L^{(+)}(\mathbf 1,\mathbf 2) = +\frac a2 - b.
$$

Matching the usual left-handed targets

$$
Q_L : (\mathbf 3,\mathbf 2)_{1/6},
\qquad
L_L : (\mathbf 1,\mathbf 2)_{-1/2}
$$

forces, in either branch choice,

$$
b = \frac12,
\qquad
a = 0.
$$

So the left-handed sector again kills the `J^{01}` contribution if it is embedded as a pure `T1` or pure `T2` doublet branch.

---

## Right-handed equations

Now take the weak singlets from the `S_{\mathrm{aux}}` singlet channel.

Their charges are:

$$
Y_R^{(-)}(\mathbf 3,\mathbf 1) = -\frac a2 + \frac b3,
\qquad
Y_R^{(-)}(\mathbf 1,\mathbf 1) = -\frac a2 - b,
$$
$$
Y_R^{(+)}(\mathbf 3,\mathbf 1) = +\frac a2 + \frac b3,
\qquad
Y_R^{(+)}(\mathbf 1,\mathbf 1) = +\frac a2 - b.
$$

To reproduce the standard one-generation right-handed pattern, one branch must carry

$$
d_R : -\frac13,
\qquad
e_R : -1,
$$

and the opposite branch must carry

$$
u_R : \frac23,
\qquad
\nu_R : 0.
$$

Those equations force

$$
b = \frac12,
\qquad
a = \pm 1,
$$

with the sign determined by which branch is identified as the up-type/neutral branch.

So the right-handed sector requires a nonzero `J^{01}` coefficient, exactly as in the previous note.

---

## The no-go

Combine the two results:

- left-handed pure-branch doublets force
  $$
  a = 0,
  \qquad
  b = \frac12;
  $$
- right-handed singlets force
  $$
  a = \pm 1,
  \qquad
  b = \frac12.
  $$

Therefore:

> on the unified carrier
> $$
> (T1 \oplus T2) \otimes (\mathbf 1 \oplus S_{\mathrm{aux}}) \otimes (\mathbf 3 \oplus \mathbf 1),
> $$
> with `S_{\mathrm{aux}}` neutral under `J^{01}` and `Q7`, there is no single global coefficient pair `(a,b)` for which
> $$
> Y = a J^{01} + b Q7
> $$
> reproduces both the standard left-handed doublet charges and the standard right-handed singlet charges.

This is a clean algebraic no-go.

---

## What fails, exactly

The important point is what the no-go does **not** say.

It does not say:

- the unified carrier is too small to contain the right representation shapes;
- `J^{01}` can never help;
- `Q7` was the wrong normalization.

In fact:

- the carrier is large enough to contain both doublets and singlets;
- `J^{01}` is exactly what makes the right-handed singlet fit work;
- `b = 1/2` is stable across all successful local fits.

What fails is only this:

> the left-handed sector, when embedded as a pure `J^{01}` branch with neutral auxiliary factor, does not tolerate the same nonzero `J^{01}` coefficient that the right-handed sector needs.

So the obstruction is now sharply localized.

---

## Consequences

There are three immediate ways the framework could escape this no-go:

1. **Enlarge the embedding of the left-handed sector.**
   The bare left-handed doublets may need to live in a larger carrier rather than in the pure `\mathbf 1` part of `\mathbf 1 \oplus S_{\mathrm{aux}}`.

2. **Give `S_{\mathrm{aux}}` extra grading data.**
   If the auxiliary factor carries its own nontrivial charge under a new commuting grading, then `Y` may need a third term beyond `a J^{01} + b Q7`.

3. **Treat the visible left-handed seed as a projection of a larger operator-level structure.**
   Then the charge fit on the bare seed would no longer be the full global constraint.

The current note does not choose among these. It only shows that the neutral-`S_{\mathrm{aux}}` unified carrier is not enough.

---

## What is now established

The following points are now closed:

1. the smallest unified carrier containing both left-handed-shaped doublets and right-handed-shaped singlets is
   $$
   (T1 \oplus T2) \otimes (\mathbf 1 \oplus S_{\mathrm{aux}}) \otimes (\mathbf 3 \oplus \mathbf 1);
   $$
2. on that carrier, the standard left-handed fit still forces
   $$
   a = 0,
   \qquad
   b = \frac12;
   $$
3. on the same carrier, the standard right-handed singlet fit forces
   $$
   a = \pm 1,
   \qquad
   b = \frac12;
   $$
4. therefore the neutral-`S_{\mathrm{aux}}` unified carrier gives a finite no-go for one global
   $$
   Y = a J^{01} + b Q7.
   $$

---

## What remains open

The next blocker is now explicit:

> what is the smallest modification of the unified carrier or of the hypercharge operator that preserves the successful `b = 1/2` structure while removing the `a = 0` versus `a = \pm 1` conflict?

That is a much narrower problem than the original hypercharge question.
