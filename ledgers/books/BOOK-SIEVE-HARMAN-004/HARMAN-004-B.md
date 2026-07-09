# HARMAN-004-B — Type-I / Type-II Information and Harman Decomposition

**Registry ID:** HARMAN-004-B
**Status:** Ingested (v0.5)
**Classification:** **Diagnostic / Boundary** (known information types read as diagnostic; not a result)

**Source Coverage:** Glyn Harman, *Prime-Detecting Sieves*, the Type-I / Type-II information split and the Harman decomposition (as recorded in transformed notes). **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-SIEVE-HARMAN-004`. Local PDF outside git.

## Object

نوعا المعلومة الحسابيّة اللذان يستهلكهما الغربال، وتحليلُ Harman الذي يوزّع دالّةَ العدّ إلى قطعٍ حسبَ نوع المعلومة التي تحتاجها.

## Classical role

```text
Type-I  : مجاميعُ خطّيّة  Σ_{d ≤ D} (level of distribution D) لحدودِ الباقي.
Type-II : مجاميعُ ثنائيّةُ الخطّيّة  Σ_m Σ_n a_m b_n  (well-factorable).
```

تحليلُ Harman يجعل معظمَ القطع محتاجًا إلى Type-I فقط، والبقيّةَ محتاجةً إلى Type-II **مستوردةٍ خارجيًّا** (dispersion / Deshouillers–Iwaniec). **معروف، مُستشهَد.**

## Type-I / Type-II diagnostic role

يُشخّص ما يستهلكه الغربال (Type-I) وما يعوزه (Type-II): حاجزُ التكافؤ هو بالضبط الجدارُ حيث Type-I وحدها لا تكشف الأوّليّات، وType-II مطلوبة. تحليلُ Harman = البنيةُ التشخيصيّةُ التي تُظهِر أيَّ القطع Type-I وأيَّها البقيّةُ من Type-II. `TOOL-TYPE-I-II-DIAGNOSTIC-001`.

## Type-I / Type-II information view

```text
Type-I  handleable  : الغربالُ يستهلكها بحرّيّة حتى مستوى التوزيع D.
Type-II residue     : المعلومةُ الشحيحةُ التي تعبر التكافؤ، وهي شهادةٌ خارجيّةٌ لا تُنتَج من البواقي.
```

## PVG support-geometry connection

Type-I = معلومةُ الدعم عند كلّ مستوى؛ Type-II = المعلومةُ العابرة/اللاقطريّة. يتّصل بـ`WALL-PARITY` (Type-II هي ما يعبر التكافؤ) و`WALL-OFF-DIAGONAL`.

## What it can diagnose

- ميزانيّةُ معلومةِ الغربال (ماذا يستهلك، ماذا يعوزه).
- أيُّ بقيّةٍ تحتاج Type-II.
- أين يعضّ حاجزُ التكافؤ.

## What it cannot prove

- **لا Type-II من البواقي** — شهادةٌ خارجيّةٌ ناقصة.
- **لا يكسر التكافؤ بذاته** ولا يبرهن RH/GRH.
- ليس كاشفًا جديدًا؛ لا تحسينَ PNT/AP.

## Related walls

`WALL-PARITY` · `WALL-SIEVE-CEILING` · `WALL-SIEGEL` · `WALL-OFF-DIAGONAL`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-001` (كسرُ parity غيرُ مشروط): **Type-II هي الشهادةُ الخارجيّةُ الناقصةُ التي قد تعبر التكافؤ — مسجَّلةٌ كنقصٍ لا كنتيجة، تبقى غيرَ محلولة.**

## Claim classification

**Diagnostic / Boundary.** الأنواعُ والتحليلُ Known ومُستشهَدة؛ المخرجُ تشخيصُ ميزانيّةِ المعلومة وحدٌّ، لا New Theorem ولا Candidate Mechanism.

## No-Go notes

```text
- Type-I/Type-II information is a diagnostic of what a sieve consumes and what it lacks.
- Type-II is NOT an independent claim here; it is the missing external certificate (linked to MC-001).
- not a parity-breaking certificate by itself; not a prime detector; not a theorem-improvement claim.
- the large sieve is not a separate unit here.
- not RH/GRH progress; not a PNT/AP improvement.
- no crossing WALL-PARITY or WALL-SIEGEL.
- MC-001 stays unsolved.
- no raw copyrighted text; transformed notes only.
```

## Next valid action

candidate v0.5 closure review (HARMAN-004-A/B), then a further Harman unit or another book — on explicit permission. **No HARMAN-004-C, no independent Type-II claim, no large sieve unit, no expansion before review.**

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] Transformed notes only (no raw text, no copied passages, no general summary)
- [x] Type-II linked to MC-001 as missing certificate, not a result · not an independent claim
- [x] No new sieve theorem · no prime detector · no parity-breaking · no PNT/AP improvement · no RH/GRH
- [x] No HARMAN-004-C · large sieve not a separate unit
- [x] No crossing WALL-PARITY / WALL-SIEGEL · MC-001 unsolved
- [x] Six guards PASS after this unit

**Ceiling:** Type-I/Type-II information is a diagnostic of what a sieve consumes and what it lacks — not a parity-breaking certificate by itself, not a prime detector, not a theorem-improvement claim. No RH/GRH progress.
