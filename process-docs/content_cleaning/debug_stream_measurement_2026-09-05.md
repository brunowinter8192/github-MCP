# Class B (DEBUG_STREAM) — Measurement + Vocabulary/Gate Proposal (2026-09-05)

Process record for re-measuring junk class B (app debug/log lines pasted from a terminal — not
build/install output, which is class A and already handled by `strip_build_logs`) on the current,
grown corpus, and for the vocabulary/gate proposal that measurement supports. Read-only throughout:
no detector, no strip, no production code. Follows this area's established methodology — read real
files, derive vocabulary from what is actually there, gate on a run/repetition property rather than
on line appearance, let the corpus decide.

## Why re-measure

The junk-class inventory in this area measured class B at 844 files (61 files, 2,199 lines,
214,916 chars, 3.09%), naming three example shapes. The corpus is now 963 files across 21 repos (2
new since that inventory). `dev/content_cleaning/08_audit_debug_stream.py` re-measured B from
scratch and — per this milestone's explicit instruction — the vocabulary below comes from reading
every file the measurement surfaced, not from re-quoting the inventory's three examples.

## Vocabulary derived from reading

**`ghostty_debug`** — `^(debug|info|warning)\([a-zA-Z_]+\):`. Example: `debug(app): mailbox
message=redraw_surface` (`ghostty__10406.md`, 96×, matching the inventory), `debug(glib): DEBUG:
Gtk: snapshot symbolic icon as recolored node` (`ghostty__10406.md`, 26×). Current corpus: **7
files, 1,135 lines, 91,110 chars** — `ghostty__10406.md`(702), `ghostty__10379.md`(337),
`ghostty__10432.md`(38), `ghostty__7987.md`(21), `ghostty__10957.md`(17), `ghostty__4632.md`(16),
`ghostty__12410.md`(4). All in the `ghostty` repo, none elsewhere.

**`playwright_pw`** — `^\s*pw:[a-z:]+`. Example: `pw:channel:event {` (`playwright__13156.md`, part
of a 393-line dump). This single anchor also covers the much more frequent `pw:browser` sub-shape
(991 corpus-wide occurrences of lines like `pw:browser [pid=289][out] Crash Annotation
GraphicsCriticalError: ...` and `pw:browser <launching> /path/to/chrome --disable-field-trial-config
...`), plus `pw:api`, `pw:protocol`, `pw:test*`. Current corpus: **27 files, 1,659 lines, 370,551
chars** — `playwright__13156.md`(393), `playwright__37199.md`(250), `playwright__33515.md`(209),
`playwright__27997.md`(165), plus 23 more, all in `playwright`.

**`loguru_narration`** — `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+ \| (TRACE|DEBUG|INFO|SUCCESS|WARNING)\s*\|`.
Example: `2024-08-05 14:10:24.378 | INFO | magic_pdf.libs.pdf_check:detect_invalid_chars:57 -
cid_count: 0, ...` (`MinerU__322.md`). **ERROR and CRITICAL levels are deliberately excluded from
the vocabulary** — a loguru `| ERROR |` line (e.g. `MinerU__163.md:65`, `... - list index out of
range`) already contains the literal substring "ERROR" and is therefore already caught by the
existing `ERROR_RE` hard exclusion; including it in the B vocabulary would be redundant at best and
risks a future accidental widening if the two regexes ever drift apart. Current corpus: **21 files,
163 lines, 23,521 chars** — 20 in `MinerU`, 1 (`playwright__26317.md`, a user's own scraper script
using loguru) unexpectedly in `playwright`, confirming the shape is about the *logging library*, not
the repo.

**Combined (union, no file double-counted across shapes): 55 files, 2,957 lines, 485,182 chars,
6.64% of the 963-file corpus.** Notably higher than the inventory's 3.09%, mostly because
`playwright_pw`'s reach was undercounted there (the inventory's single named example was
`pw:channel:event`; `pw:browser`, which is 991 occurrences corpus-wide, was not separately named).

## Explicit non-B shapes, with evidence

Found by reading every file the repeated-line ("J-detector", ≥5× literal repeat) scan surfaced,
274 files at the current corpus size — most of that growth over the inventory's 47-file measurement
is markdown fences and already-known classes, not new class-B instances. The shapes below matter
because they are the kind of thing a less careful vocabulary could sweep in:

- **crawl4ai batch-crawl `[FETCH]/[SCRAPE]/[ERROR]` progress lines** (`crawl4ai__1818.md`,
  `crawl4ai__1138.md`): `Call log:` / `Code context:` / `Error: Failed on navigating ACS-GOTO:`
  repeat 8–15× per file, but each instance wraps a *different* URL and a different traceback from a
  batch crawl. The literal-repeat detector flags the shared boilerplate phrase; the content around
  it is not disposable narration, it is per-item failure evidence.
