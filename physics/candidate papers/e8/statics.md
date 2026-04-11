# Statics / Kinematics

## Core Objects

| Object | Role | Status | Maturity |
|---|---|---|---|
| $E_8 / E_6$ | Ambient container for all exceptional structures | Choice | 5 |
| $G_2$ | Automorphism group of $\mathbb{O}$; encodes $\sqrt{3}$ coarse-graining ratio in triple bond | Structural proposal | 4 |
| $J_3(\mathbb{O})$ | 27-dim exceptional Jordan algebra; natural 24+3 split | Working branch | 4 |
| Leech lattice $\Lambda_{24}$ | Global state space; rootless; no local perturbations admitted | Established (Baez/Egan) in off-diagonal sector | 3 |
| 3 diagonal entries $(a,b,c) \in \mathbb{R}^3$ | "Snap coordinates"; bridge between Leech and active sector | Structural proposal | 5 |
| $SO(2,4)$ | Conformal group; scale ambient; RG running lives here | Established | 2 |
| $Spin(2,3)$ | Post-reduction group; scale fixed; no dilatation generator | Working branch | 3 |
| $u \in \mathrm{Im}(\mathbb{O})$ | Selected octonionic direction; fixes time anchor and observable channel | Choice (possibly derivable) | 4 |
| $u^\perp \cong \mathbb{C}^3$ | Active complex sector; where dynamics and interactions live | Derived from $u$ | 4 |

---

## The 24+3 Split

The split is intrinsic to the Jordan algebra, not imposed:

$$J_3(\mathbb{O}) = \begin{pmatrix} a & X & Y \\ X^* & b & Z \\ Y^* & Z^* & c \end{pmatrix}, \quad a,b,c \in \mathbb{R},\ X,Y,Z \in \mathbb{O}$$

$$27 = \underbrace{3}_{\text{diagonal (real, snap frame)}} + \underbrace{24}_{\text{off-diagonal (octonionic, Leech sector)}}$$

The diagonal entries are already algebraically different from the off-diagonal entries. The 24-dimensional off-diagonal sector over integral octonions contains a Leech-isometric sublattice (Baez/Egan). This is the strongest established result in the program.

---

## The Two-Sector Ontology

| Sector | Structure | Character | Status | Maturity |
|---|---|---|---|---|
| T2 (Leech / hidden) | Off-diagonal $\mathbb{O}^3_\mathbb{Z}$; $\Lambda_{24}$ sublattice | Passive, global, read-only; no roots = no local perturbations | Interpretation | 5 |
| T1 (active / observable) | $u^\perp \cong \mathbb{C}^3$; off-diagonal $J_3(\mathbb{O})$ | Dynamic; perturbative physics lives here | Proposal | 4 |

The Leech lattice being rootless is physically significant: roots generate local reflections. A rootless lattice has no reflection generators — nothing acts on it locally. This makes it a natural candidate for a passive, read-only global state space.

### The Leech consistency layer

The Golay code's minimum weight 8 means the smallest nonzero valid configuration touches 8 coordinates. Geometrically:

$$\text{minimum code weight} \quad \leftrightarrow \quad \text{minimum geometric locality}$$

Small local defects are not admissible states. This is the geometric analogue of error correction operating on the state space itself.

### Non-perturbative physics

- Perturbative physics = local fluctuations = rejected by Leech (no roots)
- Non-perturbative physics = global topology = exactly what Leech admits
- Non-perturbative effects are invisible to perturbation theory because they live on the Leech tier, which perturbative expansion cannot reach by local steps

---

## The Snap Coupling

The natural packaging map

$$\beta: \mathbb{R}^3 \times \mathbb{O}^3 \to J_3(\mathbb{O})$$

is only bookkeeping. The bridge requires a second map:

$$\Gamma: \mathbb{R}^3 \to \mathrm{End}(\mathbb{O}^3)$$

specifying how the diagonal entries act on the off-diagonal Leech sector. The natural candidate is the Jordan product $D \circ U$. The test: this map must be equivariant under the residual $SU(3)$ symmetry. Until that is verified, the diagonal bridge is a structural suggestion, not a coupling law.

---

## SU(3) as Color: What is Still Missing

The stabilizer isomorphism is step 1 only:

$$\mathrm{Stab}(u) \cong SU(3) \quad \not\Rightarrow \quad SU(3)_C \text{ of QCD}$$

