from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


VERIFIERS = (
    "verify_tkg_002_executable_rule_double_deletion_001.py",
    "verify_tkg_002_mu_two_concept_execution_001.py",
    "verify_tkg_multi_registry_loading_001.py",
    "verify_tkg_001_lambda_structured_execution_001.py",
)


def main() -> None:
    code_dir = Path(__file__).resolve().parent
    results: list[dict[str, object]] = []

    for verifier_name in VERIFIERS:
        completed = subprocess.run(
            [sys.executable, str(code_dir / verifier_name)],
            cwd=code_dir,
            text=True,
            capture_output=True,
            check=False,
        )
        results.append(
            {
                "verifier": verifier_name,
                "exit_code": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
            }
        )

    report = {
        "gate": "TKG-THREE-CONCEPT-NON-REGRESSION-001",
        "policy": "EVERY_CONCEPT_VERIFIER_OWNS_LOCAL_INVARIANTS_ONLY",
        "global_rule_count_assertions": "PROHIBITED",
        "verifiers": results,
        "status": "PASS" if all(item["exit_code"] == 0 for item in results) else "FAIL",
        "classification_on_pass": "THREE_CONCEPT_EXECUTION_FRAMEWORK_CANDIDATE_PENDING_PINNED_CLEAN_CHECKOUT_REPLAY",
        "reasoning_claim": "NOT_AUTHORIZED",
        "math": "MATH-M0",
        "pnt": "NONE",
        "pnt_ap": "NONE",
        "goldbach": "NONE",
        "rh": "NONE",
        "grh": "NONE",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))

    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
