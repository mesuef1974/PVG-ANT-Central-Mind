# PVG–ANT Central Mind

مستودعُ عقلٍ رياضيّ تراكميّ حيّ. كلُّ كتابٍ أو مهارةٍ يدخل لا كنصٍّ خام، بل كـ **أدوات + قواعد + جدران + شهادات + بطاقاتِ واجهة**. طبقةٌ تشخيصيّة/تعليميّة: zero RH progress · zero GRH progress · no secured path.

## Layers

| مجلّد | المحتوى |
|---|---|
| `00-kernel/` | الدستور، الصدق، التصنيف (10 ختوم)، القواعد، ما-لا-يُستورَد |
| `01-registries/` | مصدرُ الحقيقة (JSONL): walls · tools · rules · books · observables · claims · skills · planned · constraint |
| `02-diagnostic-cards/` | بطاقاتُ القرار والتشخيص |
| `03-skill-ledgers/` | installed-skills (14 بطاقة) · ant (Overholt، Tenenbaum) · logic (Mileti planned) · sieve · spectral · computational |
| `04-bridges/` | pvg-to-ant · skill-stack-map |
| `05-certificate-ledger/` | missing · forbidden · (known/identities/diagnostics/boundaries) |
| `06-book-pipeline/` | قوالبُ الإدخال والإغلاق |
| `tools/` | ستّةُ حرّاس |
| `99-transition-memory/` | الحالة · الفعل التالي · القدرات · compressed-prompt |
| `Books_others/` | **مكتبةُ PDF محلّيّة — مستبعَدةٌ من git** |

## المبدأ الحاكم

الـmarkdown للعرض، والـJSONL للحقيقة، والحارس للإنفاذ. graph لا pile.

## الحرّاس

```bash
python tools/honesty_audit.py            # تصنيف + عبارات محظورة + سلامة السجلّات
python tools/registry_sync_audit.py      # كل ID في markdown موجود في السجلّ، لا تكرار
python tools/no_pdf_audit.py             # لا PDF متعقَّب
python tools/forbidden_promotion_audit.py# لا ترقية بلا شهادة
python tools/duplicate_concept_audit.py  # لا مفهوم مكرَّر
python tools/citation_audit.py           # كل سجلِّ كتابٍ موثَّقُ المصدر
```

## Roadmap

`v0.1b` Integration Pass 001 (المهارات + Overholt + Tenenbaum→004-Z) → `v0.2` Mileti Logic Certificate Layer → `v0.3` Tenenbaum-005-A Dirichlet characters.

## Governance

مستودعٌ مستقلّ · بلا tag · لا merge إلّا بمراجعة (`research-release-governance`).

