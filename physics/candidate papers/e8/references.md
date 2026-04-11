# Key References

Papers and their specific contributions to the program, with the mathematical details that matter for future work.

---

## Todorov — Octonion Internal Space (arXiv:2206.06912)

**Published:** Universe 9(5), 222 (2023). The octonion version of the $sl(2|1)$ Higgs mass derivation.

**What it does:** Derives $m_H = 2\cos\theta_W m_W$ from the split $\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3$ and a Quillen superconnection normalisation condition. Claims "within one percent accuracy" of experiment.

**Numerical output:**
$$m_H^\text{pred} = 2\sqrt{5/8} \times m_W = \sqrt{5/2} \times 80.377 = 127.090 \pm 0.019 \text{ GeV}$$
The $\pm 0.019$ GeV error comes purely from $\delta m_W = \pm 0.012$ GeV (PDG input). The Weinberg angle is fixed at $\sin^2\theta_W = 3/8$ (no error). Experimental: $m_H = 125.10 \pm 0.14$ GeV. Discrepancy: $1.99$ GeV $= 13.7\sigma$ in units of $\delta m_H^\text{exp}$, but only $1.6\%$ in relative terms. The paper characterises this as "within one percent" (loosely).

**Starting postulate:** $\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3$. In the $u$-framework this split is derived: $\mathbb{C} = \mathbb{C}_u$ (span of $1, u$), $\mathbb{C}^3 = u^\perp$.

**Connection to $u$-framework:** The normalization condition $\|\Phi\|^2_Q = 3\|\Phi\|^2_L$ is a theorem in the $u$-framework (follows from $G_2 = \mathrm{Aut}(\mathbb{O})$ transitivity on $\mathrm{Im}(\mathbb{O})$). See [higgs.md](higgs.md).

---

## Todorov — Superselection of Weak Hypercharge (arXiv:2010.15621)

**Published:** JHEP 04 (2021) 164. The Clifford algebra version preceding the octonion paper.

**What it does:** The earlier, more algebraically explicit paper. Derives the same $m_H/m_W$ relation. Contains the cleaner mathematical derivation of the superconnection normalisation.

**Key algebra:** Built on $Cl_4 \hat\otimes Cl_6$ — the $\mathbb{Z}_2$-graded tensor product of:
- $Cl_4$: Clifford algebra of spacetime (4 real dims), generates Lorentz/Poincaré structure
- $Cl_6$: Clifford algebra of internal space (6 real dims = $u^\perp$ in the $u$-framework)

