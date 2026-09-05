# Automated Version-Removal Comment Strip (Class G) + Corpus Re-Clean Dry-Run (2026-09-05)

Process record for wiring junk class G (AUTOMATED_COMMENT, from the junk-class inventory in this
area) into `strip_comments_noise`, extending `07_reclean_migration_headers.py` to remove it too.
No `--apply` was run and the RAG index was not touched. Builds directly on the class-F work
earlier this same day: see this area's earlier entry for the F anchors and pipeline placement this
milestone reuses.

## What class G looks like, read from the real files

Grepped `automated comment` across the whole live corpus (963 files): exactly 5 occurrences, one
each in `pyobjc__44/76/77/175/176.md`, always the literal text `Removing version: X (automated
comment)` (X observed: 2.4, 2.5, 3.0, 3.1), zero elsewhere. In every one of the 5, the exact
structure (confirmed by direct inspection, not assumed) is:

```
--- Comment N ---
(blank)
**Original comment by NAME (...).**        <- class F header
(blank)
----------------------------------------   <- class F rule
(blank)
Removing version: X (automated comment)     <- class G marker
[optional trailing blank]
[EOF or next separator]
```

In all 5 files this is the last comment (comment 2/2/2/3/5/11 depending on file), though the
detection built here does not depend on position — it depends on the comment's content collapsing
to solely the marker.

## Anchor and drop mechanism

`AUTOMATED_COMMENT_RE = r'^Removing version: .+ \(automated comment\)$'`, anchored on the literal
`(automated comment)` marker exactly as the corpus shows it — not widened to catch any
`Removing ...` line or any parenthetical marker.

The drop is whole-comment, not line-level: at each `--- Comment N ---` separator,
`strip_comments_noise` now also looks ahead to the next separator (or end of text) and calls a new
helper, `_is_automated_only_comment(block)`, which filters `Author:`/`Date:` lines, blank lines,
and — critically — a nested class-F triplet (the same 3-line adjacency check the F-branch already
uses), then checks whether exactly one line remains and whether that line matches
`AUTOMATED_COMMENT_RE`. If true, a new `in_automated_block` flag (structured exactly like the
existing `in_bot_block` flag: set at the separator, causes the separator itself and every
subsequent line up to the next separator to be skipped) drops the whole comment — separator, blank
lines, the nested F header/rule, and the marker line together. Verified directly: for all 5 named
files, the `--- Comment N ---` count in the cleaned output is exactly one less than in the raw
input, confirming the separator itself (not just the marker) is gone.

## Why the F-branch and `[bot]`-block logic don't interact badly with this

The `elif` chain order in `strip_comments_noise` is: separator handling (sets `in_bot_block` and
`in_automated_block`) → `elif in_bot_block: continue` → `elif in_automated_block: continue` →
`elif` class-F header check → `Author:`/`Date:` strip → `> ` quote strip → append. Because
`in_automated_block` is checked before the class-F branch, once a comment is classified as
automated-only, every line inside it — including its own nested class-F header and rule — is
consumed by the `in_automated_block` skip and never reaches the F-branch at all. The F-branch's own
3-line lookahead therefore never fires on lines already being dropped by G, and there is no
double-processing or index-arithmetic conflict between the two branches. This holds identically
whether the input is the current corpus (F still present, since `07 --apply` has never run) or a
future raw fetch (same function, same single pass — F would be encountered inline exactly as it is
today, except now some of those encounters happen inside an already-in_automated_block region and
get skipped before the F-branch ever sees them).

