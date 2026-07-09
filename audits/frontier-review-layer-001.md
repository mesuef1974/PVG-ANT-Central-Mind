# Frontier Review Layer 001 — Diagnostic Map

Registry ID: FRONTIER-REVIEW-LAYER-001-REPORT · Type: read-only diagnostic map · Classification: Release Governance / Diagnostic.
Reviewed at HEAD `1cdd56e`. **Diagnostic only — no solving, no theorem claim, no RH/GRH progress, no new live IDs.** Recommendations below are non-live suggestions.

## 1–6. The 8 frontiers (serving skills · missing certificate · walls · readiness · recommendation)

| Frontier | Serving live skills | Missing certificate | Walls (uncrossed) | Ready to diagnose? | Recommendation |
|---|---|---|---|---|---|
| **001** PVG geometry of arithmetic functions | `prime-valuation-geometry` · `analytic-number-theory` · `certificate-ledger` | structural theorem: PVG-type → analytic behavior (frontier-internal) | — (predictive-gain gap) | yes | **diagnose** (no in-mind path; keep as map) |
| **002** Multiplicative functions as observables | `analytic-number-theory` · `prime-valuation-geometry` (TOOL-HALASZ/DELANGE/WIRSING/SELBERG-DELANGE) | classification theorem (mean/cancellation types) | `WALL-PHASE` · `WALL-AVERAGE-NORMAL` | yes | **diagnose** (rich toolset; no new theorem) |
| **003** Möbius/Liouville cancellation | `analytic-number-theory` · `solve-math-rigorously` | nontrivial cancellation theorem | `WALL-ZERO-FREE` (cancellation tied to zeros); MC-002 | yes | **diagnose** (cancellation not from geometry alone) |
| **004** Sieve information via PVG support | `combinatorial-sieve` · `prime-valuation-geometry` | external certificate beyond diagnostic (Type-II) | `WALL-PARITY` · `WALL-SIEVE-CEILING`; MC-001 | yes | **needs book** (Opera de Cribro / Harman / Motohashi — available) |
| **005** Residue fibers / Dirichlet characters | `analytic-number-theory` · `prime-valuation-geometry` (OBS-CHARACTER-001 · OBS-RESIDUE-FIBER-001 · TOOL-CHARACTER-SUM-PHASE-001) | AP beyond Siegel–Walfisz = GRH-level → **MC-005** | `WALL-SIEGEL` · `WALL-POSITIVITY-WEIL` | **yes — advanced (005-A ingested)** | **needs Tenenbaum-005-B** (L(s,χ)/AP as certificate requirements) |
| **006** Zero-density / large values | `analytic-number-theory` | actual improved estimate (not diagnostic) | `WALL-ZERO-FREE` · `WALL-DENSITY-HYP` · `WALL-POSITIVITY-WEIL`; MC-002 | partial (naming only) | **needs book** (Iwaniec–Kowalski / Montgomery MNT-II — available) |
| **007** Spectral / operator recoverability | `operator-theory` · `spectral-analysis` · `spectral-operator-no-go` | invertibility / reconstruction theorem | `WALL-POSITIVITY-WEIL`; MC-003 | diagnose-only | **freeze** (no-go memory active; recoverability failure) |
| **008** Computational vs proof certificates | `numerical-assistant` · `computational-number-theory` · `certificate-ledger` | formal proof / certified finite theorem | — (finite ≠ infinite) | yes | **queue / diagnose** (governance boundary: measurement ≠ proof) |

**Note (staleness corrected):** frontier 005's registered `wall` ("Not started in v0.1b") and `missing_certificate` ("Tenenbaum-005-A import") are pre-v0.3 language; 005-A is now ingested, so the standing missing certificate for 005 is **MC-005** (GRH-level AP distribution). This is a display-vs-truth note; the live registry (MC-005) is correct.

## 7. Frontier suggesting Tenenbaum-005-B

**005** (Residue fibers / Dirichlet characters) — 005-A is done; the natural in-book continuation is 005-B (characters → `L(s,χ)` / AP distribution recorded as certificate requirements). Additive, lowest risk, no new book.

## 8. Frontier suggesting a new book

**006** (Zero-density / large values) → Iwaniec–Kowalski or Montgomery MNT-II (both `available`).
**004** (Sieve) → Opera de Cribro / Harman / Motohashi (all `available`).

## 9. Frontier to freeze

**007** (Spectral / operator) — `spectral-operator-no-go` + `no-go-memory` active (recoverability failure; no operator certificate). Keep diagnostic-only; do not pursue operator models.

## 10. Any RH/GRH overclaim?

**No.** Every frontier carries `rh_grh_status: no-progress-claim`; MC-005 and MC-001..004 are missing certificates, not results; `WALL-SIEGEL` and `WALL-POSITIVITY-WEIL` are not crossed anywhere. `honesty_audit` + `forbidden_promotion_audit` green.

## Missing certificates in play

```text
MC-001 parity · MC-002 psi(x)-x error / RH · MC-003 Weil positivity ·
MC-004 Artin holomorphy · MC-005 AP distribution (GRH-level)
```

## Uncrossed walls (all 13)

```text
PARITY · MINOR-ARC · ZERO-FREE · SIEGEL · POSITIVITY-WEIL · ARTIN · LINDELOF ·
SIEVE-CEILING · OFF-DIAGONAL · DENSITY-HYP · HURWITZ-CONV · PHASE · AVERAGE-NORMAL
```
None crossed. Constraint `CONSTRAINT-NO-CONFLATION` holds.

## Final — candidate next step (recommendation only, no execution)

```text
TOP CANDIDATE: Tenenbaum-005-B  (frontier 005; additive, in-book, lowest risk)
SECONDARY:     a new book for frontier 006 (Iwaniec-Kowalski) or 004 (Opera de Cribro)
FREEZE:        frontier 007 (spectral/operator, no-go)
DIAGNOSE-ONLY: frontiers 001, 002, 003, 008 (no in-mind path; keep as map)
```

Decide calmly from this map. No execution now.

**Ceiling:** this is a diagnostic map, not a solution and not a claim. zero RH progress · zero GRH progress · no secured path.
**Honest classification:** Release Governance / Diagnostic (read-only). No RH/GRH progress.
