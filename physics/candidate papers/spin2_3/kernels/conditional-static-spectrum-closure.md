# Conditional Static Spectrum Closure

## Purpose

The last sequence of notes narrowed the static carrier problem substantially:

- the hypercharge operator
  $$
  Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}
  $$
  works on the desired sectors;
- the naive full carrier contains exotic branches;
- the best current physical-state candidate is the correlated subcarrier
  $$
  P_{\mathrm{phys}}
  =
  P_{\mathrm{obs}}P_{\mathrm{aux},0}
  \;+\;
  P_{\epsilon}P_{\mathrm{aux},1},
  $$
  with:
  - `P_{\mathrm{obs}}` the observable/readout-sector projector on the even auxiliary line,
  - `P_{\epsilon}` the odd antisymmetric `SU(2)`-invariant pairing projector.

At this point the right next step is to say clearly what is and is not already closed.

This note gives the clean conditional statement:

> if the current operational orientation rule is accepted and the current auxiliary-sector rule is accepted, then the one-generation static spectrum and hypercharge assignment are fixed on the reduced physical subspace.

That is not a derivation from first principles. But it is stronger than a loose fit.

---

## Inputs

Assume the following three inputs.

### Input A: observable orientation rule

Use the current operational rule:

> the physical forward/readout orientation is the constructive/persistent branch, equivalently the branch with `\kappa_u > 0`.

In the present reduced orientation convention, that fixes the observable-sector projector to be
$$
P_{\mathrm{obs}} = P_{T1}
=
\frac12(\mathbf 1 - 2J^{01}).
$$

### Input B: auxiliary even/odd block

Assume the reduced auxiliary sector is split into:

- an even line selected by `P_{\mathrm{aux},0}`,
- an odd weak doublet selected by `P_{\mathrm{aux},1} = 1 - P_{\mathrm{aux},0}`.

This may be read abstractly as an auxiliary `\mathbf 1 \oplus \mathbf 2` block, or concretely through the low-occupancy quaternionic-doublet completion discussed elsewhere.

### Input C: odd invariant pairing rule

Assume the odd auxiliary sector enters only through the invariant antisymmetric pairing channel
$$
P_{\epsilon}
=
\frac12(\mathbf 1 - \tau)
=
\mathbf 1 - \frac12 C_{\mathrm{tot}}
$$
on
$$
\mathbf 2 \otimes \mathbf 2 = \mathbf 3 \oplus \mathbf 1.
$$

This is the unique `SU(2)`-invariant scalar channel on the odd sector.

---

## Resulting physical subspace

Under Inputs A-C, the reduced physical static subspace is
$$
P_{\mathrm{phys}}
=
P_{\mathrm{obs}}P_{\mathrm{aux},0}
\;+\;
P_{\epsilon}P_{\mathrm{aux},1}.
$$

Equivalently:

- on the even auxiliary line, keep only the observable branch;
- on the odd auxiliary line, keep only the invariant antisymmetric scalar channel.

This removes:

1. the complementary even `T2` branch
   $$
   (\mathbf 3,\mathbf 2)_{7/6}
   \oplus
   (\mathbf 1,\mathbf 2)_{1/2},
   $$
2. the odd weak-triplet sector,
3. and, if the Fock reading is used, the full-completion exotic sectors once low occupancy is imposed.

---

## Hypercharge on the physical subspace

Keep the same hypercharge operator
$$
Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}.
$$

### Even branch

On `P_{\mathrm{obs}}P_{\mathrm{aux},0}` in the present convention,
$$
J^{01} = -\frac12,
\qquad
P_{\mathrm{aux},0}=1.
$$

So:

- color triplet:
  $$
  Y = -\frac12 + \frac16 + \frac12 = \frac16;
  $$
- color singlet:
  $$
  Y = -\frac12 - \frac12 + \frac12 = -\frac12.
  $$

This gives
$$
Q_L : (\mathbf 3,\mathbf 2)_{1/6},
\qquad
L_L : (\mathbf 1,\mathbf 2)_{-1/2}.
$$

### Odd branch

On `P_{\epsilon}P_{\mathrm{aux},1}`, one has `P_{\mathrm{aux},0}=0`, so
$$
Y = J^{01} + \frac12 Q7.
$$

Restricting to the odd weak singlet channel gives:

- `T1` branch:
  $$
  (\mathbf 3,\mathbf 1)_{-1/3}
  \oplus
  (\mathbf 1,\mathbf 1)_{-1};
  $$
- `T2` branch:
  $$
  (\mathbf 3,\mathbf 1)_{2/3}
  \oplus
  (\mathbf 1,\mathbf 1)_0.
  $$

So the odd sector gives
$$
d_R,\ e_R,\ u_R,\ \nu_R
$$
with exactly the standard one-generation hypercharges.

---

## Conditional closure statement

Under Inputs A-C, the reduced static content on `P_{\mathrm{phys}}` is exactly
$$
(\mathbf 3,\mathbf 2)_{1/6}
\oplus
(\mathbf 1,\mathbf 2)_{-1/2}
\oplus
(\mathbf 3,\mathbf 1)_{-1/3}
\oplus
(\mathbf 1,\mathbf 1)_{-1}
\oplus
(\mathbf 3,\mathbf 1)_{2/3}
\oplus
(\mathbf 1,\mathbf 1)_0.
$$

That is precisely the usual one-generation left-handed plus right-handed charge pattern.

So the safe conclusion is:

> conditional on the repo’s current observable-branch rule and auxiliary-sector rule, the reduced static spectrum is closed at the one-generation level.

---

## What this does not prove

This note does **not** prove:

1. that Inputs A-C follow from the parent geometry alone;
2. that the auxiliary low-occupancy reading is uniquely forced;
3. that this is the only possible static completion;
4. that generations, anomaly completion, or dynamics are thereby closed.

So this is a conditional closure, not an unconditional theorem.

---

## Why this matters

This conditional statement changes the status of the static line in an important way.

Before:

- there were several local fits and several local obstructions.

Now:

- the remaining uncertainty has been pushed almost entirely into a short list of explicit upstream inputs.

That means the repo can now separate:

1. **carrier algebra**, which is in relatively good shape;
2. **upstream selection principles**, which are the real remaining burden.

That is real progress.

---

## Best current formulation

The cleanest honest formulation now available is:

> the Spin(2,3) static carrier is conditionally closed at the one-generation level, provided one accepts the current observable/readout-sector selector on the even line and the invariant antisymmetric pairing selector on the odd line.

That is the right current strength.

---

## What is now established

The following point is now finite:

> given
> $$
> P_{\mathrm{phys}}
> =
> P_{\mathrm{obs}}P_{\mathrm{aux},0}
> +
> P_{\epsilon}P_{\mathrm{aux},1}
> $$
> and
> $$
> Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0},
> $$
> the reduced static spectrum on `P_{\mathrm{phys}}` reproduces exactly the standard one-generation charge pattern.

---

## What remains open

The next questions are now sharply localized:

1. can `P_{\mathrm{obs}}` be derived rather than operationally adopted?
2. can the auxiliary low-occupancy / even-odd split be derived rather than postulated?
3. do those two inputs come from one common parent principle?
