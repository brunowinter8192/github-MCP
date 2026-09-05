# Fix: strip_build_logs Swallowed a Warning Line — Protection + Cost + Restore Dry-Run (2026-09-05)

Process record for a real content-loss finding in the already-applied build-log strip, the
protection fix, its measured cost against the pre-strip backup, and the dry-run that reconstructs
the 8 affected files under the fix. No file in the live corpus was modified — the restore is a
dry-run only, awaiting separate approval to `--apply`.

## The finding

Reading the 8 build-log-stripped files against `github_issues_PRE_BUILDLOG_STRIP_BACKUP_20260828_230949/`
(the only surviving pre-strip record for these files) found one real content loss:
`MinerU__1418.md` backup line 282, `"WARNING: magic-pdf 0.6.1 does not provide the extra 'full'"`,
sits between a `Downloading ...` line and a run of `Requirement already satisfied: ...` lines —
both matched `SIGNAL_PATTERNS` — and got bridged over (`BRIDGE_GAP = 3`) because it matched neither
`ERROR_RE` (no `error`/`fatal`/`traceback`/`exception`/`failed` substring) nor any other protected
pattern. The project premise going forward: content and context have absolute priority, only pure
noise is ever removed, and a warning is content — never noise — even sitting inside an otherwise
disposable pip/build run.

## The fix

`ERROR_RE` in `src/github/text_cleaning.py` gained `warning` as a sixth keyword, folded into the
same regex as `error`/`fatal`/`traceback`/`exception`/`failed` (not a new separate constant) — a
line containing "warning" (case-insensitive) is now protected, never signal, never bridged, always
breaks a run, exactly like the other five keywords. Verified directly: `_is_protected()` now
returns `True` for the `MinerU__1418.md` line, and it survives `strip_build_logs()` intact.

Three `SIGNAL_PATTERNS` entries became dead code and were removed, not left contradicting the new
protection:
- `^\s*warning: no (directories|files|previously-included files) found matching`
- `^\s*clang: warning:`
- `^\d+ warnings? generated\.$`

One entry was narrowed rather than removed: the compiler-diagnostic header pattern
`^\s*\S+\.(c|cc|...):\d+:\d+:\s*(warning|note):` matched both compiler warnings and compiler
notes. Its `warning` alternative is now unreachable (any such line already contains "warning" and
is protected before `SIGNAL_PATTERNS` is even checked), so it was narrowed to `note:` only — a
compiler note is not a warning and stays live.

The change was made identically in `src/github/text_cleaning.py` and both dev copies
(`dev/content_cleaning/05_strip_build_logs.py`, `dev/content_cleaning/06_reclean_build_logs.py`),
then verified byte-identical across all three for the shared `ERROR_RE`/`SIGNAL_PATTERNS` block
(direct string comparison, not visual inspection). `06`'s safety-assertion report text was updated
to list `warning` alongside the other four protected keywords, since the assertion now checks
against the expanded `ERROR_RE`. `CLEANING_VERSION` in `src/github/raw_logging.py` bumped:
`"2026-09-05-strip-automated-comment"` → `"2026-09-05-protect-warning"`.

## Cost measurement on the PRE_BUILDLOG backup

