#!/usr/bin/env python3
"""Enforce the canonical RMG schema on newly added or modified registry files only.

Historical registry debt remains visible and scheduled for migration; this guard prevents
that debt from growing while avoiding an immediate repository-wide false closure.
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "research/research-memory-graph/code/enforce_rmg_new_record_policy.py"
RMG_REGISTRY = "research/research-memory-graph/registry/"


def changed_files() -> list[Path]:
    candidates = []
    commands = [
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        ["git", "diff", "--name-only", "HEAD^", "HEAD"],
    ]
    output = None
    for command in commands:
        try:
            output = subprocess.check_output(command, cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
            break
        except subprocess.CalledProcessError:
            continue
    if output is None:
        raise RuntimeError("unable to determine changed files")
    for raw in output.splitlines():
        if raw.startswith(RMG_REGISTRY) and raw.endswith((".json", ".jsonl")):
            path = ROOT / raw
            if path.exists():
                candidates.append(path)
    return candidates


def load_policy():
    spec = importlib.util.spec_from_file_location("rmg_policy", POLICY)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load RMG policy hook")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    policy = load_policy()
    files = changed_files()
    if not files:
        print("PASS: no changed RMG registry files")
        return 0
    failed = False
    for path in files:
        records = list(policy.iter_records(path))
        for index, record in enumerate(records, 1):
            errors = policy.validate(record)
            if errors:
                failed = True
                print(f"FAIL {path.relative_to(ROOT)} record {index}: {' | '.join(errors)}")
            else:
                print(f"PASS {path.relative_to(ROOT)} record {index}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
