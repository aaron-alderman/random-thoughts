# Dynamics Kernel

## Purpose

This document is the dynamics source text for the project.

It is not a paper draft. It is the place where the dynamical spine is kept coherent inside one domain. The job of this file is to say:

- what the dynamical postulates are
- what the microscopic model is
- what reduction regime is being used
- what results are actually derived in that regime
- what is interpretation rather than theorem
- what the unresolved dynamical issues are

This file depends on the static sector split, but it does not try to carry the full static or particle-representation program.

---

## Scope

This file covers:

- evolution in `T1 \oplus T2`
- the projected-observables postulate as a dynamical-epistemic input
- minimal sector-mixing generators
- weak-coupling reduction
- the reduced Markovian equation
- the long-scale transport-diffusion limit

This file does not cover:

- the full static derivation of representation content
- octonion-based generation structure
- gauge dynamics
- a relativistic field-theoretic completion
- sharp phenomenological predictions beyond the reduced-model scaling laws

---

## Inputs from the static layer

The dynamical domain assumes the following static setup.

1. The spinor space splits as
   $$
   \mathcal{H}_{\mathrm{spin}} = T1 \oplus T2
   $$
   through the `J^{01}` decomposition.
2. There is a projector
   $$
   P : \mathcal{H}_{\mathrm{spin}} \to T1,
   \qquad
   Q = 1 - P
   $$
   onto the two sectors.
3. `T1` and `T2` are structurally distinct sectors, even before a physical interpretation is attached.
4. A preferred direction has been selected so that the zero-mass traversal channel is identified with `T1`.
5. The hidden complement relevant to richer reduced corrections is interpreted as an internal complex `2`-plane, carried locally by a quaternionic slice inside `O`, not as a literal extra timelike sector of spacetime.

The dynamical layer adds the question:

- what happens if evolution takes place in the full space, but observables are extracted only after projection?

The current dynamics kernel should now be read against the working reduction kernel in `core/ambient-reduction-scaffold.md`. In that reduced reading:

- `T1/T2` is the effective image of a hidden phase-charge split on a local complex line
- the quaternionic slice is local reduction geometry, not a new dynamical interaction sector by default
- the zero-mass derivation target is to inherit support on `T1` from parent `(-)`-charge support rather than choosing the `T1` block by hand

---

## Dynamical postulates

The revised kernel uses two central ideas.

### Postulate D1: full-space evolution

States evolve in the full space `T1 \oplus T2`.

This means the hidden sector is dynamically real inside the model, even if it is not directly observed.

In the updated reading, this hidden-sector language should be handled carefully. At the kernel level the model still evolves in `T1 \oplus T2`, but the deeper structure behind the unresolved excursions is interpreted as internal hidden-plane data rather than as literal additional time coordinates.

### Principle D2: zero-mass propagation stays on `T1`

The privileged interaction or traversal channel for zero-mass propagation is `T1`.

This means:

- pure zero-mass propagation is confined to `T1`
- `T2` becomes dynamically relevant only when additional structure couples it to `T1`

This principle is now the cleanest high-level reason that `T1` matters physically.

### Effective rule D3: projected observables

Physical observables are evaluated after projection onto `T1`.

At the density-matrix level:
$$
\rho_1 = P \rho P.
$$

This is the observable rule used by the reduced dynamics. In the revised backbone it is best read as downstream of Principle D2 rather than as a completely independent primitive axiom.

---

## Minimal microscopic model

The simplest block form used in the kernel is:
$$
H =
\begin{pmatrix}
H_{\mathrm{tr}} & m V \\
m V^\dagger & H_2
\end{pmatrix}.
$$

Here:

- `H_tr` governs transport in `T1`
- `H_2` governs intrinsic hidden-sector evolution
- `V` mixes the two sectors
- `m` is the mixing strength

The full state obeys:
$$
\dot{\rho} = - i [H,\rho].
$$

For the transport model used later, one takes:
$$
H_{\mathrm{tr}} = - i v \cdot \nabla.
$$

This is a model choice. It is not forced by the static domain alone.

In the revised picture, the physical reading is:

- the `H_tr` block is the zero-mass or massless-traversal channel
- the off-diagonal block becomes relevant when mass-generating structure allows departure from pure `T1` propagation
- the parameterization by one visible and one complementary block is the reduced image of a deeper hidden complex-plane structure, not yet the full parent geometry itself

### Minimal zero-mass transport operator

If the project wants to sharpen Principle D2 beyond a slogan, the cleanest first target is the following minimal operator split:

$$
H_0 =
\begin{pmatrix}
H_{\mathrm{tr}} & 0 \\
0 & 0
\end{pmatrix},
\qquad
H_{\mathrm{mix}} =
\begin{pmatrix}
0 & m V \\
m V^\dagger & H_2
\end{pmatrix},
\qquad
H = H_0 + H_{\mathrm{mix}}.
$$

In this decomposition:

- `H_0` is the candidate zero-mass transport operator
- `H_{\mathrm{mix}}` collects everything that either mixes sectors or activates hidden-sector dynamics beyond pure transport

The intended meaning is:

- in the strict zero-mass limit, only `H_0` is active as the direct traversal operator
- `H_0` acts nontrivially only on `T1`
- `T2` contributes only once mixing or additional hidden-sector structure is turned on

This is still an ansatz-level formulation, but it is sharper than the looser claim "zero-mass propagation stays on `T1`" because it isolates the exact operator statement that would need to be derived.

### What would count as a derivation

The project should be explicit about what would elevate this from model choice to derivation.

At minimum, one would need to show that the parent reduction implies:

1. the reduced zero-mass generator commutes with the projector onto `T1`
2. the reduced zero-mass generator annihilates or decouples `T2`
3. off-diagonal terms arise only when the structure corresponding to mass or hidden-sector activation is turned on
4. the resulting block form is stable under the reduction, not merely chosen in a convenient basis

### Projector and commutator form

The same target can be written more sharply in projector language.

Let

$$
P : \mathcal{H}_{\mathrm{spin}} \to T1,
\qquad
Q = 1-P.
$$

Then the minimal zero-mass operator claim is equivalent to:

$$
H_0 = P H_0 P,
\qquad
Q H_0 = 0,
\qquad
H_0 Q = 0.
$$

These imply in particular

$$
[H_0,P] = 0,
$$

and they say more than mere commutation: not only is `T1` invariant under `H_0`, but `H_0` has no support on `T2` at all.

Because `P` is the spectral projector onto the `J^{01}` charge sector identified with `T1`, the same statement can be read as a reduced charge condition:

- `H_0` preserves the `J^{01}` grading
- the only nontrivial reduced charge sector seen by `H_0` is the `T1` sector

So the derivation target is not merely "find a basis where the matrix looks block diagonal." The real target is:

- derive `P H_0 P = H_0` from the parent reduction
- derive `Q H_0 = H_0 Q = 0` from the zero-mass selection rule
- derive `P H_{\mathrm{mix}} Q` and `Q H_{\mathrm{mix}} P` as the first activation of hidden-sector coupling

The current best candidate parent mechanism for this lives one level up in the ambient-reduction scaffold: first define a phase-charge split on the hidden complex line `\Pi(u,v)` via the complex-structure operator `J_\Pi`, then ask the reduction map to carry the corresponding parent projectors into the reduced `T1/T2` projectors. If that can be made explicit, the support of `H_0` on `T1` would be inherited from the parent charge split rather than chosen directly in the reduced model.

At the current toy level, this means looking for a reduction map that preserves support:

- parent `(-)` phase-charge sector -> reduced `T1`
- parent `(+)` phase-charge sector -> reduced `T2`
- parent zero-mass operator supported only on the `(-)` sector -> reduced `H_0` supported only on `T1`

This is the cleanest algebraic form of Route A currently available.

Until those are shown, the safe status is:

- minimal zero-mass operator: disciplined target ansatz
- derivation of that ansatz from the parent structure: open

This is already enough to sharpen the burden of proof. The project no longer needs to ask vaguely whether "something in the parent geometry explains `T1`." The sharper question is whether the reduction map preserves charge support strongly enough that the parent zero-mass channel lands entirely in `T1`.

### Minimal Route A closure statement

The current best blocker-level target can now be written as a conditional derivation rather than only as an ansatz.

Assume:

1. **Parent charge split**
   the local hidden line carries projectors
   $$
   P_{\Pi,-}, \qquad P_{\Pi,+}, \qquad P_{\Pi,-}+P_{\Pi,+}=1
   $$
   with `P_{\Pi,-}` the parent sector whose reduced image is the `J^{01}` eigenvalue `-1/2` block `T1`
