# Framework Applied: Distributed Fertilizer Production

## The Problem

The global fertilizer system is built on a hidden subsidy: cheap diesel makes centralised production and long-distance transport appear economically rational. Nitrogen fertilizer is made from air — a free, ubiquitous input — yet it is manufactured in massive centralised plants, shipped across the world under pressure as a toxic gas, distributed through long markup chains, and applied to fields where roughly 50% is lost to atmosphere or waterways.

When transport costs are honestly priced — including carbon, infrastructure, and strategic risk — the calculus inverts. Local production from local inputs becomes competitive or superior across a wide range of contexts.

This document applies the framework to that opportunity.

---

## Objects

### Resources
- **Nitrogen (N₂)**: 78% of atmosphere, free, unlimited, requires energy to fix
- **Straw / crop residue**: agricultural waste, currently burned or ploughed in
- **Methane**: produced from anaerobic digestion of organic waste
- **Hydrogen**: produced from methane (SMR) or water (electrolysis)
- **Ammonia (NH₃)**: fixed nitrogen, the target output, toxic and pressurised
- **Digestate**: nutrient-rich slurry, co-product of anaerobic digestion
- **Electricity**: input and potential output
- **Carbon credits**: tradeable value from methane capture and emissions reduction
- **Water**: input to SMR and electrolysis
- **Lime (calcium hydroxide)**: pretreatment agent, breaks lignin structure in straw
- **Iron catalyst**: standard Haber-Bosch catalyst, commodity, known since 1909
- **Nickel catalyst**: standard SMR catalyst, commodity

### Technologies
- **Anaerobic digester**: converts organic waste to methane and digestate
- **Lime pretreatment unit**: soaks straw in lime solution to break lignin, improves methane yield by 60-80%
- **Steam methane reformer (SMR)**: converts methane + water to hydrogen + CO₂
- **Pressure swing adsorption (PSA) unit**: separates nitrogen from air
- **Haber-Bosch reactor**: combines hydrogen and nitrogen under pressure and heat with iron catalyst to produce ammonia
- **Ammonia storage**: pressurised vessels for ammonia holding and distribution
- **Gas genset**: converts methane to electricity
- **Electrolyser**: alternative hydrogen source, splits water using electricity (not recommended as primary path — see dragons)

### Actors
- **Farmers**: feedstock suppliers, fertilizer consumers, capital contributors
- **Farming cooperative**: governance, capital aggregation, logistics coordination
- **Government**: food security motivation, potential emergency funder, regulatory authority
- **Carbon market**: pays for methane capture, emissions reduction
- **Grid operator**: potential buyer of surplus electricity
- **Fertilizer importers / distributors**: incumbent whose margin disappears under this model
- **Technology vendors**: SMR suppliers, Haber-Bosch unit suppliers, digester suppliers

### Institutions
- **Global fertilizer supply chain**: incumbent system, optimised for cheap transport
- **Carbon credit verification bodies**: gatekeepers to carbon revenue
- **Regulatory bodies**: safety, environmental, planning approvals

---

## Properties

### Straw
- Yield per hectare: 3-4 tonnes (confidence: high)
- Lignin content: high — resists anaerobic digestion without pretreatment (confidence: high)
- Collection cost (baling + transport): $25-45/tonne (confidence: medium — highly location dependent)
- Farmer willingness to collect year one: 20-50% of available (confidence: low — behavioural unknown, dragon)
- Seasonality: highly seasonal, requires storage consideration (confidence: high)

### Methane yield from straw
- Without pretreatment: 60-100 m³/tonne (confidence: medium)
- With lime pretreatment: 120-200 m³/tonne (confidence: medium — lab proven, field scale uncertain, dragon)
- Real world discount vs theoretical: 20-40% (confidence: medium — digesters consistently underperform theory)

