# MNTII-006-B — Distributional Limits and Barriers as Frontier-Support Diagnostics

**Registry ID:** MNTII-006-B
**Status:** Ingested (v0.6)
**Classification:** **Diagnostic / Boundary** (the LIMITS of known MNT-II machinery read as diagnostic barriers; not results)

**Source Coverage:** Hugh Montgomery, *Multiplicative Number Theory II: Primes and Sieves*, the distributional limits / barriers of the mean-value and large-value machinery (as recorded in transformed notes). **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

حدودُ آلة MNT-II (المتوسّط والقيم الكبيرة) عند نقطةِ توقّفها اللاشرطيّة، مقروءةً **كجدرانٍ تشخيصيّةٍ (barriers)** لجبهة `FRONTIER-ANT-PVG-006` — «أين تقفُ الطريقة»، لا «كيف تُكسَر». يكمّل 006-A: الأوّلُ الضغطُ (pressure)، والثاني حيثُ يتوقّف الضغط.

## Classical role

لآلة المتوسّط/القيم الكبيرة **حدودٌ لاشرطيّةٌ معروفة**: قاعُ فرضيّة الكثافة `17/30 = 1 − 1/A`، جدارُ الإيجابيّة/Weil، وحدُّ المنطقة الخالية. **معروفةٌ، مُستشهَدة.**

## Distribution-barrier diagnostic role

الحدُّ = **جدارٌ قائمٌ أو شهادةٌ ناقصة**، لا نتيجة. `TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001` يخرّط أين تقفُ الطريقةُ اللاشرطيّة.

## Barriers / limits view

```text
Density-hypothesis floor : WALL-DENSITY-HYP (17/30 = 1 − 1/A) — the unconditional zero-density limit
Positivity / Weil wall   : WALL-POSITIVITY-WEIL — the explicit-formula positivity barrier
Zero-free limit          : WALL-ZERO-FREE — the barrier to a pointwise ψ(x)−x error
```

## PVG–ANT connection

خريطةُ جدرانٍ لجبهة 006 تكمّل مرصدَ الضغط (006-A): حيثُ يبلغُ الضغطُ حدَّه يقف جدار. سلّمُ التكلفة: **residue → spectral = GRH-level** (لا يُعبَر مجّانًا).

## What it can diagnose

- أين تقفُ الطريقةُ اللاشرطيّة (قاعُ الكثافة، جدارُ الإيجابيّة، حدُّ zero-free).
- أيُّ جدارٍ يحدُّ أيَّ تقدير.
- أنّ النتائجَ التوزيعيّةَ الدقيقة (pair correlation, prime races) **مشروطةٌ بـRH** ولا تُعطي معلومةً لاشرطيّة.

## What it cannot prove

- **لا يعبر أيَّ جدار** · لا يبرهن RH/GRH · لا مبرهنةَ حدٍّ توزيعيٍّ جديدة.
- لا تحسينَ كثافة/قيمٍ كبيرة.
- لا يحلّ `MC-002` ولا `MC-005`.

## Related walls

`WALL-POSITIVITY-WEIL` · `WALL-DENSITY-HYP` · `WALL-ZERO-FREE` · `WALL-SIEGEL` · `WALL-OFF-DIAGONAL`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-002` (خطأٌ قويٌّ لـψ(x)−x / RH) · `MC-005` (توزيعُ AP GRH-level) — **تبقى غيرَ محلولة.**

## Claim classification

**Diagnostic / Boundary.** الحدودُ Known ومُستشهَدة؛ المخرجُ خريطةُ جدرانٍ وشهاداتٍ ناقصة، لا New Theorem ولا Candidate Mechanism.

## No-Go notes

```text
- distributional limits/barriers are read as walls / missing certificates, not as results.
- RH-conditional distributional statistics (Montgomery pair correlation, Rubinstein–Sarnak prime races)
  are OUT of unconditional scope here — conditional, deferred, no unconditional certificate produced.
- not RH/GRH progress; not a distributional-limit theorem; not a zero-density / large-values improvement.
- no crossing WALL-POSITIVITY-WEIL / WALL-DENSITY-HYP / WALL-ZERO-FREE / WALL-SIEGEL.
- MC-002 and MC-005 stay unsolved.
- no raw copyrighted text; transformed notes only.
```

## Next valid action

**Superseded (historical):** MNTII-006-B is closure-reviewed (`v0.6-b-closure.md` PASS); MNTII-006-C was later executed and closed. No full book mining; no expansion without explicit permission.

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] Transformed notes only (no raw text, no copied passages, no general summary)
- [x] No RH/GRH progress · no distributional-limit theorem · no zero-density / large-values improvement · no new theorem
- [x] RH-conditional distributional results (pair correlation, prime races) explicitly excluded as out-of-scope / conditional
- [x] No crossing WALL-POSITIVITY-WEIL / WALL-DENSITY-HYP / WALL-ZERO-FREE / WALL-SIEGEL · MC-002 & MC-005 unsolved
- [x] Target registered in planned then promoted to live on honest completion: `TOOL-MONTGOMERY-DISTRIBUTION-BARRIER-001` (Diagnostic / Frontier Support); planned.jsonl empty
- [x] MNTII-006-C not started · no full book mining
- [x] Six guards PASS after this unit

**Ceiling:** distributional limits / barriers enter as diagnostic walls and missing certificates for `FRONTIER-ANT-PVG-006` — where the unconditional method stops, not a crossing. RH-conditional statistics are out of scope. No RH/GRH progress.
