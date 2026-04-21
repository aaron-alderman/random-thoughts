# Spectral Framework for Mode Transition (Simplified)

## 0. Purpose

This note gives a simplified version of the spectral framework.

The full framework studies smooth families of real symmetric matrices

$$
K(\theta)\in \mathrm{Sym}(n,\mathbb{R}),
\qquad
\theta\in\mathbb{R}^k.
$$

The goal is to understand when the important modes of the system change,
mix, or reorganize as the parameters $\theta$ vary.

The central idea is:

$$
\text{mode transition is controlled by small spectral gaps and rapid eigenspace motion.}
$$

---

## 1. The Basic Object

A parameter value $\theta$ chooses a matrix $K(\theta)$.

For each value of $\theta$, we solve the eigenvalue problem

$$
K(\theta)\psi_i(\theta)=\lambda_i(\theta)\psi_i(\theta).
$$

Here:

- $\lambda_i(\theta)$ is an eigenvalue;
- $\psi_i(\theta)$ is an eigenvector, or mode;
- the eigenvalues are usually ordered as

$$
\lambda_1(\theta)\ge \lambda_2(\theta)\ge \cdots \ge \lambda_n(\theta).
$$

The dominant mode is usually associated with $\lambda_1$, but the identity
of that mode can become unstable when another eigenvalue comes close to it.

---

## 2. What Counts as a Mode Transition?

A mode transition occurs when the modal structure changes quickly as
$\theta$ changes.

This can mean:

- the leading eigenvalue becomes close to another eigenvalue;
- the leading eigenvector rotates rapidly;
- a mode changes from one basis direction to a mixture of directions;
- a mode shifts from the bulk of the system toward a boundary subspace.

The important point is that transition is not just a change in eigenvalues.
It is a change in the geometry of the eigenvectors or eigenspaces.

---

## 3. The Minimal Two-Mode Model

The simplest local model is a real symmetric $2\times 2$ matrix:

$$
K(\theta)=
\begin{pmatrix}
a_1(\theta) & b(\theta)\\
b(\theta) & a_2(\theta)
\end{pmatrix}.
$$

Define the diagonal imbalance

$$
\Delta(\theta)=a_1(\theta)-a_2(\theta).
$$

The eigenvalues are

$$
\lambda_\pm(\theta)=
\frac{a_1+a_2}{2}
\pm
\sqrt{\left(\frac{\Delta}{2}\right)^2+b^2}.
$$

This model has two competing effects:

- $\Delta$ separates the two modes;
- $b$ mixes the two modes.

When only two modes are close and all other modes are well separated, the
larger system locally behaves like this two-mode model.

---

## 4. The Spectral Gap

The gap between the two eigenvalues is

$$
\Delta_\lambda(\theta)=
\lambda_+(\theta)-\lambda_-(\theta)=
2\sqrt{\left(\frac{\Delta}{2}\right)^2+b^2}.
$$

The gap is small when both the diagonal imbalance and the mixing scale are
small enough to bring the two eigenvalues near each other.

Small gap matters for two reasons:

- it means two eigenvalues are close;
- it amplifies changes in eigenvectors.

The second point is the deeper one. A small gap makes modal identity unstable.

---

## 5. Three Main Regimes

| Regime | Condition | Meaning |
| --- | --- | --- |
| Detuning-dominated | $\lvert\Delta\rvert \gg \lvert b\rvert$ | Modes stay close to the original basis directions |
| Mixing-dominated | $\lvert b\rvert \gg \lvert\Delta\rvert$ | Modes are strongly hybridized |
| Mixed/transition region | $\lvert\Delta\rvert \sim \lvert b\rvert$, with a small gap on the relevant scale | Neither effect dominates; modes can reorganize rapidly |

There is also an exact degeneracy when

$$
\Delta=0,
\qquad
b=0.
$$

At exact degeneracy, the two eigenvalues coincide and individual eigenvectors
are not uniquely defined. Only the two-dimensional eigenspace is well defined.

Comparability by itself means the two mechanisms compete. The transition is
sharpest when that competition also occurs near a small spectral gap.

---

## 6. Eigenvector Rotation

In the two-mode model, write a normalized eigenvector as

$$
\psi(\theta)=
\begin{pmatrix}
\cos\phi(\theta)\\
\sin\phi(\theta)
\end{pmatrix}.
$$

The mixing angle satisfies

$$
\tan 2\phi(\theta)=\frac{2b(\theta)}{\Delta(\theta)}.
$$

This formula makes the transition visible.

When $\lvert\Delta\rvert$ is large compared with $\lvert b\rvert$, the angle changes slowly and
the mode stays near a basis direction. When the gap is small, the same
parameter change can produce a much larger rotation of $\psi$.

---

## 7. Sensitivity

A basic sensitivity measure is

$$
S(\theta)=
\left\|
\frac{\partial\psi}{\partial\theta}
\right\|.
$$

In general perturbation theory, for an isolated eigenvalue,

$$
\frac{\partial \psi_i}{\partial \theta_\alpha}=
\sum_{j\ne i}
\frac{
\left\langle
\psi_j,
\left(\partial_{\theta_\alpha}K\right)\psi_i
\right\rangle
}{
\lambda_i-\lambda_j
}
\psi_j.
$$

