# Project Architecture

This document records the organizational structure of the project, the rationale behind it, and the conventions for adding new work. It is intended as a durable reference so the structure can be maintained and extended without a retrospective refactor.

## Primary Artifact

**`framework.md` is the source of truth.** It is a concept map — terms with typed relationships, claims with explicit dependencies and implications, and brief example pointers. Everything else is downstream of it.

The layer directories contain **narrative essays** — human-readable expansions of subsets of the concept map, with developed examples and rhetorical arc. Essays are not the source of truth; they do not need to be updated when new concepts are added. When a new concept is introduced, it goes into `framework.md` first. An essay is written only when a narrative treatment is wanted, and it is written *from* the concept map.

This separation means:
- New topics can be added to the concept map without overhauling existing essays
- The argument's structure is inspectable independently of any particular narrative presentation
- Multiple narrative arcs can be generated from the same concept map

---

## Layer Structure

Documents are organized into four layers. Each layer depends on the layers above it but not on layers at the same level or below.

```
random-thoughts/
├── framework.md          ← living reference: terms and structural claims
│
├── foundation/           ← Layer 1: core structural derivations
│   ├── love.md
│   ├── relational-field.md
│   └── meaning.md
│
├── analysis/             ← Layer 2: structural analyses drawing on Layer 1
│   ├── forgiveness.md
│   └── correspondence.md
│
├── evaluation/           ← Layer 3: evaluations of candidates against the specification
│   ├── transcendental-forgiveness.md
│   └── christian-forgiveness.md
│
└── synthesis/            ← Layer 4: synthesis, application, extension
    ├── radical-kenosis.md
    └── kenosis-and-the-bible.md
```

### What belongs in each layer

**Layer 1 — Foundation**
Documents that derive the core structural claims from first principles, without theological commitment and without reference to other documents in this project. These are the stable core. They should only be revised if the derivation itself needs correction. Everything else draws on them.

Currently: the pure love derivation, the relational field analysis, the triad (constraints/agency/love).

**Layer 2 — Analysis**
Documents that apply the foundational framework to specific structural problems — identifying gaps, isomorphisms, or dependencies that follow from the foundational claims. They draw on Layer 1 but not on each other or on Layers 3–4.

Currently: the forgiveness dependency (with secular candidate evaluation), the trinitarian structural correspondence.

**Layer 3 — Evaluation**
Documents that evaluate specific candidates (traditions, historical claims, theological accounts) against the structural specification established in Layers 1–2. They draw on Layers 1–2 but not on Layer 4.

Currently: the cross-traditional forgiveness survey, the specifically Christian claim.

**Layer 4 — Synthesis and Application**
Documents that synthesize the full argument, name its geometry, or apply the framework to a specific domain. They can draw on any preceding layer. New topics — political philosophy, ethics, anthropology, community, anything else — slot here without touching Layers 1–3.

Currently: Radical Kenosis (synthesis), Kenosis and the Biblical Narrative (application).

---

## Adding New Concepts and Documents

### Step 1 — Add to the concept map first
Before writing any essay, add the new concept(s) to `framework.md`:
- Define the term in one sentence
- Map its relationships using the notation (← → ✗ ≈ ?)
- Add it to any existing claim's dependency chain if it affects what the claim implies or rules out
- Add a new claim entry if the concept generates a new structural proposition

This is the only required step. An essay is optional.

### Step 2 — Write an essay if narrative treatment is wanted
Before writing, answer:

**Which layer does it belong in?**
- Derives something from first principles, no theological commitment → Layer 1 (`foundation/`)
- Identifies a structural problem or isomorphism following from the derivations → Layer 2 (`analysis/`)
- Evaluates a specific candidate against the specification → Layer 3 (`evaluation/`)
- Synthesizes, names, or applies the framework to a domain → Layer 4 (`synthesis/`)

**Which concepts does it draw on?**
List these in the *Draws on:* declaration at the top of the new document. Direct dependencies only.

New essays in Layer 4 can be added freely without touching Layers 1–3. New essays in Layers 2–3 can be added freely without touching Layer 1.

---

## Conventions

### File naming
Lowercase, kebab-case, no numbers: `love.md`, `relational-field.md`, `kenosis-and-the-bible.md`. Numbers in filenames encode sequence, which this structure replaces with explicit dependency declarations.

### Dependency declarations
Every document except Layer 1 entry points opens with a dependency declaration immediately after the title, before the first section:

```markdown
# Document Title

*Draws on: [The Pure Love Derivation](../foundation/love.md) · [The Relational Field](../foundation/relational-field.md)*

---
```

Layer 1 documents that have no dependencies within the project do not need this line.

### Cross-references within prose
Use concept-indexed references, not positional ones.

| Instead of | Write |
|------------|-------|
| "the preceding analysis established" | "the pure love derivation established" |
| "as shown in the earlier document" | "as the triad analysis shows" |
| "the analysis above" | "the forgiveness specification" |

This makes references stable regardless of ordering, numbering, or restructuring. Positional language breaks silently when the structure changes; concept-indexed language does not.

When a reference warrants a link, link to the relevant document or to the entry in `framework.md`.

### The framework document
`framework.md` is the living reference for technical terms and core structural claims. It is updated incrementally as new documents introduce new terms or claims. New documents should link to it for established terms rather than re-deriving them.

---

## Known Ordering Issues (Archived)

The original sequence (numbered 1–9) has a documented logical asymmetry: `meaning.md` (originally document 7) is logically prior to the others — it establishes the ontological ground (the triad) that the earlier documents presuppose — but was written retrospectively and placed seventh. The current layer structure resolves this by placing `meaning.md` in Layer 1 (foundation), where its logical priority is visible in the structure rather than noted as a caveat.

Similarly, `correspondence.md` (originally document 3) has more evidential weight if read after the cross-traditional survey has established the convergence pattern, rather than before the forgiveness problem is fully developed. The layer structure makes this an ordering choice rather than a structural necessity — both sequences are coherent; readers can follow dependency declarations to find their own path.

The linear reading order `foundation → analysis → evaluation → synthesis` is the most natural for a first reading. But it is a reading path, not a logical constraint.

---

## Refactoring Status

| Stage | Description | Status |
|-------|-------------|--------|
| Directory structure | Four layers + file moves + renames | Complete |
| Dependency declarations | Top-of-document link lines | Complete |
| Framework document | Terms and claims reference | First pass complete; claims TBD |
| Positional language | Convert "preceding analysis" → concept-indexed | Not started — low urgency |

Positional language conversion priority when undertaken: `foundation/love.md` and `foundation/meaning.md` first (most-referenced documents), then `synthesis/radical-kenosis.md` (most cross-references), then the rest in any order.
