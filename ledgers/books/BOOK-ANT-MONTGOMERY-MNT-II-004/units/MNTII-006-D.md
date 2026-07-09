# MNTII-006-D — Selberg / Combinatorial Sieve and the Fundamental Lemma as a Bounded-Reach Diagnostic

**Registry ID:** MNTII-006-D
**Status:** Ingested (v0.6)
**Classification:** **Diagnostic / Boundary** (known classical sieve machinery read as a bounded-reach diagnostic; not results)

**Source Coverage:** Hugh Montgomery, *Multiplicative Number Theory II: Primes and Sieves*, the classical upper/lower-bound sieve machinery — the Selberg Λ²-sieve, the Brun combinatorial sieve, the fundamental lemma, and the sieve dimension κ (as recorded in transformed notes). **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

الغربالُ الكلاسيكيُّ ذو الحدّين (Selberg Λ²، Brun التوافقيّ)، اللِّمّةُ الأساسيّة، وبُعدُ الغربال `κ`، مقروءةً **كمرصدِ مدًى محدود** لجبهة `FRONTIER-ANT-PVG-004` — ركنُ «الغرابيل» في «Primes and Sieves». **الكنزُ المؤجَّلُ (combinatorial / Selberg sieve chapters) يُعدَّن الآن.**

## Classical role

Selberg يُحسّن أوزانَ `Λ²` لحدٍّ علويّ؛ Brun يبتر التضمين–الاستبعاد لحدَّين علويٍّ وسفليّ؛ اللِّمّةُ الأساسيّة تعطي الغربالَ الصغيرَ حتى مستوى توزيعٍ `D` ببُعدٍ `κ`. **معروفةٌ، مُستشهَدة.**

## Bounded-reach diagnostic role

الغرابيلُ **تَحُدُّ (علويًّا/سفليًّا) وتعدُّ الأشباهَ الأوّليّة**، لا الأوّليّاتِ نفسَها: حاجزُ التكافؤ (`WALL-PARITY`) يمنع كشفَ الأوّليّات دون معلومةِ Type-II خارجيّة (Harman)، وسقفُ الغربال (`WALL-SIEVE-CEILING`) هو الحدُّ اللاشرطيّ. `TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001`.

## Sieve view

```text
Selberg Λ² sieve   : optimized upper bound
Brun combinatorial : truncated inclusion–exclusion → upper AND lower bounds
Fundamental lemma  : small sieve to level of distribution D, dimension κ
Reading            : bounds + almost-primes, NOT primes (parity); κ is the diagnostic parameter
```

## PVG–ANT connection

مرصدُ الغربلة لجبهة 004 (sieve information through support geometry): يكمّل تحليلَ Harman (`TOOL-SIEVE-INFO-CONSUMPTION-001`, `TOOL-TYPE-I-II-DIAGNOSTIC-001`) — Type-II هي الشهادةُ الخارجيّةُ التي تعبر التكافؤ، لا الغربالُ وحدَه.

## What it can diagnose

- إلى أين يبلغُ الغربالُ (أشباهٌ أوّليّة، حدود).
- أين يعضّ حاجزُ التكافؤ.
- بُعدُ الغربال `κ` ومستوى التوزيع `D`.

## What it cannot prove

- **لا يكشفُ الأوّليّاتِ لاشرطيًّا** (parity) · لا يكسرُ التكافؤ · لا يبرهن RH/GRH.
- Brun–Titchmarsh **حدٌّ علويّ لا مقارِبٌ** (لا حدَّ رئيسيّ).
- لا يحلّ `MC-001`.

## Related walls

`WALL-PARITY` · `WALL-SIEVE-CEILING` · `WALL-OFF-DIAGONAL`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-001` (كسرُ parity غيرُ مشروط) — تبقى غيرَ محلولة؛ **Type-II هي الشهادةُ الخارجيّةُ الناقصة** (مربوطةٌ بـMC-001، لا تُنتَج من الغربال).

## Claim classification

**Diagnostic / Boundary.** الغرابيلُ الكلاسيكيّةُ معروفةٌ ومُستشهَدة؛ المخرجُ مرصدُ مدًى وحدٌّ، لا New Theorem ولا Candidate Mechanism ولا prime detector.

## No-Go notes

```text
- classical sieves give upper/lower BOUNDS and count almost-primes — NOT primes, NOT an asymptotic.
- the parity barrier blocks unconditional prime detection; Type-II is the missing external certificate (MC-001).
- Brun–Titchmarsh is an upper bound, not a main-term asymptotic.
- not a sieve theorem improvement; not a prime detector; not a parity break; not RH/GRH progress.
- no crossing WALL-PARITY / WALL-SIEVE-CEILING.
- MC-001 stays unsolved.
- no raw copyrighted text; transformed notes only.
```

## Next valid action

candidate v0.6-D closure review (MNTII-006-D), then a further Montgomery unit or another book or freeze — on explicit permission. **No MNTII-006-E, no full book mining, no expansion before review.**

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] Transformed notes only (no raw text, no copied passages, no general summary)
- [x] No RH/GRH progress · no prime detector · no parity break · no sieve-theorem improvement · no new theorem
- [x] Almost-primes / bounds only; Brun–Titchmarsh kept as an upper bound not an asymptotic
- [x] No crossing WALL-PARITY / WALL-SIEVE-CEILING · MC-001 unsolved · Type-II = missing external certificate
- [x] Target registered planned → live on honest completion: `TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001`; planned.jsonl empty
- [x] Deferred combinatorial/Selberg sieve treasure now mined; anchors FRONTIER-ANT-PVG-004; complements Harman
- [x] MNTII-006-E not started · no full book mining
- [x] Six guards PASS after this unit

**Ceiling:** the classical Selberg / combinatorial sieve enters as a bounded-reach diagnostic feeding `FRONTIER-ANT-PVG-004` — bounds and almost-primes, not primes; the parity barrier is uncrossed and Type-II stays the missing external certificate (MC-001). No RH/GRH progress.
