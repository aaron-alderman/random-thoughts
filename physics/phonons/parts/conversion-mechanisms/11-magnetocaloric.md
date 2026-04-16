# Magnetocaloric Effect

## Big Picture

The magnetocaloric effect converts changing magnetic field into heating and cooling. It sits at the intersection of magnetic order, thermodynamics, and lattice response — making it one of the most mature and still strategically important caloric mechanisms.

Within the broader phonon landscape, it matters because it shows how ordered internal degrees of freedom (magnetic moments) can be used to restructure thermal behavior. It is not a purely phononic effect, but phonon-linked heat transport remains central to how practical performance is realized: the entropy associated with magnetic disorder is what changes, but it is the phonon system that carries that heat to and from the heat exchanger.

Magnetocaloric is also the most commercially advanced of the solid-state caloric technologies. MAGNOTHERM has sold commercial beverage coolers to Coca-Cola. Its second-generation Eclipse unit won Innovation of the Year at ATMO Europe 2025 and demonstrated 15% better energy efficiency than propane (R290) refrigeration in an 11-week live trial. A $126M materials market exists and is growing at 9.2% CAGR.

## This Document Covers

This document covers magnetocaloric behavior as field-driven temperature change: the physical mechanism, the key parameters, the material landscape with quantitative benchmarks organized by temperature range, the commercial status including MAGNOTHERM's trajectory, COP data, the main engineering bottleneck (field requirements), low-field materials as the strategic frontier, market size, and connections to the broader landscape.

## What The Effect Does

Applying a magnetic field to a magnetocaloric material aligns magnetic moments, reducing magnetic entropy. In an adiabatic process, this entropy decrease raises the temperature of the material (magnetocaloric heating). Removing the field allows the moments to disorder, increasing magnetic entropy; the material cools (magnetocaloric cooling). Heat is shuttled between the material and heat exchangers at each stroke.

The thermodynamic cycle is directly analogous to gas-compression refrigeration: compression orders a system (reducing entropy, releasing heat); expansion disorders it (increasing entropy, absorbing heat). The field plays the role of compression; the magnetic moments play the role of gas molecules.

The effect is strongest near magnetic phase transitions — specifically near the Curie temperature — because that is where the magnetic susceptibility and the entropy sensitivity to field are both maximized. Engineering a material whose magnetic transition aligns with the desired operating temperature (near room temperature for household applications) is the primary materials design challenge.

## Key Physical Parameters

**ΔS_M (magnetic entropy change)** — entropy change per kg of material per unit field change, in J/kg/K or mJ/cm³/K. This drives the cooling capacity.

**ΔT_ad (adiabatic temperature change)** — temperature change under adiabatic field application, in K. The working temperature swing per magnetic cycle.

**Refrigerant capacity (RC or TEC)** — the heat that can be transferred per unit mass in one complete cycle, accounting for the width of the ΔS peak vs. temperature. Broad peaks with moderate height often outperform sharp peaks with high height for practical refrigeration across a temperature span.

**Field requirement** — the magnetic field magnitude needed to drive a useful ΔT. Conventional permanent magnets (Nd-Fe-B grade) produce up to ~1.8 T. Materials requiring >2 T need superconducting or electromagnet infrastructure, which is costly and energy-intensive.

## Material Landscape

### Classic Benchmark: Gadolinium

Gadolinium (Gd) metal near its Curie temperature (TC ≈ 294 K, close to room temperature) is the reference standard for magnetocaloric research:
- ΔTad ≈ 3–4 K per Tesla near TC
- ΔSM ≈ −10 J/kg/K at 2 T near TC
- Expensive: gadolinium is a rare-earth element; current price ~$40–60/kg depending on purity

Gd is used in most prototype systems as a benchmark material but is not commercially viable at scale due to cost and supply constraints.

### Room-Temperature High-Performance Materials

| Material | ΔTad (K) | ΔSM (J/kg/K) | TC (K) | Field (T) | Notes |
|---|---|---|---|---|---|
| Gd (pure) | ~3–4 | ~−10 | 294 | 2 | Reference; rare-earth cost |
| Gd₅(Si₂Ge₂) | ~15 | ~−18 | 276 | 5 | Giant MCE; coupled magnetic+structural transition; needs high field |
| La(Fe,Si)₁₃ (unhydrided) | ~6–8 | ~−20 | 195 | 2 | Tunable TC; cheap; dominant research material |
| La(Fe,Si)₁₃Hₓ (hydrogenated) | ~6–9 | ~−20–25 | 285–330 | 2 | H insertion shifts TC to room T; TC tunable by H content |
| MnFeP₀.₄₅As₀.₅₅ | ~14 | ~−18 | 305 | 5 | Giant MCE; As is toxic; active Mn-Fe-P-Si alternatives |
| GdMn₀.₆Cr₀.₄Si | ~3 | ~3.16 J/kg/K | 310 | 2 | Specifically tuned for household refrigerator TC ≈ 310 K |
| MM'X Heusler alloys (ML-screened) | TBD | large predicted | RT | <2 T | 2025 machine-learning discovery; not yet fully characterized |
| High-entropy alloys (HEA) | researched 2024–2025 | variable | tunable | 2 | HEA compositional space under active screening |

