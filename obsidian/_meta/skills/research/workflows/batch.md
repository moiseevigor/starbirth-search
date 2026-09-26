# Workflow — Batch Ingest

Use when the invoker hands a list of paper URLs (typically 2-20) and wants each ingested as a separate summary.

## Sequencing

Process papers **sequentially**, not in parallel. Each paper's connection-graph frontmatter may reference earlier papers in the batch; processing one at a time lets you populate `cites` / `cited_by` / `extends` correctly.

## Steps

1. **Echo back the list.** Confirm count, ask whether to proceed with all or a subset.

2. **Identify the invoking user's handle.** Same as single-paper workflow step 3.

3. **Plan the read order.** Default = order given by invoker. Optional reorder if obviously useful (e.g. read foundational paper before its citations). Confirm with invoker if you reorder.

4. **For each paper, run the single-paper workflow** ([[single-paper]]):
   - Fetch, read, extract.
   - Look up citation count.
   - Identify domain + topics + concepts + connections.
   - Translate if non-English.
   - Write the note with full frontmatter and body.
   - Tag.
   - Update concept hubs.

5. **After each paper, do a cross-batch connection sweep:**
   - Does the just-finished paper cite, extend, contradict, or replicate any of the earlier papers in this batch?
   - If yes, update both papers' frontmatter (`cites` + `cited_by`, or `extends` on this one + nothing on the other, etc.).

6. **After all papers are written, sweep for concept hubs:**
   - List all concepts that appeared in 2+ papers in this batch.
   - For each: ensure a `Concepts/<concept-name>.md` stub exists (using [[concept-note]] template).
   - Update each hub's `appears_in:` with wikilinks to every paper in the batch that references it.

7. **Consider a synthesis note** if the batch coheres around a single topic.
   - If yes: write `Research/<domain>/_synthesis-<topic>.md` via [[synthesis]] template covering all papers in the batch.
   - If no: skip; the batch is just a collection.

8. **Report back.** Per paper: path + key topics. Plus:
   - New concept hubs created
   - Cross-batch connections found
   - Synthesis written (if any)
   - Open questions surfaced across the batch

## Token discipline

Batches can be expensive. If the batch is >10 papers:
- Process one paper, write it, then move on. Don't keep multiple papers' full text in context simultaneously.
- After every ~5 papers, do a brief checkpoint with the invoker ("processed 5/12, here's where we are"). Lets them course-correct early.
- Use `Read` with limited offset/limit if revisiting an earlier paper for connection-graph reasons.

## Stop conditions

- One paper fails to fetch → ask invoker whether to skip and continue, or pause.
- Multiple papers are duplicates of existing summaries → flag in batch report, ask invoker which to update vs. skip.
- Batch contains papers from a brand-new domain → register the domain in `_meta/tags.md` once, then proceed.
