# D1 Attempt: Deriving The Orientation Rule From Bulk Stability

This note is a focused attempt at the D1 upgrade route: derive the operational orientation rule
$$
\kappa_u > 0
$$
from a bulk stability/attractor principle rather than adopting it as a readout convention.

The goal is not to force a conclusion prematurely. The goal is to isolate what can be proven from the *existing* reduced structure and what extra structure D1 would have to introduce.

Prerequisites:

- `kernels/dynamics.md` (orientation rule and Hamiltonian-Rayleigh scaffold)
- `kernels/discrete-symmetries.md` (the relevant `Z2` ledger)
- `kernels/u-selector-bracketing.md` (why symmetry/linear stability cannot fix the sign)

## What D1 Would Need To Show

A genuine D1 derivation would have to do both:

1. Identify an upstream bulk functional or principle (Lyapunov/entropy production/attractor selection) that singles out one of the two orientation-related branches.
2. Show that the selected branch corresponds to the constructive/persistent class, i.e. `\kappa_u > 0` in the phase-normalized readout gauge.

## No-Go: Reduced Linear Stability Cannot Fix The Sign

At the level of the quadratic Hamiltonian-Rayleigh generator on branch space, the two-branch system is linear in `X=(a_1,a_2,b_1,b_2)`:

$$
\dot X = M(\omega,\kappa_u)\,X - \gamma X,
$$
with the `\kappa_u` dependence entering only through off-diagonal exchange blocks.

Let `P = \mathrm{diag}(1,1,-1,-1)` (flip the sign of `B` in real coordinates). Then
$$
P^{-1} M(\omega,\kappa_u)\,P = M(\omega,-\kappa_u).
$$

So `\kappa_u` and `-\kappa_u` are *similar* at this level: the spectrum and any purely linear stability criterion depend only on `\kappa_u^2`.

Conclusion:

> Any D1 derivation that tries to fix the sign from the reduced linear generator alone is impossible.

This is not philosophical. It is a concrete conjugacy.

## Where A D1 Principle Could Still Live

The sign can only become derivable if the bulk stability principle introduces **extra structure** not invariant under the reduced similarity `B -> -B` and not reducible to linear spectrum data. Examples:

1. A **positivity constraint** on a readout intensity functional that changes sign between constructive and inverted branches.
2. A **nonlinear bulk constraint** that ties the branch-slot dictionary `(A,B)` to a physically oriented bracket completion, making `B -> -B` non-gauge.
3. A **stability principle for the coupled bulk+readout system** (not just the reduced branch generator), where the readout mechanism breaks the conjugacy.

## Minimal D1 Gate (What Needs To Be Added)

In `kernels/dynamics.md` one has, at the symmetric locked fixed point, the identity
$$
\mathrm{Re}_u(AB)\big|_{*} = \frac{R^2\,\gamma}{\kappa_u}.
$$

Therefore, any bulk/readout principle that forces
$$
\mathrm{Re}_u(AB)\big|_{*} > 0
$$
for the *direct observable* locked branch would immediately imply `\kappa_u > 0`.

So D1 can be reduced to a single crisp missing link:

> **D1 gate:** justify why the physically realized readout intensity (or stability functional) demands `\mathrm{Re}_u(AB)|_* > 0` rather than allowing the inverted branch with `\mathrm{Re}_u(AB)|_* < 0`.

Until that link is supplied from the bulk (or from a physically modeled readout coupling), D1 remains an upgrade target, not a derivation.

## Interlude: What "Bound" Means In The Reduced Dynamics

The reduced shape/phase subsystem (independent of `\gamma`) is
$$
\dot{\rho}=-\kappa_u\sinh(2\rho)\cos\Phi,
\qquad
\dot{\Phi}=2\omega-2\kappa_u\cosh(2\rho)\sin\Phi.
$$

Two regimes matter:

1. **Phase-locked (bound/persistent candidate):** trajectories for which `\Phi(t)` converges to a fixed point `\Phi_*` (in a suitable frame), so that `\cos\Phi` does not keep changing sign indefinitely.
2. **Running-phase (dephased/unbound):** trajectories for which `\Phi(t)` keeps drifting. In this regime any term involving `\cos\Phi` or `\sin\Phi` appears oscillatory over time and supports only coarse-grained persistence.

Inside the locked region, the invariant manifold `\rho=0` contains the canonical fixed points defined by
$$
\sin\Phi_*=\frac{\omega}{\kappa_u},
\qquad
|\omega|\le|\kappa_u|.
$$
There is no interior fixed point with `\rho\neq 0` unless one sits on the locking boundary (where `\cos\Phi_*=0`), so the stable "bound" attractors live on `\rho=0` in the reduced picture.

## Lifetime Maximization: What It Can And Cannot Fix

The amplitude equation is
$$
\dot R = R\left(-\gamma + \kappa_u\cosh(2\rho)\cos\Phi\right).
$$

A "maximize lifetime" principle pushes toward maximizing the *growth margin*
$$
-\gamma + \kappa_u\cosh(2\rho)\cos\Phi.
$$

