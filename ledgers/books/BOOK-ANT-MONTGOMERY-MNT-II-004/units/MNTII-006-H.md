# MNTII-006-H — Additive Prime Number Theory as Circle-Method Application Layer

**Registry ID:** MNTII-006-H
**Status:** validated_intake (from ChatGPT Treasure Packet, Ch 18) — **NOT closed, NOT PASS, pending v0.6-H Closure Review**
**Classification:** **Diagnostic / Boundary** (KNOWN circle-method applications read as an application layer; not results)
**Unit role:** application_unit — source-grounded; the FINAL content-chapter unit; not a book closure.

**Source Coverage:** Montgomery–Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, **Chapter 18 (Additive Prime Number Theory)**: §18.1 sums of three primes, §18.2 sums of two primes on average, §18.3 conditional estimates, §18.4 a lower bound for the error term, §18.5 prime k-tuples, §18.6 the distribution of primes in short intervals, §18.7 notes, §18.8 references. **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

التمثيلاتُ الجمعيّةُ للأعداد بالأوّليّات:

```text
N = p1 + p2 + ... + pk
```

بدوالِّ توليدِ طريقةِ الدائرة لمجاميع الأوّليّات، وتفكيكِ **الأقواس الكبرى/الصغرى**، وGoldbach الثلاثيّ (مجموعُ ثلاثِ أوّليّات)، و**الثنائيُّ بصيغةِ المتوسّط فقط**، ثمّ التقديراتِ المشروطةِ وk-tuples وفتراتِ القِصَر بوصفها **واجهاتِ جبهةٍ لا شهاداتٍ منجزة**.

## Classical role (KNOWN, cited)

الفصلُ 18 يستعمل **طريقةَ الدائرة (Hardy–Littlewood) بتعديل Vinogradov** للمسائل الجمعيّة على الأوّليّات. **لمجموعِ ثلاثِ أوّليّاتٍ تنجحُ الطريقة** (مبرهنةٌ معروفةٌ من المصدر). **لمجموعِ أوّليَّين تفشلُ المعالجةُ المباشرة**، لكنّ الفصلَ يبرهن نتيجةَ **«في المتوسّط / تقريبًا كلّ»** الأعدادِ الزوجيّة عبر ارتباطاتٍ موزونةٍ بـvon Mangoldt. الأقسامُ اللاحقة (المشروطة، k-tuples، الفتراتُ القصيرة) **واجهاتُ جبهةٍ** تُسجَّل كما هي. **معروفٌ، مُستشهَد.**

## Diagnostic role (application layer)

يُظهر كيف **تُستهلَك** طبقاتُ الدعم السابقة:

```text
Ch 16 (G) : oscillatory cancellation language
Ch 17 (F) : prime exponential sums / Type I-II machinery
Ch 19-20 (C) : distribution-in-average machinery (background where relevant)
Ch 21-22 (D/E) : sieve-side applications and limitations (contrast)
Ch 18 (H) : the APPLICATION layer consuming them — not a new foundational tool layer
```

`TOOL-MONTGOMERY-ADDITIVE-PRIME-CIRCLE-METHOD-DIAGNOSTIC-001`.

## PVG–ANT connection

بلغة PVG: المسائلُ الجمعيّةُ تسأل عن **مجاميعَ مُهيكلةٍ لنقاطِ دعمٍ أوّليٍّ محوريّ**؛ العوائقُ المحلّيّةُ للبواقي و**السلسلةُ الشاذّة (singular series)** تعكسان هندسةَ التطابقات؛ **الأقواسُ الكبرى** ترمّز البنيةَ المحلّيّة/الحدَّ الرئيس، و**الأقواسُ الصغرى** ترمّز **شهادةَ الإلغاء الناقصة**. يستطيع PVG **تنظيمَ هندسةِ العوائق المحلّيّة، لكنّه لا يستبدل تقديراتِ طريقةِ الدائرة التحليليّة**.

## Frontier links

`FRONTIER-ANT-PVG-006` (مجاميعُ الأوّليّات / التوزيع) · `FRONTIER-ANT-PVG-004` (الغربلة — تباينًا داعمًا). **ملاحظةُ أمانةٍ:** الحزمةُ أجازت ربطًا بجبهةِ أوّليّاتٍ جمعيّةٍ «إن وُجدت» — **لا جبهةَ جمعيّةً في السجلّ** (الجبهاتُ 001–008 معروفة) **فأُسقط الربطُ الشرطيُّ ولم تُختَرع جبهةٌ** بلا موافقةِ سجلّ. لا ربطَ بأيّ تقدّم RH/GRH.

## What it can diagnose

- كيف يفصل تفكيكُ الدائرة البنيةَ المحلّيّةَ (major arcs + singular series) عن متطلَّب الإلغاء (minor arcs).
- لماذا تنجح الطريقةُ في الثلاثيّ وتفشلُ مباشرةً في الثنائيّ، وما الذي تشتريه صيغةُ «تقريبًا كلّ».
- أين تدخل ارتباطاتُ von Mangoldt الثنائيّةُ الموزونةُ في السلوك الجمعيّ المتوسّط.
- أنّ k-tuples والفتراتِ القصيرةَ واجهاتُ جبهةٍ مشروطة/حدسيّة، لا شهاداتٍ منجزة.

## What it cannot prove

