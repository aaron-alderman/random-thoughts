
# Parametrized Spectral Framework for Mode Transition

## Abstract

We develop a minimal mathematical framework for mode transition in smooth families of real symmetric operators. The central objects are the eigenvalues, eigenvectors, and spectral projectors of a parametrized matrix family
\[
K(\theta)\in \mathrm{Sym}(n,\mathbb{R}),\qquad \theta\in\mathbb{R}^k.
\]
The framework is organized in five layers. The first layer isolates the reduced two-mode mechanism that governs local transition. The second introduces analytical perturbation formulas for eigenvalues, eigenvectors, and projectors, together with inverse-gap bounds. The third reformulates the theory geometrically in terms of the projector map into real projective space and the induced metric and curvature on parameter space. The fourth adds a bulk-boundary decomposition and boundary observables, showing that boundary weights inherit the same gap-amplified sensitivity. The resulting theory identifies transition regions as parameter zones where spectral gaps become small, eigenspaces vary rapidly, and, when relevant, boundary-restricted projectors become large or highly sensitive. The aim is not maximal generality, but a compact and coherent theory stack in which local two-mode reduction, perturbative instability, spectral geometry, and surface concentration all fit into one common language.

## Introduction

Many finite-dimensional systems exhibit parameter regimes in which dominant modes reorganize rapidly. In the simplest cases, eigenvalues approach each other without crossing exactly, while the associated eigenvectors rotate sharply in a narrow parameter window. In higher-dimensional settings the same phenomenon appears as rapid variation of spectral subspaces, concentration of weight on distinguished degrees of freedom, and instability of mode assignment near near-degenerate clusters.

The present manuscript isolates the minimal mathematics behind this phenomenon for smooth families of real symmetric matrices. The restriction to real symmetric operators gives a particularly transparent setting. Eigenvalues are real, orthonormal bases of eigenvectors exist away from degeneracy, and perturbation theory is clean enough that the core mechanism can be written explicitly. The main thesis is simple: **mode transition is governed not only by spectral proximity, but by the geometry of eigenvectors and projectors near small spectral gap**.

The framework is organized progressively. First, the reduced \(2\times 2\) model identifies the normal form of pairwise interaction. Second, first-order perturbation formulas show that eigenvector sensitivity scales inversely with spectral separation. Third, the spectral projector is promoted to the fundamental geometric object, yielding a natural metric and curvature-type viewpoint on parameter space. Fourth, if the state space carries a bulk-boundary splitting, the restriction of projectors to the boundary defines observables whose variation is again amplified by inverse gap scaling. Each stage adds only what is forced by the mathematics of the preceding one.

The result is a concise but complete theory stack. It can serve equally well as a conceptual handoff, a basis for examples, or the skeleton of a more formal paper.

---

# Phase II — Mathematical Core

## 1. Object of Study

Let
\[
K(\theta)\in \mathrm{Sym}(n,\mathbb{R})
\]
be a smooth family of real symmetric matrices depending on a parameter vector
\[
\theta=(\theta_1,\dots,\theta_k)\in \mathbb{R}^k.
\]

Throughout, smoothness may be taken as \(C^1\) when only first-order perturbation theory is needed, and \(C^2\) when second derivatives are discussed. Since \(K(\theta)\) is symmetric for every \(\theta\), each matrix admits a full orthonormal basis of real eigenvectors, and all eigenvalues are real.

The object of study is therefore not a single operator, but a **parametrized spectral family**. The problem is to understand how the spectral data of \(K(\theta)\) evolve as \(\theta\) varies, and in particular how qualitative changes in dominant modes arise.

The finite-dimensional setting is deliberate. It allows all essential ideas to appear in a technically controlled form:

- spectral gaps are explicit;
- eigenvector rotation can be written concretely;
- projectors are finite-rank matrices;
- boundary restrictions become simple orthogonal compressions.

Thus the framework isolates the mathematics of transition before any infinite-dimensional or operator-domain issues are introduced.

## 2. Spectral Problem

For each \(\theta\), consider the eigenvalue problem
\[
K(\theta)\psi_i(\theta)=\lambda_i(\theta)\psi_i(\theta),
\qquad i=1,\dots,n,
\]
with eigenvalues ordered as
\[
\lambda_1(\theta)\ge \lambda_2(\theta)\ge \cdots \ge \lambda_n(\theta),
\]
and eigenvectors normalized by
\[
\|\psi_i(\theta)\|=1.
\]

Away from degeneracies one may choose the eigenvectors locally as smooth functions of \(\theta\), up to sign. The eigenvalue ordering makes the dominant sector explicit and allows one to track the leading modes as the parameters vary.

The basic tension in spectral transition is already visible here. Eigenvalues measure spectral separation, but eigenvectors determine the actual modal structure. A small change in \(\lambda_i\) does not necessarily imply a large change in \(\psi_i\), and conversely eigenvectors may rotate very rapidly in a region where the eigenvalues are still smooth. The framework therefore treats eigenvalues and eigenvectors on equal footing from the outset.

## 3. Reduced \(2\times 2\) Model (Minimal Case)

