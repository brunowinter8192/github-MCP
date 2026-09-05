#!/usr/bin/env python3
# Detect + dry-run strip junk class B (DEBUG_STREAM — app debug/log lines pasted from a terminal,
# not build/install output, which is class A / strip_build_logs) from issue MDs. Dry-run only: no
# --apply, never modifies the corpus. Shaped like strip_build_logs (vocabulary + run-length floor +
# per-line hard exclusion, block starts/ends only on a confirmed signal line), but see the
# decisions below — this detector deliberately has no bridge, unlike strip_build_logs's BRIDGE_GAP.
#
# Vocabulary (unchanged from dev/content_cleaning/08_audit_debug_stream.py, derived by reading real
# corpus files — see process-docs/content_cleaning/):
#   - ghostty_debug:    ^(debug|info|warning)\([a-zA-Z_]+\):
#   - playwright_pw:    ^\s*pw:[a-z:]+
#   - loguru_narration: TIMESTAMP | LEVEL | module:func:line - msg, LEVEL in {TRACE,DEBUG,INFO,SUCCESS,WARNING}
#
# MIN_RUN_LINES = 3, RAISED from an initially-accepted 2 after the precision read of the first
# dry-run dump (2026-09-05) surfaced two real, corpus-observed signal lines the first pass would
# have removed — both `pw:browser <process did exit: ..., signal=SIG*>` process-exit lines, sitting
# in exactly length-2 runs: `playwright__31950.md:236` (signal=SIGBUS) and `playwright__14689.md:75`
# (signal=SIGTRAP, in an issue titled "[BUG] ... browser crashes when running it headed or debug
# mode" — the SIGTRAP is the direct technical explanation). Floor 3 excludes both for free, and a
# direct floor-sensitivity re-check confirmed no other floor-3-vs-floor-2 difference introduces any
# new risk. Every length-1/2 run read at floor 2 in the other two shapes was already safe.
#
# No bridge: gaps between same-shape runs were read directly (window <= 3 non-blank lines) and are
# overwhelmingly either genuinely protected ERROR:/FATAL: lines (playwright__33515.md,
# playwright__16168.md, playwright__27997.md — dozens of cases) or meaningful non-filler content
# (test names, config-read lines, JS console warnings) — never a harmless wrapped continuation like
# strip_build_logs's compiler-diagnostic line-wrap case. A bridge here would routinely jump across
# real, protected error content, so none is used; a block starts and ends only on a signal line or
# an intervening blank line.
#
# Protected set: ERROR_RE/TRACE_RE/BACKTRACE_RE (existing, verbatim from src/github/text_cleaning.py)
# plus CRASH_RE (decided IN, evidence below). The unresolved-backtrace-frame pattern proposed in the
# M1 measurement (`???:?:?: 0x... in ???`) is decided OUT: it never co-occurs with any B-vocabulary
# match anywhere in the corpus (0 cases), and with no bridge it has no bridging role to defend
# either — including it would be complexity against a hypothetical, not an observed failure.
#
# CRASH_RE evidence and history: an initial narrow enumeration (`SIG(ABRT|SEGV|ILL|BUS|FPE)`) was
# built from the single SIGBUS case found before the first dry-run. The precision read of that
# dry-run's dump found a second case (SIGTRAP, above) the enumeration missed, plus a third:
# `playwright__33515.md:600-604`/`606-616`/`641-643`, a genuine native crash (qemu emulation hitting
# a trap: "qemu: uncaught target signal 5 (Trace/breakpoint trap) - core dumped") wrapped in a
# 33-line `pw:browser` block — too long for any reasonable floor to exclude, so this one is not a
# "raise the floor" case; the protected set itself had to close it. CRASH_RE was rebuilt on this
# evidence as a general pattern instead of a per-signal-name enumeration: `signal=SIG\w+` (catches
# any named-signal process-exit line, not just the two names observed) and `core dumped` (catches
# both `Aborted (core dumped)` and the qemu message, without requiring the word "Aborted"). A second
# precision pass on the re-run dump found a fourth, distinct case: `playwright__27363.md:117-165`
# and `playwright__27997.md` carry native macOS/Windows Chromium crash dumps (`#FailureMessage
# Object: ...`, `Crash keys: ...`) whose own numbered/hex-address backtrace frames (`ChromeMain
# [0x...+N]`, `GetHandleVerifier [0x...+N]`, etc.) match none of ERROR_RE/CRASH_RE either. Added
# `#FailureMessage` and `Crash keys:` (6 occurrences, 3 files total) as the two Chromium-specific
# crash markers, narrowly scoped like the qemu case. The generic internal function-name+hex-address
# frame lines themselves (not the markers) are NOT separately protected — see the process-docs
# entry for why this residue is accepted rather than chased with a broader native-frame pattern.
# A third precision pass, re-reading the file that produced the SIGBUS case, found a fifth: macOS's
# own in-process signal handler ("Received signal 10 BUS_ADRALN 00000bad4007", `playwright__31950.md`,
# 12 occurrences across 5 files) and a sixth: Windows NTSTATUS crash exit codes ("exitCode=3221225477"
# = STATUS_ACCESS_VIOLATION, "exitCode=3221226519", 3 occurrences in 2 files) — every corpus exit
# code is either 0-255 (normal) or one of these >= 5-digit NTSTATUS values (checked exhaustively:
# `exitCode=` takes exactly 6 distinct values corpus-wide, 3 normal and 3 crash codes), so
# `exitCode=\d{5,}` cleanly separates the two with no ambiguity. `Received signal \d+` and
# `exitCode=\d{5,}` added on this evidence.
#
# Usage: python3 dev/content_cleaning/09_strip_debug_stream.py [--source-dir PATH]

