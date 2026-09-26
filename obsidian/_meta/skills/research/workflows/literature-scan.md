# Workflow — Literature Scan

Use when the invoker asks a topic-level question without specific URLs ("research recent work on X", "what does the literature say about Y"). Researcher proposes candidate sources, the invoker approves, then proceeds to batch ingest.

## Steps

### Phase 1 — Scoping (with invoker)

1. **Restate the question in one sentence.** Ambiguous → ask the invoker to clarify before any web searches.

2. **Check the vault for prior coverage.**
   - `grep -r "<topic-keywords>" Obsidian/Math/Research/`
   - List any existing notes on the topic. Often the answer is "already covered" or "covered partially — here's what's missing."

3. **Propose 3-7 candidate sources** to the invoker.
   - Mix journals / arxiv / textbook citations.
   - Note year + author affiliation. Recent ≠ better — include foundational papers if relevant.
   - Skip anything without an experimental section or proof.
   - Format: numbered list, one line per source with author + year + venue + one-line claim.

4. **Wait for invoker approval.** They may add, remove, or reorder. **Don't start fetching until they confirm.**

### Phase 2 — Read & extract (approved sources)

Run the [[batch]] workflow on the approved source list.

### Phase 3 — Synthesize

Write `Research/<domain>/_synthesis-<topic>.md` via [[synthesis]] template:

- **The question** — verbatim from Phase 1.
- **Sources reviewed** — numbered list with wikilinks to each paper note and a one-line takeaway.
- **Convergence** — what do sources agree on? Cite which paper(s) support each agreed point.
- **Disagreement** — where do sources disagree, contradict, or leave gaps?
- **What's settled** — claims the literature has converged on. Safe to build on.
- **What's contested** — claims still in tension. Building on these is risky.
- **What's open** — questions the literature has not yet attempted or attempted only inconclusively. Concrete pointers, not vague.
- **Methodology notes** (if applicable) — systemic concerns across the body of work (benchmark biases, replication gaps, statistical practices).
- **Recommendation** — Researcher's editorial: what should the next action be?

### Phase 4 — Report

Tell the invoker:
- Path to the synthesis note
- Paths to all paper notes covered
- Concepts hubs created or updated
- Top 1-3 open questions worth routing to an Experimenter or Validator

## Common errors to avoid

- **Scope creep.** If the invoker asked about X, don't drift into adjacent topic Y. Note the adjacency in the synthesis but don't pad the source list.
- **Padding.** If only 2 sources are actually relevant, return 2. Don't pad to 5 with weak sources.
- **Sales prose.** "This paper is groundbreaking" — only if the citation count or replication evidence backs it. Use `quality_notes` discipline.
- **Inventing settled claims.** "What's settled" must cite the supporting papers in the synthesis. Without citations, it's "what I think is true."

## Stop conditions

- Literature on the topic is sparse → say so explicitly in the synthesis. Don't pad. Recommend "no synthesis warranted yet — re-scan in N months" if appropriate.
- Literature is contradictory and the disagreement is unresolved → write the synthesis with the disagreement front-and-center. Don't pretend there's consensus.