2. **Parent zero-mass support**
   the parent zero-mass generator satisfies
   $$
   H_{\Pi}^{(0)} = P_{\Pi,-} H_{\Pi}^{(0)} P_{\Pi,-}
   $$
3. **Support-preserving reduction**
   the reduced map satisfies
   $$
   \mathcal{R}_{\mathrm{op}}(P_{\Pi,-}) = P,
   \qquad
   \mathcal{R}_{\mathrm{op}}(P_{\Pi,+}) = Q,
   \qquad
   \mathcal{R}_{\mathrm{op}}(H_{\Pi}^{(0)}) = H_0
   $$
   and does not create support on `T2` from a parent operator already confined to the `(-)` sector.

Then the reduced zero-mass operator obeys

$$
H_0 = P H_0 P,
\qquad
QH_0 = 0,
\qquad
H_0Q = 0.
$$

So the immediate `N2` burden is no longer mysterious. It is to justify those three assumptions at the parent-reduction level, or else state exactly which one still has to be postulated.

This is a useful stopping point because it separates three logically different questions:

- whether the hidden line really carries the needed charge split
- whether the parent zero-mass channel is really supported only on one charge sector
- whether the reduction map really preserves that support

If only the first two hold, the framework still needs a stronger reduction map.
If only the third holds, the framework still needs a real parent zero-mass selection rule.
If all three hold, the reduced `T1` support of `H_0` follows without choosing the block structure by hand.

### Breaking assumption 2 into smaller burdens

The parent zero-mass support condition can now be decomposed into a structural part and a residual selection part.

First impose hidden-line phase covariance:

$$
[H_{\Pi}^{(0)},J_{\Pi}] = 0.
$$

Because the complexified hidden line splits into the `P_{\Pi,-}` and `P_{\Pi,+}` charge sectors, this already implies

$$
H_{\Pi}^{(0)} = h_- P_{\Pi,-} + h_+ P_{\Pi,+}.
$$

So covariance alone removes off-diagonal zero-mass mixing between the two hidden charge sectors. That is already nontrivial progress, because it means the direct zero-mass generator is forced to be charge-diagonal before reduction.

What then remains is the narrower **one-sector traversal** question:

- why should the strict zero-mass channel keep only `h_-` and set `h_+ = 0`
- or equivalently, why should the selected direction `u` pick one oriented charge sector as the direct traversal sector

This reduces the `N2` blocker substantially. The project does not need to derive one-sector support from nothing. It only needs to justify:

1. phase covariance on the hidden line
2. one-sector traversal under the selected zero-mass channel
3. support-preserving reduction into `T1/T2`

At this point the sign dictionary itself is no longer part of the blocker. Once the static `J^{01}` convention is fixed, `P_{\Pi,-}` is by definition the parent charge sector whose reduced image is `T1`, and `P_{\Pi,+}` maps to `T2`. What remains open is the support statement, not the naming.

There is also a cleaner way to package step 3. If the reduction map is built as a charge-generator intertwiner

$$
\mathcal{R}_{\mathrm{vec}}\, J_{\Pi,\mathrm{toy}}
=
J^{01}\,\mathcal{R}_{\mathrm{vec}},
$$

with

$$
J_{\Pi,\mathrm{toy}} = \frac12 K_{\Pi} \otimes \mathbf{1}_{\mathrm{vis}},
$$

then projector compatibility and support preservation follow from spectral transport rather than from an extra independent postulate. In that stronger formulation, the `N2` burden becomes:

1. phase covariance gives charge-diagonality on the hidden line
2. oriented one-sector traversal picks the parent `(-)` sector
3. the `N1` reduction map intertwines `J_{\Pi,\mathrm{toy}}` with `J^{01}`

and then the reduced `T1` support of `H_0` follows.

At the present level of the notes, this is no longer merely abstract. The ambient-reduction scaffold now contains an explicit basis-level candidate for `\mathcal{R}_{\mathrm{vec}}` on `W_- \oplus W_+` that exactly intertwines the maximal compact generators in the chosen gamma-matrix basis. So the live open part of step 3 is no longer compact-level existence. It is extension of that explicit intertwiner beyond the maximal compact subgroup to the generators that mix `T1` and `T2`.

Moreover, even the parent basis entering that intertwiner is now partially constrained from the parent side: hidden charge eigenvectors are fixed up to common phase by `K_\Pi` together with `C_\Pi`, and the visible basis is adapted to `L_u` and `L_v` on the quaternionic carrier. So the support-preservation problem is no longer tangled up with a completely free basis choice. The remaining dynamical burden is whether those parent-adapted conditions are enough to force the physically relevant reduction, not whether some basis can be chosen to make the formulas work.

At this point the residual ambiguity is also much smaller than before: essentially one harmless overall phase and one global orientation reversal. So the live dynamical question is not about a large hidden gauge freedom in the reduction map. It is about whether the parent dynamics fixes the remaining orientation choice strongly enough to privilege one-sector traversal.

There is now a cleaner way to state that last point. The reduced observable theory already comes with a forward coarse-grained arrow:

$$
\rho_1(t) = e^{\,t\mathcal L_1}\rho_1(0),
\qquad t \ge 0.
$$

So the residual global reversal should exchange not only the two candidate readout sectors but also the sign of the reduced time parameter. In that language, the remaining dynamical choice is:

- which oriented hidden sector is aligned with the forward reduced semigroup and the direct zero-mass generator?

This yields a minimal forward-orientation criterion:

- choose the orientation for which `H_0` has support on the same sector that carries forward observable semigroup evolution

That still does not derive the choice from the bulk. But it does pin the final `\mathbf Z_2` to a concrete dynamical question rather than leaving it as a loose representational ambiguity.

If 1 and 3 hold, but 2 does not, then the reduced zero-mass operator would still be block diagonal but would generically have support on both `T1` and `T2`.
If 1, 2, and 3 all hold, then the strict `T1` support of `H_0` follows.

So the live derivation target is now more focused than before:

- derive charge-diagonality from hidden phase covariance
- derive one-sector traversal from the chosen direction and zero-mass channel
- then transport that support through the reduction map
- finally explain why that same sector is the one carrying forward reduced observable evolution

That is a much cleaner blocker statement than the older undifferentiated demand to "derive why `H_0` lives on `T1`."

There is now also a partial consistency route to step 2. Under `u \mapsto -u`, the hidden charge sectors are exchanged, so they should be read as the two orientations of one hidden line. For a charge-diagonal parent zero-mass operator

$$
H_{\Pi}^{(0)} = h_- P_{\Pi,-} + h_+ P_{\Pi,+},
$$

the cases are:

- `h_- = h_+`: the direct channel is blind to orientation
- `h_- \neq h_+` with both nonzero: there are two direct oriented zero-mass channels
- exactly one nonzero coefficient: there is one direct oriented zero-mass channel

So if the framework insists that the selected `u` remains an oriented physical choice and that zero-mass readout uses one privileged direct channel, one-sector traversal becomes the minimal consistent realization. This still falls short of a full derivation, but it is stronger than leaving step 2 as a completely free convention.

---

## Reduction regime

The main reduced-dynamics results in this kernel are only claimed under a specific regime.

### Assumptions

1. **Weak coupling**
   The mixing scale `m ||V||` is perturbative relative to the hidden-sector relaxation scale.

2. **Fast hidden-sector decorrelation**
   The sector `T2` admits a reference state whose relevant correlation functions decay on a timescale `gamma^{-1}`.

3. **Markov coarse-graining**
   The observation timescale is long compared with `gamma^{-1}` but short compared with the inverse secular scale generated by the coupling.

4. **Long-wavelength closure**
   For the diffusive limit, unresolved hidden-sector excursions are effectively short-range and isotropizing on the coarse-graining scale.

These assumptions define the domain of validity. Outside them, the reduced equation is not claimed.

---

## Reduced projected dynamics

In the interaction picture relative to the block-diagonal part of the generator, the projected state satisfies a second-order equation of Nakajima-Zwanzig type:
$$
\dot{\rho}_1(t)
= - i [H_{\mathrm{tr}},\rho_1(t)]
- m^2 \int_0^t ds \;
\mathrm{Tr}_{T2}
\Big(
[K,[K(-s),\rho_1(t) \otimes \rho_2^\ast]]
\Big)
+ \cdots
$$
where `rho_2^*` is the reference hidden-sector state.

What matters for the kernel is:

- the first nonvanishing correction from sector mixing is quadratic in `m`
- the hidden sector enters through its correlation functions
- the projected dynamics is nontrivial even though observables are extracted only in `T1`
- the privileged role of `T1` is inherited from the zero-mass channel, not just inserted after the fact

In the present revised framing, a richer hidden correction should be read as living on an internal oriented `2`-plane when antisymmetric structure is needed. That language is preferred to the older extra-timelike wording inside the effective kernel.

