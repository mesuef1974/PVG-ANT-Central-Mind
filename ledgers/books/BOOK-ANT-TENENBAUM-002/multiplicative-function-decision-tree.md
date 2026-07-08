# Multiplicative Function — Decision Tree

شجرةٌ لاختيار الشهادة الصحيحة لمتوسّطِ دالةٍ ضربيّة. الهدف: منعُ ادّعاء «عشوائيّة» قبل اختبار الطور.

> **نطاق:** مرجعٌ معروفٌ (Known). الأدواتُ المذكورة مسجَّلةٌ الآن في `registries/tools.jsonl` بعد إدخال Tenenbaum حتى 004-Z: `TOOL-HALASZ-001` · `TOOL-SELBERG-DELANGE-001` · `TOOL-WIRSING-001` · `TOOL-DELANGE-001`.

```text
f multiplicative?
├── no  → ليست هنا؛ استعمل additive-observable-card أو أدوات خاصّة.
└── yes
    ├── f ≥ 0 ?
    │   ├── yes → Wirsing / Selberg–Delange (إن F(s)=ζ(s)^z G(s))
    │   └── no  → متابعة
    ├── |f| ≤ 1 ?
    │   ├── yes → Halász (المسافة إلى n^{it})
    │   └── no  → طبِّع أو استعمل moments
    ├── f(p) قريبةٌ من 1 ?         → Selberg–Delange (ζ(s)^z)
    ├── f(p) قريبةٌ من p^{it} ?    → Halász distance صغيرة → لا إلغاء
    └── F(s) = ζ(s)^z G(s) ?      → Selberg–Delange مع z المناسب
```

## الشهادات وحدودها

| الحالة | الشهادة | الجدار |
|---|---|---|
| `f≥0`, قطبٌ نظيفٌ عند 1 | Ikehara / Wirsing | Tauberian لا يعطي معدّلًا |
| `|f|≤1` | Halász | المسافةُ الكبيرةُ لا تُثبت RH |
| `F=ζ^z G` | Selberg–Delange | يتطلّب امتدادًا ومنطقةً خاليةً |

**PVG rule:** الطورُ يُختبَر قبل ادّعاء العشوائيّة (phase misalignment = Halász distance). عدمُ اختبارِ الطور ثمّ ادّعاءُ الإلغاء = ادّعاءٌ محظور.

**Honest classification:** Tool / Diagnostic.
