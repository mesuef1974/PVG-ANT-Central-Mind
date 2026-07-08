# PVG–ANT Central Mind

> **Canonical repository:** `D:\PVG-ANT-Central-Mind`.
> **Legacy duplicate:** the "The All" in-repo copy (`1b51886`) is **do-not-edit** unless explicitly reactivated.

مستودعُ عقلٍ رياضيّ تراكميّ حيّ. كلُّ كتابٍ أو مهارةٍ يدخل لا كنصٍّ خام، بل كـ **أدوات + قواعد + جدران + شهادات + بطاقاتِ واجهة**. طبقةٌ تشخيصيّة/تعليميّة: zero RH progress · zero GRH progress · no secured path.

المبدأ الحاكم: **الـmarkdown للعرض، والـJSONL للحقيقة، والحارس للإنفاذ** (graph لا pile).

## البنية (v0.1b — spec layout)

| مسار | المحتوى |
|---|---|
| `central-mind-charter.md`, `central-mind-goals.md` | الدستور والهدف الأعلى |
| `installed-skills/{math,governance}` | 14 بطاقةَ واجهةِ مهارة (الحوكمة أعلى سلطة) |
| `ledgers/books/` | Overholt (retrofit) · Tenenbaum (حتى 004-Z) · Mileti (planned) |
| `ledgers/imports/` | sieve · spectral-no-go · computational |
| `registries/` | مصدرُ الحقيقة (JSONL): skills · books · research-frontiers · open-questions-queue · walls · tools · rules · observables · claims · planned · registry(constraint) |
| `maps/` | skill-stack-map · skill-dependency-graph · query-routing-guide · current-capabilities · pvg-to-ant |
| `governance/` | claim-classification-matrix · certificate-funnel · book-import-protocol · what-not-to-import · no-go-memory · classification-system · honesty-policy · central-rules · missing/forbidden · templates |
| `audits/` | v0.1b-audit-checklist |
| `transition-memory/` | latest-state · next-action · compressed-prompt |
| `tools/` | ستّةُ حرّاس |
| `Books_others/` | **مكتبةُ PDF محلّيّة — مستبعَدةٌ من git** |

## الحرّاس

```bash
python tools/honesty_audit.py             # تصنيف + عبارات محظورة + سلامة السجلّات
python tools/registry_sync_audit.py       # كل ID في md موجود في السجلّ، لا تكرار
python tools/no_pdf_audit.py              # لا PDF متعقَّب
python tools/forbidden_promotion_audit.py # لا ترقية بلا شهادة
python tools/duplicate_concept_audit.py   # لا مفهوم مكرَّر
python tools/citation_audit.py            # كل سجلِّ كتابٍ موثَّقُ المصدر
```

## القانون النهائي

```text
No registry, no entry.  No classification, no claim.  No certificate, no theorem.
No audit, no release.  No RH/GRH progress without proof certificate.
```

## Roadmap

`v0.1b` Integration Pass 001 → `v0.2` Mileti Logic Certificate Layer → `v0.3` Tenenbaum-005-A Dirichlet characters. بلا tag · لا merge إلّا بمراجعة. المواصفةُ الكاملة: `PVG-ANT-Central-Mind-v0.1b-full-spec.md`.
