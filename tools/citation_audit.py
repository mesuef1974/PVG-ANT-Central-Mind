#!/usr/bin/env python3
"""
Citation guard for PVG-ANT Central Mind.

Every book ledger folder (03-skill-ledgers/{ant,logic,sieve,...}/<book>/) that
has an index.md must cite a Source and a BOOK-* id present in books.jsonl.

Exit 0 = PASS, 1 = FAIL.  Usage: python tools/citation_audit.py
"""
import os, re, sys, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK_RE = re.compile(r"BOOK-[A-Z0-9]+(?:-[A-Z0-9]+)*")


def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")


def book_ids():
    ids = set()
    p = os.path.join(ROOT, "registries", "books.jsonl")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        ids.add(json.loads(line)["id"])
                    except (json.JSONDecodeError, KeyError):
                        pass
    return ids


def main():
    ids = book_ids()
    problems = []
    # book-ledger README files live at ledgers/books/<BOOK-ID>/README.md
    for idx in glob.glob(os.path.join(ROOT, "ledgers", "books", "*", "README.md")):
        relp = rel(idx)
        with open(idx, encoding="utf-8") as f:
            text = f.read()
        if "Source" not in text:
            problems.append(f"[cite] {relp}: no 'Source' block")
        found = [b for b in BOOK_RE.findall(text) if b in ids]
        if not found:
            problems.append(f"[cite] {relp}: no valid BOOK-* id from books.jsonl")
    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for p in problems:
            print("  " + p)
        return 1
    print("PASS - all book ledgers cite a registered source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
