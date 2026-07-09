# HARMAN-004-A — Prime-Detecting Sieve as Information Consumption

**Registry ID:** HARMAN-004-A
**Status:** Ingested (v0.5)
**Classification:** **Diagnostic / Boundary** (known sieve method read as information diagnostic; not a result)

**Source Coverage:** Glyn Harman, *Prime-Detecting Sieves*, the prime-detecting method as a decomposition consuming Type-I / Type-II information (as recorded in transformed notes). **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-SIEVE-HARMAN-004`. Local PDF outside git.

## Object

الغربالُ الكاشفُ للأوّليّات (طريقةُ Harman): تحليلُ دالّةِ العدّ إلى قطعٍ يستهلكها الغربالُ — **قراءةً كاستهلاكِ معلومةٍ حسابيّة**، لا كآلةٍ سحريّة.

## Classical role

يُنتج حدًّا سفليًّا موجبًا لأوّليّاتٍ في مجموعة (أوّليّاتٌ في فتراتٍ قصيرة، Piatetski–Shapiro) باستعمال معلومةِ Type-I ومقدارٍ من Type-II، عاملًا **حول** حاجز التكافؤ باستيراد تقديراتٍ ثنائيّةٍ (Type-II) خارجيّة. **طريقةٌ معروفةٌ، مُستشهَدة.**

## Sieve-information diagnostic role

يقرأ الغربالَ كمستهلِكٍ لمعلومةِ Type-I (خطّيّة/ناعمة) وType-II (ثنائيّة الخطّيّة)؛ يُشخِّص حاجزَ التكافؤ (`WALL-PARITY`) كنقطةِ فشلِ المعلومة الخطّيّة وحدها، وسقفَ الغربال (`WALL-SIEVE-CEILING`) كالحدّ اللاشرطيّ. `TOOL-SIEVE-INFO-CONSUMPTION-001`.

## Type-I / Type-II information view

```text
Type-I  : مجاميعُ على d ≤ D لحدودِ الباقي (مستوى التوزيع) — يستهلكها الغربالُ بحرّيّة.
Type-II : مجاميعُ ثنائيّةُ الخطّيّة Σ_m Σ_n a_m b_n — المعلومةُ التي تعبر التكافؤ، وهي الشحيحةُ الخارجيّة.
```

## PVG support-geometry connection

أوزانُ الغربال = مرصدُ الدعم PVG؛ المعلومةُ المُستهلَكة = أيُّ طبقاتِ دعمٍ يبلغها الغربال. يتّصل بـ`WALL-PARITY` و`WALL-SIEVE-CEILING` و«الجدار السادس فارغ» (لا غربالٌ غيرُ مشروطٍ يبلغ RH؛ EH وحده).

## What it can diagnose

- أيُّ نوعِ معلومةٍ يستهلكه الغربال.
- أين يعضّ حاجزُ التكافؤ.
- سقفُ الغربال اللاشرطيّ.
- أنّ Type-II هي الشهادةُ الخارجيّةُ الناقصة.

## What it cannot prove

- **لا يبرهن RH/GRH** ولا يكسر التكافؤ.
- لا يكشف أوّليّاتٍ دون معلومةِ Type-II خارجيّة (حاجزُ التكافؤ).
- ليس كاشفًا جديدًا؛ لا يحلّ `MC-001`.

## Related walls

`WALL-PARITY` · `WALL-SIEVE-CEILING` · `WALL-SIEGEL`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-001` (كسرُ parity غيرُ مشروط) · وشهادةُ جبهة 004: **معلومةُ Type-II خارجيّةٌ مبرهَنة** (لا من البواقي) تبقى ناقصة.

## Claim classification

**Diagnostic / Boundary.** الطريقةُ Known ومُستشهَدة؛ المخرجُ تشخيصُ استهلاكِ المعلومة وحدٌّ، لا New Theorem ولا Candidate Mechanism.

## No-Go notes

```text
- a prime-detecting sieve is studied as an information-consumption diagnostic.
- not a new prime detector; not a parity-breaking method; not a theorem-improvement engine.
- Type-II information is the missing external certificate, not produced from remainders.
- not RH/GRH progress; not a PNT/AP improvement.
- no crossing WALL-PARITY or WALL-SIEGEL.
- MC-001 stays unsolved.
- no raw copyrighted text; transformed notes only.
```

## Next valid action

`HARMAN-004-B` — Type-I / Type-II information & Harman decomposition (`TOOL-TYPE-I-II-DIAGNOSTIC-001`, still planned) — on explicit permission. **No independent Type-II expansion, no large sieve unit, no HARMAN-004-C yet.**

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] Transformed notes only (no raw text, no copied passages, no general summary)
- [x] No RH/GRH progress · no new sieve theorem · no prime detector claim · no parity-breaking claim · no PNT/AP improvement
- [x] Type-II not expanded independently · no large sieve unit · no HARMAN-004-B started
- [x] No crossing WALL-PARITY / WALL-SIEGEL · MC-001 unsolved
- [x] Six guards PASS after this unit

**Ceiling:** a prime-detecting sieve is an information-consumption diagnostic, not a new prime detector, not a parity-breaking method, and not a theorem-improvement engine. No RH/GRH progress.
