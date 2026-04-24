# Spin(2,3) Compendium

## A Guide to Where This Framework Applies

---

## Purpose

This document is an entry point for the Spin(2,3) research program.

It does not replace the detailed framework and kernel files in `core/` and `kernels/`. It is meant to answer three questions before a reader enters those files:

1. What is Spin(2,3) and where does it come from?
2. Which domains of physics does this framework genuinely speak to?
3. Which domains does it not yet address — and why is naming those boundaries useful?

The adjacent background atlas covers the full arc of physics from atomic structure to holography, organized around the thread that symmetry breaking creates quantization, boundaries have enhanced symmetry, and coherence is the fundamental quantity. This compendium sits alongside that atlas and asks a different question: where, looking back across that same territory, does the Spin(2,3) lens produce genuine insight rather than force-fitting?

---

## §0 — What Spin(2,3) Is

### The group itself

`Spin(2,3)` is the spinor double cover of `SO(2,3)`. `SO(2,3)` is the isometry group of four-dimensional anti-de Sitter space `AdS₄` and of the three-dimensional de Sitter space `dS₃`. In Lorentzian signature, `SO(2,3)` preserves a bilinear form of signature `(2,3)`:

$$
\eta = \mathrm{diag}(-1,-1,+1,+1,+1).
$$

The double cover `Spin(2,3)` acts on a four-component spinor space. This is the object at the center of the program.

### Where it comes from

The framework does not take `Spin(2,3)` as a primitive axiom. It arrives by reduction:

$$
SO(2,4) \xrightarrow{[\text{fix spacelike normal } n = e_5]} SO(2,3) \xleftarrow{\text{lift}} \mathrm{Spin}(2,3)
\xrightarrow{[\text{fix } J^{01}]} T1 \oplus T2.
$$

The parent is `SO(2,4)`, the conformal group of four-dimensional Minkowski space. `SO(2,4)` is the natural symmetry group of massless physics in four dimensions. When a spacelike normal direction `n = e₅` is fixed, the stabilizer is `SO(2,3)`. This is not an invented move; it follows from the geometry of the ambient conformal arena.

The further reduction `J^{01}` splits the four-component spinor into two two-component sectors. Under the maximal compact subgroup `K = U(1) × SU(2)`:

$$
\mathbf{4} = (\mathbf{2}, -1/2) \oplus (\mathbf{2}, +1/2) = T1 \oplus T2.
$$

Each sector is an `SU(2)` doublet. The two sectors carry opposite `U(1)` charge.

At this level, the names `T1` and `T2` are labels after an orientation has been fixed. The invariant question is which reduced projector is induced by the upstream selection data. Since the framework already passes through the parent `SO(2,4)` conformal arena before reaching `SO(2,3)`, the final readout selector may belong to that ambient scale geometry rather than to `Spin(2,3)` alone.

- `T1` names the sector aligned with the selected forward readout/scale-flow orientation
- `T2` names the opposite sector; it is hidden but dynamically real and can participate in evolution without being directly accessed through the massless channel

So the open selection problem is not to prove that the bare label `T1` is special. It is to show that the parent `SO(2,4)`/ambient scale data, the selected octonionic direction, and the reduced `J^{01}` convention all induce the same observable projector.

### What the sectors mean

The central epistemic proposal of the framework (Level 4) is:

> the observable channel is determined by the selected axis of zero-mass traversal, not by a separate axiom of visibility

Pure `T1` propagation is massless. When `T1` and `T2` mix, the result is massive structure. The observer, who interacts through the `T1` channel, sees the full dynamics only through its projection onto `T1`.

---

## §1 — Domains Where Spin(2,3) Directly Applies

These are areas where the connection is mathematically clean and the framework has something specific to add beyond standard physics.

---

### 1a. Holography and AdS/CFT

This is the most direct connection in the program.

`SO(2,3)` is, by definition, the isometry group of `AdS₄`. This is not an interpretation or an analogy. It is the statement that Spin(2,3) is the symmetry group of the anti-de Sitter bulk geometry in four dimensions.

The AdS/CFT correspondence maps:
- bulk `AdS₄` ↔ boundary conformal field theory in `2+1` dimensions
- bulk fields propagating in the interior ↔ operators in the boundary theory
- boundary-to-bulk propagator ↔ the map from observables to interior dynamics

In the Spin(2,3) framework, the `T1/T2` split can be read against this picture once the readout orientation has been fixed:

- `T1` (observable sector, massless channel) corresponds to the boundary of `AdS₄`
- `T2` (hidden, dynamically real sector) corresponds to the bulk interior

