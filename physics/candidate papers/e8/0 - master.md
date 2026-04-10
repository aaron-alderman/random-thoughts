# The Constraint-First Program: Master Map

For the reusable generic framework taxonomy, see `00 - meta framework.md`.

---

## One-Sentence Spine

The universe is a globally constrained system whose observable physics emerges from a cascade of scale-fixing reductions, each algebraically forced by the exceptional structures that house them, with the Standard Model as the locally visible slice of a rootless, error-corrected global state space.

### Working operational form

Start from `Spin(2,3)`, the octonions, and `J3(O)`; select the octonionic direction aligned with the channel of massless traversal; let that alignment define the effective observable sector; then ask how massive couplings depart from pure `T1` propagation and what representation structure, reduced dynamics, and interpretation follow.

---

## The Reduction Chain

$$E_8 \to E_6 \to J_3(\mathbb{O}) \to G_2 \to SO(2,4) \to Spin(2,3)$$

The chain is proposed to be driven by a **single** octonionic direction selection $u \in \mathrm{Im}(\mathbb{O})$ that propagates forced consequences through every level simultaneously.

**Note on arrow types:** The chain mixes two kinds of arrows. $E_8 \to E_6$ and $G_2 \to SO(2,4) \to Spin(2,3)$ are group-to-group reductions. $E_6 \to J_3(\mathbb{O})$ passes from a group to its representation space. $J_3(\mathbb{O}) \to G_2$ passes back from an algebra to a distinguished subgroup of its automorphism group ($G_2 \subset F_4 = \mathrm{Aut}(J_3(\mathbb{O}))$). The chain is a path through an interlocking mathematical structure, not a single uniform tower of quotients.

### Chain summary

| Arrow | Operation | Maturity |
|---|---|---|
| $E_8 \to E_6$ | Subgroup restriction; $SU(3)$ quotient residue | 4 |
| $E_6 \to J_3(\mathbb{O})$ | Act on natural 27-dim representation (canonical, bidirectional) | 2 |
| $J_3(\mathbb{O}) \to G_2$ | Restrict to octonionic automorphism subgroup; $F_4 \supset G_2$ embedding | 3 |
| $G_2 \to SO(2,4)$ | $G_2^{\text{split}}$ acts on split-octonionic cone → 15-parameter conformal group (Gogberashvili 2016); $u$-invariant via $\mathbb{O}_\mathbb{C}$ | 3 |
| $SO(2,4) \to Spin(2,3)$ | Fix vector $u$; simply-connected double cover | 3–4 |

---

## The Central Claim

If the chain is driven by a single selected octonionic direction $u$ propagating through every arrow:

- $u$ breaks $G_2 \to SU(3)$ — fixes color symmetry
- $u$ fixes the vector in $SO(2,4) \to Spin(2,3)$ — kills dilatation, fixes scale
- $u$ defines the $T1$ observable channel — fixes epistemics
- $u$ acts as time anchor in $Spin(2,3)$ — fixes dynamics
- $u$ selects a quaternionic slice $\mathbb{H} \subset \mathbb{O}$ — forces the Higgs doublet

Then the program's target theorem is:

> **A single octonionic direction selection propagates through the exceptional chain $E_8 \to E_6 \to J_3(\mathbb{O}) \to G_2 \to SO(2,4) \to Spin(2,3)$, forcing color symmetry, scale fixing, spinor structure, the observable channel, and the electroweak breaking structure simultaneously. The Standard Model is the local visible consequence of that one choice.**

---

## File Index

| File | Contents |
|---|---|
| [why-e8.md](why-e8.md) | Self-consistency argument for E₈ as starting point; full duality map across the chain |
| [chain/e8-e6.md](chain/e8-e6.md) | $E_8 \to E_6$ arrow; note on the two SU(3)'s |
| [chain/e6-j3.md](chain/e6-j3.md) | $E_6 \to J_3(\mathbb{O})$ arrow; real form gap |
| [chain/j3-g2.md](chain/j3-g2.md) | $J_3(\mathbb{O}) \to G_2$ arrow; $\sqrt{3}$ ratio; Leech connection |
| [chain/g2-so24.md](chain/g2-so24.md) | $G_2 \to SO(2,4)$ arrow; compact/split duality; $G_2(\mathbb{C})$ argument |
| [chain/so24-spin23.md](chain/so24-spin23.md) | $SO(2,4) \to Spin(2,3)$ arrow; same-$u$ verification; Gogberashvili check |
| [statics.md](statics.md) | Core objects; 24+3 split; two-sector ontology; snap coupling; SU(3) color gap |
| [higgs.md](higgs.md) | Quaternionic slice; Furey & Hughes matching; idempotent chain; Weinberg angle derivation |
| [dynamics.md](dynamics.md) | Coarse-graining; $\sqrt{3}$ Killing form; RG reframing; reduced dynamics |
| [epistemics.md](epistemics.md) | Observable channel; Golay snapping; Born rule question; cosmological drift |
| [phenomenology.md](phenomenology.md) | What's checkable; what's missing; full claim maturity matrix |
| [references.md](references.md) | Key papers with formulas, numerical details, community reception, open checks |

---

## Program Status

