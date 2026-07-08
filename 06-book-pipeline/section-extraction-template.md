# Section Extraction Template

كلُّ قسمٍ من كتابٍ يتحوّل إلى بطاقةٍ بهذه البنية — لا تلخيصٌ نثريّ. انسخ واملأ.

```text
Source:                  (كتاب — Author, Title, ed.)
Section:                 (Ch-Unit — عنوان)
Object:                  الكائنُ الرياضيّ المركزيّ
Identity:                الهويّة/الصيغةُ الأساسيّة
Tool:                    الأداةُ التي أضافها القسم
Main term:               الحدُّ الرئيسيّ ومصدرُه (القطب/البنية)
Error:                   مصدرُ الخطأ (أصفار/قطع/minor arcs/conductor-gamma)
Wall:                    WALL-ID من walls-registry (أو جديدٌ يُضاف أوّلًا لـ registry.jsonl)
Treasure:                القانونُ المفهوميّ الذي يُحفَظ
PVG Geometry:            القراءةُ بلغة PVG (support/height/phase/fiber)
ANT Analysis:            الأداةُ التحليليّةُ المقابلة
Certificate:             النظريّة/الحدُّ المُثبِت (أو "missing → MC-ID")
PVG Rule:                القاعدةُ التشغيليّةُ المستخرَجة (أو "none new")
Honest Classification:   Known/Identity/Tool/Reinterpretation/Diagnostic/Boundary/Open/Candidate/Theorem
Next Action:             الوحدةُ التالية
```

## قواعد الإدخال (idempotent)

1. أداةٌ موجودةٌ في `registry.jsonl` → أشِرْ إليها عبر ID، لا تكرّرها.
2. جدارٌ جديد → أضِفه إلى `registry.jsonl` أوّلًا، ثمّ استعمل ID.
3. كلُّ بطاقةٍ تحمل `Honest Classification:` غيرَ فارغ (يفرضه الحارس).
4. `Main term` بلا `Certificate`/قطب → مرفوض.
