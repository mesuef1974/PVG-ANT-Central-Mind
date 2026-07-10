# MNTII-006-F — Prime Exponential Sums and Type I/II Decomposition Diagnostic

**Registry ID:** MNTII-006-F
**Status:** CLOSED — v0.6-F Closure Review **PASS** (`audits/v0.6-f-closure.md`, AUDIT-CM-V06-F-CLOSURE-001, HEAD b85c1e4, second attempt); entered as validated_intake from the ChatGPT Treasure Packet (Ch 17; selected via Coverage Audit 007)
**Classification:** **Diagnostic / Boundary** (KNOWN analytic methods read as a bridge diagnostic; not results)

**Source Coverage:** Montgomery–Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, **Chapter 17 (Estimates for Sums over Primes)**: §17.1 principles of the method, §17.2 an exponential sum formed with primes, §17.3 further applications, §17.4 digit sums of primes, §17.5 notes, §17.6 references. **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

المجاميعُ الأُسّيّةُ الموزونةُ بالأوّليّات عبر وزنِ von Mangoldt:

```text
S(alpha) = sum_{n <= N} Lambda(n) e(n alpha)
```

وتفكيكاتُ Λ (على طريقة Vinogradov / Vaughan) التي تحوّل مجاميعَ الأوّليّات إلى **بُنى من النمطين I وII** — قطعٍ مُهيكلةٍ وثنائيّاتِ خطّيّةٍ قابلةٍ للتقدير. **وحدةُ جسرٍ** بين أدوات الفصل 16 وتطبيقات الفصل 18، لا وحدةَ مبرهنةٍ نهائيّة.

## Classical role (KNOWN, cited)

الفصلُ 17 يعالج المجاميعَ على الأوّليّات **باستبدال كشفِ الأوّليّات المباشرِ بتفكيكاتِ Λ**: التفكيكُ يردُّ تقديرَ المجموع الأُسّيّ الأوّليّ إلى بُنى Type I / Type II قابلةٍ للتحكّم — **طريقةُ برهانِ إلغاءٍ (cancellation)** في المجاميع الموزونة بالأوّليّات، خصوصًا على الأقواس الصغرى والأطوار المتذبذبة. §17.4 (المجاميعُ الرقميّةُ للأوّليّات) يعرض الآلةَ **قابلةً للنقل** لا حيلةَ مسألةٍ واحدة. **معروفٌ، مُستشهَد.**

## Diagnostic role

يشرحُ **من أين تدخل المعلومةُ المفيدة** إلى تقديرات الأوّليّات دون كاشفِ أوّليّات:

```text
Type I            : one-variable structured / divisor-like control
Type II           : bilinear cancellation
exponential phase : oscillatory test of distribution
minor-arc estimate: a cancellation CERTIFICATE, not a distribution theorem by itself
```

ويشرح **لماذا تحتاج الغرابيلُ شهاداتٍ ثنائيّةً/أُسّيّةً خارجيّة**. `TOOL-MONTGOMERY-PRIME-SUMS-TYPE-II-DIAGNOSTIC-001`.

## PVG–ANT connection

بلغة PVG: **Λ(n) وزنٌ محوريٌّ لقوى الأوّليّات، لا شهادةُ أوّليّةٍ هندسيّة**. تفكيكاتُ Type I/II تحوّل الوزنَ المحوريَّ إلى شرائحَ مُهيكلةٍ داخل مخروط التقييم: **Type I = هندسةُ قواسمَ أحاديّةُ الجانب · Type II = تفاعلٌ ثنائيُّ الخطّيّة بين كتل التقييم**. يستطيع PVG **تسميةَ** هذه الهندسات وتصنيفَها، لكنّ **شهادةَ الإلغاء تبقى تحليليّةً** — لا يستبدلها PVG.

جسرُ ANT: يربط أدواتِ Ch16 (Van der Corput، دعمٌ خلفيّ) بمجاميع الأوّليّات (Ch17) وتطبيقاتِها الجمعيّة (Ch18، أماميّ)، وبالتوزيع المتوسّط BV (`MNTII-006-C`) وسقوفِ الغربال وحاجتِها لمدخل Type II (`MNTII-006-D`) واعتمادِ الفجوات المحدودة على مدخلات التوزيع/الغربال (`MNTII-006-E`) واستهلاكِ Type I/II عند Harman (`BOOK-SIEVE-HARMAN-004`).

## Frontier links

`FRONTIER-ANT-PVG-004` (معلومةُ الغربال — المستهلكُ الرئيسُ لشهادة Type II الخارجيّة) · `FRONTIER-ANT-PVG-006` (التوزيع / مجاميع الأوّليّات). **ملاحظةُ أمانةٍ:** الحزمةُ أجازت ربطًا اختياريًّا بواجهةِ نظريّةِ أعدادٍ جمعيّةٍ «if present» — الجبهةُ `FRONTIER-ANT-PVG-003` الموجودةُ فعلًا موضوعُها Möbius/Liouville لا الجمعيّات، **فأُسقط الربطُ الاختياريُّ** (لا اختراعَ جبهةٍ). لا ربطَ بأيّ تقدّم RH/GRH.

