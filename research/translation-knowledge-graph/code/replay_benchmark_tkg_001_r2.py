#!/usr/bin/env python3
"""Create a byte-exact replay evidence bundle for BENCHMARK-TKG-001-R2.

Run this script only from a real Git checkout. It records the exact HEAD, dirty
state, SHA-256 and Git blob SHA-1 for every executed source, commands, stdout,
stderr, exit codes, and the generated benchmark report.

A successful replay certifies only the declared routing and bounded-semantic
cases. It never certifies a mathematical theorem or promotes MATH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
TKG_ROOT = ROOT / "research" / "translation-knowledge-graph"
CODE = TKG_ROOT / "code"
REGISTRY = TKG_ROOT / "registry" / "benchmark-tkg-001-r2.jsonl"
REPORT = TKG_ROOT / "reports" / "benchmark-tkg-001-r2-byte-exact-report.json"
EVIDENCE = TKG_ROOT / "reports" / "benchmark-tkg-001-r2-byte-exact-evidence.json"

EXECUTED_FILES = [
    CODE / "query_reasoning_orchestrator_001.py",
    CODE / "query_reasoning_semantic_r2.py",
    CODE / "run_benchmark_tkg_001_r2.py",
    CODE / "verify_benchmark_tkg_001_r2.py",
    REGISTRY,
]


def run_command(argv: list[str], cwd: Path = ROOT) -> dict[str, Any]:
    proc = subprocess.run(argv, cwd=cwd, text=True, capture_output=True, check=False)
    return {
        "argv": argv,
        "cwd": str(cwd),
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def require_git_checkout() -> tuple[str, str]:
    inside = run_command(["git", "rev-parse", "--is-inside-work-tree"])
    if inside["exit_code"] != 0 or inside["stdout"].strip() != "true":
        raise SystemExit("A real Git checkout is required.")
    head = run_command(["git", "rev-parse", "HEAD"])
    status = run_command(["git", "status", "--porcelain=v1"])
    if head["exit_code"] != 0 or status["exit_code"] != 0:
        raise SystemExit("Unable to read Git HEAD/status.")
    return head["stdout"].strip(), status["stdout"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob_sha(path: Path) -> str:
    result = run_command(["git", "hash-object", str(path.relative_to(ROOT))])
    if result["exit_code"] != 0:
        raise RuntimeError(result["stderr"])
    return result["stdout"].strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-dirty", action="store_true")
    args = parser.parse_args()

    head, dirty = require_git_checkout()
    if dirty and not args.allow_dirty:
        raise SystemExit("Working tree is dirty; commit or clean changes before replay.")

    missing = [str(p) for p in EXECUTED_FILES if not p.is_file()]
    if missing:
        raise SystemExit(f"Missing executed files: {missing}")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    runner_cmd = [
        sys.executable,
        str(CODE / "run_benchmark_tkg_001_r2.py"),
        "--output",
        str(REPORT),
    ]
    verifier_cmd = [sys.executable, str(CODE / "verify_benchmark_tkg_001_r2.py")]

    runner = run_command(runner_cmd)
    verifier = run_command(verifier_cmd)

    files = {}
    for path in EXECUTED_FILES:
        rel = str(path.relative_to(ROOT))
        files[rel] = {
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
            "git_blob_sha1": git_blob_sha(path),
        }

    generated_report = None
    if REPORT.is_file():
        generated_report = {
            "path": str(REPORT.relative_to(ROOT)),
            "sha256": sha256(REPORT),
            "size_bytes": REPORT.stat().st_size,
        }

    evidence = {
        "evidence_id": "BENCHMARK-TKG-001-R2-BYTE-EXACT-REPLAY",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository_root": str(ROOT),
        "git_head": head,
        "working_tree_dirty": bool(dirty),
        "working_tree_status": dirty,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "executable": sys.executable,
            "cwd": os.getcwd(),
        },
        "executed_files": files,
        "commands": {
            "runner": runner,
            "verifier": verifier,
        },
        "generated_report": generated_report,
        "overall_pass": runner["exit_code"] == 0 and verifier["exit_code"] == 0,
        "scientific_claims_certified": False,
        "math_status": "MATH-M0",
        "benchmark_sealed": False,
    }
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True))
    raise SystemExit(0 if evidence["overall_pass"] else 1)


if __name__ == "__main__":
    main()
