# Parameter Governance v1

## Backbone

The project now treats the field as a shared backbone with experiment-scoped search subsets.

- The canonical searchable parameter catalog lives in `parameter_policy.py`.
- Backbone defaults are the project-wide starting point for all experiments.
- Fixed non-evolved runtime parameters also live in `parameter_policy.py`.

Changing a backbone default is a project-level change. It is not an experiment-local tuning action.

## Active Sets

Every experiment must declare:

- a stable experiment id
- a fitness profile
- a small active searchable parameter set
- any frozen runtime overrides

No experiment may implicitly search the entire global parameter catalog.

Current active-set policy:

- `symmetry_v1`
  - active: `driveAmp`, `cueAmp`, `cycleLen`, `kAlign`, `persistAlpha`, `omegaLearn`, `edgeDecay`, `driveRamp`, `driveClamp`, `tauC`
- `replay`
  - active: `driveAmp`, `cycleLen`, `phaseInertia`, `persistAlpha`, `omegaLearn`, `edgeDecay`, `tauC`
- `temporal_v1`
  - active: `epsilon`, `beta`, `driveAmp`, `cycleLen`, `kAlign`, `tauC`

If an experiment needs more than 8 active parameters, it must justify that expansion in its config notes.

## Genome And State Storage

Artifacts are experiment-scoped:

- genomes: `genomes/<experiment>/best_genome.json`
- search state: `search_state/<experiment>/cmaes_state.pkl`
- search history: `search_state/<experiment>/cmaes_history.json`

Genome payloads contain:

- experiment id
- optional symmetry break
- `active_param_names`
- `active_params`
- `frozen_params`
- `resolved_params`
- fitness and evaluation metadata

This is a clean-break format. Legacy flat genome files are not part of the supported workflow.

## Experiment Config Contract

Every new experiment config must define:

- `experiment`
- `active_params`
- `frozen_overrides`
- `fitness_profile`
- allowed symmetry policy

The config is responsible for search dimensionality, genome payload shape, and default runtime parameter resolution.

## Promotion Rules

Add a parameter only when it changes the expressive capability of the system, not just because it helps one search run.

When adding a parameter, assign:

- semantic group
- default value
- bounds if searchable
- searchability default
- role: backbone, experiment-tunable, or derived

Promote a parameter from experiment-local relevance to backbone relevance only when:

- it matters across multiple experiment families
- its effect is interpretable
- freezing it would materially harm more than one branch
