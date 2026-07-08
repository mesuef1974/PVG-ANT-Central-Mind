# Mileti-001-C — Metatheory vs Formal Theory

**Registry ID:** MILETI-001-C
**Status:** Ingested (v0.2-A)
**Classification:** Known logic framework + **Governance / Certificate Discipline** (not theorem, not proof machinery)

**Source Coverage:** Mileti, *Modern Mathematical Logic*, §1.3 Syntax and Semantics (p23), §1.4 The Point of It All (p24) — **§1.3–1.4 only**. Book ID `BOOK-LOGIC-MILETI-001`. **Transformed notes only — no raw text, no general book summary.** Local PDF outside git.

## Object

المستوى الذي يجري فيه الاستدلال: داخلَ نظريّةٍ صوريّة، أم في ما-وراء-النظريّة التي تدرسها.

## Identity / Concept

```text
formal theory : the object being studied.
metatheory    : the external layer used to reason about that object.
"T proves phi" (inside)  ≠  "we prove, in the metatheory, that T proves phi" (about)
```

## Tool

وسمُ المستوى (level-tagging): كلُّ عبارةٍ مُعلَّمةٌ object-language / formal-system / metatheory. ما-وراء-النظريّة تستعمل رياضيّاتٍ عاديّةً صارمةً لدراسة النظام كبيانات.

## Certificate Function

انضباطُ الشهادة يقتضي **ألّا يُخلَط ادّعاءٌ داخلَ نظامٍ بادّعاءٍ مُتحقَّقٍ عن النظام**: الشهادةُ تُصرّح بمستواها (هويّة داخليّة / مبرهنة object / ملاحظة meta).

## PVG–ANT Use

كلُّ شهادة PVG/ANT تُعلن مستواها: هل هي هويّةٌ داخليّة، أم مبرهنةٌ على مستوى الكائن، أم ملاحظةٌ ما-وراءَ الطريقة؟ خلطُ المستويات = ادّعاءُ برهانٍ حيث لا برهان.

## Wall Prevented

**level-boundary / level-confusion:** يمنع استعمالَ قوّةِ نظريّةٍ لتبرير ما لا تقوله إلّا ما-وراء-النظريّة (أو العكس). يُلمِّح إلى حدِّ عدم الاكتمال (Ch12، خارج النطاق).

## Claim Classification

Known (إطارٌ منطقيّ) · دورُ الوحدة: Governance / Certificate Discipline. ليست New Theorem ولا Candidate Mechanism.

## Rule Candidate

`RULE-LOGIC-004` — «Metatheory Awareness». حيٌّ في `registries/rules.jsonl` كقاعدةِ حوكمة (`classification=Diagnostic`, `role=Governance / Certificate Discipline`).

## No-Go Notes

```text
- certificate discipline, not a proof engine.
- no proof-system overclaim.
- no RH/GRH connection.
- no raw copyrighted text; transformed notes only.
- incompleteness (Ch12) is only foreshadowed here, not imported.
```

## Next Valid Action

`Mileti-001-D` — Induction and Recursion as Generated Structure (§2.1–2.4) → `TOOL-GENERATION-001`.

## Audit Checklist

- [x] Registry ID present · classification present
- [x] §1.3–1.4 only · transformed notes (no raw text, no general summary)
- [x] No RH/GRH connection · no proof-system overclaim · no classification-system edit
- [x] RULE-LOGIC-004 only (not 003) · promoted as governance rule (Diagnostic + role)
- [x] Six guards PASS after this unit

**Ceiling:** never confuse a claim inside a system with a verified claim about the system. Certificate discipline, not a proof engine. No RH/GRH progress.
