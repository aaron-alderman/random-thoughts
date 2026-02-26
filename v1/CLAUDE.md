# CLAUDE.md

Guidance for Claude Code when working in this repository.

---

## Repository Overview

This is a philosophical writing repository, not a software project. It contains a sustained philosophical argument — a structural derivation of pure love that develops through the relational field, forgiveness dependency, cross-traditional theology, and concludes in Christian kenosis.

**Git repo root:** `random-thoughts/`
**Parent context:** This `kenosis/` folder is one thread within a larger project (`liberalism/god-thoughts/`). The kenosis sequence is self-contained but was developed alongside broader theological and political reflection.

---

## Primary Artifact

**`random-thoughts/framework.md` is the source of truth.**

It is a concept map — terms with typed relationships, claims with explicit dependency and implication chains, and brief example pointers. Essays in the layer directories are narrative expansions of subsets of this map. They are downstream of it, not the other way around.

When adding new content:
1. **Add to `framework.md` first** — define the term, map its relationships, connect it to the relevant claims
2. **Write an essay only if a narrative treatment is wanted** — and write it from the concept map, not independently

This means new topics can be integrated without overhauling existing essays. The concept map is the living environment; essays are one presentation format among others.

---

## Concept Map Notation (`framework.md`)

```
← requires / depends-on      what must be true for this term or claim to hold
→ generates / implies         what follows from this
✗ excludes / rules-out        what this is incompatible with
≈ corresponds                 structural isomorphism — not identity
? open                        what this does not settle
```

Epistemic status tags on claims:
- *structural* — follows from the derivation; no theological commitment required
- *evaluative* — assessment of a candidate against the specification
- *theological* — requires historical or experiential evaluation; not established by structural analysis

When updating `framework.md`, use this notation consistently. A term entry has: one-sentence definition + relationship graph + brief example pointer. A claim entry has: status tag + statement + `← depends-on` + `→ implies` + `✗ rules-out` + `? open` + example pointer.

---

## Document Structure

Four layers in `random-thoughts/`. Each layer depends on the layers above it. Full rationale in `random-thoughts/ARCHITECTURE.md`.

### Layer 1 — Foundation (`foundation/`)
*Core structural derivations from first principles, no theological commitment.*

| File | Role |
|------|------|
| `foundation/love.md` | Pure love stripped of contingent features → structural stance toward subjecthood. Entry point. |
| `foundation/relational-field.md` | The emergent field between two agents of pure love; the third entity; maintenance requirements. |
| `foundation/meaning.md` | The triad (constraints / agency / love) as necessary structure for meaning; tragedy as structural necessity; the geometry of alignment. Logically prior to everything; placed in Layer 1 to reflect that priority. |

### Layer 2 — Analysis (`analysis/`)
*Structural analyses following from the foundation.*

| File | Role |
|------|------|
| `analysis/forgiveness.md` | The field's structural dependency on prior unconditional forgiveness; secular sources fail; the forgiveness specification. |
| `analysis/correspondence.md` | Structural isomorphism between the relational field and Christian trinitarian theology. No theological truth claims. |

### Layer 3 — Evaluation (`evaluation/`)
*Candidates evaluated against the specification.*

| File | Role |
|------|------|
| `evaluation/transcendental-forgiveness.md` | Cross-traditional survey (Judaism, Islam, Hinduism, Buddhism, Zoroastrianism); convergence pattern. |
| `evaluation/christian-forgiveness.md` | Christianity's claim as a different logical type — historical event, not orientation; doctrines mapped to structural requirements. |

### Layer 4 — Synthesis (`synthesis/`)
*Synthesis, naming, and application.*

| File | Role |
|------|------|
| `synthesis/radical-kenosis.md` | Names the geometry as Radical Kenosis; Cross as paradigm; hiddenness, evil, and community failure as structural implications. |
| `synthesis/kenosis-and-the-bible.md` | The full biblical narrative (Creation to Eschaton) read through the framework — kenotic geometry as governing logic throughout. |

---

## Key Technical Terms

Full definitions with relationship graphs are in `random-thoughts/framework.md`. These terms carry specific structural meanings that must be preserved — do not use them in their ordinary-language senses.

| Term | Structural meaning |
|------|--------------------|
| **Pure Love** | Non-self-referential orientation toward the *subjecthood* of another; expressed through agency-preservation and non-interference |
| **Subjecthood** | The bare fact of interiority — terminal object of love; not flourishing, not behavior |
| **Agency** | Outward expression of subjecthood; criterion by which non-interference operates |
| **Self-referential contamination** | Any operation encoding the agent's own state as criterion (impression management, reciprocity tracking, outcome engineering) — primary source of field degradation |
| **The Relational Field** | Emergent bilateral structure with bandwidth, stability, generativity — not located in either agent |
| **The Third Entity** | What arises within the field; irreducible to either agent |
| **The Triad** | Constraints + agency + love — mutually constitutive necessary conditions for meaning |
| **Participatory love / Coercive control** | The two poles of the alignment gradient |
| **Structural gap** | Accumulated weight (misalignment + tragedy) no finite source can bear without depletion |
| **Forgiveness specification** | Structural shape of what would resolve the gap: external, interior, prior, covering invisible failure, non-depletable |
| **Radical Kenosis** | The geometry of alignment named in full — movement from coercive to participatory pole, enacted paradigmatically in the Cross |

---

## Essay Writing Conventions

These apply when writing or expanding narrative essays in the layer directories.

**Structure:** Roman numeral sections (I, II, III...). Examples as numbered sub-points (1., 2., 3.) within sections. Summary formulations in blockquotes. Final section states what has and has not been established.

**Epistemic discipline:** Maintain the distinction between structural claims (what the analysis establishes) and theological claims (what requires historical/experiential evaluation). This boundary is load-bearing throughout. "The structural analysis does not establish..." is precision, not hedging.

**Tone:** Dense, formal, analytical. No softening for reader comfort. Conclusions stated directly. Genuine uncertainty stated explicitly.

**Examples:** 2–3 concrete examples per major claim. Phenomenological — recognisable human situations, not abstract hypotheticals.

**Cross-references:** Concept-indexed, not positional. Write "as established in the pure love derivation" or "the triad analysis shows" — not "the preceding document" or "as document 3 showed." Use relative markdown links when linking: e.g., `[the triad](../foundation/meaning.md)`.

**Dependency declaration:** Every non-Layer-1 essay opens with a *Draws on:* line immediately after the title, listing direct dependencies with links. Layer 1 documents omit this (no in-project dependencies).

**What the argument does not claim:** The essays establish structural coherence and specification, not historical fact. "The Christian account is structurally coherent and uniquely precise" ≠ "Christianity is true." This distinction is load-bearing and must not be blurred.
