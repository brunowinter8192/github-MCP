#!/usr/bin/env python3
# Re-clean existing issue MDs — strip the tracker-migration attribution header + rule (junk
# class F): a bold "**[Original report](bitbucket_url) by NAME (...).**" line (issue body, first
# content) or "**Original comment by NAME (...).**" line (each migrated comment), always followed
# by a blank line then exactly 40 dashes. Observed only in the pyobjc repo (7 issues) as of
# 2026-08-28 — see process-docs/content_cleaning/junk_class_inventory_2026-08-28.md. Safe on
# already-built MDs: the two anchors are mutually exclusive by content (report-form only ever
# opens an issue body, comment-form only ever opens a migrated comment) and match nothing else
# observed in the corpus. Dry-run by default; --apply overwrites in place after a timestamped
# backup of the whole corpus dir — the corpus is gitignored, so the backup is the only safety net.
#
# Intentional verbatim copy of the anchor regexes + removal logic in src/github/index_issues.py
# (strip_noise()'s and strip_comments_noise()'s class-F branches, combined into one pass since the
# two anchors never collide within a single already-assembled MD). dev/ may not import src/ (hook:
# block_dev_imports_src) — intentional duplication, not drift, per the convention in 03/04/06's
# DOCS.md entries. Update this copy if the source changes. Source of truth: src/github/index_issues.py.
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

# --- verbatim copy of src/github/index_issues.py class-F anchors + removal (keep in sync) ------
# Anonymous/GitHub-less variants ("by Anonymous.**", "(Bitbucket: [..](..), ).**") both still end
# in ").**"/"s.**", so the trailing ".**" anchor covers them without widening past the corpus.
MIGRATION_REPORT_RE = re.compile(r'^\*\*\[Original report\]\([^)]*\) by .+\.\*\*$')
MIGRATION_COMMENT_RE = re.compile(r'^\*\*Original comment by .+\.\*\*$')
MIGRATION_RULE_RE = re.compile(r'^-{40}$')


# Group migration-header spans into removable (start, end) line-index spans (0-indexed, inclusive
# — header line, blank line, 40-dash rule; always exactly 3 lines)
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


# Strip tracker-migration attribution header + rule (class F) from the full text of one issue MD
def strip_migration_header(text: str) -> str:
    lines = text.splitlines()
    blocks = _find_migration_blocks(lines)
    if not blocks:
        return text
    out = []
    prev_end = -1
    for start, end in blocks:
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

# Compute per-file removable spans + before/after text + lines/chars removed for every corpus file
def measure_all(md_files: list) -> list[dict]:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        lines = before.splitlines()
        blocks = _find_migration_blocks(lines)
        after = strip_migration_header(before)
        lines_removed = sum(end - start + 1 for start, end in blocks)
        chars_removed = sum(len('\n'.join(lines[s:e + 1])) + 1 for s, e in blocks)
        results.append({
            "filename": fp.name,
            "filepath": fp,
            "before": before,
            "after": after,
            "lines": lines,
            "blocks": blocks,
            "lines_removed": lines_removed,
            "chars_removed": chars_removed,
            "changed": after != before,
        })
    return results


# Backup the whole corpus dir, then overwrite only changed files. Named so its purpose is obvious
# from the directory name alone — the corpus has no raw counterpart for fetches before raw_logging
# existed, so this backup is the only surviving record of pre-strip state for those files. Not a
# disposable safety net: do not delete.
def apply_changes(source_dir: Path, results: list[dict], ts: str) -> Path:
    backup_dir = source_dir.parent / f"{source_dir.name}_PRE_MIGRATION_HEADER_STRIP_BACKUP_{ts}"
    shutil.copytree(source_dir, backup_dir)
    for r in results:
        if r["changed"]:
            r["filepath"].write_text(r["after"], encoding="utf-8")
    return backup_dir


# Write the report: summary numbers, a per-file table, then the verbatim removed text for every
# span (one identification line — file + 1-indexed line range — then the text, nothing else) so
# the whole removal can be read in full in one pass.
def write_report(path: Path, results: list[dict], total_files: int) -> None:
    changed = [r for r in results if r["changed"]]
    total_lines_removed = sum(r["lines_removed"] for r in results)
    total_chars_removed = sum(r["chars_removed"] for r in results)
    total_blocks = sum(len(r["blocks"]) for r in changed)

    o = [
        f"# Migration-Header Reclean Dry-Run Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nCorpus: {total_files} files · `data/documents/github_issues/`",
        "\n## Summary\n",
        "| Metric | Value |",
        "|---|---|",
        f"| Files that would change | {len(changed)} / {total_files} |",
        f"| Total spans removed | {total_blocks} |",
        f"| Total lines removed | {total_lines_removed} |",
        f"| Total chars removed | {total_chars_removed:,} |",
    ]

    if changed:
        o += [
            "\n## Per-File Results (changed files)\n",
            "| File | Spans | Lines removed | Chars removed |",
            "|---|---|---|---|",
        ]
        for r in sorted(changed, key=lambda x: x["filename"]):
            o.append(f"| `{r['filename']}` | {len(r['blocks'])} | "
                      f"{r['lines_removed']} | {r['chars_removed']:,} |")

        o += ["\n## Removed Spans (verbatim)\n"]
        for r in sorted(changed, key=lambda x: x["filename"]):
            for start, end in r["blocks"]:
                o.append(f"{r['filename']}:{start + 1}-{end + 1}")
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
                    "(class F). Dry-run by default"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    p.add_argument("--apply", action="store_true",
                    help="Overwrite files in place (creates timestamped backup first)")
    args = p.parse_args()
    reclean_workflow(args.source_dir, apply=args.apply)
