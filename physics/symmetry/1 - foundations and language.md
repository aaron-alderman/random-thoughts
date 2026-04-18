# Foundations and Language

This note gathers the shared language used across the atlas: the formal machinery, the recurring mathematical structures, and the conceptual patterns that let different regions of physics talk to each other. It is the best starting point when the question is less about a particular system and more about how physics organizes description itself.

## Core Topics

### Symmetry, Noether, and Quantum Numbers

The atlas treats quantum numbers as labels of irreducible representations rather than as arbitrary tags. Energy, momentum, angular momentum, charge, statistics, chirality, and similar quantities are the conserved traces of symmetry, so this section is the shared key for reading spectra, phases, and selection rules everywhere else in the project.

Every continuous symmetry of a system gives a conserved quantity. That simple Noether logic is the first compression rule of the atlas: if the symmetry is known, a large part of the structure is known before detailed calculation begins.

| Symmetry | Conserved quantity | Typical labels |
|---|---|---|
| Time translation | Energy | `E` |
| Space translation | Momentum | `p`, `k` |
| Rotation | Angular momentum | `J`, `L`, `S`, `m` |
| Electromagnetic gauge | Charge | `Q` |
| Permutation | Statistics | boson / fermion |
| Chiral flavor symmetry | Chirality / flavor | left-right multiplets |

The important shift in viewpoint is this: `n`, `l`, `m`, spin labels, crystal momentum, point-group species, and band labels are not merely names attached after the fact. They are the representation content of the state.

### Group Theory as the Mathematics of Symmetry

This is the structural backbone: groups encode invariance, representations tell us how states transform, and irreducible representations provide the indivisible building blocks. The practical payoff is that degeneracies, allowed mixings, and symmetry-protected splittings can all be read from representation theory before solving much detailed dynamics.

A symmetry group `G` is the set of transformations that leave the Hamiltonian invariant. A representation tells us how those transformations act on states, and an irreducible representation is the smallest block that cannot be decomposed further.

Two practical facts do most of the work:

- If an operator commutes with the full symmetry action, it is block-diagonal in irreducible sectors.
- If a perturbation lowers the symmetry from `G` to a subgroup `H`, a multiplet of `G` decomposes into irreducible pieces of `H`.

That second fact is the engine behind Zeeman splitting, crystal-field splitting, molecular bonding symmetries, lattice band sticking, and many phase-transition orderings.

A compact atlas table of the most-used groups belongs here rather than only in the lookup note:

| Group | Dimension or order | Typical physical role | Common labels |
|---|---|---|---|
| `U(1)` | 1 | phase or electromagnetic gauge symmetry | integer charge |
| `SU(2)` | 3 | spin, isospin, weak symmetry | half-integer `j` |
| `SO(3)` | 3 | spatial rotation | integer `l` |
| `SU(3)` | 8 | color and some flavor organization | `(p,q)`-type labels |
| `SO(4)` | 6 | hidden hydrogen symmetry | `n,l` organization |
| `SO(3,1)` | 6 | Lorentz symmetry | spinor and tensor reps |
| `SO(4,2)` | 15 | conformal symmetry in `3+1` dimensions | dimension `Delta`, spin |
| `SO(2,1)` | 3 | Efimov / `0+1` conformal structure | continuous scaling data |
| `S_2` or `Z_2` | 2 | exchange, parity, inversion | symmetric / antisymmetric sectors |
| point groups such as `O_h`, `T_d`, `D_(6h)` | finite | molecules and crystals | symmetry species such as `A`, `E`, `T` |

The practical message is that every domain note is really using the same template: pick the right symmetry group, identify its irreducible representations, then ask what survives when the environment or dynamics reduces that symmetry.

These point-group examples are especially useful because they show that group theory is not only for abstract field theory:

- `C_(2v)` organizes water-like molecules and CuO`_2` planes
- `D_(inf h)` organizes linear molecules and infrared/Raman activity
- `O_h` organizes octahedral crystal fields and `e_g / t_(2g)` orbital splitting

That last example is particularly important for the atlas because it shows how a purely geometric reduction

```text
D^2(SO(3)) -> E_g (+) T_(2g)
```

already determines the orbital language used later in perovskites, cuprates, and iridates.

### The Wigner-Eckart Theorem and Selection Structure

The Wigner-Eckart theorem is the atlas's main compression tool. It separates geometry from dynamics, turning many matrix-element questions into one reduced matrix element times known group-theoretic factors. In practice, this is what makes transition rules, multipole couplings, and response channels legible instead of ad hoc.

