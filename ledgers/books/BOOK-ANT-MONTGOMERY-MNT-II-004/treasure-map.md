# Montgomery MNT-II — Treasure Map

Book ID: `BOOK-ANT-MONTGOMERY-MNT-II-004`. **v0.6 — mining units `MNTII-006-A` (distribution diagnostics) and `MNTII-006-B` (distributional limits / barriers) ingested.** طبقةُ تعدينٍ تحت `governance/book-treasure-extraction-protocol.md`. مؤصَّلٌ على الوحدتين (transformed notes only، PDF خارج git). كنوزٌ محدودةٌ لوحدتين ضيّقتين؛ **باقي الكتاب غيرُ مُعدَّن** (see `missed-treasures.md`). لا نصٌّ خام، لا ادّعاءُ إتقانٍ كامل.

```text
Treasure ID: TREASURE-MNTII-001
Treasure:    Montgomery-style analytic tools as distribution diagnostics
Source:      MNTII-006-A — transformed notes only
Type:        frontier-support diagnostic
Why it matters: reads MNT-II's mean-value / large-value / zero-density machinery and the primes-and-sieves interface as distribution diagnostics for frontier 006, not results.
ANT role:    mean-value theorems · large-value estimates · zero-density context · primes-and-sieves interface.
PVG translation: off-diagonal / family-level support observable for frontier 006.
Wall / certificate: WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL (uncrossed); MC-002 / MC-005.
Classification: Diagnostic / Boundary.
Normalized output: → Tool TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 ; → Frontier FRONTIER-ANT-PVG-006.
```

```text
Treasure ID: TREASURE-MNTII-002
Treasure:    Distribution estimates as certificate pressure, not proof
Source:      MNTII-006-A — transformed notes only
Type:        no-go boundary
Why it matters: a distribution estimate is unconditional/average pressure toward RH, NOT a proof — it measures distance, it does not close it.
ANT role:    average error control without RH; distance-to-RH as a bounded quantity.
PVG translation: certificate pressure on the off-diagonal, not a certificate.
Wall / certificate: WALL-ZERO-FREE (uncrossed); MC-002 unsolved.
Classification: Boundary.
Normalized output: → Tool TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 (pressure reading) ; → Missing Certificate MC-002.
```

```text
Treasure ID: TREASURE-MNTII-003
Treasure:    Mean / large-value control as family-level support
Source:      MNTII-006-A — transformed notes only
Type:        diagnostic support
Why it matters: mean-value (second-moment) and large-value estimates control the family ON AVERAGE, feeding zero-density — family control, not pointwise.
ANT role:    neighbours IK's large-value machinery; average control of Dirichlet polynomials.
PVG translation: family-average control of the off-diagonal observable.
Wall / certificate: WALL-OFF-DIAGONAL · WALL-DENSITY-HYP.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 ; relates TOOL-LARGE-VALUE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-004
Treasure:    Zero-density context as partial support, not pointwise resolution
Source:      MNTII-006-A — transformed notes only
Type:        no-go boundary
Why it matters: zero-density context is a conditional/average substitute for RH in error terms — it does NOT resolve pointwise distribution.
ANT role:    neighbours IK's zero-density diagnostic; average error, not pointwise ψ(x)−x.
PVG translation: off-diagonal average ≠ diagonal/pointwise truth.
Wall / certificate: WALL-ZERO-FREE · WALL-DENSITY-HYP (uncrossed); MC-002.
Classification: Boundary.
Normalized output: → Missing Certificate MC-002 ; relates TOOL-ZERO-DENSITY-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-005
Treasure:    Prime / sieve interface as diagnostic bridge
Source:      MNTII-006-A — transformed notes only
Type:        bridge / diagnostic
Why it matters: the primes-and-sieves interface of MNT-II bridges the analytic front (006) and the sieve-information front (004) as a diagnostic, not a crossing.
ANT role:    analytic distribution tools meet sieve information at the primes-and-sieves interface.
PVG translation: a diagnostic bridge between the analytic and sieve support geometries.
Wall / certificate: WALL-PARITY (contextual, sieve side) — uncrossed.
Classification: Diagnostic.
Normalized output: → Frontier FRONTIER-ANT-PVG-006 (bridge to FRONTIER-ANT-PVG-004).
```

```text
Treasure ID: TREASURE-MNTII-006
Treasure:    MC-002 remains unsolved
Source:      MNTII-006-A — transformed notes only
Type:        missing certificate (standing)
Why it matters: names what MNT-II distribution tools do NOT deliver — a strong ψ(x)−x error at RH strength.
ANT role:    the RH-level prime-error certificate.
PVG translation: diagonal/pointwise prime-error certificate.
Wall / certificate: WALL-ZERO-FREE; MC-002 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-002 (governance/missing-certificates.md).
```

```text
Treasure ID: TREASURE-MNTII-007
Treasure:    MC-005 remains unsolved
Source:      MNTII-006-A — transformed notes only
Type:        missing certificate (standing)
Why it matters: names what MNT-II distribution tools do NOT deliver — AP distribution beyond Siegel–Walfisz at GRH strength for the individual modulus.
ANT role:    the GRH-level AP distribution certificate.
PVG translation: individual residue-fiber distribution certificate.
Wall / certificate: WALL-SIEGEL + WALL-POSITIVITY-WEIL; MC-005 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-005 (governance/missing-certificates.md).
```