The local normal form of a pairwise interaction is the symmetric \(2\times 2\) matrix
\[
K(\theta)=
\begin{pmatrix}
a_1(\theta) & b(\theta)\\
b(\theta) & a_2(\theta)
\end{pmatrix}.
\]

Define the diagonal imbalance
\[
\Delta(\theta)=a_1(\theta)-a_2(\theta).
\]

The eigenvalues are
\[
\lambda_\pm(\theta)
=
\frac{a_1+a_2}{2}
\pm
\sqrt{\left(\frac{\Delta}{2}\right)^2+b^2}.
\]

This formula shows immediately that there are two competing mechanisms:

1. **Diagonal detuning**, encoded by \(\Delta\).
2. **Off-diagonal mixing**, encoded by \(b\).

If \(|\Delta|\gg |b|\), the matrix is nearly diagonal in the chosen basis, and the eigenvectors remain close to basis directions. If \(|b|\gg |\Delta|\), mixing dominates and the eigenvectors are strongly hybridized. The transition zone occurs when these quantities are comparable.

The reduced \(2\times 2\) model is minimal in a precise sense. Whenever exactly two modes become close while the rest remain well separated, the local spectral behavior is governed by an effective two-dimensional invariant subspace. Thus the formulas in this section are not merely illustrative: they are the universal local model of pairwise mode transition.

## 4. Eigenvector Parameterization

For the dominant eigenvector in the reduced \(2\times 2\) model, write
\[
\psi(\theta)=
\begin{pmatrix}
\cos\phi(\theta)\\
\sin\phi(\theta)
\end{pmatrix}.
\]

Then the mixing angle \(\phi\) satisfies
\[
\tan 2\phi(\theta)=\frac{2b(\theta)}{\Delta(\theta)}.
\]

This formula makes the geometry of transition completely explicit. The parameter \(\phi\) describes the rotation of the eigendirection inside the two-dimensional state space. When \(b=0\), the eigenvectors are aligned with the coordinate axes. When \(\Delta=0\) and \(b\neq 0\), maximal mixing occurs, with \(\phi\) near \(\pi/4\) up to sign conventions.

The use of \(2\phi\) rather than \(\phi\) is structurally important: the projector associated with \(\psi\) depends only on the line spanned by \(\psi\), not on its sign, and therefore the relevant angle is naturally defined modulo \(\pi\), not modulo \(2\pi\). This anticipates the geometric reinterpretation in terms of projective space.

## 5. Dimensionless Coordinates

To separate intrinsic geometry from raw scale, introduce dimensionless parameters
\[
x=\frac{\Delta}{b_0},\qquad
y=\frac{\epsilon_0}{b_0},\qquad
\tau=\frac{T_\epsilon}{T_b},\qquad
t=\frac{T}{T_b},
\]
where one writes
\[
b(\theta)=b_0 f(t),\qquad \Delta(\theta)=\delta+\epsilon(t).
\]

The purpose of this normalization is notational and conceptual:

- \(b_0\) sets a reference coupling scale;
- \(x\) measures detuning relative to coupling;
- \(y\) measures perturbation amplitude relative to coupling;
- \(\tau\) compares characteristic variation scales.

In particular, expressions such as \(|\Delta|\sim |b|\) become statements about dimensionless ratios rather than dimensional quantities. The transition analysis then depends on relative scale, not on arbitrary units.

## 6. Spectral Gap

Define the spectral gap between the top two modes by
\[
\boxed{
\Delta_\lambda(\theta)=\lambda_1(\theta)-\lambda_2(\theta)
=2\sqrt{\left(\frac{\Delta}{2}\right)^2+b^2}.
}
\]

In the reduced \(2\times 2\) model, this quantity summarizes proximity to degeneracy. It is always nonnegative and vanishes exactly when both \(\Delta=0\) and \(b=0\).

The gap plays two distinct roles:

- it measures spectral closeness;
- it controls the size of perturbative denominators in eigenvector formulas.

This second role is the deeper one. A small gap is not merely a sign that two eigenvalues are close; it is the mechanism through which small matrix perturbations can induce large changes in modal structure.

## 7. Eigenvector Functional

Define the quartic functional
\[
\boxed{
\mathcal I(\theta)=\sum_{i=1}^n |\psi_i(\theta)|^4.
}
\]

For \(n=2\), using the angle parametrization,
\[
\mathcal I
=
\cos^4\phi+\sin^4\phi
=
\frac12+\frac12\cos^2(2\phi).
\]

This quantity measures concentration of a normalized vector in a fixed basis. In the two-mode case:

- \(\mathcal I=1\) when the vector coincides with a basis direction;
- \(\mathcal I=\tfrac12\) when the vector is equally distributed between the two basis vectors.

Thus \(\mathcal I\) distinguishes basis alignment from mixing. It is not a spectral invariant, but a basis-sensitive observable adapted to the chosen decomposition of state space. In later sections, an analogous boundary participation functional will refine support on a distinguished subspace.

## 8. Degeneracy Set

Define the degeneracy set
\[
\boxed{
\mathcal D=\{\theta:\, b(\theta)=0,\ \Delta(\theta)=0\}.
}
\]

At every \(\theta\in \mathcal D\),

- the two eigenvalues coincide,
- the corresponding eigenspace becomes two-dimensional,
- individual eigenvectors are not uniquely defined.

