# MNTII-006-E — Exponential and Kloosterman Sums as an Off-Diagonal Cancellation Diagnostic

**Registry ID:** MNTII-006-E
**Status:** Ingested (v0.6)
**Classification:** **Diagnostic / Boundary** (known exponential-sum / Kloosterman machinery read as a cancellation diagnostic; not results)

**Source Coverage:** Hugh Montgomery, *Multiplicative Number Theory II: Primes and Sieves*, exponential sums (Weyl / van der Corput) and Kloosterman sums with the Weil bound (as recorded in transformed notes). **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

المجاميعُ الأُسّيّة (Weyl / van der Corput) ومجاميعُ Kloosterman مع حدِّ Weil، مقروءةً **كمرصدِ إلغاءٍ لاقطريّ** — المصدرِ التحليليِّ للمعلومة الثنائيّة (Type-II) التي تُغذّي الغربالَ الكبيرَ وطريقةَ التشتّت. الكنزُ المؤجَّل «exponential / Kloosterman sums» يُعدَّن الآن.

## Classical role

Weyl / van der Corput يحدّان المجاميعَ الأُسّيّةَ بالإلغاء؛ حدُّ Weil يعطي **إلغاءَ الجذر التربيعيّ** لمجاميع Kloosterman: `|Kl(a,b;p)| ≤ 2√p`. **معروفةٌ، مُستشهَدة.** هذا الإلغاءُ هو ما يُشغّل التقديراتِ الثنائيّةَ (Type-II) وطريقةَ التشتّت (BV، 006-C).

## Off-diagonal cancellation diagnostic role

مرصدُ الإلغاء على المحور اللاقطريّ (`WALL-OFF-DIAGONAL`): يقيسُ كم من الإلغاء متاح، وهو **مصدرُ Type-II** الذي يعبر التكافؤ (Harman، 006-D). `TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001`.

## Cancellation view

```text
Exponential sums   : Weyl / van der Corput cancellation
Kloosterman sums   : Weil bound |Kl| ≤ 2√p (square-root cancellation)
Sums of Kloosterman: Deshouillers–Iwaniec (uses automorphic-form spectral theory) — cited KNOWN external
                     input; does NOT reopen the frozen spectral front FRONTIER-ANT-PVG-007
Reading            : cancellation feeds bilinear / Type-II; NOT prime detection
```

## PVG–ANT connection

مرصدُ الإلغاء اللاقطريّ لجبهة الغربلة `FRONTIER-ANT-PVG-004`: يُغذّي Type-II (`TOOL-TYPE-I-II-DIAGNOSTIC-001`, 006-D) وطريقةَ التشتّت خلفَ الغربال الكبير (006-C). جسرٌ إلى جبهة 006 عبر متباينات المتوسّط.

## What it can diagnose

- كم من الإلغاء اللاقطريّ متاحٌ (حدُّ Weil).
- أيَّ تقديراتٍ ثنائيّةً (Type-II) يُغذّي.
- الجسرَ إلى الغربال الكبير / التشتّت.

## What it cannot prove

- **الإلغاءُ ليس كشفًا للأوّليّات** · التكافؤُ ما زال يمنع (`WALL-PARITY`).
- لا يبرهن RH/GRH · لا يُعيدُ فتحَ الجبهة الطيفيّة المجمَّدة (`FRONTIER-ANT-PVG-007`).
- لا يحلّ `MC-001`.

## Related walls

`WALL-OFF-DIAGONAL` · `WALL-PARITY`. **لا يُعبَر أيٌّ منها.** الجبهةُ الطيفيّةُ `FRONTIER-ANT-PVG-007` تبقى **مجمَّدة** (لا تُعاد).

## Related missing certificates

`MC-001` (كسرُ parity غيرُ مشروط) — تبقى غيرَ محلولة؛ **Type-II هي الشهادةُ الخارجيّةُ الناقصة**، والإلغاءُ يُغذّيها لكنّه لا يكسر التكافؤ وحدَه.

## Claim classification

**Diagnostic / Boundary.** حدُّ Weil ومجاميعُ Kloosterman معروفةٌ ومُستشهَدة؛ المخرجُ مرصدُ إلغاءٍ وحدٌّ، لا New Theorem ولا Candidate Mechanism.

## No-Go notes

```text
- exponential / Kloosterman cancellation is a diagnostic of off-diagonal cancellation, NOT prime detection.
- cancellation feeds bilinear / Type-II information; it does not break parity by itself (MC-001).
- Deshouillers–Iwaniec spectral bounds are cited as a KNOWN external input; the spectral front
  FRONTIER-ANT-PVG-007 stays FROZEN and is NOT reopened.
- not an exponential-sum / sieve theorem improvement; not a prime detector; not RH/GRH progress.
- no crossing WALL-PARITY / WALL-OFF-DIAGONAL.
- MC-001 stays unsolved.
- no raw copyrighted text; transformed notes only.
```

## Next valid action

candidate v0.6-E closure review (MNTII-006-E), then a further Montgomery unit or another book or freeze — on explicit permission. **No MNTII-006-F, no full book mining, no expansion before review.**

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] Transformed notes only (no raw text, no copied passages, no general summary)
- [x] No RH/GRH progress · no prime detector · no exponential-sum/sieve theorem · no new theorem
- [x] Cancellation feeds Type-II but does not break parity; Weil bound cited as a known result
- [x] Deshouillers–Iwaniec cited as external input; FRONTIER-ANT-PVG-007 stays frozen (not reopened)
- [x] No crossing WALL-PARITY / WALL-OFF-DIAGONAL · MC-001 unsolved
- [x] Target registered planned → live on honest completion: `TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001`; planned.jsonl empty
- [x] MNTII-006-F not started · no full book mining
- [x] Six guards PASS after this unit

**Ceiling:** exponential and Kloosterman sums enter as an off-diagonal cancellation diagnostic feeding the bilinear / Type-II information behind the large sieve — cancellation, not prime detection; the parity barrier is uncrossed and the spectral front FRONTIER-ANT-PVG-007 stays frozen. No RH/GRH progress.
