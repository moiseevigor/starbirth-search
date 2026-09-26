# Workflow — Single Paper

Use when the invoker hands one paper URL or ID and wants a structured summary in the vault.

## Steps

1. **Confirm the source.** Echo back the URL or arxiv ID. If ambiguous (e.g. "the recent Buchberger paper"), ask which one.

2. **Check for prior coverage.** Grep the vault: `grep -r "<arxiv-id>" Obsidian/Math/Research/` and `grep -r "<paper-title-keywords>" Obsidian/Math/Research/`. If a note already exists, ask whether to update or skip.

3. **Identify the invoking user's handle.** Check frontmatter of recent vault notes for `#user/<handle>` tags belonging to the invoker. If unclear, ask. If the handle isn't yet registered in `_meta/tags.md`, register it now.

4. **Fetch the paper.**
   - First try `defuddle <url>`.
   - If defuddle returns nothing useful (image-only PDF, login wall, etc.), try `WebFetch`.
   - If both fail, ask the invoker for an alternative source.

5. **Read the paper.** Extract content per the [[paper-summary]] structure.

6. **Look up citation count.** Use Semantic Scholar / Google Scholar / arXiv stats. Best-effort; record with `citation_count_date`.

7. **Identify domain.**
   - Match against registered values in `_meta/tags.md`: `group-theory`, `ai`, `cs`, `methodology`.
   - If the paper doesn't fit any current domain, register a new one in `_meta/tags.md` first (don't invent a domain on-the-fly).

8. **Identify topics.**
   - Substance test: every `#topic/*` tag must answer yes to "would a colleague searching for this topic want this paper to surface?"
   - 4-10 typical, no upper bound, but never aspirational.
   - Reuse existing topic tags before inventing new ones — check Obsidian's tag pane or grep existing notes.

9. **Identify concepts.**
   - List the concepts the paper introduces or relies on.
   - For each concept: check if `Concepts/<concept-name>.md` exists.
     - If yes: add a wikilink to the paper's `key_concepts` frontmatter.
     - If no: only create the stub if the concept appears in 2+ papers (current paper + at least one prior). Don't create singleton hubs.

10. **Identify connections.**
    - Grep the vault for papers that the current paper cites, is cited by, extends, contradicts, or replicates.
    - Populate `cites`, `cited_by`, `extends`, `contradicts`, `replicates` frontmatter with wikilinks.
    - For `cited_by`: also update the cited paper's note (bidirectional).

11. **Translate if non-English.**
    - Translate the abstract to English in the body, append `[trans.]`.
    - Translate quotes; mark each with `[trans.]`.
    - Record source language in `language:` frontmatter.
    - Do NOT preserve original-language text in the vault. Reader who needs the original follows `url:`.

12. **Choose a unique filename first.**
    - Filename must uniquely identify the paper across the vault without folder context. Pattern: `<first-author>-<year>.md` or `<first-author>-<coauthor>-<year>.md` or `<arxiv-id>.md`.
    - Never use generic names alone: `paper.md`, `note.md`, `summary.md`. Always qualify with author/year or a descriptive topic slug.
    - Verify uniqueness: `grep -r "<proposed-stem>" <vault>/Research/ --include="*.md" -l`. If there's a conflict, add more specificity (e.g. `havas-1980-computers-burnside.md`).
    - See `_meta/naming-conventions.md` for the full rule set.