This is the singular locus of the two-mode model. Away from \(\mathcal D\), the eigendirections are determined up to sign. At \(\mathcal D\), only the full eigenspace is defined. The degeneracy set is therefore not merely where formulas fail; it is where the relevant object changes from an eigenvector to a higher-rank invariant subspace.

## 9. Mixed Regime (Transition Region)

Define the mixed or transition region by
\[
\boxed{
\mathcal M=\{\theta:\, \Delta_\lambda(\theta)\ \text{is small}\}.
}
\]

In the reduced \(2\times 2\) setting, this is equivalently characterized by
\[
|\Delta(\theta)|\sim |b(\theta)|.
\]

This is the region in which neither diagonal imbalance nor off-diagonal mixing completely dominates. Spectrally, the two eigenvalues are close. Geometrically, the eigendirections interpolate rapidly between limiting configurations.

The mixed regime is the natural candidate for mode transition because it is exactly where modal identity becomes unstable. Outside this region, the modes are clearly separated either by spectral gap or by basis alignment.

## 10. Sensitivity Measures

For eigenvalues, define first-order sensitivity with respect to parameter \(\theta_j\) by
\[
\frac{\partial \lambda_i}{\partial \theta_j}.
\]

For eigenvectors, define
\[
\boxed{
S(\theta)=\left\|\frac{\partial \psi}{\partial \theta}\right\|.
}
\]

In a one-parameter setting this is simply the norm of the derivative. In a multiparameter setting one may interpret it componentwise or as the operator norm of the Jacobian. Either way, \(S\) measures the rate at which the eigendirection changes under parameter variation.

This is the first genuinely geometric quantity in the framework. It does not merely record spectral separation; it measures the deformation of the mode itself.

## 11. Key Property

Near the degeneracy set \(\mathcal D\), eigenvector sensitivity becomes large:
\[
\boxed{
S(\theta)\to \text{large as }\theta\to \mathcal D.
}
\]

In the two-mode model this follows directly from the angle formula. Since
\[
\tan 2\phi=\frac{2b}{\Delta},
\]
the derivative of \(\phi\) involves a denominator of the form \(\Delta^2+4b^2\), which becomes small near \((\Delta,b)=(0,0)\). Therefore even modest parameter motion can induce sharp rotation of the eigenvector.

This property is the first formulation of the transition mechanism: **small spectral separation causes large geometric response**.

## 12. Structural Classification

The parameter space can be divided into four structural regions:

| Region | Condition | Interpretation |
|---|---|---|
| Gap-dominated | \(|\Delta|\gg |b|\) | Eigenvectors stay close to basis directions |
| Mixing-dominated | \(|b|\gg |\Delta|\) | Eigenvectors are strongly hybridized |
| Mixed regime | \(|\Delta|\sim |b|\) | Transition zone, neither effect dominates |
| Degenerate | \(\Delta=0,\ b=0\) | Eigenbasis not uniquely defined |

This classification is minimal but complete in the \(2\times 2\) model. It separates stable modal regimes from transition and from exact degeneracy.

## 13. Extension to \(3\times 3\) (Democratic Case)

Consider the symmetric \(3\times 3\) matrix
\[
K(\theta)=
\begin{pmatrix}
a_1 & b & b\\
b & a_2 & b\\
b & b & a_3
\end{pmatrix},
\qquad a_1+a_2+a_3=\text{const}.
\]

This “democratic” form preserves equal off-diagonal coupling but allows nontrivial diagonal imbalance. The same structural ingredients appear:

- spectral gaps between nearby eigenvalues;
- codimension conditions for degeneracy;
- strong eigenvector sensitivity near small-gap regions.

Although the explicit formulas are more involved than in the \(2\times 2\) model, local pairwise interaction still reduces to an effective two-mode problem whenever a single pair of eigenvalues approaches while the third remains separated. Thus the reduced model remains the correct local template.

## 14. Core Statement

The central claim of the mathematical core is
\[
\boxed{
\text{Transition behavior is governed by the geometry of eigenvectors near small spectral gap.}
}
\]

This statement is deliberately stronger than “transition occurs when eigenvalues are close.” Spectral proximity is necessary, but the actual transition phenomenon is geometric: the modes themselves reorganize, rotate, and redistribute.

## 15. Minimal Working Procedure

A minimal computational or analytical workflow is:

1. Specify the parametrized operator \(K(\theta)\).
2. Compute eigenvalues \(\lambda_i(\theta)\).
3. Compute normalized eigenvectors \(\psi_i(\theta)\).
4. Evaluate the spectral gap and a sensitivity quantity such as
   \[
   \Delta_\lambda(\theta),\qquad
   S(\theta)=\left\|\frac{\partial \psi}{\partial \theta}\right\|.
   \]
5. Identify:
   - the degeneracy set \(\mathcal D\),
   - the mixed region \(\mathcal M\),
   - stable versus rapidly varying modal zones.

This procedure is sufficient for the minimal core. Later phases replace \(\psi_i\) by \(P_i\), then add geometric and boundary observables.

## 16. One-Line Summary

