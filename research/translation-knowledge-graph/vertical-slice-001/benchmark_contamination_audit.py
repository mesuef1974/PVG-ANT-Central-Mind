from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from tkg_data_execution_vertical_slice_001 import KnowledgeNode, RegistryLoader

CLEAN_RULE_ONLY = "CLEAN_RULE_ONLY"
PARTIALLY_CONTAMINATED = "PARTIALLY_CONTAMINATED"
DIRECT_ANSWER_PRESENT = "DIRECT_ANSWER_PRESENT"


@dataclass(frozen=True)
class ContaminationFinding:
    classification: str
    case_n: int
    expected_result: int | float | None
    evidence: tuple[str, ...]


def _walk(value: Any, path: str = "") -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield from _walk(item, f"{path}.{key}" if path else str(key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk(item, f"{path}[{index}]")
    else:
        yield path, value


def audit_case(
    nodes: Iterable[KnowledgeNode],
    *,
    n: int,
    expected_result: int | float | None = None,
    factorization: dict[int, int] | None = None,
    divisors: list[int] | None = None,
) -> ContaminationFinding:
    direct: list[str] = []
    partial: list[str] = []
    divisor_set = set(divisors or ())
    factor_tokens = {str(p): e for p, e in (factorization or {}).items()}

    for node in nodes:
        for index, example in enumerate(node.examples):
            prefix = f"{node.node_id}.examples[{index}]"
            flat = list(_walk(example, prefix))
            values = [value for _, value in flat]
            has_n = any(value == n for value in values)
            has_result = expected_result is not None and any(value == expected_result for value in values)
            if has_n and has_result:
                direct.append(f"{prefix}: input and expected result present")
                continue
            if has_n:
                partial.append(f"{prefix}: input present")
            for path, value in flat:
                if path.endswith("factorization") and isinstance(value, str):
                    if all(str(p) in value and (e == 1 or str(e) in value) for p, e in factor_tokens.items()):
                        partial.append(f"{path}: factorization components present")
                if path.endswith("divisors") and isinstance(value, list) and divisor_set:
                    overlap = divisor_set.intersection(value)
                    if overlap:
                        partial.append(f"{path}: divisor overlap {sorted(overlap)}")

    if direct:
        return ContaminationFinding(DIRECT_ANSWER_PRESENT, n, expected_result, tuple(direct + partial))
    if partial:
        return ContaminationFinding(PARTIALLY_CONTAMINATED, n, expected_result, tuple(partial))
    return ContaminationFinding(CLEAN_RULE_ONLY, n, expected_result, ())


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit TKG examples for benchmark contamination")
    parser.add_argument("registry", type=Path)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--expected", type=float)
    args = parser.parse_args()

    nodes = RegistryLoader().load(args.registry)
    finding = audit_case(nodes, n=args.n, expected_result=args.expected)
    print(json.dumps(finding.__dict__, ensure_ascii=False, indent=2))
    return 0 if finding.classification == CLEAN_RULE_ONLY else 2


if __name__ == "__main__":
    raise SystemExit(main())