What is needed:

$$\rho_q: \mathcal{H}_\mathrm{quark} \to \mathbf{3}, \quad \rho_{\bar{q}}: \mathcal{H}_\mathrm{antiquark} \to \bar{\mathbf{3}}, \quad \mathrm{ad}(SU(3)) \to \mathbf{8}$$

plus a local gauge connection, coupling law, and anomaly check.

The octonionic structure does produce 3- and 8-dimensional objects naturally under the $u$-selection. The gap is from "present" to "gauged with correct coupling and anomaly structure."

Honest claim status: **candidate color symmetry**, not derived color. This may be a permanent structural rather than forced result — some features of the universe may be natural without being uniquely derivable.

---

## Leech Equivariance Check — Results

### Part 1: Fixing the Baez/Egan Embedding

**Lattice conventions.** $E_8$ with min squared norm 2 is self-dual ($\det = 1$). The off-diagonal sector $\mathbb{O}_\mathbb{Z}^3$ with the component-sum inner product is $E_8^3$ (min norm 2, det 1, rank 24). The Leech lattice $\Lambda_{24}$ in standard normalization has min norm 4, det 1, rank 24.

**The correct containment direction.** Since both $E_8^3$ and $\Lambda_{24}$ are even unimodular of rank 24 but non-isometric (different min norms), neither can be a proper sublattice of the other in $\mathbb{R}^{24}$ (equal determinants force equal index, hence equality — but they are not isometric). The Baez/Egan embedding uses the **scaled Leech lattice** $\sqrt{2}\Lambda_{24}$, which has min norm 8 and det $2^{12}$. The index formula

$$[E_8^3 : \sqrt{2}\Lambda_{24}] = \sqrt{\det(\sqrt{2}\Lambda_{24})/\det(E_8^3)} = \sqrt{2^{12}/1} = 2^6 = 64$$

shows that $\sqrt{2}\Lambda_{24}$ is an index-64 sublattice of $E_8^3$. Integrality is satisfied: inner products in $\sqrt{2}\Lambda_{24}$ lie in $2\mathbb{Z} \subset \mathbb{Z}$, so $\sqrt{2}\Lambda_{24}$ is a valid even sublattice of $E_8^3$.

**The precise statement of Baez/Egan:** $\mathbb{O}_\mathbb{Z}^3 \cong E_8^3$ contains $\sqrt{2}\Lambda_{24}$ as a sublattice of index 64. The quotient $E_8^3/\sqrt{2}\Lambda_{24}$ has order 64. The embedding uses the octonionic multiplication: the triality structure of $D_4 \subset E_8$ (arising from $\mathbb{H} \subset \mathbb{O}$) interleaves the three $E_8$ components to select the Leech sublattice. The embedding is not unique — there are multiple index-64 sublattices of $E_8^3$ isometric to $\sqrt{2}\Lambda_{24}$, related by $\mathrm{Aut}(E_8^3) = W(E_8)^3 \rtimes S_3$.

**Note on previous notation.** Prior notes ("off-diagonal sector contains $\Lambda_{24}$") are imprecise: what is contained is $\sqrt{2}\Lambda_{24}$ (Leech at scale $\sqrt{2}$), an index-64 sublattice of $E_8^3$. In the Jordan trace inner product (which rescales the off-diagonal sector by $\sqrt{2}$ to give $\sqrt{2}E_8^3$ with min norm 4), one instead says $\Lambda_{24} \subset \sqrt{2}E_8^3$ of index 64 — both formulations describe the same geometry.

**Fixing a canonical embedding.** A canonical choice of $\sqrt{2}\Lambda_{24} \subset E_8^3$ is equivalent to fixing a triality frame: a choice of $D_4 \subset E_8$ compatible with the octonionic structure, plus a triality automorphism $\tau$ of order 3 acting on the three $E_8$ components. The $u$-selection fixes a quaternionic plane $\mathbb{H} \subset \mathbb{O}$ (Hurwitz quaternions), which specifies $D_4 \subset E_8$. However, fixing $\mathbb{H}$ does not fix $\tau$ uniquely — a residual $SU(2)$ ambiguity remains from $u^\perp \cap \mathbb{H}$. The triality frame is fully fixed only after the Furey-Hughes step that selects the electroweak $\mathbb{H}$ direction.

---

### Part 2: Equivariance Under $SU(3)$

