# Harman — Treasure Map

Book ID: `BOOK-SIEVE-HARMAN-004`. **Book Treasure Retrofit Pass 001** — طبقةٌ فوق الوحدات المُغلَقة HARMAN-004-A/B (v0.5، إغلاقٌ PASS 8/8) لا تمسّها. تحكمها `governance/book-treasure-extraction-protocol.md`. المصدر: `Prime-Detecting Sieves (Harman, Glyn)` (في `Books_others`, PDF خارج git). Harman دخل **طبقةَ دعمٍ تشخيصيّة** لـ`FRONTIER-ANT-PVG-004`، لا نتائجَ. لا نصٌّ خام، لا ادّعاءُ إتقانٍ كامل.

```text
Treasure ID: TREASURE-HARMAN-001
Treasure:    Prime-detecting sieve as information consumption
Source:      HARMAN-004-A — transformed notes only
Type:        sieve-information diagnostic
Why it matters: reframes a prime-detecting sieve as a CONSUMER of arithmetic information (Type-I/II), not a magic prime machine.
ANT role:    decomposes the counting function into pieces the sieve consumes; positive lower bound for primes (short intervals, Piatetski–Shapiro) by importing external Type-II.
PVG translation: sieve weights = PVG support observable; consumed information = which support layers the sieve reaches.
Wall / certificate: WALL-PARITY (linear info alone fails) · WALL-SIEVE-CEILING (unconditional limit) ; MC-001.
Classification: Diagnostic / Boundary.
Normalized output: → Tool TOOL-SIEVE-INFO-CONSUMPTION-001 ; → Frontier FRONTIER-ANT-PVG-004.
```

```text
Treasure ID: TREASURE-HARMAN-002
Treasure:    Sieve does not create missing information
Source:      HARMAN-004-A ("what it cannot prove") — transformed notes only
Type:        no-go boundary
Why it matters: a sieve cannot detect primes without external Type-II information — it consumes information, it does not manufacture it.
ANT role:    no primes from Type-I alone past parity; Type-II must be imported externally.
PVG translation: the sieve reaches only the support layers its input information covers.
Wall / certificate: WALL-PARITY ; MC-001 unsolved.
Classification: Boundary.
Normalized output: → Wall WALL-PARITY ; → Missing Certificate MC-001.
```

```text
Treasure ID: TREASURE-HARMAN-003
Treasure:    Type-I information as structured average input
Source:      HARMAN-004-B — transformed notes only
Type:        information type
Why it matters: Type-I (linear sums over d≤D of remainder terms, "level of distribution") is the information the sieve consumes freely.
ANT role:    Σ_{d≤D} remainder terms; level of distribution D.
PVG translation: support information available at each level.
Wall / certificate: alone insufficient past parity — WALL-PARITY.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-TYPE-I-II-DIAGNOSTIC-001 (Type-I aspect).
```

```text
Treasure ID: TREASURE-HARMAN-004
Treasure:    Type-II information as bilinear / external information input
Source:      HARMAN-004-B — transformed notes only
Type:        information type
Why it matters: Type-II (bilinear sums Σ_m Σ_n a_m b_n, well-factorable) is the scarce EXTERNAL information that crosses parity.
ANT role:    bilinear estimates imported externally (dispersion / Deshouillers–Iwaniec), NOT produced from remainders.
PVG translation: the crossing / off-diagonal information.
Wall / certificate: WALL-PARITY (Type-II is what crosses) · WALL-OFF-DIAGONAL ; MC-001.
Classification: Known / Diagnostic / Boundary.
Normalized output: → Tool TOOL-TYPE-I-II-DIAGNOSTIC-001 (Type-II aspect) ; → Wall WALL-OFF-DIAGONAL.
```

```text
Treasure ID: TREASURE-HARMAN-005
Treasure:    Harman decomposition as information-routing architecture
Source:      HARMAN-004-B — transformed notes only
Type:        architecture / routing tool
Why it matters: Harman's decomposition routes the counting function into pieces by which information type each needs — most need only Type-I, the rest need imported Type-II.
ANT role:    decompose the counting function into Type-I-handleable pieces + a Type-II-requiring remainder.
PVG translation: information-budget routing of the support observable.
Wall / certificate: the remainder's Type-II is the external missing certificate — MC-001.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-TYPE-I-II-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-HARMAN-006
Treasure:    Type-II as missing external certificate tied to MC-001
Source:      HARMAN-004-B / v0.5 closure — transformed notes only
Type:        missing certificate
Why it matters: names what crosses parity — a PROVEN external Type-II estimate — as a missing certificate, not a result.
ANT role:    Type-II is not obtainable from remainders; unconditionally at the needed strength it is missing.
PVG translation: the external crossing certificate the diagnostics identify but do not supply.
Wall / certificate: WALL-PARITY ; MC-001 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-001 (governance/missing-certificates.md).
```

