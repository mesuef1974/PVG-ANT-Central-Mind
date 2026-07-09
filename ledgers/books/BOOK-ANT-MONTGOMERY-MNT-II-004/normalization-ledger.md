# Montgomery MNT-II — Normalization Ledger

Book ID: `BOOK-ANT-MONTGOMERY-MNT-II-004`. **v0.6 units MNTII-006-A + MNTII-006-B + MNTII-006-C + MNTII-006-D.** كلُّ كنزٍ في `treasure-map.md` ← ماذا صار داخل العقل (معرِّفاتٌ حيّة). المخرجاتُ الأساسيّةُ الجديدة: `TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001` (006-A) · `TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001` (006-B) · `TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001` (006-C) · `TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001` (006-D) — كلُّها live في `registries/tools.jsonl`.

```text
TREASURE-MNTII-001  Montgomery-style analytic tools as distribution diagnostics
  → Tool (NEW)        : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001
  → Frontier          : FRONTIER-ANT-PVG-006
  → Wall              : WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL
  → PVG–ANT           : off-diagonal / family-level support observable for frontier 006

TREASURE-MNTII-002  Distribution estimates as certificate pressure, not proof
  → Tool (NEW)        : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 (pressure reading)
  → Missing Certificate: MC-002
  → PVG–ANT           : certificate pressure on the off-diagonal, not a certificate

TREASURE-MNTII-003  Mean / large-value control as family-level support
  → Tool (NEW)        : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001
  → Tool (neighbour)  : TOOL-LARGE-VALUE-DIAGNOSTIC-001
  → Wall              : WALL-OFF-DIAGONAL · WALL-DENSITY-HYP
  → PVG–ANT           : family-average control of the off-diagonal observable

TREASURE-MNTII-004  Zero-density context as partial support, not pointwise resolution
  → Tool (neighbour)  : TOOL-ZERO-DENSITY-DIAGNOSTIC-001
  → Missing Certificate: MC-002
  → Wall              : WALL-ZERO-FREE · WALL-DENSITY-HYP
  → PVG–ANT           : off-diagonal average ≠ pointwise truth

TREASURE-MNTII-005  Prime / sieve interface as diagnostic bridge
  → Frontier          : FRONTIER-ANT-PVG-006 (bridge to FRONTIER-ANT-PVG-004)
  → Wall              : WALL-PARITY (contextual)
  → PVG–ANT           : diagnostic bridge between analytic and sieve support geometries

TREASURE-MNTII-006  MC-002 remains unsolved
  → Missing Certificate: MC-002   (governance/missing-certificates.md) — UNSOLVED
  → Wall              : WALL-ZERO-FREE

TREASURE-MNTII-007  MC-005 remains unsolved
  → Missing Certificate: MC-005   (governance/missing-certificates.md) — UNSOLVED
  → Wall              : WALL-SIEGEL · WALL-POSITIVITY-WEIL

TREASURE-MNTII-008  Three walls uncrossed
  → Wall              : WALL-SIEGEL · WALL-POSITIVITY-WEIL · WALL-ZERO-FREE — UNCROSSED
  → PVG–ANT           : walls observed, not crossed
```

## Unit MNTII-006-B — normalization (distributional limits / barriers)

```text
TREASURE-MNTII-009  Distributional limits as diagnostic barriers
  → Tool (NEW)        : TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001
  → Frontier          : FRONTIER-ANT-PVG-006
  → Wall              : WALL-POSITIVITY-WEIL
  → PVG–ANT           : the wall where 006-A's certificate pressure runs out

TREASURE-MNTII-010  Density-hypothesis floor barrier
  → Wall              : WALL-DENSITY-HYP  (17/30 = 1 − 1/A)
  → PVG–ANT           : the unconditional off-diagonal density limit

TREASURE-MNTII-011  Positivity / Weil barrier
  → Wall              : WALL-POSITIVITY-WEIL
  → PVG–ANT           : the positivity barrier of the prime↔zero accounting

TREASURE-MNTII-012  Zero-free limit barrier
  → Wall              : WALL-ZERO-FREE
  → Missing Certificate: MC-002
  → PVG–ANT           : the diagonal / pointwise barrier

TREASURE-MNTII-013  RH-conditional distributional statistics (excluded)
  → Deferred          : conditional on RH (pair correlation / prime races) — no unconditional tool (see missed-treasures.md)
  → PVG–ANT           : conditional statistics give no unconditional support

TREASURE-MNTII-014  Barriers do not resolve MC-002 / MC-005
  → Missing Certificate: MC-002 · MC-005 — UNSOLVED
  → Wall              : WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL
  → PVG–ANT           : barriers located; certificates behind them stay missing

TREASURE-MNTII-015  Distributional barriers uncrossed
  → Wall              : WALL-POSITIVITY-WEIL · WALL-DENSITY-HYP · WALL-ZERO-FREE · WALL-SIEGEL — UNCROSSED
  → PVG–ANT           : barriers observed, not crossed
```

## Unit MNTII-006-C — normalization (large sieve / Bombieri–Vinogradov on-average)