**Continuous equivariance is ill-posed.** $SU(3)$ is a connected Lie group acting continuously on $\mathbb{R}^{24}$ via $(X,Y,Z) \mapsto (g(X), g(Y), g(Z))$. The orbit of any point in the discrete lattice $\sqrt{2}\Lambda_{24}$ under this action is a connected submanifold of $\mathbb{R}^{24}$. A non-trivial connected orbit cannot be discrete. Therefore:

- A continuous connected group preserves a discrete set only if it acts trivially on that set.
- $SU(3)$ acts faithfully on $\mathbb{O}$, hence non-trivially on $E_8^3$.
- **Continuous $SU(3)$ equivariance of $\sqrt{2}\Lambda_{24}$ is impossible by topology, not merely unverified.**

The failure condition in [0 - master.md](0%20-%20master.md) — "no equivariant embedding under the residual $SU(3)$ can be constructed" — must be read as referring to **discrete equivariance**.

**The correct question.** Define:
$$G_2(\mathbb{Z}) := G_2 \cap \mathrm{Aut}(E_8^3) \subset SO(24)$$
the finite subgroup of $G_2$ that preserves the integral lattice $E_8^3$. The relevant symmetry is $SU(3)_{\mathrm{disc}} := SU(3) \cap G_2(\mathbb{Z})$ — the discrete $u$-stabilizer subgroup compatible with the lattice structure.

**Equivariance of the canonical embedding.** The Baez/Egan embedding is constructed from the ring structure of $\mathbb{O}_\mathbb{Z}$ (via octonionic multiplication and the triality from $\mathbb{H} \subset \mathbb{O}$). Any $g \in G_2(\mathbb{Z})$ is an automorphism of $\mathbb{O}_\mathbb{Z}$ as a ring; it therefore maps the Baez/Egan Leech sublattice to another Baez/Egan Leech sublattice (the one defined by the frame $g(\mathbb{H})$). Restricting to $SU(3)_{\mathrm{disc}}$ (elements that additionally fix $u$): these map $\mathbb{H}$ to another quaternionic plane in $u^\perp$. The specific Leech sublattice $\sqrt{2}\Lambda_{24}$ is preserved if and only if the triality frame is also preserved, i.e., if the $SU(2)$ ambiguity in $\mathbb{H}$ is fixed.

**Conclusion for Part 2:** Discrete equivariance holds in the following sense: the Baez/Egan construction is $G_2(\mathbb{Z})$-natural (it uses only ring structure), so $G_2(\mathbb{Z})$ permutes the set of canonical Leech sublattices. The specific sublattice $\sqrt{2}\Lambda_{24}$ is preserved by those elements of $SU(3)_{\mathrm{disc}}$ that also fix the triality frame. Fixing the frame requires the additional Furey-Hughes $\mathbb{H}$-selection step. **Discrete $SU(3)$ equivariance is conditional on a fixed triality frame; with that frame fixed, it holds.**

---

### Part 3: Jordan Product $D \circ U$ — Preservation Check

**Explicit computation.** For diagonal $D = \mathrm{diag}(d_1, d_2, d_3)$ with $d_i \in \mathbb{R}$ and off-diagonal $U = (X,Y,Z) \in \mathbb{O}^3$:

$$(DU)_{ij} = d_i U_{ij}, \qquad (UD)_{ij} = U_{ij} d_j$$

(real scalars commute with octonions, and $D$ is diagonal). Therefore:

$$D \circ U = \tfrac{1}{2}(DU + UD), \qquad (D \circ U)_{ij} = \tfrac{d_i + d_j}{2}\, U_{ij}$$

The Jordan product maps $(X, Y, Z) \mapsto (\lambda_{12} X,\, \lambda_{13} Y,\, \lambda_{23} Z)$ with scaling factors

$$\lambda_{12} = \tfrac{d_1+d_2}{2}, \quad \lambda_{13} = \tfrac{d_1+d_3}{2}, \quad \lambda_{23} = \tfrac{d_2+d_3}{2}$$

**Integrality.** For $D \circ U \in \mathbb{O}_\mathbb{Z}^3$ when $U \in \mathbb{O}_\mathbb{Z}^3$: need $\lambda_{ij} \in \mathbb{Z}$, i.e., all $d_i$ the same parity.

