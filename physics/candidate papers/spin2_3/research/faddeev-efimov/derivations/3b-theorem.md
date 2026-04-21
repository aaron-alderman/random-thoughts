# 📄 Research Note

## Collective Eigenvalue Flow and Universality Classes in Few-Body Systems

---

## 1. Setup

Let (\mathcal D) denote the decomposition space of a few-body system (e.g. pair-spectator charts, cluster channels). Let
[
\mathcal O(\rho)
]
be the associated coupling operator after imposing physical constraints (symmetry, statistics, boundary conditions).

After projection onto the symmetry-allowed sector, assume the existence of a dominant collective branch with eigenvalue
[
\lambda_{\mathrm{coll}}(\rho).
]

---

## Definition 1 (Collective Eigenvalue Flow)

The function
[
\rho \mapsto \lambda_{\mathrm{coll}}(\rho)
]
is called the **collective eigenvalue flow**.

---

## 2. Radial Reduction

At zero energy, the asymptotic radial equation takes the form
[
\left[
-\frac{d^2}{d\rho^2}
+
\frac{\lambda_{\mathrm{coll}}(\rho)}{\rho^2}
\right] f(\rho) = 0.
]

Define the shifted eigenvalue
[
\Delta(\rho) := \lambda_{\mathrm{coll}}(\rho) + \frac14.
]

Then
[
U_{\mathrm{eff}}(\rho)
======================

## -\frac{1}{4\rho^2}

\frac{V(\rho)}{\rho^2},
\qquad
V(\rho) := -\Delta(\rho).
]

---

## Lemma 1 (Canonical Reduction)

Under the transformation
[
f(\rho) = \sqrt{\rho}, g(\rho),
]
the radial equation becomes
[
g''(\rho) + \frac{1}{\rho} g'(\rho) + \frac{V(\rho)}{\rho^2} g(\rho) = 0.
]

Thus the asymptotic behavior is determined entirely by (V(\rho)).

---

## 3. Asymptotic Oscillation Variables

We seek a change of variables
[
x = X(\rho)
]
such that the equation reduces asymptotically to
[
\frac{d^2 g}{dx^2} + \frac{c}{x^2} g = 0,
]
which produces oscillatory solutions.

---

## Definition 2 (Asymptotic Oscillation Variable)

A function (X(\rho)) is an **oscillation variable** if the asymptotic equation becomes oscillatory in (X).

---

## 4. Universality Classes

### Proposition 1 (Efimov Class)

If
[
\Delta(\rho) \to -s_0^2 < 0,
]
then the oscillation variable is
[
X(\rho) = \ln \rho,
]
and the spectrum is geometric:
[
E_n \sim e^{-2\pi n/s_0}.
]

---

### Proposition 2 (Super-Efimov Class)

If
[
\Delta(\rho) \sim -\frac{s_0^2}{\ln^2 \rho},
]
then the oscillation variable is
[
X(\rho) = \ln\ln \rho,
]
and the spectrum is doubly exponential:
[
E_n \sim \exp!\left(-2 e^{\pi n/s_0}\right).
]

---

### Proposition 3 (Finite Universal Class)

If
[
\Delta(\rho) = o!\left(\frac{1}{\ln^2 \rho}\right),
]
then no oscillatory asymptotic variable exists and the spectrum contains only finitely many universal bound states.

---

## 5. Threshold Condition

### Definition 3 (Universality Threshold)

A parameter value (\alpha_c) is a **threshold** if
[
\lambda_{\mathrm{coll}}(\rho;\alpha)
]
first produces real oscillatory solutions in some (X(\rho)).

---

### Proposition 4 (Unified Threshold Rule)

[
\boxed{
\text{Threshold} \iff
\text{onset of real oscillatory behavior in an asymptotic variable } X(\rho)
}
]

Examples:

* (X=\ln\rho) → Efimov threshold
* (X=\ln\ln\rho) → super-Efimov threshold

---

## 6. Control Parameters and Flow

Let (\alpha) denote a control parameter (e.g. mass ratio). Then
[
\lambda_{\mathrm{coll}}(\rho;\alpha)
]
defines a family of flows.

---

### Proposition 5 (Threshold as Flow Transition)

A universality threshold occurs when the asymptotic behavior of
[
\Delta(\rho;\alpha)
]
changes from non-oscillatory to oscillatory.

---

## 7. Mechanism

### Proposition 6 (Decomposition → Universality)

Decomposition inconsistency induces a collective eigenvalue flow
[
\lambda_{\mathrm{coll}}(\rho),
]
and universality is determined by the asymptotic behavior of
[
\lambda_{\mathrm{coll}}(\rho) + \frac14.
]

---

## 8. Interpretation

The framework replaces:

* static eigenvalue analysis
  with
* **scale-dependent spectral flow**

and replaces:

* “universality from symmetry”
  with
* “universality from asymptotic eigenvalue flow near criticality.”

---

## 9. Status of Results

### Established within framework

* canonical reduction to (V(\rho))
* derivation of Efimov and super-Efimov classes from asymptotics
* unified threshold condition

### Not yet derived internally

1. explicit construction of (\lambda_{\mathrm{coll}}(\rho)) from (\mathcal O(\rho)) outside 3D
2. strict 2D bosonic case in flow language
3. full operator derivation of super-Efimov flow
4. extension to semisuper-Efimov

---

## 10. Provisional Theorem

> **Universality Classification Principle.**
> Let (\lambda_{\mathrm{coll}}(\rho)) be the symmetry-reduced collective eigenvalue flow. Then the universality class is determined by the asymptotic behavior of (\lambda_{\mathrm{coll}}(\rho)+1/4).
> Constant negative limit gives Efimov scaling; logarithmically vanishing negative behavior gives super-Efimov scaling; faster decay yields a finite universal spectrum.

---

## 11. Outlook

The framework suggests:

* classification by asymptotic flow
* hierarchy of logarithmic universality classes
* predictive program based on (\lambda_{\mathrm{coll}}(\rho))
