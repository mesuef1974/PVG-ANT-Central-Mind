# Iwaniec–Kowalski — Treasure Map

Book ID: `BOOK-ANT-IWANIEC-KOWALSKI-003`. **Book Treasure Retrofit Pass 001** — طبقةٌ فوق الوحدات المُغلَقة IK-006-A/B (v0.4، إغلاقٌ PASS 8/8) لا تمسّها. تحكمها `governance/book-treasure-extraction-protocol.md`. المصدر: `Iwaniec H., Kowalski E. Analytic Number Theory 2004` (في `Books_others`, PDF خارج git). IK دخل **طبقةَ دعمِ جبهةٍ تشخيصيّة** لـ`FRONTIER-ANT-PVG-006`، لا نتائجَ. لا نصٌّ خام، لا ادّعاءُ إتقانٍ كامل.

```text
Treasure ID: TREASURE-IK-001
Treasure:    Zero-density estimates as diagnostic support
Source:      IK-006-A (zero-density N(σ,T)) — transformed notes only
Type:        frontier diagnostic tool
Why it matters: bounds how many zeros can lie off the critical line, giving "as if RH" results on average without proving RH.
ANT role:    N(σ,T) = #{ρ=β+iγ : β≥σ, |γ|≤T}, bounded above on 1/2<σ<1; unconditional average results (short-interval primes, Bombieri–Vinogradov flavor).
PVG translation: off-diagonal error control; zero-density = an unconditional measure of "how far from RH".
Wall / certificate: WALL-DENSITY-HYP (floor 17/30=1−1/A) · WALL-ZERO-FREE (contextual, uncrossed) ; MC-002 (an actual improved estimate) missing.
Classification: Diagnostic / Boundary.
Normalized output: → Tool TOOL-ZERO-DENSITY-DIAGNOSTIC-001 ; → Wall WALL-DENSITY-HYP ; → Frontier FRONTIER-ANT-PVG-006.
```

```text
Treasure ID: TREASURE-IK-002
Treasure:    Large values as obstruction / pressure indicators
Source:      IK-006-B (large-value estimates for Dirichlet polynomials) — transformed notes only
Type:        frontier diagnostic tool
Why it matters: the count of well-spaced points where a Dirichlet polynomial is large is the "pressure" that bounds N(σ,T) — more large values = more room for off-line zeros.
ANT role:    large-value estimates for Σ a_n n^{-it} feed zero-density; R = #{well-spaced t : |Σ| large} bounded above.
PVG translation: large values = off-diagonal pressure obstructing RH-like behavior; bounding them bounds the zeros.
Wall / certificate: WALL-OFF-DIAGONAL · WALL-DENSITY-HYP (uncrossed).
Classification: Diagnostic / Boundary.
Normalized output: → Tool TOOL-LARGE-VALUE-DIAGNOSTIC-001 ; → Wall WALL-OFF-DIAGONAL.
```

```text
Treasure ID: TREASURE-IK-003
Treasure:    Mean values as family-level control
Source:      IK-006-B (second-moment / mean-value theorems) — transformed notes only
Type:        diagnostic support
Why it matters: the second moment ∫|Σ|² controls a Dirichlet polynomial ON AVERAGE over a family — family control, not pointwise control.
ANT role:    mean-value (second-moment) theorems bound the number of large values → feed N(σ,T); large sieve is ambient context, not a separate unit.
PVG translation: family-average control of the off-diagonal observable.
Wall / certificate: average control ≠ pointwise control (feeds TREASURE-IK-008); WALL-DENSITY-HYP.
Classification: Diagnostic / Boundary.
Normalized output: → Tool TOOL-LARGE-VALUE-DIAGNOSTIC-001 (mean-value aspect).
```

```text
Treasure ID: TREASURE-IK-004
Treasure:    L-functions as family-analytic objects
Source:      IK-006-A/B (N(σ,T) for ζ and L(s,χ)) — transformed notes only
Type:        object / family reading
Why it matters: the zero-density and large-value machinery reads ζ and L(s,χ) as a FAMILY (analytic theory of families), not one isolated function.
ANT role:    N(σ,T) applies uniformly across the L(s,χ) family; family estimates drive average AP distribution.
PVG translation: a family of residue-fiber generating objects, measured together.
Wall / certificate: family zero-control at GRH strength — MC-005 (unsolved); WALL-POSITIVITY-WEIL (uncrossed).
Classification: Diagnostic / Boundary.
Normalized output: → Frontier FRONTIER-ANT-PVG-006 ; consumes TOOL-ZERO-DENSITY-DIAGNOSTIC-001, TOOL-LARGE-VALUE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-IK-005
Treasure:    Character families as distributional test beds
Source:      IK-006-A (Bombieri–Vinogradov-flavor average) — transformed notes only
Type:        observable family
Why it matters: Dirichlet characters mod q form a family whose AVERAGE behaves "as if GRH" (Bombieri–Vinogradov) — the test bed for AP distribution on average.
ANT role:    averaging over χ mod q (and over q) yields unconditional average AP distribution; the individual q stays conditional.
PVG translation: residue-fiber families as a distributional test bed.
Wall / certificate: individual AP beyond Siegel–Walfisz needs GRH — MC-005; WALL-SIEGEL (uncrossed).
Classification: Diagnostic / Boundary.
Normalized output: → Observable OBS-CHARACTER-001, OBS-RESIDUE-FIBER-001 ; → Missing Certificate MC-005.
```

