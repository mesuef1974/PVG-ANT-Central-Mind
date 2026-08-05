#!/usr/bin/env python3
"""Validate the legacy research asset support layer.

This audit checks structure and governance only. It does not certify the
mathematical truth of external research claims.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "registries" / "external-research-assets.jsonl"
NEGATIVE = ROOT / "registries" / "negative-results.jsonl"
GOALS = ROOT / "registries" / "program-goals.jsonl"
KERNEL = ROOT / "maps" / "pvg-ant-language-kernel-v1.md"
ROUTING = ROOT / "maps" / "legacy-assets-routing.md"
RECONCILIATION = ROOT / "integration" / "legacy-research-assets-reconciliation-001.md"
NEXT_ACTION = ROOT / "transition-memory" / "next-action.md"

REQUIRED_ASSET_FIELDS = {
    "kind",
    "id",
    "title",
    "status",
    "role",
    "source_archive",
    "canonical_use",
    "activation_condition",
    "keep_external",
    "research_front_active",
    "scientific_ceiling",
}
ALLOWED_STATUSES = {
    "integrated_reference",
    "external_lab",
    "design_pattern",
    "archived_negative",
}
REQUIRED_BRIDGES = {
    "BRIDGE-SIEVE-TRUNCATED-VALUATION-001",
    "BRIDGE-SIEVE-AGGREGATION-LOSS-001",
    "BRIDGE-RESIDUE-PRINCIPAL-REMOVAL-001",
    "BRIDGE-RESIDUE-VARIANCE-PARSEVAL-001",
    "BRIDGE-PVG-LAYER-SEPARATION-001",
    "BRIDGE-EDGE-ERROR-SEPARATION-001",
}


def load_jsonl(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        raise RuntimeError(f"Missing registry: {path.relative_to(ROOT)}")
    rows: list[dict[str, object]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid JSON at {path.name}:{line_number}: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError(f"Non-object JSON at {path.name}:{line_number}")
        rows.append(value)
    return rows


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    assets = load_jsonl(ASSETS)
    negatives = load_jsonl(NEGATIVE)
    goals = load_jsonl(GOALS)
    require(len(assets) >= 10, "Expected at least ten reconciled external assets")
    require(len(negatives) >= 5, "Expected at least five negative/closure records")

    ids: set[str] = set()
    for row in assets:
        missing = REQUIRED_ASSET_FIELDS - row.keys()
        require(not missing, f"Asset {row.get('id')} missing fields: {sorted(missing)}")
        asset_id = str(row["id"])
        require(asset_id.startswith("EXT-ASSET-"), f"Unexpected asset ID: {asset_id}")
        require(asset_id not in ids, f"Duplicate asset ID: {asset_id}")
        ids.add(asset_id)
        require(row["status"] in ALLOWED_STATUSES, f"Invalid status for {asset_id}")
        require(row["research_front_active"] is False, f"Legacy asset became active front: {asset_id}")
        require(bool(str(row["activation_condition"]).strip()), f"Missing activation condition: {asset_id}")
        require(bool(str(row["scientific_ceiling"]).strip()), f"Missing ceiling: {asset_id}")

    negative_ids: set[str] = set()
    for row in negatives:
        negative_id = str(row.get("id", ""))
        require(negative_id.startswith("NEG-"), f"Unexpected negative-result ID: {negative_id}")
        require(negative_id not in negative_ids, f"Duplicate negative-result ID: {negative_id}")
        negative_ids.add(negative_id)
        for field in ["status", "finding", "reopen_condition", "classification", "source"]:
            require(bool(str(row.get(field, "")).strip()), f"{negative_id} missing {field}")

    active_goals = [
        row
        for row in goals
        # Stage Review 001 PR-A: operational goals carry qualified active states
        # (e.g. active_external_validation_hold); the registry is the truth.
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]
    require(len(active_goals) == 1, f"Expected one active operational goal, found {len(active_goals)}")
    active_goal_id = str(active_goals[0].get("id", ""))
    require(active_goal_id.startswith("GOAL-OP-"), "Invalid active operational goal ID")

    for path in [KERNEL, ROUTING, RECONCILIATION, NEXT_ACTION]:
        require(path.exists(), f"Missing required file: {path.relative_to(ROOT)}")

    kernel_text = KERNEL.read_text(encoding="utf-8")
    missing_bridges = sorted(bridge for bridge in REQUIRED_BRIDGES if bridge not in kernel_text)
    require(not missing_bridges, f"Language kernel missing bridges: {missing_bridges}")

    reconciliation_text = RECONCILIATION.read_text(encoding="utf-8")
    require(
        "not a new research front" in reconciliation_text.lower(),
        "Reconciliation does not preserve the one-active-front rule",
    )

    next_action_text = NEXT_ACTION.read_text(encoding="utf-8")
    require(
        active_goal_id in next_action_text,
        f"Next action does not identify active goal {active_goal_id}",
    )
    # The prohibition, not the string. `"Dataset 004" in text` was satisfied by
    # "Dataset 004 is hereby AUTHORIZED" -- the guard confirmed the topic was mentioned,
    # never that it was still forbidden.
    require(
        bool(re.search(r"Dataset 004\s+(?:remains|is|stays)\s+(?:un|not\s+)authoriz",
                       next_action_text, re.I)),
        "Dataset 004 prohibition disappeared or was weakened",
    )
    require(
        not re.search(r"Dataset 004[^.\n]{0,40}\bauthorized\b", next_action_text, re.I),
        "Dataset 004 is stated as authorized",
    )

    print(
        "legacy_assets_audit: PASS — "
        f"{len(assets)} assets, {len(negatives)} negative records, "
        f"{len(REQUIRED_BRIDGES)} kernel bridges; active goal={active_goal_id}; "
        "no legacy front activated."
    )


if __name__ == "__main__":
    main()