In angular-momentum language the theorem has the form

```text
<a' j' m' | T^(k)_q | a j m>
= geometric factor x reduced matrix element
```

The geometric factor carries the selection rules. The reduced matrix element carries the system-specific physics. That is why one dipole calculation can generate an entire family of transition amplitudes once the symmetry is fixed.

This is the practical reason selection rules are structural rather than mnemonic. Dipole, quadrupole, magnetic, phonon-coupling, and pairing channels all become readable as tensor-operator questions.

The group-theoretic condition can be stated in a particularly clean form:

```text
<psi_f | T^(k) | psi_i> != 0    only if    Gamma_f (x) Gamma_T contains Gamma_i
```

For dipole transitions the tensor has rank 1, so the familiar rules follow from representation theory rather than from memorized exceptions:

- `Delta l = +/- 1` from the tensor product and parity
- `Delta m = 0, +/- 1` from the spherical-tensor component `q`
- `Delta J = 0, +/- 1` but not `0 -> 0`
- `Delta S = 0` for ordinary electric dipole processes because the operator acts on spatial coordinates

This is part of why the theorem matters so much across the atlas. The same logic classifies optical transitions, phonon activity, crystal-field couplings, and many order-parameter channels.

### Quantization From Boundary Conditions

One of the document's strongest themes is that quantization is usually generated by constraint. Normalizability, periodicity, single-valuedness, lattice translation symmetry, and short-distance boundary data turn continuous equations into discrete spectra, mode sets, or band labels.

The Schrodinger equation is continuous. Discreteness usually enters because not every formal solution is allowed. The admissibility conditions do the quantizing.

| System | Constraint | Quantized object |
|---|---|---|
| Particle in a box | Vanishing at walls | allowed `k` values |
| Hydrogen | Normalizability at infinity | principal level `n` |
| Rotor | Single-valuedness under `2pi` rotation | angular labels |
| Crystal electron | Periodic lattice symmetry | Bloch bands |
| Molecular vibration | Hessian eigenproblem | normal modes |
| Efimov problem | Short-distance boundary data | geometric tower |

This viewpoint is one of the strongest unifying ideas in the manuscript. Quantization is not an extra mystical ingredient added after solving the problem. It is what remains once symmetry and boundary conditions have ruled out the rest.

### Topology as Robust Quantization

Topology is treated here as the most durable source of discrete structure because its invariants survive smooth deformation. Chern numbers, winding numbers, and related classification data can only change when a gap closes, which is why topological phases are more stable than patterns protected by energetics alone.

Where symmetry can be reduced gradually, topological invariants resist change until something singular happens. This is why topology is the strongest form of quantization in the atlas. The integer is not a detail of a specific Hamiltonian fit. It is a global property of the whole structure.

The manuscript's condensed-matter examples focus on Chern numbers and the tenfold way, but the broader lesson is wider: topology is what survives when local detail no longer matters.

A more geometric layer also belongs in foundations. Homotopy groups classify the stable defects or global structures allowed by an order-parameter manifold:

| Topological data | Typical defect or object | Example |
|---|---|---|
| `pi_0(M)` | domain wall | Ising-like sign domains |
| `pi_1(M)` | vortex or winding defect | superfluid or superconducting vortex |
| `pi_2(M)` | monopole / hedgehog texture | monopole-style topological texture |
| `pi_3(M)` | skyrmion / instanton structure | skyrmions and related solitons |

That is one of the strongest reasons topology belongs in a foundations note. It gives a shared classification language for vortices in superconductors, monopole-like textures in fields, and topological defects across many-body systems.

### Second Quantization and Fock Space

Second quantization is the shift from wavefunctions for fixed particles to operators acting on a space of variable particle number. That language is what lets atoms, photons, phonons, Cooper pairs, and quantum fields all enter a single formal framework instead of living in separate theories.

The core reason it is needed is simple: physical processes change particle number. Emission, absorption, pair creation, pair annihilation, pairing, and condensation cannot be described cleanly in fixed-`N` first-quantized language.

Fock space is the direct sum of all particle-number sectors. Creation and annihilation operators move between them. The field operator is then not a wavefunction but an operator that destroys or creates excitations at a point.

That shift is what makes the following ideas natural instead of formal tricks:

- the vacuum as a structured state rather than "nothing"
- coherent states as the bridge to classical fields
- Bose condensation as nonzero field expectation
- superconductivity as condensation of fermion bilinears

