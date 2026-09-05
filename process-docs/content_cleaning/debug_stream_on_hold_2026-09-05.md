# Class B (DEBUG_STREAM) — Put On Hold (2026-09-05)

Decision record: after the dry-run detector for class B (this area's measurement and detector
entries of the same date) reached its final numbers — 41 files, 144 blocks, 2,645 lines, 382,151
gross chars, 5.23% of the 963-file corpus — the work was stopped before any production wiring,
apply, or reindex. Nothing of class B is in `src/`; `dev/content_cleaning/09_strip_debug_stream.py`
and its dump remain as the state reached.

## Why

The gate for going to production was reading the affected files in context after the strip, not
the dump alone. Rendering `ghostty__10379.md` and `playwright__33515.md` post-strip showed the
difference between the two shapes:

- ghostty: startup narration collapses to placeholders, the `thread 34041 panic` and its Zig
  backtrace stay whole. Readable, correct.
- playwright: the failure story stays (`FATAL ... Check failed`, `qemu ... core dumped`, `The GPU
  process has crashed N time(s)`, `signal=SIGTRAP`), but the Chromium backtraces around it turn
  into alternating placeholders and single surviving frames — frames survive only when their
  symbol name happens to contain `Error` or `Failed`. The result reads like data loss even though
  the crash cause is intact.

Under the premise fixed this day — content and context have absolute priority, only pure noise is
removed — a strip that leaves backtraces with holes is not acceptable as is. The candidate fix
(protect any native frame line, `#N 0xHEX ...` or `Name [0xHEX+N]`, so backtraces stay whole at a
measured cost of 206 lines in 3 files) was proposed but not decided; the user paused the class to
first verify the already-applied classes (A, F, G) against the same premise. That verification
found and repaired the warning loss in class A (this area's warning-protection entry).

## State if resumed

- Vocabulary, floor 3, no bridge, `CRASH_RE` — all in `09_strip_debug_stream.py`, with the
  iteration log in the detector entry.
- Open decision: protect native backtrace frame lines before production.
- Known vocabulary miss: 850 lines / 16 files of `[pid=N][out|err]` without `pw:` prefix, mostly
  camoufox — its own read-derive-decide pass.
- The context read of post-strip files, per affected file, is now part of the gate for every
  class, not only the dump read.
