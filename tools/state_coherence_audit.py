#!/usr/bin/env python3
"""state_coherence_audit.py -- repository-truth checker (Coherence PASS).

Not a mathematical-completeness checker. It fails on stale-state contradictions
between the audits, book READMEs, registries, transition-memory, and unit files:
closure<->README, registry<->ledger, transition-memory truth, unit-existence vs
"No MNTII-006-X" phrases, and the quarantine markers for a pre-packet unit.

stdlib only. Run from anywhere: python tools/state_coherence_audit.py
"""
import os
import sys
import glob
import re
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONT = "ledgers/books/BOOK-ANT-MONTGOMERY-MNT-II-004"


def read(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


issues = []


def need(cond, msg):
    if not cond:
        issues.append(msg)


def closure_pass(name):
    t = read(os.path.join("audits", name))
    return t is not None and "PASS" in t


def book_readme(book):
    return read(os.path.join("ledgers/books", book, "README.md")) or ""


# 1. root README mentions the current phase
readme = read("README.md") or ""
need(("Coherence Audit 005" in readme) or ("v0.6" in readme),
     "README.md does not mention the current phase (Coherence Audit 005 / v0.6)")

# 2. latest-state is not stuck in an old era
latest = read("transition-memory/latest-state.md") or ""
need(("Montgomery" in latest) or ("v0.6" in latest),
     "transition-memory/latest-state.md is stale (no v0.6 / Montgomery)")

# 3. next-action reflects the actual next action
nexta = read("transition-memory/next-action.md") or ""
need(("Intake" in nexta) or ("Coherence Audit 005" in nexta),
     "transition-memory/next-action.md does not reflect the actual next action")

# 8. planned.jsonl empty must be reflected in next-action
planned = read("registries/planned.jsonl") or ""
if planned.strip() == "":
    need("planned.jsonl" in nexta,
         "planned.jsonl is empty but transition-memory/next-action.md does not reflect it")

# 4/5/6. closure PASS must not coexist with a scope-open / awaiting book README
if closure_pass("v0.2-B-closure.md"):
    need("awaiting" not in book_readme("BOOK-LOGIC-MILETI-001").lower(),
         "Mileti README says 'awaiting' but v0.2-B-closure.md is PASS")
if closure_pass("v0.4-closure.md"):
    t = book_readme("BOOK-ANT-IWANIEC-KOWALSKI-003").lower()
    need("scope open" not in t and "scope_open" not in t and "awaiting" not in t,
         "IK README says 'scope open'/'awaiting' but v0.4-closure.md is PASS")
if closure_pass("v0.5-closure.md"):
    t = book_readme("BOOK-SIEVE-HARMAN-004").lower()
    need("scope open" not in t and "scope_open" not in t and "awaiting" not in t,
         "Harman README says 'scope open'/'awaiting' but v0.5-closure.md is PASS")

# Montgomery: which units actually exist
unit_files = sorted(glob.glob(os.path.join(ROOT, MONT, "units", "MNTII-006-*.md")))
letters = []
for u in unit_files:
    m = re.search(r"MNTII-006-([A-Z])\.md$", os.path.basename(u))
    if m:
        letters.append(m.group(1))
mont_readme = read(os.path.join(MONT, "README.md")) or ""

# 7. Montgomery README must mention every existing unit
for L in letters:
    need(("006-%s" % L) in mont_readme,
         "Montgomery README does not mention existing unit %s" % L)

# 9. no stale 'No MNTII-006-<L>' for a unit that exists
for p in glob.glob(os.path.join(ROOT, MONT, "*.md")) + glob.glob(os.path.join(ROOT, MONT, "units", "*.md")):
    with open(p, encoding="utf-8", errors="replace") as f:
        t = f.read()
    for L in letters:
        need(("No MNTII-006-%s" % L) not in t,
             "stale 'No MNTII-006-%s' in %s while that unit exists" % (L, os.path.relpath(p, ROOT)))

# 10. registry book status must not contradict unit/audit files
books = read("registries/books.jsonl") or ""
mont_line = ""
for line in books.splitlines():
    if "BOOK-ANT-MONTGOMERY-MNT-II-004" in line:
        mont_line = line
if letters:
    need('"status": "scope_open"' not in mont_line,
         "books.jsonl Montgomery status is still 'scope_open' but units exist")
    need("partial_overlay" in mont_line,
         "books.jsonl Montgomery should be 'partial_overlay' (has units, overlay in progress)")

# E QUARANTINE: E exists without a closure -> must be marked quarantined, never trusted/closed
e_exists = os.path.isfile(os.path.join(ROOT, MONT, "units", "MNTII-006-E.md"))
e_closed = os.path.isfile(os.path.join(ROOT, "audits", "v0.6-e-closure.md"))
if e_exists and not e_closed:
    qwords = ("quarantin", "unvalidated", "pre-packet", "pending validation")
    for rel in [os.path.join(MONT, "README.md"), "registries/books.jsonl", "transition-memory/next-action.md"]:
        t = (read(rel) or "").lower()
        need(any(q in t for q in qwords),
             "unit E exists without closure but %s does not mark E quarantined/unvalidated/pre-packet" % rel)
    try:
        obj = json.loads(mont_line) if mont_line.strip() else {}
    except Exception:
        obj = {}
    need("E" not in str(obj.get("trusted_closed_units", "")),
         "books.jsonl lists quarantined unit E among trusted_closed_units")
    need("E" in str(obj.get("quarantined_units", "")),
         "books.jsonl does not list unit E under quarantined_units")

if issues:
    print("FAIL - %d state-coherence issue(s):" % len(issues))
    for i in issues:
        print("  [coherence]", i)
    sys.exit(1)
print("PASS - state coherence: repository state files are consistent (repository-truth check).")
sys.exit(0)
