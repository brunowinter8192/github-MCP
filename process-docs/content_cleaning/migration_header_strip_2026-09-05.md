# Tracker-Migration Header Strip (Class F) + Corpus Re-Clean Dry-Run (2026-09-05)

Process record for wiring junk class F (TRACKER_MIGRATION, from the junk-class inventory in this
area) into the `index_issues` pipeline for future fetches, plus a dry-run re-clean check against
the live `github_issues` corpus. No `--apply` was run and the RAG index was not touched.

## What class F looks like, read from the real files

All 7 files carrying this noise are the pyobjc issues migrated from Bitbucket to GitHub:
`pyobjc__175/176/31/34/44/76/77.md`. A migration script wrote a bold attribution line into the
issue body and into every migrated comment, always followed by a blank line then exactly 40
dashes, then a blank line, then the real content:

- Issue body, first content: `**[Original report](bitbucket_url) by NAME (Bitbucket: [..](..),
  GitHub: [..](..)).**` — with two variants observed in the corpus: `by Anonymous.**` (no
  Bitbucket/GitHub parens at all, `pyobjc__31.md`) and a GitHub-less form, `(Bitbucket: [..](..),
  ).**` (empty GitHub segment, `pyobjc__176.md`).
- Every migrated comment: `**Original comment by NAME (Bitbucket: [..](..), GitHub:
  [..](..)).**`.

All three variants end in `.**` regardless of what precedes it, so the anchor used
(`^\*\*\[Original report\]\([^)]*\) by .+\.\*\*$` for the body form,
`^\*\*Original comment by .+\.\*\*$` for the comment form, plus `^-{40}$` for the rule) covers all
observed shapes without being widened past them. `pyobjc__610.md` (a native GitHub issue, not
migrated) was grepped alongside the 7 and confirmed to contain zero matches of either header form
or the 40-dash rule — the only file in the same repo that must NOT be touched, and wasn't.

Grepping the whole live corpus (963 files as of this session) for the two header prefixes and the
40-dash rule turned up exactly these same 7 files and no others — the anchor is confirmed to fire
nowhere else in the corpus, which is the basis for calling it safe.

## Where the strip lives, and why

`strip_noise` (body) and `strip_comments_noise` (comments) in `src/github/index_issues.py` each
got one added branch: on encountering a line matching the relevant header regex, check that the
next line is blank and the one after that is the 40-dash rule, and if so skip all three lines.
Implemented via an `enumerate(lines)` loop plus a `skip_until` index sentinel (the pattern already
used implicitly by nothing else in these two functions, but needed here because both functions
were previously single-line-lookback-free; the sentinel is the smallest change that adds 3-line
lookahead without restructuring the existing per-line checks into a different loop shape).

The two functions needed two separate regexes (`MIGRATION_REPORT_RE` for the body form,
`MIGRATION_COMMENT_RE` for the comment form) because `strip_noise` only ever sees the body form
and `strip_comments_noise` only ever sees the comment form — putting a single combined regex in
both would have been strictly redundant, not more correct. `MIGRATION_RULE_RE` (the 40-dash rule)
is shared, since it is the same literal string on both sides.

## Why no change was needed elsewhere

`get_issue_comments.py`'s comment format (`--- Comment N ---`, `Author:`, `Date:`, blank, body,
blank) was read in full to confirm the migration header, wherever it occurs, is always the first
line of a comment's `body` field — never mixed into the `Author:`/`Date:` lines the existing strip
already consumes, so no interaction with the `[bot]`-block detector, the `Author:`/`Date:` strip,
or the `> ` quote strip was possible in either direction. Verified directly: a synthetic input with
a `[bot]` comment, a quoted-reply line, and a plain comment (no migration header) ran through the
patched `strip_comments_noise` and every one of those three behaviors fired exactly as before —
bot block fully dropped, quoted line dropped, `Author:`/`Date:` stripped, plain content untouched.

## CLEANING_VERSION

Bumped in `src/github/raw_logging.py`: `"2026-08-28-no-prose-guard"` →
`"2026-09-05-strip-migration-header"`, per the convention that any change to
`strip_noise`/`strip_comments_noise` gets a new version string so a raw/cleaned diff found later
can be attributed to the filter version that produced it.

## Dev re-clean script: `07_reclean_migration_headers.py`

Follows `06_reclean_build_logs.py`'s shape (dry-run default, `--apply` backs up the whole corpus
dir to a timestamped sibling before overwriting only changed files) but the anchors + removal
logic are an intentional verbatim copy of `src/github/index_issues.py`'s class-F branches, combined
into a single `strip_migration_header()` pass over the whole already-built MD rather than split
across body/comments — safe because the two anchor forms are mutually exclusive by content and
match nothing else in the corpus (confirmed above). Unlike `06`'s report (a metrics table only),
this report also dumps the verbatim removed text per span (`<file>:<start>-<end>` identification
line, then the text, nothing else), per the requirement that the whole removal be readable in one
pass — closer to `05_strip_build_logs.py`'s dump format than `06`'s, merged into one file since
there is no separate detection-only/apply-capable split needed for a change this small.

## Dry-run numbers (2026-09-05)

Corpus: 963 files (grown from 873 during ongoing use since the 2026-08-28 session).
`07_reclean_migration_headers.py --source-dir <corpus>` (dry-run, no `--apply`):

- Files that would change: **7 / 963** — exactly `pyobjc__175.md`, `pyobjc__176.md`,
  `pyobjc__31.md`, `pyobjc__34.md`, `pyobjc__44.md`, `pyobjc__76.md`, `pyobjc__77.md`. Confirmed
  by direct set comparison against the expected 7 filenames: exact match, no extra file, no
  missing file. `pyobjc__610.md` confirmed absent from the changed set.
- Spans removed: **36** (1 per issue body + 1 per migrated comment; matches the earlier grep
  count of 36 body/comment header lines and 36 dash-rule lines across the same 7 files).
- Lines removed: **108** (36 spans × 3 lines each — header, blank, rule).
- Chars removed: **7,628**.

These are the current, live-corpus figures — they differ from the junk-class inventory's earlier
row for class F (8 files, 38 lines, 6,425 chars) because that earlier ad-hoc scan predates this
session's corpus growth (844→963 files via ongoing `index_issues` use) and used a narrower,
manually-eyeballed count rather than the anchor built and run here. The corpus, not the earlier
estimate, is the number that stands.

## Artifacts

- `src/github/index_issues.py` — `strip_noise`/`strip_comments_noise`, class-F branches added.
- `src/github/raw_logging.py` — `CLEANING_VERSION` bumped.
- `dev/content_cleaning/07_reclean_migration_headers.py` — new re-clean script.
- `dev/content_cleaning/md/07_reclean_dryrun_20260905_185402.md` — the dry-run report behind the
  numbers above, including the verbatim text of all 36 removed spans.
