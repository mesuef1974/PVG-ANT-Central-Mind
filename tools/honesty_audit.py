#!/usr/bin/env python3
"""
Honesty guard for PVG-ANT Central Mind.

Enforces (heuristically):
  1. Every registry record is well-formed and classified (or has a status for book/planned).
  2. No forbidden upgrade phrase appears as a positive assertion.
  3. Every diagnostic card / skill ledger .md carries a classification stamp.

Exit 0 = PASS, 1 = FAIL. Stdlib only.  Usage: python tools/honesty_audit.py
"""
import os, re, sys, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED = {
    "Known", "Identity", "Reinterpretation", "Diagnostic", "Boundary",
    "Open Problem", "Candidate Mechanism", "New Theorem",
    "Missing Certificate", "Forbidden Claim",
}
# external_research_asset entries are asset pointers with a lifecycle status,
# not mathematical claims; vocabulary amendment recorded in
# governance/classification-system.md (GOVERNANCE-ENFORCEMENT-CLOSURE-001).
STATUS_KINDS = {"book", "planned", "frontier", "question", "external_research_asset"}

CLASSIFY_DIRS = ("installed-skills", "ledgers")

FORBIDDEN = [
    r"proves?\s+(the\s+)?rh", r"proof\s+of\s+rh", r"progress\s+toward",
    r"approaching\s+rh", r"break\s*through", r"secured\s+path",
    r"يبرهن\s+rh", r"تقدّم\s+نحو", r"اقتراب\s+من",
]
FORBIDDEN_RE = [re.compile(p, re.IGNORECASE) for p in FORBIDDEN]
NEG = re.compile(r"\bno\b|\bnot\b|\bnone\b|does not|n't|\bzero\b|\bnever\b|without|لا\s|بلا|دون|no-progress|forbidden", re.IGNORECASE)
CLASSIFY_RE = re.compile(r"classification", re.IGNORECASE)

FORBIDDEN_EXEMPT_DIRS = ("governance", "tools", "transition-memory")
FORBIDDEN_EXEMPT_FILES = {
    os.path.join("governance", "forbidden-claims.md"), "README.md",
    "central-mind-charter.md", "central-mind-goals.md",
    "PVG-ANT-Central-Mind-v0.1b-full-spec.md",
}


def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")


def validate_registries():
    problems, seen = [], {}
    for path in sorted(glob.glob(os.path.join(ROOT, "registries", "*.jsonl"))):
        with open(path, encoding="utf-8") as f:
            for i, raw in enumerate(f, 1):
                line = raw.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except json.JSONDecodeError as e:
                    problems.append(f"[registry] {rel(path)}:{i}: malformed JSON ({e})")
                    continue
                for fld in ("id", "kind", "title"):
                    if not o.get(fld):
                        problems.append(f"[registry] {rel(path)}:{i}: missing '{fld}'")
                kind = o.get("kind")
                if kind in STATUS_KINDS:
                    if not o.get("status"):
                        problems.append(f"[registry] {rel(path)}:{i}: {kind} missing 'status'")
                else:
                    cls = o.get("classification")
                    if not cls:
                        problems.append(f"[registry] {rel(path)}:{i}: missing 'classification'")
                    elif cls not in ALLOWED:
                        problems.append(f"[registry] {rel(path)}:{i}: unknown classification '{cls}'")
                rid = o.get("id")
                if rid:
                    if rid in seen:
                        problems.append(f"[registry] {rel(path)}:{i}: duplicate id '{rid}' (first {seen[rid]})")
                    else:
                        seen[rid] = f"{rel(path)}:{i}"
    return problems, set(seen)


def scan_markdown():
    problems = 0
    issues = []
    for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if os.sep + ".git" + os.sep in path:
            continue
        relp = rel(path)
        top = relp.split("/")[0]
        fname = os.path.basename(relp).lower()
        with open(path, encoding="utf-8") as f:
            text = f.read()
        # (3) classification stamp
        if top in CLASSIFY_DIRS and "template" not in fname and not CLASSIFY_RE.search(text):
            issues.append(f"[classify] {relp}: missing classification stamp")
        # (2) forbidden phrases
        exempt = top in FORBIDDEN_EXEMPT_DIRS or relp in {p.replace('\\', '/') for p in FORBIDDEN_EXEMPT_FILES}
        if not exempt:
            for i, line in enumerate(text.splitlines(), 1):
                if NEG.search(line):
                    continue
                for rx in FORBIDDEN_RE:
                    if rx.search(line):
                        issues.append(f"[forbidden] {relp}:{i}: {line.strip()[:80]}")
                        break
    return issues


def main():
    problems, ids = validate_registries()
    problems += scan_markdown()
    print(f"honesty_audit: {len(ids)} registry ids.")
    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for p in problems:
            print("  " + p)
        return 1
    print("PASS - no honesty violations detected (heuristic).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
