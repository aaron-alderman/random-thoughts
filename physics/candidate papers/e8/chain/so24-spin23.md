# Arrow: $SO(2,4) \to Spin(2,3)$

## What is there

Mathematically clean. $SO(2,3)$ is the subgroup of $SO(2,4)$ that fixes a chosen vector. $Spin(2,3)$ is its simply-connected double cover. The reduction removes the dilatation generator.

## The renormalization claim

$SO(2,4)$ has a free dilatation generator — this is precisely what generates RG flow. Selecting a vector removes that freedom. The theory no longer has to be consistent across all scales simultaneously; it only has to work at the selected scale and its consequences. $Spin(2,3)$ has no dilatation generator, so no RG running in that sense.

## The double cover

The simply-connected cover is what allows spinor representations globally. Without it, only tensor representations are available. This connects to the Leech/Golay global consistency structure — the double cover is also about global rather than local consistency.

## Same-$u$ verification status

Four of the five roles of $u$ through the chain are confirmed:

- $\mathrm{Stab}_{G_2}(u) = SU(3)$: established mathematical fact
- Same $u$ across compact/split via $\mathbb{O}_\mathbb{C}$: established (Hurwitz/Jacobson) — see [g2-so24.md](g2-so24.md)
- $u = e_7$ in Furey's Cl(6), $u^\perp$ is the 6D Witt space: established by the idempotent matching — see [higgs.md](../higgs.md)
- T1 observable channel = $u$: by construction

**Check complete (explicit coordinate argument):** The Gogberashvili cone map sends $\mathrm{Im}(\tilde{\mathbb{O}}) \cong \mathbb{R}^{3,4}$ to $\mathbb{R}^{2,4}$. The image $\tilde{u}$ is **spacelike** in $\mathbb{R}^{2,4}$. The argument:

1. **$u$ is spacelike in $\mathbb{R}^{3,4}$.** From the paper's norm form $N^2 = d\omega^2 - d\lambda_n^2 + dx_n^2 - c^2dt^2$, the imaginary directions split as: $j_n$ (spacelike, $Q = +1$, $j_n^2 = -1$) and $J_n, I$ (timelike, $Q = -1$, $J_n^2 = I^2 = +1$). For $G_2^{\text{split}}$ on $\mathbb{R}^{3,4}$: spacelike vectors have stabilizer $SU(2,1)$ (left-multiplication by $u$ gives genuine complex structure $J_u^2 = -\mathrm{id}$ on $u^\perp \cong \mathbb{R}^{2,4}$, preserving a Hermitian form of signature $(1,2)$); timelike vectors have stabilizer $SL(3,\mathbb{R})$ (split complex structure $J_u^2 = +\mathrm{id}$). Since the stabilizer of $u$ in split $G_2$ is $SU(2,1)$ (see [g2-so24.md](g2-so24.md)), $u = j_n$-type — spacelike.

2. **Explicit cone map.** From eq. (10)–(11) of Gogberashvili, matching the norm form to the $(2+4)$-cone $-d\varpi^2 - (dX^0)^2 + (dX^n)^2 + dl^2$: the unique consistent identification is $\varpi = \lambda_\|/L$, $l = \omega/L$, $X^0 = ct/L$, $X^n = x_n/L$. (Inversions $l \to -l$ flip $\omega$, not $\lambda_\|$, consistent with Gogberashvili's earlier papers.) Causal characters: $X^n$ spacelike, $X^0$ and $\varpi$ timelike, $l$ spacelike.

3. **Causal character of $\tilde{u}$.** $u = j_n$ (spacelike in 7D) maps to $X^n$ (spacelike in $\mathbb{R}^{2,4}$). ✓

4. **Stabilizer.** Spacelike vector in $SO(2,4)$ has stabilizer $SO(2,3)$ (acting on $u^\perp \cong \mathbb{R}^{2,3}$). Simply-connected cover: $Spin(2,3)$. ✓

Note: the de Sitter group $SO(1,4)$ appears in the paper (eq. 20) via the dynamics of the $\lambda_n$ / $\varpi$ directions — these are the timelike $J_n$-type directions, i.e., exactly what would arise from the wrong choice of $u$. The geometry naturally separates the two outcomes.

**Note on "time anchor" language:** The description of $u$ as "time anchor in $Spin(2,3)$" refers to $u$'s role *within the reduced theory* — selecting one of the two timelike directions in the $(2+3)$-dimensional space that $Spin(2,3)$ inherits after the reduction. It does not describe the causal character of the vector fixed in $SO(2,4) \to Spin(2,3)$, which must be spacelike in $\mathbb{R}^{2,4}$ for the stabilizer to be $SO(2,3)$.

## Status

| Claim | Status | Maturity |
|---|---|---|
| $SO(2,3) \subset SO(2,4)$ as vector stabilizer: Established | Established | 2 |
| $Spin(2,3)$ = simply-connected cover: Established | Established | 2 |
| Scale-fixing / RG reframing via dilatation removal | Proposal | 4 |
| Same $u$ at $G_2$, Cl(6), T1 channel, compact/split | Established | 3 |
| Image of $\tilde{u}$ spacelike under Gogberashvili cone map | Established by explicit coordinate argument | 2 |
