# TKG-004-JSONL-STRUCTURAL-REPAIR-001

Status: SOURCE-DATA STRUCTURAL REPAIR — NO SEMANTIC AUTHORSHIP

Date: 2026-07-17

## Scope

This repair concerns exactly two JSONL records in:

`research/translation-knowledge-graph/registry/tkg-004-local-factors-log-derivatives.jsonl`

- line 3: `TKG004-IDENTITY-ZETA-LAMBDA`
- line 4: `TKG004-NODE-GENERALIZED-MANGOLDT`

An independent clean-checkout execution of `extract_tkg_human_authorship_pilot_scaffold_001.py` reported `JSONDecodeError: Extra data`. Structural inspection identified a premature root-object closing brace in each record, leaving later fields outside the root JSON object.

## Authorized change

The file is canonically rewritten as one valid JSON object per line.

The repair is restricted to JSON structure. It does not author, remove, or reinterpret any mathematical field. In particular, both repaired records retain their existing identifiers, types, names, formulas, dependencies/examples, PVG mappings, governance axes, and claim ceilings.

## Consequence

The TKG registry corpus contains 120 physical JSONL records, not 118.

The two repaired records are Family-A records and are complete on the measured type-and-governance axes. They do not enter the 37-row human-authorship queue after repair.

Corrected counts:

```text
TKG total records                         120
Family A records                           66
Family A parseable and axis-complete        66
Family B records                           54
TKG complete on measured axes               83
TKG human-authorship queue                  37
```

## Governance statement

This is not a human classification decision and not a claim-ceiling decision. It is a source-integrity repair. Future extraction must treat any unparseable record as `UNPARSEABLE / NEEDS_REPAIR` before type or ceiling classification.

Scientific state remains `MATH-M0`; no PNT, PNT-AP, Goldbach, RH, or GRH progress.