**Strong (established mathematics):**
- The 24+3 split is intrinsic to $J_3(\mathbb{O})$ and the Leech connection is established via Baez/Egan
- The $G_2$ $\sqrt{3}$ root ratio emerges from the dimension count of octonionic reduction — not chosen, forced
- The same $u$ drives all five chain roles ($G_2 \to SU(3)$ stabilizer, compact/split via $\mathbb{O}_\mathbb{C}$, Furey Cl(6) via $u^\perp$, T1 channel, spacelike image under Gogberashvili cone map) — all established
- $\sin^2\theta_W = 3/8$ is derived from the 3+2 split of $u^\perp$ with no free parameters
- $m_H = 2\cos\theta_W m_W \approx 127.1$ GeV fully derived: 1+3 split forced by $u$-selection; normalization condition $\|\Phi\|^2_Q = 3\|\Phi\|^2_L$ follows from $G_2 = \mathrm{Aut}(\mathbb{O})$ transitivity — now a theorem, not a postulate. Tree-level 1.5% residual identified as RG running from matching scale to $M_Z$; direction of correction closes the gap (needs explicit 1-loop calculation to confirm)

**Structurally established (Furey & Hughes 2022):**
- The cascade mechanism matching the $u$-selection cascade is established in arXiv:2210.10126
- The Higgs doublet emerges as the scalar component of the quaternionic triality triple — not inserted by hand
- The $u \to u^\perp \to \mathrm{Cl}(6) \to qq^\dagger$ chain is algebraically exact

**Persistent weak points:**
- $SU(3)$ as physical QCD color remains structural, not forced — may be a permanent limitation
- The Higgs vev scale $v \approx 246$ GeV is not derivable from the algebra alone
- The GUT scale: $M_X \approx 10^{13}$ GeV from SM running with $\sin^2\theta_W = 3/8$ as input; all SM embedding indices in $E_8$ are $j=1$ (computed), giving complete unification at $M_{E_8}$. Non-SUSY SM fails to unify $\alpha_3$ by 15%. The absolute scale $M_{E_8}$ and coupling $\alpha_{E_8}$ are not geometrically determined — require UV input or SUSY spectrum

---

## Next Steps (priority order)

1. ~~**Gogberashvili causal character check**~~ **Done.** $u = j_n$-type (spacelike in $\mathbb{R}^{3,4}$, stabilizer $SU(2,1)$ in split $G_2$) maps to $X^n$ (spacelike in $\mathbb{R}^{2,4}$) under the cone map $\varpi = \lambda_\|/L$, $X^n = x_n/L$. Stabilizer $SO(2,3) \to Spin(2,3)$ ✓. The de Sitter group $SO(1,4)$ appears for the timelike $J_n$/$\varpi$ direction — the wrong branch. See [chain/so24-spin23.md](chain/so24-spin23.md).

1b. ~~**$E_8$ embedding index chain**~~ **Done.** All SM gauge groups embed in $E_8$ with total index $j=1$ through the program's chain ($SU(3)_C$ via $G_2$, $SU(2)_L$ and $SU(3)_C$ via $E_6 \supset SO(10) \supset SU(5)$; $U(1)_Y$ gets the GUT factor $5/3$). Consequence: $\sin^2\theta_W = 3/8$ is forced by the $E_8$ structure automatically — the 3+2 octonionic derivation and the embedding index derivation agree. Full unification $\alpha_3 = \alpha_2 = \alpha_1$ is predicted at $M_{E_8}$; the scale itself is not fixed geometrically (non-SUSY SM gives $\sim10^{13}$ GeV with 15% non-unification of $\alpha_3$). See [higgs.md](higgs.md).

2. ~~**$m_H/m_W$ via Todorov**~~ **Done.** Derived $m_H = 2\cos\theta_W m_W$ from $u$-selection: the 1+3 split $\mathbb{O} = \mathbb{C}_u \oplus \mathbb{C}^3_{u^\perp}$ is the origin of Todorov's postulate, making the $u$-framework the common root of both $\sin^2\theta_W = 3/8$ and $m_H \approx 127.1$ GeV. Residual 1.5% gap to experiment; normalization condition not yet derived from $u$-structure. See [higgs.md](higgs.md).

3. **$\sqrt{3}$ Killing form calculation** — compute $G_2$ long/short root normalization; check whether $1/\sqrt{3}$ appears in SM coupling ratios. Half-day calculation. See [dynamics.md](dynamics.md).

4. **Leech equivariance check** — fix the Baez/Egan embedding; check equivariance under $SU(3)$ from $u$-selection; check Jordan product $D \circ U$ preserves the sublattice. See [statics.md](statics.md).

---

## Failure Conditions

The program fails if any of the following remain permanently impossible:

1. No explicit ambient-to-observable reduction map can be written with specified mathematical operations at each arrow
2. The $SU(3)$ stabilizer cannot be promoted to physical QCD color with representations $\mathbf{3}$, $\bar{\mathbf{3}}$, $\mathbf{8}$ and correct anomaly structure
3. The Jordan/Leech link remains only dimensional — no equivariant embedding under the residual $SU(3)$ can be constructed
4. No probability measure reproducing $P(i) = |\psi_i|^2$ can be defined on the Golay-admissible support
5. No geometric origin for any mass or mixing scale can be extracted from the reduction chain
6. No low-energy sector matching $SU(3)_C \times SU(2)_L \times U(1)_Y$ emerges from the reduction
7. The compact → split $G_2$ transition cannot be given a consistent treatment preserving $u$-selection throughout

## Success Conditions

The program becomes genuinely predictive when it yields one of the following:

1. **Weinberg angle at low energy:** derive the GUT scale from the octonionic geometry so that standard RG running connects $\sin^2\theta_W = 3/8$ to the measured $0.231$ at $M_Z$ without importing an external scale
2. **$m_H/m_W$ within 1%:** import Todorov's $sl(2|1)$ normalisation result into the $u$-selection framework via the quaternionic triality structure
3. A derivation of why exactly three generations are admitted and a fourth is not
4. A prediction about Born rule deviations in high-complexity entangled systems following from the Golay admissibility structure
5. A specific functional form for $T(z)$ distinguishable from $T \propto 1+z$ if the cosmological redshift-as-off-axis-drift interpretation is correct