## What it can diagnose

- كيف يُحصَّل الإلغاءُ على الأوّليّات **بلا كاشفِ أوّليّات** (عبر تفكيك Λ).
- أين يدخل التحكّمُ المُهيكل (Type I) وأين الإلغاءُ الثنائيّ (Type II).
- لماذا معلومةُ Type II هي الشهادةُ الخارجيّةُ التي تطلبها الغرابيل (سياقُ MC-001).
- أنّ تقديرَ القوس الصغرى شهادةُ إلغاءٍ لا مبرهنةَ توزيعٍ بذاتها.

## What it cannot prove

- **لا مبرهنةَ جديدة** · لا تحسينَ حدٍّ أُسّيّ · **لا اختراقَ Type II**.
- لا كسرَ تكافؤِ الغربال · لا تحسينَ PNT/AP · لا تقدّمَ RH/GRH.
- لا يحلّ `MC-001` (مدخلُ Type II يغذّي الغربالَ لكنّه لا يجعله كاشفَ أوّليّات) ولا `MC-005` (التحكّمُ المتوسّط/الثنائيّ ليس تحكّمًا فرديًّا AP/GRH) ولا `MC-002`.

## Related walls

`WALL-OFF-DIAGONAL` · `WALL-PARITY` · `WALL-SIEVE-CEILING` · `WALL-DENSITY-HYP`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-001` — تبقى غيرَ محلولة (Type II مدخلٌ لا كاشف). `MC-005` — تبقى غيرَ محلولة (متوسّط/ثنائيّ ≠ فرديّ). `MC-002` — لا تُمَسّ ولا تُعَدُّ محلولة.

## Claim classification

**Diagnostic / Boundary.** الطرائقُ (Vinogradov/Vaughan، Type I/II، الأقواسُ الصغرى، المجاميعُ الرقميّة) **معروفةٌ (Known) ومُستشهَدةٌ للمصدر**؛ مخرجُ الوحدة قراءةٌ تشخيصيّةٌ جسريّة، لا New Theorem ولا Candidate Mechanism.

## No-Go notes

```text
- prime sums are handled through Lambda decompositions, NOT direct prime detection.
- PVG does NOT prove cancellation over primes and does NOT supply Type II estimates.
- Type II does NOT break parity; the Vaughan identity does NOT solve MC-001.
- minor-arc estimates do NOT imply RH/GRH progress; a minor-arc bound is a cancellation
  certificate, not a distribution theorem.
- digit sums of primes are a KNOWN application of the Type I/II machine, NOT a PVG result.
- Chapter 17 does NOT close the Montgomery overlay; no new theorem; no improved
  exponential-sum bound; no PNT/AP improvement; no RH/GRH progress.
- no crossing WALL-OFF-DIAGONAL / WALL-PARITY / WALL-SIEVE-CEILING / WALL-DENSITY-HYP.
- MC-001, MC-002, MC-005 stay unsolved.
- no raw copyrighted text; transformed notes only.
```

## Intake / Validation note

```text
Created by SOURCE-GROUNDED intake from a ChatGPT Treasure Packet (Ch 17: Estimates for Sums
over Primes), selected via Coverage Audit 007 (AUDIT-CM-MONTGOMERY-COVERAGE-007) with explicit
permission. Entered as validated_intake; CLOSED after the second v0.6-F Closure Review
(3 auditors PASS + falsifier unrefuted + 7/7 guards; see audits/v0.6-f-closure.md).
Packet deviation (reported, not silently resolved): the optional additive-interface frontier
link was conditioned on existence; the actual FRONTIER-ANT-PVG-003 is a different topic
(Mobius/Liouville), so the optional link was dropped.
```

## Next valid action

**Historical unit record.** MNTII-006-F was closure-reviewed (`v0.6-f-closure.md` PASS, second attempt). This file does not define the current live next action. The only authoritative live next action is: `transition-memory/next-action.md`.

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary)
- [x] SOURCE-GROUNDED from Treasure Packet (Ch 17, §17.1–17.6); transformed notes only
- [x] Known methods recorded as Known; no new theorem; no improved bound; not a PVG result
- [x] Type II = input to sieves, NOT a prime detector; minor arcs = certificate, not theorem
- [x] No crossing WALL-OFF-DIAGONAL / WALL-PARITY / WALL-SIEVE-CEILING / WALL-DENSITY-HYP · MC-001/002/005 unsolved
- [x] Entered as validated_intake; CLOSED by v0.6-F Closure Review PASS (3 auditors + falsifier unrefuted)
- [x] TOOL-MONTGOMERY-PRIME-SUMS-TYPE-II-DIAGNOSTIC-001 registered; cards 037–043; planned.jsonl empty
- [x] MNTII-006-G not started · no full book mining · Seven guards PASS after this intake

**Ceiling:** Chapter-17 methods enter as a KNOWN bridge diagnostic — Λ is an axial weight not a primality certificate; Type I/II decompositions are analytic reductions; the cancellation certificate stays analytic and external to PVG. No new theorem, no Type II breakthrough, no parity break, no PNT/AP improvement. MC-001/002/005 unsolved; walls uncrossed. No RH/GRH progress.
