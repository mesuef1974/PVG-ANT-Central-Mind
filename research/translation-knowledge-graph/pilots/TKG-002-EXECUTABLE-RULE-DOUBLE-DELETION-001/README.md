# TKG-002-EXECUTABLE-RULE-DOUBLE-DELETION-001

Status: `IMPLEMENTED / LOCAL COMPONENT TEST PASS / CLEAN-CHECKOUT REAL-REGISTRY REPLAY PENDING`

Date: 2026-07-17

## Scope

This gate tests whether `tau(360)` can be computed from a reviewed executable contract attached to the authored TKG-002 node, rather than from examples, textual-formula parsing, target-specific branches, or a stored answer.

## Implemented artifacts

- `registry/executable/tkg-002-executable-rules-001.jsonl`
- `code/tkg_002_executable_rule_engine_001.py`
- `code/verify_tkg_002_executable_rule_double_deletion_001.py`

The descriptive TKG-002 registry remains unchanged. Execution is authorized through a separate reviewed overlay:

```json
{
  "source_node_id": "TKG002-NODE-TAU",
  "executable_rule": {
    "operator_id": "OP-EVALUATE-DIVISOR-SUM-001",
    "args": {"summand": "one"},
    "result_symbol": "tau"
  }
}
```

## Local component validation

A local component-level validation reported:

```text
baseline tau(360)                         24
examples deleted, executable rule kept   24
executable rule deleted, examples kept   INSUFFICIENT_KNOWLEDGE
provenance                                PASS
```

This local validation used the committed engine and rule-contract shape but a minimal registry fixture. It is not a clean-checkout replay against the full committed TKG-002 registry.

## Required clean-checkout command

From a clean checkout of the experimental branch, run:

```text
python research/translation-knowledge-graph/code/verify_tkg_002_executable_rule_double_deletion_001.py
```

The gate is not closed until that command exits zero against the real registry and its output is reviewed independently.

## Success requirements

1. Baseline `tau(360)` returns `24`.
2. Deleting every `examples` field does not change the result.
3. Deleting `executable_rule` while retaining examples returns `INSUFFICIENT_KNOWLEDGE`.
4. Every successful execution step has exactly one provenance source.
5. The engine contains no `360`, no stored result `24`, and no `if "tau" in question` branch.
6. The test case is structurally `CLEAN_RULE_ONLY`; raw numeric grep is not used.

## Claim boundary

```text
REASONING ENGINE = NOT CLAIMED
GENERALIZATION = NOT ESTABLISHED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
BENCHMARK SEALED = NO
MERGE TO MAIN = NOT AUTHORIZED
```