**The idempotent:**
$$P = \frac{1}{2}(1 - i\omega_6), \qquad \omega_6 = \gamma_1\gamma_2\gamma_3\gamma_4\gamma_5\gamma_6, \quad \omega_6^2 = -1$$
where $\gamma_1,\ldots,\gamma_6$ are the $Cl_6$ generators. $P$ satisfies $P^2 = P$ and projects the full 32-dimensional Majorana spinor space of $Cl_{10}$ onto the 16-dimensional particle subspace. This idempotent uses the $Cl_6$ volume form (not a Witt decomposition product like Furey's $qq^\dagger$) — but both are derived from the same $u^\perp$ decomposition.

**Pati-Salam intermediate:** The subgroup $G_{PS} = Spin(4) \times Spin(6)/\mathbb{Z}_2$ is left-invariant by $\omega_6$. The $Cl_6$ volume form selects Pati-Salam as the maximal subgroup preserving the complex structure on $u^\perp$.

**Sterile neutrino exclusion:** The weak hypercharge $Y$ is promoted to a **superselection rule**, not merely a gauge generator. The zero eigenspace of $Y$ — which contains right-handed neutrinos (sterile neutrinos) — is excluded from the particle subspace by the $P$ projection. Sterile neutrinos are allowed to exist but are structurally outside the observable sector defined by $P$.

**The claim:** "A relation between the masses of the W boson and the Higgs that fits the experimental values within one percent accuracy" — this is the original statement of the $m_H/m_W$ result.

**Use for future work:** For a proper derivation of $\lambda = g^2\cos^2\theta_W/2$ from first principles (rather than stating it follows from the normalisation condition), this earlier paper has the explicit supertrace calculation. Priority to read if pursuing the EW-threshold correction calculation for the residual Higgs-mass gap.

---

## Todorov — Superconnection in the Spin Factor Approach (arXiv:2003.06591)

**Published:** 2020. Precursor to both papers above.

**What it does:** Develops the Quillen superconnection language for the SM more explicitly than the later papers. Likely contains the most detailed derivation of the $sl(2|1)$ curvature and the action calculation. Not yet retrieved — flagged for reading.

**The Quillen superconnection structure (from what was retrieved):**
$$\mathbb{D} = D + L$$
where $D$ is the covariant derivative (even, gauge fields) and $L$ is the Higgs field (odd). The curvature:
$$\mathbb{D}^2 = \nabla^2 + \chi[D, \Phi] + \Phi^2$$
where $\chi$ is a grading operator. The action is $\mathrm{Str}(\mathbb{D}^2 \wedge \ast \mathbb{D}^2)$. The scalar potential term comes from $\mathrm{Str}(\Phi^4) \sim \lambda|\Phi|^4$.

---

## Furey & Hughes — Division Algebraic Symmetry Breaking (arXiv:2210.10126)

**Published:** Phys. Lett. B 831 (2022) 137186.

**What it does:** Demonstrates the cascade $Spin(10) \to \text{Pati-Salam} \to \text{Left-Right} \to \text{SM} + B-L$ driven by sequential complex structure selections from $\mathbb{O}$, then $\mathbb{H}$, then $\mathbb{C}$. Derives the Higgs doublet as the scalar component $V$ of the quaternionic triality triple $(\Psi_+, \Psi_-, V)$ of $\mathrm{tri}(\mathbb{H})$.

**Key result used:** The Higgs as the scalar component of triality — not inserted by hand. The cascade mechanism of complex structure selections structurally matches the $u$-selection cascade in this program.

**Mapping (in [higgs.md](higgs.md)):** The quaternionic slice $\mathbb{H} \subset u^\perp$ in this framework corresponds exactly to the quaternionic complex structure selected second in Furey & Hughes. The $SU(2)$ residual freedom (which direction in $\mathbb{H}$ is the vev direction) corresponds to the remaining step not fixed by Furey & Hughes.

---

## Historical Context: Ne'eman & Fairlie (1979)

**Ne'eman:** Nucl. Phys. B 158 (1979) 131.
**Fairlie:** Phys. Lett. B 82 (1979) 97.

**What they did:** Independently proposed $su(2|1)$ as a superalgebra unifying $su(2)_L$ with $u(1)_Y$. The Higgs doublet sits in the odd part of the superalgebra. The original Higgs mass prediction from $su(2|1)$ is $m_H = m_Z$ (at tree level, from the Casimir condition) — this failed: $m_Z \approx 91$ GeV $\neq 125$ GeV.

**How Todorov differs:** Todorov's construction uses Quillen's superconnection (1985) rather than the original Lie-superalgebra gauge theory. The Quillen approach allows the Higgs self-coupling $\lambda$ to be fixed differently — yielding $m_H = 2\cos\theta_W m_W$ rather than $m_H = m_Z$. The key difference is in how the action is constructed from the curvature (supertrace of $\mathbb{F}^2$ vs. gauge-theory kinetic term).

**Calibration:** The original Ne'eman-Fairlie model is firmly ruled out ($m_H = m_Z$). Todorov's refinement gives $m_H \approx 127$ GeV, which is close but not exact. The community is aware of this history; any claim based on $sl(2|1)$ will be read against this background.

---

## Community Reception: Physics Forums Discussion

A Physics Forums thread (accessible) discussed the Todorov $m_H/m_W$ claim. Key points from the discussion:

1. The $13.7\sigma$ discrepancy (in experimental error units) is flagged as significant, even though the *percentage* is only 1.6%.
2. The "within one percent" phrasing is characterised as misleading given that $\delta m_H^\text{exp} = 0.14$ GeV makes 1.9 GeV a large sigma-deviation.
3. The community distinguishes between "close in percentage" and "a genuine prediction" — the latter requires the gap to close under radiative corrections in a way that is calculable and not fine-tuned.

**Implication for this framework:** The claim must be presented as a tree-level relation with an unresolved correction term. The earlier "GUT-to-EW running closes the gap" framing no longer holds up; the live issue is an explicit electroweak-threshold correction calculation. Without that calculation, the "1%" language invites the same criticism. See the gap analysis in [higgs.md](higgs.md).

---

## Quillen — Superconnections (1985)

**Quillen, D.:** J. reine angew. Math. 346 (1985) 163–196.

**What it does:** Defines the superconnection formalism. A superconnection on a $\mathbb{Z}_2$-graded vector bundle $E = E^+ \oplus E^-$ is a map $\mathbb{A}: \Omega^*(M, E^+) \oplus \Omega^*(M, E^-) \to \Omega^*(M, E^- \oplus E^+)$ that is a graded derivation. The curvature $\mathbb{F} = \mathbb{A}^2$ is used to define characteristic classes.

**Physics use:** Bismut (1986) applied superconnections to the index theorem. Connes (1996) applied the formalism to derive the SM action from NCG. Todorov applies it to get the Higgs-gauge mass relation.

**Key point:** The Quillen superconnection is more general than a Lie superalgebra gauge connection. The Higgs mass relation from Todorov is a property of the Quillen construction, not of the Ne'eman-Fairlie $su(2|1)$ Lie superalgebra. This is why Todorov gets a different (and better) answer than Ne'eman-Fairlie.

---

## Gogberashvili — Octonionic Geometry and Physics (arXiv:1602.07979)

**What it does:** Derives the conformal group $SO(2,4)$ from $G_2^{\text{split}}$ acting on a cone of split-octonions. Used in the $G_2 \to SO(2,4)$ arrow of the chain. See [chain/g2-so24.md](chain/g2-so24.md).

**Status in this project:** This check is now completed. The image of $\tilde{u}$ under the cone map is taken to be spacelike in $\mathbb{R}^{2,4}$, giving the required $SO(2,3)$ stabilizer and hence the $Spin(2,3)$ arrow. See [chain/so24-spin23.md](chain/so24-spin23.md).

---

## Baez — Octonions (2002) and the Leech Connection

**Baez, J.C.:** Bull. AMS 39 (2002) 145–205. arXiv:math/0105155.

**Egan, G.:** "Symmetries of the Standard Model" (blog, 2022). Explicitly works out the Leech lattice embedding in $J_3(\mathbb{O})$ and the $E_8$ connection.

**Key result for this program:** $J_3(\mathbb{O})$ contains a 24+3 structure (24 off-diagonal octonion entries + 3 real diagonal) whose 24-dimensional sublattice maps to the Leech lattice. See [statics.md](statics.md).

**Status in this project:** This is no longer treated as a single open check. The current formulation is: continuous $SU(3)$ equivariance is impossible for a discrete lattice; discrete equivariance is conditional on fixing the triality frame; and the Jordan product $D \circ U$ does not preserve the Leech tier except for $D=\pm I$. See [statics.md](statics.md).
