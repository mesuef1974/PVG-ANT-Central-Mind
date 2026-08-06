#!/usr/bin/env python3
"""Prevent placeholder-filled records from being presented as completed assimilation."""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RMG_REGISTRY = "research/research-memory-graph/registry/"
ACTIVATION_BASE = os.environ.get("RMG_POLICY_BASE_REF", "78ed2fa1da04ceb55fc50a03688842cb90466da3")
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
    commands = [
        ["git", "diff", "--name-only", f"{ACTIVATION_BASE}...HEAD"],
        ["git", "diff", "--name-only", "HEAD^", "HEAD"],
    ]
    output = ""
    for command in commands:
        try:
            output = subprocess.check_output(command, cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
            break
        except subprocess.CalledProcessError:
            continue
    return [
        ROOT / line
        for line in output.splitlines()
        if line.startswith(RMG_REGISTRY) and line.endswith(".jsonl") and (ROOT / line).exists()
    ]


def records(path: Path):
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            yield line_no, json.loads(line)


def rank(level: str) -> int:
    if level.startswith("ASSIM-L") and level[-1:].isdigit():
        return int(level[-1])
    return -1


def semantic_status(value: Any) -> str:
    """Extract a semantic status from scalar or structured adapter output."""
    if isinstance(value, dict):
        for key in ("status", "value", "classification"):
            if key in value:
                return semantic_status(value[key])
        return ""
    if isinstance(value, list):
        statuses = [semantic_status(item) for item in value]
        return next((status for status in statuses if status in PLACEHOLDERS), "")
    return str(value)


def main() -> int:
    failed = False
    files = changed_paths()
    if not files:
        print("PASS: no changed canonical RMG registries requiring semantic audit")
        return 0
    for path in files:
        for line_no, record in records(path):
            level = str(record.get("assimilation_level", ""))
            placeholders = sorted(
                field for field in SEMANTIC_FIELDS
                if semantic_status(record.get(field, "")) in PLACEHOLDERS
            )
            if placeholders and rank(level) >= 3:
                failed = True
                print(
                    f"FAIL {path.relative_to(ROOT)}:{line_no}: {level} cannot coexist "
                    f"with unresolved fields: {', '.join(placeholders)}"
                )
            else:
                print(f"PASS {path.relative_to(ROOT)}:{line_no}: semantic ceiling respected")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