The statement that "the observer sees only the T1 projection" becomes the statement that "physics is organized by the boundary theory, not the bulk." The hidden sector is real — it has dynamics — but it is not directly read out by the observable algebra.

| Claim | Role | Level |
|---|---|---|
| `SO(2,3)` is the isometry group of `AdS₄` | mathematical fact | 1 |
| the `T1/T2` split has a direct geometric reading as boundary/bulk | structural identification | 3–4 |
| the observer's T1 access corresponds to boundary-theory observables | physical interpretation | 5 |

The structural identification (Level 3–4) is clean. The physical interpretation — that this is the right reason our physics is T1-organized — carries more interpretive weight (Level 5).

---

### 1b. Spin and the Fifth Direction

Standard physics treats spin-½ as a formal consequence of the structure of `Spin(1,3)`: the covering group of the Lorentz group requires a `4π` rotation to return a spinor to its original state. This is mathematically necessary but physically opaque — why does a `2π` rotation return a vector but not a spinor?

In the Spin(2,3) framework, spin-½ acquires a geometric reading:

- the fifth direction `n = e₅` is the spacelike normal that was fixed in the reduction `SO(2,4) → SO(2,3)`
- a `2π` rotation in the observable `(2,3)` slice corresponds to a `4π` rotation in the full five-dimensional geometry
- the `4π` closure condition is a geometric fact about the normal vector, not an abstract postulate

This is a re-reading of what spin is, not a new prediction. It says that the half-integer structure of spinors is the signature of living on a slice of a five-dimensional geometry — specifically, the slice obtained by fixing `n`.

The same geometry gives gravity at classical scales. Coupling to the `n = e₅` direction is what it means for matter to gravitate. Spin is the quantum-scale signature of the same structure.

| Claim | Role | Level |
|---|---|---|
| spin-½ as geometric rotation through `n` | re-reading, not new prediction | 3–4 |
| `4π` closure as fact about the normal vector | geometric statement | 3–4 |
| gravity and spin as two faces of coupling to `n` | interpretive synthesis | 5 |

---

### 1b-ii. KK-Style Spin Quantization via Spin(2,3) Representations

The isomorphism $\mathrm{Spin}(2,3) \cong \mathrm{Sp}(4,\mathbb{R})$ means the transport slice carries a symplectic structure. The two conjugate branch amplitudes $(A, B) \in \mathbb{C}_u$ of an octonionic process package as a real 4-vector $X \in \mathbb{R}^4$, and a natural coherence scalar is $\mathcal{I}=AB$ (whose exchange-odd component $\mathcal M_{\mathrm{ex}}=-\mathrm{Im}_u(AB)$ is the symplectic pairing underlying the exchange generator).

This gives a KK-like mechanism for particle classification that is representation-theoretic rather than geometric:

- In standard Kaluza-Klein theory, compactifying a geometric dimension yields momentum quantization from periodic boundary conditions
- Here the "extra direction" is the mixing axis — an internal direction, not a geometric extra dimension
- Quantization occurs through the **representation content of $\mathrm{Spin}(2,3)$**
- Allowed states = irreducible representations of $\mathrm{Spin}(2,3) \cong \mathrm{Sp}(4,\mathbb{R})$
- Observable particles = projections of these irreps onto the transport (T1) slice

Under phase locking, the coherence scalar $\mathcal{I}(s+T) = e^{u\Theta}\mathcal{I}(s)$ gives integer spin for $\Theta = 2\pi$ and half-integer spin for $\Theta = \pi$. Spin is the winding number of the conjugate branch pair around the transport axis.

The metaplectic representations of $\mathrm{Sp}(4,\mathbb{R})$ are natural homes for the two-branch amplitude structure — they are built from pairs. This suggests the framework may be most naturally expressed as a metaplectic quantization of null transport, with the octonionic bulk providing the non-associative deformation of the symplectic structure (see `archive/overflow.md`).

| Claim | Role | Level |
|---|---|---|
| $\mathcal{I}=AB$ carries the locked phase and $\mathcal M_{\mathrm{ex}}=-\mathrm{Im}_u(AB)$ is the exchange-odd symplectic pairing | structural identification | 3–4 |
| particle species as irreps of Spin(2,3) | KK-style proposal | 4–5 |
| spin as winding number of conjugate branch pair | structural reading | 5 |
| metaplectic representations as natural host for two-branch structure | direction | 5 |

---

### 1c. Color from Octonionic Geometry

The octonion algebra `O` has automorphism group `G₂`. `G₂` acts on the imaginary octonions, a seven-dimensional space. Choosing a preferred imaginary direction `e₇` (equivalently `u`, the zero-mass traversal direction) fixes a stabilizer inside `G₂`. That stabilizer is `SU(3)`.

