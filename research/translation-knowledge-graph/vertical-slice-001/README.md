# TKG-DATA-EXECUTION-VERTICAL-SLICE-001

Status: EXPERIMENTAL VERTICAL SLICE — NOT A REASONING ENGINE

Scope: TKG-002 only.

## Classification

- Registry: AUTHORED KNOWLEDGE BASE USED AS AN EXECUTION SOURCE IN THIS SLICE
- Retriever: DATA-DERIVED TERM RETRIEVER
- Operators: GENERIC FINITE ARITHMETIC OPERATORS
- Composer: REGISTRY-RULE EXECUTION COMPOSER
- Benchmark: FALSIFIABLE VERTICAL-SLICE TESTS
- Mathematical contribution: MATH-M0
- PNT / PNT-AP / Goldbach / RH / GRH progress: NONE
- Merge to main: NOT AUTHORIZED

This directory does not rename the earlier R2 fixture benchmark and does not replace it. `BENCHMARK-TKG-001-R2` remains a separate deterministic fixture-conformance regression benchmark.

## Files

- `tkg_data_execution_vertical_slice_001.py`: JSONL loader, normalized `KnowledgeNode`, data-derived retrieval, generic finite operators, and execution composer with mandatory provenance.
- `benchmark_contamination_audit.py`: classifies candidate cases as `CLEAN_RULE_ONLY`, `PARTIALLY_CONTAMINATED`, or `DIRECT_ANSWER_PRESENT`.
- `test_tkg_data_execution_vertical_slice_001.py`: tests new calculations, contamination, provenance, registry mutation, and the double-deletion criterion.

## Falsifiable cases

- `tau(360) = 24`
- `sigma(4620) = 16128`

The expected values occur only in tests. They are not embedded in the execution path.

## Required behavior

1. Rules and claim ceilings are loaded from `registry/tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl`.
2. Target selection uses terms declared by registry names, aliases, and formula left-hand sides; it contains no `if "tau"` or `if "sigma"` route.
3. Every execution step has exactly one provenance field: `source_node_id` or `operator_id`.
4. Removing examples preserves new derivations.
5. Removing formulas and equivalent forms while retaining examples returns `INSUFFICIENT_KNOWLEDGE` for unseen inputs.
6. Changing a registry rule changes execution behavior without changing the engine.

## Local validation performed before push

```text
pytest -q
8 passed
```

The local validation used the same relevant TKG-002 records and was repeated after removing target-specific routing. A clean checkout replay and independent review are still required before this slice can be marked successful.

## Claim ceiling

This slice demonstrates a small data-to-execution connection for finite divisor arithmetic. It does not establish understanding, general reasoning, semantic generalization, mathematical intelligence, or any new theorem.
