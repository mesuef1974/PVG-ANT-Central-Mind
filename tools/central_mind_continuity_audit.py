#!/usr/bin/env python3
"""Audit synchronization, maturation receipts, and the PVG–ANT language contract.

This is a governance and capability-continuity check, not a mathematical proof
checker and not a workstation scheduler probe. Standard library only.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = {
    "governance/canonical-repository-sync-policy.md",
    "governance/continuous-mind-maturation-policy.md",
    "governance/task-triggered-knowledge-activation-policy.md",
    "governance/stage-review-and-ceiling-escalation-policy.md",
    "governance/templates/maturation-receipt.md",
    "maps/pvg-ant-common-language-contract-v1.md",
    "registries/maturation-events.jsonl",
    "registries/rules.jsonl",
    "tools/sync_canonical_main.ps1",
    "tools/install_canonical_sync_task.ps1",
}

LIVE_TRUTH_FILES = {
    "README.md",
    "maps/current-capabilities.md",
    "transition-memory/latest-state.md",
    "transition-memory/next-action.md",
}

REQUIRED_RULE_IDS = {
    "RULE-CANONICAL-SYNC-001",
    "RULE-STAGE-MATURATION-RECEIPT-001",
    "RULE-KNOWLEDGE-TO-TRANSLATION-001",
}

REQUIRED_STAGE_IDS = {
    "TRANSLATION-KERNEL-V2-PASS-001",
    "PVG-ANT-BENCHMARK-001",
    "TRANSLATION-KERNEL-V2-PASS-002",
    "PVG-UNDERSTANDING-DEEPENING-001",
    "GOVERNANCE-ENFORCEMENT-CLOSURE-001",
    "CENTRAL-MIND-CONTINUITY-001",
}

REQUIRED_EVENT_FIELDS = {
    "id",
    "stage_id",
    "status",
    "capability_before",
    "capability_after",
    "knowledge_delta",
    "language_delta",
    "reasoning_delta",
    "certificate_delta",
    "failure_memory_delta",
    "verification",
    "sync_evidence",
    "claim_ceiling",
    "classification",
    "source",
}

ALLOWED_EVENT_STATUSES = {
    "checkpoint_pass",
    "closed",
    "installed_repository_side",
}

CURRENT_RECEIPT = "MATURATION-RECEIPT-006"
CURRENT_STAGE = "CENTRAL-MIND-CONTINUITY-001"

STAGE_DECLARATION_RE = re.compile(
    r"\b([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+-\d{3})\s*=\s*"
    r"(checkpoint_pass|executed|CLOSED|closed|installed|installed_repository_side)\b"
)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def load_jsonl(relative_path: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line_number, raw in enumerate(read(relative_path).splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"{relative_path}:{line_number}: invalid JSON: {exc}"
            ) from exc
        if not isinstance(value, dict):
            raise RuntimeError(
                f"{relative_path}:{line_number}: row is not a JSON object"
            )
        rows.append(value)
    return rows


def require(condition: bool, message: str, issues: list[str]) -> None:
    if not condition:
        issues.append(message)


def main() -> None:
    issues: list[str] = []

    for relative_path in sorted(REQUIRED_FILES | LIVE_TRUTH_FILES):
        require(
            (ROOT / relative_path).is_file(),
            f"missing continuity file: {relative_path}",
            issues,
        )

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    rules = load_jsonl("registries/rules.jsonl")
    rule_ids = {str(row.get("id", "")) for row in rules}
    require(
        REQUIRED_RULE_IDS <= rule_ids,
        f"missing continuity rules: {sorted(REQUIRED_RULE_IDS - rule_ids)}",
        issues,
    )

    events = load_jsonl("registries/maturation-events.jsonl")
    require(bool(events), "maturation event registry is empty", issues)

    event_ids: list[str] = []
    stage_ids: list[str] = []
    for row in events:
        event_id = str(row.get("id", ""))
        stage_id = str(row.get("stage_id", ""))
        event_ids.append(event_id)
        stage_ids.append(stage_id)

        missing = REQUIRED_EVENT_FIELDS - set(row)
        require(
            not missing,
            f"maturation event {event_id or '<missing-id>'} missing fields: {sorted(missing)}",
            issues,
        )

        for field in REQUIRED_EVENT_FIELDS:
            value = row.get(field)
            require(
                isinstance(value, str) and bool(value.strip()),
                f"maturation event {event_id or '<missing-id>'} has empty/non-string field {field}",
                issues,
            )

        require(
            str(row.get("status", "")) in ALLOWED_EVENT_STATUSES,
            f"maturation event {event_id} has unsupported status {row.get('status')!r}",
            issues,
        )

    require(len(event_ids) == len(set(event_ids)), "duplicate maturation receipt IDs", issues)
    require(len(stage_ids) == len(set(stage_ids)), "duplicate maturation stage IDs", issues)
    require(
        REQUIRED_STAGE_IDS <= set(stage_ids),
        f"missing required maturation stages: {sorted(REQUIRED_STAGE_IDS - set(stage_ids))}",
        issues,
    )

    receipt_numbers: list[int] = []
    for event_id in event_ids:
        match = re.fullmatch(r"MATURATION-RECEIPT-(\d{3})", event_id)
        require(match is not None, f"invalid maturation receipt ID: {event_id}", issues)
        if match is not None:
            receipt_numbers.append(int(match.group(1)))
    if receipt_numbers:
        expected = list(range(1, len(receipt_numbers) + 1))
        require(
            sorted(receipt_numbers) == expected,
            f"maturation receipt sequence must be contiguous: expected {expected}, got {sorted(receipt_numbers)}",
            issues,
        )

    live_documents: dict[str, str] = {
        relative_path: read(relative_path) for relative_path in LIVE_TRUTH_FILES
    }
    registered_stage_ids = set(stage_ids)
    for relative_path, document in live_documents.items():
        require(
            CURRENT_RECEIPT in document,
            f"{relative_path} omits current maturation receipt {CURRENT_RECEIPT}",
            issues,
        )
        require(
            CURRENT_STAGE in document,
            f"{relative_path} omits current continuity stage {CURRENT_STAGE}",
            issues,
        )
        for stage_id, status in STAGE_DECLARATION_RE.findall(document):
            require(
                stage_id in registered_stage_ids,
                f"{relative_path} declares {stage_id}={status} without a maturation event",
                issues,
            )

    latest_state = live_documents["transition-memory/latest-state.md"]
    next_action = live_documents["transition-memory/next-action.md"]
    require(
        "ADVERSARIAL-PVG-ANT-BENCHMARK-002 = NOT_STARTED" in latest_state,
        "latest-state does not preserve Benchmark 002 as NOT_STARTED",
        issues,
    )
    require(
        "ADVERSARIAL-PVG-ANT-BENCHMARK-002 = NOT_STARTED" in next_action,
        "next-action does not preserve Benchmark 002 as NOT_STARTED",
        issues,
    )
    require(
        "ADVERSARIAL-PVG-ANT-BENCHMARK-002" not in registered_stage_ids,
        "Benchmark 002 has a maturation receipt before its raw baseline",
        issues,
    )

    sync_policy = read("governance/canonical-repository-sync-policy.md")
    maturation_policy = read("governance/continuous-mind-maturation-policy.md")
    common_language = read("maps/pvg-ant-common-language-contract-v1.md")
    sync_script = read("tools/sync_canonical_main.ps1")
    task_installer = read("tools/install_canonical_sync_task.ps1")

    for required_text in (
        "origin/main is the canonical repository truth",
        "fast-forward",
        "strict_required_status_checks_policy = true",
        "workstation",
    ):
        require(
            required_text in sync_policy,
            f"sync policy omits required concept: {required_text}",
            issues,
        )

    for required_text in (
        "K — operational knowledge",
        "L — shared PVG–ANT language",
        "R — reasoning/composition capability",
        "F — reusable failure/negative memory",
        "maturation-events.jsonl",
    ):
        require(
            required_text in maturation_policy,
            f"maturation policy omits required concept: {required_text}",
            issues,
        )

    for required_text in (
        "Source-grounded ANT statement or object",
        "Native PVG object",
        "Forward morphism or projection",
        "Information preserved",
        "Information lost and LOSS level",
        "Reverse translation and exact recovery conditions",
        "Counterexample to an invalid reverse inference",
        "PVG materiality result",
    ):
        require(
            required_text in common_language,
            f"common-language contract omits field: {required_text}",
            issues,
        )

    for required_text in (
        '@("fetch", "--prune", "origin", "main")',
        '@("merge", "--ff-only", "origin/main")',
        '@("status", "--porcelain=v1")',
        "Repository identity mismatch",
        "PrepareBranch refused",
    ):
        require(
            required_text in sync_script,
            f"sync script omits safe operation: {required_text}",
            issues,
        )

    lower_sync_script = sync_script.lower()
    for forbidden_text in (
        "reset --hard",
        "push --force",
        "push -f",
        "git stash",
        "clean -fd",
    ):
        require(
            forbidden_text not in lower_sync_script,
            f"sync script contains forbidden destructive operation: {forbidden_text}",
            issues,
        )

    for required_text in (
        "Register-ScheduledTask",
        "sync_canonical_main.ps1",
        "-Mode SafeSync",
        "-RunLevel Limited",
    ):
        require(
            required_text in task_installer,
            f"scheduled-task installer omits required safety element: {required_text}",
            issues,
        )

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    print("Central Mind Continuity Audit: PASS")
    print(f"Maturation receipts: {len(events)}")
    print(f"Registered stages: {len(stage_ids)}")
    print(f"Current receipt: {CURRENT_RECEIPT}")
    print("Benchmark 002: NOT_STARTED")
    print("Workstation scheduled-task activation: external fact, not inferred")


if __name__ == "__main__":
    main()