> A parametrized symmetric operator exhibits a transition region where eigenvalues approach and eigenvectors vary rapidly; this region is characterized by small spectral gap and large eigenvector sensitivity.

---

# Phase III — Analytical Layer

## 17. Spectral Projector Formulation

For a simple eigenvalue \(\lambda_i(\theta)\), define the rank-one spectral projector
\[
P_i(\theta)=\psi_i(\theta)\psi_i(\theta)^\top.
\]

This object removes the sign ambiguity of the eigenvector. Replacing \(\psi_i\) by \(-\psi_i\) leaves \(P_i\) unchanged, so \(P_i\) is the natural coordinate-free representation of a one-dimensional eigenspace.

The projector perspective is essential for two reasons:

1. it is geometrically canonical;
2. it extends naturally to higher-rank spectral clusters.

Thus from this point onward the projector, rather than the eigenvector itself, becomes the fundamental object.

## 18. First-Order Eigenvalue Formula

Let
\[
\partial_j K=\frac{\partial K}{\partial \theta_j}.
\]

If \(\lambda_i(\theta)\) is simple, differentiation of the eigenvalue equation and orthonormality yields
\[
\boxed{
\frac{\partial \lambda_i}{\partial \theta_j}
=
\psi_i^\top(\partial_j K)\psi_i.
}
\]

This is the Rayleigh perturbation formula. It shows that the first derivative of the eigenvalue is determined by the matrix derivative tested against the active mode. Unlike the eigenvector derivative, no small-gap denominator appears. Eigenvalues can therefore remain comparatively well behaved even where eigenvectors become highly sensitive.

## 19. First-Order Eigenvector Formula

Assume \(\lambda_i\) is simple and impose the gauge condition
\[
\psi_i^\top \frac{\partial \psi_i}{\partial \theta_j}=0.
\]

Then the first derivative of the eigenvector is
\[
\boxed{
\frac{\partial \psi_i}{\partial \theta_j}
=
\sum_{m\neq i}
\frac{\psi_m^\top(\partial_j K)\psi_i}{\lambda_i-\lambda_m}\,\psi_m.
}
\]

This is the key perturbation formula of the framework. It says that eigenvector variation is built from couplings to all complementary modes, each weighted by an inverse spectral separation. The numerator encodes how strongly the derivative \(\partial_j K\) mixes mode \(i\) with mode \(m\); the denominator amplifies this effect when the modes are nearly degenerate.

The formula is the higher-dimensional analogue of the two-mode angle derivative and makes precise the phrase “small gap implies rapid mode variation.”

## 20. Fundamental Sensitivity Bound

Taking norms in the eigenvector formula gives
\[
\left\|
\frac{\partial \psi_i}{\partial \theta_j}
\right\|
\le
\sum_{m\neq i}
\frac{\left|\psi_m^\top(\partial_j K)\psi_i\right|}{|\lambda_i-\lambda_m|}.
\]

Defining
\[
\operatorname{gap}_i(\theta)=\min_{m\neq i}|\lambda_i(\theta)-\lambda_m(\theta)|,
\]
one obtains the clean bound
\[
\boxed{
\left\|
\frac{\partial \psi_i}{\partial \theta_j}
\right\|
\le
\frac{\|\partial_j K\|}{\operatorname{gap}_i(\theta)}.
}
\]

This estimate is the analytical backbone of the whole manuscript. It identifies inverse spectral gap as the universal amplification factor for eigenvector sensitivity.

## 21. Projector Derivative Formula

Differentiating
\[
P_i=\psi_i\psi_i^\top
\]
gives
\[
\frac{\partial P_i}{\partial \theta_j}
=
\frac{\partial \psi_i}{\partial \theta_j}\psi_i^\top
+
\psi_i\left(\frac{\partial \psi_i}{\partial \theta_j}\right)^\top.
\]

Substituting the eigenvector derivative formula yields
\[
\boxed{
\frac{\partial P_i}{\partial \theta_j}
=
\sum_{m\neq i}
\frac{\psi_m^\top(\partial_j K)\psi_i}{\lambda_i-\lambda_m}
\left(\psi_m\psi_i^\top+\psi_i\psi_m^\top\right).
}
\]

This formula shows that the tangent directions to the projector manifold are precisely cross-mode couplings between the active mode and complementary modes.

## 22. Projector Sensitivity Bound

Using the previous identity,
\[
\boxed{
\left\|
\frac{\partial P_i}{\partial \theta_j}
\right\|
\le
\frac{2\|\partial_j K\|}{\operatorname{gap}_i(\theta)}.
}
\]

The factor of \(2\) reflects the two terms in the derivative of \(\psi_i\psi_i^\top\). Up to this harmless constant, the projector has the same inverse-gap sensitivity as the eigenvector. This is conceptually cleaner, since \(P_i\) is canonical while \(\psi_i\) is not.

## 23. Degeneracy Manifold in General Dimension

For a chosen mode \(i\), define
\[
\boxed{
\mathcal D_i=\{\theta:\, \operatorname{gap}_i(\theta)=0\}.
}
\]

Equivalently,
\[
\mathcal D_i
=
\{\theta:\, \exists\, m\neq i \text{ such that } \lambda_i(\theta)=\lambda_m(\theta)\}.
\]