Appendix B makes one further point clearly: second quantization is the language in which emission and absorption stop looking like external add-ons. Once the field itself is quantized, spontaneous emission, stimulated emission, pair creation, and vacuum fluctuation effects all become ordinary transitions between neighboring Fock sectors rather than awkward exceptions to fixed-particle mechanics.

The supplementary material also makes the algebraic side explicit, which is worth carrying into the atlas directly. Fock space is the direct sum

```text
F = H^0 (+) H^1 (+) H^2 (+) ...
```

and creation / annihilation operators satisfy either commutation or anticommutation relations:

```text
[a(k), a^dagger(k')] = delta^3(k-k')          for bosons
{c(k), c^dagger(k')} = delta^3(k-k')          for fermions
```

This is one of the cleanest places where a physical principle is embedded directly in the algebra. Pauli exclusion is not an extra statement bolted onto fermions later; it is already encoded in the anticommutator algebra because repeated creation in the same state vanishes.

The field operator itself is then the Fourier transform of those ladder operators, so a quantum field is not a wavefunction but an operator-valued distribution that creates or removes excitations locally. That distinction is easy to blur in notation and central to the whole atlas.

Coherent states are the most useful bridge back to classical intuition. They are eigenstates of annihilation operators and therefore the states whose field expectation values behave most like classical waves. This is why lasers, condensates, and ordered phases keep appearing as coherent-state physics in different clothes.

The normal-ordering lesson from Supplementary G also belongs here. Products of fields at the same point carry vacuum contributions that are formally divergent, so already at this elementary level the theory teaches the need for subtraction schemes and renormalized observables. Normal ordering is the simplest local rehearsal for the more general renormalization logic that later appears in interacting field theory.

### Gauge Fields, Photons, and Minimal Coupling

The atlas repeatedly uses gauge symmetry, but the photon example is the cleanest place to state what that means. The photon is not merely "the particle of light." It is the gauge boson forced by local `U(1)` phase symmetry.

The local transformation law is:

```text
A_mu -> A_mu + partial_mu theta(x,t)
psi -> exp(i e theta(x,t)) psi
```

and the whole point is that once local phase invariance is demanded, the electromagnetic field is no longer optional. The covariant or minimal-coupling replacement introduces it:

```text
p -> p - e A
```

This is one of the cleanest places where symmetry generates a physical entity rather than only constraining one. The photon exists in the theory because local phase symmetry requires a connection field.

The Appendix B discussion is also useful because it states what the photon carries in symmetry language:

- energy `hbar omega`
- momentum `hbar k`
- angular-momentum projection `+/- hbar`
- zero charge and zero rest mass in the unbroken vacuum

Masslessness is not just an empirical fact here; it is symmetry-protected. A bare mass term for the gauge field would violate the local `U(1)` invariance. That is why the unbroken vacuum has a massless photon, while superconductors and the electroweak broken phase realize the Higgs mechanism instead and give the relevant gauge fields an effective mass.

This is also why the photon is such a good atlas object. It links Noether logic, local symmetry, angular momentum, selection rules, and symmetry breaking all in one place.

### Atomic-Radiation Coupling, Selection Rules, and Gauge Forms

Appendix B is especially valuable here because it turns a familiar topic into a foundations lesson. The atom-radiation interaction can be written in several gauge-equivalent ways:

```text
H_int = -(e/mc) A . p + (e^2 / 2mc^2) A^2
H_int = - d . E = - e r . E
H_int = -(e / m omega^2) E . grad V(r)
```

These are not different physical theories. They are different representations of the same coupling, related by gauge or unitary transformations. For exact calculations they agree. For approximate calculations their disagreement is diagnostically useful, which is why length-velocity comparisons become such a strong wavefunction-quality test in atomic structure.

This is also the natural place to keep the Einstein-process logic:

- stimulated absorption scales with radiation density
- stimulated emission scales with radiation density
- spontaneous emission remains even in the absence of a classical driving field

The thermodynamic Einstein argument matters because it shows that stimulated emission is not a later embellishment but a consistency requirement once atoms with discrete levels sit in thermal equilibrium with radiation.

Selection rules then become a direct reading of what the photon is:

- spin-1 and transversality give the angular-momentum limits
- odd parity of the electric dipole operator forces opposite parity initial and final states
- spin-blind electric dipole coupling leaves `S` unchanged