Under the Markov approximation, this becomes a time-local generator of Lindblad type:
$$
\dot{\rho}_1
= - i [H_{\mathrm{eff}},\rho_1] + \mathcal{D}(\rho_1),
$$
with dissipator
$$
\mathcal{D}(\rho_1)
= \sum_a
\left(
L_a \rho_1 L_a^\dagger
- \frac{1}{2} \{L_a^\dagger L_a,\rho_1\}
\right).
$$

So the safe derived statement is:

- projected sector dynamics becomes Markovian and completely positive in the weak-coupling reduction regime

That is one of the core level-4 claims of the dynamics domain.

---

## Diffusive limit

To pass from reduced quantum evolution to a transport law, one further assumes:

- a transport generator in `T1`
- a semiclassical or kinetic description
- an isotropizing hidden-sector effect at long scales

Then the observable density `n(x,t)` satisfies:
$$
\partial_t n + \nabla \cdot (v n) = D \nabla^2 n.
$$

Within the same reduction regime, the effective diffusion scale is:
$$
D \sim \frac{m^2}{\gamma},
$$
up to model-dependent constants and coarse-graining length scales.

This is the kernel version of the main dynamical result:

- zero mixing gives pure transport
- nonzero mixing gives diffusive broadening at the first nonvanishing order, namely order `m^2`

In the revised high-level reading:

- zero-mass propagation remains confined to `T1`
- massive structure opens access beyond pure `T1` propagation

This is the strongest clean dynamical statement currently available in the reduced model.

---

## Octonionic Two-Branch Transport

This section records an amplitude-level picture complementary to the Lindblad-Markov reduction above. The Lindblad reduction operates at the density-matrix level after coarse-graining; this section describes the coherent two-branch amplitude structure that exists before coarse-graining and from which the Lindblad picture should ultimately be derived.

### Setup

Non-associativity means that for generic bulk elements $a, b, c \in \mathbb{O}$, the two bracket completions project differently onto the transport slice:

$$A = P_u((ab)c), \qquad B = P_u(a(bc)) \in \mathbb{C}_u$$

Rather than forcing $A = B$ — which would impose associativity by hand — the framework retains both. The **transport-coherence invariant** is:

$$\mathcal{I} = A\bar{B}$$

$|\mathcal{I}|$ encodes whether both branches survive; $\arg(\mathcal{I})$ encodes the interference structure; its evolution determines stability. This replaces the single amplitude as the fundamental object.

**Spin(2,3) structural grounding.** Packaging the paired amplitudes as a real 4-vector $X = (\Re A, \Im_u A, \Re B, \Im_u B)^T \in \mathbb{R}^4$, the invariant $\mathcal{I} = A\bar{B}$ is precisely the symplectic pairing $\Omega(X, \cdot)$ for the canonical symplectic form on $\mathbb{R}^4$. Since $\mathrm{Sp}(4,\mathbb{R}) \cong \mathrm{Spin}(2,3)$, this identifies $\mathcal{I}$ as the natural Spin(2,3)-invariant object. Conjugate-branch pairing and symplectic structure are the same geometric datum.

### The signed transport coupling

The associator $[a,b,c] = (ab)c - a(bc)$ lives in $\mathrm{Im}\,\mathbb{O}$, as does the transport axis $u$. Their inner product is the natural Spin(2,3)-compatible signed scalar:

$$\kappa_u(a,b,c) = \kappa_0 \, \frac{\langle u, [a,b,c] \rangle}{\Lambda^3}$$

where $\Lambda$ is the octonionic scale and $\kappa_0$ is the transport coupling constant. The sign of $\kappa_u$ determines whether branch interaction is constructive ($\kappa_u > 0$), decoupled ($\kappa_u = 0$), or frustrated ($\kappa_u < 0$). An unsigned coupling could only strengthen coherence; the signed version allows the framework to classify states.

The associator can be packaged as a 5-vector $\mu^I$ in the vector representation of Spin(2,3), with $Q(\mu) = \eta_{IJ}\mu^I\mu^J = |[a,b,c]|^2$. The signed coupling is then the Sp(4,$\mathbb{R}$)-compatible projection of $\mu^I$ onto the transport axis.

### Orientation-forcing target from `\kappa_u`

This signed coupling gives the cleanest current bulk candidate for fixing the last global orientation choice.

Under

$$
u \mapsto -u,
$$

one has

$$
\kappa_u \mapsto -\kappa_u.
$$

So `\kappa_u` is exactly the kind of odd bulk scalar that can distinguish the two residual global orientations.

This matters because the transport classification already interprets the sign of `\kappa_u` physically:

- `\kappa_u > 0`: constructive branch coupling
- `\kappa_u < 0`: inverted or frustrated orientation

That suggests a concrete next derivation target:

> show that the sector carrying direct zero-mass readout is precisely the sector for which the bulk orientation makes the observable branch constructive/persistent.

If such a result held, then the last `\mathbf Z_2` would no longer be fixed only by a readout convention. It would be fixed by the sign of a bulk odd scalar already present in the octonionic transport dynamics.

The strongest clean version would be:

1. the residual global reversal flips both the candidate readout sector and the sign of `\kappa_u`
2. forward observable readout is required to lie on the constructive/persistent side of the transport dynamics
3. therefore the physically chosen orientation is the one with the corresponding sign of `\kappa_u`

This is not yet derived. But it is a much better target than an abstract request to "fix the last sign somehow," because it names the bulk quantity that would do the job if the programme succeeds.

### Constructive-readout criterion

The `\kappa_u` target can be sharpened one step further using the phase portrait itself.

For a locked direct-readout branch, the phase reference may be chosen so that the readout fixed point sits at

$$
\Phi_* = 0.
$$

In that phase-normalized gauge, the order parameter becomes

$$
\mathcal O_* = \kappa_u,
$$

and the persistence condition reduces to

$$
\kappa_u \cosh(2\rho_*) > \gamma.
$$

In particular, any long-lived direct readout branch in this normalization must satisfy

$$
\kappa_u > 0.
$$

So the residual global reversal has a concrete dynamical effect:

- `u \mapsto -u` flips `\kappa_u`
- hence it exchanges the constructive and inverted orientations of the locked branch

This yields the strongest current bulk-level orientation selector:

> choose the global orientation for which the direct readout branch is phase-normalized to `\Phi_*=0` and lies in the constructive/persistent sector, equivalently `\kappa_u > 0`.

This is stronger than the earlier statement "pick the forward readout arrow" because it ties the readout orientation directly to the exact reduced transport equations.

What remains open is still nontrivial:

- why the observable readout branch should be required to be constructive rather than inverted
- whether that requirement can be derived from the bulk rather than imposed as the final operational rule

### Physical content of the orientation axiom

The constructive/inverted distinction has a concrete geometric reading that converts the orientation axiom from a pure sign convention into a statement about the branch amplitudes.

At the symmetric (`\rho = 0`) locked fixed point, the persistence condition gives

$$
\kappa_u \cos\Phi_* = \gamma > 0.
$$

The real part of the transport-coherence invariant at the fixed point is

$$
\mathrm{Re}_u(AB)\big|_{*} = R^2 \cos\Phi_*.
$$

Substituting the persistence condition:

$$
\mathrm{Re}_u(AB)\big|_{*} = \frac{R^2\,\gamma}{\kappa_u}.
$$

**Constructive class (`\kappa_u > 0`).** The fixed-point phase satisfies `\cos\Phi_* > 0`, so `\mathrm{Re}_u(AB) > 0`. The two bracket completions `A = P_u((ab)c)` and `B = P_u(a(bc))` interfere constructively at the fixed point: their product `AB` has positive real part on the `u`-line.

**Inverted class (`\kappa_u < 0`).** The fixed-point phase satisfies `\cos\Phi_* < 0`, so `\mathrm{Re}_u(AB) < 0`. The two bracket completions interfere destructively: their product has negative real part on the `u`-line.

So the orientation axiom can be stated without reference to a gauge convention:

> **Orientation axiom.** The observable direct readout selects the branch class for which the two octonionic bracket completions are in constructive interference at the transport fixed point, i.e., `\mathrm{Re}_u(AB)|_* > 0`. This selects the constructive class and forces `\kappa_u > 0`.

This is a physically motivated statement: constructive interference means the two bracketings reinforce each other, sustaining the transport amplitude. Destructive interference means they partially cancel, which is the physically disfavoured outcome for a stable readout channel.

