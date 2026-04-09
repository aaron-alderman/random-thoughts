# Industrial Engineering Landscape Guide
## Multi-Plane Control Framework for Chemical Process Design & Discovery

**Version 3** — Full Model Integration: Objects · Properties · Relationships · Calculations · Pathways · Constraints · Actors

---

## Preamble

Science has exploded and no one can keep up. The missing middles are not hidden — they are in different rooms that nobody walks between. This framework builds the corridors.

---

## 1. Purpose

This document defines a structured framework for exploring, designing, and discovering chemical processes using a multi-plane control model. It has been expanded from its original engineering foundation to incorporate biological systems, materials science frontiers, emerging physics, robotics as a control mechanism, and a formal actor model covering humans, AI, and regulatory systems.

It is intended to:

- Map the full design space of chemical engineering systems across all domains
- Identify missing "middle layers" between known mechanisms
- Enable AI-assisted, tree-search-based exploration and synthesis
- Provide a common language across chemistry, physics, materials science, biology, and engineering
- Serve as a **living document** — extensible as new fields and phenomena emerge

---

## 2. Core Principles

> *Chemical processes are not controlled directly. They are controlled by shaping the environment, energy flow, and state transitions of matter.*

> *The goal is not to force reactions, but to design environments where desired pathways become statistically dominant.*

> *Multi-plane control over state-space trajectories under non-equilibrium conditions.*

---

## 3. The Modelling Framework

Before enumerating planes and pathways, a consistent modelling framework is needed. The following seven elements provide the ontological scaffold for the entire system. They apply at every level — from a single reaction step to a full industrial process.

### 3.1 Objects

The entities that exist in the system. Everything that can be named, measured, or acted upon.

- **States** — molecular geometries, electronic configurations, phases, aggregate structures
- **Intermediates** — transition states, radical species, excited states, surface-bound species
- **Control Planes** — the mechanisms themselves (see Section 5–9)
- **Materials** — catalysts, solvents, substrates, membranes, surfaces
- **Products and byproducts**
- **Actors** — agents that deploy or embody control mechanisms (see Section 10)
- **Information** — sequence data, sensor readings, model outputs, experimental results

### 3.2 Properties

Attributes of objects that determine behaviour and measurability.

- **State properties** — energy, geometry, charge, spin, chirality, symmetry, lifetime
- **Plane properties** — domain, mechanism, timescale, technology readiness, scalability
- **Material properties** — electronic structure, surface area, porosity, stability, availability
- **Process properties** — yield, selectivity, energy efficiency, throughput, separation feasibility
- **Actor properties** — capability, latency, scope of authority, risk tolerance, regulatory status

### 3.3 Relationships

How objects interact, influence, and depend upon each other. **This is where missing middles live.**

