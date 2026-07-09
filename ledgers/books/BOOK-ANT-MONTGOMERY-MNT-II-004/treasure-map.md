# Montgomery MNT-II — Treasure Map

Book ID: `BOOK-ANT-MONTGOMERY-MNT-II-004`. **v0.6 — SOURCE-GROUNDING-CORRECTED (Correction 006).** Trusted source-grounded units: `MNTII-006-C` (large sieve / Bombieri–Vinogradov, Ch 19–20), `MNTII-006-D` (Selberg / combinatorial sieve, Ch 21), `MNTII-006-E` (**bounded gaps / GPY / Maynard, Ch 22 — validated_intake, NOT closed**). **Quarantined (cross-volume / source-mismatch, NOT trusted):** `MNTII-006-A`, `MNTII-006-B` (zero-density / large values / pair-correlation — deferred by the source to a later volume) and the legacy off-diagonal E (`units/_quarantine/`). طبقةُ تعدينٍ تحت `governance/book-treasure-extraction-protocol.md`، مؤصَّلةٌ على المصدر (transformed notes only، PDF خارج git). **باقي الكتاب غيرُ مُعدَّن** (see `missed-treasures.md`). لا نصٌّ خام، لا ادّعاءُ إتقانٍ كامل.

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

## Unit MNTII-006-C — large sieve / Bombieri–Vinogradov on-average (7 cards)

```text
Treasure ID: TREASURE-MNTII-016
Treasure:    Large sieve inequality as a mean-value diagnostic
Source:      MNTII-006-C — transformed notes only
Type:        mean-value diagnostic
Why it matters: the large sieve is the duality/bilinear mean-value inequality behind average AP distribution and zero-density — mined now (kept as "context" in IK/Harman).
ANT role:    a mean-value inequality for Dirichlet polynomials / character sums over well-spaced points.
PVG translation: the family/average control inequality on the off-diagonal.
Wall / certificate: WALL-OFF-DIAGONAL · WALL-DENSITY-HYP — uncrossed.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 ; → Frontier FRONTIER-ANT-PVG-006.
```

```text
Treasure ID: TREASURE-MNTII-017
Treasure:    Bombieri–Vinogradov as on-average as-if-GRH
Source:      MNTII-006-C — transformed notes only
Type:        on-average distribution diagnostic
Why it matters: BV gives unconditional average AP distribution to level 1/2 — "as if GRH on average" — the classic AVERAGE substitute for individual GRH.
ANT role:    Σ_{q≤√x} max_a |ψ(x;q,a) − x/φ(q)| is small (unconditional).
PVG translation: average residue-fiber distribution, unconditional.
Wall / certificate: the individual case beyond BV needs GRH — MC-005 (unsolved).
Classification: Known / Diagnostic / Boundary.
Normalized output: → Tool TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 ; → Missing Certificate MC-005.
```

```text
Treasure ID: TREASURE-MNTII-018
Treasure:    Average control ≠ individual GRH certificate
Source:      MNTII-006-C — transformed notes only
Type:        no-go boundary
Why it matters: BV's average-over-q control does NOT certify the individual modulus at GRH strength — the gap is exactly MC-005.
ANT role:    average-over-q ≠ individual-q GRH-level distribution.
PVG translation: family-average observable ≠ individual residue-fiber certificate.
Wall / certificate: WALL-SIEGEL (individual exceptional zeros); MC-005 unsolved.
Classification: Boundary.
Normalized output: → Missing Certificate MC-005 ; → Wall WALL-SIEGEL.
```

```text
Treasure ID: TREASURE-MNTII-019
Treasure:    Dispersion method as a bilinear / average diagnostic
Source:      MNTII-006-C — transformed notes only
Type:        technique diagnostic
Why it matters: the Linnik–Bombieri dispersion method is the bilinear/average technique behind BV-type distribution — a diagnostic of how average control is obtained.
ANT role:    dispersion / bilinear decomposition of the AP error on average.
PVG translation: the bilinear (off-diagonal) route to average control.
Wall / certificate: WALL-OFF-DIAGONAL — diagnostic; not individual.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-020
Treasure:    Elliott–Halberstam as an unproven conjectural extension
Source:      MNTII-006-C — transformed notes only
Type:        open problem
Why it matters: EH extends BV to level 1−ε; it is UNPROVEN and provides no unconditional certificate — named as an open problem, not a result.
ANT role:    the conjectural higher level of distribution beyond Bombieri–Vinogradov.
PVG translation: a conjectural (not achieved) average-distribution level.
Wall / certificate: unproven; no certificate; "the sixth wall is empty" (no unconditional sieve reaches RH; EH alone).
Classification: Open Problem / Boundary.
Normalized output: → deferred (open problem; no tool, no certificate).
```