# INFRASTRUCTURE

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_issues"
)
REPORT_DIR = Path(__file__).parent / "md"

# Minimum consecutive (or blank-bridged) matching-shape lines to qualify as a removable block —
# see the header comment for the corpus evidence behind this number.
MIN_RUN_LINES = 3

# --- verbatim copy of src/github/text_cleaning.py's hard exclusions ("currently protected") -----
ERROR_RE = re.compile(r'error|fatal|traceback|exception|failed', re.IGNORECASE)
TRACE_RE = re.compile(r'^\s*File "[^"]+", line \d+, in ')
BACKTRACE_RE = re.compile(r':\d+:\d+:.*0x[0-9a-fA-F]+ in ')

# --- decided-in extension: real crash/signal indicators absent from ERROR_RE's vocabulary --------
# See header comment for the evidence (SIGBUS, SIGTRAP, qemu core-dump, Chromium crash markers)
# behind this decision and why it is a general pattern, not a per-signal-name enumeration.
CRASH_RE = re.compile(
    r'panic:|Segmentation fault|signal=SIG\w+|core dumped|#FailureMessage|Crash keys:|'
    r'Received signal \d+|exitCode=\d{5,}',
    re.IGNORECASE,
)

# --- class-B vocabulary (unchanged from 08_audit_debug_stream.py) -------------------------------
SHAPES = {
    "ghostty_debug": re.compile(r'^(debug|info|warning)\([a-zA-Z_]+\):'),
    "playwright_pw": re.compile(r'^\s*pw:[a-z:]+'),
    "loguru_narration": re.compile(
        r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+ \| (TRACE|DEBUG|INFO|SUCCESS|WARNING)\s*\|'
    ),
}


@dataclass
class Block:
    filename: str
    shape: str
    start_line: int   # 1-indexed
    end_line: int      # 1-indexed
    length: int
    text: str


@dataclass
class FileResult:
    filename: str
    filepath: Path
    file_chars: int
    blocks: list = field(default_factory=list)
    gross_chars_removed: int = 0   # size of the text cut out
    net_chars_removed: int = 0     # file shrinkage, accounting for the placeholder written back
    changed: bool = False


# FUNCTIONS

# Hard-excluded: never signal, always breaks a run — existing hard exclusions plus CRASH_RE
def _is_protected(line: str) -> bool:
    return bool(ERROR_RE.search(line) or TRACE_RE.search(line) or BACKTRACE_RE.search(line)
                or CRASH_RE.search(line))


# Group one shape's matched, non-protected lines into removable (start, end) line-index spans
# (0-indexed, inclusive) at or above MIN_RUN_LINES. Blank lines bridge a run but never extend or
# confirm it alone — no other bridging exists (see header comment for why).
def _find_shape_blocks(lines: list, shape_re: "re.Pattern") -> list:
    def is_signal(line: str) -> bool:
        return bool(shape_re.match(line)) and not _is_protected(line)

    n = len(lines)
    blocks = []
    i = 0
    while i < n:
        if not is_signal(lines[i]):
            i += 1
            continue
        start = i
        end = i
        j = i + 1
        while j < n:
            if is_signal(lines[j]):
                end = j
                j += 1
                continue
            if lines[j].strip() == '':
                j += 1
                continue
            break
        if end - start + 1 >= MIN_RUN_LINES:
            blocks.append((start, end))
        i = end + 1
    return blocks


# Combine all three shapes' blocks into one sorted list. The three vocabulary anchors are mutually
# exclusive by first-character prefix (debug(/info(/warning( vs. pw: vs. a digit timestamp), so no
# line can ever match two shapes and no two shapes' blocks can ever overlap.
def _find_all_blocks(lines: list) -> list:
    all_blocks = []
    for shape_name, shape_re in SHAPES.items():
        for start, end in _find_shape_blocks(lines, shape_re):
            all_blocks.append((start, end, shape_name))
    return sorted(all_blocks)


