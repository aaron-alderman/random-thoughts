# Superconductivity

## Big Picture

Superconductivity matters in this landscape because it is where several conceptual threads converge at once: phonons, symmetry breaking, coherent phase order, and extreme electronic consequence. It is not just another conversion mechanism. It is a case where lattice control may reshape the limits of electronic behavior itself.

The broader phononics program cares about superconductivity because phonons are not incidental to the standard mechanism — they are the reason the state exists in conventional superconductors. At the same time, 2025 brought a concrete milestone for the topological thread: Microsoft's Majorana 1, the first quantum processor built on topological superconductivity, moved from theory to silicon. The convergence of phonon physics, topology, and quantum information is no longer speculative.

## This Document Covers

This document covers superconductivity from the phonon landscape perspective: the phonon-mediated BCS picture with quantitative benchmarks, the Tc record landscape and what it tells us about the limits of conventional superconductivity, the symmetry-breaking meaning of the superconducting state, Josephson physics, topological superconductivity and the Majorana 1 development, existing industrial applications, the quantum computing market, and why phonon engineering is a credible lever for superconducting performance.

## Phonon-Mediated Pairing: The BCS Picture

In conventional BCS superconductivity, electrons that would ordinarily repel one another can become effectively attractive by exchanging virtual phonons. The sequence: one electron deforms the lattice slightly as it passes, creating a momentary positive charge density; a second electron is attracted to this phonon-mediated disturbance and the two electrons become correlated, forming a Cooper pair.

The critical temperature is governed primarily by two parameters:

**λ (electron-phonon coupling constant)** — how strongly electrons couple to the phonon field. Higher λ favors higher Tc.

**ω_log (logarithmic average phonon frequency)** — the characteristic frequency of the phonons mediating pairing. Higher ω_log also favors higher Tc.

The McMillan-Allen-Dynes equation encodes the tradeoff: **Tc ∝ ω_log × exp(−1/λ)**. The problem is that λ and ω_log are not independent — increasing λ (by stiffening the lattice) tends to decrease ω_log (phonon softening at large coupling), and vice versa. A 2025 Nature Communications study formalized this as an inherent trade-off, concluding that achieving room-temperature conventional superconductivity at ambient pressure is extremely unlikely within the BCS framework.

The implication: phonon engineering can optimize performance within the constraint, but the constraint is real and fundamental.

## Critical Temperature Landscape

Tc values establish the practical scope of what is available today, and what each approach costs in terms of cooling infrastructure:

| Material | Tc (K) | Tc (°C) | Pressure | Type | Notes |
|---|---|---|---|---|---|
| LaH10 | ~250 | −23 | ~170 GPa | Conventional (hydride) | Highest confirmed Tc; requires extreme pressure |
| H3S | ~203 | −70 | ~150 GPa | Conventional (hydride) | First hydride record; confirmed by SQUID |
| HgBa2Ca2Cu3O8 (Hg-1223) | 135 | −138 | Ambient | Unconventional (cuprate) | Highest ambient-pressure Tc |
| Tl2Ba2Ca2Cu3O10 (Tl-2223) | 127 | −146 | Ambient | Unconventional (cuprate) | — |
| YBa2Cu3O7 (YBCO) | 92 | −181 | Ambient | Unconventional (cuprate) | Above liquid nitrogen (77 K); first LN2-cooled material |
| MgB2 | 39 | −234 | Ambient | Conventional | Simple binary compound; surprisingly high Tc; no rare earths |
| Nb3Sn | 18 | −255 | Ambient | Conventional | Standard material for high-field research magnets |
| NbTi alloy | 9–10 | −263 | Ambient | Conventional | Dominant commercial wire material (MRI magnets) |
| Nb (elemental) | 9.3 | −264 | Ambient | Conventional | Standard Josephson junction and SQUID material |

The hydride superconductors (H3S, LaH10) hold the Tc records but require megabar pressures to stabilize — inaccessible for any practical device. The cuprates hold the ambient-pressure record but are brittle ceramics difficult to form into wire, mechanically fragile, and mechanistically unconventional (the pairing mechanism in cuprates remains incompletely understood and is emphatically not BCS). The conventional materials with actual commercial deployments (NbTi, Nb3Sn, Nb) all require liquid helium cooling (4.2 K), which adds significant operational cost.

The gap between "highest Tc ever measured" and "practically usable" is the defining tension in superconductivity research.

## Symmetry Breaking and Coherence