```text
Treasure ID: TREASURE-MNTII-021
Treasure:    Large sieve is the mean-value inequality behind zero-density
Source:      MNTII-006-C — transformed notes only
Type:        connection diagnostic
Why it matters: the large sieve is the mean-value inequality behind zero-density estimates; the trusted neighbours are the IK zero-density diagnostics (the MNTII-006-A/B readings are QUARANTINED, cross-volume).
ANT role:    large-value / mean-value input → N(σ,T) bounds (IK-006-A/B; the MNTII-006-A/B framing is quarantined).
PVG translation: the shared average-control root of the frontier-006 diagnostics.
Wall / certificate: WALL-DENSITY-HYP (the density floor it feeds) — uncrossed.
Classification: Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 ; relates TOOL-ZERO-DENSITY-DIAGNOSTIC-001 (trusted, IK) and TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 (QUARANTINED, source-mismatch — cited as history, not as a live neighbour).
```

```text
Treasure ID: TREASURE-MNTII-022
Treasure:    MC-005 unsolved; WALL-SIEGEL / WALL-POSITIVITY-WEIL uncrossed
Source:      MNTII-006-C — transformed notes only
Type:        standing certificate + walls
Why it matters: the large-sieve / BV diagnostic does NOT resolve the individual AP certificate or cross the exceptional-zero / positivity walls.
ANT role:    individual GRH-level AP (MC-005) and the Siegel / positivity obstructions.
PVG translation: average control leaves the individual certificate and the walls standing.
Wall / certificate: WALL-SIEGEL · WALL-POSITIVITY-WEIL — UNCROSSED; MC-005 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-005 ; → Wall WALL-SIEGEL, WALL-POSITIVITY-WEIL (uncrossed).
```

## Unit MNTII-006-D — Selberg / combinatorial sieve, bounded reach (7 cards)

```text
Treasure ID: TREASURE-MNTII-023
Treasure:    Selberg Λ²-sieve as an upper-bound diagnostic
Source:      MNTII-006-D — transformed notes only
Type:        sieve diagnostic (upper bound)
Why it matters: the Selberg sieve optimizes Λ² weights for an upper bound on sifted sets — the workhorse upper-bound sieve.
ANT role:    quadratic (Λ²) optimization giving Brun–Titchmarsh-type upper bounds.
PVG translation: an upper-bound observable on the sifted support.
Wall / certificate: upper bound only — no main term; WALL-SIEVE-CEILING.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001 ; → Frontier FRONTIER-ANT-PVG-004.
```

