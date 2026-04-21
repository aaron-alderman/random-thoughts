# Conjecture: Faddeev Collective Mode as an SO(2,1) Casimir Eigenstate

## Status

This file is a conjectural bridge target, not a theorem. It merges the earlier theorem-sketch material with the stronger Faddeev embedding draft, but demotes the claim until the Spin-derived Casimir calculation and the Faddeev kernel normalization are explicitly matched.

Current status: `conjecture`.

## Target Claim

The symmetric collective eigenvalue

\[
\lambda_{\rm sym} = -s_0^2 - \frac{1}{4},
\qquad s_0 \approx 1.00624,
\]

isolated from the three-identical-boson Faddeev channel-coupling problem at unitarity may equal the eigenvalue of an SO(2,1) Casimir restricted to a three-state collective transport mode inside the Spin(2,3) ~= Sp(4,R) framework.

If true, the Faddeev recoupling algebra would be a concrete realization of the threshold SO(2,1) structure already suggested by the Spin(2,3) transport classification.

## Inputs Being Compared

On the Spin(2,3) side:

- Spin(2,3) spinors split as `T1 + T2` under `J^{01}`.
- Near persistence/locking boundaries, the reduced dynamics linearize as `dot R ~= epsilon R`.
- That scaling form suggests an SO(2,1) conformal quantum-mechanics sector.
- Three near-boundary transport states are proposed to form a collective three-state mode.

On the Faddeev/Efimov side:

- The wave function decomposes into three pair channels.
- Bethe-Peierls boundary conditions at unitarity produce a symmetric 3x3 channel-coupling problem.
- The symmetric channel yields the Efimov exponent through the known transcendental equation.
- Langer reduction produces the supercritical inverse-square potential.

## Proposed Identification

The target identification is:

\[
C_{\rm SO(2,1)}\big|_{\rm collective}
\quad \longleftrightarrow \quad
K_{\rm Faddeev}^{(3\times 3)}\big|_{\rm symmetric}.
\]

In the simplest symmetric channel basis, the restricted object is expected to have the all-to-all form

\[
\begin{pmatrix}
a & b & b \\
b & a & b \\
b & b & a
\end{pmatrix},
\]

with symmetric eigenvalue `a + 2b`. The conjecture is that the Spin-derived values of `a` and `b`, after the correct normalization and Langer shift, reproduce `-s_0^2 - 1/4`.

## Assumptions To Make Explicit

- The three Faddeev channels can be embedded into a three-state transport-sector construction rather than merely compared by analogy.
- The relevant SO(2,1) subgroup is fixed by the Spin(2,3) threshold dynamics, not chosen after seeing the Faddeev answer.
- The off-diagonal Faddeev recoupling terms are matrix elements of Spin-derived generators, with no fitted normalization.
- Bethe-Peierls boundary data can be matched to the proposed T1-like threshold/boundary traversal without changing the physical problem.
- Finite T1/T2 mixing is a perturbation of the bridge, not part of the unitarity-limit identification.

## What Would Promote This

This conjecture becomes a target theorem only if the gates in `proof-obligations.md` are completed:

1. define the Spin-derived operator;
2. embed the three transport states into Faddeev channel data;
3. compute the restricted SO(2,1) Casimir matrix;
4. match Faddeev kernel normalization;
5. recover, or decisively fail to recover, `s_0 ~= 1.00624`.

Until those steps are done, the safe statement is structural:

> The Faddeev/Efimov construction is a promising quantitative test of the Spin(2,3) threshold SO(2,1) idea.