13. **Determine the correct directory path BEFORE writing.** This is a structural-placement check — a paper's filename + content alone don't tell Obsidian where it belongs; the directory does. Get this wrong and the paper is hard to find later.

    **The placement rule**: `Research/<Domain>/<Topic subdir>/<deeper subdir if applicable>/<paper-id>.md`

    - **`<Domain>`** matches the paper's `#domain/*` tag, mapped to the directory naming convention. Current dirs (see `_meta/research-folder-convention.md`):
      - `#domain/group-theory` → `Research/Group theory/`
      - `#domain/ai` → `Research/AI in Math/`
      - `#domain/cs` → `Research/Algorithm Cooperation/` (CS papers about algorithm cooperation) — for other CS papers, ask the invoker before creating a new subdir
      - `#domain/methodology` → choose carefully; usually `Research/<relevant-domain>/` if the methodology is domain-specific, or flag to invoker if it's cross-cutting
    - **`<Topic subdir>`** matches the most-specific applicable subdir under the domain. For Group theory specifically:
      - Papers about **Burnside groups (any exponent)** go in `Research/Group theory/Burnside groups/<exponent>/`. E.g. B(2,5) papers go in `Research/Group theory/Burnside groups/B25/`. B(2,3), B(4,3), B(5,3) papers go in their own respective subdirs (create if missing, ask invoker if uncertain).
      - Papers about **Word Problem techniques or theory** go in `Research/Group theory/Word Problem/` or `Research/Group theory/Word Problem/techniques/`.
      - Papers about **general group theory foundations** (subgroups, presentations, group orders) go under `Research/Group theory/General/<area>/`.
      - Papers about **open problems** go under `Research/Group theory/Open problems/<area>/` (e.g. `Open problems/Burnside groups/`, `Open problems/Free groups/`).
      - Papers about **tooling** (GAP, KBMAG, etc.) go under `Research/Group theory/Tools/<tool-name>/`.
    - **NEVER put a paper at `Research/<Domain>/` root** unless it genuinely spans all sub-topics within that domain (rare — almost always there's a more specific subdir). If you find yourself wanting to do this, **stop and ask the invoker** which subdir is right.

    **Concrete check before writing**: state the proposed path back to yourself in this format: "About to write `<proposed-path>`. Topic tags say this paper engages with `[topic-list]`. Does the path's deepest subdir match the most-specific topic? Are there sibling papers in that subdir with similar topic profiles?" Use `ls` on the proposed dir to see siblings. If the siblings have wildly different topics, the path is probably wrong.

    **If unsure**: don't write to disk yet. Ask the invoker: "Based on the paper's topics `[X, Y, Z]`, I'm considering `<proposed-path>` — is that right, or should it go under a different subdir?"

14. **Write the note.**
    - Path: the one verified in step 13 (e.g. `Research/Group theory/Burnside groups/B25/havas-newman-1980.md`).
    - Use the [[paper-summary]] template verbatim — body sections in order: Abstract, TL;DR, Problem, Approach, Key result, Assumptions, Limitations / scope, Replication evidence, Why this paper matters, Quotes, Open questions surfaced, Related material in vault.

15. **Apply 6-axis tags + mirror domain/status to frontmatter properties.**
    - Mandatory tags: `#agent/research`, `#user/<invoker-handle>`, `#domain/<one>`, `#topic/<one>` × N, `paper`, `#status/draft`.
    - Optional tag: `#project/<name>` if scoped to a named project.
    - **Mandatory frontmatter properties** (alongside the tags — Bases queries the property layer, not the tag layer): `domain: <one>` (must mirror the `#domain/*` tag) and `status: draft` (must mirror the `#status/*` tag). **Without these properties, the note shows up under "None" in Bases "By domain" / "By status" views even when the tags are correct.** F12.1/F12.2 backfill caught this bug across 20 AI-in-Math papers; refined doctrine in [[naming-conventions]] § Properties not just tags.

16. **Update any concept hubs.** For each concept linked, add the current paper to the hub's `appears_in: []` frontmatter.

17. **Verify outgoing wikilinks before saving.** The note must have at least 3 outgoing wikilinks in its "Related material in vault" section (drawn from frontmatter `extends` / `contradicts` / `replicates` / `cites` / `cited_by` / `key_concepts` plus any manually-added context). A paper with zero outgoing links is orphan-on-creation and not ready to save — go back and identify what it actually connects to in the vault. If genuinely zero connections exist (no concept hubs, no cited papers in vault, no related work), the paper is likely the first of a new sub-topic; flag to the invoker before saving and ensure at least a parent overview / domain landing-page link is present.

    **Also verify no `[[<placeholder>]]` syntax leaked into the body** from copying template text. Grep the note for `\[\[<` — if any matches, wrap each in backticks ( `` `[[<placeholder>]]` `` ). Bare `[[<...>]]` is parsed as a real wikilink by Obsidian and creates phantom orphan nodes in the graph view (see [[paper-summary]] § Notation conventions and the convention files for the rule).

18. **Report back.** Tell the invoker:
    - Path to the new note
    - Topic tags applied
    - Concept hubs created or updated
    - Open questions surfaced
    - Any blockers

## Common errors to avoid

- **Inventing relevance.** No "applies to <project>" sections unless the invoker provided a project-context brief.
- **Inventing quality verdicts.** `quality_notes` empty is fine; only fill it when you have something specific to say.
- **Paraphrasing the abstract.** Abstract is verbatim copy (or verbatim translation). The TL;DR is your distillation, not the abstract.
- **Tag-stuffing.** Every `#topic/*` must pass the substance test.
- **Singleton concept hubs.** Don't create `Concepts/<X>.md` for concepts that only appear in one paper.
