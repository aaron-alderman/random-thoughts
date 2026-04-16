# Barocaloric Effect

## Big Picture

The barocaloric effect turns pressure into temperature change. Apply hydrostatic pressure to the right material near a suitable phase transition and it heats; release the pressure and it cools. It belongs to the same caloric family as elastocaloric, twistocaloric, and magnetocaloric — same thermodynamic principle (driven entropy change), different external field (hydrostatic pressure rather than uniaxial stress, torsion, or magnetic field).

In the broader phonon landscape, barocaloric behavior matters because it reinforces a fundamental point: thermal control can emerge from any external field that couples to an entropy-rich structural transition. Pressure couples to volume; volume changes at phase transitions; entropy changes accompany structural rearrangement. The physics is clean and general. The practical advantage over elastocaloric is isotropy — hydrostatic pressure loads a material uniformly from all directions, avoiding the stress concentrations and directional fatigue that limit NiTi.

The field has moved fast in 2024–2026: plastic crystals have yielded "colossal" barocaloric effects (ΔS > 280 J/kg/K, ΔT > 30 K at moderate pressures), organic ionic plastic crystals have been identified as a new high-performance subclass, and a "dissolution barocaloric" mechanism has been reported achieving ~54 K cooling spans and simulated COP approaching 77%.

## This Document Covers

This document covers barocaloric behavior as pressure-driven temperature change: the physical mechanism, the key figure of merit, the material landscape with quantitative data, the plastic crystal breakthrough and why that class dominates, the dissolution barocaloric innovation, COP benchmarks, the pressure hardware challenge, prototype status, market context, and the main research frontiers.

## What The Effect Does

Changing pressure shifts the free energy balance between phases. Near a first-order phase transition where competing phases have different volumes and entropies, even modest pressure changes can drive the system from one phase to the other, exchanging latent heat with the surroundings.

In a barocaloric cooling cycle:

1. **Apply pressure** → material transforms to lower-volume, lower-entropy phase → releases latent heat to hot reservoir
2. **Remove pressure** → material returns to higher-entropy phase → absorbs heat from cold reservoir, producing cooling

The key figures of merit are:

**ΔS_bc (barocaloric entropy change)** — entropy change per kg of material per unit pressure, in J/kg/K. Higher is better.

**ΔT_bc (barocaloric temperature change)** — adiabatic temperature change under pressure application, in K. The working temperature swing.

**Barocaloric strength** — |ΔS| / ΔP, in J/K/kg/MPa. Measures how much entropy change you get per MPa of applied pressure. Higher strength means lower pressure infrastructure for the same ΔT.

**Reversibility** — the transition must be reversible under repeated pressure cycling. Irreversible transitions (where the material does not fully revert) degrade cooling capacity over time.

## Material Landscape

### Plastic Crystals: The Breakthrough Class

A plastic crystal is a material in which molecules occupy a regular lattice (crystal-like positional order) but rotate freely on their lattice sites (liquid-like orientational disorder). This combination produces an exceptionally large entropy associated with the orientational disorder — entropy that can be controlled by pressure, which locks or unlocks molecular rotation at a phase transition.

**Neopentylglycol (NPG)** was the first material to show "colossal" barocaloric effects (2019 landmark result). Near its solid–solid rotator transition at ~315 K, NPG shows ΔS ≈ 390 J/kg/K — comparable to the evaporation of a refrigerant fluid but driven entirely by solid-state pressure cycling. Recent work (2026, Nature Communications) improved NPG performance by blending with pentaglycerine and adding 2% pentaerythritol, tuning the transition temperature and improving reversibility at lower pressure.

**LiCB₁₁H₁₂** (lithium closo-monocarborane, a borane-based plastic crystal, 2024): |ΔSrev| = 280 J/K/kg, |ΔTrev| = 32 K at only 0.23 GPa pressure. Barocaloric strength ≈ 2 J/K/kg/MPa — one of the highest reported. The 0.23 GPa threshold is significantly lower than many other barocaloric materials, reducing the pressure infrastructure requirement.

