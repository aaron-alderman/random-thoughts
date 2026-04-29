# Upstream Selector Programme

## Purpose

The recent static cleanup changed the shape of the project.

The main one-generation carrier problem is no longer:

- find another local tensor-product carrier,
- add another small projector by hand,
- or keep searching nearby hypercharge fits.

It is now:

> identify the upstream selector principle that fixes the observable branch and explains why the reduced physical static space is the one currently isolated by the conditional closure note.

This note records that pivot explicitly.

See also:

- `kernels/conditional-static-spectrum-closure.md`
- `kernels/even-sector-observable-projector-descent.md`
- `kernels/odd-sector-epsilon-channel.md`
- `kernels/orientation-rule-upgrades.md`
- `kernels/orientation-d1-bulk-stability.md`
- `kernels/epistemics.md`

## What Is Already Closed Downstream

At the reduced carrier level, the project now has a disciplined conditional package.

1. The even-line selector is already identified with the observable/readout projector:
   $$
   P_{\mathrm{obs}} = P_{T1}
   $$
   in the current orientation convention.

2. The odd-line selector is the unique antisymmetric `SU(2)`-invariant pairing channel:
   $$
   P_{\epsilon}
   =
   \frac12(1-\tau)
   =
   1-\frac12 C_{\mathrm{tot}}.
   $$

3. With
   $$
   P_{\mathrm{phys}}
   =
   P_{\mathrm{obs}}P_{\mathrm{aux},0}
   +
   P_{\epsilon}P_{\mathrm{aux},1}
   $$
   and
   $$
   Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0},
   $$
   the reduced one-generation charge pattern is reproduced exactly on the physical subspace.

So the local carrier algebra is no longer the main uncertainty. The remaining uncertainty sits in the inputs that select `P_{\mathrm{obs}}` and the auxiliary even/odd structure.

## The Actual Upstream Debts

The live upstream debts are now short and explicit.

### U1. Observable-branch selection

Why is the physical forward/readout sector the one represented downstairs by `P_{\mathrm{obs}}`?

Equivalently:

- what fixes the last global orientation,
- why is the direct readout branch the constructive/persistent one,
- why is the sector named `T1` the observable one after orientation is fixed?

### U2. Auxiliary-sector rule

Why is the physical auxiliary contribution effectively the `\mathbf 1 \oplus \mathbf 2` low-occupancy split, rather than the full completion or some different enlargement?

Equivalently:

- why is `P_{\mathrm{aux},0}` physically visible in the static charge operator,
- why is the full `\Lambda^\bullet V` completion not the right physical carrier as-is,
- what removes or suppresses the complementary sectors?

### U3. Common-parent question

Do U1 and U2 come from:

1. one common parent selector,
2. two distinct physical principles,
3. or one parent selector plus one auxiliary superselection rule?

This is now the main synthesis question.

## Route Comparison

The existing orientation routes can now be re-read by how much of U1-U3 they can actually close.

### Route D1: bulk stability / readout intensity

Best current form:

- if the physical readout channel is the conjugate sum
  $$
  \Psi_{\mathrm{rd}} = A + \bar B,
  $$
- and persistent readout requires constructive interference there,
- then `\kappa_u > 0` follows immediately.

What D1 can plausibly close:

- U1, if the readout functional is justified physically.

What D1 does **not** automatically close:

- U2, the auxiliary low-occupancy rule.

So D1 is now a sharp route for the observable branch, but not obviously a complete route for the whole upstream-selector problem.

### Route D2: ambient selector descent

Best current form:

- identify an ambient scale/readout selector `D_{\mathrm{amb}}` or equivalent parent projector,
- show that its reduced image is `P_{\mathrm{obs}}`,
- then ask whether the same parent structure also induces the auxiliary even/odd rule.

What D2 can plausibly close:

- U1 directly,
- and possibly U2 if the auxiliary block is itself a reduced image of parent occupancy/charge structure.

This is the highest-leverage route now, because it is the only current route with a realistic chance of turning the static conditional closure into a more unified parent-level statement.

### Route D3: explicit observer/readout coupling

Best current form:

- model a physical readout coupling that breaks the residual `\mathbf Z_2`,
- show that only the constructive/persistent branch is stably readable,
- infer the even-line observable projector from that coupling.

What D3 can plausibly close:

- U1 operationally.

What D3 still leaves open:

- U2 unless the same coupling also constrains the auxiliary sector.

## Working Rule

For the next phase of the project:

1. treat the static carrier search as paused at conditional one-generation closure;
2. do not spend more default effort on nearby local carrier variants unless they directly test U1-U3;
3. treat the upstream selector as the main live proof burden;
4. prefer arguments that can explain both the observable projector and the auxiliary rule in one parent language.

## Next Concrete Tasks

The next concrete tasks should be phrased at the selector level, not at the carrier-fit level.

1. Write the minimal ambient selector data.
   - What is the parent object: `D_{\mathrm{amb}}`, `P_{\Pi,-}`, a scale-flow field, or an equivalent one-sided support principle?

2. Prove observable-projector descent.
   - Show explicitly how the parent selector reduces to
     $$
     \mathcal R_{\mathrm{op}}(P_{\Pi,-}) = P_{\mathrm{obs}}.
     $$

3. Test auxiliary descent from the same parent structure.
   - Can the low-occupancy/even-odd split be read as reduced occupancy, charge, or filtration data rather than a separate postulate?

4. If not, separate the burdens cleanly.
   - Derive `P_{\mathrm{obs}}` upstream.
   - State the auxiliary rule as an independent superselection principle rather than letting the two issues blur together.

## Current Bottom Line

The project is no longer blocked by diffuse static ambiguity.

It is blocked by one concentrated question:

> what upstream selector makes the reduced observable projector physical, and can that same selector also explain the auxiliary rule used by the static conditional closure?

That is the right next target.