This is standard mathematics (Level 3). The physical claim is that this `SU(3)` is color.

Under the `G₂ → SU(3)` reduction, the imaginary octonions split as:
$$
\mathrm{Im}(O) = \mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1},
$$
where the singlet corresponds to the fixed direction `e₇`. The `3` and `3̄` are the color triplet and antitriplet.

The `G₂` Dynkin diagram has a distinctive structure: long roots and short roots with ratio `√3`. In the framework's reading:

- long roots correspond to `SU(3)` (color, `T1`, massless/EM sector)
- short roots correspond to the `3 ⊕ 3̄` structure (`T2`, gravity, off-axis mixing)
- the `√3` root-length ratio is a geometric proxy for the coupling ratio between the EM and gravity sectors at the `G₂` breaking scale

The connection between the octonionic direction and the zero-mass traversal channel is the pivot that makes this more than a coincidental matching. The framework requires that the internal selection (choose `e₇`) and the kinematic selection (identify the massless channel as `T1`) refer to the same direction (Level 4).

| Claim | Role | Level |
|---|---|---|
| choosing `e₇` inside `G₂` gives stabilizer `SU(3)` | mathematical fact | 3 |
| this `SU(3)` is physical color | physical identification | 4–5 |
| the octonionic direction aligns with the zero-mass traversal direction | central framework proposal | 4 |
| `G₂` root-length ratio `√3` reflects EM/gravity coupling ratio | structural interpretation | 5 |

---

### 1d. Division Algebras as the Algebraic Substrate

The background atlas includes a supplementary section (Supplementary J) on the four normed division algebras `ℝ, ℂ, ℍ, O`. The existence of exactly four normed division algebras is a theorem (Hurwitz, 1898). The octonions are the largest and the only one that is non-associative. Their automorphism group is `G₂`.

The Spin(2,3) program is specifically the physics of the octonionic layer of this structure. The earlier layers appear as:

- `ℝ`: the scalar sector — mass terms and real mixing parameters
- `ℂ`: phase structure — electromagnetism, `U(1)` gauge theory
- `ℍ` (quaternions): the weak sector candidate — `SU(2)` structure fits naturally here
- `O` (octonions): color structure via `G₂ → SU(3)`, plus the gravity sector through `e₅`

The Jordan algebra `J₃(O ⊗ ℂ)` is the full ambient algebraic object. The `ℂ` factor is not decorative: it encodes the off-plane mixing that is the gravity sector. `J₃(O)` alone is only the real/`T1` projection. The imaginary part of the cubic determinant in `J₃(O ⊗ ℂ)` is the gravity coupling.

The octonionic remainder after fixing the time direction:
$$
u^\perp \cong \mathbf{C}^3
$$
is a six-dimensional space that carries color structure, hidden wandering geometry, and the candidate for generation structure. This is the current strongest convergence point in the parent inquiry (see `core/parent-inquiry-map.md`).

| Claim | Role | Level |
|---|---|---|
| program is built on the octonionic layer of the division algebra tower | framework choice | 2 |
| `J₃(O ⊗ ℂ)` is the full ambient object (not `J₃(O)`) | framework correction | 4 |
| `ℂ` factor encodes the gravity/off-plane mixing | interpretive identification | 4–5 |
| `u⊥ ≅ ℂ³` as parent of color, generation structure, hidden geometry | working convergence point | 4–5 |

---

## §2 — What the Framework Derives Internally

These are claims that follow from the framework's own structure, under stated assumptions. They are not force-fitted mappings onto external physics — they are consequences of taking the framework seriously.

---

### Mass as Sector Mixing

In standard quantum field theory, mass is a parameter in the Lagrangian. It appears either as a bare mass term or through the Higgs mechanism as a coupling to the Higgs field. In either case it is introduced rather than derived from spacetime geometry.

In the Spin(2,3) framework, mass has a different origin:

> `m` is the parameter governing the degree of mixing between `T1` and `T2`.

Pure `T1` propagation is massless. When the state develops a component in `T2`, the effective evolution in `T1` gains a mass-like term. The reduced Markovian dynamics gives:

$$
D \sim \frac{m^2}{\gamma}
$$

where `m` is the mixing strength and `γ` is the sector-transition damping rate. This is derived under weak-coupling and Markovian assumptions (Level 4 for the reduced model).

The diffusion law `D ~ m²/γ` is the visible transport signature of hidden-sector coupling. Massless particles have `m = 0` and do not diffuse.

