# MNTII-006-G — Exponential Sums and Van der Corput Cancellation Support Layer

**Registry ID:** MNTII-006-G
**Status:** CLOSED — v0.6-G Closure Review **PASS** (`audits/v0.6-g-closure.md`, AUDIT-CM-V06-G-CLOSURE-001, HEAD b6219c3, second attempt); entered as validated_intake from the ChatGPT Treasure Packet (Ch 16; selection recorded at 4a042b5)
**Classification:** **Diagnostic / Boundary** (KNOWN cancellation machinery read as a SUPPORT layer; not results, not an application closure)
**Unit role:** support_unit — source-grounded; feeds Ch 17 / Ch 18; not a standalone theorem unit.

**Source Coverage:** Montgomery–Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, **Chapter 16 (Exponential Sums I: Van der Corput's Method)**: §16.1 exponential integrals, §16.2 elementary estimates, §16.3 Van der Corput's method, §16.4 notes, §16.5 references. **Transformed notes only — no raw text, no copied passages, no general book summary.** Book ID `BOOK-ANT-MONTGOMERY-MNT-II-004`. Local PDF outside git.

## Object

المجاميعُ والتكاملاتُ المتذبذبة:

```text
integral e(f(x)) dx        (exponential integrals, 16.1)
sum e(f(n))                (exponential sums, 16.2-16.3)
```

مع اختباراتِ الإلغاء المبنيّةِ على المشتقّات، **وتفريقِ van der Corput / متباينتِه الأساسيّة**، و**أزواجِ الأُسس (exponent pairs)** بوصفها خلاصاتِ إلغاءٍ قابلةً لإعادة الاستعمال. **طبقةُ دعمٍ** لما يستهلكه الفصلان 17 و18.

## Classical role (KNOWN, cited)

الفصلُ 16 يطوّر حدودَ المجاميع الأُسّيّة **باستغلال تذبذبِ الطور لا البنيةِ الحسابيّةِ للأوّليّات**: اختباراتُ المشتقّات، تقديراتُ الجمع/التكامل الابتدائيّة، تفريقُ van der Corput، وتحويلاتُ أزواج الأُسس. **معروفٌ، مُستشهَد.** آلةُ دعمٍ تستهلكها لاحقًا مجاميعُ الأوّليّات (Ch 17) والتطبيقاتُ الجمعيّة (Ch 18).

## Diagnostic role (support)

يشرحُ **أين يدخل الإلغاءُ قبل أن تُضاف البنيةُ الحسابيّة**، ويفصل ثلاثةَ أشياءَ يُخلَط بينها:

```text
oscillatory cancellation  ≠  prime detection  ≠  sieve extraction
derivative test           :  analytic cancellation certificate from phase variation
vdC differencing          :  shifted self-correlation / differencing for cancellation
exponent pair             :  reusable bound-profile for classes of exponential sums
```

`TOOL-MONTGOMERY-VDC-EXPONENTIAL-SUMS-DIAGNOSTIC-001`.

## PVG–ANT connection

بلغة PVG: الفصلُ 16 **لا يصنّف دعمَ التقييم أساسًا — بل يورّد شهادةَ إلغاءِ طورٍ تحليليّة**. يستطيع PVG تسميةَ مواضعِ تطبيق الاختبارات التذبذبيّة على مجاميعَ مفهرسةٍ بالتقييم، ويمكن قراءةُ تفريقِ van der Corput **مقارنةَ شرائحَ مُزاحةٍ من إشارةٍ حسابيّةٍ مفهرسة** — لكنّ **شهادةَ الإلغاء تبقى تحليليّةً**: لا يستبدل PVG اختباراتِ المشتقّات ولا تقديراتِ أزواج الأُسس.

جسرُ ANT: يركّب لغةَ الإلغاء التي يستهلكها `MNTII-006-F` (Ch 17: مجاميعُ الأوّليّات وType I/II) وتطبيقاتُ Ch 18 (عُدِّنت لاحقًا وحدةَ MNTII-006-H — ملاحظةٌ تاريخيّة)؛ دعمٌ جانبيٌّ من الملحق E (توافقيّات/مثلّثيّات) والملحق G (ثنائيّات/معايير) عند الحاجة — **الملاحقُ دعمٌ فقط، لا وحدات**.

## Frontier links

`FRONTIER-ANT-PVG-006` (التوزيع / مجاميع الأوّليّات) · `FRONTIER-ANT-PVG-004` (الغربلة — مستهلكٌ لاحقٌ downstream). **لا ربطَ بأيّ تقدّم RH/GRH، ولا ربطَ بجبهةِ off-diagonal/Kloosterman** إلّا إذا جاءت حزمةٌ مؤصَّلةٌ لاحقةٌ تفعل ذلك صراحةً.

## What it can diagnose

- أين يدخل الإلغاءُ التذبذبيُّ قبل البنية الحسابيّة، وكيف يتحوّل تغيّرُ الطور إلى شهادةِ إلغاء.
- ماذا يعني «زوجُ أُسس» بوصفه خلاصةَ قوّةِ إلغاءٍ قابلةً للنقل بين عائلاتِ مجاميع.
- لماذا تفريقُ van der Corput مقارنةُ شرائحَ مُزاحة، وما الذي يشتريه ذلك.
- الفرقَ الصريح بين الإلغاء التذبذبيّ وكشفِ الأوّليّات واستخراجِ الغربال.

## What it cannot prove

- **لا حدَّ جديدًا** لمجموعٍ أُسّيّ · **لا تحسينَ أزواجِ أُسس** · لا اختراقَ Type II.
- **لا يُحيي legacy-E**: موادُّ Kloosterman/Weil/Deshouillers–Iwaniec اللاقطريّة **تبقى محجورةً/مؤجَّلةً** حتى يأتي مصدرُها الصحيح — الفصلُ 16 لا يبرّر إعادتَها للمسار الموثوق.
- لا كسرَ تكافؤ · لا تحسينَ PNT/AP · **لا تطبيقَ Goldbach من هذه الوحدة** (سجلٌّ تاريخيّ: كان Ch 18 مؤجَّلًا عند إغلاقها ثمّ عُدِّن وحدةَ MNTII-006-H) · لا تقدّمَ RH/GRH.
- لا يحلّ `MC-001` (الإلغاءُ يغذّي حججَ الغربال لكنّه لا يجعلها كواشفَ أوّليّات) ولا `MC-005` (الإلغاءُ الأُسّيّ ليس تحكّمًا فرديًّا GRH/AP) ولا `MC-002`.

## Related walls

`WALL-OFF-DIAGONAL` · `WALL-SIEVE-CEILING` · `WALL-PARITY` · `WALL-DENSITY-HYP`. **لا يُعبَر أيٌّ منها.**

## Related missing certificates

`MC-001` — تبقى غيرَ محلولة. `MC-005` — تبقى غيرَ محلولة. `MC-002` — لا تُمَسّ ولا تُعَدُّ محلولة.

## Claim classification

**Diagnostic / Boundary (support unit).** آلةُ van der Corput وأزواجُ الأُسس **معروفةٌ (Known) ومُستشهَدةٌ للمصدر**؛ مخرجُ الوحدة تركيبُ لغةِ إلغاءٍ داعمةٍ للفصلين 17 و18، لا New Theorem ولا Candidate Mechanism ولا application closure.

## No-Go notes

```text
- PVG does NOT prove van der Corput estimates and does NOT improve exponent pairs.
- Ch 16 does NOT give a Type II breakthrough; van der Corput does NOT solve MC-001;
  exponential sums do NOT break parity.
- Ch 16 does NOT revive legacy-E: Kloosterman/Weil/Deshouillers-Iwaniec off-diagonal
  material is NOT now trusted; it stays quarantined/postponed until its correct source.
- Ch 16 gives NO Goldbach application (historical note: Ch 18 was later mined as the MNTII-006-H intake) and NO PNT/AP improvement.
- no new exponential-sum bound; no exponent-pair improvement; no RH/GRH progress.
- the Montgomery overlay is NOT closed (partial_overlay stands).
- no crossing WALL-OFF-DIAGONAL / WALL-SIEVE-CEILING / WALL-PARITY / WALL-DENSITY-HYP.
- MC-001, MC-002, MC-005 stay unsolved.
- no raw copyrighted text; transformed notes only.
```

## Intake / Validation note

```text
Created by SOURCE-GROUNDED intake from a ChatGPT Treasure Packet (Ch 16: Exponential Sums I —
Van der Corput's Method), after Sufyan's explicit selection (recorded at 4a042b5): stabilize the
support layer feeding Ch 17/18 BEFORE any additive (Ch 18) unit. Entered as validated_intake;
CLOSED after the second v0.6-G Closure Review (3 auditors PASS + falsifier unrefuted + 7/7 guards;
see audits/v0.6-g-closure.md). Guard focus of this packet: legacy-E is NOT revived by Ch 16.
```

## Next valid action

**Historical unit record.** MNTII-006-G was closure-reviewed (`v0.6-g-closure.md` PASS, second attempt). This file does not define the current live next action. The only authoritative live next action is: `transition-memory/next-action.md`.

## Audit checklist

- [x] Registry ID present · classification present (Diagnostic / Boundary, support unit)
- [x] SOURCE-GROUNDED from Treasure Packet (Ch 16, §16.1–16.5); transformed notes only
- [x] Known machinery recorded as Known; no new bound; no exponent-pair improvement; not a PVG result
- [x] legacy-E NOT revived (Kloosterman/Weil/off-diagonal stays quarantined/postponed)
- [x] No Goldbach application (historical checklist: Ch 18 later mined as MNTII-006-H); no Type II breakthrough; no parity break
- [x] No crossing WALL-OFF-DIAGONAL / WALL-SIEVE-CEILING / WALL-PARITY / WALL-DENSITY-HYP · MC-001/002/005 unsolved
- [x] Entered as validated_intake; CLOSED by v0.6-G Closure Review PASS (3 auditors + falsifier unrefuted)
- [x] TOOL-MONTGOMERY-VDC-EXPONENTIAL-SUMS-DIAGNOSTIC-001 registered; cards 044–051; planned.jsonl empty
- [x] MNTII-006-H not started at the time of this audit (historical record; later executed) · no full book mining · Seven guards PASS after this intake

**Ceiling:** Chapter-16 machinery enters as a KNOWN cancellation SUPPORT layer — derivative tests, van der Corput differencing, and exponent pairs are analytic certificates that PVG can label but cannot replace. No new bound, no exponent-pair improvement, no Type II breakthrough, no legacy-E revival, no Goldbach application, no PNT/AP improvement. MC-001/002/005 unsolved; walls uncrossed. No RH/GRH progress.
