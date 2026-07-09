# Book Treasure Extraction Protocol 001

Registry ID: TREASURE-EXTRACTION-PROTOCOL-001 · Status: Active Governance · Classification: Governance / Extraction Policy.

> **ملاحظة معرِّف:** البادئةُ `TREASURE-` من قائمة الـ self-ids الآمنة (غير متتبَّعة بـ`registry_sync`)؛ لا تُعطِ وثيقةَ حوكمةٍ بادئةَ `BOOK-` (تلك للكتب المسجَّلة في `books.jsonl` فقط).

## Governing statement

```text
A book is not imported as a summary.
A book is not imported as raw text.
A book is MINED for mathematical treasures.

Book import means: deep treasure extraction + normalization into the Central Mind.
It does NOT mean: raw copying, full-text import, or a complete-mastery claim.
But it DOES mean: we actively search for every important mathematical treasure in the book
and either integrate it, queue it, or explicitly mark it as deferred.
```

هذا يصحّح صياغةً أضيقَ سابقة: لسنا في «تلخيصٍ انتقائيٍّ خفيف» ولا «نسخٍ كاملٍ للكتاب». الممنوعُ **النسخُ الخام**، لا **الاستخراجُ العميق**.

## What a "treasure" is

كلُّ فكرةٍ أو أداةٍ أو بنيةٍ أو مبرهنةٍ أو طريقةٍ أو حدٍّ أو مثالٍ كاشفٍ قد يغيّر قدرةَ العقل على التفكير أو التشخيص أو الربط بين PVG وANT. المعيارُ ليس «هل تخدم الوحدةَ الحاليّة؟» بل **«هل فيها كنزٌ رياضيٌّ/تشغيليٌّ يجب ألّا يضيع؟»**.

## Three layers per book

```text
Layer 1 — Treasure Extraction : استخراج الكنوز الرياضية من الكتاب.
Layer 2 — Normalization       : تطبيعها إلى لغة العقل (الأنواع أدناه).
Layer 3 — Integration         : ربطها بالمهارات والجبهات والسجلات والخرائط الحية.
```

## What to extract (deeply — every treasure, not every word)

```text
1. التعاريف المؤسِّسة            9.  الصيغُ المولِّدة للأدوات
2. المبرهنات المحوريّة          10. المقارناتُ بين الطرق
3. اللِّمّاتُ الحاملةُ لتقنية      11. علاقاتُ الدوال/السلاسل/الجداءات/الغربلة
4. الطرقُ المتكرِّرة             12. أيُّ فكرةٍ تصلح قاعدةَ تشغيل
5. الأمثلةُ الكاشفةُ للبنية       13. أيُّ فشلٍ منهجيٍّ مهمّ
6. التمارينُ ذاتُ الفكرة غير العاديّة  14. أيُّ no-go أو تحذيرِ مبالغة
7. الحدودُ والجدران              15. أيُّ نقطةٍ تصلح سؤالًا بحثيًّا مفتوحًا
8. الشهاداتُ الناقصة
```

## What NOT to import (unchanged ceiling)

raw text · full pages · verbatim quotes · PDF in git · prompt dumps · literal summary · complete-mastery claim · any RH/GRH progress. **الكنزُ يُطبَّع لا يُنسَخ.**

## Normalization targets

كلُّ كنزٍ يُطبَّع إلى واحدٍ أو أكثر من:

```text
Object · Identity · Tool · Observable · Diagnostic · Wall · Missing Certificate ·
Rule · Frontier Question · No-Go Memory · Skill Capability
```

## Extraction levels (ladder)

```text
Level 0 — Registry only        : الكتاب مسجَّل فقط.
Level 1 — Scope only           : نطاقٌ محدَّد، لا قراءة.
Level 2 — Diagnostic extraction: أدوات/جدران/شهادات.
Level 3 — Operational skill     : تحويل المحتوى إلى مهارات وقواعد تشغيل.
Level 4 — Proof-level           : براهين تفصيليّة والتحقّق منها (proof pass مستقلّ).
Level 5 — Mastery ledger        : تغطيةٌ شاملةٌ للفصول والتمارين والبراهين.
```

**التطبيقُ المستهدَف:** تعدينُ الكنوز يرفع كلَّ كتابٍ إلى **Level 3+** (كلُّ كنزٍ مطبَّعٌ)، مع تأجيلِ Level 4/5 (proof/mastery) بعلامةٍ صريحة. الطبقاتُ المُغلَقة سابقًا (Overholt/Tenenbaum/Mileti/IK/Harman) صُنِّفت غالبًا Level 2–3؛ **تحتاج retrofit** بملفّات الكنوز.

## Required per-book files (going forward + retrofit)

```text
treasure-map.md          : جدولُ الكنوز المستخرَجة والمطبَّعة.
normalization-ledger.md  : ربطُ كلِّ كنزٍ بمخرجه المطبَّع (Registry IDs).
missed-treasures.md      : الكنوزُ غيرُ المستخرَجة بعد + لماذا (مؤجَّلة أم غير لازمة). صدقٌ إلزاميّ.
```

## treasure-map.md card template

```text
Treasure ID:            (TREASURE-<BOOK>-<UNIT>-<n>)
Source location:        (chapter/section — no verbatim text)
Treasure type:          (one of the 15 categories)
Mathematical content:   (the idea/technique, transformed — not copied)
Why it matters:
PVG translation:
ANT role:
Certificate status:
Related wall:
Related missing certificate:
Normalized output:      (Registry IDs it becomes)
Claim classification:   (Known/Identity/Tool/Observable/Diagnostic/Boundary/Missing Certificate/...)
Next action:
```

Example:

```text
Treasure ID: TREASURE-HARMAN-004-A-001
Type: Sieve Information Shape
Content: a prime-detecting sieve consumes structured Type-I / Type-II information.
PVG translation: the sieve sees support geometry but needs external bilinear information.
Wall: WALL-PARITY   Missing Certificate: MC-001
Classification: Diagnostic / Boundary
Normalized output: TOOL-SIEVE-INFO-CONSUMPTION-001
```

## The honesty file: missed-treasures.md

الصدقُ يقتضي أن نعرف **ما الكنوزُ التي لم تُستخرَج بعد، ولماذا، وهل هي مؤجَّلةٌ أم غيرُ لازمة**. لا كتابٍ يُوصَف «كنوزُه مستخرَجةٌ كاملةً» دون هذا الملفّ.

## Ceiling (unchanged)

zero RH progress · zero GRH progress · no secured path. التعدينُ العميقُ لا يرفع السقف: الكنوزُ تُطبَّع إلى تشخيصٍ/أداةٍ/شهادةٍ ناقصة، لا إلى نتائجَ أو براهينَ أو تجاوزِ جدران. الصياغةُ الدائمة: **the book is imported as a bounded, deeply-mined operational ledger — not a complete-mastery claim.**

**Honest classification:** Governance / Extraction Policy. No RH/GRH progress.
