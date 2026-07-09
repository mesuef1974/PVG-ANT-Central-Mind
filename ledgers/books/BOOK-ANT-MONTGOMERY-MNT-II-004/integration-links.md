# Montgomery MNT-II — Integration Links

Book ID: `BOOK-ANT-MONTGOMERY-MNT-II-004`. **v0.6 units MNTII-006-A + MNTII-006-B + MNTII-006-C + MNTII-006-D + MNTII-006-E.** طبقةُ الدمج: كنوزُ الوحدات ← المهاراتُ والجبهاتُ الحيّة (معرِّفاتٌ مسجَّلة). 006-A الضغط · 006-B الجدران · 006-C المتوسّط → جبهة 006؛ **006-D الغربالُ الكلاسيكيّ · 006-E الإلغاءُ الأُسّيّ/Kloosterman → جبهة الغربلة 004**.

## Treasure clusters → skills

```text
Distribution diagnostics (001,002,003,004)              → SKILL-MATH-ANT-001, SKILL-MATH-PVG-001
Prime/sieve interface bridge (005)                       → SKILL-MATH-SIEVE-001, SKILL-MATH-ANT-001
Missing certificates + walls (006,007,008)               → SKILL-GOV-CERT-001, SKILL-GOV-NOGO-001
Distributional limits / barriers (009,010,011,012,015)   → SKILL-MATH-ANT-001, SKILL-GOV-CERT-001
Conditional exclusion + standing certs (013,014)         → SKILL-GOV-NOGO-001, SKILL-GOV-CERT-001
Large sieve / BV on-average (016,017,019,021)            → SKILL-MATH-ANT-001, SKILL-MATH-SIEVE-001
Average≠individual + EH + standing certs (018,020,022)   → SKILL-GOV-CERT-001, SKILL-GOV-NOGO-001
Classical sieve — Selberg/Brun/lemma/κ (023,024,025,026) → SKILL-MATH-SIEVE-001, SKILL-MATH-ANT-001
Parity + Brun–Titchmarsh + standing cert (027,028,029)   → SKILL-GOV-NOGO-001, SKILL-GOV-CERT-001
Exp / Kloosterman cancellation (030,031,032,035)         → SKILL-MATH-ANT-001, SKILL-MATH-SIEVE-001
DI external + cancellation no-go + cert (033,034,036)    → SKILL-GOV-CERT-001, SKILL-GOV-BIB-001, SKILL-GOV-NOGO-001
```

## Direct frontier anchors

```text
FRONTIER-ANT-PVG-006  Zero-density and large values as frontier diagnostics
    ← 001–004 (006-A pressure) · 009–012 (006-B barriers) · 016,017,019,021 (006-C on-average)
    Montgomery MNT-II analytic ammunition around frontier 006 after v0.4 IK — diagnostic support, not results.

FRONTIER-ANT-PVG-004  Sieve information through PVG support geometry
    ← 005 primes-and-sieves interface · 016 large sieve · 023–026 classical Selberg/Brun sieve
    ← 030,031 exp/Kloosterman cancellation · 032 cancellation→Type-II · 035 cancellation behind the large sieve (006-E)
    006-D/006-E mine the sieve machinery + the off-diagonal cancellation that feeds Type-II —
    complementing Harman (TOOL-SIEVE-INFO-CONSUMPTION-001, TOOL-TYPE-I-II-DIAGNOSTIC-001).
```

## Frozen front (cited, not reopened)

```text
FRONTIER-ANT-PVG-007  Spectral/operator diagnostics and recoverability — status: FROZEN
    ← 033 Deshouillers–Iwaniec spectral bounds are cited as a KNOWN external input only; the frozen
      spectral front is NOT reopened by 006-E.
```

## Certificate-ledger anchors (all unsolved)

```text
MC-001  Unconditional parity break        ← 027, 029, 032, 034, 036         (UNSOLVED; WALL-PARITY; Type-II = missing external certificate, fed by cancellation)
MC-002  ψ(x)−x error / RH                  ← 002, 004, 006, 012, 014         (UNSOLVED; WALL-ZERO-FREE)
MC-005  AP distribution / GRH-level        ← 007, 014, 017, 018, 022         (UNSOLVED; WALL-SIEGEL + WALL-POSITIVITY-WEIL)
```

## Open problem (not a certificate, not a result)

```text
Elliott–Halberstam (level 1−ε)            ← 020   UNPROVEN conjecture; extends Bombieri–Vinogradov; no unconditional certificate.
```

## Walls in play (all uncrossed)

```text
WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL   the three standing walls of frontier 006
WALL-DENSITY-HYP · WALL-OFF-DIAGONAL                  diagnostic targets (density floor 17/30 = 1 − 1/A · off-diagonal cancellation)
WALL-PARITY · WALL-SIEVE-CEILING                     the sieve walls of frontier 004 (parity · unconditional sieve ceiling)
```

## Scope honesty (v0.6)

```text
Five narrow units ingested: MNTII-006-A (distribution diagnostics / certificate pressure),
MNTII-006-B (distributional limits / barriers), MNTII-006-C (large sieve / Bombieri–Vinogradov
on-average), MNTII-006-D (classical Selberg / combinatorial sieve, bounded reach), and MNTII-006-E
(exponential / Kloosterman sums, off-diagonal cancellation — the analytic source of Type-II). No
MNTII-006-F. No full book mining. Bombieri–Vinogradov is average (family) control, NOT individual GRH;
Elliott–Halberstam stays an unproven open problem; classical sieves give bounds / almost-primes, NOT
primes (parity); cancellation feeds Type-II but is NOT prime detection; Deshouillers–Iwaniec is cited
as external input with the spectral front FRONTIER-ANT-PVG-007 FROZEN and NOT reopened; RH-conditional
distributional statistics are out of unconditional scope. All entered as diagnostics feeding frontiers
006/004 — not improvements, not theorems. No RH/GRH progress.
```

**Honest classification:** Diagnostic / Boundary (integration links, v0.6 units A + B + C + D + E). No RH/GRH progress.
