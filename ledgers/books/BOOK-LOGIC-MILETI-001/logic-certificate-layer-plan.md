# Logic Certificate Layer — Plan

Book ID: `BOOK-LOGIC-MILETI-001`. خطّةُ v0.2-A. **لا قراءةَ Mileti قبل تجميد هذا النطاق.** لا نصَّ خام؛ ملاحظاتٌ محوَّلةٌ فقط عند التنفيذ.

## Pipeline (لكل وحدة)

```text
1. section-extraction عبر governance/section-extraction-template.md  (ملاحظات محوّلة، لا نص كتاب)
2. إنتاج بطاقة الوحدة في هذا المجلد (mileti-001-<x>-*.md) بحقل Registry IDs
3. ترقية المعرِّف من registries/planned.jsonl إلى registries/{rules,tools}.jsonl
4. تحديث status الكتاب في books.jsonl -> in_progress
5. تشغيل tools/ (الستة) -> PASS
6. تحديث transition-memory/latest-state.md
```

## Certificate-layer purpose

كلُّ وحدةٍ تُحدّد مستوًى من دلالة الشهادة:
- **A** الصورنة (claim ≠ formula ≠ truth ≠ deduction ≠ certificate) → `RULE-LOGIC-001`.
- **B** نحو مقابل دلالة → `RULE-LOGIC-002`.
- **C** ما-وراء-نظريّة مقابل نظريّة صوريّة → `RULE-LOGIC-004`.
- **D** بنية مولَّدة (induction/recursion) → `TOOL-GENERATION-001`.
- **E** الاستنتاج ككائنِ شهادةٍ منتهٍ قابلٍ للفحص → `TOOL-DEDUCTION-SYSTEM-001` + `RULE-LOGIC-003` (proof≠deduction≠verification≠certificate). يربط بـ`certificate-ledger` وحارس Lean.

## Sequencing

v0.2-A (A→E) → v0.2-B (§3.6–3.7 soundness/completeness/compactness) → ثمّ v0.3 = Tenenbaum-005-A. لا تجاوزَ قبل PASS كلِّ مرحلة.

## Ceiling

soundness/completeness ليست RH؛ عدمُ الاكتمال (Ch12، مؤجَّل) طُعمٌ كاذبٌ لـRH (Π₁) — يُسجَّل كـ`Missing Certificate` (`CLAIM-PI1-RH-001`) لا كنتيجة.

**Honest classification:** Diagnostic (plan, planned). No RH/GRH progress. No proof-system overclaim.