At fixed `\rho`, the phase choice that maximizes this margin is simply:
$$
\cos\Phi \ \text{has the same sign as}\ \kappa_u,
$$
so that `\kappa_u\cos\Phi=|\kappa_u|` (constructive relative phase).

This is the conceptual cleanup:

> Lifetime maximization alone forces `\kappa_u\cos\Phi>0` on the readout-aligned locked branch, but it does not by itself force `\kappa_u>0`.

To upgrade from `\kappa_u\cos\Phi>0` to `\kappa_u>0`, D1 must additionally explain why the physically relevant readout convention pins the locked branch to the phase-normalized condition `\Phi_*=0` (rather than `\Phi_*=\pi`), i.e. why the "constructive relative phase" must coincide with the fixed phase reference used by readout.

## Candidate D1 Functional: Readout Intensity For The Conjugate Sum

The reduced equations themselves suggest a natural "readout-aligned" combination: the exchange involution uses conjugation, and the coupling terms are proportional to `\bar B`. This makes the conjugate sum
$$
\Psi_{\mathrm{rd}} := A + \bar B
$$
a reasonable candidate for a readout amplitude (it is also the combination whose relative phase is the physically invariant sum `\Phi = \theta_1+\theta_2`).

Its intensity is
$$
|\Psi_{\mathrm{rd}}|^2
=
|A+\bar B|^2
=
|A|^2+|B|^2 + 2\,\mathrm{Re}_u(AB).
$$
So the sign of `\mathrm{Re}_u(AB)` is exactly the sign of the interference term in this conjugate-sum channel.

If a bulk stability/readout principle says that the physically realized direct readout branch should maximize (or at least keep positive contribution from) the conjugate-sum intensity, then it selects
$$
\mathrm{Re}_u(AB)\big|_* > 0,
$$
which (via the fixed-point identity already used above) forces `\kappa_u > 0` for the locked/persistent readout branch.

This is not yet a derivation, because it still assumes that the correct readout functional is built from `A+\bar B` rather than from a different bulk observable. But it does identify a concrete, algebraically natural candidate for the missing D1 link, and it explains why `\Phi_*=0` is the distinguished phase normalization: it is the phase alignment of `A` with `\bar B` in the readout channel.

## Conditional Closure Under Conjugate-Sum Readout

At this point the D1 route can be stated as a clean conditional proposition rather than as a loose heuristic.

**Assumptions.**

1. the physical readout channel is the conjugate-sum amplitude
   $$
   \Psi_{\mathrm{rd}} = A + \bar B;
   $$
2. the physically realized persistent readout branch must have constructive interference in that channel, equivalently
   $$
   \mathrm{Re}_u(AB)\big|_* > 0;
   $$
3. the branch is evaluated at the locked/persistent fixed point where
   $$
   \mathrm{Re}_u(AB)\big|_* = \frac{R^2\,\gamma}{\kappa_u}.
   $$

**Conclusion.**

Because `R^2 > 0` and `\gamma > 0` on the persistent branch, the sign of `\mathrm{Re}_u(AB)|_*` is exactly the sign of `1/\kappa_u`. So the three assumptions imply
$$
\kappa_u > 0.
$$

This closes the algebraic part of D1.

### What D1 still owes

After the conditional proposition above, D1 no longer owes a transport-space sign calculation. It owes only the physical identification of the readout functional:

- why the direct observable channel is really `\Psi_{\mathrm{rd}} = A + \bar B` or an equivalent sign-sensitive observable;
- why the physical readout criterion requires constructive interference in that channel.

So the D1 burden has been reduced to:

> justify the readout functional, not the sign algebra once that functional is granted.

## If EM Readout Settles On The Selected Axis (`u` / `e1`), D1 Closes

You can now see the precise point where the "path dependence" intuition becomes a sign selection.

Assumption (EM/readout alignment):

- The physical readout coupling (EM-like interaction) is defined only after the preferred octonionic axis is selected. In an adapted octonion basis one may gauge-fix that axis to a standard imaginary unit (for example `u = e1`), and the readout functional is built on the corresponding `\mathbf C_u` line.
- The readout channel couples to the conjugate-sum amplitude
  $$
  \Psi_{\mathrm{rd}} = A + \bar B,
  $$
  so that the directly readable intensity contains the interference term `2 Re_u(AB)`:
  $$
  |\Psi_{\mathrm{rd}}|^2 = |A|^2 + |B|^2 + 2\,\mathrm{Re}_u(AB).
  $$

Then a D1 stability/lifetime principle applied to the readout channel is equivalent to requiring constructive interference in that channel at the locked fixed point:
$$
\mathrm{Re}_u(AB)\big|_* > 0.
$$
Using the fixed-point identity already recorded in `kernels/dynamics.md`,
$$
\mathrm{Re}_u(AB)\big|_* = \frac{R^2\,\gamma}{\kappa_u},
$$
this immediately implies the operational orientation rule
$$
\kappa_u > 0
$$
for the unique persistent readout branch.

So the remaining D1 burden is no longer "derive `\kappa_u > 0` from nothing." It is:

> justify that EM/readout coupling really is aligned with the selected axis `u` and samples the conjugate-sum intensity (or an equivalent sign-sensitive readout functional).