```text
TREASURE-MNTII-016  Large sieve inequality as a mean-value diagnostic
  → Tool (NEW)        : TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001
  → Frontier          : FRONTIER-ANT-PVG-006
  → Wall              : WALL-OFF-DIAGONAL · WALL-DENSITY-HYP
  → PVG–ANT           : the family/average mean-value inequality on the off-diagonal

TREASURE-MNTII-017  Bombieri–Vinogradov as on-average as-if-GRH
  → Tool (NEW)        : TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001
  → Missing Certificate: MC-005  (individual case beyond BV)
  → PVG–ANT           : unconditional average AP distribution to level 1/2

TREASURE-MNTII-018  Average control ≠ individual GRH certificate
  → Missing Certificate: MC-005
  → Wall              : WALL-SIEGEL
  → PVG–ANT           : family-average observable ≠ individual residue-fiber certificate

TREASURE-MNTII-019  Dispersion method as a bilinear / average diagnostic
  → Tool (NEW)        : TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001
  → Wall              : WALL-OFF-DIAGONAL
  → PVG–ANT           : the bilinear (off-diagonal) route to average control

TREASURE-MNTII-020  Elliott–Halberstam (unproven conjectural extension)
  → Open Problem      : level 1−ε conjecture — no tool, no certificate (deferred)
  → PVG–ANT           : a conjectural (not achieved) average-distribution level

TREASURE-MNTII-021  Large sieve = the mean-value inequality behind zero-density
  → Tool (NEW)        : TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001
  → Tool (neighbour)  : TOOL-ZERO-DENSITY-DIAGNOSTIC-001 · TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001
  → Wall              : WALL-DENSITY-HYP
  → PVG–ANT           : the shared average-control root of the frontier-006 diagnostics

TREASURE-MNTII-022  MC-005 unsolved; walls uncrossed
  → Missing Certificate: MC-005 — UNSOLVED
  → Wall              : WALL-SIEGEL · WALL-POSITIVITY-WEIL — UNCROSSED
  → PVG–ANT           : average control leaves the individual certificate and walls standing
```

## Unit MNTII-006-D — normalization (Selberg / combinatorial sieve, bounded reach)

```text
TREASURE-MNTII-023  Selberg Λ²-sieve (upper bound)
  → Tool (NEW)        : TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001
  → Frontier          : FRONTIER-ANT-PVG-004
  → Wall              : WALL-SIEVE-CEILING
  → PVG–ANT           : an upper-bound observable on the sifted support

TREASURE-MNTII-024  Brun combinatorial sieve (upper + lower bounds)
  → Tool (NEW)        : TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001
  → Wall              : WALL-SIEVE-CEILING
  → PVG–ANT           : truncated inclusion–exclusion on the support

TREASURE-MNTII-025  Fundamental lemma of sieve theory
  → Tool (NEW)        : TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001
  → Wall              : WALL-PARITY (beyond the small-sieve range)
  → PVG–ANT           : the small sieve to level of distribution D

TREASURE-MNTII-026  Sieve dimension κ (diagnostic parameter)
  → Tool (NEW)        : TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001
  → PVG–ANT           : the dimension parameter governing sieve reach

TREASURE-MNTII-027  Almost-primes, not primes — parity barrier
  → Wall              : WALL-PARITY
  → Missing Certificate: MC-001
  → Tool (neighbour)  : TOOL-SIEVE-INFO-CONSUMPTION-001 · TOOL-TYPE-I-II-DIAGNOSTIC-001 (Harman)
  → PVG–ANT           : Type-II is the missing external certificate (not from the sieve)

TREASURE-MNTII-028  Brun–Titchmarsh (upper bound, not asymptotic)
  → Wall              : WALL-SIEVE-CEILING
  → PVG–ANT           : an upper bound with no main term

TREASURE-MNTII-029  MC-001 unsolved; walls uncrossed
  → Missing Certificate: MC-001 — UNSOLVED
  → Wall              : WALL-PARITY · WALL-SIEVE-CEILING — UNCROSSED
  → PVG–ANT           : parity uncrossed; sieve reach bounded
```

## Live IDs consolidated (units A + B + C + D)

```text
Tools (NEW, live) : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 (006-A) · TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001 (006-B) · TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 (006-C) · TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001 (006-D)   (all Diagnostic / Frontier Support)
Tools (neighbour) : TOOL-ZERO-DENSITY-DIAGNOSTIC-001 · TOOL-LARGE-VALUE-DIAGNOSTIC-001 · TOOL-SIEVE-INFO-CONSUMPTION-001 · TOOL-TYPE-I-II-DIAGNOSTIC-001
Observables       : OBS-CHARACTER-001 · OBS-RESIDUE-FIBER-001
Walls             : WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL · WALL-DENSITY-HYP · WALL-OFF-DIAGONAL · WALL-PARITY · WALL-SIEVE-CEILING
Missing           : MC-001 · MC-002 · MC-005   (all UNSOLVED)
Frontier          : FRONTIER-ANT-PVG-006 (A/B/C) · FRONTIER-ANT-PVG-004 (D) (+ bridge)
Open problem      : Elliott–Halberstam (unproven; no certificate)
```

**Consistency note:** each new tool (006-A DISTRIBUTION-DIAGNOSTIC · 006-B DISTRIBUTION-BARRIER · 006-C LARGE-SIEVE-DIAGNOSTIC · 006-D SIEVE-DIAGNOSTIC) was registered as the single planned target of its unit then promoted to live in `registries/tools.jsonl` on honest completion; `planned.jsonl` is empty. Neighbour / observable ids pre-exist. MC-001, MC-002 & MC-005 UNSOLVED. Bombieri–Vinogradov is average-not-individual; Elliott–Halberstam is an unproven open problem; classical sieves give bounds / almost-primes not primes (parity); RH-conditional statistics are excluded.

**Honest classification:** Diagnostic / Boundary (normalization ledger, v0.6 units A + B + C + D). No RH/GRH progress.