The connection to standard mass — a field-theoretic identification, a clean dispersion relation — is still one layer above the current proof burden (Level 5 for the full identification).

| Claim | Role | Level |
|---|---|---|
| `m` governs departure from pure `T1` transport | derived in reduced model | 4 |
| `D ~ m²/γ` scaling law | derived under weak-coupling and Markov | 4 |
| physical mass is encoded by `T1/T2` mixing | central interpretation | 5 |

---

### Uncertainty as Projection Broadening

The epistemic reading of uncertainty in this framework is:

> observable uncertainty arises because the observer tracks `T1` but not `T2`; what appears as measurement broadening is unresolved hidden-sector excursion

This is a safer claim than saying "quantum uncertainty is nothing but hidden-sector epistemics." The safe version says that projected, coarse-grained observables inherit effective broadening because the observer does not resolve the full dynamics (Level 4–5). The broader claim — that all quantum measurement theory reduces to this — is not established by the current framework (Level 6, not claimed).

---

### Generation Structure

`J₃(O)` has three off-diagonal octonionic slots. This gives a natural three-place static arena for matter content. The three slots are structurally distinguished and can be connected by triality automorphisms.

The safe claim is that `J₃(O)` is a strong candidate organizer for three families (Level 3–4). The stronger claims — that exactly three generations are forced, that a fourth generation is genuinely excluded — require a proof burden that the current framework has not yet met (Level 5–6 for the exclusion).

The current strongest generation hypothesis sits one level above `J₃(O)`: the `2/4/6` access ladder inside the six-dimensional remainder `u⊥ ≅ ℂ³`. At higher energy, more of the hidden octonionic space becomes dynamically accessible, and each additional `2`-dimensional access level corresponds to a heavier generation. Three access levels cap naturally because `ℂ³` is six-dimensional.

The open step is making this access ladder dynamically forced rather than merely kinematically available (Level 5 for the hypothesis; Level 6 for a full proof).

---

### Forced Classification of Transport States

The two-branch amplitude framework, operating at the level of conjugate bracket completions of octonionic products, derives a forced partition of the phase space $(\rho, \Phi)$ into four disjoint transport classes (Constructive, Inverted, Frustrated, Dephased) purely from the geometry of two boundaries: the locking boundary and the persistence boundary. The classification is not assumed — it is forced by the dynamics once the signed transport coupling $\kappa_u$ and the loss rate $\gamma$ are given. Particle-like states must satisfy both the locking condition $|\omega| \leq |\kappa_u|\cosh(2\rho)$ and the persistence condition $\kappa_u\cosh(2\rho)\cos\Phi > \gamma$. See `kernels/dynamics.md` for the full derivation.

| Claim | Role | Level |
|---|---|---|
| forced partition into four transport classes from geometry of two boundaries | derived within two-branch model | 4 |
| particle-like state criterion: both locking and persistence conditions | derived consequence | 4 |
| connection between two-branch picture and Lindblad-Markov reduction | missing derivation | 5 |

---

### Chirality

The framework offers a route to chirality through sector asymmetry: if left- and right-handed modes couple to `T2` differently, chirality is a derived consequence of the geometry rather than an independent input. This is conceptually attractive but is not yet a proved result — the asymmetry must be shown to be forced by the `Spin(2,3)` structure (Level 5).

---

## §3 — Where the Framework Might Eventually Speak

These claims are motivated by the framework's structure but currently exceed its proof burden. They are marked as speculative and should be treated as directions rather than results.

---

### Topological Matter and the Tenfold Way

The tenfold way (Altland-Zirnbauer classification) classifies free-fermion topological phases by the behavior of the single-particle Hamiltonian under three discrete symmetries:
- `T`: time reversal (anti-unitary, `T² = ε_T = ±1` or absent)
- `C`: charge conjugation / particle-hole (anti-unitary, `C² = ε_C = ±1` or absent)
- `S = TC`: sublattice / chiral symmetry (unitary, `S² = +1`, anticommutes with `H`)

The 10 classes fill a 2×2×(present/absent) table. Their topological invariants in dimension `d` are either `0`, `ℤ₂`, or `ℤ`, and they repeat with Bott periodicity in `d`.

---

#### The Clifford algebra identification

The first concrete result is an algebra isomorphism:

$$
\mathrm{Cl}(2,3) \cong M_4(\mathbf{C}).
$$

This follows from the iterative isomorphism `Cl(p+1,q+1) ≅ Cl(p,q) ⊗ M₂(ℝ)`:
$$
\mathrm{Cl}(0,1) = \mathbf{C}
\;\Rightarrow\;
\mathrm{Cl}(1,2) = M_2(\mathbf{C})
\;\Rightarrow\;
\mathrm{Cl}(2,3) = M_4(\mathbf{C}).
$$

