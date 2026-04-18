# Next Best Targets

This file collects concrete next-step tasks that are ready to be worked - computations, derivations, or drafts that are well enough specified to begin immediately. Items here are Spin(2,3)-specific and have not yet been absorbed into a kernel file.

---

## T6 - Ambient-to-Observable Reduction

The single highest-value structural task is now to make the missing middle explicit: how the parent octonionic geometry reduces to the effective `Spin(2,3)` branch and then to the observable `T1` channel.

This task now has a dedicated scaffold note:

- `0d - ambient reduction scaffold.md`

The current best reduction chain is:

$$
\mathbb{O}
\supset
\mathbf{R}u \oplus u^\perp
\cong
\mathbf{R}u \oplus \mathbf{C}^3
\supset
H_{\mathrm{loc}}
\rightsquigarrow
\text{hidden complex plane}
\rightsquigarrow
\text{effective two-sector branch}
\rightsquigarrow
\mathrm{Spin}(2,3)
\rightsquigarrow
(T1,T2)
\rightsquigarrow
\text{observable } T1.
$$

The important point is that the current `T1/T2` split should be treated as a reduced output, not as an unexplained primitive.

**Immediate subproblems:**
- `R1`: show how a local quaternionic `H` slice sits inside `u^\perp` and carries the relevant complex plane
- `R2`: formalize the folding map from the exploratory `Spin(3,3)` lift into hidden complex-plane data
- `R3`: derive the effective `J^{01}` grading and two-sector branch from that folded structure
- `R4`: only then address why the observable channel should be `T1`

**Why this matters:**
- it is the bridge joining the parent inquiry map to the kernel files
- it sharpens the input to the bulk derivation problem in `2b`
- it prevents the epistemic story from floating free of the reduction story

---

## T3 - DIII d=3 Winding Number (from topological work)

The winding-number computation has now been carried out for the natural **gapped chiral DIII extension** built from the `Spin(2,3)` Clifford frame. The result is:

- with the orientation and sign conventions used in the current draft, $W_3 = -1$
- reversing orientation, or replacing $q$ by $q^\dagger$, flips the sign
- the robust statement is therefore $|W_3| = 1$

This is a stronger and cleaner result than the earlier open guesswork, but it also changes the interpretation. The invariant belongs to the **gapped chiral family on $S^3$**, not to the strictly gapless massless point by itself. The massless sector is best read as the equatorial critical slice separating opposite-sign gapped phases.

So the old speculative possibility $W_3 = 3$ is **not** supported by the natural first computation. At present, the topological result gives a nontrivial unit winding, not a generation count.

The corresponding integral is

$$W_3 = \frac{1}{24\pi^2} \int_{S^3} \mathrm{tr}\left[(Q\,dQ)^3\right],$$

with $Q$ the flattened chiral Hamiltonian on $S^3$ and, in chiral basis, off-diagonal block
$$q(X) = X_0 \mathbf{1}_2 - i(X_1\sigma^1 + X_2\sigma^2 + X_3\sigma^3).$$

**Updated priority order among T-tasks:**
1. T4 (anomaly inflow from the DIII bulk): highest-value next topological target
2. T2/T3 bridge question: identify what observable, if any, measures the unit winding in the Spin(2,3) setting
3. T2 (material realization): lower priority until a cleaner physical Hamiltonian story exists

---

## T5 - Hydrogen Threshold Symmetry and Efimov Bridge

There is now a plausible structural bridge between the two-boundary transport classification and the known compact/noncompact symmetry split of the hydrogen problem:

- constructive locked/persistent sector as the compact, bound-side analogue
- persistence boundary as the marginal threshold surface
- dephased side as the noncompact, scattering-side analogue

The stronger extension is the Efimov bridge: on the free/dephased side, `SO(3,1) \supset SO(2,1)` suggests conformal near-threshold dynamics for three-body states. If the bridge is real, the Efimov exponent should be controlled by a threshold Casimir and therefore by a dimensionless combination of transport parameters such as `\omega/\kappa_u`.