**Preservation of $\sqrt{2}\Lambda_{24}$.** For $(D \circ U) \in \sqrt{2}\Lambda_{24}$ whenever $U \in \sqrt{2}\Lambda_{24}$, the map $(\lambda_{12}, \lambda_{13}, \lambda_{23})$ must lie in $\mathrm{Aut}(\sqrt{2}\Lambda_{24}) \cong 2 \cdot Co_1$. Since $2 \cdot Co_1$ is finite, all its elements are isometries: $|\lambda_{ij}| = 1$ for all pairs is necessary. This requires $d_i + d_j = \pm 2$ for all $i \neq j$.

Solving the system $d_i + d_j = \varepsilon_{ij} \cdot 2$ ($\varepsilon_{ij} \in \{\pm 1\}$) over all pairs:

| $(\varepsilon_{12}, \varepsilon_{13}, \varepsilon_{23})$ | $(d_1,d_2,d_3)$ | Map | Preserves $\sqrt{2}\Lambda_{24}$? |
|---|---|---|---|
| $(+,+,+)$ | $(1,1,1)$ | Identity $U \mapsto U$ | Yes ✓ |
| $(-,-,-)$ | $(-1,-1,-1)$ | Negation $U \mapsto -U$ | Yes ✓ |
| Mixed signs | e.g. $(1,1,-3)$, non-$\pm 1$ entries | Non-isometric | No ✗ |

For mixed-sign cases, e.g. $(\varepsilon_{12},\varepsilon_{13},\varepsilon_{23}) = (+,-,-)$: solving gives $(d_1,d_2,d_3) = (1,-1,-3)$ and $\lambda_{23} = -2 \neq \pm 1$. Not an isometry.

The only consistent solutions with all $d_i = \pm 1$ are $d_1=d_2=d_3=\pm 1$.

**Conclusion for Part 3.** The Jordan product $D \circ U$ maps $\sqrt{2}\Lambda_{24}$ to itself **only** when $D = \pm I$. For any other snap state $(d_1,d_2,d_3) \neq (\pm 1, \pm 1, \pm 1)$ with all entries equal, the map scales the three $E_8$ components by different or non-unit factors, producing a vector in $E_8^3 \setminus \sqrt{2}\Lambda_{24}$. **The snap coupling $D \circ U$ generically exits the Leech tier.**

---

### Physical Interpretation of the Jordan Product Result

The failure of $D \circ U$ to preserve $\sqrt{2}\Lambda_{24}$ is structurally significant:

**Reading A — wrong coupling law.** The Jordan product is natural to $J_3(\mathbb{O})$ but not to the Leech tier. The correct coupling $\Gamma: \mathbb{R}^3 \to \mathrm{End}(\mathbb{O}^3)$ requires a Leech-projecting modification, e.g. $\Pi \circ (D \circ U)$ where $\Pi$ is a projection onto $\sqrt{2}\Lambda_{24}$. This would require specifying $\Pi$ non-trivially.

**Reading B — tier-transition coupling.** The snap coupling is not supposed to preserve the Leech tier; its job is to couple the passive tier to the active sector. The image $D \circ U \in E_8^3$ lies in one of the 64 cosets of $\sqrt{2}\Lambda_{24}$ in $E_8^3$. The index-64 quotient $E_8^3/\sqrt{2}\Lambda_{24} \cong (\mathbb{Z}/2)^6$ encodes the 64 "activated states" above the Leech floor. The snap coordinate $D$ selects which coset class the coupling lands in — a $2^6$-valued observable. Reading B is more compatible with the two-sector ontology: the Leech tier is ground-floor and $D \circ U$ defines a coupling into the quotient. The number 64 may have further structure (e.g., $64 = 2^6$, the weight-8 Golay codewords, the minimum weight of $\mathcal{G}_{24}$).

Reading B is structurally preferable because it does not require a modification of the Jordan product and turns the failure of preservation into a positive feature (the structure of the activated sector is determined by the Leech/E8 geometry).

---

### Part 4: Index-64 Quotient Structure

**Theorem.** $E_8^3/\sqrt{2}\Lambda_{24} \cong (\mathbb{Z}/2)^6$.

