# Walls Registry — human view

عرضٌ بشريٌّ لـ`walls.jsonl` (مصدر الحقيقة). الجدرانُ متناهيةٌ وتتكرّر عبر الكتب؛ حين يتوقّف هذا السجلُّ عن النموّ بينما تثرى الأدوات، يكون العقلُ graph لا pile.

| ID | البيان | تصنيف |
|---|---|---|
| `WALL-PARITY` | الغرابيلُ تعدّ almost-primes أفضلَ من primes | Diagnostic |
| `WALL-MINOR-ARC` | major arcs يجب أن تُقابَل بإلغاءٍ على minor arcs | Boundary |
| `WALL-ZERO-FREE` | الخطأُ القويّ يتطلّب منطقةً خاليةً من الأصفار | Boundary |
| `WALL-SIEGEL` | الأصفارُ الاستثنائيّة → ineffectivity وانحياز | Diagnostic |
| `WALL-POSITIVITY-WEIL` | RH ⟺ إيجابيّةُ Weil؛ الصيغُ الصريحة تنقل لا تحدّد | Open Problem |
| `WALL-ARTIN` | دوالُّ Artin تتطلّب holomorphy + zero-control | Open Problem |
| `WALL-LINDELOF` | حدُّ التحدّب/Lindelöf | Boundary |
| `WALL-SIEVE-CEILING` | لا غربالٌ غيرُ مشروطٍ يبلغ RH؛ EH وحده | Boundary |
| `WALL-OFF-DIAGONAL` | اللاقطريُّ متميّزٌ عن خطأ PNT وعن parity | Diagnostic |
| `WALL-DENSITY-HYP` | قاعُ OP-001: فرضيّةُ الكثافة | Open Problem |
| `WALL-HURWITZ-CONV` | تقاربُ Hurwitz نحو Ξ | Open Problem |
| `WALL-PHASE` | الطورُ (Halász/pretentious): إلغاءٌ فقط عند بُعدِ الطور عن n^{it} | Boundary |
| `WALL-AVERAGE-NORMAL` | المتوسّطُ لا يُلزِم الرتبةَ الطبيعيّة | Boundary |

## ثابتٌ مفروض

`CONSTRAINT-NO-CONFLATION`: RH ≠ PNT-error ≠ off-diagonal ≠ parity. أربعةُ جدرانٍ لا تُخلَط.

**ملاحظة:** `WALL-PHASE` و`WALL-AVERAGE-NORMAL` دخلا السجلَّ مع إدخال Tenenbaum حتى 004-Z (Integration Pass 001)؛ مصدرُهما `tenenbaum-002`.