**Why this is still an axiom, not a derivation.** The statement above identifies what `\kappa_u > 0` means geometrically, but it does not derive from the octonionic bulk which states have `\mathrm{Re}_u(AB) > 0` at their transport fixed points. That would require tracking specific octonionic data `(a,b,c)` through the reduction to the branch fixed point, which is a further derivation task. At present, `\kappa_u > 0` is the cleanly named final orientation axiom, with its geometric content now explicit.

### Conditional `N2` closure

The zero-mass / mixing split is now conditionally closed.

In place without further assumption:

1. charge-diagonality of the parent zero-mass operator from hidden-line phase covariance
2. support transport through the reduction map via the charge-generator intertwiner `J_{\Pi,\mathrm{toy}} \to J^{01}`
3. a fixed sign dictionary sending the parent `(-)` charge sector to `T1`, up to the single global orientation reversal
4. the coupling term `\kappa_u \mathcal M_{\mathrm{ex}}` is symmetry-forced: `\kappa_u` is `K`-invariant and exchange-odd, so by the uniqueness argument it can only descend as the coefficient of `\mathcal M_{\mathrm{ex}}`

The remaining live issue is one named final axiom:

> **Orientation axiom.** The unique direct observable readout branch is the constructive locked branch — the one for which `\mathrm{Re}_u(AB)|_* > 0` at the transport fixed point, equivalently `\kappa_u > 0`.

Under that axiom:

- the residual global `\mathbf Z_2` is fixed by the sign of `\kappa_u`
- the direct-support parent sector is the `(-)` charge sector
- the reduced zero-mass operator satisfies

$$
H_0 = P H_0 P,
\qquad
QH_0 = 0,
\qquad
H_0Q = 0.
$$

**Honest current state.** `N2` is conditionally closed. The projector bookkeeping, basis-level intertwiner, charge-generator intertwining, and coupling slot are all in place. The one remaining open task is to derive the orientation axiom (`\kappa_u > 0`) from the octonionic bulk geometry — or to accept it as the named final axiom and move the programme forward. The project can proceed under the axiom now; the bulk derivation is a sharpening task, not a blocker.

### Two-branch evolution equations

The minimal evolution equations preserving transport symmetry and conjugate pairing are:

$$\dot{A} = (u\omega - \gamma)A + \kappa_u \bar{B}$$
$$\dot{B} = (u\omega - \gamma)B + \kappa_u \bar{A}$$

where $\omega$ is the null transport rotation frequency and $\gamma \geq 0$ is the loss rate into the mixing sector.

**Derivation status.** These are the minimal ansatz consistent with the symmetry requirements. A derivation from a variational principle on the octonionic bulk has not been completed; the equations are structurally motivated. This is an open problem (see open-problems ledger below).

### Minimal `N3` derivation template

The bulk derivation no longer needs to be treated as a blank box. A first real derivation draft would only need to produce the following reduced data.

1. A branch state

$$
\Psi = (A,B)
$$

living in a two-component amplitude space over the selected complex line determined by `u`.

2. An anti-linear branch-exchange involution

$$
\mathcal C(A,B) = (\bar B,\bar A),
\qquad
\mathcal C^2 = 1,
$$

which packages the conjugate pairing already built into the transport ansatz.

3. A reduced first-order generator split into three conceptually distinct pieces:

$$
\dot{\Psi}
=
u\omega\,\Psi
- \gamma\,\Psi
+ \kappa_u\,\mathcal C\Psi.
$$

In that split:

- `u\omega` is the transport-axis phase rotation
- `\gamma` is the positive leakage or coarse-grained loss into the hidden/mixing sector
- `\kappa_u` is the odd associator moment along the selected axis

So the minimal bulk derivation target is not yet a full field theory. It is the production of:

- a symplectic or first-order pairing on the branch space
- an odd moment map whose projection onto `u` gives `\kappa_u`
- a hidden-sector elimination, Rayleigh term, or equivalent positive mechanism producing `\gamma \ge 0`
- a parent exchange/conjugation operation reducing to `\mathcal C`

If those four ingredients are obtained, then the two-branch equations cease to be only a strong structural ansatz. They become the reduced effective equations forced by the parent bulk data.

What still has to be shown is also now much clearer:

- that `\mathcal C` comes from the parent reduction rather than being inserted by hand
- that `\kappa_u` is a genuine Hamiltonian or moment-map generator, not merely an invariant scalar projection
- that `\gamma` emerges from hidden-sector elimination rather than being appended as a free loss term

That is the right first target for `N3`.

### Parent candidate for the exchange involution

The good news is that `\mathcal C` does not have to be conjured out of thin air. The reduction picture already contains a natural parent candidate for it.

On the hidden line, the parent charge-flip operator `C_\Pi` exchanges the two oriented charge sectors,

$$
C_\Pi \xi_- = \xi_+,
\qquad
C_\Pi \xi_+ = \xi_-.
$$

Once the selected `u`-complex line is fixed, ordinary conjugation on that line reverses the phase orientation. So the simplest reduced candidate for the amplitude-level exchange involution is:

- hidden charge flip from `C_\Pi`
- combined with conjugation on the selected complex line
- read in branch variables as `\mathcal C(A,B) = (\bar B,\bar A)`

So one piece of `N3` is already partly scaffolded by `N1/N2`. The live task is not to invent an exchange operation, but to show that the parent charge-flip-plus-conjugation structure is exactly the dynamical involution that appears in the two-branch transport equations.

### Minimal Hamiltonian-Rayleigh scaffold

The two-branch equations can also be sharpened one step further at the effective level. They are not merely an arbitrary pair of first-order equations; they already fit an exact Hamiltonian-plus-dissipation template on the selected `u`-complex line.

Write

$$
A = a_1 + u a_2,
\qquad
B = b_1 + u b_2,
$$

and package the real branch coordinates as

$$
X = (a_1,a_2,b_1,b_2)^T \in \mathbb R^4.
$$

On this branch space, use the canonical `u`-adapted symplectic form

$$
\Omega_u(X,Y) = X^T J_u Y,
\qquad
J_u =
\begin{pmatrix}
0 & -1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0
\end{pmatrix}.
$$

Then the quadratic effective Hamiltonian

$$
H_{\mathrm{eff}}
=
\frac{\omega}{2}\bigl(|A|^2 + |B|^2\bigr)
- \kappa_u\,\mathrm{Im}_u(AB)
$$

together with the Rayleigh functional

$$
\mathcal R_{\mathrm{eff}}
=
\frac{\gamma}{2}\bigl(|A|^2 + |B|^2\bigr)
$$

produces the branch equations exactly through the Hamilton-Rayleigh system

$$
\dot X = J_u \nabla H_{\mathrm{eff}} - \nabla \mathcal R_{\mathrm{eff}}.
$$

Equivalently, since

$$
\mathrm{Im}_u(AB) = a_1 b_2 + a_2 b_1,
$$

the effective Hamiltonian is

$$
H_{\mathrm{eff}}
=
\frac{\omega}{2}(a_1^2+a_2^2+b_1^2+b_2^2)
- \kappa_u(a_1 b_2 + a_2 b_1),
$$

and one checks directly that

$$
\dot X
=
\begin{pmatrix}
0 & -\omega & \kappa_u & 0 \\
\omega & 0 & 0 & -\kappa_u \\
\kappa_u & 0 & 0 & -\omega \\
0 & -\kappa_u & \omega & 0
\end{pmatrix}X
- \gamma X,
$$

which is exactly equivalent to

$$
\dot{A} = (u\omega - \gamma)A + \kappa_u \bar{B},
\qquad
\dot{B} = (u\omega - \gamma)B + \kappa_u \bar{A}.
$$

This is a real gain for `N3`. It means the bulk derivation no longer has to guess the form of the reduced dynamics. It only has to explain why the parent octonionic reduction yields:

- the `u`-adapted symplectic structure on branch space
- the rotation term `\frac{\omega}{2}(|A|^2+|B|^2)`
- the odd coupling Hamiltonian `-\kappa_u\,\mathrm{Im}_u(AB)`
- the positive Rayleigh term `\frac{\gamma}{2}(|A|^2+|B|^2)`

So the transport system has now moved beyond "strong ansatz" in one specific sense: its minimal effective generator is explicit. The remaining problem is to derive that generator from the octonionic parent rather than merely write it down at the branch level.

### Parent origin of the transport frequency `\omega`

The rotation term `\frac{\omega}{2}(|A|^2+|B|^2)` already has a clean Lie-theoretic origin in the reduction data, parallel to the `\kappa_u` descent.

**The compact `U(1)` generator on branch space.** The compact `U(1)` factor in `K = U(1) \times SU(2)` is generated by phase rotation on the selected `u`-complex line. In branch variables this acts as

$$
L_u : (A,B) \mapsto (uA,\, uB).
$$

