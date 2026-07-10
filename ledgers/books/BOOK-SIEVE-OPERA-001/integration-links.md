# Opera de Cribro — Integration Links

Book ID: `BOOK-SIEVE-OPERA-001` · Version: v0.7 · **partial_overlay — `OPERA-004-A` CLOSED (v0.7-A PASS) + `OPERA-004-B` validated_intake (v0.7-B pending).** Routing (both units): `packet_mismatch = true`, `routing_split`.

Links added AFTER normalization (promotion rule: project-governed, post-mining), never as a pre-mining selection criterion. `MC-001` appears here as standing context only — it did not drive what was mined.

## Links to installed tools (reference integration)

```text
TOOL-MOBIUS-001 (Overholt)                       ← OPERA-004-A §2 Möbius coprimality detector.
TOOL-SIEVE-INFO-CONSUMPTION-001 (Harman)         ← OPERA-004-A §1 sifting as information consumption.
TOOL-TYPE-I-II-DIAGNOSTIC-001 (Harman)           ← forward: the remainder layer becomes Type-I/II later.
TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001       ← OPERA-004-A §1 A_d = g(d)X + r_d level-of-distribution grammar.
TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001             ← OPERA-004-A §1 combinatorial-sieve remainder handling.
```

These are terminology-reconciliation links, not new tools: the exact-decomposition and level-of-distribution machinery is already installed; Opera's contribution here is the certificate-input framing.

## Frontier and walls (v0.7-A adjudicated: zero new WALL-ID, zero silent widening)

```text
FRONTIER-ANT-PVG-004 (sieve information / support geometry) — the pillar this unit deepens.
WALL-PARITY        — registered, uncrossed. This unit maps NO boundary onto it; the parity mechanism
                     is not reached by this packet.
WALL-SIEVE-CEILING — registered, uncrossed. Its text ("no unconditional sieve reaches RH; only EH
                     crosses") concerns the RH ceiling, NOT aggregate remainder failure — so the
                     aggregate-remainder boundary is NOT mapped onto it (no silent widening).
Boundaries (this intake; all Boundaries, zero new WALL-ID):
  aggregate-remainder        — Boundary (no wall mapping).
  local-model                — Boundary + governance caution (repairable via LB-05).
  formulation-vs-certificate — Boundary + governance caution; re-examination of its relation to
                               WALL-PARITY DEFERRED to the parity-grounding packet (not mapped now).
```

## Load-bearing linkage

```text
LB-04 (level of distribution) = primary anchor of this intake (validity range of A_d = g(d)X + r_d).
LB-02 (bilinear remainders)   = precursor (remainder layer named; bilinear structure not yet reached).
LB-01 / LB-03 / LB-05         = not yet reached by A.
LB-06 (application transfer)  = examples expose non-transfer; no application certificate yet.
```

## OPERA-004-B integration (LB-03, provisional_intake)

### Links to installed tools
```text
TOOL-SIEVE-INFO-CONSUMPTION-001 (Harman)   ← B one-sided certificate C_± (integration-heavy); the
                                             Positivity Information-Loss diagnostic is absorbed here (no new tool).
TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 ← normalization: z (sifting) != level of distribution; D consumes the budget.
```

### Frontier, walls, and the LB-03 boundary
```text
FRONTIER-ANT-PVG-004 (sieve information / support geometry) — the pillar B deepens.
WALL-PARITY        — registered, uncrossed. B maps NO boundary onto it. The prime-asymptotic gap and the
                     target-purity gap are Boundaries INSIDE LB-03, NOT parity claims; z>sqrt(x) avoids the
                     question (drops s), and parity re-examination is DEFERRED to the parity-grounding packet.
WALL-SIEVE-CEILING — registered, uncrossed; not mapped here.
Boundaries (B; all Boundaries, zero new WALL-ID):
  positive-lower-bound gate (a lower formula != a positive lower bound)
  prime-asymptotic gap (Boundary inside LB-03, the three-level ladder)
```

### Load-bearing linkage (B)
```text
LB-03 (upper/lower vs asymptotic prime sieve) = PRIMARY anchor of B (one-sided certificates, the ladder,
       sandwich-collapse, positive-lower gate, target-purity gap).
LB-04 (level of distribution) = reused via s = log D / log z and V^±.
LB-01 / LB-02 / LB-05 / LB-06 = not reached by B.
```

## Standing missing certificate (context only)

```text
MC-001 (parity) — unsolved. Added post-normalization as context; NOT a mining-selection criterion.
                  A sieve formulation of a prime problem is not progress on MC-001.
```

**Honest classification:** Reinterpretation / Diagnostic (integration links, intake). No RH progress. No GRH progress.
