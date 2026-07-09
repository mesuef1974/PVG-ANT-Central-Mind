# MNTII-006-E — Bounded Gaps between Primes as a GPY / Maynard Sieve Diagnostic

**Registry ID:** MNTII-006-E
**Status:** CLOSED — v0.6-E Closure Review **PASS** (`audits/v0.6-e-closure.md`, AUDIT-CM-V06-E-CLOSURE-001, HEAD 959e417, third attempt); entered as validated_intake from the ChatGPT Treasure Packet
**Classification:** **Diagnostic / Boundary** (the KNOWN bounded-gaps theorem read as a sieve diagnostic; not a new result)

**Source Coverage:** Montgomery–Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, **Chapter 22 (Bounded Gaps between Primes)**: §22.1 the GPY sieve, §22.2 the proof of Maynard's theorem, §22.3 consequences, §22.4 notes. Dependency: Ch 20 Bombieri–Vinogradov (level of distribution), Ch 21 sieve framework / fixed-dimension sieves. **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

أوزانُ الغربال متعدّدِ الأبعاد (GPY / Maynard) على k-tuples **مقبولة (admissible)**، مقروءةً **كمرصدٍ تشخيصيّ**: كشفٌ موزونٌ للإزاحاتِ الغنيّةِ بالأوّليّات `n + H`، بمستوى توزيعٍ للأوّليّات كمدخلٍ خارجيّ. **الكنزُ الصحيحُ للفصل 22** (يستبدلُ وحدةَ E القديمةَ المحجورةَ عن الإلغاء اللاقطريّ).

## Classical role (KNOWN, cited)

الفصلُ 22 يعرضُ الفجواتِ المحدودةَ **كنتيجةِ غربالٍ من مدخلٍ توزيعيّ**: مبرهنةُ Maynard تستعملُ مستوى توزيعٍ موجبًا للأوّليّات؛ **بـBombieri–Vinogradov مدخلًا، يحصلُ Maynard على فجواتٍ محدودةٍ لاشرطيًّا** (مبرهنةٌ كلاسيكيّةٌ معروفة، **لا نتيجةٌ لنا**). تحسيناتُ Elliott–Halberstam تبقى **مشروطة**.

## Diagnostic role

يشرحُ كيف يُنتج **متوسّطُ معلومةِ التوزيع + أوزانٌ مُحسَّنة** ثلاثيّاتٍ مقبولةً غنيّةً بالأوّليّات. **ليس كاشفًا للأوّليّات · ليس مبرهنةَ توائم · ليس تقدّمَ RH/GRH · لا يحلّ حاجزَ التكافؤ ولا يعبرُه.** `TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001`.

## Sieve view

```text
Admissible k-tuple H : a tuple with no local residue obstruction (NOT a guaranteed all-prime tuple)
GPY / Maynard weights: optimization devices over residue-filtered boxes (NOT primality certificates)
Level of distribution: EXTERNAL input (Bombieri–Vinogradov supplies it unconditionally, on average)
Reading             : average distribution + optimized weights -> a prime-rich translate n+H (a bounded gap)
```

## PVG–ANT connection

بلغة PVG: الثلاثيّاتُ المقبولةُ **تكويناتُ دعمٍ مُزاحةٌ تتجنّبُ عوائقَ البواقي المحلّيّة**؛ أوزانُ GPY/Maynard **أدواتُ تحسينٍ فوق صناديقَ مُرشَّحةٍ بالبواقي، لا شهاداتُ أوّليّةٍ مباشرة**. الشهادةُ الحاسمةُ تبقى **تحليليّة**: توزيعٌ متوسّطٌ + مقارباتُ الغربال الموزونة. يربطُ الغربالَ الكبير/BV (`FRONTIER-ANT-PVG-006`) بجبهة الغربلة (`FRONTIER-ANT-PVG-004`).

## What it can diagnose

- كيف يتحوّلُ مستوى التوزيع + الأوزان إلى فجوةٍ محدودة.
- لماذا الثلاثيّةُ المقبولةُ ليست ضمانًا بأوّليّةِ كلِّ مركّباتها.
- أينَ يبقى الشرطُ (EH) وأينَ اللاشرط (BV).