```text
Treasure ID: TREASURE-MNTII-008
Treasure:    WALL-SIEGEL / WALL-POSITIVITY-WEIL / WALL-ZERO-FREE remain uncrossed
Source:      MNTII-006-A — transformed notes only
Type:        standing walls
Why it matters: the three standing walls of frontier 006 are untouched by the distribution diagnostics.
ANT role:    exceptional-zero / positivity / zero-free obstructions.
PVG translation: the walls observed but not crossed.
Wall / certificate: WALL-SIEGEL · WALL-POSITIVITY-WEIL · WALL-ZERO-FREE — UNCROSSED.
Classification: Boundary.
Normalized output: → Wall WALL-SIEGEL, WALL-POSITIVITY-WEIL, WALL-ZERO-FREE (uncrossed).
```

## Unit MNTII-006-B — distributional limits / barriers (7 cards)

```text
Treasure ID: TREASURE-MNTII-009
Treasure:    Distributional limits as diagnostic barriers
Source:      MNTII-006-B — transformed notes only
Type:        barrier diagnostic
Why it matters: names where the UNCONDITIONAL mean/large-value method stops — the barrier is the diagnostic, not a crossing.
ANT role:    the unconditional stopping point of the distribution machinery.
PVG translation: the wall where 006-A's certificate pressure runs out.
Wall / certificate: WALL-POSITIVITY-WEIL (primary) — uncrossed.
Classification: Diagnostic / Boundary.
Normalized output: → Tool TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001 ; → Frontier FRONTIER-ANT-PVG-006.
```

```text
Treasure ID: TREASURE-MNTII-010
Treasure:    Density-hypothesis floor as an explicit barrier
Source:      MNTII-006-B — transformed notes only
Type:        standing wall
Why it matters: the density-hypothesis floor 17/30 = 1 − 1/A is the unconditional zero-density limit — an explicit, named barrier.
ANT role:    the best unconditional zero-density exponent region.
PVG translation: the off-diagonal density barrier.
Wall / certificate: WALL-DENSITY-HYP — uncrossed.
Classification: Boundary.
Normalized output: → Wall WALL-DENSITY-HYP.
```

```text
Treasure ID: TREASURE-MNTII-011
Treasure:    Positivity / Weil wall as the distributional barrier
Source:      MNTII-006-B — transformed notes only
Type:        standing wall
Why it matters: the explicit-formula positivity (Weil) requirement is the barrier the distribution machinery cannot supply.
ANT role:    Weil positivity of the explicit formula.
PVG translation: the positivity barrier of the prime↔zero accounting.
Wall / certificate: WALL-POSITIVITY-WEIL — uncrossed.
Classification: Boundary.
Normalized output: → Wall WALL-POSITIVITY-WEIL.
```

```text
Treasure ID: TREASURE-MNTII-012
Treasure:    Zero-free limit as the barrier to a pointwise error
Source:      MNTII-006-B — transformed notes only
Type:        standing wall
Why it matters: without a wider zero-free region / RH, a strong pointwise ψ(x)−x error is unreachable — WALL-ZERO-FREE is the barrier.
ANT role:    the zero-free-region limit on the prime error.
PVG translation: the diagonal / pointwise barrier.
Wall / certificate: WALL-ZERO-FREE — uncrossed; MC-002 unsolved.
Classification: Boundary.
Normalized output: → Wall WALL-ZERO-FREE ; → Missing Certificate MC-002.
```

```text
Treasure ID: TREASURE-MNTII-013
Treasure:    RH-conditional distributional statistics are out of unconditional scope
Source:      MNTII-006-B — transformed notes only
Type:        no-go boundary (conditional exclusion)
Why it matters: fine distributional statistics (Montgomery pair correlation, Rubinstein–Sarnak prime races) are RH-conditional and yield NO unconditional certificate — explicitly excluded here.
ANT role:    pair correlation and prime-race limiting distributions are conditional on RH (and more).
PVG translation: conditional statistics give no unconditional support to frontier 006.
Wall / certificate: conditional on RH; not usable unconditionally — deferred.
Classification: Boundary.
Normalized output: → deferred (see missed-treasures.md); no unconditional tool.
```

```text
Treasure ID: TREASURE-MNTII-014
Treasure:    Barriers do not resolve MC-002 / MC-005
Source:      MNTII-006-B — transformed notes only
Type:        missing certificates (standing)
Why it matters: mapping the barriers does NOT supply the missing certificates — MC-002 and MC-005 remain open.
ANT role:    the RH-level prime error (MC-002) and GRH-level AP distribution (MC-005).
PVG translation: the barrier map locates the walls; the certificates behind them stay missing.
Wall / certificate: WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL; MC-002 & MC-005 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-002, MC-005 (governance/missing-certificates.md).
```

```text
Treasure ID: TREASURE-MNTII-015
Treasure:    The distributional barriers remain uncrossed
Source:      MNTII-006-B — transformed notes only
Type:        standing walls
Why it matters: WALL-POSITIVITY-WEIL, WALL-DENSITY-HYP, WALL-ZERO-FREE, WALL-SIEGEL are mapped as barriers, none crossed.
ANT role:    the standing distributional walls of frontier 006.
PVG translation: barriers observed, not crossed.
Wall / certificate: WALL-POSITIVITY-WEIL · WALL-DENSITY-HYP · WALL-ZERO-FREE · WALL-SIEGEL — UNCROSSED.
Classification: Boundary.
Normalized output: → Wall WALL-POSITIVITY-WEIL, WALL-DENSITY-HYP, WALL-ZERO-FREE, WALL-SIEGEL (uncrossed).
```

**Honest classification:** Diagnostic / Boundary (treasure map, v0.6 units A + B). No RH/GRH progress. No zero-density/large-values improvement, no distributional-limit theorem; RH-conditional statistics out of scope. MC-002 & MC-005 unsolved; walls uncrossed.
