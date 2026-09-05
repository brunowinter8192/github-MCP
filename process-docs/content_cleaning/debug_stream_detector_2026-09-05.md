# Class B (DEBUG_STREAM) — Dry-Run Detector, Precision/Recall Reads, Iteration Log (2026-09-05)

Process record for `dev/content_cleaning/09_strip_debug_stream.py`: the dry-run detector built on
top of this area's earlier class-B measurement, the floor/bridge/protection decisions made before
the first run, and the iteration that followed from reading the dump and the affected files in
full. Dry-run only throughout — no `--apply`, no reindex, no production code.

## Decisions made before the first dry-run, and their evidence

**Floor = 2, accepted on vocabulary specificity.** The three class-B vocabularies
(`^(debug|info|warning)\([a-zA-Z_]+\):`, `^\s*pw:[a-z:]+`, loguru's timestamped line) are
structural, multi-part anchors — nothing a human would write as an ordinary sentence — unlike
`strip_build_logs`'s loose single-verb vocabulary, which needed `MIN_BLOCK_LINES=10` mainly to
filter accidental prose collisions. Every length-1/2 run read across all three shapes (133 loguru,
15 ghostty, 78 playwright_pw instances) was safe, low-value narration. The one exception found —
`playwright__33515.md`'s "The GPU process has crashed N time(s)" WARNING line, vocab-matched, not
caught by `ERROR_RE` — was confirmed to occur *only* in length-1 runs (0 runs of length ≥2
corpus-wide contain "has crashed"), always sandwiched between genuinely protected `ERROR:`/`FATAL:`
lines, so floor 2 excluded it for free.

**No bridge.** Every gap between two same-shape runs (window ≤3 non-blank lines) was read directly.
The overwhelming majority are genuinely protected `ERROR:`/`FATAL:` lines (`playwright__33515.md`,
`playwright__16168.md`, `playwright__27997.md` — dozens of cases) or meaningful non-filler content
(test names, config-read lines, JS console warnings) — never a harmless wrapped continuation
analogous to `strip_build_logs`'s compiler-diagnostic line-wrap case. A bridge here would routinely
jump across real, protected error content.

**Protected set: existing (`ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE`) plus a narrow `CRASH_RE`, decided
in on one concrete case**: `playwright__31950.md:236`, `signal=SIGBUS`, in an issue titled "Browser
... Target page, context or browser has been closed" — simulated precisely: without protection this
line joins the next into a length-2 run and is removed at floor 2; with it, excluded. The
unresolved-backtrace-frame pattern proposed in the M1 measurement (`???:?:?: 0x... in ???`) was
decided **out**: zero corpus overlap with any B-vocabulary match, and with no bridge it has no
bridging role to defend either.

## First dry-run, and the precision read that followed

First run: floor 2, `CRASH_RE = SIG(ABRT|SEGV|ILL|BUS|FPE)|Aborted \(core dumped\)|panic:|
Segmentation fault`. Result: 50 files, 195 blocks, 2,777 lines, 408,704 gross chars, 5.60% of
corpus. Safety assertion passed (no removed line matched a protected regex — by construction, since
the assertion checks the same regex used to build blocks).

Reading the full dump (first line to last) found two real signal lines the enumeration missed,
both in exactly length-2 runs: `playwright__14689.md:75` (`signal=SIGTRAP`, issue titled "[BUG] ...
browser crashes when running it headed or debug mode" — the SIGTRAP is the direct technical
explanation) and a re-confirmation that the SIGBUS case (used to justify `CRASH_RE` before the
first run) was itself also exactly length-2. **Both are short-run findings, so the floor was
raised (2 → 3) per the guidance to raise the floor rather than patch vocabulary for this class of
finding** — floor 3 excludes both for free, verified by direct re-simulation, with no other
floor-3-vs-floor-2 difference introducing new risk (every additional length-2 run excluded at floor
3 was independently read and confirmed benign — `<launching>`/`<launched>` pairs and similar).

A third case in the same dump was **not** a short-run finding: `playwright__33515.md:600-604` /
`606-616` / `641-643` — a genuine native crash (qemu emulation hitting a trap: `"qemu: uncaught
target signal 5 (Trace/breakpoint trap) - core dumped"`) sits inside a 33-line `pw:browser` block,
far too long for any reasonable floor to exclude. This is the one case in this milestone where the
protected set, not the floor, had to close the gap. `CRASH_RE` was rebuilt at this point as two
general patterns instead of a five-name enumeration: `signal=SIG\w+` (any named-signal process-exit
line, not just the two names observed) and `core dumped` (catches both `Aborted (core dumped)` and
the qemu message without requiring the word "Aborted"). Re-run: 41 files, 142 blocks, 2,659 lines,
385,088 gross chars, 5.27%.

## Second precision pass: two more corpus-specific crash-marker gaps

Reading the *re-run* dump in full (not just diffing) surfaced a fourth case:
`playwright__27363.md:117-165` (issue titled "[BUG] Ah Snap Error 5 using playwright ... chromium")
and `playwright__27997.md` carry native macOS/Windows Chromium crash dumps whose own markers
(`#FailureMessage Object: ...`, `Crash keys: ...`) match neither `ERROR_RE` nor the rebuilt
`CRASH_RE`. Added both as narrowly-scoped literal markers (6 occurrences, 3 files corpus-wide).
Re-run: 41 files, 143 blocks, 2,655 lines, 384,387 gross chars, 5.26%.

A further read of the *files themselves* (not just the dump, since the recall check requires
reading every affected file in full) turned up two more, both in the very files that had already
motivated `CRASH_RE`: `playwright__31950.md:152` carries macOS's own in-process signal handler
output, `"Received signal 10 BUS_ADRALN 00000bad4007"` — a different phrasing than
`signal=SIG\w+`, appearing 12 times across 5 files corpus-wide, all in what are clearly crash
contexts on inspection. And `playwright__37199.md` carries Windows NTSTATUS crash exit codes
(`exitCode=3221225477` = `STATUS_ACCESS_VIOLATION`, `exitCode=3221226519` =
`STATUS_INVALID_CRUNTIME_PARAMETER`) — confirmed as the retrieval target directly: a maintainer
comment in that same file reads *"Looking at `exitCode=3221226519` in the logs, which is
`0xC0000417`. This is probably `STATUS_INVALID_CRUNTIME_PARAMETER`... I'd recommend updating your
system."* Every `exitCode=` value in the whole corpus was enumerated (6 distinct values: `0`, `1`,
`255` — all normal — and the three NTSTATUS values above, all ≥10 digits), so `exitCode=\d{5,}`
cleanly separates normal exits from crash codes with no ambiguity. Both patterns added. Final
re-run: **41 files, 144 blocks, 2,645 lines, 382,151 gross chars, 376,352 net chars, 5.23% of
corpus.** Safety assertion: PASS, 2,645 lines checked, 0 violations.