In real coordinates `X = (a_1,a_2,b_1,b_2)^T`, left-multiplication by `u` is exactly the symplectic matrix `J_u`. So the `U(1)` generator on branch space is

$$
V_{U(1)} = J_u X.
$$

**The `\omega` term as the `U(1)` moment map.** For the Hamiltonian system on branch space with symplectic form `\Omega_u`, the moment map of the `U(1)` action is the function whose Hamiltonian vector field is `J_u X`:

$$
\mu_{U(1)}(X)
=
\frac{1}{2}\,\Omega_u(X, J_u X)
=
\frac{1}{2}(a_1^2 + a_2^2 + b_1^2 + b_2^2)
=
\frac{1}{2}(|A|^2 + |B|^2).
$$

The rotation term in `H_{\mathrm{eff}}` is

$$
\frac{\omega}{2}(|A|^2 + |B|^2) = \omega\,\mu_{U(1)}(X).
$$

So `\omega` is not an independent phenomenological frequency. It is the `U(1)` moment map value: the symplectic charge conjugate to the phase-rotation angle on branch space.

**Parent identification.** In the octonionic bulk, the `U(1)` is the phase rotation on `\mathbb C_u = \mathbb R \oplus u\mathbb R`. The preferred direction `u` generates a `U(1) \subset G_2` that is already contained in `\mathrm{Stab}_{G_2}(u)` (acting by left-multiplication). The moment map value for this action, evaluated on the branch amplitudes, is exactly `(1/2)(|A|^2+|B|^2)`. So `\omega` is the octonionic transport phase momentum projected onto the selected axis — the null transport frequency inherited from the parent `U(1)` charge.

**What this closes.** The rotation term `\frac{\omega}{2}(|A|^2+|B|^2)` in `H_{\mathrm{eff}}` is now identified as the `U(1)` moment map of the compact reduction data. It is not a free term chosen to match the transport ansatz. It is the unique quadratic `U(1)`-Hamiltonian on branch space, fixed by the same compact reduction data that determines the coupling slot.

**What remains.** The moment map value `\omega` is a number — the actual transport phase momentum of a given state — not a universal constant of the theory. Its dependence on the parent octonionic data (the specific amplitudes `a, b, c` entering the transport slice) is not yet derived. That is a further reduction question, but it is now a quantitative question about the `U(1)` charge of physical states, not a structural question about the form of the Hamiltonian.

### Reduced generator slot for `\kappa_u`

The Hamiltonian scaffold also clarifies the geometric role of the signed coupling. On branch space, define the fixed quadratic function

$$
\mathcal M_{\mathrm{ex}}(A,B)
:=
-\mathrm{Im}_u(AB)
=
-(a_1 b_2 + a_2 b_1).
$$

Its Hamiltonian vector field with respect to `\Omega_u` is exactly the conjugate branch-exchange flow:

$$
X_{\mathcal M_{\mathrm{ex}}}
=
J_u \nabla \mathcal M_{\mathrm{ex}}
=
(b_1,-b_2,a_1,-a_2)^T,
$$

which in complex form is precisely

$$
\dot A = \bar B,
\qquad
\dot B = \bar A.
$$

So at the reduced level, `\kappa_u` is not filling an arbitrary coupling slot. It multiplies a very specific Sp(4,`R`)-compatible quadratic generator:

$$
H_{\mathrm{cpl}} = \kappa_u\,\mathcal M_{\mathrm{ex}}.
$$

This sharpens the remaining parent task. The bulk does not need to invent the coupling structure from scratch. It needs to show that the octonionic associator moment projected onto `u` reduces to the coefficient of this already-identified exchange generator.

### Why `\kappa_u` has a unique symmetry-allowed reduced slot

The reduction data make the coupling slot more rigid than it may first appear.

As a representation of the compact subgroup, the branch carrier is

$$
W
=
(\mathbf 1_- \otimes \mathbf 2)\oplus(\mathbf 1_+ \otimes \mathbf 2).
$$

Consider anti-linear maps `T : W \to W` with the following properties:

- they intertwine the visible `SU(2)` action
- they swap the hidden `U(1)` charge sectors
- they square to the identity up to harmless overall phase

Then `T` is unique up to an overall scalar. The reason is simple:

- on the visible doublet factor, any `SU(2)`-equivariant map is proportional to the identity
- on the hidden factor, charge swapping is already fixed by `C_\Pi`
- anti-linearity is supplied by conjugation on the selected `u`-complex line

So, up to normalization, the only compact-equivariant anti-linear exchange map is exactly

$$
\mathfrak C_u = (C_\Pi \otimes \mathbf 1_{\mathrm{vis}})\circ \mathfrak K_u.
$$

Consequently, the only quadratic Hamiltonian of this symmetry type is proportional to

$$
\mathcal M_{\mathrm{ex}}(\Psi)
=
-\frac12\,\Omega_u(\Psi,\mathfrak C_u\Psi)
=
-\mathrm{Im}_u(AB).
$$

This is a strong narrowing of `N3`. If the parent bulk preserves the compact reduction data and produces any odd scalar moment from the associator projected onto `u`, then that scalar has only one symmetry-allowed reduced destination: it must appear as the coefficient multiplying `\mathcal M_{\mathrm{ex}}`. In that sense, `\kappa_u` is not merely compatible with the exchange generator; it is the unique symmetry-allowed coefficient of that generator.

This can be packaged as a practical descent criterion:

> If the parent bulk produces a reduced quadratic Hamiltonian contribution that is compact-equivariant, anti-linear-exchange odd, and linear in the projected associator moment along `u`, then that contribution must take the form `\kappa_u \mathcal M_{\mathrm{ex}}` up to normalization.

So one clean way to advance `N3` is not to derive the full equations at once, but to show that the parent odd scalar moment satisfies those hypotheses.

### Parent anti-linear candidate for the exchange moment

The reduction data also suggest a clean parent-level source for `\mathcal M_{\mathrm{ex}}`.

Let `\mathfrak K_u` denote conjugation on the selected `u`-complex line, and let `C_\Pi` be the hidden charge-flip involution already fixed by the reduction scaffold. On the branch carrier, define the anti-linear map

$$
\mathfrak C_u := (C_\Pi \otimes \mathbf 1_{\mathrm{vis}})\circ \mathfrak K_u.
$$

In the adapted charge basis, this acts exactly as

$$
\mathfrak C_u(A,B) = (\bar B,\bar A).
$$

So the reduced exchange involution used in the transport equations is not floating freely; it is the direct descendant of parent charge flip plus `u`-conjugation.

Moreover, the exchange Hamiltonian itself can be written as the symplectic pairing with this anti-linear map:

$$
\mathcal M_{\mathrm{ex}}(\Psi)
=
-\frac12\,\Omega_u(\Psi,\mathfrak C_u\Psi).
$$

In the real coordinate basis above this reduces exactly to

$$
\mathcal M_{\mathrm{ex}}(A,B) = -\mathrm{Im}_u(AB).
$$

This is useful because it localizes the parent task even more sharply. To derive the coupling term, the octonionic bulk does not need to guess a new quadratic form. It needs to produce the already-identified anti-linear exchange map `\mathfrak C_u` together with the `u`-adapted symplectic structure.

### Compact equivariance and exchange-odd character of the associator moment

The previous two sections establish: (a) there is a unique compact-equivariant anti-linear-exchange odd coupling slot; and (b) the parent exchange involution reduces to `\mathfrak C_u`. This section shows that the associator moment `\kappa_u` itself satisfies the required properties, so the descent is forced rather than merely compatible.

**Compact equivariance.** The compact subgroup is `K = U(1) \times SU(2)`. By construction, `K` is contained in the stabilizer of `u` in `G_2`:

$$
K \subset \mathrm{Stab}_{G_2}(u).
$$

This is not additional input. The compact reduction data — the charge structure on the hidden line, the visible `SU(2)` action — are defined relative to the fixed direction `u`. Any element `g \in K` preserves the octonionic product (since `K \subset G_2`) and fixes `u` (since `K \subset \mathrm{Stab}_{G_2}(u)`).

For `g \in G_2`, the associator is `G_2`-covariant:

$$
[ga,\, gb,\, gc] = g[a,b,c].
$$

This follows from the automorphism property: `(ga \cdot gb) \cdot gc - ga \cdot (gb \cdot gc) = g(ab) \cdot gc - ga \cdot g(bc) = g((ab)c) - g(a(bc)) = g[a,b,c]`.

Therefore

$$
\kappa_u(ga,\, gb,\, gc)
=
\langle u,\, g[a,b,c]\rangle
=
\langle g^{-1}u,\, [a,b,c]\rangle
=
\langle u,\, [a,b,c]\rangle
=
\kappa_u(a,b,c).
$$

