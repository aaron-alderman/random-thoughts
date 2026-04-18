# References and Formula Sheets

This note is the compact lookup layer of the atlas. It is not meant to carry long prose arguments. Instead, it holds the formulas, group-theory summaries, classification tables, and compact reference structures that support the regional notes.

## Core Topics

### Quantum Mechanics Formulas

This section holds the recurring equations that support atomic, molecular, and few-body discussions without repeating derivations in each chapter.

Representative formulas:

```text
Schrodinger equation:   i hbar dpsi/dt = H psi
Hydrogen spectrum:      E_n = -13.6 eV / n^2
Rigid rotor:            E_J = B J(J+1)
Harmonic oscillator:    E_v = hbar omega (v + 1/2)
Berry phase:            gamma = i integral <u_nk|nabla_k|u_nk> . dk
Chern number:           C = (1/2pi) integral_BZ Omega_n(k) d^2k
```

The purpose of this section is not derivation but recall. The main notes should explain why these formulas matter; this note should let the reader retrieve them quickly.

Additional widely reused formulas:

```text
Time evolution:         U(t) = exp(-iHt/hbar)
Anharmonic correction:  E_v = hbar omega_e (v+1/2) - hbar omega_e x_e (v+1/2)^2
Symmetric top:          E(J,K) = B J(J+1) + (A-B) K^2
```

Additional transition and response formulas:

```text
Fermi Golden Rule:      W_(i->f) = (2pi/hbar) |<f|H_int|i>|^2 delta(E_f - E_i +/- hbar omega)
Einstein A coefficient: A_(eg) = (e^2 omega^3 / 3pi epsilon_0 hbar c^3) |<e|r|g>|^2
Oscillator strength:    f_(ge) = (2m omega_(ge) / 3hbar) |<e|r|g>|^2
TRK sum rule:           sum_(n != g) f_(gn) = N
Einstein balance:       g_g B_(ge) = g_e B_(eg)
A/B relation:           A_(eg) = (hbar omega^3 / pi^2 c^3) B_(eg)
```

These formulas matter because they compress a large amount of atomic and optical structure into a few reusable expressions: matrix elements, density of states, and exact commutator constraints.

Useful interaction-picture reminders:

```text
Velocity gauge:         H_int = -(e/mc) A . p + (e^2 / 2mc^2) A^2
Length gauge:           H_int = - d . E = - e r . E
Acceleration gauge:     H_int = -(e / m omega^2) E . grad V(r)
```

These are gauge-equivalent for exact work and are useful partly because discrepancies between them become an approximation diagnostic.

### Group Theory Reference

This section is the compact place for reduction formulas, representation identities, angular-momentum couplings, and notation conventions used across the atlas.

Representative formulas:

```text
Reduction formula:      n_i = (1/|G|) sum_g chi(g) chi_i*(g)
Clebsch-Gordan:         D^(j1) x D^(j2) = sum_J D^J
Wigner-Eckart:          matrix element = geometric factor x reduced matrix element
Goldstone counting:     N_GB = dim(G) - dim(H)
```

A quick-reference map of common symmetry breakings and their physical consequences belongs in this section.

Useful group inventory:

| Group | Dimension or order | Physical role | Labels |
|---|---|---|---|
| `U(1)` | 1 | electromagnetic gauge or phase symmetry | integer charge |
| `SU(2)` | 3 | spin, isospin, weak symmetry | `j = 0, 1/2, 1, ...` |
| `SO(3)` | 3 | spatial rotations | `l = 0, 1, 2, ...` |
| `SU(3)` | 8 | QCD color | `(p,q)` |
| `SO(4)` | 6 | hidden hydrogen symmetry | `n,l` structure |
| `SO(3,1)` | 6 | Lorentz symmetry | `(j_1, j_2)` |
| `SO(4,2)` | 15 | conformal / AdS isometry | `Delta`, spin |
| `SO(2,1)` | 3 | Efimov / one-dimensional conformal structure | scaling data |
| `S_2 = Z_2` | 2 | exchange symmetry | symmetric / antisymmetric |
| `O_h`, `T_d`, `D_(6h)` | finite | crystal and molecular symmetry | character-table species |

