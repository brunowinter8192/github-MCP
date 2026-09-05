# Class F + G Reindex of github_issues (2026-09-05)

Process record for the reindex that followed the one-and-only `--apply` run of
`dev/content_cleaning/07_reclean_migration_headers.py` (recorded in this area's apply entry of the
same date). Run by the orchestrator directly with `rag-cli index --collection github_issues`, in a
single invocation with a generous timeout, per this area's lesson from the 2026-08-28 reindex.

## Before

Collection total: **5,260 chunks**. Per pyobjc file, queried via `rag-cli list_documents`:
`pyobjc__175.md`=13, `pyobjc__176.md`=10, `pyobjc__31.md`=4, `pyobjc__34.md`=108,
`pyobjc__44.md`=7, `pyobjc__76.md`=2, `pyobjc__77.md`=4, `pyobjc__610.md`=10.

## Run

One invocation, completed cleanly. Summary line: `Done: 7 files indexed (141 chunks), 956 skipped,
0 adopted`. The 7 indexed files are exactly the 7 rewritten by the apply; `pyobjc__610.md` was
skipped (hash unchanged). For every one of the 7 the indexer printed `Deleted N existing chunks`
with N equal to the before-count above, then `Indexed M/M chunks` — delete-then-insert, no
accumulation, no lock contention, no retry needed.

## After

Collection total: **5,253 chunks** (−7). Per file: `pyobjc__175.md`=12, `pyobjc__176.md`=9,
`pyobjc__31.md`=3, `pyobjc__34.md`=107, `pyobjc__44.md`=5, `pyobjc__76.md`=2, `pyobjc__77.md`=3.
Sum over the 7 files: 148 → 141.

The small delta is expected: the strip removed 7,942 chars spread over 36 short spans, mostly
3-line headers, so few files lost a whole chunk. The retrieval effect is the one the inventory
named, not a size effect: the first content chunk of every migrated pyobjc issue no longer opens
with the Bitbucket attribution line, and the 5 "Removing version" comments no longer exist as
chunks at all.

## Result

As of 2026-09-05 the `github_issues` corpus and index carry no class-F headers and no class-G
comments. Together with the build-log strip of 2026-08-28 (this area), all three goals of the
Residue issue are met: build/terminal output, tracker-migration headers, and automated
version-management comments are stripped for future fetches, and the pyobjc files already in the
corpus meet the same standard.