**Organic ionic plastic crystals (OIPCs, 2025 Science):** OIPCs combine ionic bonding (larger entropy from ion reordering) with plastic crystal orientational disorder. Measured ΔS: 92–240 J/kg/K, subambient transition temperatures. Tunable by structural modification of the ions. This is a large new chemical space — hundreds of candidate OIPCs have not yet been screened barocalorically.

**KPF₆ (2025, Nature Communications — "all-temperature" barocaloric):** ΔTad = 12 K at room temperature under 250 MPa. Unique feature: functional across an exceptionally wide temperature range from 77.5 K to 300 K — the same material operates from liquid-nitrogen temperature to room temperature. This broadens the application space to cryogenic cooling, hydrogen liquefaction, and scientific instrumentation.

**Adamantane derivatives (1-Cl-adamantane, 1-Br-adamantane):** Reversible colossal barocaloric effects near room temperature; adamantane-based molecular crystals are a well-characterized chemical platform that allows systematic structural modification.

| Material | ΔS (J/kg/K) | ΔT (K) | Pressure (GPa) | Notes |
|---|---|---|---|---|
| Neopentylglycol (NPG) | ~390 | ~10–15 | ~0.25 | Original colossal result; transition ~315 K |
| LiCB₁₁H₁₂ | 280 | 32 | 0.23 | Highest strength (2 J/K/kg/MPa); low pressure |
| OIPCs (best) | 240 | — | ~0.3 | 2025; large tunable class |
| KPF₆ | ~100 | 12 | 0.25 | All-temperature; 77–300 K range |
| Dissolution barocaloric | — | 30–54 | — | 2026; new mechanism; simulated COP ~77% |

### Dissolution Barocaloric (January 2026, Chinese Academy of Sciences)

A fundamentally new mechanism reported in Nature in early 2026. Rather than a solid–solid structural transition, the dissolution barocaloric effect uses the pressure-dependent solubility of a solid in a solvent: pressure dissolves the solid (entropy-increasing process, absorbs heat); pressure release causes precipitation (entropy-decreasing, releases heat). The "working fluid" transitions between dissolved and precipitated states rather than between two crystalline phases.

Results:
- Temperature drop of ~30 K in 20 seconds at room temperature
- Cooling span up to 54 K at elevated temperatures
- Simulated cooling capacity: 67 J/g
- Simulated efficiency: approaching 77% of Carnot

The dissolution approach has an engineering advantage: the working material can be pumped as a fluid through heat exchangers when dissolved, eliminating the solid-in-heat-exchanger contact problem that limits elastocaloric and conventional barocaloric devices. This may be the route to practical barocaloric systems at scale.

## COP Performance

Barocaloric systems show high theoretical COP, especially in optimized cycle designs:

| Cycle type | Estimated COP | Conditions |
|---|---|---|
| Reverse Stirling cycle (plastic crystal) | ~14 | ΔT = 5 K span |
| Reverse Brayton cycle (plastic crystal) | ~7.5 | ΔT = 5 K span, 30 kJ/kg cooling density |
| Barocaloric refrigerator (0.1 GPa) | ~5.5 | ΔT = 2.4 K, 1 mHz cycle frequency |
| Dissolution barocaloric (simulated) | ~77% of Carnot | — |

For comparison: a typical household vapor-compression refrigerator achieves COP 2–4. The barocaloric Stirling-cycle estimate of COP ~14 at small ΔT is exceptional — it reflects the large entropy change per pressure increment in colossal barocaloric materials, which translates directly to efficient pumping.

## The Pressure Hardware Challenge

The central engineering constraint of barocaloric systems: generating 0.1–0.5 GPa (1,000–5,000 atmospheres) hydrostatic pressure requires hydraulic or pneumatic infrastructure that has no natural analog in conventional refrigeration architecture. Compressors that operate at these pressures exist in industrial and research settings but are not the miniaturized, low-cost devices that fill homes and supermarkets.