The important feature is the denominator:

$$
\lambda_i-\lambda_j.
$$

As another eigenvalue approaches $\lambda_i$, this denominator becomes small.
Therefore eigenvector sensitivity can become large.

In simplified form:

$$
\text{small gap}
\quad\Longrightarrow\quad
\text{large possible eigenvector response}.
$$

This is the core mechanism of mode transition.

---

## 8. Projectors: The Better Geometric Object

Eigenvectors have a sign ambiguity: $\psi$ and $-\psi$ represent the same
direction.

To remove this ambiguity, use the rank-one spectral projector

$$
P_i(\theta)=\psi_i(\theta)\psi_i(\theta)^\top.
$$

The projector tracks the eigendirection rather than a signed vector.

So the geometric object is the map

$$
\theta\mapsto P_i(\theta).
$$

Near a small spectral gap, the projector can move rapidly:

$$
\|dP_i\|
\sim
\frac{\|dK\|}{\text{gap}}.
$$

Higher derivatives can be even more singular, often scaling like higher powers
of the inverse gap. This is why the transition region can look sharply curved
or unstable in parameter space.

---

## 9. Concentration and Mixing

A simple basis-dependent measure of concentration is

$$
\mathcal I(\theta)=
\sum_{\ell=1}^n |\psi_\ell(\theta)|^4.
$$

In the two-mode case,

$$
\mathcal I=
\cos^4\phi+\sin^4\phi=
\frac12+\frac12\cos^2(2\phi).
$$

Interpretation:

- $\mathcal I=1$ means the mode is concentrated in one basis direction;
- $\mathcal I=\frac12$ means the mode is evenly mixed between two directions.

This is not an intrinsic spectral invariant. It depends on the chosen basis.
But it is useful when that basis represents meaningful components of the
system.

---

## 10. Avoided Crossing

In many parameter families, two eigenvalues approach but do not actually cross.
This is an avoided crossing.

Near an avoided crossing:

- the eigenvalues come close;
- the eigenvectors rotate;
- the projectors change fastest near the smallest gap.

The spectral gap identifies the location of the transition, while the
projector motion describes what changes geometrically.

---

## 11. Bulk-Boundary Decomposition

Suppose the state space splits into a bulk part and a boundary part:

$$
\mathcal H=
\mathcal H_{\mathrm{bulk}}
\oplus
\mathcal H_{\partial}.
$$

Let $\Pi_{\partial}$ be the orthogonal projector onto the boundary subspace.

For a mode $\psi_i$, define the boundary weight

$$
B_i(\theta)=\|\Pi_{\partial}\psi_i(\theta)\|^2.
$$

Equivalently, using the spectral projector,

$$
B_i(\theta)=\operatorname{tr}\left(\Pi_{\partial}P_i(\theta)\right).
$$

Interpretation:

- $B_i\approx 0$: the mode is mostly bulk-supported;
- $B_i\approx 1$: the mode is mostly boundary-supported.

Because $B_i$ depends on $\psi_i$ or $P_i$, it inherits the same
small-gap sensitivity. Near a transition, boundary weight can change rapidly.

---

## 12. Types of Transition

| Type | Description |
| --- | --- |
| Spectral transition | Eigenvalues approach or reorder |
| Geometric transition | Eigenvectors or projectors rotate rapidly |
| Mixing transition | A mode changes from localized to hybridized |
| Boundary transition | A mode shifts weight between bulk and boundary |

These are not mutually exclusive. In the framework, they are different
observations of the same small-gap mechanism.

---

## 13. Minimal Working Procedure

To analyze a concrete model:

1. Specify the parameter-dependent matrix $K(\theta)$.
2. Compute the eigenvalues $\lambda_i(\theta)$.
3. Compute the eigenvectors $\psi_i(\theta)$ or projectors $P_i(\theta)$.
4. Track the relevant spectral gap:

$$
g_i(\theta)=
\min_{j\ne i}
\lvert\lambda_i(\theta)-\lambda_j(\theta)\rvert.
$$

5. Measure eigenvector or projector sensitivity:

$$
\left\|
\frac{\partial\psi_i}{\partial\theta}
\right\|,
\qquad
\left\|
\frac{\partial P_i}{\partial\theta}
\right\|.
$$

6. If a bulk-boundary split is present, compute

$$
B_i(\theta)=\operatorname{tr}\left(\Pi_{\partial}P_i(\theta)\right).
$$

7. Identify regions where the gap is small and the modes or boundary weights
change quickly.

---

## 14. Short Summary

The simplified framework is:

$$
K(\theta)
\longrightarrow
\{\lambda_i(\theta),\psi_i(\theta),P_i(\theta)\}
\longrightarrow
\text{gap, sensitivity, and boundary weight}.
$$

Small gaps do not only make eigenvalues close. They make eigenspaces sensitive.
That sensitivity is what produces mode transition.

---

## 15. One-Line Takeaway

Mode transitions occur when small spectral gaps make eigenvectors, projectors,
or boundary weights change rapidly as parameters vary.
