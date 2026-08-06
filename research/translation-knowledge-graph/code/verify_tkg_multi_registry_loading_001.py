from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    TKG002Executor,
    load_registry_jsonl,
)


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    tkg001 = repo_root / "research/translation-knowledge-graph/registry/tkg-001-von-mangoldt-core.jsonl"
    tkg002 = repo_root / "research/translation-knowledge-graph/registry/tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"
    rules = repo_root / "research/translation-knowledge-graph/registry/executable/tkg-002-executable-rules-001.jsonl"

    records = load_registry_jsonl((tkg001, tkg002))
    ids = [record["record_id"] for record in records]
    assert "TKG001-NODE-LAMBDA" in ids
    assert "TKG002-NODE-TAU" in ids
    assert "TKG002-NODE-MU" in ids
    assert len(ids) == len(set(ids))

    executor = TKG002Executor((tkg001, tkg002), rules)
    tau = executor.execute("tau(360)")
    mu = executor.execute("mu(12)")
    assert tau.status == EXECUTED_FROM_REGISTRY_RULE and tau.result == 24
    assert tau.source_node_id == "TKG002-NODE-TAU"
    assert mu.status == EXECUTED_FROM_REGISTRY_RULE and mu.result == 0
    assert mu.source_node_id == "TKG002-NODE-MU"

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        duplicate_a = root / "a.jsonl"
        duplicate_b = root / "b.jsonl"
        write(duplicate_a, '{"record_id":"DUP"}\n')
        write(duplicate_b, '{"record_id":"DUP"}\n')
        try:
            load_registry_jsonl((duplicate_a, duplicate_b))
        except ValueError as exc:
            assert "duplicate record_id" in str(exc)
        else:
            raise AssertionError("cross-registry duplicate was accepted")

        blank = root / "blank.jsonl"
        write(blank, '{"record_id":"A"}\n\n')
        try:
            load_registry_jsonl(blank)
        except ValueError as exc:
            assert "blank JSONL record" in str(exc)
        else:
            raise AssertionError("blank physical JSONL record was accepted")

    print(json.dumps({
        "phase": "PHASE-001-MULTI-REGISTRY-LOADING",
        "parse_gate": "PASS",
        "duplicate_id_audit": "PASS",
        "registries": ["TKG-001", "TKG-002"],
        "non_regression": {"tau(360)": tau.result, "mu(12)": mu.result},
        "classification_change": "NONE",
        "math": "MATH-M0",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
