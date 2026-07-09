# MNTII-006-A (QUARANTINED — source-mismatch / cross-volume) — Montgomery-style Analytic Tools

> **Status: source-mismatch / cross-volume-context / not trusted.** Zero-density / large values / pair-correlation
> are deferred by the Montgomery MNT-II source to a LATER volume; this unit was invented before source grounding.
> Prior A closure audit was a safety/coherence check only and is SUPERSEDED by Source-Grounding Correction 006;
> it does NOT certify source-grounded Montgomery extraction. See `audits/montgomery-source-grounding-correction-006.md`.

**Registry ID:** MNTII-006-A
**Status:** QUARANTINED (source-mismatch / cross-volume)
**Classification:** **Diagnostic / Boundary** (known MNT-II analytic tools read as frontier-support diagnostics; not results)

**Source Coverage:** Hugh Montgomery, *Multiplicative Number Theory II: Primes and Sieves*, the mean-value / large-value / zero-density machinery and the primes-and-sieves interface (as recorded in transformed notes). **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

أدواتُ MNT-II التحليليّة (مبرهناتُ المتوسّط، تقديراتُ القيم الكبيرة، سياقُ كثافة الأصفار، واجهةُ الأوّليّات-والغربال) مقروءةً **كمراصدِ توزيعٍ تشخيصيّةٍ** تدعم جبهةَ `FRONTIER-ANT-PVG-006`، لا كنتائجَ جديدة.

## Classical role

مبرهناتُ المتوسّط والقيم الكبيرة وكثافةُ الأصفار في MNT-II **معروفةٌ، مُستشهَدة**؛ تُغذّي التحكّمَ في توزيع الأوّليّات في المتوسّط (أدوات Montgomery–Vaughan، بنكهة Bombieri–Vinogradov). **لا تُدخَل كبراهين، بل كسياقِ دعم.**

## Distribution diagnostic role

تقديراتُ التوزيع = **ضغطُ شهادةٍ لا برهان**: تحدُّ بُعدَنا عن RH لاشرطيًّا في المتوسّط، دون حلٍّ نقطيّ. التحكّمُ في المتوسّط/القيم الكبيرة = دعمٌ عائليّ. `TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001`.

## Family / support interpretation

```text
Tools    : mean-value theorems · large-value estimates · zero-density context · primes-and-sieves interface
Reading  : certificate pressure (average / family control), not pointwise proof
Serves   : FRONTIER-ANT-PVG-006, deepening after v0.4 Iwaniec–Kowalski
```

## PVG–ANT connection

مرصدُ الدعم اللاقطريّ/العائليّ لجبهة 006: يجاورُ أدواتِ IK (`TOOL-ZERO-DENSITY-DIAGNOSTIC-001`, `TOOL-LARGE-VALUE-DIAGNOSTIC-001`) ويقوّي واجهةَ الأوّليّات-والغربال (جسرٌ إلى `FRONTIER-ANT-PVG-004`). سلّمُ التكلفة: التحكّمُ في المتوسّط رخيصٌ نسبيًّا؛ **residue → spectral = GRH-level** (لا يُعبَر مجّانًا).

## What it can diagnose

- كيف تحدُّ أدواتُ التوزيع بُعدَنا عن RH في المتوسّط.
- أين تُغذّي القيمُ الكبيرة/المتوسّطُ كثافةَ الأصفار.
- جسرُ الأوّليّات-والغربال كواجهةٍ تشخيصيّة.

## What it cannot prove

- **لا يبرهن RH/GRH** ولا يحسّن كثافةَ الأصفار.
- لا مبرهنةَ قيمٍ كبيرةٍ جديدة، ولا تحسينَ PNT/AP.
- لا يحلّ `MC-002` ولا `MC-005`.

## Related walls

`WALL-ZERO-FREE` · `WALL-SIEGEL` · `WALL-POSITIVITY-WEIL` · `WALL-DENSITY-HYP` · `WALL-OFF-DIAGONAL`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-002` (خطأٌ قويٌّ لـψ(x)−x / RH) · `MC-005` (توزيعُ AP GRH-level) — **كلاهما شهادةٌ ناقصةٌ لا نتيجة، تبقى غيرَ محلولة.**

## Claim classification

**Diagnostic / Boundary.** الأدواتُ Known ومُستشهَدة؛ المخرجُ مرصدُ توزيعٍ وحدٌّ، لا New Theorem ولا Candidate Mechanism.

## No-Go notes

```text
- Montgomery-style analytic tools are read as distribution diagnostics / certificate pressure, not proof.
- not RH/GRH progress; not a zero-density improvement; not a large-values theorem; not a PNT/AP improvement.
- distribution / average control is family-level support, not pointwise resolution.
- no crossing WALL-SIEGEL / WALL-POSITIVITY-WEIL / WALL-ZERO-FREE.
- MC-002 and MC-005 stay unsolved.
- no raw copyrighted text; transformed notes only.
```

## Next valid action

**Historical unit record (QUARANTINED — source-mismatch).** The prior closure audit (`v0.6-a-closure.md`) is SOURCE-GROUNDING-SUPERSEDED. This file does not define the current live next action. The only authoritative live next action is: `transition-memory/next-action.md`.

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] Transformed notes only (no raw text, no copied passages, no general summary)
- [x] No RH/GRH progress · no zero-density improvement · no large-values theorem · no PNT/AP improvement · no new theorem
- [x] No crossing WALL-SIEGEL / WALL-POSITIVITY-WEIL / WALL-ZERO-FREE · MC-002 & MC-005 unsolved
- [x] Target registered in planned then promoted to live on honest completion: `TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001` (Diagnostic / Frontier Support); planned.jsonl empty
- [x] MNTII-006-B not started · no full book mining
- [x] Six guards PASS after this unit

**Ceiling:** Montgomery-style analytic tools enter as distribution diagnostics / certificate pressure feeding `FRONTIER-ANT-PVG-006` — not RH/GRH progress, not zero-density/large-values improvements, not new theorems. No RH/GRH progress.
