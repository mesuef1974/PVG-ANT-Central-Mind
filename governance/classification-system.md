# Classification System — the ten stamps

كلُّ مخرجٍ يحمل ختمًا من هذه المجموعة المغلقة. أيُّ ملفٍّ/سجلٍّ بلا تصنيفٍ يفشل في الحارس.

| Stamp | التعريف | يتطلّب Certificate؟ |
|---|---|---|
| **Known** | نتيجةٌ/أداةٌ كلاسيكيّةٌ من مصدرٍ مدرسيّ | مرجع |
| **Identity** | مساواةٌ جبريّة/تحليليّةٌ مضبوطة | اشتقاق |
| **Reinterpretation** | لغةٌ/قراءةٌ جديدةٌ لمعلومةٍ معروفة | لا يُرقّى بلا برهانٍ مستقلّ |
| **Diagnostic** | تسميةُ جدارٍ أو موضعِ عجز | — |
| **Boundary** | حدُّ ما تستطيع الأداةُ إثباته | — |
| **Open Problem** | مسألةٌ مفتوحة (RH/GRH/Artin) | — |
| **Candidate Mechanism** | آليّةٌ محتملة تحتاج برهانًا واختبارًا | **إلزاميّ + اختبار** |
| **New Theorem** | برهانٌ كاملٌ ومراجعةٌ حقيقيّة فقط | **إلزاميّ + peer review** |
| **Missing Certificate** | شهادةٌ ناقصة — **ليست نتيجة** | — |
| **Forbidden Claim** | ادّعاءٌ محظور (يُوثَّق منفيًّا فقط) | — |

## قواعد الترقية

- `Reading → Diagnostic`: مسموحٌ دائمًا.
- `Diagnostic → Candidate Mechanism`: صياغةٌ قابلةٌ للتكذيب + شهادةٌ جزئيّة.
- `Candidate → New Theorem`: برهانٌ كامل + مراجعةٌ خارجيّة — **لا يقوم به العقلُ وحده**.
- أيُّ ترقيةٍ نحو RH/GRH ممنوعة (خارجُ السقف).

## للسجلّات (registries/)

- `wall/tool/rule/identity/diagnostic/observable/constraint/claim` → حقلُ `classification` من المجموعة أعلاه.
- `book` → حقلُ `status`. القيمُ المستعملة فعلًا: `available` · `retrofitted` · `in_progress_through_004Z` · `planned_v02_seed` (وعامّةً `planned`/`in_progress`/`ingested`/`closed` عند الحاجة).
- `frontier` → `status` (`open`/`queued`) · `question` → `status` (`queued`) · `planned` → `status` (`planned`).