- **Config-file paste** (`searxng__1003.md`: `disabled: true`-family lines repeated up to 36×;
  `searxng__1162.md` similarly): a full `settings.yml` pasted as direct evidence for a
  "Preferences reversed" bug. Structured data, not a log stream — the reported anomaly is *in* the
  config values themselves.
- **Raw scraped-HTML paste** (`crawl4ai__421.md`): `</button>` 16×, `</div>` 9×, etc. — HTML markup
  pasted as evidence of a scraping bug, not log lines.
- **Structured dict/fingerprint dump** (`camoufox__222.md`): repeated `'rangeMin': 127}` /
  `'rangeMax': 30,` lines — a pasted Python dict (browser fingerprint config), not narration.
- **Shell script source** (`curl_cffi__74.md`): `fi`, `set -e`, `set +e`, `log "━━━...━━━"` — script
  source pasted as a repro step; already substantially within `strip_build_logs`'s existing domain.
- **Java Selenium stack trace** (`playwright__18892.md`): `org.openqa.selenium.WebDriverException:
  java.lang.IllegalArgumentException: statusCode`, `at org.openqa.selenium...` frames — a genuine
  stack trace and the retrieval target. The exception line is already caught by `ERROR_RE`'s
  `exception` substring; the individual `at ...` frame lines are not separately protected by
  `ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE` (those are Python/native-specific), but they also don't match
  any of the three B vocabularies, so this file is a true negative today, not a hole.
- **SSE ping-heartbeat reproduction** (`claude-code__31932.md`): `event: ping` /
  `data: {"type": "ping"}` repeated 8× in a pasted API response. **The repetition count is the
  reported bug** — the user is showing that the API "stalls," sending only heartbeat pings and never
  completing. This is the strongest evidence against ever adding a generic "any line repeated ≥5×"
  removal rule on top of the J-detector: here, repetition is the signal a searcher would query for,
  not noise. This shape does not match any of the three vocabularies, so it is unaffected by what
  is proposed here, but it is why the J-detector must stay a *pointer for a human/detector-design
  process*, never a removal criterion by itself.
- **Short, interleaved debug+error mix** (`camoufox__296.md`): only 5 scattered `DEBUG:` lines (out
  of 142 total lines) sit inside a `[pid=N][out]`/`[pid=N][err]` "Browser logs:" block that is
  otherwise dominated by real errors and crash annotations, with a debug line and an error line
  sometimes 1–2 lines apart. Too short and too interleaved to isolate as a removable run — this is
  the direct evidence behind the run-length floor proposed below.
- **Rich-Python-traceback locals annotation** (`MinerU__2121.md`, plus 25 more files across
  `MinerU`/`crawl4ai`/`claude-code`, 2,678 `│` chars corpus-wide): box-drawing connector lines
  pointing at local-variable values, directly interleaved between `TRACE_RE`-matching
  `File "...", line N, in ...` frames. Part of a real traceback, not narration — a cross-cutting
  adjacency risk for any block-bridging detector, not specific to class B.

## Critical protection gap found (drives the gate proposal)