```text
Treasure ID: TREASURE-HARMAN-007
Treasure:    Large sieve as context, not a unit
Source:      HARMAN-004-A/B + v0.5 closure — transformed notes only
Type:        scope / deferred treasure
Why it matters: the large-sieve inequality is ambient context in v0.5, NOT ingested as a separate unit — a deferred treasure, honestly marked.
ANT role:    large sieve = ambient mean-value context around the sieve, not an ingested unit.
PVG translation: (deferred) — a possible future unit.
Wall / certificate: n/a (contextual).
Classification: Diagnostic (deferred).
Normalized output: → deferred (see missed-treasures.md); not a live unit in v0.5.
```

```text
Treasure ID: TREASURE-HARMAN-008
Treasure:    Parity wall as uncrossed boundary
Source:      HARMAN-004-A/B — transformed notes only
Type:        standing wall
Why it matters: the parity barrier is exactly where Type-I alone cannot separate primes from products of two primes; Harman works AROUND it by importing Type-II, never breaking it.
ANT role:    the classical parity obstruction.
PVG translation: the wall the support geometry observes but does not cross.
Wall / certificate: WALL-PARITY — UNCROSSED ; MC-001.
Classification: Boundary.
Normalized output: → Wall WALL-PARITY (uncrossed) ; → Missing Certificate MC-001.
```

```text
Treasure ID: TREASURE-HARMAN-009
Treasure:    Sieve diagnostics ≠ prime detector
Source:      HARMAN-004-A (No-Go) — transformed notes only
Type:        no-go boundary
Why it matters: reading the sieve as an information diagnostic is NOT a new prime detector.
ANT role:    a diagnostic of consumption, not a detection theorem.
PVG translation: measurement, not mechanism.
Wall / certificate: WALL-SIEVE-CEILING ; MC-001.
Classification: Boundary.
Normalized output: → Wall WALL-SIEVE-CEILING.
```

```text
Treasure ID: TREASURE-HARMAN-010
Treasure:    Sieve diagnostics ≠ parity-breaking
Source:      HARMAN-004-A/B (No-Go) — transformed notes only
Type:        no-go boundary
Why it matters: diagnosing WHERE parity bites is NOT breaking parity; only externally-proven Type-II crosses it.
ANT role:    no unconditional parity break from the diagnostics.
PVG translation: naming the wall ≠ crossing it.
Wall / certificate: WALL-PARITY (uncrossed) ; MC-001 unsolved.
Classification: Boundary.
Normalized output: → Wall WALL-PARITY (uncrossed) ; → Missing Certificate MC-001.
```

```text
Treasure ID: TREASURE-HARMAN-011
Treasure:    WALL-SIEGEL remains uncrossed
Source:      HARMAN-004-A/B (walls in play) — transformed notes only
Type:        standing wall
Why it matters: exceptional (Siegel) zeros remain untouched by the sieve-information diagnostics.
ANT role:    the exceptional-zero obstruction — standing, orthogonal to the sieve layer.
PVG translation: an uncrossed fiber anomaly.
Wall / certificate: WALL-SIEGEL — UNCROSSED.
Classification: Boundary.
Normalized output: → Wall WALL-SIEGEL (uncrossed).
```

```text
Treasure ID: TREASURE-HARMAN-012
Treasure:    FRONTIER-ANT-PVG-004 supported-diagnostic-layer only
Source:      v0.5 closure (AUDIT-CM-V05-CLOSURE-001) — transformed notes only
Type:        frontier status
Why it matters: Harman v0.5 deepens frontier 004 as a SUPPORTED diagnostic layer — support, not a result and not a crossing.
ANT role:    the sieve-information layer feeds FRONTIER-ANT-PVG-004.
PVG translation: diagnostic support of the sieve-information front.
Wall / certificate: MC-001 standing; WALL-PARITY uncrossed.
Classification: Diagnostic.
Normalized output: → Frontier FRONTIER-ANT-PVG-004 (supported-diagnostic-layer).
```

**Honest classification:** Diagnostic / Boundary (treasure map, retrofit layer). No RH/GRH progress. No new sieve theorem, no prime-detector claim, no parity-breaking. MC-001 unsolved; WALL-PARITY & WALL-SIEGEL uncrossed.
