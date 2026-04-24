# Field Dynamics — TODO

## Immediate (blocking)

- [x] Install Python from python.org
- [x] Install dependencies — torch (CUDA 12.4), numpy, matplotlib
- [ ] Run `python check_gpu.py` — confirm RTX 3060 is visible to PyTorch
- [ ] Run `python run.py --device cuda` — verify simulation runs on GPU and matches v7 JS behaviour visually
- [ ] Confirm dwell measurement works — watch corr panel through at least one full day/night cycle

## Short term — v8: Evolutionary search

Goal: stop tuning parameters by hand.

- [x] `batched_field.py` — `BatchedField` runs B instances as `(B, N, N)` tensors in a single GPU pass
- [x] Fitness function — `peak_corr * clamp(night_rms / day_rms, max=2)` (correlation × signal retention)
- [x] `evolve.py` — GA over `{W, alpha, beta, selfEx, epsilon, retain, phaseInertia}`, population 16, uniform crossover + Gaussian mutation with annealing
- [x] Genome saved to `best_genome.json` after each generation
- [x] `--load_genome best_genome.json` flag in `run.py` to visualise the best individual
- [ ] Run the search: `python evolve.py --device cuda --gens 40` — confirm fitness increases generation over generation
- [ ] Fix the triadic remainder computation — the current formula telescopes to ~0 (same as JS). The correct version wraps each individual edge phase difference before summing. Low risk to try; revert if behaviour changes.

## Medium term

### v9 — Second scale
- [ ] Add coarse grid `(N//2, N//2)` — receives `pool(R_fine)` only (not X, not C, not drive)
- [ ] Coarse → fine: upsample `C_coarse` only
- [ ] Test: does coarse structure outlast fine structure overnight?

### v10 — Organic growth
- [ ] Remove fixed grid size — grid grows as a result of dynamics, not a parameter
- [ ] Implement triadic closure as explicit growth mechanism — new nodes added where C is high and R is high in adjacent triangle
- [ ] Implement recycling — nodes where both C and R are low get absorbed by neighbours

### v11 — Second task (symmetry breaking)
- [ ] Two conflicting input signals at spatially separated nodes
- [ ] Measure: does the field resolve to one basin rather than oscillating?
- [ ] Measure: does the resolved basin persist overnight?

## Long term

- [ ] Websocket visualiser — Python sends field state each frame, browser renders (preserves the WebGPU-style live view from v7)
- [ ] RLHF analog — structural critic trained on human evaluation of field output quality
- [ ] Edge field `E(i,j)` as first-class field entity — relations become the primary object, not a derived quantity
- [ ] Real inputs — camera or audio stream drives input nodes
- [ ] 3D spatial field — vortex filaments, topologically protected memory states
- [ ] Quaternion field values — make the SU(2) structure exact rather than emergent from complex phases

## Known issues

- `triRem` is effectively zero (inherited from JS — the phase sum telescopes algebraically). `R` is still meaningful because it is dominated by the `1 - coh` term. Fixing this is in the v8 backlog above.
- `matplotlib` interactive mode slows significantly for N > 64. Switch to the websocket renderer before scaling up.
