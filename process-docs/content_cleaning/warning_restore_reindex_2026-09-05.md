# Warning-Protection Restore — Reindex of github_issues (2026-09-05)

Process record for the reindex after the warning-protection restore of the same date (this
area's warning-protection entry). Run by the orchestrator with one `rag-cli index --collection
github_issues` invocation, generous timeout, no retry.

## Before

Collection total: **5,253 chunks** (the state after the class F+G reindex earlier the same day).
Per restored file: `MinerU__1418.md`=1, `MinerU__2262.md`=5, `MinerU__826.md`=9,
`curl_cffi__74.md`=44, `pyobjc__34.md`=107 — sum 166.

## Run

`Done: 5 files indexed (183 chunks), 958 skipped, 0 adopted`. Exactly the 5 files the restore
rewrote; each printed `Deleted N existing chunks` with N equal to the before-count, then indexed
its replacement — delete-then-insert, no accumulation.

## After

Collection total: **5,270 chunks** (+17). Sum over the 5 files: 166 → 183. The growth is the 352
restored lines, 334 of them compiler warnings with source context in `pyobjc__34.md`.

## Context check that triggered this work

As of 2026-09-05 all 8 build-log-stripped files and all 7 migration-stripped files were read
against their backups for context integrity. 14 of 15 were intact. The one loss — `WARNING:
magic-pdf 0.6.1 does not provide the extra 'full'` bridged over inside a pip run — turned out to
exist in three MinerU files, not one, and is now restored in all three. The class-F/G strip lost
no content, but it removed the per-comment speaker attribution that the migration header carried
(reporter vs. maintainer); whether that attribution returns, for pyobjc alone or for all repos via
the `Author:` line, was left open at this date.
