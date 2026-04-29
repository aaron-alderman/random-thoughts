# Minimal Physical Subcarrier Candidate

## Purpose

The last two screens sharpened the status of the hypercharge repair:

- the projector term
  $$
  Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}
  $$
  works on the desired slots;
- but the same carrier still contains unwanted sectors:
  - the complementary `T2` branch on the auxiliary even line, with exotic doublet charges
    $$
    (\mathbf 3,\mathbf 2)_{7/6} \oplus (\mathbf 1,\mathbf 2)_{1/2};
    $$
  - and, if one uses the full Fock completion of the quaternionic doublet, the top-wedge sector adds another wrong-type doublet family.

So the natural next move is no longer to enlarge the operator. It is:

> define the smallest non-factorized **physical subcarrier** that keeps the wanted sectors and removes the unwanted ones.

This note gives that candidate explicitly.

---

## Desired content

From the previous notes, the wanted one-generation sectors are:

1. left-handed doublets from the auxiliary even line on the `T1` branch,
2. right-handed singlets from the weak-singlet channel of the auxiliary odd sector on both `T1` and `T2`.

So the minimal desired carrier is
$$
\mathcal H_{\mathrm{phys}}
=
\Big( T1 \otimes \mathbf 1_{\mathrm{aux}} \Big)
\;\oplus\;
\Big( (T1 \oplus T2)\otimes S_{\mathrm{aux}} \Big)_{j=0},
$$
tensored throughout with the color/lepton factor
$$
\mathbf 3 \oplus \mathbf 1.
$$

In words:

- keep only the `T1` branch on the even auxiliary line;
- keep only the weak-singlet channel on the odd auxiliary doublet factor.

This is the smallest carrier that retains exactly the sectors previously used in the slot-level fit.

---

## Projector onto the physical subcarrier

The candidate is naturally encoded by a projector.

### Even-line branch projector

Since `J^{01}` has eigenvalue `-1/2` on `T1` and `+1/2` on `T2`, the projector onto `T1` is
$$
P_{T1}
=
\frac12\bigl(\mathbf 1 - 2J^{01}\bigr).
$$

This gives:

- `P_{T1}=1` on `T1`,
- `P_{T1}=0` on `T2`.

### Odd-sector singlet projector

On the odd auxiliary sector, the weak content is
$$
\mathbf 2 \otimes \mathbf 2 = \mathbf 1 \oplus \mathbf 3.
$$

Let `C_{\mathrm{tot}}` be the total weak `SU(2)` Casimir on
$$
(T1 \oplus T2)\otimes S_{\mathrm{aux}}.
$$

With the standard normalization:

- `C_{\mathrm{tot}} = 0` on the singlet,
- `C_{\mathrm{tot}} = 2` on the triplet.

Therefore the projector onto the singlet channel is
$$
P_{\mathrm{odd},0}
=
\mathbf 1 - \frac12 C_{\mathrm{tot}}.
$$

### Combined physical projector

Let `P_{\mathrm{aux},0}` be the projector onto the auxiliary even line and
$$
P_{\mathrm{aux},1} := \mathbf 1 - P_{\mathrm{aux},0}
$$
the projector onto the auxiliary odd doublet.

Then the minimal physical-subcarrier projector is
$$
P_{\mathrm{phys}}
=
P_{T1}\,P_{\mathrm{aux},0}
\;+\;
P_{\mathrm{odd},0}\,P_{\mathrm{aux},1}.
$$

This is non-factorized, which is exactly the point. The successful spectrum is not living on the full tensor product. It lives on a smaller correlated subcarrier.

---

## Hypercharge on the kept sectors

Keep the same operator
$$
Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}.
$$

### Even sector kept by `P_{T1} P_{\mathrm{aux},0}`

On the kept even line:

- `J^{01} = -1/2`,
- `P_{\mathrm{aux},0}=1`.

So:

