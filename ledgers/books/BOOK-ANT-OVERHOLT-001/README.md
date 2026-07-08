# Overholt Ledger — Book 001

**Source:**
Marius Overholt, *A Course in Analytic Number Theory*, AMS GSM 160.
Book ID: `BOOK-ANT-OVERHOLT-001`.
Local source present outside git in `Books_others/`. PDF excluded by `.gitignore`. Transformed notes only, no book text.

```text
Status:         retrofitted from a prior ANT Skill Ledger.
Role:           baseline ANT training source.
Classification: known textbook-derived skill extraction + PVG diagnostic reinterpretation.
Scope:          partial — only what was actually extracted below is represented.
                NOT "complete mastery", NOT "fully absorbed", NOT a source of new theorems.
```

**Honest classification:** Skill atlas / Diagnostic. No RH/GRH progress.

## المحتوى

- `ledger-summary.md` — الفهرسُ النهائيّ: 10 فصول (Ch1–Ch10) + وحدةُ تدريب، القوانين والهويّات والجدران وقواعد نقل PVG.
- `overholt-ledger.json` — البيانات المنظَّمة للفصول.
- `overholt-problem-templates.md` — 10 قوالبِ حلٍّ عمليّة.

## الربطُ بالسجلّات المركزيّة (graph not pile)

جدرانُ Overholt الستّة **موصولةٌ** بسجلِّ الجدران الموحَّد، لا مكرَّرة:

| Overholt wall | → Central wall ID |
|---|---|
| Parity | `WALL-PARITY` |
| Minor-arc | `WALL-MINOR-ARC` |
| Zero-free | `WALL-ZERO-FREE` |
| Siegel-zero | `WALL-SIEGEL` |
| RH/GRH (explicit formula) | `WALL-POSITIVITY-WEIL` |
| Artin | `WALL-ARTIN` |

## تصحيحان عند الإدخال (تدقيقٌ صادق)

1. الكتابُ **عشرةُ فصول** لا أحد عشر. «Ch11 Supplementary Exercises» في الفهرس وحدةُ تدريبٍ خارجَ ترقيم الكتاب، لا فصلٌ حقيقيّ.
2. الحزمةُ الأصليّةُ بلا frontmatter؛ هنا أُدرِجت كـ ledger داخليّ لا كـskill مستقلّ، فلا حاجة لذلك.

## Registry IDs produced

`TOOL-EULER-PRODUCT-001` · `TOOL-MOBIUS-001` · `TOOL-HYPERBOLA-001` · `TOOL-PERRON-001` · `TOOL-CHARACTER-ORTHOGONALITY-001` · `OBS-OMEGA-001` · `OBS-BIGOMEGA-001` · `OBS-MOBIUS-001` · `OBS-LIOUVILLE-001` · `OBS-CHARACTER-001`.

## Next

بطاقاتُ الدوال (μ, λ, squarefree) مسجَّلةٌ في `registries/observables.jsonl`؛ توسيعُها عند الطلب.
