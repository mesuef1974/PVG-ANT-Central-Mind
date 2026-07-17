from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable

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
class OperatorExecution:
    result: Any
    steps: tuple[ExecutionStep, ...]


@dataclass(frozen=True)
class ExecutionResult:
    status: str
    query: str
    source_node_id: str | None
    rule_id: str | None
    result: Any | None
    steps: tuple[ExecutionStep, ...]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"{path}: empty JSONL file")
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError(f"{path}:{line_number}: blank JSONL record")
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: record must be an object")
        records.append(value)
    return records


def _normalize_paths(paths: Path | Iterable[Path]) -> tuple[Path, ...]:
    if isinstance(paths, Path):
        normalized = (paths,)
    else:
        normalized = tuple(Path(path) for path in paths)
    if not normalized:
        raise ValueError("at least one registry path is required")
    return normalized


def load_registry_jsonl(paths: Path | Iterable[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen: dict[str, Path] = {}
    for path in _normalize_paths(paths):
        for record in load_jsonl(path):
            record_id = record.get("record_id")
            if not isinstance(record_id, str) or not record_id:
                raise ValueError(f"{path}: every registry record requires a non-empty string record_id")
            previous = seen.get(record_id)
            if previous is not None:
                raise ValueError(f"duplicate record_id {record_id!r} across {previous} and {path}")
            seen[record_id] = path
            records.append(record)
    return records


def load_rule_jsonl(path: Path) -> list[dict[str, Any]]:
    records = load_jsonl(path)
    seen: set[str] = set()
    for record in records:
        rule_id = record.get("rule_id")
        if not isinstance(rule_id, str) or not rule_id:
            raise ValueError(f"{path}: every executable rule requires a non-empty string rule_id")
        if rule_id in seen:
            raise ValueError(f"{path}: duplicate rule_id {rule_id!r}")
        seen.add(rule_id)
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
        divisors = [existing * prime**power for existing in divisors for power in range(exponent + 1)]
    return sorted(divisors)


def evaluate_divisor_sum(args: dict[str, Any], n: int) -> OperatorExecution:
    if args.get("summand") != "one":
        raise ValueError(f"unsupported summand: {args.get('summand')!r}")
    factors = factor_integer(n)
    divisors = enumerate_divisors(n)
    result = len(divisors)
    return OperatorExecution(result, (
        ExecutionStep("Factor input integer", factors, operator_id="OP-FACTOR-INTEGER-001"),
        ExecutionStep("Enumerate divisors", divisors, operator_id="OP-ENUMERATE-DIVISORS-001"),
        ExecutionStep("Count divisors", result, operator_id="OP-EVALUATE-DIVISOR-SUM-001"),
    ))


def evaluate_mobius(args: dict[str, Any], n: int) -> OperatorExecution:
    if args:
        raise ValueError(f"unsupported Mobius arguments: {args!r}")
    factors = factor_integer(n)
    has_square_factor = any(exponent > 1 for exponent in factors.values())
    support_cardinality = len(factors)
    result = 0 if has_square_factor else (-1 if support_cardinality % 2 else 1)
    return OperatorExecution(result, (
        ExecutionStep("Factor input integer", factors, operator_id="OP-FACTOR-INTEGER-001"),
        ExecutionStep("Detect exponent greater than one", has_square_factor, operator_id="OP-DETECT-SQUARE-FACTOR-001"),
        ExecutionStep("Count distinct prime support", support_cardinality, operator_id="OP-COUNT-PRIME-SUPPORT-001"),
        ExecutionStep("Evaluate Mobius from squarefreeness and support parity", result, operator_id="OP-EVALUATE-MOBIUS-001"),
    ))


Operator = Callable[[dict[str, Any], int], OperatorExecution]
OPERATORS: dict[str, Operator] = {
    "OP-EVALUATE-DIVISOR-SUM-001": evaluate_divisor_sum,
    "OP-EVALUATE-MOBIUS-001": evaluate_mobius,
}


class TKG002Executor:
    def __init__(self, registry_path: Path | Iterable[Path], rules_path: Path):
        self.registry_paths = _normalize_paths(registry_path)
        self.registry = load_registry_jsonl(self.registry_paths)
        self.rules = load_rule_jsonl(rules_path)
        self.nodes = {str(record["record_id"]): record for record in self.registry}

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
            if isinstance(contract, dict) and source_node_id in self.nodes and str(contract.get("result_symbol", "")).lower() == symbol:
                candidates.append(rule)
        if len(candidates) != 1:
            return ExecutionResult(INSUFFICIENT_KNOWLEDGE, query, None, None, None, ())
        rule = candidates[0]
        source_node_id = str(rule["source_node_id"])
        contract = rule["executable_rule"]
        operator_id = str(contract.get("operator_id", ""))
        operator = OPERATORS.get(operator_id)
        if operator is None:
            return ExecutionResult(INSUFFICIENT_KNOWLEDGE, query, source_node_id, str(rule.get("rule_id")), None, ())
        operator_execution = operator(dict(contract.get("args") or {}), n)
        steps = (ExecutionStep("Load reviewed executable contract", contract, source_node_id=source_node_id), *operator_execution.steps)
        return ExecutionResult(EXECUTED_FROM_REGISTRY_RULE, query, source_node_id, str(rule.get("rule_id")), operator_execution.result, steps)