*Proof.* Since $\sqrt{2}\Lambda_{24} \subset E_8^3$ and both are even unimodular of rank 24, dualizing the inclusion reverses it: $(E_8^3)^* \subset (\sqrt{2}\Lambda_{24})^*$, i.e., $E_8^3 \subset \tfrac{1}{\sqrt{2}}\Lambda_{24}$ (using $E_8^{3*} = E_8^3$ and $(\sqrt{2}\Lambda_{24})^* = \tfrac{1}{\sqrt{2}}\Lambda_{24}^* = \tfrac{1}{\sqrt{2}}\Lambda_{24}$). Therefore $2v \in \sqrt{2}\Lambda_{24}$ for every $v \in E_8^3$. Every element of the quotient has order $\leq 2$. A group of order $2^6$ killed by 2 is $(\mathbb{Z}/2)^6$. ☐

**Chain structure.** The duality argument gives the three-step chain
$$\sqrt{2}\Lambda_{24} \;\subset\; E_8^3 \;\subset\; \tfrac{1}{\sqrt{2}}\Lambda_{24}$$
with $[E_8^3 : \sqrt{2}\Lambda_{24}] = 2^6$ and $[\tfrac{1}{\sqrt{2}}\Lambda_{24} : E_8^3] = 2^6$ (both equal by symmetry of the unimodular case). $E_8^3$ sits precisely at the midpoint of the scale-2 Leech chain. This is the lattice analogue of a self-dual code sitting midway in a glue tower.

**Hexacode identification (structural).** The MOG (Miracle Octad Generator) construction of $\Lambda_{24}$ organizes $\mathbb{R}^{24}$ as a $4\times 6$ array. The *hexacode* $\mathcal{H}_6$ is a $[6,3,4]_{\mathbb{F}_4}$ linear code with $4^3 = 64$ codewords. As an additive group, $\mathcal{H}_6 \cong (\mathbb{F}_4,+)^3 \cong (\mathbb{Z}/2)^6$. In the MOG construction, a vector $(x,y,z)\in E_8^3$ belongs to $\sqrt{2}\Lambda_{24}$ iff its MOG coordinate satisfies the zero hexacodeword condition; the other 63 cosets correspond bijectively to the 63 non-zero elements of $\mathcal{H}_6$. This identifies

$$E_8^3/\sqrt{2}\Lambda_{24} \;\cong\; \mathcal{H}_6 \;\cong\; (\mathbb{Z}/2)^6$$

as additive groups. **Status: the abstract group isomorphism $\cong(\mathbb{Z}/2)^6$ is a theorem (above). The explicit identification of coset labels with hexacode codewords is structurally established via the MOG; writing it as an explicit coset-to-codeword bijection requires fixing the MOG frame, which is precisely the triality frame of §4b.**

**$S_3$ symmetry.** The three $E_8$ factors of $E_8^3$ are permuted by $S_3 \cong \mathrm{Aut}(D_4)/\mathrm{Inn}(D_4)$. The hexacode group $(\mathbb{F}_4)^3$ is permuted by $S_3$ acting on the three $\mathbb{F}_4$ coordinates. These actions are compatible: the $S_3$ symmetry of $E_8^3$ acts on the quotient $(\mathbb{Z}/2)^6 \cong (\mathbb{F}_4)^3$ by permuting the three $\mathbb{F}_4$ factors, each of which contributes exactly 2 bits (one $\mathbb{F}_4 \cong (\mathbb{Z}/2)^2$ per $E_8$ component). This is the "2 bits per $E_8$ factor" structure.

**Golay-admissibility.** The hexacode has minimum distance 4: every non-zero codeword has weight $\geq 4$, meaning it is supported on $\geq 4$ of the 6 hexacode positions. In the MOG layout, each hexacode position corresponds to one column of 4 rows; weight $\geq 4$ activates $\geq 4$ columns. A weight-4 hexacodeword activates exactly $4 \times 2 = 8$ of the 24 $E_8^3$-coordinate directions — matching the Golay minimum weight 8. Therefore:

- **Coset 0** (the Leech ground state) is the unique coset with weight 0.
- **All 63 non-zero cosets** have hexacode weight $\geq 4$, meaning any deviation from the Leech tier must touch $\geq 8$ coordinates.
- There are **no weight-1, 2, or 3 cosets**: "small" local deviations from the Leech tier are not admissible coset labels. This is the mathematical formulation of the error-correcting floor — the Golay minimum-weight constraint operates directly on the coset structure.

