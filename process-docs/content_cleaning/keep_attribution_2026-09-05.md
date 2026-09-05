# Keep Speaker Attribution and Date, Add GitHub Role (2026-09-05)

Process record for reversing part of `strip_noise`/`strip_comments_noise`'s original behavior:
`Author:`/`Date:` (comments) and `Author:`/`Created:` (issue body) have been dropped since the
tool's first day; they are now kept, and `Author:` gains the commenter's GitHub role next to the
login. Future fetches only — no corpus re-fetch, no reindex, nothing in the live corpus changed.

## Decision

Same premise as the same day's build-log warning-protection fix: content and context have
priority. Speaker attribution and date are context a searcher needs to judge a comment (who said
this, when, with what standing in the repo) — not noise. `Updated:`/`Branch:`/`Commits:`/
`Changed Files:`/`Mergeable:`/`URL:`/`Comments:` are unaffected and stay stripped; the `[bot]`
drop, the quote strip, and the class-F/class-G branches stay exactly as they are.

## `author_association` — confirmed present, not assumed

Read `get_issue.py` and `get_issue_comments.py` first; neither module's docstrings or existing
code mentioned `author_association`, so its presence was verified directly against the real API
before writing any code, per this project's evidence-first methodology — never invented, never
assumed from memory of the GitHub API's general shape:

```
fetch_issue('anthropics', 'claude-code', 1)['author_association']       -> 'COLLABORATOR'
fetch_comments('anthropics', 'claude-code', 1)[0]['author_association'] -> 'NONE'
```

Both `GET /repos/{o}/{r}/issues/{n}` and `GET /repos/{o}/{r}/issues/{n}/comments` carry
`author_association` as a top-level field, alongside `user`. Real values observed across several
issues while picking test candidates: `OWNER`, `MEMBER`, `COLLABORATOR`, `CONTRIBUTOR`, `NONE`.
Present in both payloads identically — no module-specific gap to report.

## Changes

- `get_issue.py::format_issue` — `Author: {login}` → `Author: {login} ({author_association})`.
- `get_issue_comments.py::format_comments` — same change, per comment.
- `index_issues.py::strip_noise` — `"Author:"` and `"Created:"` removed from `METADATA_PREFIXES`;
  the rest of the tuple unchanged.
- `index_issues.py::strip_comments_noise` — the `elif line.startswith('Author:') or
  line.startswith('Date:'): continue` branch removed entirely; those lines now fall through to
  the existing `else: out.append(line)`, no new branch needed.
- `CLEANING_VERSION` (`raw_logging.py`) bumped: `"2026-09-05-protect-warning"` →
  `"2026-09-05-keep-attribution"`.

## A break found and fixed while implementing: the `[bot]` check

`strip_comments_noise`'s bot-comment drop identified a bot author by `author_line.rstrip().
endswith('[bot]')` — correct when the line was `Author: some-app[bot]`, but broken by the new
format: `Author: some-app[bot] (NONE)` no longer *ends* with `[bot]`, it ends with the role
parenthetical. This was caught by reasoning through the change before testing, then confirmed by
reading `strip_comments_noise` in full — not something a shallow diff would have surfaced. Fixed
by checking for the substring `'[bot] ('` (the login's `[bot]` suffix immediately followed by the
new role-parenthetical's opening paren) instead of a line-ending match. Verified against a real
bot comment, not a synthetic one: `anthropics/claude-code#30677` has a `github-actions[bot]`
comment (confirmed present in the raw fetch, confirmed absent after `strip_comments_noise`) with
`author_association: NONE` and `user.type: Bot` in the raw payload — the fix correctly drops it
under the new Author-line format. `user.type == 'Bot'` would be an equally valid, arguably more
robust bot-detection signal, but was not adopted: it would require emitting a new field the
milestone did not ask for, whereas the substring fix keeps the existing mechanism's shape and
scope, just adapted to the line format it now has to parse.

Also verified: the `[bot]`-lookahead itself (which scans forward from a `--- Comment N ---`
separator for the first `Author:` line to classify the block) only *reads* that line — it does not
depend on whether the line is later stripped or kept, so it needed no change beyond the suffix
check above. `_is_automated_only_comment()` (class G) keeps its own internal `Author:`/`Date:`
skip when classifying whether a comment reduces to solely the automated marker — that is
classification logic, separate from the strip's output, and is untouched, per this milestone's
explicit scope.

## Real-API test (three issues, no corpus/index touched)

A one-shot script (worktree root, not `dev/`, not staged) called the same chain
`index_issues_workflow` calls — `get_issue_workflow` → `get_issue_comments_workflow` →
`strip_noise`/`strip_comments_noise` → `strip_generic_noise` → `strip_build_logs` →
`build_issue_md` — skipping `search_raw`/`run_index`/`get_collection_stats`, for three issues
picked from repos already in the corpus and verified live (before picking) to have several
comments including a maintainer reply:

- `anthropics/claude-code#22172` — 9 comments, 8× `NONE` + a `COLLABORATOR` (`bcherny`) closing reply.
- `ghostty-org/ghostty#10406` — 5 comments, 4× `MEMBER` (`jcollie`) + a `CONTRIBUTOR` (`mitchellh`) reply.
- `ghostty-org/ghostty#10773` — 3 comments, `CONTRIBUTOR`/`CONTRIBUTOR`/`MEMBER` (`jcollie`) reply.

Output MDs (read directly, not just generated): all three show `Author: {login} ({ROLE})` on the
issue body line and on every comment, `Created:`/`Date:` lines present, no `[bot]` comment leaked
through (separately re-confirmed against a real bot comment in `anthropics/claude-code#30677`,
above). Written only to
`/private/tmp/claude-501/-Users-brunowinter2000-Documents-ai-Meta-ClaudeCode-cli-gh-cli/
caa897d1-7ce3-4e9c-86a2-112716079599/scratchpad/fetch_test/` — never to `RAG_DOC_DIR`, `run_index`
never called. The one-shot script itself was deleted after the run, per this project's convention
for uncommitted one-shot scripts.

Confirmed separately: the live `github_issues` corpus directory's file count and the three
existing corpus files for these same issue numbers (`claude-code__22172.md`, `ghostty__10406.md`,
`ghostty__10773.md`) are untouched — they still show the old `Author: {login}` format (no role),
exactly as this milestone's "future fetches only" scope requires.

## Artifacts

- `src/github/get_issue.py`, `src/github/get_issue_comments.py` — `Author:` line format changed.
- `src/github/index_issues.py` — `strip_noise`/`strip_comments_noise` keep Author/Date/Created;
  `[bot]` check adapted to the new Author-line format.
- `src/github/raw_logging.py` — `CLEANING_VERSION` bumped.
