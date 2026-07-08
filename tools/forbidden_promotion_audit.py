#!/usr/bin/env python3
"""
Forbidden-promotion guard for PVG-ANT Central Mind.

A 'New Theorem' or 'Candidate Mechanism' must carry a real Certificate.
  - Registry entries with those classifications need a non-empty 'certificate' field.
  - Markdown whose own classification is one of those needs a non-trivial 'Certificate:' line.

Exit 0 = PASS, 1 = FAIL.  Usage: python tools/forbidden_promotion_audit.py
"""
import os, re, sys, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEEDS_CERT = ("New Theorem", "Candidate Mechanism")
TRIVIAL = {"", "-", "none", "missing", "pending", "n/a", "na", "tbd"}
CERT_RE = re.compile(r"certificate\s*[:=]\s*(.*)", re.IGNORECASE)
# an assertion that THIS file's classification IS one of the promoted kinds.
# Requires the value to START with the promoted stamp (after optional ** / spaces),
# so a template enumeration like "(Known/.../New Theorem/...)" does NOT match.
SELF_CLS_RE = re.compile(r"classification[^:\n]*[:=]\s*\*{0,2}\s*(New Theorem|Candidate Mechanism)\b", re.IGNORECASE)


def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")


def main():
    problems = []
    # registries
    for path in sorted(glob.glob(os.path.join(ROOT, "01-registries", "*.jsonl"))):
        with open(path, encoding="utf-8") as f:
            for i, raw in enumerate(f, 1):
                line = raw.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if o.get("classification") in NEEDS_CERT:
                    cert = str(o.get("certificate", "")).strip().lower()
                    if cert in TRIVIAL:
                        problems.append(f"[promo] {rel(path)}:{i}: {o.get('id')} is '{o.get('classification')}' without a certificate")
    # markdown
    for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if os.sep + ".git" + os.sep in path:
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        if SELF_CLS_RE.search(text):
            m = CERT_RE.search(text)
            val = (m.group(1).strip().lower() if m else "")
            val = re.sub(r"[*`.]", "", val).strip()
            if val in TRIVIAL:
                problems.append(f"[promo] {rel(path)}: classification is promoted but no real Certificate: field")
    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for p in problems:
            print("  " + p)
        return 1
    print("PASS - no unsupported promotions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
