# Montgomery MNT-II — Normalization Ledger

Book ID: `BOOK-ANT-MONTGOMERY-MNT-II-004`. **v0.6 units MNTII-006-A + MNTII-006-B + MNTII-006-C + MNTII-006-D + MNTII-006-E.** كلُّ كنزٍ في `treasure-map.md` ← ماذا صار داخل العقل (معرِّفاتٌ حيّة). المخرجاتُ الأساسيّةُ الجديدة: `TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001` (006-A) · `TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001` (006-B) · `TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001` (006-C) · `TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001` (006-D) · `TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001` (006-E) — كلُّها live في `registries/tools.jsonl`.

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

## Unit MNTII-006-E — normalization (exponential / Kloosterman sums, off-diagonal cancellation)

```text
TREASURE-MNTII-030  Exponential sums (Weyl / van der Corput)
  → Tool (NEW)        : TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001
  → Frontier          : FRONTIER-ANT-PVG-004
  → Wall              : WALL-OFF-DIAGONAL
  → PVG–ANT           : oscillation / cancellation observable on the off-diagonal

TREASURE-MNTII-031  Kloosterman sums / Weil bound (√ cancellation)
  → Tool (NEW)        : TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001
  → Wall              : WALL-OFF-DIAGONAL
  → PVG–ANT           : square-root cancellation on the residue-fiber off-diagonal

TREASURE-MNTII-032  Cancellation feeds Type-II / bilinear
  → Tool (NEW)        : TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001
  → Tool (neighbour)  : TOOL-TYPE-I-II-DIAGNOSTIC-001 (Harman, 006-D)
  → Wall              : WALL-PARITY
  → Missing Certificate: MC-001
  → PVG–ANT           : the off-diagonal cancellation feeding the Type-II certificate

TREASURE-MNTII-033  Deshouillers–Iwaniec spectral bounds (external; 007 frozen)
  → External (cited)  : known input; FRONTIER-ANT-PVG-007 stays FROZEN (not reopened)
  → PVG–ANT           : a deep external input, cited — not our result

TREASURE-MNTII-034  Cancellation ≠ prime detection (parity)
  → Wall              : WALL-PARITY
  → Missing Certificate: MC-001
  → PVG–ANT           : an oscillation observable, not a prime count

TREASURE-MNTII-035  Cancellation behind the large sieve / dispersion
  → Tool (NEW)        : TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001
  → Tool (neighbour)  : TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 (006-C)
  → PVG–ANT           : the shared cancellation source behind frontiers 006 and 004

TREASURE-MNTII-036  MC-001 unsolved; walls uncrossed; 007 frozen
  → Missing Certificate: MC-001 — UNSOLVED
  → Wall              : WALL-OFF-DIAGONAL · WALL-PARITY — UNCROSSED
  → Frontier (frozen) : FRONTIER-ANT-PVG-007 — FROZEN (not reopened)
  → PVG–ANT           : cancellation observed; parity and frozen spectral front standing
```

## Live IDs consolidated (units A + B + C + D + E)

```text
Tools (NEW, live) : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 (006-A) · TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001 (006-B) · TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 (006-C) · TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001 (006-D) · TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001 (006-E)   (all Diagnostic / Frontier Support)
Tools (neighbour) : TOOL-ZERO-DENSITY-DIAGNOSTIC-001 · TOOL-LARGE-VALUE-DIAGNOSTIC-001 · TOOL-SIEVE-INFO-CONSUMPTION-001 · TOOL-TYPE-I-II-DIAGNOSTIC-001
Observables       : OBS-CHARACTER-001 · OBS-RESIDUE-FIBER-001
Walls             : WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL · WALL-DENSITY-HYP · WALL-OFF-DIAGONAL · WALL-PARITY · WALL-SIEVE-CEILING
Missing           : MC-001 · MC-002 · MC-005   (all UNSOLVED)
Frontier          : FRONTIER-ANT-PVG-006 (A/B/C) · FRONTIER-ANT-PVG-004 (D/E) (+ bridge)
Frozen front      : FRONTIER-ANT-PVG-007 (spectral) — cited, not reopened
Open problem      : Elliott–Halberstam (unproven; no certificate)
```

**Consistency note:** each new tool (006-A/B/C/D + 006-E EXPSUM-DIAGNOSTIC) was registered as the single planned target of its unit then promoted to live in `registries/tools.jsonl` on honest completion; `planned.jsonl` is empty. Neighbour / observable ids pre-exist. MC-001, MC-002 & MC-005 UNSOLVED. Cancellation feeds Type-II but does not break parity; Deshouillers–Iwaniec cited as external input with FRONTIER-ANT-PVG-007 frozen; Bombieri–Vinogradov average-not-individual; Elliott–Halberstam unproven; classical sieves bounds / almost-primes not primes.

**Honest classification:** Diagnostic / Boundary (normalization ledger, v0.6 units A + B + C + D + E). No RH/GRH progress.
