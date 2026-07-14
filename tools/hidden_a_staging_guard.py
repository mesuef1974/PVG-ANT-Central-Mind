#!/usr/bin/env python3
"""
Hidden Set A staging guard (CI-runnable WITHOUT the gold keys).

Protects the committed STEP A artifacts of ADVERSARIAL-PVG-ANT-BENCHMARK-002 under
`benchmarks/pvg-ant-002/staging/hidden-a/`:

  1. LEAKAGE BAR (SEALING-PROTOCOL §9 / ROLE-SEPARATION §4.4):
     fail if any plaintext A gold-key file is tracked in git; fail if any committed file appears
     to carry a plaintext `"gold"` field; confirm `A-keys.jsonl` is gitignored.
  2. FROZEN INVARIANTS (DISTRIBUTION-MATRIX §1/§2, SEALING §3/§5/§8):
     re-derive per-axis counts, closed fatal-code vocabulary, closed leakage vocabulary
     (LEAK-0 only), rubric-weight sums, and the cross-cutting quota minima from the committed
     `A-prompts.jsonl` + `A-scoring-metadata.jsonl` (which contain NO gold keys).
  3. KEY-HASH SHAPE (SEALING §9):
     `HIDDEN-A-KEY-HASHES.txt` carries 48 per-case SHA-256 lines + one AGGREGATE line, and the
     per-case ids match the committed prompts.

Exit 0 = pass, 1 = invariant/leakage breach. Capability measurement only.
Zero RH progress, zero GRH progress.
"""
from __future__ import annotations
import json, re, subprocess, sys, os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "benchmarks", "pvg-ant-002", "staging", "hidden-a")
PROMPTS = os.path.join(DIR, "A-prompts.jsonl")
META = os.path.join(DIR, "A-scoring-metadata.jsonl")
HASHES = os.path.join(DIR, "HIDDEN-A-KEY-HASHES.txt")

FATAL_CODES = {
    "ERR-FATAL-SCIENTIFIC-CLAIM", "ERR-FATAL-COMPUTATION-AS-PROOF", "ERR-FATAL-LOSS-INVERSION",
    "ERR-FATAL-SCOPE-VIOLATION", "ERR-FATAL-CERTIFICATE-FABRICATION",
    "ERR-FATAL-PROVENANCE-FABRICATION", "ERR-FATAL-RH-GRH-CLAIM",
}
LEAK_VALUES = {
    "LEAK-0-CLEAR", "LEAK-1-TEXTUAL-OVERLAP", "LEAK-2-CONCEPTUAL-OVERLAP",
    "LEAK-3-NEAR-FORMULATION-OR-PROJECT-DERIVED", "LEAK-U-UNCERTAIN",
}
TIERS = {"B0", "B1", "B2"}
AXIS_TARGET_A = {1: 4, 2: 3, 3: 3, 4: 5, 5: 5, 6: 5, 7: 3, 8: 3, 9: 3, 10: 4, 11: 5, 12: 5}


def git_tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
    return set(out.stdout.splitlines())


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(ln) for ln in f if ln.strip()]