**La(Fe,Si)₁₃** is the most commercially promising class: large ΔS, no rare-earth dependence on the working element (La is abundant), cheap Fe/Si precursors, and TC that can be tuned to room temperature by hydrogen insertion. The hydrogenated form La(Fe,Si)₁₃Hₓ is the material in MAGNOTHERM's devices.

**Machine-learning screening (2025, ScienceDirect):** High-throughput DFT calculations combined with ML models screened MM'X Heusler alloy families, identifying candidates with giant room-temperature MCE at fields below 2 T. Experimental validation is ongoing; this represents the frontier of computational materials discovery applied to the MCE problem.

### Cryogenic Applications (below 77 K)

| Material | Temperature range | Notes |
|---|---|---|
| Dy, Ho, Er compounds | 10–80 K | Rare-earth compounds; large MCE at low T for hydrogen liquefaction (20 K) |
| GdLiF₄, GdF₃ | 4–30 K | Used in adiabatic demagnetization refrigerators for sub-Kelvin cooling |
| Paramagnetic salts (CMN, FAA) | <1 K | Classic adiabatic demagnetization; used in dilution refrigerator precooling |

## The Giant Magnetocaloric Effect

The "giant MCE" in Gd₅(Si₂Ge₂) and related alloys arises from a coupled first-order magnetostructural transition: the magnetic and structural phase transitions occur simultaneously, with the latent heat of both contributing to the caloric effect. ΔTad up to 15 K and ΔSM up to −18 J/kg/K are substantially larger than the ~3 K in pure Gd at the same field.

The tradeoff: coupled magnetostructural transitions often require larger magnetic fields (5 T typical), are more hysteretic (energy dissipated per cycle), and have narrower temperature windows. These properties make the giant MCE impressive in the lab but challenging to engineer into a practical cycling device with good COP.

La(Fe,Si)₁₃ achieves a better balance: large ΔS at moderate field (2 T), lower hysteresis, broader temperature peak, and tunable TC.

## COP and Efficiency

Magnetocaloric refrigeration can in principle achieve COP higher than vapor-compression because the magnetic entropy change is thermodynamically reversible (no throttling loss) and can be made highly regenerative.

- **MAGNOTHERM Eclipse (live 11-week trial, 2025):** 15% more energy efficient than propane (R290) refrigeration at equivalent operating conditions — a direct, practical comparison in a commercial product context
- **Prototype systems with model predictive control:** COP improved by up to 10.7% over baseline; heating capacity improved by up to 30.9%
- **Theoretical limit:** A perfectly reversible AMR (active magnetic regenerator) cycle approaches Carnot efficiency; practical systems achieve roughly 20–40% of Carnot in current prototypes

The 15% field result is conservative but commercially significant: it means a room-temperature magnetocaloric device already beats the best alternative natural refrigerant (propane) in a real-world deployment.

## Commercial Status: MAGNOTHERM

MAGNOTHERM GmbH (Darmstadt, Germany) is the leading commercial actor in magnetocaloric cooling:

**Polaris (first generation):** 0.04 kW beverage cooler, 100% magnetically driven using La(Fe,Si)₁₃Hₓ as the working material and Nd-Fe-B permanent magnets for field generation. Delivered first unit to Coca-Cola in early 2023; 40 Polaris units built, 20 sold as of 2024.

**Eclipse (second generation, 2025):** Scaled-up commercial refrigeration cabinet for retail applications. Won Innovation of the Year / Refrigeration at ATMO Europe 2025. 15% lower energy than R290 propane in 11-week field trial maintaining 4–5°C. Eliminates all refrigerants.

**Technology approach:** Active magnetic regenerator (AMR) cycle — the magnetocaloric material acts as both the refrigerant and the regenerator, with a water/glycol heat transfer fluid shuttled through the material bed as the magnetic field cycles. The Nd-Fe-B magnet rotates to apply and remove field from the regenerator beds.

## The Field Hardware Bottleneck

The main engineering constraint: the best magnetocaloric materials operate at 1–2 T, requiring large, heavy, expensive Nd-Fe-B permanent magnet assemblies. A 2 T magnet assembly for a practical cooling system weighs 5–15 kg and costs hundreds to thousands of dollars depending on configuration — far more than the compressor in a vapor-compression refrigerator of equivalent capacity.

Permanent magnet costs have declined with Nd-Fe-B production scale, but the magnets still dominate system cost and weight. The solution is material-side: finding materials with large ΔS at <1 T would allow smaller, cheaper magnets.

Current 1 T materials:
- Standard Gd: ~1–2 K per Tesla
- La(Fe,Si)₁₃: ~3–4 K per Tesla at optimal composition
- Target: >5 K per Tesla at 1 T — would make 1 T systems practical