Superconductivity is described as spontaneous U(1) gauge symmetry breaking. Below Tc, electron pairs condense into a macroscopic quantum state described by a single wavefunction with a definite phase. All Cooper pairs lock into this common quantum phase, producing a condensate that behaves as one coherent macroscopic object — the origin of the Meissner effect (perfect diamagnetism, flux expulsion) and zero DC resistance.

This matters for the broader program because it demonstrates how phonon-mediated interactions can generate a qualitatively different phase of matter, not merely modify transport coefficients. The lattice restructures the electronic system at a fundamental level, producing coherent order that persists macroscopically. The phonon field is not a passive background here — it is the mediator of a phase transition.

## Josephson Physics

When two superconductors are separated by a thin insulating barrier (a Josephson junction), Cooper pairs tunnel coherently through the barrier. The current through the junction is determined by the phase difference Δφ between the two superconductors:

**I = Ic × sin(Δφ)**

where Ic is the critical current. This DC Josephson effect means current flows without any applied voltage, driven entirely by relative quantum phase. Under an applied voltage V, the phase difference evolves at frequency **f = 2eV/h** — the AC Josephson effect. This frequency (approximately 483.6 MHz per μV) is exact and reproducible to parts per billion, making it the basis of the international voltage standard.

The Josephson junction is the fundamental nonlinear element of superconducting electronics. Its applications span:

- **SQUIDs (Superconducting Quantum Interference Devices)** — the most sensitive magnetic field detectors known (sensitivity below 1 fT/√Hz), used in MEG brain imaging, geophysical surveys, submarine detection, dark matter searches
- **Voltage standards** — Josephson junction arrays define the volt in the SI system
- **THz sources and detectors** — intrinsic Josephson junctions in cuprate superconductors emit coherent THz radiation
- **Superconducting qubits** — transmon, fluxonium, and other qubit designs are Josephson junction-based nonlinear LC circuits operated at millikelvin temperatures

## Topological Superconductivity and Majorana 1

Topological superconductors add band-topology structure to superconducting order. In a topologically nontrivial superconductor, edges and defects host **Majorana zero modes (MZMs)** — quasiparticle states that are their own antiparticle and that encode quantum information non-locally, in the parity of a fermionic mode distributed between two spatially separated endpoints.

The strategic importance: Majorana-based qubits store quantum information in a way that is fundamentally protected against local noise. A local perturbation at one end of the wire cannot flip the qubit state because the information is encoded in the global parity, accessible only by operations that span the entire wire. This is topological protection — fault tolerance that comes from physics rather than from error correction overhead.

**February 2025: Microsoft unveiled Majorana 1**, the world's first quantum processing unit built on a topological core. The device uses nanowires of InAs (semiconductor) coated with Al (superconductor), cooled to ~15 mK and tuned with magnetic fields to create topological superconducting nanowires. Rabi-like oscillations between MZM states were demonstrated, and a new interferometric readout method enabled single-shot parity measurements — digital control of topological qubits.

**July 2025:** Microsoft demonstrated the first hardware implementation of a "tetron" qubit — a device using four MZMs on two nanowires, forming a single protected qubit. The architecture is designed to scale to a million qubits on a single chip.

The material innovation enabling this is what Microsoft terms a **topoconductor** — a class of hybrid semiconductor-superconductor heterostructures designed to support topological superconducting phases at millikelvin temperatures.

This is not a solved problem: MZMs are fragile, require precise tuning, and the topological gap protecting them is small compared to the thermal and noise energy at even modest temperatures. But the theoretical case for fault-tolerant topological qubits is strong, and the 2025 hardware demonstrations represent the first experimental realizations of the architecture.

## Industrial Applications of Existing Superconductors

**MRI magnets** — the dominant commercial application of superconductivity by revenue. NbTi wire wound into solenoids, operated at 4.2 K in liquid helium cryostats, produces the strong, stable magnetic fields (1.5–7 T) required for clinical MRI. The global MRI market is multi-billion dollars annually; the superconducting magnet is its core enabling component.

**Particle accelerators** — the LHC at CERN uses ~1,200 Nb3Sn and NbTi dipole magnets to bend 7 TeV proton beams. Future accelerators (FCC) require higher fields, pushing the need for Nb3Sn (18 T capable) and HTS candidates.

**SQUIDs** — used in magnetoencephalography (MEG) for brain mapping, submarine detection, geophysical prospecting, and calibration of quantum sensors. Commercial SQUID systems are manufactured by companies including Tristan Technologies, Supracon, and Magnicon.

