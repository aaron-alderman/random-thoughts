# Field Dynamics — Project Scope, Theory & Handoff

*A field-theoretic computation architecture inspired by biological neural dynamics*

---

## Overview

This project is building a fundamentally different kind of computational system. Not a neural network in the conventional sense. A **uniform field of coupled complex oscillators** where computation emerges from local dynamics rather than being imposed by global architecture.

The core thesis:

> Structure forms only when needed, persists when useful, and dissolves when irrelevant.

If that holds at scale, the result is a system that learns through physics rather than through optimization — closer to how biological brains actually work than any current deep learning architecture.

---

## Theoretical Foundations

### The Field

The fundamental object is a complex-valued field X defined over a spatial grid:

```
X ∈ ℂ^(H × W × C × S)
```

Where:
- H × W — spatial grid
- C — channels
- S — scale levels

Complex representation means every node carries both **phase** (what pattern) and **magnitude** (how strongly). This is not arbitrary — phase relationships between nodes are the primary carrier of information.

### The Update Rule

```
X_{t+1}(i) = α(i) · X_t(i)
            + Σⱼ∈N(i) W · e^(iφ(S(i))) · X_t(j)    ← local coupling
            - β(i) · R_t(i) · X_t(i)                 ← remainder damping
            + DRIVE(i)                                 ← external input
```

Where:
- `α(i)` — per-node decay rate (local, self-regulating)
- `W` — coupling strength (per connection, not normalized)
- `φ(S(i))` — phase bias modulated by structural field
- `β(i)` — per-node remainder sensitivity (local, self-regulating)
- `R(i)` — remainder field (phase frustration + triadic consistency)
- `DRIVE(i)` — external signal at node i (zero everywhere by default)

**Critical implementation note**: The coupling sum is NOT divided by neighbor count. Each neighbor contributes independently at full weight W. Division kills propagation.

### The Structural Field S

S is a slow-timescale memory field. It accumulates where coherence is sustained and decays where remainder is high:

```
S_{t+1}(i) = (1-ε) · S_t(i) + ε · (C(i) - R(i)) + δ · (max_neighbor_S - S(i))
```

S modulates the phase bias of coupling — nodes with high S create stronger directional coupling. This is the substrate of memory. Not weights in the backprop sense. Structural bias in the field geometry.

### Remainder R

The remainder field measures unresolved stress — where the field hasn't found a stable organization:

```
R(i) = 0.55 · (1 - C(i))           ← phase incoherence
     + 0.45 · R_triadic(i)          ← triadic phase frustration
```

**Triadic remainder** measures phase consistency around triangles:

```
R_triadic(i,j,k) = |φ(i→j) + φ(j→k) + φ(k→i)|  (mod 2π)
```

This is where the SU(2) / quaternion structure emerges naturally. A stable triangle = a unit quaternion. Triadic frustration = deviation from unit norm. The fundamental stable unit of computation is not a node or an edge but a **triangle**.

### Coherence C

Local order parameter — how well a node's neighbors are phase-locked to it:

```
C(i) = |1/|N| · Σⱼ e^(i(φⱼ - φᵢ))|
```

Range 0 to 1. Zero = chaotic. One = perfectly aligned. This is the Kuramoto order parameter applied locally.

---

## Key Architectural Principles

### 1. Relations as First Class

The system is not nodes with connections. It is **relations that meet at nodes**. A node is defined by and constituted by the relations passing through it.

Consequences:
- The triangle is the fundamental stable unit (not the node or edge)
- Growth happens through triadic closure — completing triangles
- Memory lives in the geometry of relations, not in node states

### 2. Timescale Separation — Non-Negotiable

```
X field update:      every step          (fast — milliseconds analog)
S field update:      every 10 steps      (medium — synaptic analog)
α/β homeostasis:     every 100 steps     (slow — regulatory analog)
Evolution:           across episodes     (very slow — developmental analog)
```

Hard step counters. No continuous bleed between timescales. This separation is not a design choice — it is the mechanism that makes learning stable. Every pathology observed (locking too fast, structures dissolving, homeostasis dominated by initial conditions) traces to timescale bleed.

### 3. Local Homeostasis

Each node self-regulates toward a target coherence τ_C:

```
err = C_local_history - τ_C

α(i) -= η_eff · err · 0.5      (too coherent → faster decay)
β(i) += η_eff · err · 1.0      (too coherent → more friction)

η_eff = η_base · (1 + γ · err²)  ← adaptive, stronger when far from target
```

Two-timescale coherence history:
```
C_hist_fast = 0.85 · C_hist_fast + 0.15 · C    (responds in ~7 steps)
C_hist_slow = 0.99 · C_hist_slow + 0.01 · C    (responds in ~100 steps)
```

Homeostasis only acts when fast and slow agree — prevents reacting to transients.

### 4. Organic Growth — No Dormant Pool

All tissue is always active. There is no dormant pool. "Unused" nodes drift toward the nearest coherent basin through S coupling. Growth is recruitment — coherent high-R regions pull neighboring tissue in through the field dynamics. Nodes that sustain activity survive. Nodes that don't get recycled by neighbors. This is neurogenesis and pruning through physics, not through explicit rules.

