#!/usr/bin/env python3
# Re-clean existing issue MDs — strip two junk classes left by the Bitbucket-to-GitHub migration:
#
# Class F (tracker-migration attribution header + rule): a bold "**[Original report](bitbucket_url)
# by NAME (...).**" line (issue body, first content) or "**Original comment by NAME (...).**" line
# (each migrated comment), always followed by a blank line then exactly 40 dashes.
#
# Class G (automated version-removal comment): a comment whose entire body is one line, "Removing
# version: X (automated comment)" — Bitbucket generated these when a version field was removed,
# and the migration copied them under the maintainer's human account, so the existing '[bot]'
# author check cannot see them. The whole comment (separator through body) is dropped, not just
# the marker line. A class-G comment always carries a class-F header too (nested inside its body),
# so a class-G span fully contains its own class-F span — see `_find_all_blocks`.
#
# Observed only in the pyobjc repo (7 issues for class F, 5 of those 7 for class G) as of
# 2026-09-05 — see process-docs/content_cleaning/. Safe on already-built MDs: the anchors are
# mutually exclusive by content and match nothing else observed in the corpus. Dry-run by default;
# --apply overwrites in place after a timestamped backup of the whole corpus dir — the corpus is
# gitignored, so the backup is the only safety net.
#
# Intentional verbatim copy of the anchor regexes + removal logic in src/github/index_issues.py
# (strip_noise()'s class-F branch and strip_comments_noise()'s class-F + class-G branches,
# combined into one pass since the anchors never collide within a single already-assembled MD).
# dev/ may not import src/ (hook: block_dev_imports_src) — intentional duplication, not drift, per
# the convention in 03/04/06's DOCS.md entries. Update this copy if the source changes.
# Source of truth: src/github/index_issues.py.
#
# Usage: python3 dev/content_cleaning/07_reclean_migration_headers.py [--apply] [--source-dir PATH]

# INFRASTRUCTURE

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_issues"
)
REPORT_DIR = Path(__file__).parent / "md"

# --- verbatim copy of src/github/index_issues.py class-F/G anchors + removal (keep in sync) ----
# Anonymous/GitHub-less variants ("by Anonymous.**", "(Bitbucket: [..](..), ).**") both still end
# in ").**"/"s.**", so the trailing ".**" anchor covers them without widening past the corpus.
MIGRATION_REPORT_RE = re.compile(r'^\*\*\[Original report\]\([^)]*\) by .+\.\*\*$')
MIGRATION_COMMENT_RE = re.compile(r'^\*\*Original comment by .+\.\*\*$')
MIGRATION_RULE_RE = re.compile(r'^-{40}$')
SEP_RE = re.compile(r'^--- Comment \d+ ---$')
AUTOMATED_COMMENT_RE = re.compile(r'^Removing version: .+ \(automated comment\)$')


# Group class-F spans into removable (start, end) line-index spans (0-indexed, inclusive — header
# line, blank line, 40-dash rule; always exactly 3 lines)
def _find_migration_blocks(lines: list) -> list:
    n = len(lines)
    blocks = []
    i = 0
    while i < n:
        line = lines[i]
        if ((MIGRATION_REPORT_RE.match(line) or MIGRATION_COMMENT_RE.match(line))
                and i + 2 < n and lines[i + 1].strip() == ''
                and MIGRATION_RULE_RE.match(lines[i + 2])):
            blocks.append((i, i + 2))
            i += 3
            continue
        i += 1
    return blocks


# True if a comment's body (the lines between its separator and the next one, or end of text)
# reduces to solely the automated version-removal marker once Author/Date metadata and a nested
# class-F migration header (if present) are excluded
def _is_automated_only_comment(block: list) -> bool:
    content = []
    i = 0
    n = len(block)
    while i < n:
        line = block[i]
        if line.strip() == '' or line.startswith('Author:') or line.startswith('Date:'):
            i += 1
            continue
        if (MIGRATION_COMMENT_RE.match(line) and i + 2 < n
                and block[i + 1].strip() == '' and MIGRATION_RULE_RE.match(block[i + 2])):
            i += 3
            continue
        content.append(line)
        i += 1
    return len(content) == 1 and bool(AUTOMATED_COMMENT_RE.match(content[0]))


# Group class-G spans into removable (start, end) line-index spans (0-indexed, inclusive —
# separator line through the last line before the next separator or end of text)
def _find_automated_comment_blocks(lines: list) -> list:
    n = len(lines)
    blocks = []
    i = 0
    while i < n:
        if SEP_RE.match(lines[i]):
            end_idx = next((j for j in range(i + 1, n) if SEP_RE.match(lines[j])), n)
            if _is_automated_only_comment(lines[i + 1:end_idx]):
                blocks.append((i, end_idx - 1))
                i = end_idx
                continue
        i += 1
    return blocks


# Combine class-F and class-G spans into one non-overlapping, class-labeled, sorted list. A
# class-G span (whole comment) always fully contains its own nested class-F header when the
# comment carried one — such an F span is dropped from the F list here (already covered by the G
# span) rather than listed and spliced twice, so per-class totals and the text splice never
# double-count the same lines.
def _find_all_blocks(lines: list) -> list:
    g_blocks = _find_automated_comment_blocks(lines)
    f_blocks_raw = _find_migration_blocks(lines)
    f_blocks = [
        b for b in f_blocks_raw
        if not any(g[0] <= b[0] and b[1] <= g[1] for g in g_blocks)
    ]
    tagged = [(s, e, 'F') for s, e in f_blocks] + [(s, e, 'G') for s, e in g_blocks]
    return sorted(tagged)