The third equality uses `g^{-1}u = u`, which holds because `K \subset \mathrm{Stab}_{G_2}(u)`. So `\kappa_u` is `K`-invariant.

**Exchange-odd character.** The exchange involution is `\mathfrak C_u = (C_\Pi \otimes \mathbf 1_{\mathrm{vis}}) \circ \mathfrak K_u`. The `\mathfrak K_u` factor is conjugation on the selected `u`-complex line. Under `\mathfrak K_u`, the imaginary unit reverses:

$$
\mathfrak K_u : u \mapsto \bar u = -u.
$$

This is standard complex conjugation: on `\mathbb C_u = \mathbb R \oplus u\mathbb R`, conjugation sends `u \mapsto -u`. Since `\kappa_u = \langle u, [a,b,c]\rangle` is linear in `u`:

$$
\kappa_u \;\mapsto\; \langle -u,\, [a,b,c]\rangle = -\kappa_u.
$$

So `\kappa_u` is exchange-odd: it changes sign under the `\mathfrak K_u` component of `\mathfrak C_u`.

**Forced descent.** Combining: `\kappa_u` is `K`-invariant (compact-equivariant) and negated by `\mathfrak K_u` (exchange-odd). The uniqueness criterion already established says that any parent coupling satisfying those two properties must descend as `\kappa_u \mathcal M_{\mathrm{ex}}` up to normalization. Therefore the coupling term in the two-branch equations is not a free parameter. It is the symmetry-mandated image of the octonionic associator moment projected onto `u`.

**What this closes.** The `N3` live proof target — show the octonionic associator moment is compact-equivariant and anti-linear-exchange odd, forcing it to descend as `\kappa_u \mathcal M_{\mathrm{ex}}` — is answered at the Lie-algebraic symmetry level. The two-branch coupling term `\kappa_u \mathcal M_{\mathrm{ex}}` is the unique symmetry-allowed image, and the associator moment is the unique `G_2`-covariant bulk scalar carrying those properties for fixed `u`.

**Residual gaps.** Two gaps survive this argument.

1. **Variational origin.** This is a symmetry descent, not a variational derivation. The reduced effective Hamiltonian `H_{\mathrm{eff}}` is the unique compatible quadratic form on branch space, but obtaining it as the Legendre transform or moment map of a parent octonionic action remains open.

2. **Orientation.** Compact equivariance and exchange-odd character together fix the reduced coupling slot but not the sign of `\kappa_u`. Whether the direct readout branch must be constructive (`\kappa_u > 0`) or whether the sign can be derived from a bulk forcing argument is still open. At present the sign is fixed by the forward-semigroup / readout alignment criterion rather than from the parent geometry.

### Minimal hidden-sector elimination template for `\gamma`

The damping term can also be narrowed to a standard effective mechanism rather than a free appendage.

Let `X` denote the branch coordinates above, and let `\chi` denote a hidden-sector variable coupled to them. Consider the linear parent-effective system

$$
\dot X = J_u \nabla H_{\mathrm{eff}} - \lambda K^T \chi,
\qquad
\dot \chi = -\Gamma \chi + \lambda K X,
$$

with `\Gamma` positive on the hidden sector.

In the adiabatic or Markov regime,

$$
\chi \approx \lambda \Gamma^{-1} K X,
$$

so substitution gives

$$
\dot X
\approx
J_u \nabla H_{\mathrm{eff}}
- \lambda^2 K^T \Gamma^{-1} K X.
$$

If the hidden coupling is isotropic on the branch sector, so that

$$
\lambda^2 K^T \Gamma^{-1} K = \gamma\,\mathbf 1_4,
\qquad
\gamma > 0,
$$

then the reduced branch equations become exactly

$$
\dot X = J_u \nabla H_{\mathrm{eff}} - \gamma X,
$$

which is the real-coordinate form of

$$
\dot{A} = (u\omega - \gamma)A + \kappa_u \bar B,
\qquad
\dot{B} = (u\omega - \gamma)B + \kappa_u \bar A.
$$

This does not yet derive the actual hidden operator `K` or decay matrix `\Gamma` from the octonionic bulk. But it does show something important: `\gamma` no longer has to be treated as a mysterious phenomenological insertion. It already has a minimal positive effective origin as a Schur-complement or reservoir-elimination term.

### Why scalar `\gamma` is symmetry-natural

The reduction scaffold gives a further reason the damping should appear as a scalar on branch space rather than as an arbitrary `4 \times 4` matrix.

Let

$$
\mathcal D := \lambda^2 K^T \Gamma^{-1} K
$$

be the positive reduced dissipation operator obtained after hidden-sector elimination.

If `\mathcal D` commutes with the compact reduction data transported by `\mathcal R_{\mathrm{vec}}`, namely:

- the hidden `U(1)` charge generator
- the visible `SU(2)` action

then, on the branch space

$$
(\mathbf 1_- \otimes \mathbf 2) \oplus (\mathbf 1_+ \otimes \mathbf 2),
$$

it must have the form

$$
\mathcal D = \gamma_-\,\mathbf 1_2 \oplus \gamma_+\,\mathbf 1_2.
$$

That is already enough to say the damping is isotropic inside each charge sector. If, in addition, the hidden elimination respects the same charge-exchange symmetry implemented by `\mathfrak C_u`, then the two coefficients must agree:

$$
\gamma_- = \gamma_+ = \gamma.
$$

So the full reduced damping becomes

$$
\mathcal D = \gamma\,\mathbf 1_4.
$$

This is a meaningful narrowing of `N3`. Scalar damping no longer has to be postulated as a lucky simplification. It is the natural reduced outcome of:

- compact-equivariant hidden elimination
- plus symmetry under the parent charge-exchange involution

What still remains open is whether the actual octonionic bulk coupling really has those symmetry properties.

### Minimal admissible hidden coupling class

The symmetry argument above can be packaged as a concrete admissibility criterion for parent hidden-sector couplings.

Let the hidden reservoir carry some compact representation `R_{\mathrm{hid}}`, and let the branch space carry the compact reduction action already fixed by the scaffold. A hidden coupling pair `(K,\Gamma)` is minimally admissible if:

1. `K` intertwines the compact action between branch and hidden sectors
2. `\Gamma` commutes with the hidden compact action
3. both `K` and `\Gamma` respect a lifted charge-exchange involution compatible with `\mathfrak C_u`

Under these three conditions:

- `\mathcal D = \lambda^2 K^T\Gamma^{-1}K` automatically commutes with the compact action
- therefore `\mathcal D` is sectorwise scalar: `\gamma_- I_2 \oplus \gamma_+ I_2`
- charge-exchange symmetry then forces `\gamma_- = \gamma_+`

So one gets

$$
\mathcal D = \gamma\,\mathbf 1_4
$$

without having to impose scalar damping by hand.

This gives the next bulk target a much cleaner form. To derive `\gamma`, it is enough to identify a physically credible parent hidden coupling class satisfying those admissibility properties. If such a class cannot be found, then the theory should expect anisotropic damping or charge-sector-dependent leakage rather than the present scalar `\gamma`.

This can also be read as a falsifiable criterion:

> If the actual parent hidden elimination fails compact equivariance, or fails charge-exchange symmetry, then the reduced damping should not be scalar. One should instead expect `\gamma_- \neq \gamma_+` or a more general positive matrix on branch space.

That is useful because it tells us exactly what kind of bulk result would force a revision of the current transport ansatz, rather than merely leaving the status vague.

### Why `\gamma > 0` is forced by full hidden-sector coupling

The admissibility argument establishes that `\mathcal D = \gamma\,\mathbf 1_4` (scalar damping), but it does not by itself guarantee `\gamma > 0`. A zero or negative value would be pathological (no damping or anti-damping). The following argument closes this.

The reduced dissipation operator is

$$
\mathcal D = \lambda^2 K^T \Gamma^{-1} K.
$$

Since `\Gamma` is positive on the hidden sector (`\Gamma > 0`), `\Gamma^{-1}` exists and is also positive. Therefore `\mathcal D` is positive semi-definite for any `K`. It is strictly positive definite if and only if `K : \mathbb R^4_{\mathrm{branch}} \to \mathbb R^{n_{\mathrm{hid}}}` is injective — equivalently, if no branch-space direction lies in the kernel of the hidden coupling.

Physically, injectivity of `K` means every branch mode is coupled to the hidden reservoir. No branch direction is hidden-sector-transparent. This is the content of "full coupling": the reservoir damps all branch-space modes, not just some of them.

Under the admissibility scalar argument, `\mathcal D = \gamma\,\mathbf 1_4`. Strict positivity of `\mathcal D` then forces `\gamma > 0`.

**Summary.** Under two natural assumptions:

1. the hidden sector is stable/dissipative (`\Gamma > 0`)
2. the hidden coupling is full (`K` injective, no branch mode is invisible to the reservoir)

the scalar damping coefficient satisfies `\gamma > 0`. Neither assumption requires additional structure beyond what the admissibility criterion already takes as input.

**What remains open.** The actual value of `\gamma` — its dependence on the parent octonionic couplings, its momentum dependence, and its relation to the hidden-sector correlation timescale — requires the first-principles hidden correlator derivation. What is established here is only the sign, not the magnitude.

### Reduced system

Writing $A = r_1 e^{u\theta_1}$, $B = r_2 e^{u\theta_2}$ and defining:

$$R = \sqrt{r_1 r_2}, \qquad \rho = \tfrac{1}{2}\ln(r_1/r_2), \qquad \Phi = \theta_1 + \theta_2$$

**Proposition 1.** The two-branch dynamics reduce exactly to:

$$\dot{R} = R\big(-\gamma + \kappa_u\cosh(2\rho)\cos\Phi\big)$$
$$\dot{\rho} = -\kappa_u\sinh(2\rho)\cos\Phi$$
$$\dot{\Phi} = 2\omega - 2\kappa_u\cosh(2\rho)\sin\Phi$$

The effective coupling throughout is $\kappa_{\mathrm{eff}} = \kappa_u\cosh(2\rho) \geq |\kappa_u|$.

**Proposition 2.** Branch asymmetry ($\rho \neq 0$) strictly enhances phase locking. The symmetric sector $\rho = 0$ gives the most restrictive locking condition. All three equations are governed by the single order parameter $\mathcal{O} = \kappa_u\cos\Phi$.

### Classification theorem

Two geometric boundaries organize the phase space $(\rho, \Phi)$:

- **Locking boundary:** $|\omega| = |\kappa_u|\cosh(2\rho)$
- **Persistence boundary:** $\kappa_u\cosh(2\rho)\cos\Phi = \gamma$

**Theorem (forced classification).** These two boundaries partition the phase space into exactly four disjoint transport classes. The partition is forced by the geometry of the boundaries, not assumed.

| Class | Conditions | Fixed-Point Type | Physical Reading |
|-------|-----------|-----------------|-----------------|
| Constructive | $\kappa_u > 0$, locked, $\mathcal{O}\cosh(2\rho) > \gamma$ | Stable node | Long-lived coherent transport |
| Inverted | $\kappa_u < 0$, locked, $\lvert\mathcal{O}\rvert\cosh(2\rho) > \gamma$ | Stable node (opposite sector) | Phase-inverted coherent state |
| Frustrated | Locked but $\mathcal{O}\cosh(2\rho) < \gamma$ | Unstable node | Decaying resonance |
| Dephased | $\lvert\omega\rvert > \kappa_{\mathrm{eff}}$ | No fixed point | Incoherent, non-particle-like |

A state is **particle-like** if and only if it satisfies both:
$$|\omega| \leq |\kappa_u|\cosh(2\rho) \quad \text{(locking)}$$
$$\kappa_u\cosh(2\rho)\cos\Phi > \gamma \quad \text{(persistence)}$$

This is a geometric condition on $(\rho, \Phi, \kappa_u)$ determined entirely by the associator data and transport projection — not imposed externally.

### Relation to the Lindblad picture

The Lindblad-Markov reduction above is the density-matrix-level coarse-grained description. The two-branch amplitude picture is complementary: it operates at the coherent amplitude level before coarse-graining. How averaging the two-branch dynamics over bulk octonionic degrees of freedom produces the Lindblad reduction is an open derivation task. In the dephased class, where locking fails and amplitude decays as $\dot{R} \approx -\gamma R$, the $D \sim m^2/\gamma$ diffusion law should emerge from incoherent branch mixing.

---

## What the dynamics domain really establishes

The dynamics domain safely establishes the following.

1. A full-space microscopic evolution can induce nontrivial reduced dynamics on the projected sector.
2. The first correction generated by sector mixing is second order in the mixing strength.
3. In the Markov regime, the reduced equation has Lindblad form.
4. In the long-scale closure regime, the observable density obeys an advection-diffusion law.
5. The effective diffusion scale is controlled by the same mixing parameter that appears in the microscopic generator.

These are the core dynamical results.

---

## What remains interpretation

The following should remain interpretive unless proved more strongly elsewhere.

### Mass as mixing

It is natural to read `m` as an effective mass parameter because it controls the first departure from purely ballistic projected transport.

But the safe statement is:

- `m` is the microscopic sector-mixing scale

The stronger statement:

- `m` is mass

is interpretation unless tied to a broader dynamical or field-theoretic identification.

The new related interpretive possibility is:

- Higgs-mediated mass generation is the mechanism that opens the `T1/T2` bridge

That is promising, but still interpretive at present.

Another important interpretive proposal now in play is:

- the hidden two-direction structure needed for Heisenberg-type extensions is an internal complex `2`-plane, locally carried by a quaternionic slice of `O`

This comes from the folded `Spin(3,3)` analysis, but it remains a working proposal rather than a derived theorem.

### Uncertainty as hidden-sector effect

It is natural to read diffusive broadening as an observable shadow of unresolved hidden-sector excursions.

That is a strong conceptual reading, but still a reading.

### Chirality and spinorial meaning

The dynamics file should not claim that chirality or spin-1/2 behaviour has been fully derived unless that argument is independently carried in a clean and checkable way.

At present those belong outside the core dynamical theorem set.

---

## Dynamic claim ledger

This section records the main dynamical claims in kernel form.

| Claim | Role | Level | Comment |
|---|---|---|---|
| states evolve in the full space `T1 (+) T2` | postulate | 4 | central model input |
| zero-mass propagation remains on `T1` | central framework proposal | 4 | new dynamical center |
| observables are projected onto `T1` | effective rule downstream of channel selection | 4 | still central but less primitive |
| sector mixing can be modeled by an off-diagonal block term | model choice | 4 | minimal but not unique |
| the leading reduced correction is second order in `m` | derived under weak coupling | 4 | strong and useful |
| the reduced equation is of Lindblad type in the Markov regime | derived under assumptions | 4 | core JMP-style claim |
| the long-scale density satisfies advection-diffusion | derived under closure assumptions | 4 | main reduced transport result |
| `D ~ m^2 / gamma` | derived within model | 4 | clean scaling law |
| richer hidden corrections are best interpreted through an internal oriented `2`-plane rather than literal extra time directions | working interpretation | 4 | aligns the kernel with the revised parent story |
| `m` may encode physical mass after further identification | interpretation | 5 | plausible but stronger than the theorem |
| Higgs-mediated mass generation may be what opens the `T1/T2` channel | interpretation / future work | 5 | promising but not established |
| hidden-sector projection explains quantum uncertainty in general | interpretation / future work | 5 | suggestive but not established |
| the hidden-sector correlator is derived from first principles | missing | 6 | major dynamical gap |
| the transport-coherence invariant $\mathcal{I} = A\bar{B}$ is the Sp(4,ℝ)-invariant symplectic pairing of branch amplitudes | structural identification | 3–4 | $\mathcal{I}$ replaces single amplitude as fundamental object; connects to Spin(2,3) ≅ Sp(4,ℝ) |
| the signed coupling $\kappa_u = \kappa_0\langle u, [a,b,c]\rangle/\Lambda^3$ is the Spin(2,3)-compatible projection of the associator | structural identification | 4 | sign determines constructive / frustrated / inverted class |
| $\kappa_u$ is $K$-invariant (compact-equivariant) and exchange-odd, forcing it to descend as the unique coefficient of $\mathcal M_{\mathrm{ex}}$ | symmetry descent established | 3 | $K \subset \mathrm{Stab}_{G_2}(u)$ gives equivariance; $\mathfrak K_u: u \mapsto -u$ gives odd sign; uniqueness argument then forces the coupling slot — variational origin and orientation sign remain open |
| two-branch evolution equations are the minimal Spin(2,3)-compatible ansatz | coupling term symmetry-forced; full variational derivation open | 4 | the $\kappa_u \mathcal M_{\mathrm{ex}}$ coupling is now forced by symmetry descent; the remaining open task is deriving $\omega$ and $\gamma$ from a parent action |
| Propositions 1–2: exact reduction to $(R,\rho,\Phi)$ with effective coupling $\kappa_{\mathrm{eff}} = \kappa_u\cosh(2\rho)$ | derived within two-branch model | 4 | clean exact result once equations are accepted |
| forced classification into four transport classes (Constructive, Inverted, Frustrated, Dephased) | derived from geometry of locking and persistence boundaries | 4 | classification is forced, not assumed |
| particle-like state criterion: locking + persistence conditions are jointly necessary and sufficient | derived consequence of classification | 4 | geometric, not empirical |
| $\omega$ is the $U(1)$ moment map value on branch space — the null transport phase momentum | moment map identification established | 3 | $H_\omega = \omega\,\mu_{U(1)} = \frac{\omega}{2}(\lvert A\rvert^2+\lvert B\rvert^2)$ is the unique $U(1)$-Hamiltonian; $\omega$ is the symplectic charge conjugate to the phase-rotation angle |
| $\gamma > 0$ from full hidden-sector coupling: $\mathcal D = \lambda^2 K^T\Gamma^{-1}K > 0$ under $\Gamma > 0$ and $K$ injective | conditionally established | 3–4 | sign forced; magnitude requires hidden correlator derivation |
| $\kappa_u > 0$ is equivalent to $\mathrm{Re}_u(AB)\rvert_* > 0$ at the transport fixed point: constructive branch interference | orientation axiom named with geometric content | 4 | this is the final named axiom; bulk derivation of the sign remains open |
| derivation of two-branch evolution equations from variational principle on octonionic bulk | partially closed: $\kappa_u \mathcal M_{\mathrm{ex}}$ and $\omega\,\mu_{U(1)}$ terms are symmetry-derived; $\gamma$ mechanism identified; full parent action derivation open | 5 | the remaining open task is a parent action from which all three generator pieces descend simultaneously |
| connection between two-branch amplitude picture and Lindblad-Markov density-matrix picture | missing | 5 | how coarse-graining recovers the Lindblad picture is an open task |