Key pressure engineering considerations:
- **Pressure vessel design** — containing 0.25 GPa without leakage or fatigue failure in a cycling system requires high-strength materials and careful seal design
- **Pressure medium** — hydrostatic pressure is typically transmitted through a liquid medium (silicon oil, glycol-water). In the dissolution barocaloric case, the working fluid itself is the pressure medium, simplifying the design
- **Cycle frequency** — barocaloric systems operating at slow cycle frequencies (mHz to Hz) have adequate time for pressure equilibration; higher frequencies improve cooling power but require faster pressure actuation
- **Scale** — unlike vapor-compression compressors (which are mature, miniaturized, and inexpensive), high-pressure hydraulic systems at barocaloric operating pressures are expensive at small scale

LiCB₁₁H₁₂'s lower pressure threshold (0.23 GPa) and the dissolution mechanism's potential for pump-driven cycling are both responses to this challenge.

## Prototype Status

As of early 2026, barocaloric cooling remains at the laboratory and early-device-modeling stage. No commercial barocaloric product exists. Published work includes:

- Lab-scale demonstrations of colossal ΔS and ΔT in plastic crystal samples under quasi-static pressure
- Device models for solid-state barocaloric refrigerators (Wiley Energy Technology, 2025)
- Numerical simulations of dissolution barocaloric cooling cycles
- California Energy Commission 2024 report assessing barocaloric (alongside elastocaloric and magnetocaloric) as a priority solid-state cooling pathway

The dissolution barocaloric result from CAS (2026) is the most significant recent step toward practical implementation because it converts the working material into a pumpable fluid, removing the primary device-engineering barrier.

## Market Context

The barocaloric market is currently zero — no products, no commercial revenue. The addressable opportunity is the same as for all caloric cooling technologies: a fraction of the **~$250B global HVAC and refrigeration market**, specifically driven by the regulatory elimination of HFC refrigerants and the efficiency mandates pushing beyond vapor-compression COP.

The plastic crystal barocaloric class has potential cost advantages: neopentylglycol is an inexpensive industrial chemical (used in alkyd resins and lubricants), and the OIPC class, while diverse, includes materials with accessible precursors. The borane-based LiCB₁₁H₁₂ is more specialized and expensive, but other high-strength plastic crystals may not require rare or costly inputs.

## Current Research Frontiers

**OIPC compositional space** — hundreds of organic ionic plastic crystals have not been barocalorically characterized. Systematic screening (DSC under pressure, direct ΔT measurement) could identify materials with large ΔS at lower pressures and better-tuned transition temperatures.

**Dissolution barocaloric mechanism development** — following the 2026 CAS result, the dissolution mechanism is the most promising new direction. Key questions: which solute-solvent systems show the largest dissolution entropy; how to optimize pressure cycling; how dissolution and precipitation kinetics scale with device volume.

**Multilayer and graded architectures** — stacking layers with slightly different transition pressures or temperatures creates a pseudo-continuous caloric response over a broader operating range, improving the match to real refrigeration operating conditions (not just a fixed 5 K span).

**Pressure reduction through materials design** — identifying or engineering materials where the same ΔS is achievable at lower applied pressure. LiCB₁₁H₁₂ at 0.23 GPa represents progress; targets below 0.1 GPa would transform the pressure hardware requirement.

**Integration with fluid heat exchangers** — the dissolution barocaloric approach and slurry-based solid plastic crystal suspensions both enable fluid-phase heat exchange, directly addressing the thermal contact problem in solid barocaloric devices.

## Connections to the Larger Landscape

- **Elastocaloric** (Part VIII) is the mechanistically nearest competitor: both use first-order structural transitions driven by a mechanical field (stress vs. pressure). The key practical distinction is geometry: barocaloric pressure is isotropic (no preferred direction, no fatigue from directional cycling) while elastocaloric stress is anisotropic (creates fatigue at preferred crack sites).
- **Twistocaloric and magnetocaloric** (Parts IX, XI) complete the caloric family. A comparison across all four requires COP, scalability, operating temperature range, and input field infrastructure cost.
- **Part VIII (characterization)** is particularly important for barocaloric: pressure-dependent calorimetry (DSC under hydrostatic pressure) and direct ΔT measurement under pressure cycling require specialized apparatus that constrains which groups can contribute and where measurement artifacts arise.
- **Part VI** frames the motivation: refrigerant-free solid-state cooling at competitive COP would have very large energy and climate impact; barocaloric is a serious contender in that competition.
