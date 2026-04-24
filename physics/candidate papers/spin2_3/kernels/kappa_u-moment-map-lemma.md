# Lemma Note: `\kappa_u` As The Unique Exchange-Odd Cross-Coupling Slot

This note isolates and formalizes the symmetry-descent statement used in the two-branch transport dynamics: once the selected octonionic direction `u` is fixed (pointwise in `u`), the reduced dynamics admit a *unique* exchange-odd quadratic *cross* coupling between the two branches. The coefficient of that coupling is the scalar `\kappa_u` (which is separately tracked as `K`-invariant data descending from the parent reduction).

This is a pointwise-in-`u` statement: it does not decide whether `u` is kinematic or dynamical, and it does not fix the orientation/sign choice `\kappa_u > 0`.

## Setup (Branch Space And The Exchange Involution)

Fix a unit imaginary `u` with `u^2=-1` and write the selected complex line as `\mathbf C_u = \mathrm{span}_{\mathbf R}\{1,u\}`.

Treat branch amplitudes as a pair
$$
(A,B)\in \mathbf C_u^2.
$$

The reduced transport kernel uses an exchange-with-conjugation involution
$$
\mathcal C(A,B) := (\bar B, \bar A).
$$
In real coordinates,
$$
A=a_1+ua_2,\qquad B=b_1+ub_2,
$$
this acts as
$$
(a_1,a_2,b_1,b_2)\mapsto (b_1,-b_2,a_1,-a_2).
$$

## Lemma (Uniqueness Of The Exchange-Odd Quadratic Invariant)

Consider real-valued quadratic functionals on `\mathbf C_u^2`. The exchange-odd condition is the constraint
$$
Q(\mathcal C(A,B))=-Q(A,B).
$$

The transport coupling term is a *cross* quadratic (bilinear in the `A` and `B` coordinates). Write the most general real cross quadratic as
$$
Q_{\times}(A,B)=c_1\,a_1b_1+c_2\,a_1b_2+c_3\,a_2b_1+c_4\,a_2b_2.
$$

Imposing exchange-oddness under `(a_1,a_2,b_1,b_2)\mapsto (b_1,-b_2,a_1,-a_2)` forces
$$
c_1=c_4=0,\qquad c_2=c_3,
$$
so the exchange-odd cross sector is one-dimensional:
$$
Q_{\times}(A,B)\propto a_1b_2+a_2b_1=\mathrm{Im}_u(AB).
$$

Equivalently: **up to an overall scalar**, the only exchange-odd cross quadratic is `\mathrm{Im}_u(AB)`.

## Corollary (The Coupling Slot And Moment-Map Interpretation)

In the reduced Hamiltonian description, an exchange-odd coupling must therefore enter (at quadratic order) as
$$
H_{\mathrm{cpl}}(A,B) = -\kappa_u\,\mathrm{Im}_u(AB),
$$
for a scalar coefficient `\kappa_u`.

This identifies `\kappa_u` as the coefficient of the unique exchange-odd quadratic coupling slot on branch space. In symplectic terms: the quadratic `\mathrm{Im}_u(AB)` is the moment map for the corresponding exchange-mixing generator on the reduced branch space (up to normalization), and `\kappa_u` is its moment-map coordinate.

## What This Does Not Do

This lemma does **not** derive:

- why the preferred direction `u` is selected (kinematic vs dynamical bracket remains open);
- why the physical readout orientation should pick the constructive class `\kappa_u > 0` (this is the orientation axiom / selector gate);
- any quantitative matching to Efimov/Faddeev kernels (that remains a separate proof obligation).

It is also worth recording a simple degeneracy: at the level of the quadratic Hamiltonian-Rayleigh generator, changing `\kappa_u \mapsto -\kappa_u` is equivalent to flipping the branch label `B\mapsto -B`, so purely linear stability data cannot fix the sign.