**Snap coupling coset landing.** The Jordan product $D \circ U$ for $D = \mathrm{diag}(d_1,d_2,d_3)$ maps $U = (X,Y,Z) \in \sqrt{2}\Lambda_{24}$ to the coset labeled by $(\lambda_{12} \bmod \mathbb{F}_4,\, \lambda_{13} \bmod \mathbb{F}_4,\, \lambda_{23} \bmod \mathbb{F}_4) \in (\mathbb{F}_4)^3$, where $\lambda_{ij} = (d_i+d_j)/2$. The coset is 0 (Leech ground state) iff $\lambda_{12} \equiv \lambda_{13} \equiv \lambda_{23} \equiv 0 \pmod{2}$, which holds iff all $d_i$ have the same parity *and* $\lambda_{ij} \in 2\mathbb{Z}$ for all pairs — satisfied exactly when $D = \pm I$. For all other snap states, $D \circ U$ lands in a non-zero coset and is Golay-admissible by the minimum-weight property above.

**Hexacode weight distribution.** The hexacode $\mathcal{H}_6$ as a $[6,3,4]_{\mathbb{F}_4}$ code (equivalently a 3-dimensional $\mathbb{F}_4$-vector space) has weight enumerator $A_0 = 1$, $A_4 = 45$, $A_6 = 18$ (total: 64 ✓). Among the 63 non-zero cosets: **45 are weight-4 (octad-type, 71%)** and **18 are weight-6 (hexad-type, 29%)**. This can be verified from the systematic generator matrix: messages with exactly one or two non-zero components always give weight-4 codewords (36 of them); messages with all three components non-zero split 9 weight-4 and 18 weight-6.

**What the snap state $D$ determines.** The Jordan product $D \circ U$ with $D = \mathrm{diag}(d_1, d_2, d_3)$ maps the coset label in $(\mathbb{Z}/2)^6 \cong (\mathbb{F}_4)^3$ to $(\lambda_{12} \bmod \mathbb{F}_4, \lambda_{13} \bmod \mathbb{F}_4, \lambda_{23} \bmod \mathbb{F}_4)$. However, the hexacode weight is a property of the 6-dimensional codeword $c \in \mathcal{H}_6 \subset \mathbb{F}_4^6$, not the 3-dimensional information vector $(m_1, m_2, m_3) \in \mathbb{F}_4^3$. The weight depends on the generator matrix $G$, which encodes the MOG frame (= the triality frame from §4b).

**What is and is not determined by $D$ alone.** The snap state $D$ contributes the "inter-block" coset data: the 3 parities $(\lambda_{12} \bmod 2, \lambda_{13} \bmod 2, \lambda_{23} \bmod 2) \in \{0,1\}^3$, which are a function of $d_i \bmod 4$. The remaining 3 bits (intra-block, one per $E_8$ factor) come from the specific element $U \in \sqrt{2}\Lambda_{24}$ and depend on how $U$ is positioned within its $E_8$ block. Therefore **the hexacode weight of the coset is NOT determined by $D$ alone** — it also depends on $U$.

**Consequence for the snap coupling.** For a given snap state $D \neq \pm I$, the coset type (octad vs hexad) varies across different $U \in \sqrt{2}\Lambda_{24}$. The snap coupling $D \circ U$ samples different cosets as $U$ varies over the Leech tier. Whether the octad (weight-4) or hexad (weight-6) type is preferred depends on which $U$-values are dynamically selected — a question about the measure on the Leech tier, not on the algebra alone.

**Conclusion for item 7.** The hexacode weight cannot be determined from $D$ alone without the explicit triality frame (item 4b) fixing the MOG generator matrix. With that frame fixed: the full 6-bit coset label is computable, and for any given $(D, U)$ pair the weight-4 or weight-6 classification follows directly. The a priori probability of weight-4 vs weight-6 (assuming uniform measure on $U$) is 45:18 ≈ 71%:29%. **Open: explicit triality frame needed to give specific snap states a definite weight classification.**

**Conclusion for item 5.** The structure of the index-64 quotient is now determined:
1. $E_8^3/\sqrt{2}\Lambda_{24} \cong (\mathbb{Z}/2)^6$ — **theorem** (duality proof).
2. The 64 cosets biject with the hexacode $\mathcal{H}_6$ — **structurally established** (MOG; explicit bijection requires triality frame from §4b).
3. Golay-admissibility is automatic for all 63 non-zero cosets, with minimum activation size 8 — **established from hexacode minimum distance 4**.
4. The snap coupling $D \circ U$ lands on a non-trivial (Golay-admissible) coset for all $D \neq \pm I$ — **established from Part 3**.

