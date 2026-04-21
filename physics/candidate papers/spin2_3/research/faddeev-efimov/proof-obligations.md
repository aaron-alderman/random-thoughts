# Proof Obligations For The Faddeev / Efimov Bridge

The bridge can feed back into the core Spin(2,3) framework only after these gates are completed or explicitly marked as partially complete with limits.

## Gate 1: Define The Spin-Derived Operator

Define the SO(2,1) generators and Casimir from Spin(2,3) threshold data without importing the Faddeev answer.

Acceptance:

- the relevant subgroup is specified;
- the carrier space is specified;
- normalization conventions are fixed;
- the operator is computable in a basis.

## Gate 2: Embed Three Transport States Into Faddeev Channel Data

Show that the three near-boundary transport states map to the three Faddeev spectator/pair channels.

Acceptance:

- the channel basis is explicit;
- the role of T1 projection is stated;
- Bethe-Peierls boundary data are matched or identified as an external input;
- symmetrization for identical bosons is handled without extra fitting.

## Gate 3: Compute The Restricted Casimir Matrix

Restrict the Spin-derived SO(2,1) Casimir to the proposed three-state collective subspace.

Acceptance:

- the resulting matrix is computed;
- diagonal and off-diagonal terms are derived;
- the symmetric eigenvalue is written explicitly;
- no Faddeev kernel value is inserted by hand.

## Gate 4: Match Faddeev Kernel Normalization

Compare the restricted Spin-side matrix with the Faddeev 3x3 channel-coupling matrix.

Acceptance:

- normalization of visible/quaternionic generators is fixed;
- the Faddeev recoupling constants are recovered or the mismatch is quantified;
- the Langer shift is accounted for separately;
- assumptions are recorded in `CLAIM_LEDGER.md`.

## Gate 5: Recover Or Fail To Recover `s_0`

Determine whether the Spin-side calculation gives the Efimov exponent.

Acceptance:

- the calculation recovers `s_0 ~= 1.00624`, or
- it fails cleanly and identifies which assumption breaks.

## Status Rule

Only after Gates 1-5 are satisfied may `casimir-faddeev-conjecture.md` be promoted from conjecture to target theorem or theorem. Partial progress should be recorded as `conditional`, not `established`.
