# Field Dynamics v7 Phase-Persist Debugging Guide

## Overview
This tool simulates a complex-valued field on a 2D toroidal grid. The input node is externally driven during day, the field learns a directional memory trace while that drive propagates, and the output node is inspected during night to see whether the learned structure can retain or replay the driven pattern.

The core thing to keep in mind is that this simulation is not only about amplitude. Each node is a rotating complex vector `(Xr, Xi)`, so a node can look "alive" by magnitude while its actual rotational frequency changes a lot.

## What the Tool Is Doing
### 1. Field State
- `Xr`, `Xi`: the complex state of each node.
- `S`: slower structural state updated every 10 steps.
- `R`, `C`: remainder and coherence measures derived from local neighborhood phase relationships.
- `AL`, `BL`: local damping terms updated by homeostasis every 100 steps.

### 2. Day / Night Cycle
- Warmup: no external drive, just settle the field.
- Day: input node receives the rotating external drive.
- Night: drive is truly off and the field relies on learned edge memory plus learned phase velocity.

`cycleMode` and `cycleStepInPhase` are the main counters to inspect when behavior feels surprising.

### 3. Complex Drive
- The external drive only touches the input node.
- The drive phase is continuous across day and night.
- The amplitude envelope is day-gated by `driveEnv`, so the field is not hit with a hard amplitude step at day start.

### 4. Fast Field Update (`X`)
Every step, each node:
- Collects neighbor coupling through `W`.
- Applies direct phase alignment through `kAlign`.
- Uses learned directional memory `Sedge` to strengthen remembered routes.
- Applies damping and self-excitation.
- During day, clamps the input node close to the external drive so the source frequency is explicit.

### 5. Structural Update (`S`)
Every 10 steps, `S` is updated from local coherence and remainder. This is the slower field backdrop that shapes where propagation is easier or harder.

### 6. Edge Memory (`Sedge`)
Also every 10 steps, the simulation reinforces edges that:
- carry real amplitude,
- are locally coherent,
- are aligned with the daytime driven signal.

This produces a directional path memory rather than a generic global persistence effect.

### 7. Learned Phase Velocity (`Omega`)
Every step, the simulation estimates local phase advance:
- `PhaseDelta[i]` stores the observed per-step phase change,
- `DriveLock[i]` stores how aligned the node currently is with the drive phase,
- `Omega[i]` learns a smoothed local angular velocity during day and decays slowly at night.

This is the main "overnight phase storage" mechanism in the current version.

### 8. Night Replay
At night, the simulation does not simply keep amplitude. It computes a replay advance:

`adv = phaseInertia * retain * memAvg * Omega[i]`

Where:
- `Omega[i]` is the learned local angular velocity,
- `memAvg` is how much learned memory is available around that node,
- `retain` is the night retention factor,
- `phaseInertia` scales how strongly learned angular motion is reapplied.

This explains the high-amplitude / low-frequency behavior:
- amplitude can remain visible because damping is relieved by memory and retained edges,
- but replay speed can become much slower than the daytime drive because `adv` is multiplied by memory strength.

If `memAvg` is small, the effective replay period becomes much longer even when the node still has substantial magnitude.

### 9. Signal History and Correlation
- `inputHistory`: external day-only drive trace.
- `probeHistory`: first hop from input toward output.
- `outputHistory`: raw output `Xr`.
- `outputLockHistory`: output projected onto the drive phase.
- `outputDayHistory` / `outputNightHistory`: used for night memory scoring.

Night dwell is scored with:
- `corrValue`: current day-vs-night correlation,
- `peakCorr`: best correlation seen in the current night,
- `dwellSteps`: current run above the threshold,
- `bestDwell`: best dwell run so far.

## What the UI Now Shows
### Main plots
- External drive R: the actual injected day drive.
- 1-hop probe R: whether the drive leaves the input node.
- Output raw R: the raw output signal used for visible frequency checks.
- Drive-locked output: output projected onto the current drive phase, useful for entrainment diagnostics.

### Top metrics
- Expected drive period.
- Probe estimated period.
- Output estimated period.
- Path memory mean.
- Night/day RMS gain.
- Completed cycles.

### Debug panel
The new debug panel surfaces the live internals most useful for explaining anomalies:
- cycle mode and cycle step,
- `driveEnv`, drive phase, and drive omega,
- `corrValue`, `peakCorr`, `dwellSteps`, and `bestDwell`,
- per-node magnitude, phase, phase delta, drive lock, omega, and node memory,
- output replay explanation: learned omega, memory gate, replay memory, applied replay advance, and implied effective period,
- path aggregate metrics over the selected input-to-output route.

## Anomalies Found
### Fixed in this pass
- The UI displayed `phaseInertia = 0.55` while the engine default was `1.25`.
- `persistAlpha` existed in the engine and UI bindings but had no HTML control.
- The "Night retained output" plot was actually showing raw night output, not the drive-locked trace its label implied.
- `renderCorrPlot()` referenced a missing canvas/context path and was dead code.

### Still worth watching
- The path walk uses straight sign-stepping on a torus. That is consistent with the current memory summary logic, but it is not a true shortest wrapped path solver.
- `outputNightHistory` is still the raw signal used for memory scoring. That is correct for the current metric, but it means "retained output" and "drive-locked output" should stay conceptually separate.

## How to Debug the "High Amplitude, Very Low Frequency" Case
1. Watch `Output raw R` and `Drive-locked output` together.
2. Check `dbgOutputMag` and `dbgReplayAdv`.
3. If magnitude stays healthy but replay advance is tiny, the slow night frequency is expected.
4. Check `dbgReplayMem` and `dbgReplayGain`.
5. If memory is weak, the night replay period can become far longer than the daytime drive period.
6. Compare `dProbePer`, `dOutPer`, and the replay implied period to see where the slowdown appears.

## Files
- Simulation engine: [field-dynamics-v7-phasepersist-experiment.js](/C:/Users/aaron/Desktop/liberalism/god-thoughts/kenosis/random-thoughts/ai/experiments/field-dynamics-v7-phasepersist-experiment.js)
- UI wiring: [field-dynamics-v7-phasepersist-ui.js](/C:/Users/aaron/Desktop/liberalism/god-thoughts/kenosis/random-thoughts/ai/experiments/field-dynamics-v7-phasepersist-ui.js)
- Page shell: [field-dynamics-v7-phasepersist.html](/C:/Users/aaron/Desktop/liberalism/god-thoughts/kenosis/random-thoughts/ai/experiments/field-dynamics-v7-phasepersist.html)