At points of \(\mathcal D_i\), the one-dimensional eigenspace associated with \(\lambda_i\) ceases to be isolated. The individual projector \(P_i\) is no longer well defined as a smooth local object. The appropriate replacement is the projector onto the whole degenerate cluster.

## 24. Local Two-Mode Reduction Principle

If exactly two eigenvalues become close and the remaining spectrum stays uniformly separated, then in a neighborhood of that parameter point the transition dynamics reduces to an effective \(2\times 2\) problem on the corresponding two-dimensional invariant subspace.

This principle justifies the reduced model introduced in Phase II. The two-mode formulas are not special-case artifacts; they are the local normal form of generic pairwise transition.

## 25. Analytical Principle

The content of the perturbation formulas can be summarized as
\[
\boxed{
\text{Small spectral gap amplifies eigenspace sensitivity.}
}
\]

More explicitly,
\[
\left\|
\frac{\partial \psi_i}{\partial \theta_j}
\right\|
\lesssim
\frac{\|\partial_j K\|}{\operatorname{gap}_i(\theta)},
\qquad
\left\|
\frac{\partial P_i}{\partial \theta_j}
\right\|
\lesssim
\frac{\|\partial_j K\|}{\operatorname{gap}_i(\theta)}.
\]

The exact constants are secondary. What matters is the inverse power of the gap.

## 26. Minimal Analytical Summary

The analytical layer adds three indispensable facts:

1. eigenvalues vary by Rayleigh quotients;
2. eigenvectors vary by cross-mode coupling divided by spectral separation;
3. projectors inherit the same inverse-gap instability in a canonical form.

This completes the minimal perturbative structure of the framework.

---

# Phase IV — Geometric Layer (Spectral Geometry)

## 27. Geometric Object

The fundamental geometric object is now the spectral projector map
\[
\boxed{
P_i:\theta\mapsto P_i(\theta).
}
\]

For a simple eigenvalue, \(P_i(\theta)\) is a rank-one orthogonal projector satisfying
\[
P_i(\theta)^2=P_i(\theta),\qquad
P_i(\theta)^\top=P_i(\theta),\qquad
\operatorname{Tr}P_i(\theta)=1.
\]

The set of all rank-one orthogonal projectors is naturally identified with real projective space:
\[
\boxed{
\mathbb{RP}^{n-1}.
}
\]

Indeed, a line \([\psi]\in \mathbb{RP}^{n-1}\) corresponds exactly to the projector \(\psi\psi^\top\). Thus the spectral problem defines a map from parameter space into projective space.

## 28. Tangent Structure

From the projector derivative formula,
\[
\frac{\partial P_i}{\partial \theta_j}
=
\sum_{m\neq i}
\frac{\psi_m^\top(\partial_j K)\psi_i}{\lambda_i-\lambda_m}
(\psi_m\psi_i^\top+\psi_i\psi_m^\top).
\]

This shows that tangent vectors to the projector manifold are built from cross-mode projectors. Geometrically, a change in the eigenspace is achieved by rotating weight from the active line into complementary directions.

The associated norm bound
\[
\boxed{
\left\|
\frac{\partial P_i}{\partial \theta_j}
\right\|
\le
\frac{2\|\partial_j K\|}{\operatorname{gap}_i(\theta)}
}
\]
implies that the tangent structure becomes singular as the gap collapses.

## 29. Metric Structure

Define the pullback metric on parameter space by
\[
\boxed{
g_{jk}(\theta)=
\operatorname{Tr}\!\left(
\frac{\partial P_i}{\partial \theta_j}
\frac{\partial P_i}{\partial \theta_k}
\right).
}
\]

This is the natural metric induced by the embedding of the projector manifold into the space of matrices. It measures how rapidly the eigenspace changes under parameter variation.

Interpretationally:

- \(g_{jj}\) measures squared speed in the \(\theta_j\)-direction;
- mixed terms \(g_{jk}\) capture directional coupling in parameter space.

Large values of \(g\) indicate rapid rotation of the eigenspace. Thus the induced metric gives a quantitative version of “transition steepness.”

## 30. Curvature / Second Variation

The second derivative
\[
\frac{\partial^2 P_i}{\partial \theta_j\partial \theta_k}
\]
measures nonlinear bending of the projector map. Differentiating the first-order perturbation formulas shows that the dominant small-gap scaling is
\[
\boxed{
\left\|
\frac{\partial^2 P_i}{\partial \theta^2}
\right\|
\sim
\frac{\|\partial K\|^2}{\operatorname{gap}^2}
}
\]
up to additional lower-order terms involving \(\partial^2 K\).

Thus second variation is typically more singular than first variation. Intuitively, once a map is already steep due to inverse-gap scaling, its bending becomes even more pronounced under further differentiation.

## 31. Geometric Transition Criterion

The transition region can now be stated geometrically:
\[
\boxed{
\mathcal M_i
=
\left\{
\theta:\,
\operatorname{gap}_i(\theta)\ \text{small},
\quad
g(\theta)\ \text{large}
\right\}.
}
\]

At the level of scaling,
\[
\boxed{
g(\theta)\sim \frac{\|\partial K\|^2}{\operatorname{gap}^2}.
}
\]