```text
Treasure ID: TREASURE-IK-006
Treasure:    Zero-density does not solve pointwise distribution alone
Source:      IK-006-A ("what it cannot prove") — transformed notes only
Type:        no-go boundary
Why it matters: a zero-density bound is a conditional/average substitute for RH in error terms — it does NOT deliver pointwise prime distribution.
ANT role:    N(σ,T) bounds average error; pointwise ψ(x)−x at RH strength is not implied.
PVG translation: off-diagonal average ≠ diagonal/pointwise truth.
Wall / certificate: WALL-ZERO-FREE (contextual, uncrossed); MC-002 unsolved.
Classification: Boundary.
Normalized output: → Missing Certificate MC-002 ; → Wall WALL-ZERO-FREE (contextual).
```

```text
Treasure ID: TREASURE-IK-007
Treasure:    Large-value control does not imply GRH
Source:      IK-006-B ("what it cannot prove") — transformed notes only
Type:        no-go boundary
Why it matters: bounding large values / mean values improves zero-density diagnostics but is NOT GRH and NOT a large-values theorem.
ANT role:    large-value bounds are conditional/average support, not zero-location control.
PVG translation: pressure bounds do not locate zeros.
Wall / certificate: WALL-POSITIVITY-WEIL · WALL-SIEGEL (uncrossed); MC-002 / MC-005 unsolved.
Classification: Boundary.
Normalized output: → Wall WALL-POSITIVITY-WEIL, WALL-SIEGEL ; → Missing Certificate MC-002, MC-005.
```

```text
Treasure ID: TREASURE-IK-008
Treasure:    Family average control ≠ individual AP certificate
Source:      IK-006-A/B (average vs individual) — transformed notes only
Type:        no-go boundary
Why it matters: Bombieri–Vinogradov-type average control over a family does NOT certify the individual arithmetic progression at GRH strength.
ANT role:    average-over-q distribution ≠ individual-q GRH-level distribution.
PVG translation: family-average observable ≠ individual residue-fiber certificate.
Wall / certificate: WALL-SIEGEL (uncrossed); MC-005 unsolved.
Classification: Boundary.
Normalized output: → Missing Certificate MC-005 ; → Wall WALL-SIEGEL.
```

```text
Treasure ID: TREASURE-IK-009
Treasure:    MC-002 remains unsolved
Source:      IK-006-A/B — transformed notes only
Type:        missing certificate (standing)
Why it matters: names what IK does NOT deliver — a strong ψ(x)−x error at RH strength.
ANT role:    the RH-level error certificate for the primes.
PVG translation: diagonal/pointwise prime-error certificate.
Wall / certificate: WALL-ZERO-FREE; MC-002 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-002 (governance/missing-certificates.md).
```

```text
Treasure ID: TREASURE-IK-010
Treasure:    MC-005 remains unsolved
Source:      IK-006-B — transformed notes only
Type:        missing certificate (standing)
Why it matters: names what IK does NOT deliver — AP distribution beyond Siegel–Walfisz at GRH strength for the individual modulus.
ANT role:    the GRH-level AP distribution certificate.
PVG translation: individual residue-fiber distribution certificate.
Wall / certificate: WALL-SIEGEL + WALL-POSITIVITY-WEIL; MC-005 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-005 (governance/missing-certificates.md).
```

```text
Treasure ID: TREASURE-IK-011
Treasure:    WALL-SIEGEL remains uncrossed
Source:      IK-006-A/B (walls in play) — transformed notes only
Type:        standing wall
Why it matters: exceptional (Siegel) zeros keep AP distribution ineffective/biased; IK's diagnostics do not remove them.
ANT role:    the exceptional-zero obstruction to effective AP distribution.
PVG translation: a fiber anomaly the diagnostics observe but do not cross.
Wall / certificate: WALL-SIEGEL — UNCROSSED.
Classification: Boundary.
Normalized output: → Wall WALL-SIEGEL (uncrossed).
```

```text
Treasure ID: TREASURE-IK-012
Treasure:    WALL-POSITIVITY-WEIL remains uncrossed
Source:      IK-006-A/B (walls in play) — transformed notes only
Type:        standing wall
Why it matters: zero location / Weil positivity is untouched by zero-density and large-value diagnostics.
ANT role:    the positivity/zero-location obstruction (explicit-formula wall).
PVG translation: the residue→spectral crossing the diagnostics do not make.
Wall / certificate: WALL-POSITIVITY-WEIL — UNCROSSED.
Classification: Boundary.
Normalized output: → Wall WALL-POSITIVITY-WEIL (uncrossed).
```

**Honest classification:** Diagnostic / Boundary (treasure map, retrofit layer). No RH/GRH progress. No zero-density improvement, no large-values theorem. MC-002 & MC-005 unsolved; WALL-SIEGEL & WALL-POSITIVITY-WEIL uncrossed.
