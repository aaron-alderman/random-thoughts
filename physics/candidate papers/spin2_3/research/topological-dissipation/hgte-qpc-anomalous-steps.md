# HgTe QPC Experimental Neighbor

## Source

Paper: [Anomalous conductance steps in 3D TI HgTe-based quantum point contacts](https://arxiv.org/html/2410.17786v3)

Date on arXiv HTML version used here: January 14, 2025.

## Why It Belongs Here

This paper sits in the same broad material and transport landscape as the QWZ/Lindblad Chern-plateau note:

- strained HgTe appears explicitly as the experimental platform;
- conductance plateaus and nonstandard step structure are central observables;
- the paper works in a topological-transport setting rather than in generic mesoscopic transport language alone.

That makes it relevant as a nearby experimental/control paper for this track.

## What It Reports

The paper studies quantum point contacts (QPCs) fabricated in strained three-dimensional topological-insulator HgTe. At zero magnetic field it reports no clean quantization. At higher magnetic fields it finds distinct non-integer conductance steps, with representative values on the electron side around `0.6`, `0.8`, and `1.0` in units of `e^2/h`.

The step positions are reported to remain stable across the explored magnetic-field window once they emerge, and the plateau positions are only weakly temperature-dependent across the tested range. The macroscopic Hall region outside the QPC still shows standard quantum Hall quantization, so the anomaly is attributed to what the constriction does to the edge channels rather than to a breakdown of the surrounding bulk transport.

## Mechanism Proposed In The Paper

This is the key reason the paper matters for this repo: it gives a different mechanism from the QWZ/Lindblad testbed.

The authors interpret the anomalous steps primarily as a consequence of strong scattering or filtering at the QPC. Their modeling stack is:

- a Landauer-Buettiker interpretation of partial transmission of edge channels through the constriction;
- numerical tight-binding simulations using `Kwant`;
- an effective 2D conduction-band model with spin-orbit, Zeeman, and disorder terms in the main text;
- a more HgTe-specific 2D BHZ-model lane in an appendix.

Their conclusion is not that unusual plateaus require a dissipative Berry-curvature weighting mechanism. Instead, the paper argues that disorder and scattering in the QPC region can already generate robust non-integer conductance steps.

## Why It Is Useful For The Current Track

This paper should be read as a control or competing-mechanism reference.

It is useful because it says:

- HgTe can indeed show unusual plateau structure in experiment;
- but that fact alone does **not** isolate a Lindblad/dephasing explanation;
- in this material neighborhood, QPC scattering and edge-channel filtering are realistic alternative explanations.

That makes it a good guardrail against over-reading the QWZ/Lindblad note as if "HgTe-like material + odd plateau = dephasing formula confirmed."

## Relationship To The QWZ / Lindblad Testbed

The two papers live near each other, but they are not doing the same job.

The QWZ/Lindblad note in [chern-plateaus-testbed.md](chern-plateaus-testbed.md):

- is an analogue/testbed calculation;
- emphasizes Berry-curvature concentration and momentum-selective dephasing;
- proposes a doubled-cusp signature near two simultaneous gap closures.

The HgTe QPC paper:

- is an experimental/topological-transport paper in a real HgTe device platform;
- emphasizes magnetic-field-induced edge-channel transport through a disordered constriction;
- explains anomalous plateaus through partial transmission and scattering, not through the same dissipative-response mechanism.

So the right read is: **same neighborhood, different mechanism**.

## Use In This Repo

Good uses:

- cite it when discussing the experimental landscape around strained HgTe and anomalous plateau structure;
- use it as a counterweight when comparing dissipative explanations to scattering/filtering explanations;
- mine it later if a material-specific HgTe/BHZ modeling branch is created.

Bad uses:

- treating it as direct evidence for the QWZ/Lindblad response formula;
- promoting it into the core framework as though it established a Spin(2,3) material realization;
- using its plateau anomalies as proof of the same mechanism proposed in `paper3`.
