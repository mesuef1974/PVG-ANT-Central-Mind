#!/usr/bin/env python3
"""Honesty guard for PVG-ANT Central Mind.

Enforces heuristically:
1. Every registry record is well formed and classified (or has a lifecycle status).
2. Canonical IDs are unique; ordered goal-state overrides are explicit replacements,
   not duplicate concept definitions.
3. No forbidden upgrade phrase appears as a positive assertion.
4. Every diagnostic card / skill ledger markdown carries a classification stamp.

Exit 0 = PASS, 1 = FAIL. Stdlib only.
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED = {
    "Known", "Identity", "Reinterpretation", "Diagnostic", "Boundary",
    "Open Problem", "Candidate Mechanism", "New Theorem",
    "Missing Certificate", "Forbidden Claim",
}
STATUS_KINDS = {"book", "planned", "frontier", "question", "external_research_asset"}
CLASSIFY_DIRS = ("installed-skills", "ledgers")
FORBIDDEN = [
    r"proves?\s+(the\s+)?rh", r"proof\s+of\s+rh", r"progress\s+toward",
    r"approaching\s+rh", r"break\s*through", r"secured\s+path",
    r"يبرهن\s+rh", r"تقدّم\s+نحو", r"اقتراب\s+من",
]
FORBIDDEN_RE = [re.compile(pattern, re.IGNORECASE) for pattern in FORBIDDEN]
NEG = re.compile(
    r"\bno\b|\bnot\b|\bnone\b|does not|n't|\bzero\b|\bnever\b|without|"
    r"لا\s|بلا|دون|no-progress|forbidden",
    re.IGNORECASE,
)
CLASSIFY_RE = re.compile(r"classification", re.IGNORECASE)
FORBIDDEN_EXEMPT_DIRS = ("governance", "tools", "transition-memory")
FORBIDDEN_EXEMPT_FILES = {
    os.path.join("governance", "forbidden-claims.md"),
    "README.md",
    "central-mind-charter.md",
    "central-mind-goals.md",
    "PVG-ANT-Central-Mind-v0.1b-full-spec.md",
}


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT).replace("\\", "/")


def is_goal_override(path: str) -> bool:
    return os.path.basename(path).startswith("goal-state-overrides-")


def validate_row(path: str, line_number: int, row: object) -> list[str]:
    problems: list[str] = []
    if not isinstance(row, dict):
        return [f"[registry] {rel(path)}:{line_number}: row is not a JSON object"]
    for field in ("id", "kind", "title"):
        if not row.get(field):
            problems.append(f"[registry] {rel(path)}:{line_number}: missing '{field}'")
    kind = row.get("kind")
    if kind in STATUS_KINDS:
        if not row.get("status"):
            problems.append(f"[registry] {rel(path)}:{line_number}: {kind} missing 'status'")
    else:
        classification = row.get("classification")
        if not classification:
            problems.append(f"[registry] {rel(path)}:{line_number}: missing 'classification'")
        elif classification not in ALLOWED:
            problems.append(
                f"[registry] {rel(path)}:{line_number}: unknown classification "
                f"'{classification}'"
            )
    return problems


def read_registry(path: str) -> tuple[list[tuple[int, dict[str, object]]], list[str]]:
    rows: list[tuple[int, dict[str, object]]] = []
    problems: list[str] = []
    with open(path, encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, 1):
            if not raw.strip():
                continue
            try:
                value = json.loads(raw)
            except json.JSONDecodeError as error:
                problems.append(
                    f"[registry] {rel(path)}:{line_number}: malformed JSON ({error})"
                )
                continue
            problems.extend(validate_row(path, line_number, value))
            if isinstance(value, dict):
                rows.append((line_number, value))
    return rows, problems


def validate_registries() -> tuple[list[str], set[str]]:
    problems: list[str] = []
    canonical_seen: dict[str, str] = {}
    override_seen: dict[str, str] = {}
    paths = sorted(glob.glob(os.path.join(ROOT, "registries", "*.jsonl")))

    for path in (path for path in paths if not is_goal_override(path)):
        rows, row_problems = read_registry(path)
        problems.extend(row_problems)
        for line_number, row in rows:
            registry_id = str(row.get("id", ""))
            if not registry_id:
                continue
            location = f"{rel(path)}:{line_number}"
            if registry_id in canonical_seen:
                problems.append(
                    f"[registry] {location}: duplicate id '{registry_id}' "
                    f"(first {canonical_seen[registry_id]})"
                )
            else:
                canonical_seen[registry_id] = location

    for path in (path for path in paths if is_goal_override(path)):
        rows, row_problems = read_registry(path)
        problems.extend(row_problems)
        for line_number, row in rows:
            registry_id = str(row.get("id", ""))
            if not registry_id:
                continue
            location = f"{rel(path)}:{line_number}"
            if registry_id in override_seen:
                problems.append(
                    f"[registry] {location}: duplicate goal-state override id "
                    f"'{registry_id}' (first {override_seen[registry_id]})"
                )
            else:
                override_seen[registry_id] = location
            canonical_seen.setdefault(registry_id, location)

    return problems, set(canonical_seen)


def scan_markdown() -> list[str]:
    issues: list[str] = []
    exempt_files = {path.replace("\\", "/") for path in FORBIDDEN_EXEMPT_FILES}
    for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if os.sep + ".git" + os.sep in path:
            continue
        relative_path = rel(path)
        top = relative_path.split("/")[0]
        filename = os.path.basename(relative_path).lower()
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        if top in CLASSIFY_DIRS and "template" not in filename and not CLASSIFY_RE.search(text):
            issues.append(f"[classify] {relative_path}: missing classification stamp")
        exempt = top in FORBIDDEN_EXEMPT_DIRS or relative_path in exempt_files
        if exempt:
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            if NEG.search(line):
                continue
            for expression in FORBIDDEN_RE:
                if expression.search(line):
                    issues.append(
                        f"[forbidden] {relative_path}:{line_number}: {line.strip()[:80]}"
                    )
                    break
    return issues


def main() -> int:
    problems, ids = validate_registries()
    problems += scan_markdown()
    print(f"honesty_audit: {len(ids)} registry ids; goal-state overrides resolved as replacements.")
    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for problem in problems:
            print("  " + problem)
        return 1
    print("PASS - no honesty violations detected (heuristic).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
