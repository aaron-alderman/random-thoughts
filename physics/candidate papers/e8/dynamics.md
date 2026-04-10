# Dynamics

## Core Dynamical Ingredients

- Evolution in full space $T1 \oplus T2$
- Transport operator acting in $T1$
- Off-diagonal coupling between $T1$ and $T2$
- Reduced evolution for the projected sector
- Effective transport-diffusion after coarse-graining

---

## The $G_2$ Coarse-Graining and Scale Fixing

The $\sqrt{3}$ root ratio in $G_2$ is the algebraic record of coarse-graining from 7 imaginary octonionic dimensions to rank 2. The Cartan matrix of $G_2$ is:

$$\begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$$

giving root length ratio $|\alpha_\mathrm{long}|/|\alpha_\mathrm{short}| = \sqrt{3}$. This is the only such ratio in any exceptional Lie algebra.

Under $G_2 \to SU(3)$ via $u$-selection, the short root generators become $SU(3)$ Cartan generators. The coupling ratio inherited through Killing form normalization is:

$$\frac{g_\mathrm{long}}{g_\mathrm{short}} = \frac{|\alpha_\mathrm{short}|}{|\alpha_\mathrm{long}|} = \frac{1}{\sqrt{3}}$$

Whether this ratio survives to observable couplings is the key calculation (see next steps below).

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

## Next Step: $\sqrt{3}$ Killing Form Calculation

Compute the Killing form normalization of the $G_2$ long and short root generators. Track how that normalization feeds into candidate coupling strengths through the reduction map. Check whether the ratio $1/\sqrt{3}$ appears in Standard Model coupling structure (weak mixing angle, $SU(3)/SU(2)$ coupling ratio at unification). This is a half-day calculation.

---

## Status

| Claim | Status | Maturity |
|---|---|---|
| $\sqrt{3}$ root ratio forced by $G_2$ Dynkin diagram | Established | 2 |
| $1/\sqrt{3}$ coupling ratio from Killing form normalization | Derived structurally | 4 |
| $1/\sqrt{3}$ appears in observable SM coupling ratios | Unverified — key calculation | 4 |
| RG reframing: scale fixing kills dilatation generator | Interpretation / Proposal | 5 |
| $D \sim m^2/\gamma$ reduced dynamics | Formal derivation under stated approximations | 4 |