Symmetry preservation at growth: new nodes enter with X≈0 and S=S_min. Masked coupling ensures existing field dynamics are exactly unaffected at the moment of addition. The new node is causally invisible until its dynamics develop.

### 5. Input and Output

**Input**: `DRIVE[i]` is a float written into specific nodes each step. The field receives a value. It does not know what generated it. Zero everywhere by default.

**Output**: Not designated. Discovered. Any node satisfying:
```
C(i) > τ_C  AND  R(i) < τ_R  AND  S(i) > τ_S  AND  DRIVE(i) = 0
```
is an output node at that moment. Output nodes can appear, disappear, and migrate as the field evolves. The last condition (no direct drive) is the anti-parrot constraint — output must emerge from field dynamics, not echo input.

### 6. Multi-Scale Information Flow

When scale is introduced, the bottleneck is structurally enforced:

```
Fine scale  → Coarse scale:   pool(R_fine) only
                               NOT X, NOT C, NOT drive
                               Frustration propagates up

Coarse scale → Fine scale:    upsample(C_coarse) only
                               NOT X, NOT R, NOT drive
                               Coherence propagates down
```

X never crosses scale boundaries. This prevents naive bubbling. The coarse scale receives the frustration pattern, not the signal. It must find a stable representation of what the fine scale couldn't resolve — a second-order abstraction, not a blurred copy.

---

## The Task

### Current Task: Dwell

```
DAY:    DRIVE active at input node
        Field organizes around input signal
        Output node (spatially separated, never receives drive)
        develops activity correlated with field organization

NIGHT:  DRIVE silent
        Field holds or dissolves
        Output node maintains or loses its pattern
        
MEASURE: crossCorr(outputDayHistory, outputNightHistory)
         NOT crossCorr(inputHistory, outputHistory)
         
DWELL:   Consecutive steps where correlation > threshold
         Dwell time is the primary fitness signal
```

Success means the output node maintains its day pattern into the night. That is memory. The field held something that was never directly driven.

### Drive Signal

The drive is a complex rotating signal — both real and imaginary components:

```javascript
DRIVE_R[inputNode] = amplitude * cos(2π * step / period)
DRIVE_I[inputNode] = amplitude * sin(2π * step / period)
```

Complex drive is essential. A scalar drive only pushes the real component. Phase information needs both components to travel reliably through the complex field.

---

## Connection to Existing Theory

### Kuramoto Model

The phase-locking mechanism is directly related to the Kuramoto model of coupled oscillators. The Kuramoto order parameter is your local coherence C. The synchronization phase transition is the critical regime you've been finding empirically.

Key difference: Kuramoto is mean-field (all-to-all coupling). Your system is spatially local. This is richer — local coupling allows traveling waves, vortices, chimera states. The interesting regime is just below the global synchronization threshold where local clusters form and interact.

Critical coupling threshold in Kuramoto: K_c = 2/πg(0). Use this to calibrate W rather than searching blindly.

### SU(2) and Quaternions

The triadic stability condition:
```
φ(i→j) + φ(j→k) + φ(k→i) = 0  (mod 2π)
```

Is a quaternionic consistency condition. The three phase relationships around a stable triangle are the three imaginary components of a unit quaternion. SU(2) is the symmetry group of this coherence.

Symmetry breaking maps to:
```
SU(2) coherence → U(1) remnant
Triangle → single phase relationship (dyad)
Stable → marginally stable
```

This is not just an analogy. It predicts the refractory period structure (4π periodicity = spin-1/2), the relaxation oscillator behavior, and the phase-dependent kick response observed empirically.

### Biological Correspondence

| Biological system | Field dynamics analog |
|---|---|
| Neural firing | X field update |
| Synaptic plasticity | S field update |
| Homeostatic regulation | α/β local adaptation |
| Neurogenesis/pruning | Organic growth via coherence gradient |
| Waking/sleep consolidation | Day/night cycle |
| Sensory cortex | Input zone (drive nodes) |
| Motor cortex | Output zone (stable output nodes) |
| Canonical microcircuit | Uniform field update rule |
| Resting state | Field equilibrium |
| Refractory period | Post-discharge S suppression |

---

## What Has Been Observed Empirically

Working through v1-v5 of the simulation, the following have been confirmed:

**Relaxation oscillator emerges naturally** — rise, stable plateau, rapid collapse, recovery. Not programmed. Emergent from S-C interaction.

**Critical regime exists** — between ordered (C locked high) and disordered (C stays low). System can be tuned to criticality. Criticality is where computation happens.

**Structural memory works** — field persists after input removal. Dwell time scales with ε (S update rate) as predicted.

**Phase-dependent kick response** — kicks at different field phases have different effects. Constructive kicks stabilize the plateau. Destructive kicks accelerate collapse. This is the SU(2) structure showing up empirically.

