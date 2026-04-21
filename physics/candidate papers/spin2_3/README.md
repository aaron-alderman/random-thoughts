# Spin(2,3) Programme

This repository is the working corpus for the Spin(2,3) research programme. The current organization separates core framework material, kernels, research tracks, papers, and archived snapshots so claims do not drift across maturity levels.

## How To Read This Repo

- Start with `core/README.md`, then `core/master-framework.md` for the project spine and claim taxonomy.
- Use `core/spin23-compendium.md` as the current broad map.
- Use `kernels/README.md` for the domain-specific working documents.
- Use `CLAIM_LEDGER.md` to check whether a statement is established, conditional, conjectural, speculative, or retired.
- Use `ROADMAP.md` for the current order of work.

## Directory Map

| Path | Role |
| --- | --- |
| `core/` | Core Spin(2,3) framework and parent-reduction scaffolding |
| `kernels/` | Statics, dynamics, epistemics, consistency, interpretation, phenomenology, topology, and open problems |
| `research/` | Research-track index and non-core tool/bridge work |
| `research/spectral-transition/` | General spectral-gap and projector-geometry toolkit |
| `research/faddeev-efimov/` | Conjectural Faddeev/Casimir/Efimov bridge track |
| `papers/` | Draft paper artifacts and supporting scripts |
| `archive/` | Snapshots, overflow, and non-live synthesis material |

## Governance Rule

Research tracks may suggest new core claims, but they must pass through `CLAIM_LEDGER.md` before they are treated as part of the framework.

## Stability Checks

Before treating the corpus as stable after a reorg:

- scan for old flat-corpus filenames and absolute local paths;
- scan for retired bridge-overclaim phrases;
- scan `core/` for Efimov references and confirm they mark the bridge as conjectural/open;
- check backticked `.md` references resolve either relative to their file or from the repo root.
