#!/usr/bin/env python3
"""Static verifier for RMG-GOV-005 governance artifacts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV = ROOT / "governance"

REQUIRED = [
    GOV / "RMG-GOV-005-SOURCE-LOCATOR-RESOLUTION.md",
    GOV / "rmg-prior-art-citation-queue.jsonl",
    GOV / "RMG-GOV-005-SOURCE-FILE-MIGRATION-PLAN.md",
    ROOT / "units" / "RMG-GOV-005.md",
]


def main() -> int:
    checks: list[tuple[str, bool]] = []
    checks.append(("required_files", all(path.exists() for path in REQUIRED)))

    queue_path = GOV / "rmg-prior-art-citation-queue.jsonl"
    rows = []
    if queue_path.exists():
        for line in queue_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    ids = [row.get("id") for row in rows]
    checks.append(("queue_nonempty", len(rows) >= 5))
    checks.append(("unique_ids", len(ids) == len(set(ids))))
    checks.append(("unverified_is_explicit", any(row.get("prior_art_status") == "UNVERIFIED" for row in rows)))
    checks.append(("claim_ceilings_present", all(row.get("claim_ceiling") for row in rows)))

    locator_text = REQUIRED[0].read_text(encoding="utf-8") if REQUIRED[0].exists() else ""
    checks.append(("no_locator_novelty_upgrade", "never upgrades" in locator_text))

    plan_text = REQUIRED[2].read_text(encoding="utf-8") if REQUIRED[2].exists() else ""
    checks.append(("bulk_rewrite_prohibited", "BULK_AUTOMATIC_REWRITE = PROHIBITED" in plan_text))
    checks.append(("migration_not_started", "SOURCE_FILE_MIGRATION = NOT_STARTED" in plan_text))

    failed = [name for name, ok in checks if not ok]
    print(json.dumps({"unit": "RMG-GOV-005", "checks": checks, "failed": failed}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