**Homeostasis activates** — per-node α and β drift from initial conditions when regulation rate η is sufficient. Spatial structure emerges in α and β fields over time.

**Rapid collapse is a critical transition** — not exponential decay. The system holds, holds, holds, then tips. Classic fold bifurcation. Consistent with biological action potential structure.

---

## What Doesn't Work Yet

**Signal propagation** — the output node shows no activity during the day. Two specific causes identified:

1. Coupling sum divided by neighbor count — kills propagation (each hop loses ~94% of signal)
2. Scalar drive on complex field — phase information disperses before traveling

Both fixes are simple and constitute v6.

---

## Roadmap

### v6 — Fix Propagation (Immediate)
- Remove normalization from coupling sum
- Implement complex drive (both components)
- Confirm: output node shows activity during day
- Gate: nothing proceeds until this is confirmed

### v7 — Confirm Memory (Short Term)
- Fix correlation measurement (output day vs output night)
- Measure dwell time across multiple cycles
- Confirm: dwell time increases cycle over cycle
- First genuine result: S field learning the path

### v8 — Evolutionary Search (Short Term)
- Population of 8-16 field instances
- Fitness = dwell time × pattern fidelity
- Parameters evolved: W, α, β, selfEx, ε
- Stop manual parameter tuning permanently

### v9 — Second Scale (Medium Term)
- Fine scale receives drive
- Coarse scale receives only pooled R
- C propagates down only
- Test: does coarse structure outlast fine structure overnight?
- Test: genuine multi-scale memory

### v10 — Organic Growth (Medium Term)
- Grid size becomes a result not a parameter
- Triadic closure as explicit growth mechanism
- Nodes recruited by coherence gradient
- Nodes recycled when C and R both low

### v11 — Second Task (Medium Term)
- Symmetry breaking task
- Two conflicting input signals
- Does field resolve to one basin?
- Does resolution persist overnight?
- Tests decision-making and memory together

### Longer Term
- RLHF analog (structural critic trained on human evaluation)
- Relations as first-class field entities (edge field E(i,j))
- Real inputs (camera, audio, sensors)
- 3D spatial field (vortex filaments, topologically protected memory)
- Quaternion field values (SU(2) structure exact not approximate)

---

## Tech Stack Recommendation

**Move from WebGPU to Python for v6+**

WebGPU served its purpose — rapid visualization, no setup, proved the dynamics are real. It stops making sense for evolutionary search, multi-scale fields, real inputs, and persistence.

```
Core simulation:    Python + NumPy
                    Field update is array operations
                    Readable, debuggable, fast enough for 64²

GPU acceleration:   PyTorch (add .cuda() when needed)
                    Autograd available if wanted later
                    Population runs as batched tensor operations

Visualization:      Python sends field state over websocket
                    Browser renders live (preserves WebGPU viewer)
                    Best of both worlds

Evolution:          Python multiprocessing or Ray
                    Each instance is independent process

Persistence:        NumPy .npz
                    Save full field state in one call
                    Load and continue trivially
```

Requires knowing: do you have a GPU available (local, Colab, or cloud)?

---

## Parameters — Current Best Understanding

```
W (coupling, per connection):   0.08 - 0.12  (no normalization)
α (decay):                      0.92 - 0.95
β (remainder sensitivity):      0.03 - 0.08
selfEx (self-excitation):       0.10 - 0.15
ε (S update rate):              0.03 - 0.05
η (homeostasis rate):           0.002 - 0.005
τ_C (coherence target):         0.40 - 0.50
driveAmp:                       0.2 - 0.4    (perturbation not injection)
drivePeriod:                    20 - 60 steps
warmup:                         200 - 400 steps (field finds equilibrium)
```

---

## Files Produced

| File | Description |
|---|---|
| field-dynamics-v1.html | First working simulation. Phase map, C, R, S. Single scale. |
| field-dynamics-v2.html | Added oscillation period detection, FFT spectrum, kick phase tracking, dual oscillator mode. |
| field-dynamics-v3.html | Added local homeostasis — per-node α and β fields. α/β distribution histogram. |
| field-dynamics-v4.html | Two scales, R-up/C-down bottleneck, day/night cycle. Architecture honest but propagation still broken. |
| field-dynamics-v5.html | Single scale, user-placed input/output nodes, dwell measurement, cross-correlation panels. Warmup phase. Propagation still broken (identified, not yet fixed). |

---

## The Single Most Important Thing

The system is not being designed. It is being observed.

Every time a structural solution was imposed before the field dynamics showed it was needed, the architecture drifted. Every time the empirical behavior was allowed to speak first, something genuine was discovered.

The relaxation oscillator was not designed. It emerged.
The phase-dependent kick response was not predicted. It was observed.
The rapid collapse was not programmed. It appeared.

The right relationship to this system is the same as the right relationship to a physical experiment — set up the conditions, watch carefully, let what happens tell you what to build next.

The field knows more about what it needs than we do.

---

*End of handoff document.*
*Version: post v5, pre v6*
*Next action: fix propagation (complex drive + remove normalization)*