`M₄(ℂ)` is a complex algebra (not a real one). This is significant: the 10 tenfold-way classes split into 2 complex classes (A and AIII) and 8 real classes (AI, BDI, D, DIII, AII, CII, C, CI). Only the complex Clifford algebras `Cl(n) ≅ M_{2^{n/2}}(ℂ)` host the complex classes.

The consequence: **Spin(2,3) spinor representations live in the complex sector of the tenfold-way classification.** When looking for a symmetry class, the search space is already narrowed to A and AIII. (Level 3 — mathematical fact)

---

#### J^{01} as the chiral operator

The `J^{01}` generator splits the four-component spinor as:

$$
J^{01} = -\tfrac{1}{2}\,\mathrm{diag}(+1,+1,-1,-1).
$$

Define the rescaled grading operator:
$$
\Sigma = 2J^{01} = \mathrm{diag}(+1,+1,-1,-1), \qquad \Sigma^2 = +1.
$$

`Σ` is unitary. Now ask what it does to a Hamiltonian that mixes the two sectors.

Any Hamiltonian `H` on the full spinor space can be decomposed:
$$
H = H_{\mathrm{diag}} + H_{\mathrm{mix}},
$$
where `H_diag` preserves T1 and T2 separately, and `H_mix` couples them.

- `Σ` commutes with `H_diag` (both T1 and T2 blocks are eigenspaces of `Σ`)
- `Σ` **anticommutes** with `H_mix` (mixing flips the sector eigenvalue)

This is precisely the condition for a **chiral symmetry**: `{Σ, H_mix} = 0`.

Therefore:
- In the **massless limit** (`m = 0`, `H_mix = 0`): `Σ` is an exact symmetry of `H`. The theory is in **class AIII** — the chiral unitary class. (Level 3–4)
- In the **massive case** (`m ≠ 0`, `H_mix ≠ 0`): `Σ` is broken. The theory is in **class A** — no symmetry. (Level 3–4)

The statement "mass breaks chiral symmetry" is not a new claim. It is the standard physics of class AIII. What is new here is identifying `Σ = 2J^{01}` as that chiral operator — i.e., it is a generator of `Spin(2,3)` itself, not an additional structure imported from outside.

---

#### The mass transition is a topological phase transition

Class AIII in various dimensions has topological invariants:

| Dimension `d` | Invariant |
|---|---|
| 0 | `ℤ` |
| 1 | `ℤ` (winding number) |
| 2 | `0` |
| 3 | `ℤ` (3D winding number, Weyl-like) |

In `d = 3`, class AIII has topological invariant `ℤ`. The prototypical physical realization is the **Weyl semimetal**: gapless band-touching points (Weyl nodes) that are topologically protected by chirality and come in pairs of opposite chiral charge. They cannot be gapped out without either breaking the chiral symmetry or annihilating a node with its opposite-chirality partner.

In the Spin(2,3) framework:
- T1 sector states at `m = 0` are protected from acquiring mass by exactly this mechanism: `Σ` symmetry forbids a gap
- Turning on `m` (T1/T2 coupling) **breaks** `Σ` and opens a gap — the mass is the topological gap parameter
- The transition `m = 0 → m ≠ 0` is the same type of event as moving from a topologically non-trivial phase (class AIII) to a trivial one (class A) through a gap-closing transition (Level 4)

The Spin(2,3) mass generation mechanism — `T1/T2` mixing — is structurally identical to the mechanism that destroys topological protection in class AIII: it is the symmetry-breaking coupling that opens the gap. Mass is not put in by hand; it is the order parameter of a chiral symmetry-breaking transition.

---

#### Natural discrete symmetries and the full class structure

The explicit gamma matrices (from `kernels/statics.md`) have definite reality properties:
$$
(\gamma^\mu)^* = \begin{cases}
+\gamma^\mu & \mu = 0, 2, 4 \quad (\text{real gammas}) \\
-\gamma^\mu & \mu = 1, 3 \quad (\text{imaginary gammas})
\end{cases}
$$

From this, two natural discrete anti-unitary operators can be extracted:

**Time reversal** `T = (\gamma^2\gamma^4) K`:
$$
T\,\gamma^\mu\, T^{-1} = -\gamma^\mu \text{ for } \mu=0,1 \quad (+\gamma^\mu \text{ for } \mu=2,3,4).
$$
This reverses both timelike directions and preserves all spacelike directions. Computing `T²` from `M_T = \gamma^2\gamma^4 = -i(1_2 \otimes \sigma_2)`:
$$
T^2 = M_T M_T^* = (-i(1_2 \otimes \sigma_2))\bigl(-i(1_2 \otimes \sigma_2)\bigr) = -1 \cdot (1_2 \otimes \sigma_2^2) ... \to T^2 = +1.
$$