## Market Size and TAM

**Magnetocaloric materials market:** ~$126 million in 2024, projected ~$234 million by 2031 at 9.2% CAGR. This is the upstream materials segment.

**System-level opportunity:** As with all caloric cooling technologies, the addressable market is a fraction of the ~$250B global HVAC/refrigeration market — specifically the portion driven by HFC phase-out, efficiency standards, and noise/vibration requirements. Magnetocaloric has the most mature commercialization pathway of the solid-state caloric technologies, giving it a head start in capturing this market.

**Hydrogen liquefaction:** A significant near-term application. Hydrogen must be cooled to 20 K for liquid storage. Rare-earth magnetocaloric materials perform exceptionally at cryogenic temperatures (unlike room-temperature refrigerants). The growing hydrogen economy is creating direct demand for cryogenic magnetocaloric cooling systems.

## Current Research Frontiers

**Low-field materials** — the most commercially important research direction. Identifying or designing materials with ΔSM > 15 J/kg/K at 1 T would transform the magnet economics. La(Fe,Si)₁₃ near its composition-optimized first-order transition, Heusler alloys, and MM'X compounds are the main candidate classes.

**Machine-learning materials discovery** — the 2025 MM'X Heusler screening exemplifies the approach: DFT + ML to predict MCE across a vast compositional space, then synthesize only the promising candidates. The approach is being extended to other material families and integrated with experimental feedback loops.

**High-entropy magnetocaloric alloys** — HEA compositional space contains materials with broad MCE peaks (beneficial for wide temperature span), tunable TC, and potentially reduced hysteresis compared to single-composition alloys. Active screening 2024–2025.

**Multicaloric effects** — materials with coupled magnetic and structural transitions (Ni-Mn-Ga, Fe-Rh, FeCoMnSi) respond to both magnetic field and mechanical stress. Driving both simultaneously can produce larger effective ΔT than either effect alone, or allow one field to pre-stage the material for efficient response to the other.

**Cryogenic expansion for hydrogen economy** — mapping rare-earth and transition-metal compound families for large MCE in the 20–80 K range to address green hydrogen liquefaction. The California Energy Commission 2024 report specifically identified this as a priority application.

**AMR cycle engineering** — active magnetic regenerator design, fluid flow optimization, and magnet geometry engineering to close the gap between material-level ΔT and system-level temperature span. MAGNOTHERM's work provides real-world validation; academic programs at DTU, TU Denmark, University of Victoria, and elsewhere are pushing cycle efficiency.

## Main Limitations

**Field requirement and magnet cost** — see above. The most commercially significant bottleneck. Eclipse mitigates it through engineering optimization and volume production of Nd-Fe-B assemblies; the long-term solution is low-field materials.

**Nd-Fe-B supply chain** — the permanent magnets needed for magnetocaloric systems use neodymium and dysprosium, both rare-earth elements with concentrated production (primarily China). Supply chain diversification and magnet recycling are active concerns for the industry, heightened by the broader rare-earth geopolitical situation.

**Hysteresis losses** — first-order magnetostructural transitions (which give the giant MCE) have hysteresis: the forward and reverse transitions occur at slightly different fields, dissipating energy as heat in each cycle. This reduces COP and can limit cycling frequency. Materials engineering to reduce hysteresis while preserving large ΔS is a key optimization target.

**Working material degradation** — La(Fe,Si)₁₃Hₓ can dehydrogenate under repeated cycling at elevated temperatures, shifting TC and reducing MCE over time. Encapsulation and surface stabilization strategies are being developed.

**Temperature span limitation** — a single magnetocaloric material has a large ΔS only near its TC. Operating across a wide temperature range (e.g., −20°C freezer to +25°C ambient) requires either a material with a broad peak or a cascade of materials with different TC values. Multi-bed AMR systems address this but add complexity.

## Connections to the Larger Landscape

- **Elastocaloric, twistocaloric, barocaloric** (Parts VIII–X) are the caloric family companions. Magnetocaloric is the most commercially mature; comparing all four reveals the tradeoffs between field type, operating temperature, COP, and infrastructure requirements.
- **Spin-related physics** (Parts XIII–XIV, spin Seebeck and magnon-phonon coupling) share the magnetic materials space. YIG, Heusler alloys, and garnets appear across multiple effects; understanding how magnetic order contributes to each helps identify multi-functional material opportunities.
- **Part IV's frontier discussion** around magnetic and topological materials indirectly expands the set of candidate magnetocaloric systems: Weyl magnets, topological semimetals, and Kagome magnets being studied for the anomalous Nernst effect may also show unusual magnetocaloric behavior near their magnetic transitions.
- **Part VI (cooling as global impact)** frames the stakes: refrigerant-free cooling at competitive COP is one of the most impactful applications across the entire phonon landscape, and magnetocaloric is the technology in this space with the clearest near-term commercial path.