This formulation is sharper than one based on eigenvalues alone. It says that the relevant transition set is not merely where eigenvalues are close, but where the projector map becomes metrically steep.

## 32. Path Geometry (Adiabatic Motion)

Let \(\theta=\theta(t)\) be a smooth path in parameter space. Then
\[
P_i(t)=P_i(\theta(t))
\]
and
\[
\frac{dP_i}{dt}
=
\sum_j
\frac{\partial P_i}{\partial \theta_j}\dot\theta_j.
\]

If
\[
\dot K=\sum_j (\partial_j K)\dot\theta_j,
\]
then
\[
\boxed{
\left\|\frac{dP_i}{dt}\right\|
\le
\frac{2\|\dot K\|}{\operatorname{gap}_i}.
}
\]

This estimate links geometric variation directly to dynamical parameter motion. It implies:

- large gap + slow motion \(\Rightarrow\) stable eigenspace evolution;
- small gap \(\Rightarrow\) rapid mode variation remains possible even under slow forcing.

## 33. Two-Mode Normal Form (Geometric)

Near a two-mode interaction,
\[
K\sim
\begin{pmatrix}
\lambda & \epsilon\\
\epsilon & \lambda+\delta
\end{pmatrix}.
\]

Then the eigenspace geometry is captured by
\[
\tan(2\phi)=\frac{2\epsilon}{\delta}.
\]

This is the universal local geometry: spectral transition is projective rotation in a two-dimensional plane. The entire higher-dimensional theory reduces locally to this one formula when a single pair of modes dominates the transition.

## 34. Avoided Crossing Geometry

When two eigenvalues approach but do not meet exactly,
\[
\lambda_1\approx \lambda_2,
\]
one observes the characteristic pattern of avoided crossing:

- eigenvalue graphs repel;
- eigenvectors rotate sharply;
- the projector trajectory bends strongly.

The key fact is
\[
\boxed{
\text{maximum rotation occurs where the spectral gap is minimal.}
}
\]

Thus avoided crossing is not merely a spectral picture. It is the geometric signature of near-degeneracy.

## 35. Degenerate Case (Higher Rank)

At exact gap closure, individual projectors become ill-defined. The correct object is the cluster projector
\[
\boxed{
P_{\mathcal C}=\sum_{m\in\mathcal C} P_m,
}
\]
where \(\mathcal C\) indexes the degenerate spectral cluster.

This object remains canonical even when the internal basis of the cluster is not. The singularity therefore lies in the attempt to separate the cluster into one-dimensional modes, not in the total invariant subspace itself.

## 36. Refined Core Principle (Geometric)

The geometric content of the framework may be summarized by
\[
\boxed{
\|dP_i\|\sim \frac{1}{\operatorname{gap}},
\qquad
\|d^2P_i\|\sim \frac{1}{\operatorname{gap}^2},
}
\]
modulo the size of matrix derivatives.

In words: first-order instability is controlled by inverse gap scaling, and second-order bending is controlled by inverse square gap scaling.

## 37. Minimal Geometric Summary

Parameter space is the base manifold. The spectral projector defines a map into projective space. The spectral gap controls the singularity of this map. Transition occurs where the map becomes steep and sharply curved.

This closes the geometric layer.

---

# Phase V — Boundary / Surface Layer

## 38. Bulk–Boundary Decomposition

Assume that the finite-dimensional state space admits an orthogonal decomposition
\[
\mathcal H=\mathcal H_{\mathrm{bulk}}\oplus \mathcal H_{\partial}.
\]

Let
\[
\Pi_{\mathrm{bulk}},\qquad \Pi_{\partial}
\]
denote the corresponding orthogonal projectors.

For a normalized eigenvector \(\psi_i(\theta)\), define the boundary weight
\[
\boxed{
B_i(\theta)=\|\Pi_{\partial}\psi_i(\theta)\|^2
}
\]
and the bulk weight
\[
\boxed{
Q_i(\theta)=\|\Pi_{\mathrm{bulk}}\psi_i(\theta)\|^2=1-B_i(\theta).
}
\]

These are the first boundary observables. They measure how strongly a mode lives on the distinguished boundary subspace as opposed to the bulk.

## 39. Boundary Projector of a Mode

For the spectral projector
\[
P_i(\theta)=\psi_i(\theta)\psi_i(\theta)^\top,
\]
define the boundary restriction
\[
\boxed{
P_i^\partial(\theta)=\Pi_{\partial}P_i(\theta)\Pi_{\partial}.
}
\]

Then
\[
\operatorname{Tr}(P_i^\partial)=B_i(\theta).
\]

Thus total boundary weight is encoded directly as the trace of the boundary-compressed projector. This is the natural boundary analogue of the projector formalism developed in Phases III and IV.

## 40. Boundary Participation Functional

In a basis adapted to the bulk-boundary decomposition, define
\[
\boxed{
\mathcal I_{\partial}(\psi_i)
=
\sum_{j\in \partial\Omega} |\psi_{i,j}|^4.
}
\]

This quantity refines boundary support. The total boundary weight \(B_i\) records how much of the mode lies on the boundary, but does not distinguish between:

- a mode spread broadly along the boundary,
- a mode concentrated on a few boundary sites.

The quartic functional \(\mathcal I_\partial\) separates these regimes. Large \(B_i\) with small \(\mathcal I_\partial\) corresponds to boundary support that is delocalized across the boundary. Large \(B_i\) with large \(\mathcal I_\partial\) corresponds to concentration on a small boundary subset.

## 41. Boundary-Sensitive Transition Region

To detect transitions controlled specifically by boundary-supported modes, define
\[
\boxed{
\mathcal M_i^\partial(\eta,\beta)
=
\left\{
\theta:\,
\operatorname{gap}_i(\theta)\le \eta,
\quad
B_i(\theta)\ge \beta
\right\}.
}
\]

Here \(\eta\) is a near-degeneracy threshold and \(\beta\) is a boundary-dominance threshold. This definition refines the earlier mixed regime by requiring not only small spectral gap, but significant boundary concentration.

## 42. Boundary Sensitivity Formula

Differentiate
\[
B_i(\theta)=\langle \psi_i,\Pi_{\partial}\psi_i\rangle.
\]

Then
\[
\frac{\partial B_i}{\partial \theta_j}
=
2\,\Re\left\langle
\frac{\partial \psi_i}{\partial \theta_j},
\Pi_{\partial}\psi_i
\right\rangle.
\]

Substituting the eigenvector derivative formula gives
\[
\boxed{
\frac{\partial B_i}{\partial \theta_j}
=
2\Re\sum_{m\neq i}
\frac{\psi_m^\top(\partial_j K)\psi_i}{\lambda_i-\lambda_m}
\langle \psi_m,\Pi_{\partial}\psi_i\rangle.
}
\]

This identity is the boundary analogue of the projector sensitivity formula. It shows explicitly that boundary-weight variation is built from mode coupling, overlap with the boundary component, and inverse spectral separation.

## 43. Boundary Sensitivity Bound

By Cauchy–Schwarz,
\[
\left|
\frac{\partial B_i}{\partial \theta_j}
\right|
\le
2
\left\|
\frac{\partial \psi_i}{\partial \theta_j}
\right\|
\,
\|\Pi_{\partial}\psi_i\|.
\]

Using
\[
\|\Pi_{\partial}\psi_i\|=\sqrt{B_i(\theta)}
\]
and the eigenvector sensitivity bound
\[
\left\|
\frac{\partial \psi_i}{\partial \theta_j}
\right\|
\le
\frac{\|\partial_j K(\theta)\|}{\operatorname{gap}_i(\theta)},
\]
one obtains
\[
\boxed{
\left|
\frac{\partial B_i}{\partial \theta_j}
\right|
\le
\frac{2\|\partial_j K(\theta)\|}{\operatorname{gap}_i(\theta)}
\sqrt{B_i(\theta)}.
}
\]

This is the basic boundary estimate. It states that boundary concentration becomes highly sensitive in the same small-gap regime that destabilizes eigenspace geometry.

## 44. Surface-Dominated Instability Principle

The instability principle can now be refined:
\[
\boxed{
\text{Near-degeneracy amplifies not only eigenspace sensitivity, but also boundary-weight sensitivity.}
}
\]

Equivalently, if the gap is small, then \(|\partial_{\theta_j}B_i|\) can become large. Thus transition may be bulk-dominated, boundary-dominated, or mixed depending on where the modal weight concentrates and how that concentration changes.

## 45. Surface-to-Volume Scaling Regimes

Suppose the system size grows and the mode family \(\psi_i^{(N)}\) is indexed by size \(N\). Then the asymptotic behavior of
\[
B_i^{(N)}=\|\Pi_{\partial}^{(N)}\psi_i^{(N)}\|^2
\]
classifies support relative to the bulk-boundary decomposition:

- **bulk regime**:
  \[
  B_i^{(N)}\to 0;
  \]
- **boundary regime**:
  \[
  B_i^{(N)}\to c>0;
  \]
- **pure surface regime**:
  \[
  B_i^{(N)}\to 1.
  \]

This is an asymptotic classification of spectral modes by support distribution.

## 46. Boundary-Projected Cluster Projectors

Near exact degeneracy, the correct object is not \(P_i\) but the cluster projector
\[
P_{\mathcal C}=\sum_{m\in\mathcal C}P_m.
\]

Its boundary restriction is
\[
\boxed{
P_{\mathcal C}^{\partial}
=
\Pi_{\partial}P_{\mathcal C}\Pi_{\partial}.
}
\]

The trace of this matrix gives the total boundary weight of the nearly degenerate cluster. This is the right boundary observable when individual modes lose canonical meaning.

## 47. Refined Geometric Picture

There are now three coupled layers of structure:

1. **Spectral geometry**, governed by \(P_i\).
2. **Boundary geometry**, governed by \(P_i^\partial\).
3. **Transition geometry**, governed jointly by
   - small spectral gap,
   - large projector derivative,
   - large boundary weight or large boundary sensitivity.

A natural transition set is therefore
\[
\boxed{
\mathcal T_i
=
\left\{
\theta:\,
\operatorname{gap}_i(\theta)\ \text{small},
\;
\|\nabla P_i(\theta)\|\ \text{large},
\;
B_i(\theta)\ \text{large or rapidly varying}
\right\}.
}
\]