A compact point-group reference:

| Point group | Main use in the atlas | Key consequence |
|---|---|---|
| `C_(2v)` | CuO`_2` planes, bent molecules | mode labels and selection rules |
| `D_(inf h)` | linear molecules | IR/Raman mutual exclusion by parity |
| `O_h` | octahedral coordination | `e_g (+) t_(2g)` crystal-field splitting |

Useful free-field / relativistic reminders:

```text
Free Hamiltonian:       H = p^2 / 2m
Plane wave:             psi_k(r) = exp(i k . r)
Dirac equation:         (i hbar gamma^mu partial_mu - mc) psi = 0
```

### Symmetry and Goldstone Reference

This section distills the standard formulas for spontaneous symmetry breaking, Goldstone counting, and gauge-field mass generation.

Useful core formulas:

```text
Goldstone theorem:      N_bosons = dim(G) - dim(H)
Mexican-hat potential:  V(phi) = lambda (|phi|^2 - v^2)^2 / 4
GMOR relation:          m_pi^2 ~ m_quark <qbar q> / f_pi^2
Higgs mechanism:        gauge field mass ~ e v
```

Additional formal reminders:

```text
Ward identity signal:   d_mu <J^mu_a phi_b> = <[Q_a, phi_b]> != 0
Sigma model vacuum:     |phi| = v  =>  vacuum manifold S^(N-1)
```

Compact symmetry-breaking map:

| Breaking pattern | Consequence |
|---|---|
| `SU(2)_L x SU(2)_R -> SU(2)_V` | pions as pseudo-Goldstones |
| `SO(3) -> SO(2)` | magnons in a magnet |
| global `U(1) ->` broken phase | phase mode / superfluid sound |
| local `U(1) ->` Higgsed phase | Meissner screening, massive gauge field |

Compact photon / gauge-boson reminders:

| Quantity | Photon property |
|---|---|
| gauge origin | local `U(1)` connection field |
| spin | 1 |
| physical helicities | `+/- 1` |
| mass in unbroken vacuum | 0 |
| momentum / energy | `hbar k`, `hbar omega` |

Compact anomaly / topology reminders:

```text
ABJ anomaly:            partial_mu J_A^mu ~ (alpha / pi) E . B
Chern-Simons term:      S_CS ~ int epsilon^(mu nu lambda) A_mu partial_nu A_lambda
TI theta term:          S_theta ~ int E . B
QCD theta term:         S_theta^(QCD) ~ int Tr[G_(mu nu) Gtilde^(mu nu)]
```

These are included because they are the shortest route from topology to physical response and from classical symmetry to quantum anomaly.

### Solids and Band Theory Formulas

This section gathers Bloch, reciprocal-lattice, tight-binding, and response formulas that otherwise clutter the main materials chapters.

Representative formulas:

```text
Bloch theorem:          psi_nk(r) = e^(ik.r) u_nk(r)
Reciprocal lattice:     a_i . b_j = 2pi delta_ij
Nearly-free gap:        Delta_E = 2 |V_G|
1D tight binding:       E(k) = e0 - 2t cos(ka)
Hall conductance:       sigma_xy = (e^2/h) sum_n C_n
```

Additional useful formulas:

```text
2D square tight binding: E(k) = e0 - 2t(cos k_x a + cos k_y a)
LO-TO splitting:         omega_LO^2 / omega_TO^2 = epsilon_static / epsilon_infinity
```

### Gravity and Holography Formulas

This section holds the compact horizon, entropy, temperature, and AdS/CFT equations that are repeatedly referenced in the gravity chapter.

