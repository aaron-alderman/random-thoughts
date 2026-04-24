# Discrete `Z2` Ledger (Orientation, Exchange, And Gauge)

This note exists to keep concepts from getting mixed.

The programme contains several distinct `\mathbf Z_2` operations that can look similar if they are not tracked explicitly. Some are gauge conventions, some are genuine physical reversals, and some are bookkeeping symmetries of the reduced equations.

## 1) `u -> -u` (Octonionic Axis Reversal)

**Object:** the selected imaginary octonionic direction `u` (the `\mathbf C_u` line orientation).

**Effect:** flips any scalar built as an odd projection onto `u`, in particular the signed coupling `\kappa_u`.

**Status:** upstream datum. Whether `u` is kinematic or dynamical is bracketed (see `kernels/u-selector-bracketing.md`). Either way, this `\mathbf Z_2` is not something that can be "derived inside" the reduced slice; the reduced slice is already written in an adapted frame.

## 2) `J^{01} -> -J^{01}` (Reduced Orientation Flip)

**Object:** the reduced `Spin(2,3)` convention that names the two `J^{01}` eigenspaces as `T1` and `T2`.

**Effect:** swaps the sector labels:
$$
T1 \leftrightarrow T2.
$$

**Status:** a naming/orientation convention at the reduced level. Physical content should be attached to the induced projector (the chosen observable sector), not the bare label `T1`.

## 3) Exchange+Conjugation `\mathcal C(A,B)=(\bar B,\bar A)`

**Object:** the two-branch amplitude variables on the selected line `\mathbf C_u`:
$$
(A,B)\in \mathbf C_u^2.
$$

**Effect:** swaps the two branch slots and flips the sign of the exchange-odd cross term:
$$
\mathrm{Im}_u(AB) \mapsto -\mathrm{Im}_u(AB).
$$

**Status:** structural involution required by the reduction picture (charge-flip on the hidden line combined with conjugation on `\mathbf C_u`). It is a symmetry of the reduced coupling slot, not itself an "observable selection" rule.

## 4) Branch Sign Flip `(A,B) -> (A,-B)`

**Object:** a linear change of reduced variables.

**Effect:** at the level of the quadratic Hamiltonian-Rayleigh generator on branch space, this is a similarity transformation that sends
$$
\kappa_u \mapsto -\kappa_u,
$$
so the linear spectrum depends only on `\kappa_u^2`.

**Status:** reduced-variable gauge/bookkeeping. This is one reason the sign choice `\kappa_u > 0` cannot be fixed from symmetry or linear stability alone. The sign becomes meaningful only once the reduction dictionary ties the branch slots `(A,B)` to parent data (and/or once an external readout arrow is imposed).

## 5) What Actually Needs Fixing

The framework's remaining "last sign" is not a single abstract `\mathbf Z_2`. It is the compatibility of:

1. the upstream orientation of `u`,
2. the reduced sector naming (`T1/T2` via `J^{01}`),
3. the branch-slot dictionary (what `A` and `B` mean as parent bracket completions),
4. the readout/observability arrow (which sector is "forward" and actually coupled to observation).

Any derivation that claims to fix the sign must say which of these four items it is using as input and which it is producing as output.