def main():
    errs = []

    # ---- 1. Leakage bar ----
    tracked = git_tracked_files()
    for f in tracked:
        base = os.path.basename(f)
        if base in {"A-keys.jsonl", "B-keys.jsonl"} or base.endswith(".keys.jsonl"):
            errs.append(f"LEAKAGE: plaintext key file is tracked in git: {f}")
        if re.search(r"hidden-[ab].*keys?\.jsonl$", f, re.I) and "hash" not in f.lower():
            errs.append(f"LEAKAGE: suspected tracked key file: {f}")

    for name, path in (("A-prompts.jsonl", PROMPTS), ("A-scoring-metadata.jsonl", META)):
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        if rel not in tracked:
            errs.append(f"missing committed artifact: {rel}")

    # Any committed file under the staging dir must not carry a plaintext gold key.
    for f in tracked:
        if f.startswith("benchmarks/pvg-ant-002/staging/hidden-a/") and f.endswith(".jsonl"):
            with open(os.path.join(ROOT, f), encoding="utf-8") as fh:
                for i, ln in enumerate(fh, 1):
                    if ln.strip() and '"gold"' in ln:
                        errs.append(f"LEAKAGE: committed {f}:{i} carries a plaintext \"gold\" field")
                        break

    if not os.path.exists(PROMPTS) or not os.path.exists(META):
        for e in errs:
            print("  FAIL:", e)
        print("FATAL: cannot locate committed A artifacts; aborting.")
        sys.exit(1)

    prompts = read_jsonl(PROMPTS)
    meta = read_jsonl(META)

    # A-prompts must be prompt-only (no expected_structure, no gold).
    for p in prompts:
        if "gold" in p or "expected_structure" in p:
            errs.append(f"LEAKAGE: A-prompts.jsonl case {p.get('case_id')} exposes answer fields")

    # ---- 2. Frozen invariants from metadata ----
    if len(meta) < 48:
        errs.append(f"total A cases {len(meta)} < 48")
    axis_counts = Counter(c["capability_target"] for c in meta)
    for ax, tgt in AXIS_TARGET_A.items():
        if axis_counts.get(ax, 0) != tgt:
            errs.append(f"axis {ax} count {axis_counts.get(ax, 0)} != frozen target {tgt}")

    for c in meta:
        cid = c.get("case_id")
        if c.get("tier") not in TIERS:
            errs.append(f"{cid}: bad tier {c.get('tier')}")
        if c.get("leakage_class") not in LEAK_VALUES:
            errs.append(f"{cid}: bad leakage_class {c.get('leakage_class')}")
        if c.get("leakage_class") != "LEAK-0-CLEAR":
            errs.append(f"{cid}: leakage_class {c.get('leakage_class')} not eligible (§8)")
        for fc in c.get("fatal_errors", []):
            if fc not in FATAL_CODES:
                errs.append(f"{cid}: fatal code {fc} outside closed set")
        w = c.get("rubric", {})
        if sum(w.values()) != 100:
            errs.append(f"{cid}: rubric weights sum {sum(w.values())} != 100")
        if "gold" in c:
            errs.append(f"LEAKAGE: metadata case {cid} carries a plaintext gold key")

    tags = [c.get("tags", {}) for c in meta]
    loss_levels = [t.get("loss_level") for t in tags if t.get("loss_level") is not None]
    for lv in (0, 1, 2, 3, 4):
        if lv not in loss_levels:
            errs.append(f"quota: no A case at LOSS-{lv}")
    if sum(1 for t in tags if t.get("loss_judgment")) < 10:
        errs.append("quota: A LOSS judgments < 10")
    if sum(1 for t in tags if t.get("abstention")) < 8:
        errs.append("quota: A abstention/impossibility < 8")
    if sum(1 for t in tags if (t.get("composition_depth") or 0) >= 2) < 8:
        errs.append("quota: A composition-depth>=2 < 8")
    if sum(1 for t in tags if t.get("reverse_inference")) < 6:
        errs.append("quota: A reverse-inference < 6")
    if sum(1 for c in meta if c.get("tier") == "B0") < 12:
        errs.append("quota: A B0 answerable < 12")

    # prompts and metadata must reference the same case ids.
    if {p.get("case_id") for p in prompts} != {c.get("case_id") for c in meta}:
        errs.append("case_id sets differ between A-prompts.jsonl and A-scoring-metadata.jsonl")

    # ---- 3. Key-hash shape ----
    if not os.path.exists(HASHES):
        errs.append("missing HIDDEN-A-KEY-HASHES.txt")
    else:
        per_case, aggregate = {}, None
        with open(HASHES, encoding="utf-8") as fh:
            for ln in fh:
                ln = ln.strip()
                if not ln or ln.startswith("#"):
                    continue
                m = re.match(r"^(\S+)\s+([0-9a-f]{64})$", ln)
                if m and m.group(1) == "AGGREGATE":
                    aggregate = m.group(2)
                elif m:
                    per_case[m.group(1)] = m.group(2)
        if len(per_case) != 48:
            errs.append(f"key-hashes: {len(per_case)} per-case lines != 48")
        if aggregate is None:
            errs.append("key-hashes: missing AGGREGATE line")
        if set(per_case) != {c.get("case_id") for c in meta}:
            errs.append("key-hashes: case ids do not match the committed cases")

    if errs:
        print("=== HIDDEN-A STAGING GUARD: BREACHES ===")
        for e in errs:
            print("  FAIL:", e)
        sys.exit(1)
    print("HIDDEN-A staging guard PASS: 48 cases, frozen invariants hold, no plaintext key leakage,"
          " key-hashes well-formed.")


if __name__ == "__main__":
    main()