A broad, uncurated keyword sweep (`signal|SIG[A-Z]{2,}|SEGV|BUS_ADR|EXC_BAD|core.?dump|panic|
Segmentation|FailureMessage|Crash keys|fatal|abort|crash|exitCode=\d{4,}|Received signal`) was then
run against every kept block corpus-wide as a convergence check. The only remaining hits are
confirmed benign or already-documented: `exitCode=0`/`exitCode=1` with `signal=null` (normal,
successful process exits — routine teardown narration), `net::ERR_ABORTED` (a generic, common
Chrome network-cancellation code, not a distinguishing failure), and generic native backtrace frame
lines (see below). No further protected-set change was made.

## Accepted, documented residue: generic native backtrace frames

`playwright__27363.md`, `playwright__27997.md`, and `playwright__33515.md` still lose their own
internal Chromium backtrace frames (`ChromeMain [0x...+N]`, `GetHandleVerifier [0x...+N]`,
`base::debug::CollectStackTrace()`, numbered `#N 0xHEX func()` frames — 206 lines total across the
3 files) as part of otherwise-legitimate removed blocks. These lines were read directly and judged
non-retrieval-value: they are Chromium's own internal C++ symbol names, generic and near-identical
across countless unrelated Chromium crash reports (not distinctive search targets), and — critically
— the actual distinguishing crash indicator in each case (the signal name, the `core dumped`/
`#FailureMessage`/`Crash keys:` marker, the exit code) is separately protected and survives
untouched. No broader "native backtrace frame" pattern was built to catch these: the formats vary
too much across platforms (Linux `#N 0xHEX func()`, Windows `FunctionName [0xHEX+offset]`, macOS
numbered-frame-with-Framework-name) to bound safely without either missing cases or over-matching
ordinary lines that happen to contain a hex address (e.g. `objc[30993]: Class WebSwapCGLLayer ...
(0x24c4d31a8)`, which is completely benign). This residue is accepted, not silently absorbed.

