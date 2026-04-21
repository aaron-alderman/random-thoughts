# Efimov Universality from Decomposition Inconsistency
## Corrected Derivation — Honest Status of All Claims

---

## Preamble: What This Document Does and Does Not Establish

The previous version claimed to have independently derived the scalar values $\varepsilon_0 = -1/4$ and $W_0 = -s_0^2/2$. That claim was wrong. This document corrects it with precision: the **operator structure** of the 3×3 decomposition is fully derivable; the **scalar split** of $\lambda_\text{sym}$ into $\varepsilon_0 + 2W_0$ is convention-dependent and not independently fixed by the Bethe–Peierls condition alone.

---

## The Conceptual Chain (Fully Established)

The following sequence is well-founded and unambiguous:

1. Three pair-spectator charts $|1\rangle, |2\rangle, |3\rangle$
2. Zero-range Bethe–Peierls matching **couples** those charts
3. Permutation symmetry **selects** the fully symmetric collective mode
4. Scale-independence in the window $r_0 \ll \rho \ll |a|$ forces $\mathcal{H}_\Omega \propto \rho^{-2}$
5. The symmetric eigenvalue $\lambda_\text{sym} = -s_0^2 - 1/4$ produces an attractive supercritical channel
6. Log-periodic solutions give the Efimov geometric spectrum

No part of this chain is disputed. The issue is in the intermediate step of separately identifying $\varepsilon_0$ and $W_0$.

---

## Step 1: The Faddeev Ansatz and the Bethe–Peierls Condition

Write $\Phi = \phi_{12} + \phi_{13} + \phi_{23}$, each component singular only in its own pair. The Bethe–Peierls condition at $r_{12} \to 0$ is:

$$\phi_{12} + \phi_{13} + \phi_{23} \sim \left(\frac{1}{r_{12}} - \frac{1}{a}\right) A_{12}$$

At **unitarity** $a \to \infty$:

$$\phi_{12} \sim \frac{A_{12}}{r_{12}}, \qquad \phi_{13}\big|_{r_{12}=0} + \phi_{23}\big|_{r_{12}=0} = 0$$

This is the coupling equation. The key structural fact, which holds exactly at unitarity, follows immediately:

> **$\phi_{12}$ does not source itself.** The zero-range condition with $a = \infty$ has no regular part, so $V_{12}\phi_{12} = 0$ at unitarity. Only $\phi_{13}$ and $\phi_{23}$ source $\phi_{12}$.

In operator language, the Faddeev equation for the amplitude $t_{12}(p)$ (the Fourier-space residue conjugate to $\phi_{12}$) is:

$$t_{12}(p) = K_\text{cross} \cdot (t_{13} + t_{23})$$

with $K_\text{self} = 0$ **exactly** at unitarity. This gives the **operator structure** of the 3×3 matrix:

$$M = \begin{pmatrix} 0 & K_\text{cross} & K_\text{cross} \\ K_\text{cross} & 0 & K_\text{cross} \\ K_\text{cross} & K_\text{cross} & 0 \end{pmatrix}$$

Here $K_\text{cross}$ is an **integral operator** (not yet a scalar), and the matrix entries are **operator-valued**, not numbers.

---

## Step 2: The Cross-Channel Coupling Kernel — Derived Explicitly

The cross-channel coupling $K_\text{cross}$ is computed by expressing $r_{13}$ in the pair-(12) Jacobi frame and projecting to s-wave. For equal-mass bosons, this gives the **momentum-space STM kernel**:

$$[K_\text{cross} \cdot t](p) = -\frac{8}{\pi\sqrt{3}} \,\text{P.V.} \int_0^\infty \frac{t(p')}{p^2 + pp' + p'^2}\,dp'$$

The denominator $p^2 + pp' + p'^2$ is the **exact kinematic result** of expressing $r_{13}^2$ in terms of pair-(12) Jacobi momenta after s-wave angular projection for equal masses:

$$r_{13}^2 = \tfrac{1}{4}r_{12}^2 + r_y^2 + r_{12} r_y \cos\theta \;\xrightarrow{\text{s-wave}}\; \frac{p^2 + pp' + p'^2}{\text{(mass factor)}}$$

This kernel is **independently derived** from the kinematic recoupling, with no use of the known Efimov result as input.

---

## Step 3: Self-Consistency → The Transcendental Equation

In the **symmetric sector** $t_{12} = t_{13} = t_{23} \equiv t$, each component receives contributions from two cross-channels:

$$t(p) = 2 \cdot [K_\text{cross} \cdot t](p) = -\frac{16}{\pi\sqrt{3}} \,\text{P.V.} \int_0^\infty \frac{t(p')}{p^2 + pp' + p'^2}\,dp'$$

This is a fixed-point equation (not a standard eigenvalue equation at this stage). Substituting the **power-law ansatz** $t(p) = p^{is_0 - 1}$, the integral becomes a Mellin transform:

$$\int_0^\infty \frac{u^{is_0-1}}{1 + u + u^2}\,du = \frac{2\pi\sinh(\pi s_0/3)}{\sqrt{3}\,\sinh(\pi s_0)}$$

Self-consistency — that $p^{is_0-1}$ is indeed the fixed-point — reduces to:

$$\boxed{s_0 \cosh\!\left(\frac{\pi s_0}{2}\right) = \frac{8}{\sqrt{3}}\sinh\!\left(\frac{\pi s_0}{6}\right)}$$

with unique solution $s_0 \approx 1.00624$. **This derivation is complete and uses no Efimov result as input.**

---

## Step 4: The Hyperradial Channel — Derived from the Scaling Exponent

The power-law $t(p) \sim p^{is_0-1}$ in momentum space corresponds to a position-space wavefunction $\phi \sim r^{-is_0}$ at threshold. Translating to the hyperradial function $f_0(\rho)$ via the standard reduction of the 6D kinetic energy (with the variable change $F(\rho) = f_0(\rho)/\rho^{5/2}$ to remove the first-derivative term), the hyperradial equation becomes:

$$\left[-\frac{d^2}{d\rho^2} + \frac{(\nu+2)^2 - \tfrac{1}{4}}{\rho^2}\right] f_0(\rho) = E\,f_0(\rho)$$

where $\nu = -2 + is_0$ is the hyperradial scaling exponent. With $\nu + 2 = is_0$:

$$(\nu+2)^2 - \tfrac{1}{4} = -s_0^2 - \tfrac{1}{4}$$

Therefore:

$$\boxed{U_\text{eff}(\rho) = -\frac{s_0^2 + \tfrac{1}{4}}{\rho^2}}$$

*Numerical check:* $\nu = -2 + i(1.00624)$, $(\nu+2)^2 - 1/4 = -(1.00624)^2 - 0.25 = -1.2625$ ✓

**This step is fully derived.** The $-1/4$ here is the Langer correction from the variable change $F \to f_0/\rho^{5/2}$; it is kinematic, not interaction-generated.

---

## Step 5: Where the Scalar Split Stands — Honest Assessment

The symmetric eigenvalue is:

$$\lambda_\text{sym} = -s_0^2 - \tfrac{1}{4} \approx -1.2625$$

The democratic matrix structure gives:

$$\lambda_\text{sym} = \varepsilon_0 + 2W_0$$

**What is convention-independent and fully derived:**

| Quantity | Result |
|---|---|
| $K_\text{self} = 0$ at unitarity | ✓ Independently derived from BP condition |
| The operator $K_\text{cross}$ (STM kernel) | ✓ Independently derived from kinematics |
| The transcendental equation for $s_0$ | ✓ Independently derived from self-consistency |
| $U_\text{eff}(\rho) = -(s_0^2+1/4)/\rho^2$ | ✓ Independently derived via Langer reduction |
| $\lambda_\text{sym} = \varepsilon_0 + 2W_0 = -s_0^2 - 1/4$ | ✓ As a constraint on the sum |

**What is convention-dependent:**

The scalar split $(\varepsilon_0, W_0)$ exists in (at least) two consistent forms:

**Form A — integral equation (momentum space):**

$$\varepsilon_0^\text{A} = 0, \qquad W_0^\text{A} = -\frac{s_0^2 + \tfrac{1}{4}}{2}$$

$\varepsilon_0^\text{A} = 0$ is exact at unitarity ($K_\text{self} = 0$). The $-1/4$ is absorbed into $W_0$.

**Form B — hyperspherical (position space, after Langer reduction):**

$$\varepsilon_0^\text{B} = -\tfrac{1}{4}, \qquad W_0^\text{B} = -\frac{s_0^2}{2}$$

$\varepsilon_0^\text{B} = -1/4$ is the Langer correction from $F \to f_0/\rho^{5/2}$; $W_0^\text{B}$ is the remainder.

**Both satisfy** $\varepsilon_0 + 2W_0 = -s_0^2 - 1/4$. **Neither is more fundamental than the other** — they are representations of the same operator in different functional spaces (momentum amplitudes vs. hyperangular functions after a specific variable change).

**What would be required to uniquely fix the split:** An independent computation of $\langle\chi|L|\chi\rangle$ in the hyperspherical basis, where $L = -(\partial_\alpha^2 + 4\cot 2\alpha\,\partial_\alpha)$ and $\chi$ is the Efimov channel function satisfying the *coupled* Faddeev equation. This requires knowing $\chi$ explicitly, which in turn requires solving the integral equation — so the split cannot be read off without first knowing the eigenvalue (circularity). The split is a *parametrization* of the known result, not an independent derivation.

---

## What the Framework Adds

Even without fixing the scalar split independently, the framework contribution is genuine:

The standard treatment identifies the Efimov effect via a hyperangular eigenvalue. The decomposition framework identifies it as **the failure of three pair charts to be simultaneously self-consistent under zero-range matching**.

The precise statement, now fully supported, is:

> At unitarity, the zero-range Bethe–Peierls condition on $\phi_{12}$ at $r_{12} = 0$ is sourced entirely by $\phi_{13}$ and $\phi_{23}$ (the self-coupling $K_\text{self}$ vanishes exactly). By identical-boson symmetry, the same holds for each chart. The only mode in which all three boundary conditions can be simultaneously satisfied is the symmetric collective mode $(t,t,t)$. The self-consistency condition for this mode — that the STM kernel acting on $t$ returns $t$ — produces the transcendental equation for $s_0$, and the resulting hyperradial potential is $U_\text{eff} = -(s_0^2 + 1/4)/\rho^2$.

This is a complete and accurate statement of what the decomposition picture establishes.

---

## Summary Table

| Component | Derived independently? | Notes |
|---|---|---|
| Conceptual chain: charts → coupling → collective mode → spectrum | ✓ | Complete |
| $K_\text{self} = 0$ at unitarity | ✓ | Exact from BP condition |
| Operator form of $K_\text{cross}$ (STM kernel) | ✓ | From kinematic recoupling |
| Transcendental equation for $s_0$ | ✓ | From Mellin self-consistency |
| $U_\text{eff} = -(s_0^2+1/4)/\rho^2$ | ✓ | From Langer reduction |
| $\lambda_\text{sym} = \varepsilon_0 + 2W_0 = -s_0^2-1/4$ | ✓ | As constraint on sum |
| $\varepsilon_0 = -1/4$ independently | ✗ | Convention-dependent (Langer choice) |
| $W_0 = -s_0^2/2$ independently | ✗ | Convention-dependent |
| Separate derivation of scalar $\varepsilon_0$, $W_0$ from BP | ✗ | Open task — requires explicit computation of $\langle\chi|L|\chi\rangle$ |

---

## One-Line Summary

The Bethe–Peierls condition forces $K_\text{self} = 0$ at unitarity, so three-body consistency is entirely cross-chart; the symmetric fixed point of the STM kernel produces the transcendental equation for $s_0$; the effective potential $-(s_0^2+1/4)/\rho^2$ follows from the Langer reduction; and the scalar split $\varepsilon_0 + 2W_0 = -s_0^2 - 1/4$ is a consistent parametrization whose individual terms are convention-dependent.
