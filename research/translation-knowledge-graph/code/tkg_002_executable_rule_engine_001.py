from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

INSUFFICIENT_KNOWLEDGE = "INSUFFICIENT_KNOWLEDGE"
EXECUTED_FROM_REGISTRY_RULE = "EXECUTED_FROM_REGISTRY_RULE"


@dataclass(frozen=True)
class ExecutionStep:
    description: str
    value: Any
    source_node_id: str | None = None
    operator_id: str | None = None

    def __post_init__(self) -> None:
        if (self.source_node_id is None) == (self.operator_id is None):
            raise ValueError("each step must carry exactly one provenance source")


@dataclass(frozen=True)
class ExecutionResult:
    status: str
    query: str
    source_node_id: str | None
    rule_id: str | None
    result: int | None
    steps: tuple[ExecutionStep, ...]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: record must be an object")
        records.append(value)
    return records


def factor_integer(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    factors: dict[int, int] = {}
    remaining = n
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def enumerate_divisors(n: int) -> list[int]:
    divisors = [1]
    for prime, exponent in factor_integer(n).items():
        divisors = [
            existing * prime**power
            for existing in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def evaluate_divisor_sum(args: dict[str, Any], n: int) -> int:
    if args.get("summand") != "one":
        raise ValueError(f"unsupported summand: {args.get('summand')!r}")
    return sum(1 for _ in enumerate_divisors(n))


OPERATORS = {
    "OP-EVALUATE-DIVISOR-SUM-001": evaluate_divisor_sum,
}


class TKG002Executor:
    def __init__(self, registry_path: Path, rules_path: Path):
        self.registry = load_jsonl(registry_path)
        self.rules = load_jsonl(rules_path)
        self.nodes = {
            str(record["record_id"]): record
            for record in self.registry
            if isinstance(record.get("record_id"), str)
        }

    def execute(self, query: str) -> ExecutionResult:
        match = re.search(r"([A-Za-z_]+)\s*\(\s*(\d+)\s*\)", query)
        if not match:
            return ExecutionResult(INSUFFICIENT_KNOWLEDGE, query, None, None, None, ())

        symbol = match.group(1).lower()
        n = int(match.group(2))
        candidates = []
        for rule in self.rules:
            contract = rule.get("executable_rule")
            source_node_id = rule.get("source_node_id")
            if (
                isinstance(contract, dict)
                and source_node_id in self.nodes
                and str(contract.get("result_symbol", "")).lower() == symbol
            ):
                candidates.append(rule)

        if len(candidates) != 1:
            return ExecutionResult(INSUFFICIENT_KNOWLEDGE, query, None, None, None, ())

        rule = candidates[0]
        source_node_id = str(rule["source_node_id"])
        contract = rule["executable_rule"]
        operator_id = str(contract.get("operator_id", ""))
        operator = OPERATORS.get(operator_id)
        if operator is None:
            return ExecutionResult(
                INSUFFICIENT_KNOWLEDGE,
                query,
                source_node_id,
                str(rule.get("rule_id")),
                None,
                (),
            )

        steps = [
            ExecutionStep(
                "Load reviewed executable contract",
                contract,
                source_node_id=source_node_id,
            )
        ]
        steps.append(
            ExecutionStep(
                "Factor input integer",
                factor_integer(n),
                operator_id="OP-FACTOR-INTEGER-001",
            )
        )
        steps.append(
            ExecutionStep(
                "Enumerate divisors",
                enumerate_divisors(n),
                operator_id="OP-ENUMERATE-DIVISORS-001",
            )
        )
        result = operator(dict(contract.get("args") or {}), n)
        steps.append(
            ExecutionStep(
                "Execute reviewed operator contract",
                result,
                operator_id=operator_id,
            )
        )
        return ExecutionResult(
            EXECUTED_FROM_REGISTRY_RULE,
            query,
            source_node_id,
            str(rule.get("rule_id")),
            result,
            tuple(steps),
        )
