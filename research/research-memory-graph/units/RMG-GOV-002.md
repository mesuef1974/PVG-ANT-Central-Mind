# RMG-GOV-002 — Repository-Wide Migration Inventory and Non-Destructive Schema Adapter

Status: COMPLETED_SPECIFICATION / EXECUTION_NOT_YET_CLAIMED

## Objective

Prevent ambiguous maturity labels and incomplete assimilation records from contaminating the Research Memory Graph while preserving all historical evidence.

## Delivered artifacts

- migration inventory contract;
- non-destructive legacy-to-canonical schema adapter;
- migration registry;
- static verifier for the adapter contract.

## Core decisions

1. Historical source records are never overwritten by the adapter.
2. Bare `L0..L7` labels are not accepted as canonical outputs.
3. Legacy computational assimilation labels map only to `ASSIM-*`.
4. Mathematical contribution defaults to `MATH-M0` unless separately justified.
5. PVG necessity fields default to `NOT_AUDITED`, never to an inferred positive contribution.
6. Missing information is represented explicitly rather than silently omitted.
7. Ambiguous legacy values remain `AMBIGUOUS_REQUIRES_REVIEW`.

## Honest state

The adapter and verifier are committed. A repository-wide execution, generated migrated registry, and reviewed retrospective reclassification have not yet been claimed.

## Scientific ceiling

This governance unit makes no new theorem claim, no PVG novelty claim, no RH/GRH progress claim, and no training-corpus authorization.

## Next unit

`RMG-GOV-003` — Executed Inventory Report, Claim Reclassification Queue, and New-Record Enforcement Hook.