---

## NS Programme structural corroboration

This section records corroboration of key dynamical claims from the NS/J3(O) regularity programme. All bridge identifications are structural proposals (Level 5). The underlying NS results are at Level 3–4. None of the items here substitute for independent derivation within the Spin(2,3) framework.

---

### T1/T2 split and the strain-only blow-up ray

**What the NS programme established (Level 3):**

The NS programme identifies a 1D curve in the Q-R invariant plane — the strain-only ray Q = −3a²/4, R = −a³/4 — as the exact blow-up attractor of restricted Euler dynamics. On this ray: the cubic defect J̃ = det[ξ̂, ê₁, Ω̂ω] vanishes; vorticity aligns with a strain eigenvector; the discriminant Δ = 27R² + 4Q³ = 0 is maintained; and the flow has no transverse triadic coupling. This is an exact algebraic result. The complementary result is that physical NS solutions are regularised by transverse terms (vortex line curvature and twist) which prevent collapse onto the ray.

**What this addresses here (Level 4):**

The central dynamical claim of this framework is that zero-mass interactions propagate only on T1, with T2 entering through off-diagonal mixing once mass is present (Principle D2). The question of why T1-pure propagation should be dynamically unstable — equivalently, why the hidden sector relaxation γ > 0 is forced rather than assumed — is an open problem.

**Proposed bridge identification (Level 5):**

The strain-only ray corresponds to the T1-pure sector. More precisely: T1-pure propagation = no transverse coupling = strain-only ray (J̃ = 0); T2 mixing = transverse triadic coupling = off-strain-ray deviation (J̃ ≠ 0). NS regularity = T2 mixing prevents T1 collapse. Under this identification, the NS result that T1-pure blow-up is prevented by transverse (T2) terms translates into: the T1 channel is stable precisely because T2 mixing is present.

This belongs in discussion at Level 5 as structural corroboration of the hidden-sector picture. It should not appear as a derivation.

**What this file still needs:**

An independent argument that T1-pure propagation is dynamically unstable in the Spin(2,3) setting, or that hidden sector relaxation γ > 0 is forced by the dynamics. This is the Spin(2,3) analogue of Gap A in the NS programme.

---

### Exponent gap 1/2 and the fermionic sector

**What the NS programme established (Level 4):**

The NS programme derives a scaling contradiction under Type I blow-up. Near T*: N_lifted ~ C'/(T*−t)^{7/2} from β·b² scaling, while Type I + Jacobi gives N_lifted ≤ C/(T*−t)³. The gap is 7/2 − 3 = 1/2. This gap is robust to logarithmic corrections because the separation is 1/2, not approaching zero.

**What this addresses here:**

The exponent gap of 1/2 is a half-integer. In Spin(2,3), half-integer scaling dimensions correspond to fermionic representations. The spinor representation of Spin(2,3) = Sp(4) has dimension 4 and carries half-integer quantum numbers.

**Proposed bridge identification (Level 5):**

The robustness of the exponent gap 1/2 reflects the rigidity of the fermionic sector in the Spin(2,3) representation theory. Integer exponent gaps can be corrected by bosonic renormalisation effects; half-integer gaps are protected by spin-statistics and cannot be perturbed by bosonic interactions. The exponent gap 1/2 in the NS programme may be robust for the same algebraic reason that the Dirac operator gap is robust in Spin(2,3): both are protected by the representation theory of the same group.

This is a structural observation, not a derived result. It does not prove the gap is exactly 1/2 in the rigorous PDE sense; it observes that if the gap is 1/2, its robustness has a representation-theoretic explanation.

**What this file still needs:**

A derivation within the Spin(2,3) setting that the relevant scaling exponents are forced to differ by exactly 1/2 by the representation theory of Spin(2,3).

---

### Diffusion law D ~ m²/γ and the NS exponent scaling

**What the NS programme established (Level 4):**

Under Type I blow-up near T*: a(t) ~ 2/(T*−t) (strain rate); b_ij ~ ω_i · u_j ~ C/(T*−t)^{5/4} (vorticity correlation); ratio b/(a/2) ~ (T*−t)^{−1/4} → ∞ confirming b exceeds the filter threshold near blow-up. The Raychaudhuri Riccati equation gives C_eff = 0.022 ≪ 1/3 (Level 4, N=32³, needs N=64³ confirmation), placing the NS flow well inside the stable regime.

**What this addresses here (Level 4):**

The diffusion law D ~ m²/γ is derived here under reduction assumptions. The physical identification of m and γ from more fundamental data remains open.

**Proposed bridge identification (Level 5):**

The NS scaling quantities map onto the Spin(2,3) diffusion law parameters as: m ~ a(t) ~ (T*−t)⁻¹ (strain rate as sector-mixing scale); γ ~ |b_ij| ~ (T*−t)^{−5/4} (vorticity correlation rate as hidden-sector relaxation); D ~ m²/γ ~ (T*−t)^{−3/4}. The diffusion coefficient diverges near blow-up, consistent with the flow becoming singular. The exponent 3/4 is dimensionally related to the gap 1/2 and the Spin(2,3) spinor representation.

Note: this mapping is dimensional and structural, not a derivation. The identification m ~ a(t) requires an independent physical argument and should not be imported as a derived result; it belongs in discussion.

---

## Interfaces to other domains

The dynamics domain uses and supplies the following interfaces.

### From statics

- the `T1/T2` split
- the projector structure
- the representation space on which the generator acts
- the selected axis that identifies the privileged zero-mass channel

### To epistemics

- a concrete model in which the zero-mass channel determines the effective observable law

### To consistency

- the reduced generator to be checked for positivity, trace preservation, and stability

### To interpretation

- the parameter `m`
- the hidden-sector excursions
- the reduced diffusion law

### To phenomenology

- the scaling relation `D ~ m^2 / gamma`
- the possibility of observable broadening or decoherence-like effects

---

## Major unresolved issues

The dynamics domain still owes:

1. a first-principles model for the hidden-sector correlator
2. a cleaner derivation of the Markov regime from microscopic assumptions
3. a relativistic field-theoretic completion
4. a sharper bridge from reduced transport to standard quantum observables
5. a sharper account of how Higgs-mediated mass generation relates to `T1/T2` coupling
6. quantitative predictions or bounds

These are not cosmetic gaps. They are the main reasons the dynamics domain must still be handled carefully in paper form.

---

## Working bottom line

The dynamics spine of the project is coherent.

At its safest level, it says:

1. evolution occurs in `T1 \oplus T2`
2. zero-mass propagation is confined to `T1`
3. observables are read through that privileged `T1` channel
4. sector mixing induces nontrivial reduced dynamics in `T1`
5. in the weak-coupling Markov regime, this reduced dynamics is Lindblad-like
6. in the long-scale closure regime, it becomes advection-diffusion with `D ~ m^2 / gamma`
7. the deeper hidden structure needed for richer corrections is best read as internal complex-plane data rather than literal extra timelike dynamics

That is already a meaningful kernel.

The main caution is that the strongest physical readings, especially "mass as mixing" in a full physical sense, still sit one layer above what the present dynamical derivation strictly proves.
