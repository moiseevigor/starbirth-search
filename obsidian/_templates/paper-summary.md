---
title: <paper title in English>
authors: <First Author, Second Author, ...>
year: <YYYY>
venue: <arxiv | journal name | thesis | textbook | preprint>
url: <link to canonical source>
url_translated: <link to English translation if separate from source>
language: <en | ru | de | zh | ...>            # source paper's language (for filtering / discovery)
domain: <astrophysics | methodology>  # MANDATORY property — Bases queries this. Must mirror the #domain/* tag below; tag alone is not enough.
status: <draft | review | validated | rejected | superseded>  # MANDATORY property — Bases queries this. Must mirror the #status/* tag below.
methodology_type: <theoretical | empirical | review | methodology | tutorial>
citation_count: <integer>
citation_count_date: <YYYY-MM-DD>
key_concepts: []                                 # wikilinks to Concepts/<name>.md hubs
extends: []                                      # wikilinks to other paper notes this paper builds on
contradicts: []                                  # wikilinks to other paper notes whose results this contradicts
replicates: []                                   # wikilinks to other paper notes this paper's experiment replicates
cites: []                                        # selected upstream citations relevant to this vault's interests
cited_by: []                                     # known downstream papers in this vault that cite this one
quality_notes: <free text, OPTIONAL — only write if there's something specific to say about the evidence quality, replication status, withdrawal, or reception. Examples: "Foundational; cited by every subsequent B(2,5) paper", "Withdrawn from arXiv 2024-03 — see retraction note", "Has 14 citations but all from the same research group — needs external replication.">
author: <handle of human who owns this note>
tags:
  - agent/research
  - user/<handle>
  - domain/<one>
  - topic/<one>
  - topic/<two>
  # add as many topic/* tags as the paper genuinely engages with (typically 4-10, no upper bound, substance test)
  - paper
  - status/draft
project: <optional — only if scoped to a named project>
---

# {{title}}

> **Translation note**: vault language is English. If the source is non-English, the Abstract below is translated to English (mark inline with `[trans.]` if needed for clarity); quotes are translated and tagged `[trans.]`. Original-language text is **not** preserved in the vault — `language:` frontmatter records the source language for filtering. If a reader needs the original, follow the `url:`.

## Abstract

<Verbatim copy of the paper's abstract. If the source is non-English, translate to English here and append `[trans.]` at the end of the section. Do not paraphrase — translate as literally as the language allows.>

## TL;DR

<2–3 sentences. Researcher's distillation: what would a colleague need to know to decide whether to read this paper? Different from the abstract — the abstract is the authors' framing; the TL;DR is the retrieval framing.>

## Problem

<What question does this paper answer? State the open problem it engages with, in plain prose. If the paper poses a new question, state both the framing and the question.>

## Approach

<High-level method. For theoretical papers: the proof strategy. For empirical papers: the experimental design. For algorithmic papers: the algorithm sketch. Cite paper sections for anything technical.>

## Key result

<Verbatim numbers, theorem statements, complexity bounds. Cite section. For theorems: state the theorem in English, then in mathematical notation. Don't paraphrase numbers — copy them. If the paper has multiple results, list each.>

## Assumptions

<Explicit list of what the paper assumes. Foundational assumptions (e.g. "assumes ZFC"), structural assumptions (e.g. "assumes the group is finitely presented"), empirical assumptions (e.g. "tested on instances with N ≤ 10⁶"). Be specific.>

## Limitations / scope

<What the paper does NOT claim, and what doesn't apply. Either as stated by the authors or as observed by Researcher.>

## Replication evidence

<Has this result been replicated? By whom, where, how? `yes` (link the replications) / `no` (note absence) / `partial` (describe what's been confirmed).>

## Why this paper matters

<Researcher's editorial — 1-3 paragraphs. Where does this paper sit in the literature? What does it enable? What does it foreclose? If `quality_notes` in frontmatter says something specific about reception, expand on it here.>

## Quotes

<Maximum 2 quotes. Each: short (fewer than 15 words ideal, never more than 30), verbatim with quotation marks, cite section. If translated, append `[trans.]` after the quote.>

1. > "<quote>" — Section X.Y
2. > "<quote>" — Section X.Y

## Open questions surfaced

<Questions the paper raises but doesn't answer. Future-work pointers. Open empirical questions that an Experimenter could attempt. Open theoretical questions that a Validator could investigate. Concrete and bounded, not vague.>

## Related material in vault

<Wikilinks to related paper notes, concepts, and experiments. This section is auto-generated from frontmatter `extends`/`contradicts`/`replicates`/`cites`/`cited_by` plus any manually-added context. Researcher updates as the vault grows.>

- Extends: <wikilinks from frontmatter `extends`>
- Contradicts: <wikilinks from frontmatter `contradicts`>
- Replicates: <wikilinks from frontmatter `replicates`>
- Concepts introduced/used: <wikilinks from frontmatter `key_concepts`>
- Cites: <selected wikilinks from frontmatter `cites`>
- Cited by (in this vault): <wikilinks from frontmatter `cited_by`>

---

## Notation conventions

**Commutator notation in body prose:** All expressions containing `[[...]]` (double brackets) must be escaped — Obsidian's wikilink parser runs BEFORE any rendering, including LaTeX. `$...$` and `$$...$$` do NOT protect `[[...]]` from being parsed as wikilinks. The **only safe escape is backticks**.

**Priority order:**

1. **Backtick inline code** (PRIMARY — always safe): `` `[[2,1,2,1,1,2], [2,1,2,1,1]]` `` or `` `[[[[[[x,y],y],y],y],y],y]` ``
2. **LaTeX inline math** (SAFE only if the expression does NOT contain `[[`): `$[a,b]$` is fine; `$[[a,b],c]$` is NOT — the wikilink parser sees `[[a,b]` before LaTeX renders.
3. **Escaped brackets**: `\[x, y\]` — safe for single-bracket expressions like `[a,b]`, but not for `[[...]]`.

**Why LaTeX doesn't work for `[[...]]`:** Empirically confirmed 2026-05-28: wrapping `[[2,1,2,1,1,2], [2,1,2,1,1]]` in `$...$` left the orphan node `2,1,2,1,1,2]` visible in the graph view. Obsidian parses wikilinks before rendering LaTeX; any `[[..., ...]]` pattern with a matching `]]` terminator creates a phantom regardless of context.

**Rule:** Use backticks for any expression containing `[[`. Use LaTeX only for expressions with single brackets (`[a,b]`, `[a,b,c]`, etc.) that don't contain `[[`.

**Template placeholders** in example wikilinks must also be in backticks — `` `[[<placeholder>]]` `` — to prevent phantom-node creation in Obsidian's graph view. Same root cause: the wikilink parser sees `[[<placeholder>]]` literally and creates an orphan node for the placeholder name.

This convention applies to all vault notes, not just paper summaries.