Ran the fixed `06_reclean_build_logs.py --source-dir <PRE_BUILDLOG backup>` (873 files, the
pre-strip state of every file the 2026-08-28 build-log strip ever touched or could have touched):
**8 files affected, 51 blocks, gross 310,370 / net 308,431 chars** — versus the original applied
run's 8 files / 56 blocks / 333,184 gross chars. A separate one-shot analysis (not committed;
computed by running the old, pre-fix detection logic and the new, fixed logic side by side over
the same 873 files) found every line that was in an old removed block but is in no new block —
**352 lines newly kept**, across 5 of the 8 files (`MinerU__1418.md`: 4, `MinerU__2262.md`: 2,
`MinerU__826.md`: 1, `curl_cffi__74.md`: 11, `pyobjc__34.md`: 334; `ghostty__2210.md`,
`pyobjc__175.md`, `pyobjc__176.md`: 0 each — their build-log blocks never happened to contain a
warning line). All 352 were read in full: the overwhelming majority (334, in `pyobjc__34.md`) are
`clang`/compiler diagnostic warnings (`"implicit conversion loses integer precision"`,
`"argument unused during compilation"`) plus their wrapped continuation/source-context lines and
`"N warnings generated."` summary lines, now kept as a coherent unit around each warning; the
`MinerU`/`curl_cffi` cases are pip's own `WARNING: ... does not provide the extra 'full'` and
`warning: no files found matching '...'` lines. All are genuine content, matching the fix's intent
exactly — no unexpected inclusions.

Report artifacts: `dev/content_cleaning/md/06_reclean_dryrun_20260905_204023.md` (the standard
06-format report, old-vs-new totals) and
`dev/content_cleaning/md/warning_protection_cost_20260905_204054.md` (the custom diff report with
every newly-kept line listed verbatim per file).

## Restore dry-run: `dev/content_cleaning/10_restore_build_log_files.py`

For each of the 8 files, reconstructs the expected live state under the fix: PRE_BUILDLOG backup
version → fixed `strip_build_logs()` → class F+G strip (an intentional verbatim copy of
`07_reclean_migration_headers.py`'s logic — needed because the 3 pyobjc files in the backup
predate the 2026-09-05 F/G milestone and still carry that noise; the 5 non-pyobjc files pass
through this step as a no-op since neither anchor matches) → diff against the current live file.

The diff excludes placeholder lines from comparison before running `difflib.SequenceMatcher`: a
placeholder's wording and count are expected to change under the fix (fewer lines removed per
block, or a block splitting in two around a newly-protected line) — that is not "content" that
could regress, so comparing raw placeholder text would manufacture false "unexpected difference"
noise on every single changed file. Every remaining opcode is classified: `insert` (lines present
in the reconstruction but not live — the expected, newly-kept warning content) is reported as
"added back"; `delete`/`replace` (real content missing or changed) is reported as "unexpected" and
would refuse `--apply`.

Dry-run result: **5/8 files changed, 352 lines added back, 0 unexpected differences** across all 8
files — the added-back count and per-file breakdown match the cost measurement above exactly, and
`pyobjc__175.md`/`pyobjc__176.md` (0 lines added back) reconstruct to be byte-identical to their
live counterparts, confirming the class-F/G verbatim copy correctly reproduces the current live
state on top of the fixed build-log strip. Report:
`dev/content_cleaning/md/10_restore_dryrun_20260905_204243.md`.

**`--apply` was not run.** It is implemented (backs up the live corpus dir to
`<corpus>_PRE_WARNING_RESTORE_BACKUP_<timestamp>` then overwrites only the 8 files, refusing if
any file shows an unexpected diff) but awaits separate approval on this dry-run before executing.

## Artifacts

- `src/github/text_cleaning.py` — `ERROR_RE` gained `warning`; three dead `SIGNAL_PATTERNS`
  entries removed, one narrowed to `note:` only.
- `src/github/raw_logging.py` — `CLEANING_VERSION` bumped.
- `dev/content_cleaning/05_strip_build_logs.py`, `dev/content_cleaning/06_reclean_build_logs.py` —
  same change applied verbatim; `06`'s safety-assertion report text updated to mention `warning`.
- `dev/content_cleaning/10_restore_build_log_files.py` — new restore script (dry-run only, not
  applied).
- `dev/content_cleaning/md/06_reclean_dryrun_20260905_204023.md`,
  `dev/content_cleaning/md/warning_protection_cost_20260905_204054.md`,
  `dev/content_cleaning/md/10_restore_dryrun_20260905_204243.md` — the reports behind the numbers
  above.