## What it cannot prove

- **ليست مبرهنةَ توائم** · ليست تحسينًا للفجوات المحدودة · ليست كشفًا للأوّليّات.
- لا تكسرُ التكافؤ · لا تقدّمَ RH/GRH · لا تحسينَ PNT/AP.
- لا تحلّ `MC-001` ولا `MC-005`.

## Related walls

`WALL-PARITY` · `WALL-SIEVE-CEILING` · `WALL-OFF-DIAGONAL` · `WALL-DENSITY-HYP`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-001` (كسرُ parity غيرُ مشروط) — تبقى غيرَ محلولة (الأوزانُ ليست كواشفَ أوّليّات). `MC-005` (توزيعُ AP الفرديّ GRH-level) — تبقى غيرَ محلولة (المتوسّطُ ليس تحكّمًا فرديًّا). `MC-002` لا تُمَسّ ولا تُعَدُّ محلولة.

## Claim classification

**Diagnostic / Boundary.** مبرهنةُ الفجوات المحدودة (Maynard/GPY) **معروفةٌ (Known) ومُستشهَدةٌ للمصدر**؛ مخرجُ الوحدة قراءةٌ تشخيصيّةٌ لها، لا New Theorem ولا Candidate Mechanism ولا نتيجةٌ لنا.

## No-Go notes

```text
- bounded gaps (GPY / Maynard) is a KNOWN classical theorem recorded as known mathematics; NOT our result.
- bounded gaps are NOT twin primes and NOT a parity breakthrough.
- GPY / Maynard weights are optimization devices, NOT prime detectors / primality certificates.
- Bombieri–Vinogradov is average distribution input, NOT individual GRH; Elliott–Halberstam is conditional only.
- no new theorem; no bounded-gaps improvement; no PNT/AP improvement; no RH/GRH progress.
- no crossing WALL-PARITY / WALL-SIEVE-CEILING / WALL-OFF-DIAGONAL / WALL-DENSITY-HYP.
- MC-001 and MC-005 stay unsolved; MC-002 not marked solved.
- no raw copyrighted text; transformed notes only.
```

## Intake / Validation note

```text
Created by SOURCE-GROUNDED intake from a ChatGPT Treasure Packet (Ch 22), replacing the legacy
MNTII-006-E (exponential / Kloosterman off-diagonal), which is quarantined as source-mismatch
(units/_quarantine/MNTII-006-E-legacy-offdiagonal-source-mismatch.md). Entered as validated_intake;
CLOSED after the third v0.6-E Closure Review (3 auditors PASS + falsifier unrefuted + 7/7 guards).
See audits/montgomery-source-grounding-correction-006.md and audits/v0.6-e-closure.md.
```

## Next valid action

**Historical unit record.** MNTII-006-E was closure-reviewed (`v0.6-e-closure.md` PASS, third attempt). This file does not define the current live next action. The only authoritative live next action is: `transition-memory/next-action.md`.

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] SOURCE-GROUNDED from Treasure Packet (Ch 22); transformed notes only
- [x] Known bounded-gaps theorem recorded as Known; NOT our result; NOT twin primes; NOT a parity breakthrough
- [x] BV = average input; EH = conditional; NOT individual GRH
- [x] No crossing WALL-PARITY / WALL-SIEVE-CEILING / WALL-OFF-DIAGONAL / WALL-DENSITY-HYP · MC-001 & MC-005 unsolved
- [x] Entered as validated_intake; CLOSED by v0.6-E Closure Review PASS (3 auditors + falsifier unrefuted)
- [x] Legacy off-diagonal E quarantined; TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 registered
- [x] Seven guards PASS after this intake

**Ceiling:** bounded gaps (GPY / Maynard) enter as a KNOWN theorem read as a sieve diagnostic — not our result, not twin primes, not a parity breakthrough, not RH/GRH progress. Weights are optimization devices, not prime detectors. MC-001 / MC-005 unsolved; walls uncrossed. No RH/GRH progress.