### Anaerobic Digester
- Capex: f(straw_volume, site_conditions, civil_works, local_labour_cost)
  - Estimated range: $800k-2.5m (confidence: medium)
  - Skew: pessimistic — civil works highly variable
  - Dragon: civil works cost in remote locations
- Opex: f(maintenance_rate, labour_cost, lime_cost, throughput_utilisation)
  - Estimated range: $150-400k/year (confidence: low)
- Lifetime: 20+ years with maintenance (confidence: high)
- Failure modes: biological upset, gas handling failure, digestate overflow — all recoverable

### Steam Methane Reformer
- Capex: f(hydrogen_volume_required, purity_specification, local_installation_cost)
  - Estimated range: $500k-1.5m (confidence: low)
  - Dragon: hydrogen purity requirement for Haber-Bosch may require additional cleanup
- Opex: f(methane_input_cost, catalyst_replacement_frequency, labour_cost)
- Catalyst: nickel, commodity, replacement every 3-5 years
- Efficiency: 70-80% methane to hydrogen conversion (confidence: medium)

### PSA Nitrogen Separation
- Capex: $150-400k (confidence: medium-high — commodity technology)
- Opex: electricity dominated, low
- Output purity: >99.5% nitrogen (confidence: high)

### Haber-Bosch Reactor
- Capex: f(ammonia_volume_required, pressure_specification, local_installation_cost)
  - Estimated range: $500k-3m+ (confidence: very low — this is the central dragon)
  - Skew: strongly pessimistic — small scale units not yet commodity
  - Dragon: single most important unknown in the entire system
- Opex: f(energy_input, catalyst_replacement, labour, maintenance)
- Catalyst: iron, commodity, known since 1909, replacement every 5-10 years
- Energy requirement: ~10 MWh per tonne ammonia (confidence: high — well established)
- Operating conditions: 150-300 bar, 400-500°C (confidence: high)
- Small scale viability: physically proven, commercially uncertain (dragon)

### Nitrogen Fertilizer
- Current global commodity price: $300-400/tonne nitrogen (confidence: high)
- Farm gate price after last mile (remote): $800-1,500/tonne nitrogen (confidence: medium)
- Emergency price (supply disruption): $2,000-4,000+/tonne (confidence: low — scenario dependent)
- Application efficiency: ~50% — half is lost to atmosphere or waterways (confidence: medium)

### Electrolyser (alternative hydrogen path)
- Capex: falling rapidly but not yet commodity at relevant scale (confidence: medium)
- Stack lifetime: 60,000-100,000 hours claimed, real world uncertain (dragon)
- Vendor concentration: high — not yet open market (dragon)
- Dependency: requires reliable cheap electricity — problematic in remote locations
- Recommendation: not primary path, monitor for future integration

### Carbon Credits
- Value: f(carbon_price, methane_volume_captured, verification_cost, political_stability)
- Current price range: $20-50/tonne CO₂e (confidence: medium)
- Dragon: politically volatile, cannot be relied upon as primary revenue stream
- Methane warming equivalence: 25x CO₂ — captured methane generates significant credits

---

## Relationships

### Physical Flows
- Straw → [collection, transport] → Lime pretreatment unit
  - Rate: f(farmer_uptake, collection_cost, seasonality)
  - Cost: $25-45/tonne (confidence: medium)
  - Dragon: uptake rate year one

- Lime pretreatment unit → [treated straw] → Digester
  - Lime dosing: ~5-10% of straw weight
  - Yield improvement: 60-80% more methane (confidence: medium, lab proven)

- Digester → [methane, digestate]
  - Methane yield: 120-200 m³/tonne treated straw (confidence: medium)
  - Digestate: high nutrient content, returned to farms

- Methane → [6-12% of total] → SMR → Hydrogen
  - Conversion: 2.5 kg hydrogen per kg methane
  - Remainder: electricity generation

- Methane → [88-94% of total] → Genset → Electricity

- Hydrogen + Nitrogen (from PSA) → Haber-Bosch → Ammonia
  - Ratio: 3:1 hydrogen to nitrogen by mass
  - Energy: ~10 MWh/tonne ammonia

