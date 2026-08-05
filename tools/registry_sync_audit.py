#!/usr/bin/env python3
"""Registry-to-markdown synchronization audit.

Canonical IDs must be unique across ordinary registries. Ordered
`goal-state-overrides-*.jsonl` files are explicit state replacements for goal
IDs already present in the base goal registry and therefore are not duplicate
concept definitions.
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ID_RE = re.compile(
    r"(?<![A-Z0-9-])(?:WALL|TOOL|RULE|BOOK|OBS|CLAIM|CONSTRAINT|SKILL)-"
    r"[A-Z0-9]+(?:-[A-Z0-9]+)*"
)
PLACEHOLDERS = {
    "WALL-ID",
    "TOOL-ID",
    "RULE-ID",
    "BOOK-ID",
    "OBS-ID",
    "CLAIM-ID",
    "SKILL-ID",
}
SKIP_DIRS = ()
SKIP_FILES = {"PVG-ANT-Central-Mind-v0.1b-full-spec.md"}


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT).replace("\\", "/")


def is_goal_override(path: str) -> bool:
    return os.path.basename(path).startswith("goal-state-overrides-")


def load_ids() -> tuple[set[str], list[str]]:
    ids: dict[str, str] = {}
    dups: list[str] = []
    override_ids: set[str] = set()
    paths = sorted(glob.glob(os.path.join(ROOT, "registries", "*.jsonl")))

    # Ordinary registries define canonical IDs.
    for path in (path for path in paths if not is_goal_override(path)):
        with open(path, encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, 1):
                line = raw.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                registry_id = row.get("id")
                if not registry_id:
                    continue
                if registry_id in ids:
                    dups.append(
                        f"[dup] {registry_id}: {ids[registry_id]} and {rel(path)}:{line_number}"
                    )
                else:
                    ids[registry_id] = f"{rel(path)}:{line_number}"

    # Goal-state override rows may replace an existing goal ID or introduce a
    # newly authorized goal. Repeating an ID inside the override layer itself
    # remains an error because override order would then become ambiguous.
    for path in (path for path in paths if is_goal_override(path)):
        with open(path, encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, 1):
                line = raw.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                registry_id = row.get("id")
                if not registry_id:
                    continue
                if registry_id in override_ids:
                    dups.append(
                        f"[duplicate-override] {registry_id}: repeated at {rel(path)}:{line_number}"
                    )
                    continue
                override_ids.add(registry_id)
                ids.setdefault(registry_id, f"{rel(path)}:{line_number}")

    return set(ids), dups


def main() -> int:
    ids, dups = load_ids()
    problems = list(dups)
    for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if os.sep + ".git" + os.sep in path:
            continue
        relative_path = rel(path)
        if (
            relative_path.split("/")[0] in SKIP_DIRS
            or os.path.basename(relative_path) in SKIP_FILES
            or relative_path.endswith("-template.md")
        ):
            continue
        with open(path, encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                for token in ID_RE.findall(line):
                    if token in PLACEHOLDERS or token in ids:
                        continue
                    problems.append(
                        f"[unknown-id] {relative_path}:{line_number}: {token}"
                    )
    print(
        f"registry_sync_audit: {len(ids)} ids, scanned markdown; "
        f"{len(override_ids_for_report())} explicit goal-state overrides."
    )
    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for problem in problems:
            print("  " + problem)
        return 1
    print("PASS - registry and markdown are in sync; override rows are state replacements.")
    return 0


def override_ids_for_report() -> set[str]:
    out: set[str] = set()
    for path in sorted(glob.glob(os.path.join(ROOT, "registries", "goal-state-overrides-*.jsonl"))):
        with open(path, encoding="utf-8") as handle:
            for raw in handle:
                if not raw.strip():
                    continue
                try:
                    row = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                if row.get("id"):
                    out.add(str(row["id"]))
    return out


if __name__ == "__main__":
    sys.exit(main())
