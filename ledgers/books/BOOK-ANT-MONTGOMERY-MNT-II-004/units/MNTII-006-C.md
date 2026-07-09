# MNTII-006-C — Large Sieve and Bombieri–Vinogradov as On-Average Distribution Diagnostics

**Registry ID:** MNTII-006-C
**Status:** Ingested (v0.6)
**Classification:** **Diagnostic / Boundary** (known large-sieve / Bombieri–Vinogradov machinery read as an on-average diagnostic; not results)

**Source Coverage:** Hugh Montgomery, *Multiplicative Number Theory II: Primes and Sieves*, the large-sieve inequality and the Bombieri–Vinogradov theorem (as recorded in transformed notes). **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

الغربالُ الكبيرُ (متباينةُ المتوسّط/الازدواج) ومبرهنةُ Bombieri–Vinogradov، مقروءةً **كمرصدِ توزيعٍ في المتوسّط** لجبهة `FRONTIER-ANT-PVG-006`. **الكنزُ الذي أُجِّل عمدًا في IK/Harman («large sieve = سياقٌ لا وحدة») يُعدَّن الآن كوحدةٍ تشخيصيّة.**

## Classical role

الغربالُ الكبيرُ متباينةُ متوسّطٍ (duality / bilinear) لمتعدّدات Dirichlet ومجاميع الشخصيّات؛ Bombieri–Vinogradov يعطي توزيعَ الأوّليّات في المتتاليّات **لاشرطيًّا في المتوسّط** حتى مستوى `1/2` («GRH-strength on average»). **معروفةٌ، مُستشهَدة.**

## On-average diagnostic role

تحكّمٌ **عائليٌّ/متوسّطٌ لاشرطيّ، لا فرديّ**: BV يبلغ قوّةَ GRH في المتوسّط على `q`، **لكنّه لا يعطي الحالةَ الفرديّة** (تبقى `MC-005`). وهو أيضًا متباينةُ المتوسّط خلفَ كثافة الأصفار (تربط 006-A/B). `TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001`.

## Family / average view

```text
Large sieve         : a mean-value (duality / bilinear) inequality for Dirichlet polynomials / character sums
Bombieri–Vinogradov : unconditional average AP distribution to level 1/2 — "as if GRH on average"
Dispersion method   : Linnik–Bombieri bilinear / average technique
Reading             : average / family control, NOT individual-modulus GRH
```

## PVG–ANT connection

مرصدُ المتوسّط العائليّ لجبهة 006: يجاورُ أدواتِ IK وأداتَي 006-A/B، ويربطُ عائلاتِ الشخصيّات (`OBS-CHARACTER-001`, `OBS-RESIDUE-FIBER-001`). سلّمُ التكلفة: **residue → spectral = GRH-level** (لا يُعبَر).

## What it can diagnose

- كم يبلغُ توزيعُ AP في المتوسّط لاشرطيًّا (مستوى `1/2`).
- الفجوةُ بين المتوسّط والفرديّ.
- أنّ الغربالَ الكبيرَ هو متباينةُ المتوسّط خلفَ كثافة الأصفار.

## What it cannot prove

- **لا الحالةَ الفرديّة (`MC-005`)** · لا RH/GRH.
- **Elliott–Halberstam** (المستوى `1−ε`) **حدسٌ غيرُ مبرهن** — لا نتيجة، لا شهادة.
- لا تحسينَ كثافة / PNT / AP.

## Related walls

`WALL-SIEGEL` (الأصفارُ الاستثنائيّة الفرديّة) · `WALL-POSITIVITY-WEIL` · `WALL-OFF-DIAGONAL` · `WALL-DENSITY-HYP`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-005` (توزيعُ AP الفرديّ GRH-level) — تبقى غيرَ محلولة. `MC-002` تبقى غيرَ محلولة. (Elliott–Halberstam حدسٌ مفتوحٌ لا شهادةٌ مُنجَزة.)

## Claim classification

**Diagnostic / Boundary.** الغربالُ الكبيرُ وBV معروفان ومُستشهَدان؛ المخرجُ مرصدُ متوسّطٍ وحدٌّ، لا New Theorem ولا Candidate Mechanism. Elliott–Halberstam = Open Problem.

## No-Go notes

```text
- large sieve / Bombieri–Vinogradov give AVERAGE (family) AP distribution, NOT individual-modulus GRH.
- "as if GRH on average" is an unconditional KNOWN theorem — not RH/GRH progress and not the individual case.
- Elliott–Halberstam (level 1−ε) is an UNPROVEN conjecture / open problem — no unconditional certificate.
- not a zero-density / large-values / PNT-AP improvement; not a new theorem.
- no crossing WALL-SIEGEL / WALL-POSITIVITY-WEIL.
- MC-005 stays unsolved; MC-002 stays unsolved.
- no raw copyrighted text; transformed notes only.
```

## Next valid action

candidate v0.6-C closure review (MNTII-006-C), then a further Montgomery unit or another book or freeze — on explicit permission. **No MNTII-006-D, no full book mining, no expansion before review.**

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] Transformed notes only (no raw text, no copied passages, no general summary)
- [x] No RH/GRH progress · average ≠ individual · Elliott–Halberstam kept as an unproven Open Problem
- [x] No crossing WALL-SIEGEL / WALL-POSITIVITY-WEIL · MC-005 & MC-002 unsolved
- [x] Target registered planned → live on honest completion: `TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001`; planned.jsonl empty
- [x] Previously-deferred large-sieve treasure now mined as a diagnostic (IK/Harman kept it as context)
- [x] MNTII-006-D not started · no full book mining
- [x] Six guards PASS after this unit

**Ceiling:** the large sieve and Bombieri–Vinogradov enter as an on-average distribution diagnostic feeding `FRONTIER-ANT-PVG-006` — unconditional average control, NOT individual GRH; Elliott–Halberstam stays an unproven open problem. No RH/GRH progress.
