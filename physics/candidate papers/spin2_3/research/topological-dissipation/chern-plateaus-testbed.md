# QWZ / Lindblad Chern-Plateau Testbed

## Source

Primary extracted notes: [../../papers/paper3/paper3 - dissipative softening of chern plateaus.md](../../papers/paper3/paper3%20-%20dissipative%20softening%20of%20chern%20plateaus.md)

This note reads the paper as an analogue/testbed, not as direct Spin(2,3) material evidence.

## What The Model Is

The source paper studies the Qi-Wu-Zhang two-band lattice Dirac model with a dephasing bath represented by the Lindblad jump operator $L = \sigma_z$. Its main output is a closed-form dissipatively softened Hall response

$$
\sigma_{xy}^{\mathrm{eff}}(M,\gamma)
= \frac{e^2}{h}\int_{\mathrm{BZ}} \frac{d^2k}{2\pi}\,
\Omega(k)\,\frac{4|d(k)|^2}{4|d(k)|^2 + \gamma^2}.
$$

The key structural point is that dephasing enters as a momentum-dependent suppression factor tied to the local band gap, not as a uniform occupation smearing.

## Assumptions

- The underlying band structure is the QWZ lattice Dirac model, not a Spin(2,3)-derived Hamiltonian.
- The environment is modeled by a Markovian Lindblad master equation with diagonal jump operator $L = \sigma_z$.
- The dephasing rate $\gamma$ is taken momentum-independent and weak compared with the bandwidth.
- The finite self-energy $\Sigma = i\gamma/2$ is used as a Born-level approximation in the Kubo-Bastin response calculation.
- The doubled-cusp estimate assumes independent Berry-curvature contributions from the two simultaneous gap closures at $M = 0$.

These assumptions matter because the main formulas are only as strong as the open-system approximation beneath them.

## Main Falsifiable Result

The central prediction is the phase map $\sigma_{xy}^{\mathrm{eff}}(M,\gamma)$ together with a specific asymmetry:

- near $M = \pm 2$, dephasing softens a single cusp associated with one gap closure;
- near $M = 0$, dephasing softens a doubled cusp associated with simultaneous closures at $X$ and $Y$;
- for small broadening, plateau suppression near $M = 0$ is predicted to be about twice the suppression near $M = \pm 2$.

This gives an experimentally checkable ratio rather than only a qualitative "broadening happens" statement.

## Why The Doubled Cusp Matters

The doubled cusp is the paper's load-bearing idea. It ties together:

- Berry-curvature concentration near gap closures;
- the geometry of having one closure versus two simultaneous closures;
- a response suppression mechanism that is local in momentum-space gap size.

That matters for framework use because it shows how topological response can carry geometric memory of where and how the protected gap closes. Even if the QWZ model is only an analogue, it is a clean example of "structure near the transition surface matters quantitatively."

## Dissipative Signature Versus Thermal Broadening

The paper's strongest discriminator is not that both mechanisms soften plateaus, but that they soften them differently:

- thermal broadening works through occupation and tends to suppress the $M = 0$ and $M = \pm 2$ transitions at comparable rates;
- dissipative dephasing works through a spectral-weight factor $f_{\gamma}(E)$ that is sensitive to local band geometry, producing the near-$2\times$ asymmetry.

This is precisely the kind of difference that makes an external model useful: it offers a concrete observable for telling one physical broadening mechanism from another.

## Framework Hooks

This paper can be used to sharpen questions already present elsewhere in the repo:

- [../../kernels/topological.md](../../kernels/topological.md): useful for thinking about how protected response changes near transition surfaces, especially when Berry curvature or related topological density becomes sharply localized.
- [../../kernels/dynamics.md](../../kernels/dynamics.md): useful as an external example of a reduced Lindblad/Markov description that produces quantitative broadening rather than only qualitative decoherence language.
- [../../kernels/consistency.md](../../kernels/consistency.md): useful for regime-of-validity hygiene, because the paper states exactly where the self-energy approximation is meant to hold and where momentum-dependent corrections would matter.

What this note does **not** do is identify the QWZ sectors with `T1/T2`, derive the jump operator from hidden-sector coupling, or infer that the Spin(2,3) framework already has the same response formula.

## Related Experimental Landscape

For a nearby experimental/control paper in the same HgTe transport neighborhood, see [hgte-qpc-anomalous-steps.md](hgte-qpc-anomalous-steps.md).

That paper is useful precisely because it points to a different mechanism. It reports anomalous non-integer conductance steps in strained HgTe quantum point contacts under magnetic field, but interprets them mainly through QPC scattering, edge-channel filtering, and Landauer-Buettiker plus tight-binding modeling rather than through the present Berry-curvature-weighted Lindblad response formula.

So the combined lesson is sharper than either paper alone:

- the QWZ/Lindblad note gives a clean analogue model for geometry-sensitive dissipative softening;
- the HgTe QPC paper shows that unusual plateau structure in a nearby experimental platform can also arise from constriction disorder and partial transmission;
- therefore any future bridge to experiment needs a mechanism-discrimination step, not just a visual plateau anomaly.

## Do Not Overclaim

The missing bridge steps are substantial:

- no derivation from a Spin(2,3) Hamiltonian to the QWZ model;
- no proof that the Lindblad operator $L = \sigma_z$ is the correct reduced image of any framework coupling;
- no material-realization argument showing that this paper instantiates the repo's topological class;
- no claim-level promotion into [../../CLAIM_LEDGER.md](../../CLAIM_LEDGER.md);
- no warrant to rewrite the kernels as though the analogue result were already a framework theorem.

The right use is narrower and still valuable: treat this paper as a worked external example of topological response under controlled dephasing, and as a candidate source of sharper observable language for future bridge work.
