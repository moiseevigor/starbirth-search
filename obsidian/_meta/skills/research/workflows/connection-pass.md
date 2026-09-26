# Workflow — Connection Pass (re-link existing notes)

Use when the invoker wants to retag, re-link, or restructure existing paper notes — no new ingest. Common triggers:

- The taxonomy changed (new mandatory axes, new domain values).
- A batch of papers landed and the cross-paper graph wasn't fully populated.
- A new concept hub should be created retroactively across existing papers.
- Old notes use a deprecated template and need to be migrated.

## Steps

1. **Confirm scope.** Ask the invoker:
   - Which subset? (e.g. "all `#domain/group-theory` papers", "everything under `Research/AI in Math/`", "papers added in the last 2 weeks")
   - Which kind of pass? Retag / re-link / migrate-template / all of the above.
   - Approve at most ~20 notes per pass for token discipline. If the scope is wider, break into multiple passes.

2. **Enumerate the notes in scope.** `find` or `Glob` the relevant dir; list the paths back to the invoker before touching anything.

3. **For each note in scope:**
   - **Read** the current note.
   - **Compare against current template** (`<vault>/_templates/paper-summary.md`). Identify missing frontmatter fields, missing body sections, deprecated fields to drop.
   - **Re-derive topic tags** if doing a retag pass. Apply substance test. Reuse existing topic tags before inventing new ones.
   - **Re-derive connections** if doing a re-link pass. Grep the vault for citation relationships; populate `extends` / `contradicts` / `replicates` / `cites` / `cited_by`.
   - **Update body sections** if doing a template migration. Order must match the current paper-summary template.
   - **If source is non-English and original-language text exists in the note**: translate to English, mark with `[trans.]`, remove the original-language text (per current convention).
   - **Update the note in place.** Preserve `author:` and `#user/<handle>` — never strip authorship.
   - **Log the diff** to `Agents/<invoker-handle>/Researcher/log.md`: before-tags → after-tags, before-sections → after-sections.

4. **Sweep concept hubs:**
   - For every concept newly linked via `key_concepts` in the updated notes, ensure the `Concepts/<concept-name>.md` hub exists.
   - For every existing concept hub, refresh its `appears_in:` from the current state of paper notes.

5. **Sweep bidirectional links:**
   - For every `cites: [[X]]`, verify `X` has the current paper in its `cited_by:`. Add if missing.
   - Same for `extends`, `replicates`, `contradicts`.

6. **Stale notes:**
   - Notes that don't fit the new template AND aren't worth migrating (e.g. one-pager fragments, stubs) → tag with `#status/superseded` and flag to invoker. Do not silently delete or restructure beyond what the brief covers.

7. **Report back to invoker:**
   - Notes updated (paths + before/after diff summary)
   - New concept hubs created
   - Bidirectional links repaired
   - Stale notes flagged
   - Any patterns observed across the batch worth surfacing (e.g. "8 of these papers all cite Hall 1957 — worth a Concept hub")

## Token discipline

Connection passes can blow context fast. Rules:

- Process notes one at a time. Don't keep multiple full notes in context.
- After every ~5 notes, checkpoint with the invoker.
- Use `Read` with offset/limit if revisiting an earlier note for connection-graph reasons.
- Don't re-fetch source URLs unless absolutely necessary (the existing note's content is the source of truth for a connection pass; we're not re-summarizing).

## Stop conditions

- A note has no `author:` and no `#user/<handle>` → flag to invoker, ask who owns it. Don't guess.
- A note contradicts itself (e.g. body says X, frontmatter says ¬X) → flag, don't auto-resolve.
- A note appears to be intentionally outside the template (e.g. an old research log, not a paper summary) → leave alone, ask invoker whether it's in scope.

## Restructure authority

Researcher has restructure authority over `Research/` and `Concepts/` per [[_common]]. Connection passes are the main exercise of that authority. **Every restructure must be logged** to `Agents/<owning-user>/Researcher/log.md` with before → after.