def _placeholder(n_lines: int) -> str:
    return f"[debug-stream output removed — {n_lines} lines]"


# Strip class-B debug-stream blocks from the full text of one issue MD
def strip_debug_stream(text: str) -> str:
    lines = text.splitlines()
    blocks = _find_all_blocks(lines)
    if not blocks:
        return text
    out = []
    prev_end = -1
    for start, end, _shape in blocks:
        out.extend(lines[prev_end + 1:start])
        out.append(_placeholder(end - start + 1))
        prev_end = end
    out.extend(lines[prev_end + 1:])
    result = '\n'.join(out)
    if text.endswith('\n') and not result.endswith('\n'):
        result += '\n'
    return result


# Compute per-file block detail (verbatim removed text) + gross/net chars removed
def measure_all(md_files: list) -> list:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        lines = before.splitlines()
        blocks_idx = _find_all_blocks(lines)
        after = strip_debug_stream(before)
        blocks = []
        gross = 0
        for start, end, shape_name in blocks_idx:
            block_text = '\n'.join(lines[start:end + 1])
            blocks.append(Block(
                filename=fp.name, shape=shape_name,
                start_line=start + 1, end_line=end + 1,
                length=end - start + 1, text=block_text,
            ))
            gross += len(block_text) + 1
        results.append(FileResult(
            filename=fp.name, filepath=fp, file_chars=len(before),
            blocks=blocks, gross_chars_removed=gross,
            net_chars_removed=len(before) - len(after),
            changed=after != before,
        ))
    return results


# Explicit assertion: no removed line matches any protected regex. Returns lines_checked; exits
# (writes nothing) on failure — mirrors 06_reclean_build_logs.py's safety gate.
def assert_safety(results: list) -> int:
    violations = []
    total_checked = 0
    for fr in results:
        for b in fr.blocks:
            for line in b.text.split('\n'):
                total_checked += 1
                if _is_protected(line):
                    violations.append((fr.filename, line))
    if violations:
        for fname, line in violations:
            print(f"SAFETY VIOLATION: {fname}: {line[:120]!r}", file=sys.stderr)
        print(f"ASSERTION FAIL: {len(violations)} violation(s) in {total_checked} removed lines "
              f"checked — refusing to write report.", file=sys.stderr)
        sys.exit(1)
    return total_checked


# Write the dump: nothing but the removed content. One identification line per block (source file
# + line range + shape, nothing else on that line), then the removed text verbatim and unmodified,
# then the next block. No summary, no tables — all measurement belongs in stdout.
def write_dump(path: Path, results: list) -> None:
    o = []
    for fr in sorted(results, key=lambda x: x.filename):
        for b in fr.blocks:
            o.append(f"{b.filename}:{b.start_line}-{b.end_line} [{b.shape}]")
            o.append(b.text)
            o.append("")
    path.write_text('\n'.join(o))


# ORCHESTRATOR

def strip_debug_stream_workflow(source_dir: Path) -> None:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    results = measure_all(md_files)
    total_checked = assert_safety(results)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"09_strip_debug_stream_dryrun_{ts}.md"
    write_dump(report_path, results)

    changed = [fr for fr in results if fr.changed]
    total_blocks = sum(len(fr.blocks) for fr in results)
    total_lines = sum(b.length for fr in results for b in fr.blocks)
    total_gross = sum(fr.gross_chars_removed for fr in results)
    total_net = sum(fr.net_chars_removed for fr in results)
    total_corpus_chars = sum(fr.file_chars for fr in results)
    pct = 100 * total_gross / total_corpus_chars if total_corpus_chars else 0

    print(f"report: {report_path}")
    print(f"files_scanned={len(md_files)} files_affected={len(changed)} blocks={total_blocks} "
          f"lines_removed={total_lines} gross_chars_removed={total_gross} "
          f"net_chars_removed={total_net} pct_corpus={pct:.2f}% "
          f"safety=PASS ({total_checked} lines checked)")

    for shape_name in SHAPES:
        shape_blocks = [b for fr in results for b in fr.blocks if b.shape == shape_name]
        shape_files = {b.filename for b in shape_blocks}
        shape_lines = sum(b.length for b in shape_blocks)
        shape_chars = sum(len(b.text) + 1 for b in shape_blocks)
        print(f"shape={shape_name} files={len(shape_files)} blocks={len(shape_blocks)} "
              f"lines={shape_lines} chars={shape_chars}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Detect + dry-run strip junk class B (DEBUG_STREAM) from issue MDs — "
                    "dry-run only, no --apply"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    args = p.parse_args()
    strip_debug_stream_workflow(args.source_dir)
