# TKG-DATA-EXECUTION-VERTICAL-SLICE-001

Status: FAMILY-A-ONLY PROTOTYPE — GLOBAL VALIDATION WITHDRAWN

Scope: TKG-002 only.

## Corrected classification

- Registry sample: one Family-A authored file only
- Retriever: experimental data-derived term retriever
- Operators: project-authored finite arithmetic operators
- Composer: prototype formula-pattern execution composer
- Benchmark: local prototype tests, not a sealed benchmark
- Mathematical contribution: MATH-M0
- PNT / PNT-AP / Goldbach / RH / GRH progress: NONE
- Merge to main: NOT AUTHORIZED
- Reasoning-engine claim: PROHIBITED
- Global executable-knowledge-base claim: PROHIBITED

The earlier implementation and its tests remain preserved as falsifiable prototype evidence. Their interpretation is narrowed.

They show that one selected Family-A file can be connected to finite arithmetic code. They do not show that TKG-001 through TKG-015 share a schema or that unrestricted mathematical formula strings form an execution language.

## Blocking findings

1. TKG-001 through TKG-008 and TKG-009 through TKG-015 use different identity conventions.
2. TKG-002 belongs to the first family, so success on it is sample-dependent.
3. Human-readable `formula` and `equivalent_forms` strings are not a machine-execution contract.
4. Parsing selected formula shapes in Python is a prototype convenience, not proof of data-driven mathematical execution.
5. The current composer must not be extended to more registries by adding further formula regex cases.

See:

- `../governance/TKG-SCHEMA-FAMILY-SPLIT-AUDIT-001.md`
- `../schema/tkg-canonical-executable-schema-001.json`

## Preserved prototype files

- `tkg_data_execution_vertical_slice_001.py`
- `benchmark_contamination_audit.py`
- `test_tkg_data_execution_vertical_slice_001.py`

The previous local result remains historical evidence:

```text
pytest -q
8 passed
```

It is not a certificate of global schema adequacy.

## Candidate cases

The following remain valid clean candidate inputs for a later migrated slice:

- `tau(360) = 24`
- `sigma(4620) = 16128`
- additional clean inputs may include `2310` and `59049`

Their expected values must remain outside the execution path.

## Contamination correction

Contamination decisions must inspect structured examples and match contextual case tuples. Raw grep over numbers is forbidden. A value such as `24` appearing in benchmark metadata does not by itself contaminate `tau(360)=24`.

## Required replacement path

Before resuming execution work:

1. adopt the canonical node schema;
2. normalize both source families;
3. add explicit `executable_rule` fields to selected executable nodes;
4. load at least one record from each family through the same canonical model;
5. reject execution when `executable_rule` is absent;
6. keep operator implementations explicit and project-authored;
7. rerun deletion, mutation, provenance, and structured-contamination tests.

## Current verdict

```text
IMPLEMENTATION = PRESERVED PROTOTYPE
FAMILY-A LOAD = DEMONSTRATED LOCALLY
FAMILY-B LOAD = NOT DEMONSTRATED
EXECUTABLE SCHEMA = NOT YET MIGRATED
GLOBAL SLICE SUCCESS = NO
INDEPENDENT REVIEW = PENDING
BENCHMARK SEALED = NO
```