- **لا برهانَ Goldbach**: **الثنائيُّ مفتوحٌ (open) ولا يُدَّعى أبدًا**؛ «تقريبًا كلّ» ≠ «كلّ».
- لا تحسينَ Goldbach الثلاثيّ (معروفٌ من المصدر لا نتيجتُنا) · لا حدَّ minor-arc جديدًا · لا مبرهنةَ singular-series جديدة.
- لا مبرهنةَ k-tuples · لا اختراقَ فتراتٍ قصيرة · التقديراتُ المشروطةُ **تبقى مشروطة**.
- لا يُحيي A/B ولا legacy-E · لا twin primes · لا تحسينَ PNT/AP · لا تقدّمَ RH/GRH.
- لا يحلّ `MC-001` (الطرائقُ الجمعيّةُ لا تجعل الغرابيلَ كواشفَ أوّليّات) ولا `MC-005` (المتوسّط/المشروطُ ليس تحكّمًا فرديًّا GRH/AP) ولا `MC-002`.

## Related walls

`WALL-OFF-DIAGONAL` · `WALL-SIEVE-CEILING` · `WALL-PARITY` · `WALL-DENSITY-HYP` · `WALL-ZERO-FREE`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-001` — تبقى غيرَ محلولة. `MC-005` — تبقى غيرَ محلولة. `MC-002` — لا تُمَسّ ولا تُعَدُّ محلولة.

## Claim classification

**Diagnostic / Boundary (application unit).** طريقةُ الدائرة وGoldbach الثلاثيُّ ونتيجةُ المتوسّط الثنائيّةُ **معروفةٌ (Known) ومُستشهَدةٌ للمصدر**؛ Goldbach الثنائيُّ **Open Problem**؛ المشروطُ **conditional**؛ مخرجُ الوحدة قراءةُ طبقةِ تطبيقاتٍ، لا New Theorem ولا Candidate Mechanism.

## No-Go notes

```text
- PVG does NOT prove Goldbach and does NOT prove binary Goldbach; Goldbach is NOT solved.
- binary Goldbach is an OPEN problem; only average / almost-all forms are source-grounded here,
  and 'almost all even numbers' does NOT mean all even numbers.
- ternary Goldbach (three primes) is KNOWN source mathematics — NOT a PVG result, NOT improved here.
- a conditional estimate is NOT a theorem; it stays explicitly conditional.
- the singular series does NOT prove the representation by itself; major arcs alone do NOT solve
  the problem; minor arcs are NOT solved by PVG — they are the missing cancellation certificate.
- prime k-tuples are NOT proved; short-interval conjectures are NOT proved — frontier interfaces only.
- Ch 18 does NOT revive A/B or legacy-E; no twin primes; no PNT/AP improvement; no RH/GRH progress.
- the Montgomery overlay is NOT closed (partial_overlay stands until a post-H coverage audit).
- no crossing WALL-OFF-DIAGONAL / WALL-SIEVE-CEILING / WALL-PARITY / WALL-DENSITY-HYP / WALL-ZERO-FREE.
- MC-001, MC-002, MC-005 stay unsolved.
- no raw copyrighted text; transformed notes only.
```

## Intake / Validation note

```text
Created by SOURCE-GROUNDED intake from a ChatGPT Treasure Packet (Ch 18: Additive Prime Number
Theory) — the FINAL content-chapter unit, mined on the completed support base (G: Ch 16 cancellation,
F: Ch 17 prime sums, C: Ch 19-20 average distribution). Status = validated_intake: NOT closed,
NOT PASS, pending v0.6-H Closure Review.
Central fencing of this packet: binary Goldbach is OPEN and is never claimed; 'almost all' is an
average statement; conditional estimates stay conditional.
Packet deviation (reported, not silently resolved): the conditional additive-prime frontier link
('if an additive-prime frontier exists') was dropped — no such frontier exists in the registry
and none was invented.
After the H closure, the next action is a Montgomery post-H coverage/overlay audit — NOT an
automatic MNTII-006-I.
```

## Next valid action

**Pending unit.** This unit awaits its v0.6-H Closure Review (see the Status line). This file does not define the current live next action. The only authoritative live next action is: `transition-memory/next-action.md`.

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary, application unit)
- [x] SOURCE-GROUNDED from Treasure Packet (Ch 18, §18.1–18.8); transformed notes only
- [x] Ternary Goldbach = KNOWN source result; binary Goldbach = OPEN, never claimed; almost-all ≠ all
- [x] Conditional estimates stay conditional; k-tuples / short intervals = frontier interfaces only
- [x] No revival of A/B/legacy-E; no twin primes; no minor-arc/singular-series/PNT/AP claims
- [x] No crossing the five listed walls · MC-001/002/005 unsolved
- [x] Status = validated_intake (NOT closed, NOT PASS); pending v0.6-H Closure Review
- [x] TOOL-MONTGOMERY-ADDITIVE-PRIME-CIRCLE-METHOD-DIAGNOSTIC-001 registered; cards 052–060; planned.jsonl empty
- [x] MNTII-006-I not started · post-H step = coverage/overlay audit · Seven guards PASS after this intake

**Ceiling:** Chapter-18 material enters as a KNOWN application layer — the circle method separates major-arc structure from the minor-arc cancellation requirement; PVG organizes local obstruction geometry but cannot replace the analytic estimates. No Goldbach proof; binary Goldbach OPEN; no new theorem; no minor-arc bound; no k-tuples/short-interval breakthrough; no PNT/AP improvement. MC-001/002/005 unsolved; walls uncrossed. No RH/GRH progress.
