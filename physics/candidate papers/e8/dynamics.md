# Dynamics

## Core Dynamical Ingredients

- Evolution in full space $T1 \oplus T2$
- Transport operator acting in $T1$
- Off-diagonal coupling between $T1$ and $T2$
- Reduced evolution for the projected sector
- Effective transport-diffusion after coarse-graining

---

## The $G_2$ Coarse-Graining and Scale Fixing

The $\sqrt{3}$ root ratio in $G_2$ is the algebraic record of coarse-graining from 7 imaginary octonionic dimensions to rank 2. The Cartan matrix of $G_2$ (with rows/columns indexed by short root $\alpha_1$, long root $\alpha_2$) is:

$$\begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$$

giving root length ratio $|\alpha_\mathrm{long}|/|\alpha_\mathrm{short}| = \sqrt{3}$ (only such ratio in any exceptional Lie algebra).

**$SU(3) \subset G_2$ via the long roots.** Positive long roots $\{\alpha_2,\; 3\alpha_1+\alpha_2,\; 3\alpha_1+2\alpha_2\}$ form the $A_2 = SU(3)$ subsystem. Positive short roots $\{\alpha_1,\; \alpha_1+\alpha_2,\; 2\alpha_1+\alpha_2\}$ transform as $\mathbf{3}\oplus\bar{\mathbf{3}}$ under this $SU(3)$ — the "extra matter" sector, not the $SU(3)$ Cartan generators.

**Killing form normalization:** In the Chevalley-Weyl basis $B(E_\alpha, E_{-\alpha}) = 2/|\alpha|^2$, so long root generators have a smaller Killing form value ($2/3$) than short root generators ($2$). After canonical field normalization (dividing out $\sqrt{B}$), the physical coupling goes as $g \propto 1/\sqrt{B} \propto |\alpha|/\sqrt{2}$, giving:

$$\frac{g_\mathrm{long}}{g_\mathrm{short}} = \frac{|\alpha_\mathrm{short}|}{|\alpha_\mathrm{long}|} = \frac{1}{\sqrt{3}}$$

The $SU(3)$ (long-root) coupling is $1/\sqrt{3}$ of the short-root coupling within $G_2$.

**Embedding index:** $j_{SU(3) \subset G_2} = [T(\mathbf{8}) + T(\mathbf{3}) + T(\bar{\mathbf{3}})]/T_{G_2}(\mathbf{14}) = [3 + \tfrac{1}{2} + \tfrac{1}{2}]/4 = 1$. So the overall coupling $g_{SU(3)} = g_{G_2}$ at the $G_2$ breaking scale — the $1/\sqrt{3}$ is a generator-normalization ratio within $G_2$, not a group-level coupling mismatch.

**Does $1/\sqrt{3}$ appear in SM coupling ratios? No — structural reason identified.**

- $g_3/g_2$ at $M_{GUT} = 1$ (by $j=1$ embedding indices, all SM groups). No $\sqrt{3}$.
- $g'/g_2 = \sqrt{3/5}$ from $\sin^2\theta_W = 3/8$. Contains $\sqrt{3}$, but this is the octonionic 3+2 split $\sqrt{3}$, not the $G_2$ root ratio $\sqrt{3}$.
- Both $\sqrt{3}$'s share the same origin: $N_c = 3$. The $G_2$ root squared ratio $|\alpha_L|^2/|\alpha_S|^2 = 3 = N_c$ (because $G_2 \supset SU(3)$ via long roots, and $N_c = 3$ determines the root ratio). The Weinberg angle uses $N_c = 3$ via the 3+2 counting. They are two projections of the same $N_c$ fact, not independent $\sqrt{3}$ appearances.

**Observable consequence of $1/\sqrt{3}$:** If the short-root generators of $G_2$ (transforming as $\mathbf{3}\oplus\bar{\mathbf{3}}$ of $SU(3)$, i.e., leptoquark-type bosons) are massive at the $G_2$-breaking scale, their coupling to SM particles is $\sqrt{3}$ times the QCD coupling at that scale. This would be observable in leptoquark searches — not in SM coupling ratios among $g_3, g_2, g_1$.

---

## Renormalization Reframed

- $SO(2,4)$: free dilatation generator → RG running → UV divergences are artifacts of unresolved scale freedom
- Vector selection + double cover → $Spin(2,3)$: scale physically fixed by geometry
- RG "running" becomes a one-time geometric fact rather than ongoing scale dependence
- UV divergences in standard QFT may be artifacts of using $SO(2,4)$ language when the actual theory has already fixed its scale via $u$

---

## Reduced Dynamics

Under weak coupling, fast hidden-sector relaxation, and Markov coarse-graining, the reduced observable evolution is time-local with:

$$D \sim \frac{m^2}{\gamma}$$

where $m$ is the sector-mixing scale and $\gamma$ is the hidden-sector relaxation rate.

---

## Mass as Sector Mixing

$m$ is read as an effective mass parameter because it controls the first departure from purely ballistic visible transport. Diffusion $D \sim m^2/\gamma$ is the observable shadow of hidden-sector excursions. Higgs-mediated mass generation may be what opens access away from pure $T1$ propagation — the Higgs sets the scale at which the system first mixes between T1 and T2 channels.

---

## Status

| Claim | Status | Maturity |
|---|---|---|
| $\sqrt{3}$ root ratio forced by $G_2$ Dynkin diagram | Established | 2 |
| $SU(3) \subset G_2$ via long root subsystem | Established | 2 |
| $1/\sqrt{3}$ coupling ratio from Killing form normalization | Established (Chevalley-Weyl basis, explicit) | 2 |
| Embedding index $j_{SU(3)\subset G_2} = 1$ | Established | 2 |
| $1/\sqrt{3}$ appears in SM $g_3/g_2$ | No — structural reason: $j=1$ embedding gives $g_3=g_2$ at GUT scale | 2 |
| Both $\sqrt{3}$'s (root ratio + Weinberg angle) have same origin $N_c=3$ | Established — not independent predictions | 2 |
| $1/\sqrt{3}$ observable in short-root (leptoquark-type) coupling at $G_2$-breaking scale | Prediction — if $G_2$ breaks at accessible scale | 4 |
| RG reframing: scale fixing kills dilatation generator | Interpretation / Proposal | 5 |
| $D \sim m^2/\gamma$ reduced dynamics | Formal derivation under stated approximations | 4 |