This combines the spectral, geometric, and surface layers into one criterion.

## 48. Refined Core Statement

The full framework can now be summarized by
\[
\boxed{
\text{Mode transition is governed by spectral projector geometry; surface effects enter through boundary-projected projectors and their gap-amplified sensitivity.}
}
\]

This statement contains every previous phase in compressed form: reduced two-mode structure, analytical inverse-gap bounds, geometric steepness of the projector map, and boundary observables derived from compressed projectors.

## 49. Minimal Package for the Boundary Layer

A complete minimal boundary layer consists of:

- the bulk-boundary decomposition
  \[
  \mathcal H=\mathcal H_{\mathrm{bulk}}\oplus \mathcal H_{\partial};
  \]
- the bulk and boundary weights
  \[
  Q_i,\ B_i;
  \]
- the boundary projector
  \[
  P_i^\partial=\Pi_{\partial}P_i\Pi_{\partial};
  \]
- the boundary participation functional
  \[
  \mathcal I_\partial;
  \]
- the boundary sensitivity identity;
- the boundary sensitivity bound.

Nothing further is required for the minimal theory. Any deeper surface analysis would be an extension, not a structural necessity.

## 50. One-Line Summary

> Boundary effects are encoded by restricting spectral projectors to the boundary subspace, and near small spectral gap these boundary observables vary rapidly enough to shape the transition geometry.

---

# Conclusion

Across Phases II–V, a unified picture emerges. A smooth symmetric matrix family determines spectral data that may reorganize sharply in narrow parameter regions. The primary mechanism is the collapse of spectral separation. Analytical perturbation theory shows that eigenvector and projector sensitivity scale inversely with gap. Geometric reformulation shows that the projector map into projective space becomes steep and sharply bent in the same regime. Boundary compression shows that surface observables inherit this same amplification principle.

The reduced \(2\times 2\) model identifies the local normal form of pairwise transition. The projector formalism lifts this to arbitrary finite dimension. The boundary layer adds a distinguished subspace without altering the underlying mechanism. Thus the entire framework is governed by a single mathematical principle:

\[
\boxed{
\text{small spectral gap amplifies geometric and boundary sensitivity of spectral projectors.}
}
\]

This gives a complete minimal theory stack for mode transition in finite-dimensional symmetric systems.

# Compact Proposition Package

For convenience, we record the main formulas in theorem-style form.

## Proposition A (Eigenvalue sensitivity)

If \(K(\theta)\) is \(C^1\) and \(\lambda_i(\theta)\) is simple, then
\[
\frac{\partial \lambda_i}{\partial \theta_j}
=
\psi_i^\top(\partial_j K)\psi_i.
\]

## Proposition B (Eigenvector sensitivity)

If \(K(\theta)\) is \(C^1\), \(\lambda_i(\theta)\) is simple, and the gauge condition
\[
\psi_i^\top \frac{\partial \psi_i}{\partial \theta_j}=0
\]
is imposed, then
\[
\frac{\partial \psi_i}{\partial \theta_j}
=
\sum_{m\neq i}
\frac{\psi_m^\top(\partial_j K)\psi_i}{\lambda_i-\lambda_m}\,\psi_m.
\]

## Corollary C (Gap bound)

Under the assumptions of Proposition B,
\[
\left\|
\frac{\partial \psi_i}{\partial \theta_j}
\right\|
\le
\frac{\|\partial_j K\|}{\operatorname{gap}_i(\theta)}.
\]

## Proposition D (Projector derivative)

If \(\lambda_i\) is simple, then
\[
\frac{\partial P_i}{\partial \theta_j}
=
\sum_{m\neq i}
\frac{\psi_m^\top(\partial_j K)\psi_i}{\lambda_i-\lambda_m}
(\psi_m\psi_i^\top+\psi_i\psi_m^\top).
\]

## Corollary E (Projector gap bound)

\[
\left\|
\frac{\partial P_i}{\partial \theta_j}
\right\|
\le
\frac{2\|\partial_j K\|}{\operatorname{gap}_i(\theta)}.
\]

## Proposition F (Boundary sensitivity)

For
\[
B_i(\theta)=\|\Pi_{\partial}\psi_i(\theta)\|^2,
\]
one has
\[
\frac{\partial B_i}{\partial \theta_j}
=
2\Re\sum_{m\neq i}
\frac{\psi_m^\top(\partial_j K)\psi_i}{\lambda_i-\lambda_m}
\langle \psi_m,\Pi_{\partial}\psi_i\rangle.
\]

## Corollary G (Boundary gap bound)

\[
\left|
\frac{\partial B_i}{\partial \theta_j}
\right|
\le
\frac{2\|\partial_j K(\theta)\|}{\operatorname{gap}_i(\theta)}
\sqrt{B_i(\theta)}.
\]

# Final Summary

The minimal theory can be read in one sentence:

> A parametrized symmetric operator defines spectral projectors whose first and second variations scale like inverse powers of the spectral gap; when a bulk-boundary decomposition is present, the same inverse-gap mechanism controls boundary concentration and its instability.