- Ammonia → [storage, distribution] → Farms
  - Distribution cost: f(distance, diesel_price, infrastructure)

- Digestate → [processing, transport] → Farms
  - Value: replaces lime and micronutrient purchases
  - Estimated value: $80-150/tonne (confidence: low)

### Economic Flows
- Fertilizer saving → Cooperative → Farmers
  - Value: f(ammonia_volume, current_fertilizer_price, distribution_cost)

- Electricity → Grid → Revenue
  - Value: f(electricity_price, grid_access, surplus_volume)
  - Dragon: grid access in remote locations may be unavailable or prohibitively expensive

- Methane capture → Carbon market → Revenue
  - Value: f(carbon_price, methane_volume, verification_cost)
  - Dragon: politically volatile

- Straw delivery → Farmers → Fertilizer credit
  - Farmers paid in fertilizer credit not cash
  - Net cash cost to system: near zero if credit value ≥ collection cost

### Actor Relationships
- Farmer trust → Cooperative → Straw uptake rate
  - Trust builds over time, non-linear
  - Early adopters reduce risk perception for later adopters
  - Dragon: initial trust level unknown

- Cooperative → Capital → System build
  - Governance already exists in many contexts
  - Capital appetite unknown without specific engagement (dragon)

- Government → Emergency funding → Capital availability
  - Activated by emergency state
  - Can compress payback period to near zero

- Open source installations → Model improvement → Reduced uncertainty
  - Each installation resolves dragons
  - Loot shared with all subsequent actors

---

## Calculations

All calculations take distributions as inputs and produce distributions as outputs. Point estimates below are central estimates only.

### Methane Available
```
methane_available = farm_hectares × straw_yield_per_ha × farmer_uptake_rate 
                    × lime_pretreatment_yield_improvement × digester_efficiency
                    × methane_content_of_biogas
```
Confidence: medium. Skew: pessimistic — multiple uncertain terms multiply.

### Hydrogen Required for Full Fertilizer Replacement
```
hydrogen_required = nitrogen_demand_tonnes × 220 kg_H2_per_tonne_N
```
Confidence: high — well established chemistry.

### Methane Required for Hydrogen (via SMR)
```
methane_for_SMR = hydrogen_required / (2.5 × SMR_efficiency)
```
Confidence: medium.

### Surplus Methane for Electricity
```
surplus_methane = methane_available - methane_for_SMR
electricity_generated = surplus_methane × energy_content × genset_efficiency
```
Confidence: medium — depends on methane_available calculation.

### System Capex
```
system_capex = digester_capex(straw_volume, site) 
             + pretreatment_capex(straw_volume)
             + SMR_capex(hydrogen_volume)
             + PSA_capex(nitrogen_volume)
             + haber_bosch_capex(ammonia_volume)    ← central dragon
             + storage_capex(ammonia_volume)
             + genset_capex(surplus_methane)
             + grid_connection_capex                 ← location dragon
             + civil_and_installation(site_conditions, remoteness)
```
Confidence: low overall — Haber-Bosch and grid connection dominate uncertainty.

### System Opex
```
system_opex = lime_cost(straw_volume, lime_price)
            + labour_cost(automation_level, local_labour_rate)
            + maintenance_cost(capex, maintenance_rate)
            + catalyst_replacement(volume, replacement_frequency)
            + electricity_cost(self_powered_fraction)
```
Confidence: low — labour cost in remote locations particularly uncertain.

### Annual Value Generated
```
annual_value = fertilizer_saving(ammonia_produced, fertilizer_price)
             + electricity_revenue(surplus_electricity, grid_price, grid_access)
             + carbon_credits(methane_captured, carbon_price)
             + digestate_value(digestate_volume, nutrient_content)
             - system_opex
```
Confidence: low-medium. Skew: optimistic risk — electricity revenue and carbon credits are dragons.

