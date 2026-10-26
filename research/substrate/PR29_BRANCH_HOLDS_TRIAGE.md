# PR #29 triage rows that are not the current ledger

PR #29 (`f2b1c27eb9a9bd3776e3e451e714a04e4f262ddf`, branch `cursor/research-substrate-audit-081d`) is not a merge candidate. Its base is `ingest/drive-history-v1` at `ffd4ec2c`, not `main`. Merging it onto `main` conflicts, and the copy of `scripts/query_source_history.py` on that branch would drop the later exclusion of the queried id from `family_live`.

The audit narrative and the ported queries are already on `main`:

- `research/substrate/RESEARCH_SUBSTRATE_AUDIT_2026-10-05.md` is the snapshot, with a banner that it is not the current verdict.
- `research/substrate/RESEARCH_SUBSTRATE_AUDIT_2026-10-05-MAIN.md` is the addendum after PR #25 and PR #30.
- PR #31, PR #36, and PR #40 carried the recommended fixes that were actually done. Open archive gaps that the audit named and that are still open (revision bodies, an uninvented manuscript order, Season 3 directory headings) remain in the main gap ledger. They are not new work created by this note.

What `main` does not contain is the pre-admission `candidate_triage.jsonl` from that branch (132 rows). The regenerated ledger on `main` has 99 rows and does not keep the dropped candidates' `basis` lines. Those lines are not an ingest mandate. Containers that were later admitted should be read from the catalog, not from the old "not yet a container" status.

PR #29 was closed without merge on 2026-10-26. Keep the branch. Do not delete it to tidy the queue. If a later edit needs one of those `basis` sentences, copy that sentence onto the admitted source's own record and cite `f2b1c27`. Do not recreate the 132-row ledger on `main`.