The remaining open question: **does the specific coset landed on by a given snap state $D$ correspond to a weight-4 (octad) or weight-6 hexacodeword?** Weight-4 codewords (octads) are the most constrained activated states. Whether generic snap states produce octad-type or hexad-type coset labels is not yet determined.

---

## Status

| Claim | Status | Maturity |
|---|---|---|
| 24+3 split intrinsic to $J_3(\mathbb{O})$ | Established | 2 |
| $E_8^3$ contains $\sqrt{2}\Lambda_{24}$ as sublattice of index 64 | Established (determinant argument + Baez/Egan) | 2 |
| Continuous $SU(3)$ equivariance of $\sqrt{2}\Lambda_{24}$ | Impossible — topology rules it out | — |
| Discrete equivariance: $G_2(\mathbb{Z})$ permutes canonical Leech sublattices | Follows from ring-structure construction | 3 |
| Discrete equivariance: $SU(3)_\mathrm{disc}$ preserves $\sqrt{2}\Lambda_{24}$ with fixed triality frame | Holds conditionally (requires fixed $\mathbb{H}$-frame from Furey-Hughes) | 3 |
| Triality frame fixed by $u$-selection alone | No — requires Furey-Hughes $\mathbb{H}$-selection | 4 |
| Triality frame fixed by $(u\text{-selection} + \mathbb{H}\text{-selection})$ cascade | **Yes** — up to octonionic orientation (see §Triality below) | 2 |
| Jordan product $D \circ U$ preserves $\sqrt{2}\Lambda_{24}$ | **No** — only for $D = \pm I$ | 2 |
| Jordan product $D \circ U$ maps Leech tier to index-64 quotient $E_8^3/\sqrt{2}\Lambda_{24}$ | Structurally established; physical interpretation open | 3 |
| Index-64 quotient $\cong (\mathbb{Z}/2)^6$ | **Theorem** — duality proof (see Part 4) | 2 |
| Cosets $\leftrightarrow$ hexacode $\mathcal{H}_6$ codewords; Golay minimum weight 8 = min activation size | Structurally established (MOG); explicit bijection pending triality frame | 3 |
| Snap coupling $D \circ U$ lands on Golay-admissible coset for all $D \neq \pm I$ | Established from Part 3 + hexacode minimum distance | 2 |
| $\mathrm{Stab}(u) \cong SU(3)$ | Established structural fact | 3 |
| $SU(3)$ as physical QCD color with representations $\mathbf{3}, \bar{\mathbf{3}}, \mathbf{8}$ | Gap — may be permanent | 6 |

---

## Triality Frame from Furey-Hughes: Results

### The key structural fact: $G_2 = SO(8)^\tau$

The triality automorphism $\tau$ of $D_4 \cong \mathfrak{so}(8)$ is an outer automorphism of order 3. The classical theorem (Élie Cartan; see also Adams) is:

$$G_2 = SO(8)^\tau = \{g \in SO(8) : \tau \circ g = g \circ \tau\}$$

$G_2$ is precisely the **fixed-point subgroup** of the $D_4$ triality in $SO(8)$. This is why $G_2$ is the automorphism group of $\mathbb{O}$: the octonionic multiplication is the structure preserved by $\tau$-fixed isometries.

This fact has an immediate consequence for the Leech embedding: any construction of $\sqrt{2}\Lambda_{24} \subset E_8^3$ that is built from $\tau$-covariant conditions is automatically covariant under the diagonal $G_2$ action at the level of the ambient algebraic data. This does **not** by itself show that the full continuous group acts as a symmetry of the discrete integral lattice; that stronger claim is ruled out by the topology argument above.

### What $\mathbb{H}$-selection determines

**Step 1 ($u$-selection → $D_4$).** Fixing $u \in \mathrm{Im}(\mathbb{O})$ singles out the subalgebra $\mathrm{span}(1, u) \cong \mathbb{C} \subset \mathbb{O}$. The stabilizer $\mathrm{Stab}(u) = SU(3) \subset G_2$ and $u^\perp \cong \mathbb{C}^3$.