**What to compute:**
- identify the precise subgroup chain from `Spin(2,3)` to the threshold `SO(4)` sector and then to the free-side `SO(3,1)` sector
- determine whether the persistence boundary should be read as the analogue of the hydrogen ionization threshold or only as its transport-space image
- derive the effective near-threshold radial generator from `\dot{R} = R(-\gamma + \kappa_u\cosh(2\rho)\cos\Phi)` and check whether it closes with dilation and special-conformal generators into `so(2,1)`
- compute the relevant quadratic Casimir in terms of transport variables and test whether the Efimov constant `s_0` can be expressed as a function of `\omega/\kappa_u` at threshold
- decide whether the result is genuinely predictive or only a structural analogy

**Why this matters:**
- a positive result would be the first concrete bridge from the transport classification to a known nontrivial few-body scaling law
- a negative result would still be valuable, because it would sharply separate the hydrogen-threshold analogy from the Efimov claim instead of letting them travel together

---

## Phase Portrait Diagram

The $(\rho, \Phi)$ phase portrait of the two-branch transport system needs to be rendered explicitly, showing:

- The locking boundary $|\omega| = |\kappa_u|\cosh(2\rho)$ as a curve
- The persistence boundary $\mathcal{O}\cosh(2\rho) = \gamma$ as a second curve
- The four transport class regions labeled (Constructive, Inverted, Frustrated, Dephased)
- Branch 1 fixed points (symmetric, $\rho^* = 0$) as stable/unstable nodes
- Branch 2 fixed points (complementary, $\cos\Phi^* = 0$) as centers
- Flow arrows in each region

For a specific representative parameter set (e.g. $\kappa_u = 1$, $\omega = 0.5$, $\gamma = 0.3$), the locking boundary and persistence boundary intersect, and the four regions become visible. The diagram makes the classification theorem visually transparent and is required for any publication on the two-branch system.

**What to compute:**
- Fix $\kappa_u, \omega, \gamma$ and plot $(\rho, \Phi) \in [-2,2] \times [0, 2\pi]$
- Locking curve: $\cosh(2\rho) = |\omega/\kappa_u|$, a constant-$|\rho|$ pair of lines
- Persistence curve: $\kappa_u\cos\Phi = \gamma/\cosh(2\rho)$, a $\rho$-dependent $\Phi$-band
- Fixed points at intersections of $\dot{\rho}=0$ and $\dot{\Phi}=0$ loci

---

## Paper II Outline - Spin(2,3) Representations

Paper I (the two-branch transport classification) is complete as a dynamical statement. Paper II would develop the representation theory side:

**Scope:**
1. Full irrep classification of $\mathrm{Spin}(2,3) \cong \mathrm{Sp}(4,\mathbb{R})$ relevant to the transport slice - including the metaplectic (half-integer) representations
2. Identification of which irreps correspond to which transport class (Constructive <-> which irrep? Inverted <-> which?)
3. Metaplectic representation as the natural quantum structure for the two-branch amplitude pair
4. Connection to AdS4/CFT3 if the SO(2,3) structure is interpreted geometrically
5. The $G_2 \cap \mathrm{Spin}(2,3)$ calculation and its irrep content - this is the phenomenological bridge

**Concrete first step for Paper II:**
Classify the lowest-dimensional unitary irreps of $\mathrm{Sp}(4,\mathbb{R})$ and identify which ones admit the locking condition $|\omega| \leq |\kappa_u|\cosh(2\rho)$ at their natural $\omega$ and $\kappa_u$ values.

**Key open input:**
The $G_2 \cap \mathrm{Spin}(2,3)$ computation (see open problems ledger). If this intersection contains structure analogous to $SU(3) \times SU(2) \times U(1)$, Paper II becomes a phenomenological paper. If not, it is still a clean representation-theory paper.