In `ghostty__10406.md`, the actual crash — `Segmentation fault at address 0x7fffbc02acc0` — is
followed by unresolved backtrace frames of the shape `???:?:?: 0x7ffff7f8b84e in ???
(libgobject-2.0.so.0)` (100× in this one file alone, per the normalized-fingerprint measure — each
literal-distinct because the hex address differs, invisible to a literal-repeat check). In
`ghostty__10379.md`, `thread 34041 panic: start index 1 is larger than end index 0` sits on the very
next line after the last `debug(app): mailbox message=redraw_surface` narration line — **zero-line
gap**. None of `Segmentation fault`, `thread N panic:`, `Aborted (core dumped)`, or the unresolved
`???:?:?:` frame shape contain any of `ERROR_RE`'s substrings (`error|fatal|traceback|exception|
failed`) or match `TRACE_RE`/`BACKTRACE_RE` (both require digit-based frame markers; `???` is not a
digit). A class-B detector that reused only today's protected set would have no hard stop at this
boundary.

`08_audit_debug_stream.py` measures this precisely via `PROPOSED_CRASH_RE`
(`panic:|Segmentation fault|SIG(ABRT|SEGV|ILL|BUS|FPE)\b|Aborted \(core dumped\)`) and
`PROPOSED_UNRESOLVED_FRAME_RE` (`^\?\?\?:\?:\?:.*0x[0-9a-fA-F]+ in `), both measurement-only and
never wired into anything. Adjacency counts (window = lines on each side of a vocabulary-matched
line that contain a protected line), existing protection vs. existing+proposed:

| Shape | Window | Existing only | Existing + proposed |
|---|---|---|---|
| `ghostty_debug` | 0 | 5 | 5 |
| `ghostty_debug` | 3 | 41 | 43 |
| `ghostty_debug` | 10 | 87 | 90 |
| `playwright_pw` | 0 | 251 | 252 |
| `playwright_pw` | 3 | 617 | 617 |
| `playwright_pw` | 10 | 929 | 929 |
| `loguru_narration` | 0 | 2 | 2 |
| `loguru_narration` | 3 | 26 | 26 |
| `loguru_narration` | 10 | 58 | 58 |

The proposed extension's marginal effect on these particular files/windows is small in absolute
count (the existing `ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE` already catch most nearby protected
content, including the `GraphicsCriticalError`/`gpu_process_host.cc(...)ERROR:` lines that show up
*inside* `pw:browser`-prefixed lines — those match `ERROR_RE`'s `error` substring directly). The
value of the proposed extension is not in these adjacency counts; it is in the two ghostty files
specifically, where the *entire crash* — not just a nearby line — would otherwise be unprotected.
A block-level, not line-adjacency-level, safety check is what actually matters there, which is why
the gate proposal below is a hard exclusion applied per-line during block-building (like
`_is_protected` in the build-log detector), not an adjacency-window heuristic.

At window 0, `ghostty_debug` already shows 5 vocabulary lines that are themselves caught by
`ERROR_RE` — checked directly: all 5 are benign narration that merely contains the word
"error"/"failed" (`info(cli): compatibility handler for bold-is-bright handled error, you may be
using a deprecated field: error.InvalidField`; `warning(...): failed to activate the on-screen
keyboard`; `warning(...): failed to initialize cgroups ... err=error.DbusCallFailed`) — not real
crashes. This confirms `ERROR_RE` is a conservative, blunt instrument: it sometimes over-protects
(keeps genuinely disposable narration from being stripped) but — on every case read here — never
under-protects a real crash by mistake. That asymmetry is the safe direction and should be kept.

## Literal-repeat vs. normalized-fingerprint

Literal repeats (≥5×, exact line, the inventory's "J" detector): **274 files, 7,326 instances**.
Normalized-fingerprint repeats (≥5×, digits/hex/UUID/timestamp collapsed to placeholders): **451
files, 15,120 instances** — a delta of 7,794 instances the literal measure misses entirely. The
clearest case: `ghostty__10406.md` shows only 493 literal-repeat instances but 654 once normalized,
with the single biggest normalized cluster being the 100× unresolved backtrace frame shape above —
proof that fingerprinting, not literal matching, is the right lens for judging how much of a
debug/crash dump is actually repetitive, since addresses/PIDs/counters make most machine output
literally-unique line-by-line while being structurally identical.

## Proposed gate

Three properties together, mirroring the build-log detector's own shape:

1. **Vocabulary anchor per shape** (the three regexes above), analogous to `SIGNAL_PATTERNS`.
2. **A run-length floor**, analogous to `MIN_BLOCK_LINES`. `camoufox__296.md`'s 5 scattered `DEBUG:`
   lines (run length 1, never consecutive) is the concrete case a floor must exclude, while
   `ghostty__10406.md`'s 702-line and `playwright__13156.md`'s 393-line runs are the concrete cases
   it must keep catching. The run-length histogram measured here (`08_audit_debug_stream.py`'s
   report) gives the actual distribution needed to pick a number in a follow-up milestone; this
   milestone does not choose one.
3. **An expanded hard-exclusion set**, applied per-line during block-building exactly like
   `_is_protected` in the build-log detector: today's `ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE` plus the
   proposed `PROPOSED_CRASH_RE`/`PROPOSED_UNRESOLVED_FRAME_RE` — required specifically to close the
   ghostty gap, since without it a debug-stream run has no reason to stop before a panic/segfault
   that sits on the very next line.

Whether the proposed crash/unresolved-frame protections are added to `src/github/text_cleaning.py`
is explicitly **not decided here** — it is a decision for the milestone that builds the actual
detector, made by reading this milestone's full dump, per this instruction.

## Artifacts

- `dev/content_cleaning/08_audit_debug_stream.py` — the measurement script (read-only).
- `dev/content_cleaning/md/08_audit_20260905_195802.md` — the report behind the numbers above:
  per-shape file/line/char/repo/run-length breakdown with per-file evidence, plus the literal-vs-
  fingerprint comparison with the top-delta files and their normalized examples.
