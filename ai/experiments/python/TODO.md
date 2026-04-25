# Field Dynamics - TODO

## Short term - v8: Evolutionary search

Goal: stop tuning parameters by hand, now with experiment-scoped objectives and artifacts.

- [x] `batched_field.py` - `BatchedField` runs B instances as `(B, N, N)` tensors in a single GPU pass
- [x] Replay fitness includes frequency faithfulness as well as correlation / retention
- [x] `evolve.py` - GA over `{W, alpha, beta, selfEx, epsilon, retain, phaseInertia}`, population 16, uniform crossover + Gaussian mutation with annealing
- [x] Experiment-scoped genomes are saved:
- [x] `python/best_genome.symmetry_v1.spatial.json`
- [x] `python/best_genome.replay.json`
- [x] CMA-ES state/history are now experiment-scoped too
- [x] `--experiment` and `--symmetry-break` flags exist on the search entrypoints
- [x] Run the symmetry search: `python evolve.py --device cuda --experiment symmetry_v1 --gens 40`
- [x] Run the replay baseline search explicitly: `python evolve.py --device cuda --experiment replay --gens 20`
- [x] Run fresh CMA-ES on the new default objective: `python evolve_cmaes.py --device cuda --fresh --experiment symmetry_v1 --gens 20`
- [x] Fix the triadic remainder computation - the current formula telescopes to ~0 (same as JS). The correct version wraps each individual edge phase difference before summing. Low risk to try; revert if behaviour changes.

## Medium term

### Active task - Symmetry breaking
- [x] Separate shared gate waveform from content signals
- [x] Use `symmetry_v1` as the default experiment family
- [x] Hard-code the first symmetry break: `--symmetry-break spatial`
- [x] Add choice/persistence metrics:
- [x] `choice_strength`
- [x] `choice_consistency`
- [x] `overnight_persistence`
- [x] `switch_penalty`
- [ ] Validate the default symmetry task visually and with search
- [ ] Add a second programmed break type once `spatial` is stable

### Replay baseline
- [x] Characterise the night waveform at the output node
- [x] Compare day vs night replay period, not just correlation
- [x] Fix replay so memory no longer slows angular velocity directly
- [ ] Replace zero-lag replay correlation with a more phase-aware metric if needed

### v9 - Second scale
- [ ] Add coarse grid `(N//2, N//2)` - receives `pool(R_fine)` only (not X, not C, not drive)
- [ ] Coarse -> fine: upsample `C_coarse` only
- [ ] Test: does coarse structure outlast fine structure overnight?

### v10 - Organic growth
- [ ] Remove fixed grid size - grid grows as a result of dynamics, not a parameter
- [ ] Implement triadic closure as explicit growth mechanism - new nodes added where C is high and R is high in adjacent triangle
- [ ] Implement recycling - nodes where both C and R are low get absorbed by neighbours

## Long term

- [ ] Websocket visualiser - Python sends field state each frame, browser renders (preserves the WebGPU-style live view from v7)
- [ ] RLHF analog - structural critic trained on human evaluation of field output quality
- [ ] Edge field `E(i,j)` as first-class field entity - relations become the primary object, not a derived quantity
- [ ] Real inputs - camera or audio stream drives input nodes
- [ ] 3D spatial field - vortex filaments, topologically protected memory states
- [ ] Quaternion field values - make the SU(2) structure exact rather than emergent from complex phases

## Known issues

- `triRem` is effectively zero (inherited from JS - the phase sum telescopes algebraically). `R` is still meaningful because it is dominated by the `1 - coh` term. Fixing this is in the v8 backlog above.
- `matplotlib` interactive mode slows significantly for N > 64. Switch to the websocket renderer before scaling up.
- Replay is now treated as a validated baseline, but zero-lag correlation can still under-score good phase-shifted replay.
- `symmetry_v1` uses a small fixed spatial bias by construction. That is intentional for the first experiment family and should not be mistaken for an evolved asymmetry.