Verified directly with synthetic input covering all four existing behaviors plus the new one in a
single test: a `[bot]`-authored comment (block fully dropped, unchanged from before), a comment
with a `> ` quoted reply line (quote dropped, real content kept, unchanged from before), a plain
comment with `Author:`/`Date:` lines and no migration header (metadata stripped, content kept,
unchanged from before), and a comment carrying a full class-F header + rule + the class-G marker
as its only content (the entire comment — separator included — dropped). All four behaviors fired
exactly as expected in one pass. A second synthetic case confirmed the anchor is not over-wide: a
comment with class-F header + rule + **two** content lines, the second of which happens to be the
literal G marker text, is correctly left alone (multi-line body fails the "exactly one line
remains" check), so a genuine reply that happens to quote or mention the marker text is not at
risk of being swallowed.

## CLEANING_VERSION

Bumped in `src/github/raw_logging.py`: `"2026-09-05-strip-migration-header"` →
`"2026-09-05-strip-automated-comment"` (same day as the class-F work, per the existing convention
that any change to `strip_noise`/`strip_comments_noise` gets a new version string).

## Dev re-clean script: extending `07_reclean_migration_headers.py`

The script works by finding removable line-spans and splicing them out of the whole already-built
MD text (not a line-state-machine like the src pipeline), so class G needed a genuinely different
detection strategy than a straight port of the src logic: `_find_automated_comment_blocks()` scans
for `--- Comment N ---` separators, looks ahead to the next separator, and reuses
`_is_automated_only_comment()` (an intentional verbatim copy of the src helper) to decide whether
the whole span — separator through the line before the next separator or end of text — qualifies.

A class-G span always fully contains its own nested class-F span (the corpus confirms this in all
5 cases: `_find_migration_blocks()`'s F span for that comment's header sits entirely inside the G
span's line range). The block-splicing approach does not get the "don't double-process" protection
the src state machine gets for free from `elif` ordering, so `_find_all_blocks()` explicitly
excludes any F span that is fully nested inside a G span before combining the two lists — without
this, the nested F span would be listed and spliced a second time, corrupting both the output text
and the per-class totals. Verified directly: for every changed file in the dry-run, no two spans in
the combined, sorted block list overlap (checked by asserting each span's end line is strictly
before the next span's start line, across all 7 changed files).

The report format was extended, not replaced: the summary table now has Total/Class F/Class G
columns, the per-file table has separate F-span and G-span counts, and every entry in the verbatim
"Removed Spans" dump — both classes — carries a `[F]`/`[G]` tag on its identification line so the
class of each removed span is visible without cross-referencing the summary.

## Dry-run numbers (2026-09-05)

Corpus: 963 files. `07_reclean_migration_headers.py --source-dir <corpus>` (dry-run, no `--apply`):

- Files that would change: **7 / 963** — the same 7 pyobjc files as the class-F-only dry-run
  earlier this session (class G never introduces a new affected file; every G occurrence is inside
  a file that already had at least one F occurrence).
- Spans: **36 total** (**31 class F**, **5 class G**). The G set is exactly `pyobjc__175.md`,
  `pyobjc__176.md`, `pyobjc__44.md`, `pyobjc__76.md`, `pyobjc__77.md` — confirmed by direct set
  comparison against the expected 5 filenames: exact match. `pyobjc__31.md` and `pyobjc__34.md`
  show F spans only (5 and 3 respectively), 0 G spans each, matching the corpus fact that neither
  file contains an automated-comment occurrence.
- Lines removed: **131 total** (**93 F**, **38 G** — a class-G span is a whole comment, several
  lines longer than the 3-line class-F triplet it contains, so per-span line counts are not
  comparable 1:1 across classes).
- Chars removed: **7,942 total** (**6,568 F**, **1,374 G**).
- The 31 remaining F spans plus the original 36 F-only spans from the earlier class-F dry-run
  reconcile exactly: 36 − 5 = 31, i.e. every class-G comment "used up" exactly one of the class-F
  occurrences counted in the earlier, class-F-only run (its own nested header), and no other F
  count changed.
- `pyobjc__610.md` (native GitHub issue, not migrated) confirmed absent from both the F set and
  the G set — unaffected, as in the class-F milestone.

## Artifacts

- `src/github/index_issues.py` — `_is_automated_only_comment()` added, `strip_comments_noise`
  gained the `in_automated_block` branch, `AUTOMATED_COMMENT_RE` added.
- `src/github/raw_logging.py` — `CLEANING_VERSION` bumped.
- `dev/content_cleaning/07_reclean_migration_headers.py` — extended with class-G detection
  (`SEP_RE`, `AUTOMATED_COMMENT_RE`, `_is_automated_only_comment`,
  `_find_automated_comment_blocks`, `_find_all_blocks`), the combined strip function renamed
  `strip_migration_and_automated`, report format extended to split F/G, backup dir naming
  generalized to `_PRE_MIGRATION_NOISE_STRIP_BACKUP_<timestamp>`.
- `dev/content_cleaning/md/07_reclean_dryrun_20260905_190609.md` — the dry-run report behind the
  numbers above, including the verbatim, class-tagged text of all 36 removed spans.