Representative formulas:

```text
Schwarzschild radius:   r_s = 2GM/c^2
Hawking temperature:    T_H = hbar c^3 / (8 pi G M k_B)
Bekenstein entropy:     S = k c^3 A / (4 G hbar)
Ryu-Takayanagi:         S_A = Area(gamma_A) / 4 G_N
AdS metric:             ds^2 = (L^2/z^2)(-dt^2 + dx^2 + dz^2)
```

RG / holography bridge reminders:

```text
Beta function:          beta(g) = mu dg / dmu
RG coarse graining:     exp[-S_eff[phi_<]] = integral Dphi_> exp[-S[phi]]
Dynamical scaling:      xi_tau ~ xi^z
```

### Superconductivity and Quantum Materials Formulas

This section collects coherence lengths, penetration depths, flux quantization, transport scales, and similar relations for fast lookup.

Representative formulas:

```text
London depth:           lambda_L = (m / mu0 n_s e^2)^(1/2)
Coherence length:       xi ~ hbar v_F / Delta
Flux quantization:      Phi = n h / 2e
BCS transition:         k_B T_c ~ 1.13 hbar omega_D exp[-1/N(0)V]
Planckian rate:         1/tau = k_B T / hbar
Josephson relations:    I = I_c sin(phi),  V = (hbar/2e) dphi/dt
```

### Nuclear and Molecular Formula Sheets

This section gathers the compact working equations for isotope shifts, effective nuclear forces, normal modes, anharmonicity, and rotational structure.

Representative formulas:

```text
Normal modes:           3N-6 (nonlinear), 3N-5 (linear)
Morse anharmonicity:    E_v = hbar omega_e (v+1/2) - hbar omega_e x_e (v+1/2)^2
OPE potential:          V_OPE ~ (tau1.tau2)[sigma1.q sigma2.q /(q^2+m_pi^2) - ...]
Efimov spectrum:        E_n = E_0 exp(-2 pi n / s_0)
Efimov ratio:           a_(n+1)/a_n = exp(pi/s_0) ~ 22.7
```

Additional useful formulas:

```text
Rotational distortion:  D = 4 B^3 / omega^2
CO2 vibrational pattern: Gamma_vib = Sigma_g^+ + Pi_u + Sigma_u^+
```

### Character Tables and Classification Maps

This section is the home for the most frequently used tables, especially when they are helpful for reference but disruptive to the reading flow of the main notes.

The long-term goal is to keep this note compact but high-value: formulas, classification tables, and symmetry maps that are repeatedly needed across the atlas without repeating explanatory prose each time.

A compact symmetry-to-physics map is useful here:

| Topic | Main symmetry move | Result |
|---|---|---|
| helium exchange | permutation plus spin symmetry | para / ortho split |
| hydrogen fine structure | hidden `SO(4)` reduced by corrections | lifted `l` degeneracy |
| molecular vibrations | point-group decomposition | IR / Raman activity |
| crystal electrons | continuous translation -> lattice translation | Bloch states and bands |
| broken continuous symmetry | `G -> H` | Goldstone counting |
| superconductivity | broken local `U(1)` | Meissner effect and flux quantization |
| AdS/CFT | shared `SO(d,2)` structure | bulk / boundary duality |

More of Appendix B in direct reference form:

