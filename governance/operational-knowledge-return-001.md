# P8 Operational Knowledge Return 001

```text
STATUS       = OPERATIONAL-KNOWLEDGE-RETURN
SOURCE CYCLE = I_r PRIORITY GATE / CLOSED
SCIENTIFIC CLAIM = NONE
GOAL CHANGE      = NONE
TARGET FREEZE    = NONE
REGISTRY CHANGE  = NONE

DEPOSIT STATUS   = DEPOSITED 2026-08-05
ORIGIN CYCLE     = mesuef1974/PVG-What-is (workspace for the closed I_r front)
```

---

## 1. الغرض

إعادة الأدوات والمسارات التشغيلية المكتسبة في دورة `I_r` إلى عقل المشروع، بحيث تصبح قابلة لإعادة الاستخدام في بوابات الأولوية اللاحقة.

هذه الوثيقة:

- لا تعيد فتح جبهة `I_r`.
- لا تعدّل `GOAL-PVG-ANT-STRATEGIC-001`.
- لا تعتمد المراجعة الاستراتيجية المقترحة.
- لا تفتح مشروعًا غير قطري أو مشروع انتظام في `q`.
- لا تصدر حكمًا علميًا جديدًا.

## 2. قاعدة المصادر

يُرتَّب الدليل وفق السلم الآتي:

```text
PRIMARY FULL TEXT
  > refereed paper metadata/review
  > authoritative bibliographic database
  > public dated mathematical record
  > secondary report
  > search snippet
```

ولا يجوز رفع نتيجة من طبقة أدنى إلى طبقة أعلى.

قواعد إلزامية:

```text
negative search result != proof of absence
metadata != theorem content
abstract != proof
dated public posting != refereed result
candidate identifier != verified endpoint
internal proof != externally certified proof
```

## 3. مسار OEIS — كشف الاصطدام المبكر

### 3.1 الاستخدام الصحيح

يُستخدم OEIS في بداية أي جبهة تخص دالة حسابية أو متتالية من أجل:

1. حساب قيم أولية قابلة لإعادة الإنتاج.
2. البحث بالقيم وبالصيغة المحلية عند القوى الأولية.
3. اختبار الضربية أو شبه الضربية.
4. مقارنة الدالة بمعادلات أو تعليقات الإدخال.
5. تسجيل تاريخ ظهور المدخل.
6. فصل هوية المتتالية عن مصدر براهين صيغها المقاربة.

**نقطة النهاية العملية:**

```bash
curl -sS "https://oeis.org/search?q=<comma-separated-values>&fmt=json"
curl -sS "https://oeis.org/search?q=id:A361430&fmt=json"
```

الحقول المفيدة: `data`، `name`، `formula`، `author`، `created`، `keyword`، `reference`، `link`.

### 3.2 ما يجوز استنتاجه

يجوز أن يثبت OEIS:

- وجود سجل عام مؤرَّخ.
- تطابقًا عدديًا أوليًا يحتاج برهانًا.
- صيغةً مقترحة تستحق التحقق.
- إحالات ببليوغرافية أولية.

ولا يجوز أن يثبت بمفرده:

- صحة صيغة مقاربة.
- أصالة مبرهنة.
- وجود برهان منشور.
- مرتبة تحكيمية مساوية لورقة محكّمة.

### 3.3 بروتوكول الهوية

عند الاشتباه في تطابق دالتين ضربيتين:

```text
1. compare prime-power values exactly
2. prove equality on p^e
3. invoke multiplicativity
4. classify as IDENTITY, not FINITE-VERIFIED
5. audit the entry's proof provenance separately
```

المثال المستعاد من الدورة:

```text
I_1 = A361430
```

وهوية الدالتين ثبتت من القيم على القوى الأولية والضربية، لا من المطابقة العددية وحدها.

## 4. مسار zbMATH Open — الفرز الببليوغرافي

### 4.1 الوظيفة

يُستخدم zbMATH Open من أجل:

- تثبيت هوية الورقة أو الكتاب.
- الحصول على `Zbl` والبيانات الببليوغرافية.
- قراءة مراجعة المحرر أو المراجع لتحديد نطاق المصدر.
- تتبع الطبعات المتكافئة أو المعاد طبعها.
- فرز سلسلة أوراق طويلة قبل فتح النصوص.

**نقطة النهاية العملية** — مفتوحة، بلا اشتراك:

```bash
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=au:Knopfmacher,%20John&results_per_page=25"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=an:0322.10001&results_per_page=1"
```

قيدان عمليان لوحظا في الدورة: الاستعلامات الحرة المركّبة تُرجع نتيجة فارغة، فتُستعمل صيغة الحقول (`au:`، `an:`، `ti:`)؛ وبعض نصوص المراجعات محجوبة برسالة `contents unavailable due to conflicting licenses`.

### 4.2 حدود الأداة

مراجعة zbMATH تساعد على تحديد:

```text
which source to read first
what the source is broadly about
whether an edition is equivalent
which cited predecessor is likely governing
```

لكنها لا تسمح باستنتاج:

```text
exact theorem hypotheses
exact error exponent
multi-layer versus one-layer extraction
uniformity in parameters
absorption verdict
```

كل حكم من هذه الأحكام يحتاج نص المبرهنة أو مصدرًا أوليًا ناقلًا لها بدقة.

### 4.3 مخرج الفرز المطلوب

لكل مصدر:

```text
bibliographic identity
review identifier
declared scope
priority rank
full-text status
reason for reading or skipping
content claims not yet verified
```

## 5. مسار GDZ وIIIF — استعادة المصادر المصوّرة

### 5.1 نقطة الدخول

تُفحص بنية المجلد أولًا عبر IIIF Presentation Manifest:

```text
https://gdz.sub.uni-goettingen.de/iiif/presentation/{WORK_ID}/manifest
```

يحمل `structures` جدول محتويات المجلد، ويمكن أن يحتوي كل مقال على `rendering` خاص به.

مسار PDF:

```text
https://gdz.sub.uni-goettingen.de/download/pdf/{DOCUMENT_ID}/{STRUCTURE_ID}.pdf
```

مسار صورة صفحة مفردة — لازم عندما يخلو الـPDF من طبقة نص:

```text
https://images.sub.uni-goettingen.de/iiif/image/gdz:{DOCUMENT_ID}:{CANVAS}/full/1600,/0/default.jpg
```

حيث `{CANVAS}` يُقرأ من الـmanifest، ولا يُخمَّن.

مثال الدورة:

```text
DOCUMENT_ID   = PPN243919689_0254
STRUCTURE_ID  = LOG_0008
PRINTED PAGES = 74–99
CANVASES      = 00000078 … 00000103
TEXT LAYER    = ABSENT
```

### 5.2 بروتوكول الحل

```text
1. retrieve manifest
2. inspect structures
3. identify article label and printed pages
4. record structureId
5. map canvases from manifest, not by guessed offset
6. inspect rendering link
7. determine whether PDF has a text layer
8. if image-only, read through IIIF canvases
```

لا يجوز نقل فرق أرقام المسح من مجلد إلى مجلد آخر دون تحقق من الـmanifest.

### 5.3 القيد القانوني

عندما تمنع شروط المصدر إعادة الإيداع:

```text
DO NOT COMMIT:
  article PDF
  page images
  derived image archive

COMMIT ONLY:
  identifiers
  retrieval recipe
  page references
  short compliant quotations
  extracted theorem statements in paraphrase
```

وتُضاف مسارات التنزيل المحلية إلى `.gitignore` عند الحاجة.

## 6. بروتوكول قراءة المبرهنات

لكل مبرهنة تُستخرج الحقول الآتية:

```text
source and page
statement number
exact hypotheses
main terms
number of distinct powers
log-polynomial degree at each power
error term
parameter dependence
uniformity range
dependencies on earlier lemmas
classification
```