This does not yet determine $\mathbb{H}$. There is a residual $SU(2)$ freedom: the set of quaternionic subalgebras $\mathbb{H} \ni u$ forms a 2-sphere $S^2 \cong SU(3)/U(2)$ within $u^\perp$.

**Step 2 ($\mathbb{H}$-selection → $D_4 \subset E_8$).** Fixing $\mathbb{H} \subset \mathbb{O}$ (with $u \in \mathbb{H}$) determines the Cayley-Dickson decomposition $\mathbb{O} = \mathbb{H} \oplus \mathbb{H}\ell$ for a unit $\ell \perp \mathbb{H}$. The Hurwitz quaternion sublattice $\mathbb{H}_\mathbb{Z} \subset \mathbb{O}_\mathbb{Z}$ is then a specific rank-4 sublattice of $E_8$, isometric to $D_4^+$ (the $F_4$ root lattice, or equivalently $D_4$ with minimum norm 1 before rescaling to match $E_8$'s normalization).

The $D_4$ sublattice of $E_8$ is fixed by $\mathbb{H}$, and the $D_4$ Dynkin diagram carries a canonical order-3 symmetry (the triality $\tau$) that extends uniquely (up to inversion) to an automorphism of $E_8$.

**Step 3 (octonionic orientation → uniqueness of $\tau$).** The extension of $D_4$-triality to $E_8$-triality has a residual $\mathbb{Z}/2$ ambiguity: $\tau$ vs $\tau^{-1} = \tau^2$. These correspond to swapping two of the three $\tau$-orbits of $D_4$ representations, equivalently swapping the two spinor representations $S^+, S^-$ of $\mathfrak{so}(8)$ while fixing the vector $V$.

This ambiguity is resolved by the orientation of $\mathbb{O}$. The octonionic multiplication table specifies a particular orientation of $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$ (via the associative 3-form $\phi(x,y,z) = \langle x, yz \rangle$). This orientation, together with the choice of $u$ and $\mathbb{H}$, gives an ordered frame $(u, v, w, uv, uw, vw, uvw)$ in $\mathrm{Im}(\mathbb{O})$ that distinguishes $\tau$ from $\tau^{-1}$.

**Conclusion for item 4b:** The two-step cascade $(u\text{-selection}) + (\mathbb{H}\text{-selection})$, with the octonionic orientation fixed by the multiplication table, **fully determines the triality frame** and hence the canonical Leech sublattice $\sqrt{2}\Lambda_{24} \subset E_8^3$. No further free choices are required.

### The cascade encodes two structures simultaneously

The physical interpretation: the same cascade that forces the SM Higgs doublet also fixes the Leech ground state.

| Cascade step | SM/gauge consequence | Leech consequence |
|---|---|---|
| $u$ selected in $\mathrm{Im}(\mathbb{O})$ | $G_2 \to SU(3)$; color structure | $u^\perp$ as active sector; $\mathbb{H}$-family parameterized by $S^2$ |
| $\mathbb{H} \subset u^\perp$ selected | $SU(3) \to SU(2)_L$; Higgs doublet | $D_4 \subset E_8$ fixed; triality $\tau$ determined up to $\mathbb{Z}/2$ |
| Orientation of $\mathbb{O}$ (fixed) | Chirality (left vs right $SU(2)$) | $\tau$ vs $\tau^{-1}$ resolved; canonical $\sqrt{2}\Lambda_{24} \subset E_8^3$ fixed |

The program's cascade is therefore **doubly canonical**: each step has a SM interpretation and a Leech/global-state-space interpretation, both forced by the same algebraic choice.

Clarification: the triality-based argument here is about covariance of the *ambient algebraic construction*. It should not be read as overturning Part 2's topology result. A connected continuous group still cannot act nontrivially as a literal symmetry of a discrete integral lattice; the actual lattice symmetry remains the discrete subgroup compatible with the fixed triality frame.

### Equivariance - clarified statement

Using $G_2 = SO(8)^\tau$ and the fact that the Leech sublattice is defined by $\tau$-covariant conditions, the most defensible conclusion is this: the canonical Leech embedding is $G_2$-covariant at the level of the ambient algebraic data. That explains why the discrete subgroup $G_2(\mathbb{Z})$ acts naturally on the integral construction once the triality frame is fixed. It should not be read as a literal continuous symmetry of the discrete lattice itself; at the lattice level, the actual symmetry remains the discrete subgroup compatible with the fixed triality frame.