| Section topic | Group `G` | Reduction / subgroup `H` | Physical result |
|---|---|---|---|
| hydrogen threshold | `SO(4) -> E(3) -> SO(3,1)` | boundary restructuring | enhanced threshold symmetry |
| Efimov problem | `SO(2,1)` | boundary condition breaks to discrete scaling | geometric spectrum |
| dipole transitions | `SO(3) x Z_2` | tensor-selection condition | `Delta J = +/- 1, Delta L = +/- 1, Delta S = 0` |
| Bloch theorem | continuous translation | Bravais lattice `T` | crystal momentum and bands |
| band gaps | space group | little group `G_k` | band labels and degeneracies |
| van Hove points | little-group critical point structure | nonanalytic density of states | singular response |
| phonons | continuous translation | discrete lattice symmetry | acoustic Goldstone branches |
| crystal field | `SO(3)` | `O_h` | `e_g (+) t_(2g)` splitting |
| Jahn-Teller | `O_h` | lower symmetry such as `D_(4h)` | orbital order and distortion |
| BdG topology | tenfold-way symmetry class | classification by invariant | Chern or `Z_2` data |
| holographic RG | conformal group | broken by relevant deformation | radial flow as RG flow |
| electroweak symmetry | `SU(2)_L x U(1)_Y` | `U(1)_EM` | `W`, `Z`, Higgs structure |
| cuprate orbital selection | local point group of CuO`_2` | unique orbital irrep | `d_(x^2-y^2)` dominance |

Compact character-table reminders:

```text
D^2(SO(3)) -> E_g (+) T_(2g)    under O_h
```

| `D_(inf h)` species | IR active? | Raman active? | Example meaning |
|---|---|---|---|
| `Sigma_g^+` | no | yes | symmetric stretch |
| `Pi_u` | yes | no | bending mode |
| `Sigma_u^+` | yes | no | asymmetric stretch |

The goal of this section is not completeness. It is to keep the most reused classification maps close at hand so the main chapters do not have to keep re-explaining them.

### Vacuum, Linewidth, and Field-Coupling Reminders

Compact QFT-facing reference formulas:

```text
Vacuum field fluctuation: <0|E^2|0> = sum_k (hbar omega_k / 2 epsilon_0 V)
Wigner-Weisskopf:        dot c_e(t) = -(A_(eg)/2 + i Delta omega) c_e(t)
Excited-state amplitude: c_e(t) = exp[-(A_(eg)/2 + i Delta omega)t]
Natural linewidth:       Gamma = A_(eg) = 1/tau
```

These are included because they connect spontaneous emission, Lamb shifts, and natural line broadening in the most compact possible way.

QFT propagator reminders:

```text
Electron propagator:    S_F(p) ~ i (gamma . p + mc) / (p^2 - m^2 c^2 + i epsilon)
Photon propagator:      D_F(k) ~ -i eta_(mu nu) / (k^2 + i epsilon)
```

### Information-Theory Reminders

Compact information formulas:

```text
Shannon entropy:        H = -sum_i p_i log p_i
Von Neumann entropy:    S(rho) = -Tr[rho ln rho]
Mutual information:     I(A:B) = S_A + S_B - S_(AB)
Quantum channel:        E(rho) = sum_k K_k rho K_k^dagger
```

These are here because the atlas repeatedly uses entropy, entanglement, and channel language in condensed matter, foundations, and holography.

### Statistical / Euclidean Field Theory Reminders

Compact partition-function formulas:

```text
Partition function:     Z = Tr exp(-beta H)
Wick rotation:          t -> -i hbar beta
Euclidean path integral: Z = integral_periodic Dphi exp[-S_E[phi] / hbar]
Boson Matsubara:        omega_n = 2 pi n k_B T / hbar
Fermion Matsubara:      omega_n = (2n+1) pi k_B T / hbar
Landau free energy:     F(m) = a_0 + a_2 m^2 + a_4 m^4 + c (grad m)^2 + ...
```

### Algebraic Structure Reminders

Compact division-algebra map:

| Algebra | Dimension | Key role in the atlas |
|---|---|---|
| `R` | 1 | classical real-valued structure |
| `C` | 2 | quantum phase and unitary interference |
| `H` | 4 | spinors and `SU(2)` structure |
| `O` | 8 | exceptional groups and speculative high-energy structure |
## Connections to Other Regions

This note supports all regions and stays concise. Detailed explanation belongs in the main regional notes; this file is for retrieval and cross-reference.