```text
Treasure ID: TREASURE-MNTII-024
Treasure:    Brun combinatorial sieve (upper and lower bounds)
Source:      MNTII-006-D — transformed notes only
Type:        sieve diagnostic (two-sided)
Why it matters: truncated inclusion–exclusion gives BOTH upper and lower bounds — the combinatorial route to almost-primes.
ANT role:    Brun's truncation of the Legendre sieve; upper/lower sieve bounds.
PVG translation: two-sided bounds on the sifted support.
Wall / certificate: bounds only; WALL-SIEVE-CEILING.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-025
Treasure:    The fundamental lemma of sieve theory
Source:      MNTII-006-D — transformed notes only
Type:        sieve law
Why it matters: for a small sieve (bounded dimension) up to level of distribution D, the sifted count matches the expected main term with a controlled error.
ANT role:    the small-sieve asymptotic to level D, dimension κ.
PVG translation: the reach of the sieve as a function of the level of distribution.
Wall / certificate: valid only in the small-sieve range; parity beyond — WALL-PARITY.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-026
Treasure:    Sieve dimension κ as the diagnostic parameter
Source:      MNTII-006-D — transformed notes only
Type:        diagnostic parameter
Why it matters: the sieve dimension κ (e.g. κ=1 linear sieve) governs what the sieve can deliver and where lower bounds hold.
ANT role:    κ = average number of residue classes removed per prime.
PVG translation: the parameter tuning sieve reach on the support geometry.
Wall / certificate: κ bounds the reach; parity independent — WALL-PARITY.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-027
Treasure:    Sieves count almost-primes, not primes — the parity barrier
Source:      MNTII-006-D — transformed notes only
Type:        no-go boundary
Why it matters: classical sieves cannot distinguish numbers with an even vs odd number of prime factors — the parity barrier blocks prime detection without external Type-II.
ANT role:    the parity obstruction; Type-II is the missing external certificate (Harman).
PVG translation: the wall the sieve observes but does not cross; Type-II crosses it.
Wall / certificate: WALL-PARITY — uncrossed; MC-001 unsolved.
Classification: Boundary.
Normalized output: → Wall WALL-PARITY ; → Missing Certificate MC-001 ; relates TOOL-SIEVE-INFO-CONSUMPTION-001, TOOL-TYPE-I-II-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-028
Treasure:    Brun–Titchmarsh as an upper bound, not an asymptotic
Source:      MNTII-006-D — transformed notes only
Type:        no-go boundary
Why it matters: Brun–Titchmarsh bounds π(x;q,a) from above by ~2x/(φ(q) log(x/q)) — an UPPER bound with a factor ~2, not a main-term asymptotic.
ANT role:    the sieve upper bound for primes in APs; no lower/main term.
PVG translation: a ceiling observable, not a count.
Wall / certificate: WALL-SIEVE-CEILING — uncrossed.
Classification: Boundary.
Normalized output: → Wall WALL-SIEVE-CEILING.
```

```text
Treasure ID: TREASURE-MNTII-029
Treasure:    MC-001 unsolved; WALL-PARITY / WALL-SIEVE-CEILING uncrossed
Source:      MNTII-006-D — transformed notes only
Type:        standing certificate + walls
Why it matters: the classical-sieve diagnostic does NOT break parity or supply the external Type-II certificate.
ANT role:    the unconditional parity break (MC-001) and the sieve ceiling.
PVG translation: sieve reach bounded; parity uncrossed.
Wall / certificate: WALL-PARITY · WALL-SIEVE-CEILING — UNCROSSED; MC-001 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-001 ; → Wall WALL-PARITY, WALL-SIEVE-CEILING (uncrossed).
```

## Unit MNTII-006-E — bounded gaps / GPY / Maynard (7 cards, source-grounded intake; Ch 22)

> **Source-Grounding Correction 006:** these seven cards replace the quarantined off-diagonal / Kloosterman
> cards (topic deferred by the source to a later volume). Unit E status = **validated_intake, NOT closed**.

```text
Treasure ID: TREASURE-MNTII-030
Treasure:    Admissible tuples as local obstruction geometry
Source:      MNTII-006-E (Ch 22) — transformed notes only
Type:        object / support geometry
Why it matters: an admissible k-tuple avoids a local residue obstruction at every prime; it is NOT a guaranteed all-prime tuple.
ANT role:    H is admissible iff for every prime p the tuple does not cover all residue classes mod p.
PVG translation: a shifted support configuration avoiding local residue obstructions.
Wall / certificate: local admissibility is necessary, not sufficient; WALL-PARITY.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 ; → Frontier FRONTIER-ANT-PVG-004.
```

```text
Treasure ID: TREASURE-MNTII-031
Treasure:    GPY weights as a prime-rich-tuple diagnostic
Source:      MNTII-006-E (Ch 22, §22.1) — transformed notes only
Type:        sieve-weight diagnostic
Why it matters: the GPY sieve weights select translates n+H richer in primes than average — a weighting device, NOT a prime detector.
ANT role:    Selberg-type weights over the tuple, tuned to prime indicators.
PVG translation: an optimization weight over residue-filtered boxes, NOT a primality certificate.
Wall / certificate: WALL-SIEVE-CEILING; MC-001 (weights are not prime detectors).
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-032
Treasure:    Maynard multidimensional sieve optimization
Source:      MNTII-006-E (Ch 22, §22.2) — transformed notes only
Type:        method (KNOWN theorem)
Why it matters: Maynard's multidimensional weights optimize the count of primes in a translate, yielding bounded gaps from a positive level of distribution — a KNOWN theorem, NOT our result.
ANT role:    variational optimization over multidimensional sieve weights.
PVG translation: optimization over residue-filtered boxes; the decisive certificate stays analytic.
Wall / certificate: needs an external level of distribution; WALL-SIEVE-CEILING.
Classification: Known.
Normalized output: → Tool TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-033
Treasure:    Level of distribution as external certificate
Source:      MNTII-006-E (Ch 20 / 22) — transformed notes only
Type:        external input
Why it matters: the sieve needs a positive level of distribution for the primes as EXTERNAL input; it does not produce it.
ANT role:    the level parameter controlling average distribution over moduli.
PVG translation: the analytic distribution certificate the weighted sieve consumes.
Wall / certificate: Bombieri–Vinogradov supplies level 1/2 unconditionally (on average); MC-005 (individual) unsolved.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 ; relates TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 (006-C).
```