**Charge conjugation** `C = (\gamma^1\gamma^3) K`:

`C` uses the imaginary gammas; it anticommutes with `γ¹` and `γ³`, and commutes with `γ⁰, γ², γ⁴`. Computing `C²` from `M_C = \gamma^1\gamma^3 = \sigma_2 \otimes \sigma_2`:
$$
C^2 = M_C M_C^* = (\sigma_2 \otimes \sigma_2)(\sigma_2^* \otimes \sigma_2^*) = (\sigma_2)(-\sigma_2) \otimes (\sigma_2)(-\sigma_2) = (-\sigma_2^2)\otimes(-\sigma_2^2) = (-(-1))^2 = +1.
$$

So: `T² = +1`, `C² = +1`.

In the Altland-Zirnbauer table, `T² = +1` and `C² = +1` with chiral symmetry `S` present corresponds to **class BDI** (the real class with ℤ topological invariant in `d = 1`). This is the class of the SSH chain and its higher-dimensional analogues.

However, the chiral operator `S = M_C M_T^*` computed from these `T` and `C` satisfies `S² = -1` rather than the expected `+1`. This discrepancy signals that the natural `T` and `C` operations in the Spin(2,3) representation do not map directly to the standard condensed-matter conventions without a phase redefinition. The resolution is likely a sign choice in the definition of `C` or `T`, or the presence of the second timelike direction modifying the canonical identification. This is an open point — the symmetry class identification is narrowed to {A, AIII, BDI} but not yet pinned precisely. (Level 4 for the constraint, Level 5 for the exact class assignment)

---

#### Two time-like directions: partial time reversals

A qualitative feature with no Spin(1,3) analogue: Spin(2,3) has **two** time-like directions (0 and 1). This means there are three distinct time-reversal-type operations:
- `T_{01}`: reverse both time directions (the full `T` computed above, `T² = +1`)
- `T_0`: reverse direction 0 only
- `T_1`: reverse direction 1 only

`T_0` and `T_1` individually are not generally symmetries of an arbitrary Spin(2,3) Hamiltonian — they do not generate a symmetry of the full theory unless the theory has additional structure. However, the **J^{01} grading** `Σ` is the commutator of these two partial operations (up to phase), which is why `Σ` appears even when neither partial time reversal is separately a symmetry.

[*Level 5: plausible but future work*: if a physical system is described by a Spin(2,3)-symmetric Hamiltonian in which `T_0` and `T_1` are separately preserved (for example, by a lattice regularization that distinguishes the two time directions), then the system simultaneously carries two independent time-reversal symmetries with `T_0² = ε₀` and `T_1² = ε₁`. Having two commuting time-reversal symmetries is outside the standard 10-fold classification, which assumes at most one `T`. Such a system might realize a class that requires a **16-fold way** or extended classification table. Whether physical lattice systems with approximate Spin(2,3) symmetry exist that would exhibit this is not known.]

---

#### Summary: what the tenfold-way analysis gives

| Result | Role | Level |
|---|---|---|
| `Cl(2,3) ≅ M₄(ℂ)` — complex Clifford algebra | mathematical fact | 3 |
| Spin(2,3) representations live in the complex tenfold-way classes (A or AIII) before anti-unitary refinement | direct consequence | 3 |
| `Σ = 2J^{01}` is the chiral grading operator; at the chiral-only level this is the AIII structure | structural identification | 3–4 |
| `T_0^2 = -1`, `C^2 = +1`, and `Σ = C T_0` in the explicit Cl(2,3) representation | computed / structural identification | 4 |
| Full massless class assignment: DIII | structurally pinned by `(T_0^2=-1, C^2=+1, Σ=CT_0)` | 4 |
| Massive limit (`m≠0`) breaks `Σ` and lands in class D | derived consequence | 4 |
| DIII `d=3` winding computation for the natural gapped extension gives `|W_3| = 1` | computed | 4 |
| Mass generation = chiral-symmetry-breaking topological transition | structural identification | 4 |
| A second time reversal `T_{01}` with `T_{01}^2 = -1` gives an extended two-`T` structure beyond the standard tenfold assumption | structural observation / open algebraic question | 4–5 |
| Specific material realizations with Spin(2,3) symmetry | open | 6 |

