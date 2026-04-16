# Nernst Effect

## Big Picture

The Nernst effect matters because it changes the geometry of thermoelectric conversion. Instead of voltage forming along the same direction as heat flow, it appears transverse to the thermal gradient. That geometric rotation can turn an awkward conversion layout into a more useful one.

In the broader phonon landscape, this makes the Nernst effect interesting not only as a thermoelectric phenomenon, but as an example of how symmetry, magnetic order, and transport geometry can open better control architectures. The anomalous Nernst effect — the field-free version driven by Berry curvature in magnetic materials — has emerged in 2024–2025 as one of the most active frontiers in solid-state energy conversion.

## This Document Covers

This document covers the Nernst effect as a transverse thermoelectric response: the physical mechanism, the ordinary and anomalous variants, the key coefficient and what it means quantitatively, the most promising material systems, current device demonstrations, the geometric advantage over Seebeck layouts, market context, and why this area remains underexplored relative to its potential.

## What The Effect Does

When heat flows longitudinally through a conductor in a magnetic field, a transverse voltage develops perpendicular to both the heat flow direction and the field. This is the **ordinary Nernst effect**, and it requires an external magnetic field to operate.

The output is characterized by the **Nernst coefficient** N (also written as the transverse thermopower or Nernst-Ettingshausen coefficient), in units of μV/K. A material with N = 5 μV/K generates 5 μV of transverse voltage per degree of temperature difference per unit geometry factor.

The key geometric difference from the Seebeck effect: the temperature gradient runs one direction, the voltage appears at right angles to it. This means a flat slab heated from below produces a voltage across its width — a layout that can be more convenient to wire and tile than the collinear Seebeck geometry in some harvester configurations.

## The Anomalous Nernst Effect

The **anomalous Nernst effect (ANE)** is the more important variant for this landscape. In magnetic materials with spontaneous magnetization, a transverse thermoelectric response appears even without any externally applied field.

The physical origin is Berry curvature: the quantum-mechanical geometric phase accumulated by Bloch electrons as they traverse the Brillouin zone. In topologically nontrivial or ferromagnetic band structures, this Berry curvature acts as an effective internal magnetic field, generating a transverse Hall-like response to both electrical and thermal currents. The result is a transverse thermoelectric voltage driven by the material's internal magnetic order rather than an external magnet.

This changes the engineering problem substantially:

- No external-field hardware needed
- The field-producing and heat-converting functions are integrated into a single material
- Device geometry simplifies: a magnetized slab harvests heat transversely without field coils, Helmholtz cages, or permanent-magnet arrays (though permanent magnets can still be used to set the magnetization direction)
- The effect links thermoelectric conversion directly to topology and magnetic order — two of the most active areas in contemporary condensed matter physics

## Key Materials and Quantitative Benchmarks

The anomalous Nernst thermopower Sxy is the primary figure of merit, in μV/K.

| Material | Sxy at 300 K (μV/K) | Notes |
|---|---|---|
| Co2MnGa (Heusler) | ~6.5 | Polycrystalline bulk; matches record single-crystal values |
| Co2MnAl1-xSix (Heusler, tuned) | ~4.9 | Atomic ordering + Fermi level tuning; ANE conductivity 1.46 A/m/K |
| Fe3Pt | ~3–4 | Early classic ANE material |
| Co3Sn2S2 (topological semimetal) | ~8 | One of the largest ANE signals known; Weyl semimetal |
| ErMn6Sn6 (Kagome magnet) | ~1.71 | Both topological and anomalous Nernst observed at 300 K |
| Mn3Sn (noncollinear antiferromagnet) | ~0.6 | ANE without net magnetization; anomalous Hall also large |

For reference, the best conventional Seebeck materials (Bi2Te3, SnSe) have longitudinal Seebeck coefficients of 200–700 μV/K, so the Nernst transverse values are currently 10–100× smaller in raw coefficient. However, the geometric and device-level advantages can compensate for this, and the field is young — the equivalent of Seebeck materials research circa 1960.

## Device Demonstrations

Recent work has translated material properties into working devices:

**Bulk Nernst generator (2024):** A centimeter-sized generator using Co2MnAl0.69Si0.31 delivered 2.2 mV output voltage and maximum power of 7.7 μW under ΔT = 15 K. This is a proof-of-concept rather than a competitive generator, but demonstrates the architecture is functional at room temperature without any external field.

**Miniaturized transverse TEG (2025):** A device with footprint under 0.17 mm² produced thermoelectric output over 10 mV by combining anomalous Nernst and spin Seebeck effects. This demonstrates the principle scales down to MEMS-compatible dimensions.

**Permanent-magnet-assisted generator:** A bulk module with 12 pairs of permanent magnets (to fix magnetization direction in a soft magnetic material) achieved fill factors of ~80%, compared to ~30–60% typical of conventional Seebeck thermopile modules. The geometry works in the Nernst harvester's favor: a single continuous slab of material can be used rather than many small paired legs.