### Payback Period
```
payback = system_capex / annual_value
```
Output is a distribution, not a point estimate. Range: 1-15 years depending on scenario state.

---

## Pathways

### Path A: Digestate Only
**Description**: Optimise capture and application of nitrogen already in waste stream. No synthesis.

**Objects**: Straw → Digester → Digestate → Farms (+ Methane → Genset → Electricity)

**Properties**:
- Nitrogen replacement: 20-30% of synthetic fertilizer need (confidence: medium)
- Capex: $800k-1.5m (confidence: medium-high)
- Build time: 6-12 months
- Dragon count: low

**Viability**: High across all scenarios. Viable today.

**Option value**: High — infrastructure built here is reused by Paths C and D. Does not foreclose any future path.

**Forced moves after choosing**: Straw collection logistics must be solved. Digestate application system required.

---

### Path B: Digestate + Bulk Ammonia Hub
**Description**: Local system handles organic nitrogen. Remaining synthetic fertilizer purchased in bulk to town, not per farm.

**Objects**: Path A + Bulk ammonia storage + Cooperative purchasing

**Properties**:
- Cost reduction vs current: 20-40% on purchased fertilizer (transport markup eliminated)
- Additional capex: $200-400k for bulk storage (confidence: medium)
- Dragon count: very low

**Viability**: High across all scenarios. Viable today. No novel technology.

**Option value**: High — preserves all future options, adds bulk storage infrastructure Path C needs.

---

### Path C: Full Synthesis — SMR + Haber-Bosch
**Description**: Full nitrogen independence from local feedstock via methane → hydrogen → ammonia pathway.

**Objects**: Path A + Lime pretreatment + SMR + PSA + Haber-Bosch + Ammonia storage

**Properties**:
- Nitrogen replacement: up to 100% (confidence: medium — depends on straw volume)
- Capex: $4-12m (confidence: low — Haber-Bosch is central dragon)
- Opex: $1.5-4m/year (confidence: low)
- Dragon count: high — SMR purity, Haber-Bosch capex, labour, grid connection
- All-commodity components: yes — iron catalyst, nickel catalyst, standard pressure vessels

**Viability**:
- Normal market: marginal to viable depending on Haber-Bosch capex resolution
- High fuel price: viable
- Emergency: strongly compelling

**Option value**: Medium — forecloses electrolyser path if SMR infrastructure dominates site

**Forced moves after choosing**: Methane purity specification forces SMR design. SMR forces hydrogen cleanup specification. Haber-Bosch forces ammonia storage safety compliance.

**Key dragon**: Small scale Haber-Bosch unit cost. Everything else can be estimated with reasonable confidence. This cannot. First dragon to slay.

---

### Path D: Electrolyser + Haber-Bosch
**Description**: Green hydrogen via electrolysis rather than SMR.

**Objects**: Path A (electricity only) + Electrolyser + PSA + Haber-Bosch + Ammonia storage

**Properties**:
- Capex: higher than Path C currently (confidence: medium)
- Opex: electricity price dominated
- Dragon count: very high — electrolyser stack lifetime, electricity price, vendor concentration
- Carbon accounting: cleaner than Path C

**Viability**:
- Normal market: not viable currently
- If electricity price falls and electrolyser commoditises: viable in 3-5 years
- Emergency: unlikely — electrolyser supply chains are concentrated and fragile

**Recommendation**: Monitor. Design Path C to accept electrolyser as future substitution for SMR when economics improve. Do not depend on it.

---

### Path E: Open Source Design Package
**Description**: Not a physical pathway. A meta-pathway that improves all others.

**Objects**: All of the above + Knowledge commons + Peer review network + Installation data feedback

**Properties**:
- Reduces Haber-Bosch capex uncertainty as installations accumulate
- Eliminates dragons progressively
- Changes actor relationships — cooperative becomes knowledge node
- Accelerates adoption across all contexts

