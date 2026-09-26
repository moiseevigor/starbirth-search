---
tags: [meta, convention]
---

# Research/ folder convention

The `Research/` subtree holds paper summaries, syntheses, and concept-anchor notes. It is **multi-user and multi-domain** — it scales to thousands of papers by combining a flat-ish directory structure with the 6-axis tag taxonomy ([[tags]]) for retrieval.

## Structure

```
Research/
├── <Domain>/                ← matches one #domain/* value (group-theory, ai, cs, methodology, ...)
│   ├── <Topic>/             ← optional sub-grouping when papers naturally cluster
│   │   ├── <paper-id>.md
│   │   ├── <paper-id>.md
│   │   └── _synthesis-<topic>.md     ← multi-paper synthesis (optional)
│   └── <paper-id>.md        ← papers that don't fit a sub-grouping go at domain level
└── ...
```

Notes:
- **Top-level dirs are domains.** One dir per registered `#domain/*` value.
- **Topic dirs are organizational, not the source of truth.** Topics live in tags (`#topic/*`), which are what drive search and Bases queries. Directory placement is just for humans browsing the tree.
- **Paper-id filenames**: short kebab-case from first-author + year (`havas-newman-1980.md`) or arxiv-id (`2410.12345.md`).
- **Syntheses** prefixed with `_synthesis-` so they sort to the top of their dir.

## When to create a new sub-topic dir

Only when a topic has accumulated **3+ papers** that naturally co-locate. Single-paper sub-dirs are clutter — leave the paper in the **closest matching existing subdir** until the cluster forms.

**"Closest matching subdir" — NOT "domain root."** If a paper is about Burnside groups B(2,5) and the `Research/Group theory/Burnside groups/B25/` subdir already exists with 5+ papers, the new paper goes **there**, not at `Research/Group theory/` root. Use the topic tags as the primary signal for placement: if the paper carries `#topic/burnside` and `#topic/b25`, and `Burnside groups/B25/` exists, that's the right home.

Only place a paper at a domain root (e.g. `Research/Group theory/`) if it genuinely spans the entire domain and doesn't fit any sub-topic — extremely rare. When in doubt, **ask the invoker** which subdir is right. Don't default to domain root.

When you do create a sub-topic dir, add a brief `_README.md` explaining what belongs there (3-5 lines).

## Where do concepts go?

`Concepts/<concept-name>.md` is **separate from `Research/`**. Concept notes are reusable anchors that multiple paper summaries link to (via `key_concepts: []` frontmatter). They are the connection-graph hubs.

Rules:
- Create a concept hub only when the concept appears in **2+ papers**.
- Concept hubs use [[concept-note]] template — short, authoritative, mostly auto-from-frontmatter.
- Long discussion goes in paper notes (or in syntheses), not in concept hubs.

## Domain naming

The domain a paper goes under is the **field whose methodology the paper contributes to**, not the field the paper happens to be applied to.

- AI-applied-to-group-theory paper → `Research/AI in Math/` (the methodology is AI; the application is group theory).
- KB completion analysis using group-theoretic techniques → `Research/Group theory/` (methodology is group theory; KB is just the object of study).

When in doubt, pick one, and link to the other via `key_concepts` or a `See also` section.

## Adding new domains

Don't add a new top-level `Research/<NewDomain>/` until:
1. The corresponding `#domain/*` value is registered in `_meta/tags.md`.
2. There's at least one paper to place there.

Researcher has restructure authority over `Research/` and `Concepts/` — they can add new domain dirs as colleagues bring papers from new fields. But the registration step in `_meta/tags.md` is mandatory first.

## Restructuring

When the directory tree starts feeling wrong (a domain has too many papers and needs sub-topics, two domains overlap and should merge, a topic has migrated across domains), Researcher restructures with their authority. Every restructure must be logged to `Agents/<owning-user>/Researcher/log.md` with before → after.

For colleagues using `/research` (not on the Maestri canvas): if your domain isn't well-served by the current structure, raise it with Maria. Don't restructure unilaterally — the vault is shared.

## Filename conventions (added 2026-05-28)

See `_meta/naming-conventions.md` for the vault-wide rules. Research/-specific additions:

- **Paper-id filenames** follow `<first-author>-<year>.md` or `<first-author>-<coauthor>-<year>.md`. For open-problem notes: descriptive kebab-case (`b25-finiteness-11.48-kostrikin.md`).
- **`_overview.md` is deprecated** in Research/. Replaced by `<subject>-overview.md` per Rule 1 in [[naming-conventions]]. Existing `_overview.md` files created before 2026-05-28 are being renamed in Phase 7.
- **Syntheses**: `_synthesis-<topic>.md` (underscore-prefixed, sorts to top). This is the one legitimate `_` prefix for Research/ notes.
- **MOC files**: `_moc-<topic>.md` in `Research/<Domain>/_MOCs/`.

## Cross-linking discipline (added 2026-05-28, Phase 9)

**Every content note in `Research/` must end with a `## Related material` section containing at least 3 substantive wikilinks.** A note with zero outgoing wikilinks is incomplete — it's an orphan-on-creation regardless of its topical substance.

Minimum link set per note:

- **Parent overview**: every note in a subdir links up to its parent `<subject>-overview.md` (e.g. `decidability-landscape.md` → `[[word-problem-overview]]`; `01-group-order.md` → `[[gap-overview]]` and `[[group-theory-tools-overview]]`).
- **Relevant MOC**: every note links to at least one MOC in `Research/<Domain>/_MOCs/` — `[[_moc-word-problem]]`, `[[_moc-knuth-bendix]]`, `[[_moc-burnside]]`, etc. (substance test — only MOCs where this note is genuinely a curated landing target).
- **Substantive siblings / concepts / papers**: 1+ wikilinks to related siblings in the same dir, to `Concepts/<name>.md` hubs the note relies on, or to specific papers the note's content was developed in or builds on.

**Bidirectional discipline**: every wikilink added to a note's Related material section is reciprocated on the target end. If a content note links to a MOC, that MOC's "Concepts" / "Techniques" / "Tools" section must include a wikilink back. If a content note links to a paper, that paper's `cited_by:` or its `Related material in vault` section must include the back-link.

**Substance test** (mandatory on every link): "would a reader following this link land somewhere genuinely relevant?" Not "link everything to everything." Aspirational links — "this paper *could* use this concept" without specific engagement — are rejected.

**Exemption**: housekeeping notes (logs, READMEs, scratch entries — anything under [[naming-conventions]] § Rule 2) are not required to carry a Related material section.

**Wikilink-like syntax in example/template content** (`[[<placeholder>]]`, `[[<topic>]]`, `[[<paper-id>]]`, etc.) **must be wrapped in backticks**. Bare `[[<...>]]` in body text is treated as a real wikilink by Obsidian's parser and creates phantom orphan nodes in the graph view (root cause: same wikilink-parser-before-rendering issue documented in [[paper-summary]] § Notation conventions for commutator brackets). The backtick wrap renders the example syntax in monospace for the human reader without triggering Obsidian's node graph. Applies vault-wide: templates, agent prompts, scratch briefs, conventions.
