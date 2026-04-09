# A Framework for Modelling Complex Distributed Systems Under Uncertainty

## Core Idea

At any moment a system exists at a point in a phase space. From that point there are genuine degrees of freedom — choices that are open. Once a choice is made, symmetry breaks. The space collapses around that decision. Some options open, others close permanently.

The framework is a tool for navigating that space — identifying where you are, what choices are real, where the breaking points are, and what becomes forced after each decision.

---

## The Framework Elements

### 1. Objects

Physical things, technologies, resources, and institutions that exist in the system. Not abstract — things you can point to.

Examples: a digester, a farmer, a tonne of straw, a cooperative, a government agency.

### 2. Properties

Measurable attributes of objects. Critically, properties are not single values — they are distributions with:

- A range (min, max)
- A central estimate
- A confidence level (high / medium / low / unknown)
- A skew (pessimistic or optimistic bias and why)
- A flag if the uncertainty is deep enough to constitute a dragon

Properties can be static or dynamic. Dynamic properties change as the system evolves.

### 3. Relationships

Connections between objects. Each relationship has:

- Direction (one-way or bidirectional)
- A flow (what moves along it — material, energy, money, information, trust)
- A rate (how much, how fast) — itself a distribution with uncertainty
- Dependencies (what conditions must hold for the relationship to be active)
- Substitutions (alternative relationships that can replace it if it fails)

### 4. Calculations

Functions that derive values from properties and relationships. Critically:

- Capex, opex, yield, payback — these are outputs of calculations, not inputs
- Every calculation takes distributions as inputs and produces distributions as outputs
- Calculations propagate uncertainty — a change anywhere propagates through the entire system
- Calculations can be simple (linear) or complex (non-linear, feedback-dependent)

Example:
```
digester_capex = f(straw_volume, lignin_content, pretreatment_method, 
                   site_conditions, local_labour_cost, civil_works_complexity)
```

Not a number. A function of other things, each of which is itself a function.

### 5. Pathways

Sequences of objects and relationships from inputs to outputs. Each pathway has:

- A viability distribution — probability of being viable under current conditions
- A capex and opex profile (derived from calculations, not assumed)
- A robustness score — does it survive across multiple states and constraint sets
- A dragon count — how many high-uncertainty flags does it carry
- Single points of failure — where one broken link kills the whole path
- Substitution options — alternative nodes or edges that preserve the path if one fails
- An option value — what future pathways does choosing this one enable or foreclose

Pathways are generative — given the objects, properties, relationships, calculations, and constraints, the model produces the set of viable pathways rather than having them specified in advance.

### 6. Constraints

Ambient rules that govern the space. Constraints are a distinct ontological category:

- They have no physical existence — they are not objects
- They do not belong to a specific object — they are not properties
- They do not connect two specific things — they are not relationships
- They cross-cut the entire model simultaneously
- They may or may not be active at a given moment
- They may be conditional — activated by specific states or events
- They range from hard (thermodynamic, physical) to soft (regulatory, behavioural, financial)
- They can appear and disappear — emergency conditions dissolve some constraints, create others
- They are partially discoverable — some constraints are unknown until you hit them

Constraints are what prune the pathway space. Without them, everything looks possible.

### 7. Actors

Entities with agency — they make decisions, not just have properties. Actors:

- Have goals that may conflict with each other and with system optimality
- Have incomplete information about the system they operate in
- Change behaviour based on what other actors do
- Can activate or block pathways
- Can create or dissolve constraints
- Learn and adapt — their properties change endogenously
- Have decision rules (which may be simple or complex)
- Have trust relationships with other actors that evolve over time

Actors are what make the system social rather than purely physical. They are often the most important and least tractable part of the model.

---

## Phase Space Structure

The framework represents the system as existing in a phase space with three types of critical points:

### Symmetry Points
Moments where multiple pathways are genuinely equivalent and the choice is real and open. These are where decisions have the highest leverage. Before a technology is chosen. Before a cooperative is formed. Before a commitment is made.

### Breaking Points
Where a small input causes a large, often irreversible change in the system's trajectory. These are not smooth transitions — the system snaps into a new configuration. An emergency price spike. A first successful installation. A cooperative saying yes or no.

Breaking points are the most important things to find in advance. A breaking point hit unexpectedly is a crisis. A breaking point identified in advance is a decision opportunity.

### Forced Moves
Once a breaking point is passed, what follows is not really a choice. Path dependence is real. You cannot un-build infrastructure. You cannot un-sign a contract. The model must track which decisions foreclose which future options.

---

## Dragons

Dragons are uncertainties significant enough to hide breaking points or invalidate entire pathways. They are not just wide error bars — they are cases where:

- The uncertainty is deep enough that the model's output in that region is unreliable
- A wrong assumption could lead to a decision that forecloses better options
- The unknown could represent a hard constraint not yet discovered

Dragons require active resolution — not better estimation, but going out and finding the answer.

### Dragon Taxonomy

- **Value dragons**: a property whose range is too wide to be useful
- **Structural dragons**: a relationship that may or may not exist
- **Constraint dragons**: a rule that may apply but is not yet known
- **Actor dragons**: a decision-maker whose behaviour is unknown
- **Cascade dragons**: an uncertainty that propagates through multiple calculations

---

## The Mapping Process

The framework is not a static model. It is a living map that improves through active exploration:

1. Model identifies highest-uncertainty regions and their dragons
2. Teams are dispatched to resolve specific dragons
3. Real data returns — error bars collapse, new structure becomes visible
4. Model updates — new symmetry points and breaking points become visible
5. New dragons emerge that were hidden behind resolved ones
6. Process repeats

The value of dragon-slaying is not just the data. It is:
- Resolved uncertainty that improves the model for everyone
- Demonstrated feasibility that changes actor behaviour
- New constraints discovered that were previously invisible
- New objects and relationships nobody knew existed

### Open Source Principle

The map is a shared asset. Every installation, every team, every resolved dragon improves the map for all subsequent actors. This is not just an ethical preference — it is the fastest way to collapse uncertainty across the whole system.

The loot from dragon-slaying belongs to everyone.

---

## Modelling Methodology Notes

Time is methodology, not a framework element. Different aspects of the system suit different approaches:

- **Stochastic / Monte Carlo**: uncertainty propagation through calculations
- **System dynamics**: feedback loops, stocks and flows over time
- **Agent-based**: emergent behaviour from actor decision rules
- **Path dependence / decision trees**: option value, irreversibility, sequencing

These are not alternatives — they are layers applied to the same underlying framework. The choice of which to apply where depends on which dynamics are dominant in a given region of the phase space.

---

## What the Framework Produces

For any given state of the system:

- The set of viable pathways with probability distributions over outcomes
- Identification of genuine symmetry points — where decisions are real
- Location of breaking points — where the system will snap
- Prioritised dragon list — which uncertainties most need resolving
- Forced move map — what becomes inevitable after each choice
- Option value assessment — which early choices preserve the most future flexibility
- Data collection priorities — what real-world information would most improve the model
