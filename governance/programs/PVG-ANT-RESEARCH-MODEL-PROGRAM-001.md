# PVG–ANT Research Model Program 001

**Program ID:** `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`
**Status:** active — stage S0 (foundation)
**Authorization:** owner order "AUTHORIZE P8 STRATEGIC HOLD AND START MODEL PROGRAM" (2026-07-12)
**Plan of record:** Roadmap v2.1 (`PVG_ANT_Model_Roadmap/index.html`, sync-governed)
**Classification:** Diagnostic (capability program; creates no theorem)

## Purpose

Build a local specialist component inside the PVG–ANT Central Mind —
measured before trained, compared against the full current mind, and never
confused with the mind itself. The program produces durable assets first
(evaluation suites, benchmark protocol, error maps, sourced corpus) and
trains realistic components second (translator, critic, retriever,
tool-routing) instead of claiming a full researcher.

## System identity (binding)

- The **Central Mind** is the memory, governance, evaluation, and tools:
  the canonical repository (`origin/main`), its registries, guards,
  transition memory, and the frontier engine operating them.
- The **Local Specialist Model** is a replaceable member inside the mind,
  never a substitute for it and never the legal truth of it.
- **Mandatory comparison arms** at every capability/promotion gate:

```text
ARM-BASE     raw base model, untrained
ARM-LOCAL    the trained local specialist component(s)
ARM-CURRENT  the full current mind: engine + repository + tools
ARM-HYBRID   the current mind augmented with the local components
```

No capability or promotion gate is valid without `ARM-CURRENT` present.
`ARM-CURRENT` composition is frozen in
`governance/programs/CURRENT-MIND-FREEZE-MANIFEST-001.md`.

## Corrected cycle (measure before training)

```text
continuity closure
→ P8 decision
→ design and seal Benchmark 002 A/B
→ raw run of Hidden Set A on ARM-CURRENT
→ immutable error map (IMMUTABLE-ERROR-MAP-002-A)
→ model study and architecture decision
→ error-driven targeted corpus
→ training of local specialist components
→ four-arm comparison
→ targeted repair and hybrid integration
→ final hidden test on B and naming decision
```

The reversed order (corpus → training → measurement) is forbidden.

## Stages and gates (dates from Roadmap v2.1)

| Stage | Window | Gate |
|---|---|---|
| S0 foundation: continuity + P8 decision + current-mind freeze | 2026-07-13 → 07-19 | G0: clean synced main, strict ruleset, P8 legally decided |
| S1 design and seal Benchmark 002 (A ≥ 48, B ≥ 48 encrypted) | 2026-07-20 → 08-16 | G1: A/B sealed, roles separated, rubric frozen |
| S2 raw baseline of ARM-CURRENT on A | 2026-08-17 → 08-31 | G2: raw baseline + immutable error map frozen before any training |
| S3 model study and architecture decision | 2026-09-01 → 09-21 | G3: every proposed component answers a named, measured failure |
| S4 durable assets and targeted corpus | 2026-09-22 → 10-31 | G4: K0/K1/R1 and corpus sourced, clean, separated, hash-frozen |
| S5 training of specialist components | 2026-11-01 → 11-21 | G5: ARM-LOCAL beats ARM-BASE on targets without fatal regressions |
| S6 open four-arm comparison | 2026-11-22 → 12-15 | G6: ARM-CURRENT present; ARM-HYBRID adds real value |
| S7 targeted repair and hybrid integration | 2026-12-16 → 2027-01-15 | G7: repair targeted, B still sealed, regression acceptable |
| S8 final hidden test on B and naming decision | 2027-01-16 → 02-14 | G8: generalization and PVG materiality measured against ARM-CURRENT |

Stage closure additionally requires the pre/post sync receipts of
`governance/sync-per-stage-receipts-policy.md`.

## G0 evidence (recorded 2026-07-12)

- P8 decision: `registries/p8-outreach-decision.json` =
  `HOLD_AUTHORIZED`, named blocker
  `STRATEGIC_REPRIORITIZATION_TO_PVG_ANT_MODEL_PROGRAM`, hold recorded
  `2026-07-12T19:47:20Z`, new decision deadline `2026-07-26T19:47:20Z`
  (merged through the gate as PR #31, squash commit `2a6f0ff`).
- Continuity: local `main` = `origin/main` = `2a6f0ff`, ahead 0, behind 0,
  tracked tree clean; workstation task `PVG-ANT-Canonical-Sync` State=Ready,
  LastTaskResult=0; ruleset 18833305 enforces required status
  `governance-gate` with `strict_required_status_checks_policy = true` and
  no bypass actors.
- Current-mind freeze: `CURRENT-MIND-FREEZE-MANIFEST-001` recorded in this
  program package.

## Benchmark unification (binding)

Stage S1 executes the registered protocol
`governance/programs/ADVERSARIAL-PVG-ANT-BENCHMARK-002.md` exactly — one
benchmark, not two. The immutable order stands: raw hidden baseline →
immutable error map → morphism composer → same-set rerun with contamination
accounting → PVG-materiality ablation → targeted learning only from named
failure clusters. `ADVERSARIAL-PVG-ANT-BENCHMARK-002 = NOT_STARTED` until
its own package opens.

## Prohibitions (owner order 2026-07-12)

1. No P8 send during the hold without independent explicit authorization.
2. No P8 cancellation; a new reviewed decision is mandatory before
   `2026-07-26T19:47:20Z`.
3. No training before the raw baseline on A and its immutable error map.
4. No broad book mining; targeted corpus engineering only — every training
   record tied to a named failure cluster from A, sourced, hash-frozen,
   separated from all evaluation sets.
5. No second theorem target.
6. No originality claim.
7. No RH or GRH progress claims; zero RH progress, zero GRH progress.
8. No "Researcher" naming before the local system competes with
   ARM-CURRENT on Hidden Set B with independent review and no loss of
   scientific discipline.

## Key promotion thresholds

- ARM-LOCAL vs ARM-BASE transfer gain ≥ 8 points (capability, not style).
- Retention regression ≤ 3 points after every training step.
- Fatal-overclaim detection = 100%; zero uncertified originality claims.
- ARM-HYBRID must not materially regress against ARM-CURRENT; a component
  that weakens the existing system is not shipped.
- Hidden Set B stays sealed until S8; A becomes a contaminated development
  set after its keys open.

## Ceiling

This program is governance and capability engineering. It creates no
theorem, certifies no originality, and makes zero RH progress and zero GRH
progress. Datasets and evaluation suites outlive any adapter and are the
durable asset.
