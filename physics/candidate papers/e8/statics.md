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

## Open: Leech Equivariance Check

The Baez/Egan result establishes that the Leech sublattice lives in the off-diagonal sector. What remains:

- Fix a specific embedding (there may be multiple non-equivalent ones, related by the Conway group $Co_0$)
- Check whether that embedding is equivariant under the $SU(3)$ action induced by $u$-selection
- Check whether the Jordan product $D \circ U$ preserves the Leech sublattice

If the equivariant embedding exists, the snap coupling becomes a theorem rather than an interpretation. If no equivariant embedding exists, the Leech structure and color structure are in tension — which is important information either way.

## Status

| Claim | Status | Maturity |
|---|---|---|
| 24+3 split intrinsic to $J_3(\mathbb{O})$ | Established | 2 |
| Off-diagonal sector contains $\Lambda_{24}$ (Baez/Egan) | Established | 3 |
| Leech embedding equivariant under $SU(3)$ | Unknown — key calculation | 4 |
| Jordan product $D \circ U$ preserves $\Lambda_{24}$ | Unverified | 4 |
| $\mathrm{Stab}(u) \cong SU(3)$ | Established structural fact | 3 |
| $SU(3)$ as physical QCD color with representations $\mathbf{3}, \bar{\mathbf{3}}, \mathbf{8}$ | Gap — may be permanent | 6 |
