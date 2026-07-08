#!/usr/bin/env python3
"""
Registry <-> markdown sync audit for PVG-ANT Central Mind.

  - Every registry ID is unique across all registries/*.jsonl.
  - Every ID token referenced in markdown exists in a registry.
This is the graph-not-pile enforcer.

Exit 0 = PASS, 1 = FAIL.  Usage: python tools/registry_sync_audit.py
"""
import os, re, sys, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Prefixes tracked as canonical registry IDs. MC- (missing certificates) is
# certificate-ledger-internal and intentionally excluded.
ID_RE = re.compile(r"\b(?:WALL|TOOL|RULE|BOOK|OBS|CLAIM|CONSTRAINT|SKILL)-[A-Z0-9]+(?:-[A-Z0-9]+)*")
PLACEHOLDERS = {"WALL-ID", "TOOL-ID", "RULE-ID", "BOOK-ID", "OBS-ID", "CLAIM-ID", "SKILL-ID"}
SKIP_DIRS = ()
# Planning/spec docs and templates hold proposed or placeholder IDs; not live references.
SKIP_FILES = {"PVG-ANT-Central-Mind-v0.1b-full-spec.md"}


def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")


def load_ids():
    ids, dups = {}, []
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
                rid = o.get("id")
                if not rid:
                    continue
                if rid in ids:
                    dups.append(f"[dup] {rid}: {ids[rid]} and {rel(path)}:{i}")
                else:
                    ids[rid] = f"{rel(path)}:{i}"
    return set(ids), dups


def main():
    ids, dups = load_ids()
    problems = list(dups)
    for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if os.sep + ".git" + os.sep in path:
            continue
        relp = rel(path)
        if (relp.split("/")[0] in SKIP_DIRS or os.path.basename(relp) in SKIP_FILES
                or relp.endswith("-template.md")):
            continue
        with open(path, encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                for tok in ID_RE.findall(line):
                    if tok in PLACEHOLDERS or tok in ids:
                        continue
                    problems.append(f"[unknown-id] {relp}:{i}: {tok}")
    print(f"registry_sync_audit: {len(ids)} ids, scanned markdown.")
    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for p in problems:
            print("  " + p)
        return 1
    print("PASS - registry and markdown are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