The cleanest conclusion at present: the T1/T2 splitting in Spin(2,3) gives the chiral grading `Σ = 2J^{01}`. At the refined anti-unitary level, the massless sector is DIII and the massive sector is D. The older AIII/A reading is still the correct chiral-only shadow, but it is no longer the sharpest statement.

The full domain analysis — including the `T_0`, `T_{01}`, and `C` computation, the resolved `S^2 = -1` issue, the DIII winding computation, the Weyl semimetal correspondence, and the remaining open obligations — lives in `kernels/topological.md`.

---

### Hydrogen Threshold Symmetry and the Efimov Bridge

[*Level 5: plausible but future work*: the two-boundary transport picture has the same compact/noncompact/threshold symmetry pattern as the hydrogen problem. In standard hydrogen, bound states carry hidden `SO(4)`, scattering states carry `SO(3,1)`, and the ionization threshold is the contraction point `ISO(3)` between them. In the present framework, the constructive locked/persistent sector is the natural analogue of the compact bound domain, the dephased side is the natural analogue of the noncompact free domain, and the persistence boundary `\kappa_u\cosh(2\rho)\cos\Phi = \gamma` is the marginal surface separating them. The safe claim is a structural correspondence of symmetry pattern, not a derivation of the hydrogen spectrum or of the exact Laplace-Runge-Lenz algebra inside the transport model.]

[*Level 5-6: plausible direction with a significant proof issue*: on the free/dephased side, the subgroup chain `SO(3,1) \supset SO(2,1)` suggests a route to Efimov-type conformal dynamics for three-body states near the locking/persistence boundary. Near threshold, the reduced law `\dot{R} = R(-\gamma + \kappa_u\cosh(2\rho)\cos\Phi)` linearizes to `\dot{R} \approx \epsilon R`, which is scale-covariant in the radial variable and therefore a plausible entry point for conformal quantum mechanics. The stronger claim would be that three simultaneous near-boundary transport states realize an Efimov tower, with the geometric ratio fixed by an `SO(2,1)` Casimir and therefore by a threshold combination such as `\omega/\kappa_u`. That quantitative step has not been derived.]

---

### Dark Matter

[*Level 5: plausible but future work*: T2-sector matter — matter that couples primarily to `T2` rather than `T1` — would not project onto the T1 observable algebra. It would have gravitational coupling (gravity lives in the T2/fifth-direction sector) but no electromagnetic or strong-force coupling. This is exactly the phenomenological signature of dark matter. The identification is structurally motivated by the framework; it does not yet amount to a model, a mass spectrum, or a prediction.]

---

### Three-Generation Forcing

[*Level 5: plausible but future work*: if the `2/4/6` access ladder inside `u⊥ ≅ ℂ³` can be made dynamical — if higher energy physically opens additional dimensions of the hidden remainder rather than merely making them available — then the generation count of three would follow from the dimensionality of the octonionic complement. The open step is a forcing argument: why exactly 2, then 4, then 6, and not some other sequence? The kinematic picture is suggestive; the dynamics has not been derived.]

---

## §4 — Where the Framework Currently Has Little or Nothing to Say

Naming the boundaries of a framework is as important as naming its content. The following domains from the broad physics atlas are mostly not addressed by the Spin(2,3) program at present, except where a narrow structural bridge has been noted. No broad claim is being forced onto them.

| Domain | Coverage |
|---|---|
| Atomic energy levels (He, H, Rydberg) | quantitative spectra not addressed; hydrogen hidden-symmetry pattern now has a speculative threshold-symmetry bridge |
| Electric dipole selection rules | not addressed |
| Nuclear structure beyond isospin embedding | not addressed |
| Chemical bonding and molecular physics | not addressed |
| Condensed matter: phonons, band structure, superconductivity | not addressed |
| Topological insulators and Weyl semimetals | structural connection established (class AIII); see `kernels/topological.md` |
| Photochemistry, biology, chemistry bridge | not addressed |
| Renormalization group and fixed points | not addressed in the current framework |
| Goldstone bosons in specific models | not addressed |

This is not a failure. A framework that claims to address everything addresses nothing precisely. The Spin(2,3) program has a specific domain: the geometry of the observable/hidden sector split, color structure from octonionic reduction, and the holographic boundary organization of physics. Everything else is future work or not this program's problem.

---

## §5 — Looking Back at the Atlas Thread

The background atlas is organized around four claims:

1. Symmetry breaking creates quantization.
2. Boundaries between phases have enhanced symmetry.
3. All dynamics are bosonic.
4. Coherence is the fundamental quantity.

Through the Spin(2,3) lens, the second claim shifts most sharply.

