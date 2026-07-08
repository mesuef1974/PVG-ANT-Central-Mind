# Book Ingestion Template

لإدخال كتابٍ جديدٍ كـ ledger (لا كتلخيص).

## الخطوات

1. أنشئ `03-ant-skill-ledgers/<book>-ledger/` مع `index.md`.
2. لكلِّ قسمٍ مهمّ: بطاقةٌ عبر `section-extraction-template.md`.
3. اربط الجدرانَ بـ `WALL-*` القائمة (أضِف جديدًا إلى `data/registry.jsonl` أوّلًا عند اللزوم).
4. الأدواتُ المكرَّرة عبر الكتب → إشارةٌ بـ ID، لا نسخة.
5. حدّث `04-pvg-bridges/*` إن أضاف الكتابُ ترجمةً جديدة.
6. سجّل الشهاداتِ الناقصةَ في `missing-certificates.md`.
7. شغّل `python tools/honesty_audit.py` → يجب PASS.
8. حدّث `99-transition-memory/latest-state.md`.

## index.md المطلوب لكلِّ كتاب

```text
# <Book> Ledger — Book NNN
Source:                 (Author, Title, ed.)
Honest classification:  Skill atlas / Diagnostic
Walls linked:           (جدول Overholt-style: book wall → WALL-ID)
Corrections on ingest:  (أيُّ تدقيقٍ صادقٍ على المصدر)
Next:
```

## قائمةُ الكتب المرشَّحة (حسب الأولويّة، عند الطلب)

Tenenbaum · Davenport (Multiplicative NT) · Montgomery–Vaughan · Iwaniec–Kowalski · Halberstam–Richert (Sieve Methods) · Friedlander–Iwaniec (Opera de Cribro) · Titchmarsh (Riemann Zeta).