**Viability**: Always viable. Zero marginal cost to share knowledge.

**Relationship to other paths**: Does not compete with Paths A-D. Amplifies all of them. Each installation is a team walking territory and returning loot.

---

## Constraints

*(Ambient, conditional, cross-cutting — not owned by any object)*

**Hard constraints** (physical, invariant):
- Nitrogen fixation requires energy input regardless of process — thermodynamic floor
- Haber-Bosch requires elevated temperature and pressure — cannot be designed away
- Straw is seasonal — storage or process scheduling required
- Geography — distance between farms and facility is fixed

**Soft constraints** (regulatory, financial, behavioural — may dissolve):
- Ammonia storage safety regulations — significant compliance cost, location dependent
- Grid connection approval — Western Power or equivalent may refuse or price prohibitively
- ACCU verification requirements — administrative burden, lag between action and credit
- Cooperative governance rules — capital decisions require member agreement
- Planning approval for industrial facility in agricultural zone

**Conditional constraints** (activated or dissolved by state change):
- Emergency state dissolves: planning approval timelines, capital availability constraints, regulatory timelines
- Emergency state activates: government funding, strategic priority status, fast-track approval
- Farmer trust below threshold: straw uptake too low to sustain system — minimum viable cooperative size required
- Carbon price below threshold: carbon revenue insufficient to contribute meaningfully to payback

**Unknown constraints** (dragons — may exist, not yet discovered):
- Western Power grid capacity at specific Wheatbelt locations
- Australian safety compliance cost for ammonia at this scale
- CBH governance rules around novel capital investments
- Water availability and quality requirements for SMR at specific sites

---

## Phase Space

### Current Position
Centralised fertilizer system dominant. Transport cost subsidy intact but eroding. Emergency risk real and growing. Local production technically viable but not yet demonstrated at relevant scale.

### Symmetry Points (genuine open choices right now)
1. **Technology choice**: SMR vs electrolyser for hydrogen. Genuine choice — path dependent, not reversible cheaply once infrastructure built
2. **Scale**: Individual farm vs cooperative vs town. Cooperative is almost certainly right but not yet proven in this context
3. **Ownership model**: Farmer-owned cooperative vs external operator vs open source commons
4. **First market**: Which context has the right combination of need, ability to pay, and cooperative structure to be first?

### Breaking Points (where system snaps)
1. **Haber-Bosch capex resolution**: If a vendor quotes $500k-1m installed at relevant scale, Path C becomes compelling in normal market. If quote is $3m+, Path C is emergency-only.
2. **First cooperative commits**: Changes actor behaviour in neighbouring cooperatives — demonstration effect
3. **Emergency trigger**: Fertilizer price spike changes all calculations simultaneously, activates government funding
4. **Open source first release**: Changes the nature of the problem from commercial to collaborative

### Forced Moves
- Choose SMR → forced to solve hydrogen purity for Haber-Bosch
- Choose cooperative ownership → forced to engage CBH governance process
- Build Path A infrastructure → forced to solve digestate application logistics (but this is a good forcing)
- Choose Path C before Path A → forced to solve farmer trust and straw logistics simultaneously with synthesis — high risk

### Dragons (priority order)
1. **Haber-Bosch unit cost at relevant scale**: Central dragon. Slay first. Get vendor quotes.
2. **Real world methane yield from lime-pretreated straw at field scale**: Lab proven, field uncertain
3. **Grid connection cost and feasibility at specific locations**: May eliminate electricity revenue entirely
4. **Farmer straw uptake rate year one**: Behavioural, unknown without pilot
5. **CBH cooperative capital appetite**: Institutional, unknown without direct engagement
6. **Australian ammonia safety compliance cost**: Regulatory, location specific
7. **SMR hydrogen purity output vs Haber-Bosch requirement**: Technical, resolvable with engineering study
8. **Electrolyser stack lifetime at continuous operation in remote conditions**: Monitor, not urgent