**Thin-film bilayer (2024):** Combining a thermoelectric silicon film with a magnetic Fe-Ga layer produced a maximum output of 15.2 μV/K — approximately six times larger than the Fe-Ga alloy alone — by the off-diagonal Seebeck coupling between layers.

## The Geometric Advantage

The Seebeck thermopile requires carefully cut and electrically connected alternating n- and p-type legs arranged in a π-array. Achieving high fill factors (the fraction of the module area actually occupied by active material rather than gaps and contacts) is difficult: commercial Seebeck modules typically reach 30–60%.

Nernst-based harvesters can use a simpler geometry: a single flat sheet or coil of material carries heat in one direction and produces voltage at the edges. No alternating legs, no p/n pairing requirement, no complex dicing. This simplicity could reduce fabrication costs and increase fill factor substantially. Coiled-wire Nernst geometries have demonstrated fill factors approaching 70–80%.

The tradeoff is coefficient magnitude: without Berry-curvature enhancement, the Nernst transverse output per Kelvin is much smaller than longitudinal Seebeck output. The anomalous Nernst in topological and Heusler magnets is narrowing this gap.

## Why It Remains Underexplored

Compared with the Seebeck effect, the Nernst effect has attracted far less industrial development. Several reasons:

- The ordinary Nernst effect requires an external magnetic field, which is a hardware overhead that makes it impractical for most applications
- The anomalous Nernst effect was understood to be small in classical ferromagnets; the recognition that topological and Weyl materials could have large ANE driven by Berry curvature is relatively recent (post-2019)
- There is no commercial ANE module market yet — the field is at the stage of material-discovery and laboratory demonstration

This leaves a strategic gap. Several obvious opportunities remain barely explored:

- Screening of low-cost magnetic alloys (particularly Mn- and Fe-based compounds) for large ANE without rare-earth or noble-metal content
- Geometry optimization: the right module architecture for the transverse geometry has not been standardized the way Seebeck π-modules have
- Thin-film integration: the ANE is a surface/volume effect that may integrate well with MEMS and thin-film deposition processes

## Market Context

There is no dedicated commercial market for anomalous Nernst generators as of 2025. The effect sits within the broader thermoelectric generator market (~$1.0–1.05B in 2025, growing to ~$1.4–1.7B by 2030), as an emerging alternative geometry rather than a distinct product category.

The nearest commercial analogues are the spin Seebeck effect devices and magnonic devices being developed in Japan (particularly through the NIMS/Tohoku University ecosystem), where anomalous Hall and Nernst effects in magnetic oxides and Heusler compounds are part of active device programs.

The commercial inflection point for ANE devices would require: (1) a material with Sxy > 10 μV/K at 300 K in an earth-abundant, easily fabricated form, and (2) a module architecture that demonstrates competitive power density vs. Seebeck at the same ΔT. Both remain research targets rather than solved problems.

## Current Research Frontiers

**Topological Weyl and Kagome magnets** — Co3Sn2S2, Mn3Sn, and Kagome-lattice materials like ErMn6Sn6 combine large Berry curvature with room-temperature magnetic order, producing anomalous Nernst signals that dwarf earlier ferromagnetic metals. These are the current leading materials.

**Berry curvature engineering** — the ANE signal is proportional to the Berry curvature integrated over the Fermi surface. Band structure calculations can identify materials where Weyl points or nodal lines sit close to the Fermi level, maximizing this integral. This has become a predictive design strategy.

**Artificially tilted multilayers** — layering magnetic and non-magnetic materials at a tilt angle induces off-diagonal Seebeck-like contributions that mimic a large transverse thermoelectric effect without requiring a bulk Nernst material. This is an architecture-level design strategy that bypasses the need for topological band structure.

**Antiferromagnetic ANE** — Mn3Sn produces an ANE despite having essentially zero net magnetization. This opens the effect to antiferromagnets, which are more common, more stable, and have faster switching than ferromagnets — potentially important for scalable applications.

## Connections to the Larger Landscape

- **The Seebeck effect** provides the more familiar thermoelectric baseline. The Nernst geometry departs from it in both physics (transverse vs. longitudinal) and materials strategy (magnetic/topological vs. semiconducting).
- **Spin Seebeck effect** (Part XIII) is a close cousin — also transverse, also involving magnetic order, but driven by magnon rather than electron transport. The two effects often coexist in the same material and require careful separation in measurements.
- **Magnon-phonon coupling** (Part XIV) is relevant here because phonon drag and magnon-phonon scattering can contribute to or suppress the observed Nernst signal.
- **Part IV** highlights anomalous Nernst screening in cheap magnets as one of the more accessible university-scale experimental opportunities — the measurement requires only a temperature gradient, a voltmeter, and a magnet, making it low-barrier to explore.