This compact formulation matters because the rules are not arbitrary rules, but consequences of angular momentum and parity conservation together with the representation carried by the photon.

### Vacuum Fluctuations, Spontaneous Emission, and the Lamb Shift

The atlas uses the word "vacuum" structurally rather than rhetorically, and Appendix B gives one of the best concrete examples. In quantum field theory the vacuum is not empty. The electromagnetic field retains zero-point fluctuations even in its lowest state.

The core point can be stated directly:

```text
<0|E^2|0> != 0
```

so an excited atom is never completely isolated from the field. The vacuum itself can induce transitions. In that language, spontaneous emission is simply stimulated emission driven by the zero-point field rather than by a populated classical radiation background.

This is one of the most useful foundational bridges in the atlas because it connects several ideas that otherwise get taught separately:

- Einstein `A` coefficients
- density of states and `omega^3` scaling
- linewidths and exponential decay
- the Lamb shift as vacuum-induced level renormalization

The Wigner-Weisskopf picture gives the cleanest compressed statement:

```text
dot c_e(t) = - (A_eg / 2 + i Delta omega) c_e(t)
```

which leads to exponential decay of the excited-state amplitude, a Lorentzian natural line shape, and a frequency shift from the same underlying vacuum coupling.

That is why the Lamb shift matters so much in the atlas. It is not only a precision correction. It is the point where the vacuum announces that the atom and the field cannot be cleanly separated.

### Path Integrals, Partition Functions, and Wick Rotation

This is the bridge between dynamics, thermodynamics, and field theory. The path integral recasts amplitudes as sums over histories, Wick rotation ties quantum evolution to statistical weighting, and partition functions turn phase structure and response into geometric or field-theoretic questions.

The key move is the replacement of real time by imaginary time. Under that rotation, the unitary evolution operator becomes the Boltzmann weight. Quantum propagation and thermal weighting become two faces of the same mathematics.

That is why the Euclidean action is so important in the atlas. It is the natural language for:

- partition functions
- saddle-point structure
- symmetry-breaking minima
- fluctuations around ordered phases
- the bridge from microscopic theory to effective field theory

Landau theory then appears as the local effective free-energy description near symmetry-breaking transitions, while the full path integral explains where Landau succeeds and where fluctuations force us beyond it.

This core identity recurs almost everywhere:

```text
Z = Tr exp(-beta H)
```

and after Wick rotation the same weighting appears as a Euclidean path integral rather than as unitary time evolution. This is why statistical mechanics, quantum field theory, black-hole thermality, and holographic Euclidean calculations keep reusing the same formal objects.

It is also why Matsubara structure matters so much to the atlas. Finite temperature means imaginary time is compactified to a circle of length `hbar / k_B T`, making temperature itself a geometric or topological feature of the Euclidean formulation rather than only a phenomenological parameter.

The Supplementary I material makes this sharper by keeping the boundary conditions explicit:

- bosonic fields are periodic in imaginary time
- fermionic fields are antiperiodic in imaginary time

which leads to the Matsubara frequencies

```text
omega_n^(boson) = 2 pi n k_B T / hbar
omega_n^(fermion) = (2n+1) pi k_B T / hbar
```

The `n=0` bosonic mode is especially important because it is the mode that dominates the high-temperature or dimensionally reduced limit, and it is often the mode most directly associated with ordering phenomena such as Bose condensation.

This is also the cleanest place to preserve the partition-function path-integral identity:

```text
Z = Tr exp(-beta H) = integral_periodic Dphi exp(-S_E[phi] / hbar)
```

so the atlas keeps the exact bridge between statistical mechanics and Euclidean field theory in view rather than only alluding to it.

### Spontaneous Symmetry Breaking as Formal Machinery

Several domain notes use spontaneous symmetry breaking operationally, but the formal pattern belongs here. The simplest shared model is the `O(N)`-symmetric or complex-scalar "Mexican hat" potential:

```text
V(phi) = lambda (phi_i^2 - v^2)^2 / 4
```

Choosing one vacuum direction breaks the full symmetry down to the subgroup that preserves that direction. The remaining structure can then be summarized in the language that the whole atlas keeps using:

- radial fluctuations become massive amplitude modes
- tangential fluctuations become Goldstone modes
- for local gauge symmetry, the would-be Goldstone is absorbed by the gauge field

The linear-sigma-model picture is useful enough to state directly:

| Situation | Outcome |
|---|---|
| global broken symmetry | `dim(G) - dim(H)` Goldstone modes |
| local broken gauge symmetry | gauge boson becomes massive, Goldstone not separately visible |
| approximate broken symmetry | pseudo-Goldstones acquire small mass |

This is the shared formal reason that pions, phonons, magnons, superfluid modes, the Meissner effect, and electroweak gauge-boson masses can all be discussed within one family.

The Landau-theory side of the same story also belongs here. Near a transition, the free energy is organized as an expansion in the order parameter consistent with symmetry:

```text
F(m) = a_0 + a_2 m^2 + a_4 m^4 + a_6 m^6 + c (grad m)^2 + ...
```

The entire transition structure is then encoded in the coefficients:

- `a_2 > 0` favors the symmetric phase
- `a_2 < 0` favors an ordered phase
- the sign of `a_4` helps distinguish continuous from first-order behavior

The reason Landau theory is useful but not final is also worth retaining. It is the saddle-point approximation to the Euclidean path integral. It captures symmetry structure beautifully, but below the upper critical dimension fluctuations invalidate the naive mean-field exponents and force the RG to take over.

### Renormalization Group, Fixed Points, and Universality

The renormalization group is how the atlas thinks about scale. Couplings run, descriptions simplify or thicken with scale, and fixed points explain why very different microscopic systems can share the same macroscopic critical behavior.

The central question is: when we zoom out, which information survives? The Wilsonian answer is to integrate out short-distance modes and track how couplings change. Relevant perturbations grow, irrelevant ones die away, and marginal ones require closer inspection.

This is why universality is possible. Systems with very different microscopic makeup can flow toward the same fixed point and therefore share the same low-energy or long-distance behavior. That logic connects:

- classical critical phenomena
- quantum criticality
- effective field theory in particle physics
- emergent phases in condensed matter
- radial flow in holographic descriptions

The supplementary RG material is strong enough that some of its explicit formulas belong here, not just the summary. The Wilsonian move is:

```text
exp[-S_eff[phi_<]] = integral Dphi_> exp[-S[phi]]
```

meaning that high-momentum or short-distance modes are integrated out, leaving an effective theory for the remaining low-energy modes. The couplings in that effective theory then flow with scale according to the beta function

```text
beta(g) = mu dg / dmu
```

and the zeros of that function are fixed points.

The relevance classification is one of the main explanatory payoffs of the RG:

- relevant perturbations grow under coarse-graining
- irrelevant perturbations fade away
- marginal perturbations require higher-order analysis

That is the formal reason universality exists. Systems can differ wildly in microscopic detail and still flow to the same infrared description because most of those details are irrelevant in the RG sense.

The supplementary material also sharpens the connection to critical phenomena by tying a universality class to:

- spatial dimension
- symmetry of the order parameter
- whether the transition is classical or quantum

and, for quantum critical points, to the dynamical critical exponent `z` through

```text
xi_tau ~ xi^z
```

This belongs in foundations because it is the cleanest shared language for classical criticality, quantum phase transitions, effective field theory, and holography alike.

The RG-as-geometry idea is also worth preserving here: the beta function is a vector field on theory space, fixed points are its zeros, and holography turns that flow into literal geometry along the radial AdS direction. That is one of the most elegant examples in the atlas of an abstract organizing principle becoming a geometric picture.

### Information Theory as a Cross-Domain Language

Information appears here as a common descriptive layer rather than a separate subject. Shannon entropy, von Neumann entropy, mutual information, and entanglement structure are used as tools for describing boundaries, correlations, channels, and emergent organization across many different physical domains.

This is especially important near boundaries. Entanglement entropy measures how strongly regions are tied together, mutual information tracks shared structure, and channel language clarifies what can move across an interface. That makes information theory one of the cleanest shared vocabularies between condensed matter, quantum foundations, and holography.

Thermodynamic entropy is not merely analogous to information entropy but a physical realization of it. In that language:

```text
H = - sum_i p_i log p_i
S(rho) = - Tr[rho ln rho]
S_Boltzmann = k_B ln W
```

are not three unrelated definitions. They are the same structural idea at different levels of description: missing information about which state is realized.

The quantum version matters especially because it sharpens several recurring atlas ideas:

- decoherence is information flow into an environment, not literal destruction of information
- entanglement entropy measures how much a boundary region is tied to what lies across it
- mutual information measures how much one domain tells you about another

This is why information theory links so naturally to holography. The area-law scaling of entanglement in gapped systems and the Ryu-Takayanagi formula are both statements that physically important information is often organized by boundaries rather than volumes.