**Boundaries have enhanced symmetry** is no longer a pattern to be explained case by case. The `T1` observable sector *is* the boundary of `AdS₄`, and it carries the full `SO(2,3)` symmetry because that is the boundary symmetry of the anti-de Sitter bulk. The pattern that interfaces and edges carry more symmetry than the bulk phases they separate becomes, in this framework, a consequence of the geometry — not an empirical observation that needs separate explanation in each material system.

The other three claims sit outside the current proof reach of the framework. The relationship between symmetry breaking and quantization in the `T1/T2` context, the bosonicity of `T1` dynamics, and the role of coherence in the hidden-sector projection story are all directions the program can potentially develop. They are not yet part of what the framework has established.

---

## §6 — Summary Claim Ledger

| Claim | Domain | Role | Level |
|---|---|---|---|
| `SO(2,3)` is the isometry group of `AdS₄` | holography | mathematical fact | 1 |
| `T1/T2` split as boundary/bulk duality | holography | structural identification | 3–4 |
| spin-½ as rotation through the fifth direction `n` | spin | re-reading | 3–4 |
| G₂ stabilizer of `e₇` is `SU(3)` | octonionic geometry | mathematical fact | 3 |
| this `SU(3)` is physical color | color | physical identification | 4–5 |
| octonionic direction aligns with zero-mass channel | framework proposal | central choice | 4 |
| hydrogen bound/free split has a structural analogue in the transport classification | atomic / threshold symmetry | speculative structural correspondence | 5 |
| Efimov scaling may be governed by a threshold `SO(2,1)` Casimir in the dephased sector | few-body / conformal dynamics | open conjecture | 6 |
| `J₃(O ⊗ ℂ)` as full ambient algebra, `ℂ` encodes gravity | algebra | framework identification | 4–5 |
| `u⊥ ≅ ℂ³` as parent of color, hidden planes, generation structure | parent geometry | working convergence | 4–5 |
| `m` governs departure from pure `T1` transport | dynamics | derived in reduced model | 4 |
| `D ~ m²/γ` scaling law | dynamics | derived (weak-coupling, Markov) | 4 |
| physical mass encoded by `T1/T2` mixing | interpretation | central interpretation | 5 |
| uncertainty as projection broadening | epistemics | interpretation | 4–5 |
| `J₃(O)` as three-slot generation organizer | statics | structural observation | 3–4 |
| three-generation count forced by geometry | statics | open proof burden | 5–6 |
| chirality from sector asymmetry | interpretation | interpretive route | 5 |
| topological matter from Spin(2,3) Clifford structure | speculation | speculative | 5 |
| dark matter as T2-sector matter | speculation | speculative | 5 |
| three-generation forcing via `2/4/6` ladder | speculation | speculative | 5 |
| $\mathcal{I}=AB$ and $\mathcal M_{\mathrm{ex}}=-\mathrm{Im}_u(AB)$ as the branch quadratic structure; forced classification into four transport classes | structural identification | 3–4 |
| particle species as Spin(2,3) irreps; spin as branch winding number | KK-style representation proposal | 4–5 |
| $G_2 \cap \mathrm{Spin}(2,3)$ calculation: symmetry group seeing both octonionic structure and transport projection | open calculation | 5–6 |

---

## For Further Reading

- `core/master-framework.md` - taxonomy of all claims and their logical status
- `kernels/statics.md` - detailed static representation structure
- `kernels/dynamics.md` - reduced dynamics and scaling laws
- `kernels/epistemics.md` - observability, projection, hidden-sector meaning
- `kernels/interpretation.md` - mass, uncertainty, chirality as interpretive readings
- `kernels/open-problems.md` - what the framework still owes
- `core/parent-inquiry-map.md` - ranked plausibility of current directions
- `research/faddeev-efimov/` - conjectural Efimov/Faddeev bridge track

## Appendix: Efimov Bridge Status

The threshold linearization near persistence/locking boundaries suggests an SO(2,1)-type conformal structure. Efimov physics supplies a concrete three-body system in which an SO(2,1)-controlled inverse-square problem produces discrete scaling.

The safe claim is therefore structural:

- the Spin(2,3) transport framework has a plausible threshold scaling sector;
- the Efimov/Faddeev derivation is a useful quantitative comparison target;
- the proposed Casimir/Faddeev identification remains an open conjecture until the Spin-derived operator, channel embedding, normalization, and `s_0` calculation are explicit.

The live bridge work has been moved to `research/faddeev-efimov/`. It should not be read as established framework content unless the gates in `research/faddeev-efimov/proof-obligations.md` are completed or explicitly marked as partially complete with stated limits.