## Precision read: final answer

Zero is the answer **after** the iteration above, not before it — the full first-line-to-last read
of the dump found five real gaps across three iterations (SIGBUS, SIGTRAP, qemu core-dump,
Chromium crash markers, macOS `Received signal`/Windows NTSTATUS exit codes), each fixed and
re-verified. The one open item is the documented, judged-acceptable native-backtrace-frame residue
(206 lines, 3 files) described above — reported here explicitly rather than folded into a "zero"
claim, since it is technically part of removed crash-adjacent content even though its retrieval
value is judged nil.

## Recall check: every affected file read after the strip, in full

410 lines still match a class-B vocabulary after the strip, across 36 of the 41 affected files.
Classified by direct re-scan of every vocabulary-matched line in every affected file:

- **257 lines** are individually protected (the line itself matches `ERROR_RE`/`TRACE_RE`/
  `BACKTRACE_RE`/`CRASH_RE`) — a mix of genuinely benign narration that merely contains the word
  "error"/"failed" (`ghostty__10379.md`: `"info(cli): compatibility handler for bold-is-bright
  handled error, you may be using a deprecated field..."` — not a crash) and the accepted
  backtrace-frame residue described above.
- **153 lines** survive because their run never reached the floor — isolated 1–2-line vocabulary
  matches surrounded by other, non-B content (progress bars, other loggers, blank lines followed
  by non-matching text). Every one of these was already read directly during the floor decision
  (see above) and judged safe, low-value narration (`MinerU` init/model-load lines interspersed
  with `Fetching ... 100%|...` progress bars and other logger formats being the dominant pattern).

**Vocabulary miss, found during the recall read, reported but not fixed this milestone**: 850 lines
across 16 files carry the shape `^\s*\[pid=\d+\]\[(out|err)\]` — functionally the same
browser-process stdout/stderr forwarding as the `pw:browser [pid=N][out/err]` sub-shape, but
*without* the `pw:` prefix (seen in `camoufox` files and some `playwright` files, likely from a
different capture path — pytest-captured output, or camoufox's own non-`pw:`-namespaced
forwarding, consistent with the `camoufox__296.md` finding in the M1 measurement, where only 5 of
142 lines in a "Browser logs:" block were `DEBUG:`-prefixed and the rest were real errors tightly
interleaved). This shape was **not** added to the vocabulary in this milestone: it is a
newly-discovered, differently-shaped candidate that needs its own read-derive-decide pass (matching
this area's established methodology) rather than a reactive addition under an already-large
iteration count. Recommended as the subject of a follow-up milestone.

## Final numbers

**Files: 41 · Blocks: 144 · Lines removed: 2,645 · Chars removed — gross: 382,151, net: 376,352 ·
5.23% of the 963-file corpus.** Safety assertion: PASS, 2,645 lines checked, 0 violations.

Iteration summary (files / blocks / lines / gross chars / % corpus at each stage):

| Stage | Files | Blocks | Lines | Gross chars | % corpus |
|---|---|---|---|---|---|
| Initial (floor 2, narrow `CRASH_RE`) | 50 | 195 | 2,777 | 408,704 | 5.60% |
| Floor → 3, `CRASH_RE` generalized (SIGBUS/SIGTRAP/qemu) | 41 | 142 | 2,659 | 385,088 | 5.27% |
| + Chromium crash markers (`#FailureMessage`/`Crash keys:`) | 41 | 143 | 2,655 | 384,387 | 5.26% |
| + `Received signal N` / `exitCode=\d{5,}` (final) | 41 | 144 | 2,645 | 382,151 | 5.23% |

## Artifacts

- `dev/content_cleaning/09_strip_debug_stream.py` — the detector (dry-run only, no `--apply`).
- `dev/content_cleaning/md/09_strip_debug_stream_dryrun_20260905_202152.md` — the final dump behind
  the numbers above (superseded intermediate dumps from the iteration were not retained; every
  intermediate number is stated inline above with its supporting evidence).
