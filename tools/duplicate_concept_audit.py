#!/usr/bin/env python3
"""
Duplicate-concept guard for PVG-ANT Central Mind.

Two different registry IDs sharing a normalized title are a likely duplicate
concept (pile, not graph). Flag them.

Exit 0 = PASS, 1 = FAIL.  Usage: python tools/duplicate_concept_audit.py
"""
import os, re, sys, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")


def norm(t): return re.sub(r"[^a-z0-9]", "", t.lower())


def main():
    by_norm = {}
    problems = []
    for path in sorted(glob.glob(os.path.join(ROOT, "registries", "*.jsonl"))):
        with open(path, encoding="utf-8") as f:
            for i, raw in enumerate(f, 1):
                line = raw.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                title, rid = o.get("title"), o.get("id")
                if not title or not rid:
                    continue
                key = (o.get("kind"), norm(title))
                if key in by_norm and by_norm[key][0] != rid:
                    problems.append(f"[dup-concept] '{title}' shared by {by_norm[key][0]} and {rid}")
                else:
                    by_norm.setdefault(key, (rid, f"{rel(path)}:{i}"))
    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for p in problems:
            print("  " + p)
        return 1
    print(f"PASS - no duplicate concepts across {len(by_norm)} titled entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
