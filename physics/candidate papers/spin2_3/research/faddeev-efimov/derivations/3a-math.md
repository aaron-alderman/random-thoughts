# Mathematical synopsis

## 1. Structural starting point

Let (\mathcal D) be the decomposition space of the few-body system: pair-spectator charts, cluster channels, or other admissible factorizations. Let
[
\mathcal O(\rho)
]
denote the corresponding coupling operator after imposing the physical constraints of the problem: symmetry, statistics, dimensionality, boundary conditions, and interaction topology.

After projection to the symmetry-allowed sector, the framework reduces to a distinguished collective branch. Write its effective eigenvalue as
[
\lambda_{\mathrm{coll}}(\rho).
]

This is the central object.

The radial problem is then put in the form
[
\left[-\frac{d^2}{d\rho^2}+\frac{\lambda_{\mathrm{coll}}(\rho)}{\rho^2}\right]f(\rho)=0,
]
at zero energy in the asymptotic regime.

We then split off the critical radial value by defining
[
\Delta(\rho):=\lambda_{\mathrm{coll}}(\rho)+\frac14.
]
Equivalently,
[
\lambda_{\mathrm{coll}}(\rho)=-\frac14-\Delta_-(\rho),
\qquad \Delta_-(\rho):=-\Delta(\rho).
]

So the effective channel is
[
U_{\mathrm{eff}}(\rho)
======================

-\frac{1}{4\rho^2}-\frac{\Delta_-(\rho)}{\rho^2}.
]

The whole classification problem is therefore reduced to the asymptotic behavior of
[
\Delta(\rho)=\lambda_{\mathrm{coll}}(\rho)+\frac14.
]

---

## 2. Definition: collective eigenvalue flow

Call
[
\rho\mapsto \lambda_{\mathrm{coll}}(\rho)
]
the **collective eigenvalue flow**.

The universality class is determined by how this flow approaches the critical value (-1/4).

This is the revised invariant of the framework.

---

## 3. Canonical asymptotic equation

Write
[
U_{\mathrm{eff}}(\rho)
======================

## -\frac{1}{4\rho^2}

\frac{V(\rho)}{\rho^2},
]
where
[
V(\rho):=-\lambda_{\mathrm{coll}}(\rho)-\frac14.
]

Then the radial equation is
[
\left[
-\frac{d^2}{d\rho^2}
-\frac{1}{4\rho^2}
-\frac{V(\rho)}{\rho^2}
\right]f(\rho)=0.
]

Now remove the critical term by setting
[
f(\rho)=\sqrt{\rho},g(\rho).
]

A direct substitution gives
[
g''(\rho)+\frac1\rho g'(\rho)+\frac{V(\rho)}{\rho^2}g(\rho)=0.
]

So the asymptotic class is encoded in the decay law of (V(\rho)).

---

## 4. Efimov class

Suppose
[
V(\rho)\to s_0^2>0.
]

Then set
[
x=\ln \rho.
]

Using
[
\frac{dg}{d\rho}=\frac1\rho \frac{dg}{dx},
\qquad
\frac{d^2g}{d\rho^2}
====================

\frac{1}{\rho^2}\left(\frac{d^2g}{dx^2}-\frac{dg}{dx}\right),
]
the equation becomes asymptotically
[
\frac{d^2g}{dx^2}+s_0^2 g=0.
]

Hence
[
g(x)\sim A\sin(s_0 x+\delta),
]
and therefore
[
f(\rho)\sim \sqrt{\rho},\sin(s_0\ln\rho+\delta).
]

The nodes satisfy
[
\ln \rho_n \sim \frac{\pi n}{s_0},
]
so
[
\rho_n\sim e^{\pi n/s_0},
\qquad
E_n\sim \rho_n^{-2}\sim e^{-2\pi n/s_0}.
]

Thus:

[
\boxed{
\lambda_{\mathrm{coll}}(\rho)+\frac14\to -s_0^2
\quad\Longrightarrow\quad
\text{Efimov class}.
}
]

This is the ordinary 3D Efimov mechanism. In the standard identical-boson case the reduced channel has (\lambda=-s_0^2-1/4), and in the 3D heteronuclear fermionic (L=1) problem the Efimov threshold occurs above mass ratio (M/m\approx 13.6069).

---

## 5. Super-Efimov class

Suppose instead
[
V(\rho)\sim \frac{s_0^2}{\ln^2\rho}.
]

Again set
[
x=\ln \rho.
]

Then the equation becomes asymptotically
[
\frac{d^2g}{dx^2}+\frac{s_0^2}{x^2}g=0.
]

This has solutions
[
g(x)\sim \sqrt{x},\sin(s_0\ln x+\delta),
]
so
[
f(\rho)\sim \sqrt{\rho\ln\rho},
\sin!\big(s_0\ln\ln\rho+\delta\big).
]

Now the nodes satisfy
[
\ln\ln \rho_n \sim \frac{\pi n}{s_0},
]
hence
[
\rho_n\sim \exp!\left(e^{\pi n/s_0}\right),
\qquad
E_n\sim \exp!\left(-2e^{\pi n/s_0}\right).
]

Thus:

[
\boxed{
\lambda_{\mathrm{coll}}(\rho)+\frac14
\sim
-\frac{s_0^2}{\ln^2\rho}
\quad\Longrightarrow\quad
\text{super-Efimov class}.
}
]

For 2D spinless fermions at a (p)-wave resonance, the asymptotic channel is
[
U_{\mathrm{eff}}(\rho)
======================

## -\frac{1}{4\rho^2}

\frac{s_0^2+\tfrac14}{\rho^2\ln^2(\rho/r_0)},
\qquad s_0=\frac43,
]
which yields the known doubly exponential super-Efimov spectrum.

---

## 6. Finite universal class

If
[
V(\rho)\to 0
]
faster than (1/\ln^2\rho), then the reduced equation does not generate oscillations in any first iterated logarithmic variable by the above mechanism. In that regime there is no asymptotic runaway tower.

So the natural mathematical criterion for the finite universal sector is

[
\boxed{
\lambda_{\mathrm{coll}}(\rho)+\frac14=o!\left(\frac{1}{\ln^2\rho}\right)
\quad\Longrightarrow\quad
\text{no Efimov- or super-Efimov-type tower}.
}
]

Strict 2D identical bosons are the canonical example: there is no Efimov tower, but there remain finitely many universal trimers, specifically two in the strict 2D limit.

---

## 7. Unified threshold condition

The previous three cases suggest the following rule.

Let (X(\rho)) be the asymptotic variable in which the reduced equation becomes oscillatory. Then the threshold into a universality class occurs when the collective eigenvalue flow first generates a real oscillation exponent in (X).

Formally:

[
\boxed{
\text{threshold}
\iff
\text{the asymptotic reduction of }
\lambda_{\mathrm{coll}}(\rho)
\text{ yields real oscillatory solutions in }X(\rho).
}
]

Examples:

* (X(\rho)=\ln\rho): Efimov threshold
* (X(\rho)=\ln\ln\rho): super-Efimov threshold

---

## 8. Mass-ratio thresholds as flow transitions

In this language, a control parameter such as the mass ratio (\alpha) deforms the collective eigenvalue flow:
[
\lambda_{\mathrm{coll}}(\rho;\alpha).
]

The threshold value (\alpha_c) is the point where the asymptotic behavior crosses into an oscillatory class.

For 2D mass-imbalanced (p)-wave systems, the super-Efimov tower appears only above critical mass ratios:
[
\frac{m_1}{m_2}>4.03404
\quad\text{(identical bosons)},
\qquad
\frac{m_1}{m_2}>2.41421=1+\sqrt2
\quad\text{(identical fermions)}.
]
These are naturally interpreted as entry into the (\ln\ln\rho)-oscillatory class.

---

## 9. Formal reformulation of the framework

The framework can now be stated as a three-layer map:

### Structural layer

[
(\text{decomposition graph},\ \text{constraints})
\longmapsto
\mathcal O_{\mathrm{red}}(\rho).
]

### Spectral layer

[
\mathcal O_{\mathrm{red}}(\rho)
\longmapsto
\lambda_{\mathrm{coll}}(\rho).
]

### Asymptotic layer

[
\lambda_{\mathrm{coll}}(\rho)+\frac14
\longmapsto
V(\rho)
\longmapsto
X(\rho)
\longmapsto
\text{spectrum class}.
]

This is the mathematically strongest form we have reached so far.

---

## 10. Provisional theorem-form statement

A concise theorem-like version is:

> **Provisional classification principle.**
> Let (\lambda_{\mathrm{coll}}(\rho)) be the symmetry-reduced collective eigenvalue flow of a few-body system. Then the universality class is determined by the asymptotic behavior of (\lambda_{\mathrm{coll}}(\rho)+1/4).
> If this quantity tends to a negative constant, the system is Efimov.
> If it tends to zero like (-c/\ln^2\rho), the system is super-Efimov.
> If it tends to zero faster than (1/\ln^2\rho), the system belongs to a finite universal sector.

This is the cleanest mathematical statement available right now.

---

## 11. What remains unfinished

This is the part to keep explicit in any later summary.

### Not yet derived internally

We do **not yet** have a full first-principles derivation of
[
\mathcal O_{\mathrm{red}}(\rho)\longmapsto \lambda_{\mathrm{coll}}(\rho)
]
for the non-3D cases inside this framework itself. Outside the 3D Efimov case, we are currently inferring the collective eigenvalue flow from known asymptotic channels rather than deriving it directly.

### Still missing mathematically

We still need:

1. a direct eigenvalue-flow derivation for strict 2D bosons;
2. a direct eigenvalue-flow derivation for the super-Efimov class from the reduced operator, not only from the known asymptotic hyperradial potential;
3. a cleaner statement of when (-1/4) is truly universal versus when it is an artifact of a particular radial reduction convention;
4. integration of semisuper-Efimov into the same formal hierarchy.

### Status of the framework

So the framework is now mathematically structured, but it is still partly **classification backed by known model asymptotics**, rather than a fully closed derivation pipeline in every class.

---

## 12. Where this gets you

Mathematically, the main gain is that the old statement

> “competing decompositions produce universality”

has been sharpened into

[
\boxed{
\text{competing decompositions}
\to
\text{collective eigenvalue flow}
\to
\text{asymptotic spectral class}.
}
]

That is a significant evolution from the starting point.
