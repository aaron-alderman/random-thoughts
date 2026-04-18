# Next Best Targets

This file collects concrete next-step tasks that are ready to be worked — computations, derivations, or drafts that are well enough specified to begin immediately. Items here are Spin(2,3)-specific and have not yet been absorbed into a kernel file.

---

## T3 — DIII d=3 Winding Number (from topological work)

The corrected topological picture is:

- $m=0$: class DIII ($T_0^2=-1$, $C^2=+1$, $\Sigma = CT_0$), $d=3$ invariant $\mathbb{Z}$
- $m\neq 0$: class D ($T_0^2=-1$, $C^2=+1$, $\Sigma$ broken)
- Two independent $T^2=-1$ operators ($T_0$, $T_{01}$) → possible 16-fold way structure

The highest-value open target is T3: compute the DIII $d=3$ winding number $W_3$ in terms of the Spin(2,3) data and determine what integer it equals. The computation is explicit:

$$W_3 = \frac{1}{24\pi^2} \int_{S^3} \mathrm{tr}\left[(Q\,dQ)^3\right]$$

where $Q$ is the flat-band matrix constructed from the eigenvectors of $H$ at $m=0$. In the Spin(2,3) framework, $H$ at $m=0$ is block-diagonal in T1/T2, and $Q$ is built from the $\Sigma$-grading. The question is whether $W_3$ evaluates to an integer with physical meaning — and the most interesting possibility is $W_3 = 3$ (generations).

If $W_3 = 3$, the topological structure connects directly to the generation count — the most productive convergence the framework could hope for.

**Priority order among T-tasks:**
1. T3 (winding number → observables/generations): highest-value
2. T4 (anomaly inflow from DIII bulk): medium-value
3. T2 (material realization): lower priority

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

## Paper II Outline — Spin(2,3) Representations

Paper I (the two-branch transport classification) is complete as a dynamical statement. Paper II would develop the representation theory side:

**Scope:**
1. Full irrep classification of $\mathrm{Spin}(2,3) \cong \mathrm{Sp}(4,\mathbb{R})$ relevant to the transport slice — including the metaplectic (half-integer) representations
2. Identification of which irreps correspond to which transport class (Constructive ↔ which irrep? Inverted ↔ which?)
3. Metaplectic representation as the natural quantum structure for the two-branch amplitude pair
4. Connection to AdS₄/CFT₃ if the SO(2,3) structure is interpreted geometrically
5. The $G_2 \cap \mathrm{Spin}(2,3)$ calculation and its irrep content — this is the phenomenological bridge

**Concrete first step for Paper II:**
Classify the lowest-dimensional unitary irreps of $\mathrm{Sp}(4,\mathbb{R})$ and identify which ones admit the locking condition $|\omega| \leq |\kappa_u|\cosh(2\rho)$ at their natural $\omega$ and $\kappa_u$ values.

**Key open input:**
The $G_2 \cap \mathrm{Spin}(2,3)$ computation (see open problems ledger). If this intersection contains structure analogous to $SU(3) \times SU(2) \times U(1)$, Paper II becomes a phenomenological paper. If not, it is still a clean representation-theory paper.
