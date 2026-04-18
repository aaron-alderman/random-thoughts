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

### Two-branch evolution equations

The minimal evolution equations preserving transport symmetry and conjugate pairing are:

$$\dot{A} = (u\omega - \gamma)A + \kappa_u \bar{B}$$
$$\dot{B} = (u\omega - \gamma)B + \kappa_u \bar{A}$$

where $\omega$ is the null transport rotation frequency and $\gamma \geq 0$ is the loss rate into the mixing sector.

**Derivation status.** These are the minimal ansatz consistent with the symmetry requirements. A derivation from a variational principle on the octonionic bulk has not been completed; the equations are structurally motivated. This is an open problem (see open-problems ledger below).

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

| Claim | Status | Maturity | Comment |
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
| two-branch evolution equations are the minimal Spin(2,3)-compatible ansatz | structurally motivated ansatz | 4 | derivation from octonionic bulk action is open |
| Propositions 1–2: exact reduction to $(R,\rho,\Phi)$ with effective coupling $\kappa_{\mathrm{eff}} = \kappa_u\cosh(2\rho)$ | derived within two-branch model | 4 | clean exact result once equations are accepted |
| forced classification into four transport classes (Constructive, Inverted, Frustrated, Dephased) | derived from geometry of locking and persistence boundaries | 4 | classification is forced, not assumed |
| particle-like state criterion: locking + persistence conditions are jointly necessary and sufficient | derived consequence of classification | 4 | geometric, not empirical |
| derivation of two-branch evolution equations from variational principle on octonionic bulk | missing | 5 | would close the main gap in this section |
| connection between two-branch amplitude picture and Lindblad-Markov density-matrix picture | missing | 5 | how coarse-graining recovers the Lindblad picture is an open task |

---

## NS Programme structural corroboration

This section records corroboration of key dynamical claims from the NS/J3(O) regularity programme. All bridge identifications are structural proposals (maturity 5). The underlying NS results are at maturity 3–4. None of the items here substitute for independent derivation within the Spin(2,3) framework.

---

### T1/T2 split and the strain-only blow-up ray

**What the NS programme established (maturity 3):**

The NS programme identifies a 1D curve in the Q-R invariant plane — the strain-only ray Q = −3a²/4, R = −a³/4 — as the exact blow-up attractor of restricted Euler dynamics. On this ray: the cubic defect J̃ = det[ξ̂, ê₁, Ω̂ω] vanishes; vorticity aligns with a strain eigenvector; the discriminant Δ = 27R² + 4Q³ = 0 is maintained; and the flow has no transverse triadic coupling. This is an exact algebraic result. The complementary result is that physical NS solutions are regularised by transverse terms (vortex line curvature and twist) which prevent collapse onto the ray.

**What this addresses here (maturity 4):**

The central dynamical claim of this framework is that zero-mass interactions propagate only on T1, with T2 entering through off-diagonal mixing once mass is present (Principle D2). The question of why T1-pure propagation should be dynamically unstable — equivalently, why the hidden sector relaxation γ > 0 is forced rather than assumed — is an open problem.

**Proposed bridge identification (maturity 5):**

The strain-only ray corresponds to the T1-pure sector. More precisely: T1-pure propagation = no transverse coupling = strain-only ray (J̃ = 0); T2 mixing = transverse triadic coupling = off-strain-ray deviation (J̃ ≠ 0). NS regularity = T2 mixing prevents T1 collapse. Under this identification, the NS result that T1-pure blow-up is prevented by transverse (T2) terms translates into: the T1 channel is stable precisely because T2 mixing is present.

This belongs in discussion at maturity 5 as structural corroboration of the hidden-sector picture. It should not appear as a derivation.

**What this file still needs:**

An independent argument that T1-pure propagation is dynamically unstable in the Spin(2,3) setting, or that hidden sector relaxation γ > 0 is forced by the dynamics. This is the Spin(2,3) analogue of Gap A in the NS programme.

---

### Exponent gap 1/2 and the fermionic sector

**What the NS programme established (maturity 4):**

The NS programme derives a scaling contradiction under Type I blow-up. Near T*: N_lifted ~ C'/(T*−t)^{7/2} from β·b² scaling, while Type I + Jacobi gives N_lifted ≤ C/(T*−t)³. The gap is 7/2 − 3 = 1/2. This gap is robust to logarithmic corrections because the separation is 1/2, not approaching zero.

**What this addresses here:**

The exponent gap of 1/2 is a half-integer. In Spin(2,3), half-integer scaling dimensions correspond to fermionic representations. The spinor representation of Spin(2,3) = Sp(4) has dimension 4 and carries half-integer quantum numbers.

**Proposed bridge identification (maturity 5):**

The robustness of the exponent gap 1/2 reflects the rigidity of the fermionic sector in the Spin(2,3) representation theory. Integer exponent gaps can be corrected by bosonic renormalisation effects; half-integer gaps are protected by spin-statistics and cannot be perturbed by bosonic interactions. The exponent gap 1/2 in the NS programme may be robust for the same algebraic reason that the Dirac operator gap is robust in Spin(2,3): both are protected by the representation theory of the same group.

This is a structural observation, not a derived result. It does not prove the gap is exactly 1/2 in the rigorous PDE sense; it observes that if the gap is 1/2, its robustness has a representation-theoretic explanation.

**What this file still needs:**

A derivation within the Spin(2,3) setting that the relevant scaling exponents are forced to differ by exactly 1/2 by the representation theory of Spin(2,3).

---

### Diffusion law D ~ m²/γ and the NS exponent scaling

**What the NS programme established (maturity 4):**

Under Type I blow-up near T*: a(t) ~ 2/(T*−t) (strain rate); b_ij ~ ω_i · u_j ~ C/(T*−t)^{5/4} (vorticity correlation); ratio b/(a/2) ~ (T*−t)^{−1/4} → ∞ confirming b exceeds the filter threshold near blow-up. The Raychaudhuri Riccati equation gives C_eff = 0.022 ≪ 1/3 (maturity 4, N=32³, needs N=64³ confirmation), placing the NS flow well inside the stable regime.

**What this addresses here (maturity 4):**

The diffusion law D ~ m²/γ is derived here under reduction assumptions. The physical identification of m and γ from more fundamental data remains open.

**Proposed bridge identification (maturity 5):**

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