# Strip class-F headers/rules and whole class-G comments from the full text of one issue MD
def strip_migration_and_automated(text: str) -> str:
    lines = text.splitlines()
    blocks = _find_all_blocks(lines)
    if not blocks:
        return text
    out = []
    prev_end = -1
    for start, end, _cls in blocks:
        out.extend(lines[prev_end + 1:start])
        prev_end = end
    out.extend(lines[prev_end + 1:])
    result = '\n'.join(out)
    if text.endswith('\n') and not result.endswith('\n'):
        result += '\n'
    return result
# --- end verbatim copy ---------------------------------------------------------------------------


# ORCHESTRATOR

def reclean_workflow(source_dir: Path, apply: bool) -> None:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    results = measure_all(md_files)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"07_reclean_dryrun_{ts}.md"
    write_report(report_path, results, len(md_files))
    print(report_path)

    if apply:
        backup_dir = apply_changes(source_dir, results, ts)
        print(f"Backup: {backup_dir}")


# FUNCTIONS

# Compute per-file removable spans (class-labeled) + before/after text + per-class lines/chars
# removed for every corpus file
def measure_all(md_files: list) -> list[dict]:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        lines = before.splitlines()
        blocks = _find_all_blocks(lines)
        after = strip_migration_and_automated(before)
        f_blocks = [(s, e) for s, e, c in blocks if c == 'F']
        g_blocks = [(s, e) for s, e, c in blocks if c == 'G']
        f_lines = sum(e - s + 1 for s, e in f_blocks)
        g_lines = sum(e - s + 1 for s, e in g_blocks)
        f_chars = sum(len('\n'.join(lines[s:e + 1])) + 1 for s, e in f_blocks)
        g_chars = sum(len('\n'.join(lines[s:e + 1])) + 1 for s, e in g_blocks)
        results.append({
            "filename": fp.name,
            "filepath": fp,
            "before": before,
            "after": after,
            "lines": lines,
            "blocks": blocks,
            "f_spans": len(f_blocks),
            "g_spans": len(g_blocks),
            "f_lines": f_lines,
            "g_lines": g_lines,
            "f_chars": f_chars,
            "g_chars": g_chars,
            "lines_removed": f_lines + g_lines,
            "chars_removed": f_chars + g_chars,
            "changed": after != before,
        })
    return results


# Backup the whole corpus dir, then overwrite only changed files. Named so its purpose is obvious
# from the directory name alone — the corpus has no raw counterpart for fetches before raw_logging
# existed, so this backup is the only surviving record of pre-strip state for those files. Not a
# disposable safety net: do not delete.
def apply_changes(source_dir: Path, results: list[dict], ts: str) -> Path:
    backup_dir = source_dir.parent / f"{source_dir.name}_PRE_MIGRATION_NOISE_STRIP_BACKUP_{ts}"
    shutil.copytree(source_dir, backup_dir)
    for r in results:
        if r["changed"]:
            r["filepath"].write_text(r["after"], encoding="utf-8")
    return backup_dir


# Write the report: summary numbers split F/G, a per-file table split F/G, then the verbatim
# removed text for every span (one identification line — file + 1-indexed line range + class tag —
# then the text, nothing else) so the whole removal can be read in full in one pass.
def write_report(path: Path, results: list[dict], total_files: int) -> None:
    changed = [r for r in results if r["changed"]]
    total_f_spans = sum(r["f_spans"] for r in results)
    total_g_spans = sum(r["g_spans"] for r in results)
    total_f_lines = sum(r["f_lines"] for r in results)
    total_g_lines = sum(r["g_lines"] for r in results)
    total_f_chars = sum(r["f_chars"] for r in results)
    total_g_chars = sum(r["g_chars"] for r in results)

    o = [
        f"# Migration-Header + Automated-Comment Reclean Dry-Run Report — "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nCorpus: {total_files} files · `data/documents/github_issues/`",
        "\n## Summary\n",
        "| Metric | Total | Class F | Class G |",
        "|---|---|---|---|",
        f"| Files that would change | {len(changed)} / {total_files} | — | — |",
        f"| Spans removed | {total_f_spans + total_g_spans} | {total_f_spans} | {total_g_spans} |",
        f"| Lines removed | {total_f_lines + total_g_lines} | {total_f_lines} | {total_g_lines} |",
        f"| Chars removed | {total_f_chars + total_g_chars:,} | {total_f_chars:,} | "
        f"{total_g_chars:,} |",
    ]

    if changed:
        o += [
            "\n## Per-File Results (changed files)\n",
            "| File | F spans | G spans | Lines removed | Chars removed |",
            "|---|---|---|---|---|",
        ]
        for r in sorted(changed, key=lambda x: x["filename"]):
            o.append(f"| `{r['filename']}` | {r['f_spans']} | {r['g_spans']} | "
                      f"{r['lines_removed']} | {r['chars_removed']:,} |")

        o += ["\n## Removed Spans (verbatim)\n"]
        for r in sorted(changed, key=lambda x: x["filename"]):
            for start, end, cls in r["blocks"]:
                o.append(f"{r['filename']}:{start + 1}-{end + 1} [{cls}]")
                o.append('\n'.join(r["lines"][start:end + 1]))
                o.append("")

    unchanged = [r for r in results if not r["changed"]]
    o += [
        "\n## Unchanged Files\n",
        f"{len(unchanged)} files would not change.",
    ]

    path.write_text('\n'.join(o) + '\n')


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Re-clean existing issue MDs — strip tracker-migration header + rule "
                    "(class F) and whole automated version-removal comments (class G). "
                    "Dry-run by default"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    p.add_argument("--apply", action="store_true",
                    help="Overwrite files in place (creates timestamped backup first)")
    args = p.parse_args()
    reclean_workflow(args.source_dir, apply=args.apply)