ويجب التمييز صراحةً بين:

$$x^{\delta}P(\log x)$$

الناتج من قطب واحد متعدد الرتبة، وبين:

$$\sum_j x^{\lambda_j}P_j(\log x)$$

الناتج من متفردات عند مواضع مختلفة.

**كثير حدود كامل في `log x` عند قوة واحدة لا يُسمى «استخراج عدة طبقات قوى».**

## 7. بروتوكول بوابة الأولوية

قبل محاولة البرهان:

```text
P0 — define the exact claim
P1 — identify nearest classical objects
P2 — search sequence/function databases
P3 — search primary literature
P4 — read governing theorem text
P5 — compare hypotheses and output term by term
P6 — issue one verdict
```

الأحكام المسموحة:

```text
ABSORBED
PARTIALLY ABSORBED
NOT ABSORBED IN THIS SOURCE
TARGET-WORTH-FREEZING
ACCESS-STILL-BLOCKED
NOT DETERMINED
CORRECT BUT ROUTINE
```

ولا يُجمَّد هدف عند:

```text
source unread
proof provenance unresolved
nearest analogue not audited
only fixed-parameter evidence available
published uniformity bar not identified
```

## 8. دروس تشغيلية من الدورة المغلقة

### 8.1 البحث عن الأقرب قبل الأعم

البدء من الكائن الحسابي الأقرب أكثر كفاءة من البحث عن المصطلح الجديد الذي وضعه المشروع.

في دورة `I_r` كان المسار الفعّال:

```text
observable values
→ OEIS identity
→ mother family J_k
→ classical squarefull/powerful literature
→ general arithmetical-semigroup theorems
```

### 8.2 فصل صحة البرهان عن قيمة المساهمة

ينبغي أن يحمل كل ملف حقلين مستقلين:

```text
MATHEMATICAL VALIDITY
PRIORITY / CONTRIBUTION STATUS
```

وقد تكون الحالة:

```text
VALIDITY     = CORRECT INTERNALLY
CONTRIBUTION = FAILED / ROUTINE
```

من دون سحب البرهان أو ترقيته.

### 8.3 الأولوية تسبق التوسيع

لا يُفتح تعميم لعائلة كاملة قبل فحص:

- العضو الأول.
- العائلة الأم.
- أقرب دالة كلاسيكية.
- أقرب مبرهنة نقل عامة.
- أقوى نسخة منتظمة في الوسائط.

### 8.4 لا يُحوَّل حاجز صحيح تلقائيًا إلى فجوة بحثية

قد يكون الحاجز:

```text
real
correctly derived
structurally informative
already known
already bypassed in a specialised setting
```

لذلك يلزم فحص تاريخ المعالجة، لا مجرد إثبات وجود الحاجز.

## 9. الأدوات المكتسبة

```text
OEIS:
  early sequence collision detection
  dated-public-record verification
  identity/provenance separation

zbMATH Open:
  reviewer-level source triage
  edition-equivalence checks
  primary-source routing

GDZ IIIF:
  volume structure discovery
  article structureId resolution
  canvas/page mapping
  image-only source reading

GitHub:
  immutable gate reports
  correction commits rather than silent rewrites
  explicit supersession and source-of-truth control
```

## 10. معايير قبول العودة

تُعد المعرفة التشغيلية مُعادة عندما:

```text
[x] توجد وصفة قابلة لإعادة الإنتاج لكل أداة
[x] حدود كل أداة منصوص عليها
[x] لا تُنقل ادعاءات علمية غير محققة
[x] تُفصل الهوية عن البرهان وعن الأولوية
[x] تُفصل صحة النتيجة عن كونها مساهمة
[x] تُسجل القيود القانونية للمصادر
[x] لا تُعدّل غاية أو سجل برنامج
[x] لا يُفتح هدف بحثي جديد
```

## 11. السقف

```text
This is operational knowledge, not a scientific result.
No goal amended.
No target frozen.
No successor project opened.
No RH progress. No GRH progress.
```
