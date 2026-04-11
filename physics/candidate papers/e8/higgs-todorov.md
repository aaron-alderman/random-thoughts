# Todorov Superconnection Note

This note collects the Todorov-specific part of the Higgs-mass story that was previously making [higgs.md](higgs.md) too large.

---

## Core Claim

Todorov's $sl(2|1)$ superconnection gives the tree-level relation

$$m_H = 2\cos\theta_W\,m_W.$$

Within the $u$-framework, the key octonionic input

$$\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3$$

is no longer postulated. After choosing

$$u \in \mathrm{Im}(\mathbb{O}),$$

one gets

$$\mathbb{O} = \mathbb{C}_u \oplus \mathbb{C}^3_{u^\perp}.$$

So the Todorov split is internal to the program.

Using the already-derived value

$$\sin^2\theta_W = \frac{3}{8}, \qquad \cos^2\theta_W = \frac{5}{8},$$

the mass formula becomes

$$m_H = \sqrt{\frac{5}{2}}\,m_W \approx 127.1 \text{ GeV}.$$

This is about $1.5\%$ above the observed Higgs mass.

---

## What Is Imported vs Derived

**Derived inside the present framework**

- the `1+3` octonionic split
  $$\mathbb{O} = \mathbb{C}_u \oplus \mathbb{C}^3_{u^\perp};$$
- the Weinberg-angle value
  $$\sin^2\theta_W = \frac{3}{8};$$
- the representation-theoretic singlet-plus-triplet reading of Todorov's lepton/quark channels.

**Imported from Todorov unless the remaining metric step is closed**

- the exact odd-sector superconnection normalization;
- the resulting coupling relation
  $$\lambda = \frac{g^2\cos^2\theta_W}{2};$$
- hence
  $$m_H = 2\cos\theta_W\,m_W.$$

---

## Formalized Normalization Statement

Let

$$\mathcal{N}(\Phi)$$

be the positive quadratic form on the Higgs doublet sector induced by the odd part of the superconnection.

Assume:

1. Before selecting a specific $u$, $\mathcal{N}$ comes from a $G_2$-invariant positive Hermitian form on the relevant octonionic data.
2. After fixing $u$, the decomposition
   $$\mathbb{O} = \mathbb{C}_u \oplus \mathbb{C}^3_{u^\perp}$$
   is orthogonal for $\mathcal{N}$.
3. The same Higgs amplitude is copied into each colour channel.

Then there is a constant $c>0$ such that

$$\mathcal{N}_L(\Phi) = c|\Phi|^2, \qquad \mathcal{N}_Q(\Phi) = 3c|\Phi|^2,$$

so

$$\boxed{\mathcal{N}_Q(\Phi) = 3\,\mathcal{N}_L(\Phi).}$$

This is the invariant octonionic version of Todorov's lepton-vs-single-colour comparison.

---

## Translation to Todorov's `\rho`

Todorov does not package the normalization as a raw factor of `3`. Instead he compares the leptonic contribution with one single-colour quark contribution inside the restricted projector formalism.

So the dictionary is:

- octonionic full quark sector:
  $$\mathcal{N}_Q = 3\mathcal{N}_L;$$
- Todorov single-colour comparison:
  $$\mathcal{N}_{Q,j} = \mathcal{N}_L.$$

In his basis this equality is encoded by

$$\rho^2 = \frac{1}{2},$$

and substituting this into his mass formula gives

$$\frac{m_H^2}{m_W^2} = 4\,\frac{1+6\rho^4}{1+6\rho^2} = \frac{5}{2}.$$

So the factor `1/2` is not contradicting the octonionic factor `3`; it is the basis-dependent way the same equality appears after restricting to one quark channel.

---

## Representation Side: Essentially Closed

With Todorov's projector convention

$$\ell = p_1p_2p_3, \qquad q_j = p_jp_k'p_\ell',$$

the colour Fock space decomposes by occupation number:

$$\Lambda^0(\mathbb{C}^3)\oplus\Lambda^1(\mathbb{C}^3)\oplus\Lambda^2(\mathbb{C}^3)\oplus\Lambda^3(\mathbb{C}^3).$$

Then:

- $\ell$ is the colour vacuum sector, so it is a singlet;
- each $q_j$ lies in the two-particle / one-hole sector, hence in a three-dimensional irreducible colour module, naturally $\bar{\mathbf 3}$ in these conventions.

Using Todorov's state identifications

$$\ell aa^\dagger = \nu, \qquad \ell a^\dagger a = e,$$
$$q_j aa^\dagger = u_j, \qquad q_j a^\dagger a = d_j,$$

and the fact that the weak oscillators preserve colour occupation number, one gets:

$$\nu,e \in \Lambda^0(\mathbb{C}^3), \qquad u_j,d_j \in \Lambda^2(\mathbb{C}^3).$$

So:

- $(\nu,e)$ are colour singlets;
- $(u_1,u_2,u_3)$ and $(d_1,d_2,d_3)$ each furnish the same irreducible three-dimensional colour representation.

The representation part is therefore no longer the bottleneck.

---

## What Todorov's Explicit Formulas Already Force

The primary-source formulas sharpen the remaining metric problem a lot.

In the restricted projector formalism the odd Higgs operator has the form

$$\Phi = \Phi_\ell + \Phi_q,$$

with

$$\Phi_\ell=\ell(\phi_1A_1^\dagger-\overline{\phi}_1A_1+\phi_2A_2^\dagger-\overline{\phi}_2A_2),$$
$$\Phi_q=\rho\,q\sum_{\alpha=1}^2(\phi_\alpha a_\alpha^\dagger-\overline{\phi}_\alpha a_\alpha), \qquad q=q_1+q_2+q_3.$$

Since

$$q_jq_k = \delta_{jk}q_j, \qquad \ell q_j = 0 = q_j\ell,$$

and the weak oscillators live in the separate $Cl_4$ factor, one may decompose

$$\Phi_q = \sum_{j=1}^3 \Phi_{q_j}, \qquad \Phi_{q_j} := \rho\,q_j\sum_{\alpha=1}^2(\phi_\alpha a_\alpha^\dagger-\overline{\phi}_\alpha a_\alpha).$$

Then distinct-channel cross terms vanish formally:

$$\Phi_\ell\Phi_{q_j}=0, \qquad \Phi_{q_j}\Phi_{q_k}=0 \quad (j\neq k).$$

So orthogonality of different quark channels is already built into the projector algebra.

For the diagonal terms, Todorov's explicit formula gives

$$\Phi_{q_j}^2 = -\rho^2 q_j(\phi_1\overline{\phi}_1+\phi_2\overline{\phi}_2) = -\rho^2 q_j\,\phi\overline{\phi},$$

hence

$$-\,\mathrm{Tr}(\Phi_{q_j}^2)=\rho^2\,\phi\overline{\phi}$$

for each $j$.

Therefore the quark block is automatically

$$bI_3.$$

The leptonic diagonal entry is the only genuinely nontrivial part left. Todorov computes

$$-\,\mathrm{Tr}\!\left(\ell(1-\pi_1\pi_2)\Phi^2\right)=\frac12\,\phi\overline{\phi},$$

while a single quark channel contributes

$$-\,\mathrm{Tr}\!\left(\rho^2 q_j\Phi^2\right)=\rho^2\,\phi\overline{\phi}.$$

Equality of the leptonic contribution with one coloured-quark contribution is exactly

$$\rho^2=\frac12.$$

So the source-level metric problem is no longer "show that an arbitrary $4\times 4$ channel matrix is scalar". The formulas already collapse it to

$$a \oplus bI_3,$$

and the open question is the remaining scalar equality

$$a=b.$$

---

## Sharpest Remaining Theorem Target

The whole normalization program has now been reduced to:

**Target.** Show that Todorov's odd quadratic form on the channel basis

$$ (\ell, q_1, q_2, q_3) $$

is not merely

$$a \oplus bI_3,$$

but actually

$$cI_4.$$

Equivalently:

1. off-diagonal channel pairings vanish;
2. the three quark diagonal entries are equal;
3. the leptonic diagonal entry equals each quark one;
4. the common value is positive.

Items 1 and 2 are now essentially forced by the explicit projector algebra. The real remaining content is item 3.

---

## Residual 1.5% Gap

The old idea that the `127.1 GeV -> 125.2 GeV` discrepancy is explained by ordinary GUT-to-EW running is not credible.

Running the boundary condition

$$\lambda_0 = \frac{5}{16}g_2^2(\Lambda)$$

down from a high matching scale pushes the Higgs mass far too high, not gently down to the observed value.

So the better interpretation is:

- Todorov's formula is a tree-level EW-scale relation inside the $sl(2|1)$ framework;
- the `1.5%` mismatch should be treated as a finite electroweak threshold / one-loop correction problem;
- there is also a genuine vacuum-stability tension if one insists on reading the formula as a high-scale UV boundary condition.

The live next calculation is therefore an explicit one-loop correction to

$$R = \frac{m_H^2}{m_W^2} = \frac{8\lambda}{g_2^2}$$

inside the superconnection framework.

---

## Current Status

| Claim | Status |
|---|---|
| Todorov's `1+3` octonionic split is internalized by the $u$-framework | Established |
| The representation-theoretic singlet-plus-triplet structure is essentially closed | Established up to notation bookkeeping |
| The quark-channel metric block is already forced to be `bI_3` by explicit formulas | Established |
| The lepton-vs-single-quark equality `a=b` is still open | Main remaining gap |
| The `1.5%` residual should be read as an EW-threshold issue, not successful GUT-to-EW running | Reframed |
