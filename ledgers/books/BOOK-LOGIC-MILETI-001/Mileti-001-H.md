# Mileti-001-H — Compactness

**Registry ID:** MILETI-001-H
**Status:** Ingested (v0.2-B, layer-closing unit)
**Classification:** Known logic framework + **Governance / Certificate Discipline** (not theorem, not proof machinery)

**Source Coverage:** Mileti, *Modern Mathematical Logic*, §3.7 Compactness and Applications (p94) — **§3.7 only**. Book ID `BOOK-LOGIC-MILETI-001`. **Transformed notes only — no raw text, no general book summary.** Local PDF outside git.

## Object

المبدأُ المحلّيّ→الكلّيّ لقابليّة الإرضاء: `satisfiable ⟺ every finite subset satisfiable`.

## Identity / Concept

```text
Compactness: a set of sentences is (globally) satisfiable
             iff every finite subset is satisfiable.
```

بلغة الشهادة: **قابليّةُ الإرضاء الكلّيّةُ تُشهَد عبر قابليّة الإرضاء المنتهية** داخل الإطار المنطقيّ المعتمَد.

## Compactness anatomy (required)

```text
1. Finite satisfiability      : كلُّ مجموعةٍ جزئيّةٍ منتهيةٍ لها نموذج.
2. Global satisfiability      : للمجموعة كاملةً نموذج.
3. Local-to-global certificate: (1) لكلِّ منتهٍ ⟹ (2) للكلّ — هذه هي الشهادة.
4. Model existence boundary   : النموذجُ الناتجُ موجودٌ لكنّه قد يكون غيرَ قياسيّ (nonstandard).
5. What compactness certifies : وجودَ نموذجٍ ما يُرضي كلَّ الجُمَل (existence of satisfiability).
6. What compactness does NOT certify : صدقًا في البنية المقصودة؛ ولا يحلّ مسألةً مفتوحة؛ ولا يميّز النموذجَ القياسيَّ من غيره.
```

## Tool

`TOOL-COMPACTNESS-001` — أداةُ حوكمة/شهادةٍ للانتقال المحلّيّ→الكلّيّ في الإرضاء، لا آلةَ حلٍّ للمسائل المفتوحة.

## Certificate Function

يمنح شهادةَ وجودٍ كلّيّةً من فحوصٍ منتهية — لكنّها شهادةُ **إرضاءٍ (وجودُ نموذج)** لا شهادةُ **صدقٍ في البنية المقصودة**.

## PVG–ANT Use

7. **فحوصُ السجلّ المنتهية مقابل الادّعاءات الكلّيّة:** اجتيازُ فحوصٍ منتهيةٍ على سجلٍّ/مرصدٍ يشهد بإرضاءٍ منتهٍ، لا بحقيقةٍ لانهائيّةٍ في البنية المقصودة. الانتقالُ الكلّيُّ يحتاج شهادةً إضافيّةً لا مجرّدَ تراكمِ المنتهي.

## Wall Prevented

**finite-to-intended wall:** يمنع القفزَ من «كلُّ فحصٍ منتهٍ نجح» إلى «المبرهنةُ اللانهائيّةُ المقصودةُ صحيحة»؛ النموذجُ قد يكون غيرَ قياسيّ.

## Claim Classification

Known (مبرهنةٌ منطقيّةٌ كلاسيكيّة) · دورُ الوحدة: Governance / Certificate Discipline. ليست New Theorem ولا Candidate Mechanism.

## Rule / Tool Candidate

`TOOL-COMPACTNESS-001` — حيٌّ في `registries/tools.jsonl` كأداةِ حوكمة/شهادة (`classification=Diagnostic`, `role=Governance / Certificate Discipline`).

## No-Go Notes

```text
8. passing every finite check is NOT automatically proof of the intended infinite theorem
   (the compactness model may be nonstandard).
- compactness certifies satisfiability, not truth-in-the-intended-structure.
- not a tool for solving open problems; not a proof engine.
- no proof-system overclaim.  - no RH/GRH connection.
- no raw copyrighted text; transformed notes only.
```

## Next Valid Action

**v0.2-B complete** (001-F/G/H). Candidate next: v0.2-B closure review → then v0.3 (Tenenbaum-005-A). No expansion before review.

## Audit Checklist

- [x] Registry ID present · classification present
- [x] §3.7 only · transformed notes (no raw text, no general summary)
- [x] No RH/GRH connection · no proof-system overclaim · no classification-system edit · no theorem claim
- [x] TOOL-COMPACTNESS-001 promoted as governance/certificate tool (Diagnostic + role); planned.jsonl now empty
- [x] Six guards PASS after this unit

**Ceiling:** compactness certifies global satisfiability via finite satisfiability, not truth of the intended structure; passing finite checks is not proof of the intended infinite theorem. Certificate discipline, not a proof engine. No RH/GRH progress.