- color triplet:
  $$
  Y = -\frac12 + \frac16 + \frac12 = \frac16;
  $$
- color singlet:
  $$
  Y = -\frac12 - \frac12 + \frac12 = -\frac12.
  $$

This is exactly
$$
(\mathbf 3,\mathbf 2)_{1/6}
\oplus
(\mathbf 1,\mathbf 2)_{-1/2}.
$$

### Odd singlet sector kept by `P_{\mathrm{odd},0} P_{\mathrm{aux},1}`

On the odd sector:

- `P_{\mathrm{aux},0}=0`,
- so `Y = J^{01} + \frac12 Q7`.

Restricting to the weak singlet channel then gives:

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

So the projector-defined subcarrier reproduces exactly the intended one-generation static content.

---

## What this removes

The projector `P_{\mathrm{phys}}` removes both previously identified exotic families:

1. **Complementary even branch.**
   `P_{T1}` kills the `T2` auxiliary-even sector
   $$
   (\mathbf 3,\mathbf 2)_{7/6}
   \oplus
   (\mathbf 1,\mathbf 2)_{1/2}.
   $$

2. **Odd triplet channels.**
   `P_{\mathrm{odd},0}` kills the triplet part of
   $$
   \mathbf 2 \otimes \mathbf 2 = \mathbf 1 \oplus \mathbf 3.
   $$

So this is the first candidate that actually addresses the carrier problem itself, not only the operator fit.

---

## Fock-space reading

If the auxiliary block is taken from the low-occupancy completion of the quaternionic doublet `V`,
$$
\Lambda^0 V \oplus \Lambda^1 V,
$$
then:

- `P_{\mathrm{aux},0}` becomes the vacuum projector `P_{\mathrm{vac}}`,
- `P_{\mathrm{aux},1}` becomes the one-particle projector.

In that language,
$$
P_{\mathrm{phys}}
=
P_{T1} P_{\mathrm{vac}}
\;+\;
P_{\mathrm{odd},0}\,P_{\mathrm{1p}}.
$$

So the physical content can be read as:

- left-handed doublets = `T1` vacuum sector,
- right-handed singlets = one-particle weak-singlet sector.

This is the cleanest structural interpretation reached so far.

---

## Why this is progress

This candidate is better than the earlier ones in three ways:

1. it explains exactly which subspace of the carrier is being used, instead of silently selecting slots;
2. it removes the already-identified even-branch and odd-triplet exotics at the representation level;
3. it packages the selection in canonical operators:
   - `J^{01}` for branch choice,
   - auxiliary even/odd projector,
   - total weak Casimir for singlet-versus-triplet choice.

So the problem has moved from “which slots were we informally using?” to a precise operator-level question.

---

## What remains open

This note still does **not** finish the static sector.

The remaining burden is now:

> why should the physical Hilbert space be the `P_{\mathrm{phys}}` subcarrier rather than the full tensor-product carrier?

More concretely, one still needs a principled reason for:

1. selecting `T1` rather than `T2` on the even auxiliary line;
2. selecting the weak singlet rather than the triplet on the odd auxiliary sector;
3. if using the Fock-space reading, restricting to the low-occupancy block rather than the full completion.

But these are now sharply localized operator questions, not diffuse carrier ambiguity.

---

## What is now established

The following statement is now finite:

> the smallest candidate carrier that reproduces exactly the intended one-generation static content is not the full tensor product, but the correlated subcarrier cut out by
> $$
> P_{\mathrm{phys}}
> =
> P_{T1}P_{\mathrm{aux},0} + P_{\mathrm{odd},0}P_{\mathrm{aux},1}.
> $$

That is the first fully explicit operator-level candidate for the physical static subspace.

---

## What remains open

The next question is:

> can the subcarrier projector `P_{\mathrm{phys}}` be derived from the parent reduction, the eventual orientation selector, or a dynamical superselection rule, rather than imposed as the minimal fix by hand?
