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

**One remaining check:** The Gogberashvili cone map sends $\mathrm{Im}(\tilde{\mathbb{O}}) \cong \mathbb{R}^{3,4}$ to $\mathbb{R}^{2,4}$. For the stabilizer of the image vector $v_u$ to be $SO(2,3)$ — giving $Spin(2,3)$ via double cover, as required — $v_u$ must be **spacelike** in $\mathbb{R}^{2,4}$. If $v_u$ were timelike, the stabilizer would be $SO(1,4)$ (the de Sitter group) instead — a different endpoint entirely. Whether $\tilde{u}$ maps to a spacelike vector under the Gogberashvili cone map is the single concrete coordinate check remaining. This requires working through Gogberashvili (arXiv:1602.07979) explicitly in components.

**Note on "time anchor" language:** The description of $u$ as "time anchor in $Spin(2,3)$" refers to $u$'s role *within the reduced theory* — selecting one of the two timelike directions in the $(2+3)$-dimensional space that $Spin(2,3)$ inherits after the reduction. It does not describe the causal character of the vector fixed in $SO(2,4) \to Spin(2,3)$, which must be spacelike in $\mathbb{R}^{2,4}$ for the stabilizer to be $SO(2,3)$.

## Next step: Gogberashvili coordinate check

Work through Gogberashvili arXiv:1602.07979 explicitly in components. Write out the cone map $\mathrm{Im}(\tilde{\mathbb{O}}) \to \mathbb{R}^{2,4}$. Identify which of the 7 split-imaginary directions corresponds to $u$ via $\mathbb{O}_\mathbb{C}$. Check whether its image is spacelike.

- Spacelike $\Rightarrow$ stabilizer $SO(2,3) = Spin(2,3)/\mathbb{Z}_2$ ✓
- Timelike $\Rightarrow$ stabilizer $SO(1,4)$ (de Sitter group) — hidden branch point ✗

## Status

| Claim | Status | Maturity |
|---|---|---|
| $SO(2,3) \subset SO(2,4)$ as vector stabilizer: Established | Established | 2 |
| $Spin(2,3)$ = simply-connected cover: Established | Established | 2 |
| Scale-fixing / RG reframing via dilatation removal | Proposal | 4 |
| Same $u$ at $G_2$, Cl(6), T1 channel, compact/split | Established | 3 |
| Image of $\tilde{u}$ spacelike under Gogberashvili cone map | Requires explicit coordinate check | 4 |