- **Plane → Transition** — plane X influences transition Y (or could, but hasn't been attempted)
- **State → State** — state A can reach state B under specific conditions
- **Plane ↔ Plane** — planes couple, reinforce, or interfere with each other
- **Actor → Plane** — actor deploys, monitors, or restricts a control plane
- **Constraint → Relationship** — a constraint blocks or modifies a relationship
- **Field boundary gaps** — plane known in domain A, never applied in domain B

The relationship layer is the primary target of AI-assisted exploration. The tree search is fundamentally a search over undefined or undiscovered relationships.

### 3.4 Calculations

Quantitative operations that evaluate feasibility, score candidates, and predict outcomes.

- **Thermodynamics** — is the pathway energetically allowed?
- **Kinetics** — are rates compatible with the cascade timescale?
- **Transport** — do mass and heat transfer permit the process?
- **Energy efficiency** — what is the minimum theoretical energy cost?
- **Selectivity scoring** — how strongly does the control plane bias the target pathway?
- **Technology readiness scoring** — how mature is the implementation of this plane?
- **Climate impact scoring** — net carbon, energy source compatibility, materials criticality
- **Missing middle scoring** — novelty × feasibility × potential impact

### 3.5 Pathways

Sequences of transitions from feedstock to product. The cascade model (Section 11) is the formal pathway representation.

- **Known pathways** — industrially established, optimised within existing plane combinations
- **Candidate pathways** — thermodynamically allowed, not yet demonstrated
- **Blocked pathways** — kinetically or mechanistically inaccessible without a missing control plane
- **Branching points** — where multiple pathways diverge; the tree search expands here
- **Dead ends** — paths pruned by feasibility filters

### 3.6 Constraints

Conditions that restrict which objects, relationships, and pathways are accessible. Critically: **constraints are often misclassified control planes** — a mechanism treated as a fixed limit is frequently an undiscovered lever.

- **Thermodynamic constraints** — forbidden by equilibrium
- **Kinetic constraints** — rates incompatible with process timescale
- **Transport constraints** — mass or heat transfer limited
- **Scalability constraints** — control plane not implementable at industrial scale
- **Materials constraints** — required material does not exist
- **Regulatory constraints** — Actor class; some pathways require permissions, approvals, or are prohibited (see Section 10)
- **Safety constraints** — Actor class; some planes require human oversight by design
- **Timescale constraints** — two steps in a cascade operate at incompatible rates

> **The key diagnostic question:** Is this a true constraint, or a constraint because no one has applied the right control plane to overcome it?

### 3.7 Actors

Agents that deploy, monitor, restrict, or discover control planes. Actors are first-class objects in the model, not background assumptions. A missing middle may be solvable by a **known plane deployed by a new actor**.

See Section 10 for full treatment.

---

## 4. The Missing Middle Problem

Most industrial chemistry is stuck in local optima. Processes were discovered empirically, scaled up, and locked in before anyone had the conceptual tools to ask: *what else could control this transition?*

Between feedstock A and product B, there are intermediate states that are thermodynamically accessible but kinetically invisible because no one has combined the right control planes to stabilise them long enough. This is not a small gap — it is potentially where most of the value in next-generation chemistry lives.

### Historical Missing Middles — Obvious in Retrospect

| Discovery | What Was Known | What Was Missing |
|---|---|---|
| Zeolites in catalysis | Mineral structure known in geology | Connection to confinement as a control plane |
| CRISPR | Restriction enzymes known for decades | Programmable editing as an application |
| Perovskite solar cells | Crystal structure known since 1839 | Application to photovoltaics (first in 2009) |
| Graphene | Existed in pencil marks | Isolation method (scotch tape, 2004) |
| Statins | Fungal metabolites known | Connection to human cardiovascular pathway |
| Frustrated Lewis Pairs | Lewis acids and bases well understood | Sterically prevented self-neutralisation as a feature |

Every one of these was a missing middle: known components, unasked question connecting them.

---

## 5. Primary Control Planes — Engineering & Physics

The foundational set, derived from physical chemistry and engineering practice. Expanded here to include chirality, mechanical, acoustic, and interfacial planes identified as systematically overlooked by treating them as constraints rather than controls.

### 5.1 Electronic Plane
- **Domain:** Electrons, orbitals, charge
- **Controls:** Bond strength, radical formation, reactivity
- **Tools:** Electrochemistry, band alignment, redox systems
- **Missing middle signal:** Most industrial electrochemistry operates at bulk electrode level; molecular-scale electronic control is largely unexplored

### 5.2 Vibrational Plane
- **Domain:** Molecular motion
- **Controls:** Bond elongation, symmetry breaking, selective bond activation
- **Tools:** IR excitation, thermal energy, ultrasound
- **Coupling note:** Overlaps with Photonic (IR excitation) and Acoustic planes; the coupling between them is underexplored

### 5.3 Photonic Plane
- **Domain:** Electromagnetic radiation
- **Controls:** Excitation, energy injection, photocatalysis
- **Tools:** Visible/UV light, lasers, optical cavities
- **Missing middle signal:** Circularly polarised light as a chirality control input sits at the intersection of Photonic and Chirality planes — almost entirely unexplored industrially

### 5.4 Field / Gradient Plane
- **Domain:** Spatial electromagnetic variation
- **Controls:** Polarisation, quadrupole coupling, orientation
- **Tools:** Electric fields, plasmonics, nanogaps
- **Missing middle signal:** Field gradients at sub-nanometre scale accessible via STM tips and nanogap devices remain almost entirely disconnected from preparative chemistry

### 5.5 Structural Plane
- **Domain:** Material geometry
- **Controls:** Adsorption, orientation, binding geometry
- **Tools:** Catalysts, surfaces, defects, interfaces
- **Note:** Bulk surfaces are well-studied; defect engineering as intentional design is underutilised

### 5.6 Confinement / Entropic Plane
- **Domain:** Accessible configurations
- **Controls:** Selectivity, pathway restriction, effective concentration
- **Tools:** Zeolites, pores, cavities, MOFs, COFs, covalent organic frameworks
- **Missing middle signal:** COFs are more designable than zeolites and less explored; most confinement work remains inorganic

### 5.7 Thermal Plane
- **Domain:** Statistical energy distribution
- **Controls:** State population, diffusion, reaction rates
- **Tools:** Heat, temperature gradients, cryogenics
- **Constraint reframe:** Thermal noise is a nuisance in engineering; biology exploits it for sampling and switching (stochastic resonance)

### 5.8 Chemical Potential Plane
- **Domain:** Concentrations and pressures
- **Controls:** Reaction direction, equilibrium position
- **Tools:** Reactant ratios, pressure, flow rate, membrane separation
- **Coupling note:** Deeply entangled with Thermal plane; biology resolves this entanglement by operating isothermally and coupling reactions — an underused industrial strategy

### 5.9 Temporal Plane
- **Domain:** Timing and sequencing
- **Controls:** Synchronisation of cascade steps
- **Tools:** Pulsed fields, residence time, flow control, microreactors
- **Missing middle signal:** Endogenous timing logic (as in circadian rhythms) has no industrial equivalent; all temporal control is currently exogenous

### 5.10 Feedback Plane (Meta)
- **Domain:** System evolution over time
- **Controls:** Stability, self-regulation, adaptive response
- **Tools:** Recycling loops, adaptive environments, closed-loop control
- **Actor dependency:** Effective feedback planes require an actor — human, automated system, or AI — to close the loop

### 5.11 Chirality Plane
- **Domain:** Spatial asymmetry at molecular and supramolecular scale
- **Controls:** Enantiomeric selectivity, asymmetric pathway access, chiral amplification
- **Tools:** Chiral catalysts, circularly polarised light, chiral surfaces, asymmetric templating
- **Why it is systematically overlooked:** Treated as a purity problem to be managed rather than a control lever to be pulled. There are almost certainly reaction pathways only accessible by maintaining chiral control throughout — intermediates that racemise before anyone stabilises them long enough to see where they lead.
- **Scale of the gap:** Chirality connects electronic, photonic, structural, and confinement planes simultaneously. It is one of the most underdeveloped cross-cutting control mechanisms in industrial chemistry.

### 5.12 Mechanical / Stress Plane
- **Domain:** Force, strain, and pressure at material and molecular scale
- **Controls:** Mechanochemistry, piezoelectric coupling, strain-tuned reactivity
- **Tools:** Ball milling, strain engineering, atomic force microscopy, high-pressure synthesis
- **Constraint reframe:** Pressure is typically a processing parameter. It actually reshapes entire potential energy surfaces and accesses phases unavailable at ambient conditions.

### 5.13 Acoustic / Phonon Plane
- **Domain:** Sound waves and lattice vibrations
- **Controls:** Cavitation, local energy deposition, phonon-assisted reactions
- **Tools:** Ultrasound, phononic crystals, acoustic reactors
- **Coupling note:** Distinct from Vibrational plane despite apparent overlap; cavitation creates extreme local conditions (temperature, pressure) inaccessible by any other means

### 5.14 Interfacial / Phase Boundary Plane
- **Domain:** Boundaries between bulk phases
- **Controls:** Unique reactivity unavailable in either bulk phase
- **Tools:** Liquid-liquid interfaces, Pickering emulsions, solid-liquid interfaces
- **Constraint reframe:** Interfaces are treated as boundaries to manage. They are distinct chemical environments — often the most reactive sites in a system.

### 5.15 Spin Plane
- **Domain:** Electron and nuclear spin states
- **Controls:** Radical pathways, recombination selectivity, spin-forbidden transitions
- **Tools:** Magnetic fields, spin-polarised currents, CIDNP, MRI-guided chemistry

---

## 6. Biological Control Planes

Biology has spent 3.8 billion years solving the missing middle problem through evolution. It is the most sophisticated process discovery engine that exists. Every biological control mechanism that has no engineering equivalent is a gap in the industrial landscape.

**Note on photosynthesis:** Photosynthesis is the canonical multi-plane coupled system — photonic energy harvesting, quantum coherence for transfer efficiency, charge separation via the electronic plane, proton gradient via the membrane/compartment plane, enzymatic fixation via molecular recognition, all synchronised via temporal and feedback planes. It is not a special case. It is the template.

### 6.1 Allosteric / Conformational Plane
- **Domain:** Shape-mediated information transfer
- **Controls:** Remote control of reactivity via binding events at distant sites
- **Tools:** Allosteric enzymes, cooperative proteins, biosensors, synthetic allosteric catalysts
- **Industrial gap:** Engineering has no equivalent of remote conformational control at molecular scale. Closest analogue is feedback control in process engineering — operating at vastly larger scales and slower timescales.

### 6.2 Molecular Recognition Plane
- **Domain:** Complementary geometry and charge
- **Controls:** Transition state stabilisation, binding selectivity
- **Tools:** Enzymatic lock-and-key, induced fit, aptamers, molecularly imprinted polymers
- **Relationship to Confinement plane:** Zeolites are a crude static approximation. Molecular recognition adds dynamic adaptation — the cavity responds to the substrate.

### 6.3 Membrane / Compartment Plane
- **Domain:** Lipid bilayers, vesicles, organelle boundaries
- **Controls:** Ion gradients, reaction localisation, proton-motive force
- **Tools:** Liposomes, synthetic cells, proteoliposomes, polymersome reactors
- **Missing middle signal:** Compartmentalisation without membranes (see Phase Separation plane) is even less explored industrially

### 6.4 Signalling Cascade Plane
- **Domain:** Molecular information propagation
- **Controls:** Amplified downstream response triggered by minimal input
- **Tools:** Kinase networks, second messengers, synthetic gene circuits
- **Ontological note:** This is an information plane. The signal is not energy — it is instruction. Engineering rarely thinks in these terms.

### 6.5 Coupled Reaction Networks Plane
- **Domain:** Thermodynamically linked reactions
- **Controls:** Driving thermodynamically unfavourable reactions via coupling to favourable ones
- **Tools:** ATP hydrolysis coupling, NAD+/NADH cycling, chemiosmotic coupling
- **Industrial gap:** Biology runs isothermally by coupling reactions. Industry drives reactions thermally. The biological strategy is more energy-efficient but almost never replicated in industrial design.

### 6.6 Chaperone / Scaffolding Plane
- **Domain:** Folding and assembly assistance
- **Controls:** Preventing misfolding, holding intermediates in productive conformations
- **Tools:** HSP proteins, synthetic scaffolds, DNA origami, supramolecular hosts
- **Relationship to Trap concept:** Chaperones are biological traps — they extend the lifetime of productive conformations. The engineering equivalent barely exists.

### 6.7 Cooperative / Switch-like Plane
- **Domain:** Nonlinear concentration response
- **Controls:** Threshold-triggered state switching, signal amplification
- **Tools:** Hill equation systems, bistable genetic circuits, allosteric cooperativity
- **Constraint reframe:** Cooperative effects are treated as complications in kinetic models. They are actually precision control mechanisms for switch-like responses.

### 6.8 Quorum / Population Plane
- **Domain:** Collective behaviour at population density threshold
- **Controls:** Coordinated switching across a population of units
- **Tools:** Quorum sensing molecules, synthetic gene circuits, population-level control
- **Industrial gap:** Industrial fermentation almost entirely ignores population-level coordination. Each cell is treated as independent.

### 6.9 Evolutionary / Adaptive Plane
- **Domain:** Self-modifying control logic
- **Controls:** The system rewrites its own mechanisms in response to outcomes
- **Tools:** Directed evolution, in vitro selection, SELEX, continuous evolution platforms
- **Actor intersection:** This plane requires an actor to select and propagate — whether natural selection, a scientist, or an automated platform

### 6.10 Phase Separation / Biomolecular Condensate Plane
- **Domain:** Liquid-liquid phase separation within a single compartment
- **Controls:** Spatial concentration and reaction localisation without membranes
- **Tools:** Intrinsically disordered proteins, stress granule engineering, synthetic condensates
- **Status:** Discovered recently; almost entirely unexplored for industrial application

### 6.11 Post-translational / Dynamic Modification Plane
- **Domain:** Reversible chemical modification of existing machinery
- **Controls:** Switching activity without rebuilding the catalyst
- **Tools:** Phosphorylation, ubiquitination, acetylation, synthetic post-translational systems
- **Industrial analogue:** Catalyst regeneration is the crude equivalent. Reversible switching of activity is not yet achievable in synthetic systems.

### 6.12 Glycan / Molecular Code Plane
- **Domain:** Sugar chain information encoding on cell surfaces
- **Controls:** Cell signalling, molecular recognition, immune modulation
- **Tools:** Glycoengineering, lectins, glycan arrays
- **Status:** The glycan code is largely undeciphered. It may represent an entire control language not yet readable.

### 6.13 Intrinsic Disorder Plane
- **Domain:** Proteins and polymers with no fixed structure that are nevertheless functional
- **Controls:** Disorder itself as the control mechanism — flexible, adaptive binding
- **Tools:** Intrinsically disordered proteins, disordered polymer networks
- **Constraint reframe:** Disorder is treated as failed structure. In biology, it is a feature — enabling promiscuous binding, rapid response, and hub function in networks.

---

## 7. Emerging & New Physics Planes

Phenomena discovered in physics and materials science that have not yet been connected to process design. These represent the frontier of the missing middle landscape — the rooms that exist but have no corridors to chemistry yet.

### 7.1 Quantum Coherence Plane
- **Domain:** Quantum superposition in biological and material systems
- **Controls:** Efficient energy transfer, pathway selection via interference
- **Tools:** Photosynthetic complexes, quantum dots, cold molecules, engineered chromophore arrays
- **Status:** Biology already exploits this (photosynthesis, avian navigation, enzyme tunnelling). Engineering does not.

### 7.2 Topological Protection Plane
- **Domain:** Symmetry-protected states immune to local perturbation
- **Controls:** Robust transitions that cannot be disrupted by local disorder
- **Tools:** Topological insulators, edge states, Majorana fermions
- **Missing middle signal:** Reaction pathways that are robust by topology rather than engineering tolerance — entirely unexplored

### 7.3 Vibronic Coupling Plane
- **Domain:** Linked electronic and vibrational states
- **Controls:** Energy transfer across planes, non-adiabatic dynamics
- **Tools:** Conical intersections, non-adiabatic molecular dynamics, Jahn-Teller systems
- **Ontological note:** This is a coupling plane — it exists at the interface between Electronic and Vibrational planes. Its power comes from the coupling itself.

### 7.4 Polaritonic / Strong Coupling Plane
- **Domain:** Light-matter hybridisation in optical cavities
- **Controls:** Modified potential energy surfaces, altered reaction rates and selectivity
- **Tools:** Fabry-Pérot cavities, plasmonic nanocavities, polariton condensates
- **Status:** Laboratory demonstration only; industrial implementation pathway unknown

### 7.5 Quantum Tunnelling Plane
- **Domain:** Barrier crossing below classical energy thresholds
- **Controls:** Low-temperature reaction rates, proton and hydrogen transfer
- **Tools:** STM-induced reactions, enzyme active sites, H-transfer catalysis
- **Relationship:** Connects to Biological planes — enzymatic tunnelling is an evolved exploitation of this plane

### 7.6 Non-equilibrium / Dissipative Structure Plane
- **Domain:** Far-from-equilibrium self-organisation
- **Controls:** Pattern formation, Turing instabilities, oscillating reactions
- **Tools:** Reaction-diffusion systems, Belousov-Zhabotinsky reaction, dissipative self-assembly
- **Industrial gap:** Almost all industrial processes minimise deviations from equilibrium. Far-from-equilibrium organisation as a design strategy is nearly unexplored.

### 7.7 Twistronics / Moiré Plane
- **Domain:** Stacking angle of 2D materials creating emergent electronic properties
- **Controls:** Electronic, optical, and superconducting properties tuned by geometry alone
- **Tools:** Magic-angle graphene, TMD heterostructures, moiré superlattices
- **Status:** New physics (2018); zero industrial application yet. The control parameter is purely geometric.

### 7.8 Time Crystal / Temporal Order Plane
- **Domain:** Matter that oscillates periodically without energy input
- **Controls:** Synchronisation of coupled processes, persistent oscillation
- **Tools:** Floquet systems, driven quantum systems, discrete time crystals
- **Status:** Very new physics; speculative industrial relevance but potentially significant for temporal synchronisation of cascades

### 7.9 Casimir / Quantum Vacuum Plane
- **Domain:** Quantum vacuum fluctuations at nanoscale separations
- **Controls:** Adhesion, self-assembly, nanoscale forces
- **Tools:** Casimir force devices, nanogap engineering, van der Waals heterostructures
- **Status:** Significant at sub-10nm; increasingly relevant as engineering moves to molecular scale

### 7.10 Neuromorphic / Computational Matter Plane
- **Domain:** Materials that compute through their own state changes
- **Controls:** Adaptive response, memory encoded in material rather than software
- **Tools:** Memristors, phase-change materials, ionic neuromorphic devices
- **Missing middle signal:** The material itself as the control logic — eliminating the need for external computation in process control

---

## 8. Acid / Base & Hybrid Equilibrium Systems

Acidity and basicity are typically treated as fixed process conditions. They are more accurately understood as a continuous control spectrum with underexplored extremes — and as a dynamic variable that can be programmed across a cascade.

### 8.1 Superacids
Beyond 100% sulfuric acid on the Hammett acidity scale. Fluoroantimonic acid is approximately 10²⁰ times stronger than sulfuric acid. Protonates substrates considered non-basic. Opens reaction pathways thermodynamically inaccessible under normal acidity. Essentially unexplored at industrial scale.

### 8.2 Superbases
Activates C-H bonds and drives reactions considered thermodynamically impossible under normal conditions. Largely confined to academic research. The industrial gap is significant.

### 8.3 Frustrated Lewis Pairs (FLPs)
A molecule simultaneously acting as Lewis acid and base but unable to self-neutralise due to steric bulk. Creates a reactive cavity that activates H₂, CO₂, and N₂ without metal catalysts. A control plane with massive unexplored industrial potential — particularly relevant to climate applications (CO₂ activation, green hydrogen).

### 8.4 Proton-Coupled Electron Transfer (PCET)
Proton and electron move together; neither alone achieves the same selectivity. Central to biology (photosynthesis, respiration), peripheral to industrial chemistry. A coupling plane sitting at the intersection of Electronic and Chemical Potential planes.

### 8.5 Amphoteric / Switchable Equilibrium Systems
Using pH as a programmable control variable across a cascade, not a fixed condition. Tilting equilibrium dynamically. Chemically switchable acid/base systems can be used to drive sequential steps — an underutilised active control strategy.

---

## 9. Materials Science Frontiers

New material classes that represent unexplored substrates for control plane implementation.

### 9.1 High Entropy Alloys
Five or more principal elements creating vast compositional space with emergent catalytic properties. Mostly unexplored for catalysis. The composition itself becomes a searchable design space.

### 9.2 2D Materials Beyond Graphene
MXenes, boron nitride, transition metal dichalcogenides. Each has unique electronic, chemical, and mechanical properties. Most have not been thought of as control plane substrates.

### 9.3 Covalent Organic Frameworks (COFs)
Crystalline, porous, designable at molecular level. More designable than zeolites, less explored. Represent the intersection of Confinement and Structural planes with atomic precision.

### 9.4 Programmable / Active Matter
Materials that reconfigure in response to stimuli, or that consume energy and generate organisation internally. The material is not passive — it is a participant.

### 9.5 Metamaterials
Structured to have properties impossible in natural materials. Negative refractive index, acoustic cloaking, electromagnetic field concentration. The structure is the property.

### 9.6 Defect-Engineered Materials
Intentional vacancies, dopants, grain boundaries as designed control sites rather than contamination. The most active sites in many catalytic systems are the defects, not the bulk.

---

## 10. Actors

Actors are agents that deploy, monitor, restrict, or discover control planes. They are first-class objects in the modelling framework, not background assumptions.

**Key principle:** A missing middle may be solvable by a known plane deployed by a new actor. The actor layer is as important as the plane layer for systematic discovery.

### 10.1 Human Actors

**Process operators and engineers**
- Deploy and tune control planes in real time
- Carry institutional knowledge that is rarely formalised
- Safety-critical decisions remain human by design and regulation

**Scientists and researchers**
- Primary source of new plane discovery
- Currently siloed by discipline — the framework is designed to bridge this
- Cross-domain movement of planes (biology → chemistry, physics → materials) is almost always human-initiated

**Safety actors**
- Some planes require human oversight by design, not just by regulation
- High-energy planes (superacids, high-pressure, plasma), radiological processes, and processes with irreversible failure modes require human-in-the-loop architectures
- The framework must flag these explicitly at the pathway level

**Domain experts as validators**
- AI-generated missing middle candidates require human expert validation before experimental pursuit
- The human is not replaced by the framework — they are given better questions to answer

### 10.2 AI / LLM Actors

AI systems are powerful for traversing the plane-transition relationship space and surfacing missing middle candidates. Their role is **exploration and pattern detection**, not decision or execution.

**Appropriate roles:**
- Systematic crossing of planes against transitions
- Literature synthesis across field boundaries
- Pattern detection in known process motifs
- Scoring and ranking of missing middle candidates
- Generating hypotheses for human expert review

**Limitations that must be respected:**
- LLMs hallucinate — all outputs require expert validation before experimental pursuit
- LLMs lack genuine physical intuition — scoring functions must be externally validated
- LLMs cannot assess practical implementability — a human or domain simulation must evaluate this
- LLMs should not drive experimental decisions without human review in the loop
- The framework treats AI as a powerful search tool, not an autonomous agent

**Recommended architecture:** AI generates candidates → human expert filters → robotic system tests → results feed back into AI search

### 10.3 Regulatory & Governmental Actors

Regulation is not a soft constraint — it is a hard actor that controls which pathways are accessible in practice, independent of thermodynamic or kinetic feasibility.

**Regulatory domains with major process implications:**

| Domain | Regulatory Challenge | Impact on Pathways |
|---|---|---|
| Nuclear / radiological | Extreme regulatory overhead, public perception, liability | Radiochemical control planes largely inaccessible for industrial use despite known efficacy |
| GMO / synthetic biology | Variable by jurisdiction; EU highly restrictive | Biological control planes using engineered organisms blocked in many markets |
| Nanotechnology | Emerging regulatory frameworks; uncertain | Novel material planes face approval timelines longer than development timelines |
| Electrochemical / high-voltage | Safety regulations constrain operating windows | Some electronic plane configurations not permissible at scale |
| Superacids / hazardous reagents | Handling, transport, and waste regulations | Superacid control planes restricted by practical regulatory burden |
| CO₂ and climate | Evolving carbon markets and mandates | Creates incentive structures that make previously uneconomic pathways viable |
| Pharmaceutical synthesis | GMP, impurity profiling, regulatory filing | Pathway changes require full revalidation — locking in suboptimal processes |

**The regulatory actor as a search filter:**
The framework should flag regulatory status as a property of pathways, not just a footnote. A missing middle that is thermodynamically valid, kinetically feasible, and practically implementable but regulatory-blocked is a different kind of gap — one that requires a different kind of actor to unlock.

**Regulatory actors as potential enablers:**
Policy change, regulatory sandboxes, and international harmonisation can open pathways previously inaccessible. The framework should track these as events that expand the searchable space.

### 10.4 Robotic Actors

Physical robotic intervention is not simply automation of existing steps. It is a distinct control mechanism operating at a different ontological level — one that can intervene on other control planes in real time.

**Microrobotics / Nanorobotics**
Swimming robots delivering catalysts, removing products, maintaining local conditions inside a reactor. The robot as mobile missing middle — bringing a control plane to the state rather than bringing the state to the plane.

**Soft Robotics as Dynamic Confinement**
Programmable soft structures that reshape reaction spaces in response to process state. Confinement that adapts in real time — the biological equivalent is the enzyme active site.

**Robotic Evolutionary Search**
Physical robots iterating through experimental space faster than human intuition. The Cronin group at Glasgow has demonstrated early versions of this. The framework extends this concept to the full plane taxonomy.

**Precise Mechanical Intervention**
Robotic systems manipulating reaction environments at molecular scale — not automation of existing steps but robots as active chemical participants deploying the Mechanical/Stress plane with precision.

**The Human-Robot-AI Triad**
The most powerful actor configuration: AI generates missing middle candidates → robotic system executes experimental tests → human expert evaluates results and steers the search. The triad is itself a control mechanism over the discovery process.

### 10.5 Evolutionary / Biological Actors (Meta)

Evolution is the original missing middle discovery engine. Directed evolution platforms, continuous evolution systems (PACE, OrthoRep), and synthetic biology foundries represent the industrialisation of evolutionary search.

These actors are distinct from biological control planes — they are agents that discover and deploy new planes, not planes themselves.

---

## 11. The Cascade Model

All viable processes follow a common sequence. Missing middles correspond to missing steps or uncontrolled transitions within this sequence.

1. **Activation** — energy input to the system (which plane delivers it?)
2. **Symmetry breaking** — selection of a pathway direction (which plane biases it?)
3. **Intermediate stabilisation (Trap)** — extending lifetime of reactive species (which plane creates the trap?)
4. **Conversion** — the reaction step itself
5. **Product formation** — reaching the target state
6. **Removal / separation** — extracting product to prevent back-reaction

### The Trap Concept

A trap is any structure that selectively stabilises specific states, extends the lifetime of reactive intermediates, and prevents relaxation into lower-energy configurations. Traps are the engineering equivalent of enzyme active sites.

**Known trap implementations:**

| Trap Type | Plane | Biological Analogue |
|---|---|---|
| Catalytic surface site | Structural | Enzyme active site |
| Zeolite pore | Confinement | Ribosome tunnel |
| Electric field gradient | Field/Gradient | Membrane potential |
| Solvent cage | Chemical Potential | Hydrophobic pocket |
| Optical cavity | Photonic/Polaritonic | Photosystem reaction centre |
| Chaperone protein | Scaffolding | HSP70/90 system |
| Biomolecular condensate | Phase Separation | P-body, stress granule |
| DNA origami scaffold | Structural/Confinement | Cellulosome |

---

## 12. Constraints Reframed as Controls

The most productive source of missing middles. Every field has mechanisms it treats as fixed parameters, nuisances, or noise. Those are exactly where undiscovered control planes hide.

> **Ask of every field: what is it treating as noise?**

| Apparent Constraint | Actual Control Plane | Example of Reframing |
|---|---|---|
| Chirality | Chirality Plane | Asymmetric amplification, pathway access gating |
| Isotope effects | Electronic / Tunnelling | Kinetic isotope control for pathway selection |
| Solvent | Chemical Potential | Active participant in proton shuttling and TS geometry |
| Defects / Impurities | Structural | Most catalytically active sites in many systems |
| Pressure | Mechanical | Reshapes entire potential energy surfaces |
| Thermal noise | Thermal / Cooperative | Exploited by biology for sampling (stochastic resonance) |
| Aging / History | Feedback | Hysteresis and memory effects as designed features |
| Interfaces | Interfacial | Distinct reactive environments unavailable in bulk |
| Disorder | Intrinsic Disorder | Adaptive binding, hub function in networks |
| Cooperative effects | Cooperative / Switch-like | Precision nonlinear switching |

---

## 13. Universal Industrial Insights

Across scalable processes — observations that hold broadly but with domain-specific exceptions:

1. **Surfaces dominate chemistry** — true for heterogeneous catalysis; less so for homogeneous or enzymatic systems
2. **Cascades outperform single-step reactions** — biological systems have known this for 3.8 billion years
3. **Selectivity is achieved by constraint, not precision** — confinement, shape, and environment bias outcomes; force does not
4. **Energy must be delivered locally** — bulk heating is wasteful; targeted delivery is the biological strategy
5. **Equilibrium must be actively managed** — removal of product, coupling reactions, non-equilibrium conditions
6. **Transport limits performance** — mass and heat transfer are frequently rate-limiting, not kinetics
7. **Robustness beats optimality** — processes that survive perturbation outperform theoretically optimal but fragile ones
8. **Separation is as important as reaction** — frequently overlooked in early-stage design
9. **The actor layer determines what is accessible** — a thermodynamically valid pathway blocked by regulation or missing technology is not yet a viable pathway

---

## 14. AI-Assisted Exploration

### Representation
- **Nodes** = states (with properties: energy, geometry, charge, spin, chirality, lifetime)
- **Edges** = transitions (with properties: rate, selectivity, timescale, active planes)
- **Attributes** = control planes active at each transition; technology readiness; feasibility scores

### Search Strategy
The framework operationalises as a **guided tree search**:
- Root: feedstock + target product
- Branching logic: which control planes could enable this transition?
- Pruning: thermodynamic impossibility, transport limits, missing stabilisation, regulatory blocks
- Expansion: for surviving branches, enumerate next-level transitions
- **Cross-domain flag:** which planes exist in another field but have never been applied here?

### Objective Functions
- Yield, selectivity, energy efficiency
- Scalability and continuous operation capability
- Climate impact (net carbon, renewable energy compatibility, materials criticality)
- Missing middle novelty score (novel plane combination × feasibility × potential impact)

### Pattern Detection
- Recurring cascade motifs across different chemistries
- Planes that consistently appear together (coupling signatures)
- Field-boundary gaps: plane known in domain A, never applied in domain B
- Constraints that appear repeatedly — strong signal of a missing control plane

### The Living Map
As new fields emerge — twistronics, biomolecular condensates, time crystals — they are encoded as new planes or new transitions. The crossing engine immediately surfaces new implications across everything already in the system. This is what a scientific community does over decades through conferences and serendipity. This framework does it systematically and continuously.

---

## 15. Failure Modes Checklist

- **Relaxation faster than reaction** — intermediate decays before conversion; trap missing
- **Competing pathways dominate** — selectivity problem, not yield problem; wrong plane or insufficient bias
- **Intermediates not stabilised** — trap missing or wrong plane for stabilisation
- **Transport limitations** — mass or heat transfer is rate-limiting, not kinetics
- **Catalyst poisoning** — stability over time not addressed at design stage
- **Energy misalignment** — control plane delivers energy at wrong frequency, location, or timescale
- **Timescale mismatch** — two cascade steps at incompatible rates; temporal plane missing
- **Missing technology** — control plane theoretically valid but not yet implementable; flag for materials science or instrumentation
- **Regulatory block** — pathway valid but inaccessible; requires actor-level intervention
- **Actor gap** — no actor capable of deploying the required plane at the required scale

---

## 16. Scalability Filters

A process must satisfy:

- Continuous operation capability
- Material availability at required scale
- Manageable temperatures and pressures (or regulatory approval for extreme conditions)
- Separation feasibility
- Long-term stability of control plane implementation
- Energy input compatible with renewable sources
- Actor availability — human oversight, regulatory approval, robotic capability where required

---

## 17. Ontological Notes — Observations on the Taxonomy

These observations emerged from building the framework. They suggest principles for how the taxonomy should be structured and extended.

**Controls vs. Constraints**
The most productive framing shift. Every field has mechanisms it treats as fixed parameters. Those are exactly where undiscovered control planes hide. Chirality is the clearest example — treated as a purity problem, actually a control lever for pathway access, asymmetric amplification, and surface selectivity.

**Planes operate at different ontological levels**
Some planes are physical (Electronic, Photonic). Some are geometric (Structural, Chirality). Some are informational (Signalling, Glycan code, Allosteric). Some are statistical (Thermal, Cooperative). Some are temporal (Temporal, Circadian). A complete taxonomy needs to span all levels — and the level itself is a searchable property.

**Biology is not a special case — it is the benchmark**
3.8 billion years of evolutionary search has solved the missing middle problem repeatedly. Every biological control mechanism with no engineering equivalent is a gap in the industrial landscape.

**The most powerful mechanisms are coupling planes**
Vibronic coupling, proton-coupled electron transfer, allosteric signalling — these are planes that exist at the interface between other planes. The coupling itself is the control mechanism. Single-plane thinking systematically misses these.

**Timescale mismatch is a meta-plane**
Many missing middles exist because two processes operate at incompatible timescales. Finding mechanisms that bridge timescales — traps, scaffolds, synchronisation — is a systematic source of discovery.

**The taxonomy should be generative, not enumerated**
A fixed list will always be incomplete. The generative rule is: *what can causally influence a state transition?* Physical, geometric, informational, statistical, temporal, and coupling mechanisms each define a class. New planes are discovered by asking which class a new phenomenon belongs to.

**Actors are a parallel taxonomy**
The plane taxonomy asks what mechanisms exist. The actor taxonomy asks who can deploy them. Missing middles exist in both dimensions — an unknown plane, or a known plane never deployed by the right actor in the right domain.

**Regulatory actors create a third search dimension**
Beyond planes and actors, regulatory status creates a third dimension of accessibility. Some pathways are thermodynamically and kinetically valid, actor-available, but regulatory-blocked. The framework must represent this explicitly, and track regulatory change as an event that expands the searchable space.

**The missing middle pattern clusters at field boundaries**
Missing middles are not uniformly distributed across the space. They cluster at discipline boundaries, at extreme conditions (superacids, topological matter, quantum regimes), and wherever a mechanism was discovered by one community and never exported to another. The framework should weight search effort accordingly.

---

## 18. Next Extensions

- **Quantitative scoring** of control plane effectiveness per transition type
- **Simulation integration** for feasibility pre-screening before experimental pursuit
- **Automated pathway generation** across the full plane taxonomy
- **Experimental design loops** with robotic execution
- **Formal ontology structure** for the plane registry — enabling machine-readable representation
- **Cross-domain index** — plane × transition matrix with known and unknown combinations flagged
- **Regulatory tracking layer** — monitoring policy changes that open previously blocked pathways
- **Climate impact integration** — scoring all pathways against net carbon and energy source compatibility
- **Actor capability registry** — what can current robotic, AI, and human actor configurations actually deploy?

---

## Appendix: The Modelling Framework Applied

A quick reference showing how the seven modelling elements map to the framework:

| Element | What It Captures | Where in Framework |
|---|---|---|
| **Objects** | States, intermediates, planes, materials, actors | Sections 5–10 |
| **Properties** | Energy, geometry, charge, timescale, TRL, regulatory status | Plane definitions throughout |
| **Relationships** | Plane→transition, state→state, plane↔plane, actor→plane | Section 3.3; the core of tree search |
| **Calculations** | Thermodynamics, kinetics, transport, scoring functions | Section 3.4; Section 15–16 |
| **Pathways** | Cascade sequences from feedstock to product | Section 11 |
| **Constraints** | Thermodynamic, kinetic, regulatory, actor gaps | Sections 3.6, 12, 15 |
| **Actors** | Humans, AI, regulators, robots, evolution | Section 10 |

---

*This document is version 3 of a living framework. It is designed to grow as new planes are discovered, new actors become available, and new regulatory environments open previously blocked pathways.*