```text
Treasure ID: TREASURE-MNTII-034
Treasure:    BV gives bounded gaps through average distribution, not GRH
Source:      MNTII-006-E (Ch 22, §22.4 notes) — transformed notes only
Type:        boundary
Why it matters: with Bombieri–Vinogradov as input, Maynard obtains bounded gaps UNCONDITIONALLY — via average distribution, NOT individual GRH.
ANT role:    BV (average, level 1/2) feeds the sieve; no individual GRH is used.
PVG translation: average residue-fiber distribution, not individual control.
Wall / certificate: individual case — WALL-SIEGEL; MC-005 unsolved.
Classification: Known / Boundary.
Normalized output: → Missing Certificate MC-005 ; relates TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-MNTII-035
Treasure:    EH-dependent improvements are conditional only
Source:      MNTII-006-E (Ch 22, §22.3/22.4) — transformed notes only
Type:        open problem / conditional
Why it matters: stronger bounded-gap conclusions under Elliott–Halberstam-type hypotheses are CONDITIONAL — EH is unproven.
ANT role:    EH (level 1−ε) would sharpen the gap; it is not available unconditionally.
PVG translation: a conditional (not achieved) sharpening.
Wall / certificate: EH unproven; no unconditional certificate; WALL-DENSITY-HYP context.
Classification: Open Problem / Boundary.
Normalized output: → deferred (open problem; no certificate).
```

```text
Treasure ID: TREASURE-MNTII-036
Treasure:    Bounded gaps are not twin primes and not a parity breakthrough
Source:      MNTII-006-E (Ch 22) — transformed notes only
Type:        no-go boundary
Why it matters: bounded gaps between primes is a KNOWN theorem; it is NOT the twin-prime conjecture and does NOT break the parity barrier.
ANT role:    a finite gap bound, not gap = 2; the parity obstruction stands.
PVG translation: a prime-rich translate, not a certified prime pair; parity uncrossed.
Wall / certificate: WALL-PARITY — UNCROSSED; MC-001 UNSOLVED.
Classification: Boundary.
Normalized output: → Wall WALL-PARITY (uncrossed) ; → Missing Certificate MC-001.
```

## Quarantined cards (source-mismatch / cross-volume)

```text
TREASURE-MNTII-001..015 (units A/B): CROSS-VOLUME context. Zero-density / large values / pair-correlation
  are deferred by the source to a later volume; these are NOT counted in the trusted source-grounded
  treasure map (units A/B are quarantined — see README / books.jsonl).
Old TREASURE-MNTII-030..036 (off-diagonal / Kloosterman): superseded / quarantined; preserved in
  units/_quarantine/MNTII-006-E-legacy-offdiagonal-source-mismatch.md.
Trusted source-grounded Montgomery treasures: C (016-022, Ch 19-20) · D (023-029, Ch 21) · E (030-036, Ch 22 bounded gaps).
```

**Honest classification:** Diagnostic / Boundary (treasure map, **source-grounding-corrected**). Trusted source-grounded = C + D + E (bounded gaps); A/B + legacy off-diagonal E = quarantined (cross-volume / source-mismatch). No RH/GRH progress. No new theorem; **bounded gaps recorded as a KNOWN theorem, not our result, not twin primes, not a parity breakthrough**; Bombieri–Vinogradov = average input; Elliott–Halberstam = conditional. MC-001 & MC-002 & MC-005 unsolved; walls uncrossed.
