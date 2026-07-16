#!/usr/bin/env python3
"""Prevent placeholder-filled records from being presented as completed assimilation."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RMG_REGISTRY = "research/research-memory-graph/registry/"
PLACEHOLDERS = {"NOT_YET_ANALYSED", "NOT_YET_ANALYZED", "UNMAPPED_LEGACY_VALUE", "AMBIGUOUS_REQUIRES_REVIEW"}
SEMANTIC_FIELDS = {
    "ant_standard_definition",
    "ant_to_pvg_map",
    "pvg_geometric_object",
    "pvg_to_ant_return_map",
    "translation_type",
    "injectivity_status",
    "kernel_or_information_loss",
}


def changed_paths() -> list[Path]:
    for command in (["git", "diff", "--name-only", "origin/main...HEAD"], ["git", "diff", "--name-only", "HEAD^", "HEAD"]):
        try:
            output = subprocess.check_output(command, cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
            break
        except subprocess.CalledProcessError:
            output = ""
    return [ROOT / line for line in output.splitlines() if line.startswith(RMG_REGISTRY) and line.endswith(".jsonl") and (ROOT / line).exists()]


def records(path: Path):
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            yield line_no, json.loads(line)


def rank(level: str) -> int:
    if level.startswith("ASSIM-L") and level[-1:].isdigit():
        return int(level[-1])
    return -1


def main() -> int:
    failed = False
    files = changed_paths()
    if not files:
        print("PASS: no changed canonical RMG registries requiring semantic audit")
        return 0
    for path in files:
        for line_no, record in records(path):
            level = str(record.get("assimilation_level", ""))
            placeholders = sorted(field for field in SEMANTIC_FIELDS if str(record.get(field, "")) in PLACEHOLDERS)
            if placeholders and rank(level) >= 3:
                failed = True
                print(f"FAIL {path.relative_to(ROOT)}:{line_no}: {level} cannot coexist with unresolved fields: {', '.join(placeholders)}")
            else:
                print(f"PASS {path.relative_to(ROOT)}:{line_no}: semantic ceiling respected")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
