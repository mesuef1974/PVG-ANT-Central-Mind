# Montgomery MNT-II — Integration Links

Book ID: `BOOK-ANT-MONTGOMERY-MNT-II-004`. **v0.6 — source-grounding-corrected (Correction 006).** طبقةُ الدمج: الكنوزُ المؤصَّلةُ على المصدر ← المهاراتُ والجبهاتُ الحيّة. **المسارُ الموثوق:** C (Ch 19-20 large sieve/BV) · D (Ch 21 sieves) · E (Ch 22 bounded gaps) · F (Ch 17 prime sums / Type I-II) · G (Ch 16 Van der Corput support) — الخمسةُ مُغلَقةٌ مُراجَعة — + H (Ch 18 additive / circle method، intake بانتظار مراجعة الإغلاق). **محجور (cross-volume / source-mismatch):** A · B · legacy off-diagonal E.

## Trusted source-grounded clusters → skills

```text
Large sieve / BV (C: 016-022)                → SKILL-MATH-ANT-001, SKILL-MATH-SIEVE-001
Classical sieve (D: 023-029)                 → SKILL-MATH-SIEVE-001, SKILL-MATH-ANT-001
Bounded gaps / GPY / Maynard (E: 030-036)    → SKILL-MATH-SIEVE-001, SKILL-MATH-ANT-001, SKILL-GOV-CERT-001
Prime sums / Type I-II (F: 037-043)          → SKILL-MATH-ANT-001, SKILL-MATH-SIEVE-001
VdC cancellation support (G: 044-051)         → SKILL-MATH-ANT-001
Additive / circle method (H: 052-060, intake) → SKILL-MATH-ANT-001, SKILL-MATH-SIEVE-001
```

## Quarantined clusters (NOT trusted; source-mismatch)

```text
A (001-008), B (009-015)  : zero-density / large values / pair-correlation — deferred by the source to a later volume.
legacy off-diagonal E     : exponential / Kloosterman — units/_quarantine/.
```

## Direct frontier anchor (sieve frontier)

```text
FRONTIER-ANT-PVG-004  Sieve information through PVG support geometry
    ← C large sieve (016) · D Selberg/Brun (023-026) · E GPY/Maynard weights + admissible tuples (030-032, 036)
    The trusted Montgomery path is the sieves-and-gaps pillar of the source (Ch 19-22).

FRONTIER-ANT-PVG-006  (distribution input only)
    ← 033/034 level of distribution / BV as the external average-distribution input to the bounded-gaps sieve.
    Distribution enters only as EXTERNAL input; zero-density / large values themselves are deferred (A/B quarantined).
```

## Cross-unit links (trusted path)

```text
C → E : level of distribution / Bombieri–Vinogradov feeds the GPY / Maynard sieve (033, 034).
D → E : sieve weights / parity ceiling — bounded gaps live under the same parity / sieve-ceiling walls (031, 036).
E → Harman / IK sieve context : TOOL-SIEVE-INFO-CONSUMPTION-001, TOOL-TYPE-I-II-DIAGNOSTIC-001 (Type-II / level input).
F backward: Ch 16 (Van der Corput support — mined and CLOSED as MNTII-006-G, v0.6-g-closure PASS) · C (BV average distribution, 038↔017-range) ·
            D (sieve ceilings need Type II input, 040) · E (bounded gaps consume distribution/sieve inputs) ·
            Harman overlay (Type I/II consumption: TOOL-TYPE-I-II-DIAGNOSTIC-001).
F forward : Ch 18 additive prime number theory (now mined as MNTII-006-H intake).
F note    : the packet's optional additive-interface frontier link was dropped — the existing
            FRONTIER-ANT-PVG-003 is a different topic (Mobius/Liouville); reported, not invented.
G backward: none required (Ch 16 is foundational support).
G lateral : Appendix E (trigonometric/harmonic) and Appendix G (norm/bilinear) as support-only.
G forward : F (Ch 17 prime sums / Type I-II consumes the cancellation language) ·
            H (Ch 18 additive applications — now mined as MNTII-006-H intake).
H backward: G (Ch 16 cancellation support) · F (Ch 17 prime sums / Type I-II) ·
            C (Ch 19-20 BV average-distribution background) · D/E (sieve-side contrast).
H forward : Montgomery post-H coverage/overlay audit after the H closure — NOT unit I.
H caution : Ch 18 must NOT be used to revive A/B or legacy-E, and must NOT be read as
            claiming binary Goldbach, twin primes, RH/GRH, or PNT/AP movement.
G caution : legacy-E stays QUARANTINED — Ch 16 must NOT be reinterpreted as legacy-E coverage
            or a Kloosterman/Weil revival.
No RH/GRH progress links.
```

## Certificate-ledger anchors (all unsolved)

```text
MC-001  Unconditional parity break     ← 031, 036   (UNSOLVED; WALL-PARITY; weights are not prime detectors)
MC-005  AP distribution / GRH-level      ← 033, 034   (UNSOLVED; BV is average, not individual GRH)
MC-002  ψ(x)−x error / RH                : not touched; not marked solved.
```

## Open problem (not a certificate, not a result)

```text
Elliott–Halberstam (level 1−ε)  ← 035   UNPROVEN conjecture; EH-dependent bounded-gap sharpenings are conditional only.
```

## Walls in play (all uncrossed)

```text
WALL-PARITY · WALL-SIEVE-CEILING · WALL-OFF-DIAGONAL · WALL-DENSITY-HYP   the sieve / gaps walls (frontier 004)
(the frontier-006 walls WALL-ZERO-FREE / WALL-SIEGEL / WALL-POSITIVITY-WEIL belong to the quarantined A/B context)
```

## Scope honesty (v0.6, source-grounding-corrected)

```text
Trusted source-grounded units: C (Ch 19-20), D (Ch 21), E (Ch 22 bounded gaps, v0.6-e-closure PASS),
F (Ch 17 prime sums / Type I-II, v0.6-f-closure PASS) — all four closure-reviewed — plus
G (Ch 16 Van der Corput support, v0.6-g-closure PASS) — all five closure-reviewed — plus
H (Ch 18 additive / circle method, validated_intake, NOT closed, pending v0.6-H Closure Review;
from an explicit ChatGPT Treasure Packet; binary Goldbach stays OPEN, never claimed).
Quarantined (source-mismatch): A, B (cross-volume: zero-density / large values / pair-correlation deferred to a
later volume) and the legacy off-diagonal E (Kloosterman — NOT revived by the Ch-16 unit). No MNTII-006-I without an explicit Treasure Packet and permission; after the H closure the next step is a post-H coverage/overlay audit. No new book. Bounded gaps is a KNOWN theorem, not our result, not twin primes, not a parity breakthrough; BV = average
input; EH = conditional. No RH/GRH progress.
```

**Honest classification:** Diagnostic / Boundary (integration links, source-grounding-corrected). No RH/GRH progress.