**Superconducting cables for power transmission** — HTS (YBCO, Bi-2223) cables cooled by liquid nitrogen (77 K, much cheaper than LHC-grade helium) can carry 3–5× more current per unit conductor cross-section than copper. Demonstration projects exist in New York, Tokyo, and Copenhagen; full commercial deployment remains limited by cryogenic infrastructure cost.

**Fusion magnets** — Commonwealth Fusion Systems and the ITER project both rely on superconducting magnets. Commonwealth's SPARC tokamak uses HTS (REBCO) high-field magnets achieving 20 T, enabled by HTS wire production at commercial scale.

## Market Size and TAM

**Superconducting quantum chip market:** ~$512 million in 2024, projected to grow at >17.2% CAGR through 2034. This covers the transmon and Josephson-junction qubit ecosystem (IBM, Google, Rigetti, IQM, and the topological Majorana path from Microsoft).

**Quantum computing cryogenic systems:** ~$1.33 billion in 2024, projected to reach ~$1.72 billion by 2031 at 7.4% CAGR. Dilution refrigerators (Bluefors, Oxford Instruments, Leiden Cryogenics) are a supply-constrained bottleneck for quantum computer deployment.

**Conventional superconductor market (MRI, research magnets, cables):** multi-billion dollars, dominated by NbTi/Nb3Sn wire suppliers (Bruker, Oxford Superconducting Technology, Supercon) and MRI system integrators (Siemens, Philips, GE).

## Why Phonon Engineering Matters

Phonon engineering is a credible lever for superconducting performance through several channels:

**Tc enhancement in conventional superconductors** — if the phonon spectrum can be shaped (by confinement, interfaces, or composite structures) to increase the coupling integral λω_log without violating the fundamental tradeoff, Tc increases. Substrate effects on thin-film Tc (well documented in Nb and NbN films) show that phonon boundary conditions at interfaces are not passive.

**Phonon softening near quantum critical points** — materials near structural phase transitions show phonon softening that increases λ locally. This is one mechanism proposed to explain anomalously high Tc in some materials. Engineering proximity to such transitions is an active research direction.

**Quadratic electron-phonon coupling** — a 2025 Scientific Reports paper proposed a Hamiltonian incorporating both linear and quadratic phonon-mediated electron interactions in a 2D cuprate-like lattice, predicting enhanced pairing beyond what linear coupling alone achieves. This has not been realized experimentally but represents a theoretical route to higher effective coupling.

**Phonon engineering for qubit coherence** — in superconducting qubits, phonon modes in the substrate and chip package are a dominant source of decoherence (two-level systems at surfaces and interfaces). Phononic bandgap structures that suppress phonon modes at qubit operating frequencies can extend qubit coherence times. This is an active applied engineering problem, distinct from Tc enhancement.

## Main Limitations

**Cryogenic requirement** — all practical superconductors require cooling well below room temperature. NbTi/Nb3Sn require liquid helium (4.2 K); YBCO and Bi-2223 require liquid nitrogen (77 K). Both add operational cost and infrastructure that limits deployment to specialized applications. Room-temperature operation remains the theoretical goal; the 2025 analysis suggests it is not achievable in conventional BCS materials at ambient pressure.

**Brittleness of high-Tc materials** — cuprate superconductors are brittle ceramics. Forming them into wire, handling them under mechanical stress, and connecting them reliably in magnets is difficult and expensive compared to NbTi alloy wire.

**Flux creep and quench** — in practical magnet applications, thermal fluctuations or local disturbances can drive the magnet above Tc in a runaway process (quench), dumping all stored magnetic energy as heat. Managing quench protection in large magnets is a significant engineering challenge.

**Topological qubit scalability** — Majorana-based qubits require precise material quality, magnetic field tuning, and millikelvin temperatures. The topological gap is small, making MZMs vulnerable to disorder and thermal excitation. Scaling from proof-of-concept tetrons to million-qubit chips remains an unsolved fabrication and engineering challenge.

## Connections to the Larger Landscape

- **Part I** provides the deepest conceptual support through symmetry, geometry, and topology — superconductivity is the clearest example of macroscopic symmetry breaking driven by microscopic phonon exchange.
- **Phonon-electron coupling in Part VII** is the direct bridge from the broader phononics program into superconducting Tc engineering.
- **Topological effects** link to the broader topology thread in the landscape: the Majorana modes in topological superconductors are protected by the same mathematical structures (topological invariants, edge states) that appear in topological insulators and the Nernst/Hall effects discussed earlier.
- **The spin Seebeck effect and magnon-phonon coupling** (Parts XIII–XIV) share the setting of magnetic and spin-orbit-coupled materials where phonon engineering, topological band structure, and collective excitations all intersect.
