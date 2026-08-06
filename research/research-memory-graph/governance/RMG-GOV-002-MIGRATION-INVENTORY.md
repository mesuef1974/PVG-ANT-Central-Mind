# RMG-GOV-002 — Repository-Wide Migration Inventory

Status: IMPLEMENTED_SPECIFICATION / EXECUTION_NOT_YET_CLAIMED

## Purpose

Inventory legacy maturity labels, assimilation schemas, and PVG-contribution claims without deleting or rewriting historical records.

## Legacy classes to inventory

1. Bare `L0` through `L7` labels.
2. `assimilation_level` values using the bare ladder.
3. Operational states such as `validated_intake`, `closed`, `architecture_only_unbenchmarked`, and `production_ready`.
4. Certificate labels mixed with mathematical contribution labels.
5. RMG records using compact fields such as `ant_view`, `pvg_view`, and `inverse_status`.
6. Files claiming a PVG contribution without a documented removal test.

## Canonical target namespaces

- `ASSIM-L0` through `ASSIM-L7`: assimilation depth only.
- `MATH-M0` through `MATH-M5`: mathematical contribution depth only.
- `OPS-*`: operational maturity only.
- `CERT-*`: evidence or certificate strength only.
- `PVG-N0` through `PVG-N5`: PVG necessity only.

## Non-destructive migration policy

Historical files remain unchanged unless a later reviewed migration explicitly updates them. The adapter must expose a canonical view while preserving:

- original path;
- original record;
- original label;
- inferred mapping;
- confidence of inference;
- unresolved ambiguity;
- migration status.

## Migration statuses

- `EXACTLY_MAPPED`
- `MAPPED_WITH_EXPLICIT_ASSUMPTION`
- `AMBIGUOUS_REQUIRES_REVIEW`
- `NOT_APPLICABLE`
- `UNMAPPED_LEGACY_VALUE`
- `HISTORICAL_RECORD_PRESERVED`

## Hard rule

A regression test, finite computation, or executable harness may increase `ASSIM-*`, `OPS-*`, or `CERT-*`. It must never automatically increase `MATH-*`.

## Current ceiling

This file defines the inventory contract. It does not claim that a repository-wide scan has been executed or that all historical records comply.