The channel language from Supplementary L is also useful. A quantum channel is the most general completely positive, trace-preserving map between input and output states, and that turns out to be exactly the right level of abstraction for every quantum transducer. A Josephson junction, a cavity-QED interface, a SAW bus, or an optomechanical converter is not only a device; it is a quantum-information channel between physical domains.

One more interpretive idea fits naturally here: emergence is compression. On that view, higher-level concepts such as functional group, gene, order parameter, or quasiparticle are not arbitrary conveniences but efficient compression schemes for the underlying microscopic information relevant to a given scale.

### Anomaly Inflow and Bulk-Boundary Consistency

Anomaly language belongs in foundations because it explains why some boundary states are not optional low-energy accidents but consistency requirements of the full theory. A quantum anomaly is the failure of a classical symmetry to survive quantization, and the key point is that anomalies can sometimes be cancelled only when bulk and boundary are considered together.

The axial anomaly remains the prototype:

```text
partial_mu J_A^mu ~ E . B
```

which shows that a classically conserved current can fail to remain conserved in the quantum theory. In particle physics this constrains which gauge theories are consistent at all. In condensed matter it explains why topological bulk phases force protected boundary structure.

The Supplementary K version of the story is worth stating directly. A bulk Chern-Simons or theta term is not gauge invariant by itself in the presence of a boundary. Its variation becomes a boundary term. The boundary theory then carries an anomaly of exactly the opposite form. The combined system is consistent, but neither piece is consistent on its own.

That is the deep reason bulk-boundary correspondence is not merely energetic:

- the bulk term is topological and carries the would-be gauge variation
- the edge or surface theory is anomalous by itself
- the full system cancels only when both are present

This is why protected edge states in the quantum Hall effect or topological-insulator surface states cannot simply be removed without changing the topology or violating consistency.

The Standard Model side of this story also belongs here. Gauge anomalies must cancel exactly, which is one of the sharpest reasons the particle content of each fermion generation looks constrained rather than arbitrary. This is not a full derivation of the Standard Model, but anomaly cancellation remains one of the strongest consistency filters in high-energy theory.

### Algebraic Constraints: Reals, Complex Numbers, Quaternions, and Octonions

The division-algebra material sits near the speculative edge of the foundations note, but part of it is solid enough to keep. Hurwitz's theorem says that the normed division algebras over the reals are exhausted by:

- `R`
- `C`
- `H`
- `O`

and that sequence matters because each step preserves some structures while sacrificing others.

The most solid atlas uses of this are:

- complex numbers organize phase, interference, and unitary quantum mechanics
- quaternions organize spinor and `SU(2)` structure
- octonions generate the exceptional Lie groups and appear naturally near some high-dimensional and string-theoretic structures

The manuscript is on firmest ground when it says:

- ordinary quantum mechanics is deeply tied to `C`
- spin and relativistic spinor structure are naturally tied to quaternionic mathematics
- exceptional groups such as `G_2`, `F_4`, and `E_8` have octonionic constructions

The more ambitious claims about three fermion generations or a unique algebraic derivation of the Standard Model remain frontier material. They motivate a real research program, but they are not on the same evidential footing as the complex-number structure of ordinary quantum mechanics.

### Conformal Structure, Operator Dimensions, and the Bulk-Boundary Dictionary

Conformal symmetry appears in the atlas whenever scale invariance sharpens into a larger structure. Critical points, the Efimov problem, and AdS/CFT all reuse this language, so the formal ingredients belong here rather than only in the gravity chapter.

The conformal group extends Poincare symmetry by adding dilatations and special conformal transformations:

| Generator | Role |
|---|---|
| `P_mu` | translations |
| `M_(mu nu)` | Lorentz rotations / boosts |
| `D` | scale transformation |
| `K_mu` | special conformal transformation |

The key reason this matters physically is that correlation functions are then heavily constrained by symmetry alone. The AdS/CFT mass-dimension relation is:

```text
Delta = d/2 + sqrt(d^2/4 + m^2 L^2)
```

which is one of the clearest examples of mathematics turning directly into a cross-domain dictionary. A bulk field mass becomes a boundary operator dimension. Renormalization-group flow and radial bulk depth can then be read as two descriptions of the same structural change in scale.
## Connections to Other Regions

This note provides the common grammar for the rest of the atlas. Atomic physics, condensed matter, particle theory, and holography all reuse this vocabulary, even when the physical systems are very different.
