# Mileti-001-B — Syntax vs Semantics

**Registry ID:** MILETI-001-B
**Status:** Ingested (v0.2-A)
**Classification:** Known logic framework + **Governance / Certificate Discipline** (not theorem, not proof machinery)

**Source Coverage:** Mileti, *Modern Mathematical Logic*, §1.3 Syntax and Semantics (p23) — **§1.3 only**. Book ID `BOOK-LOGIC-MILETI-001`. **Transformed notes only — no raw text, no general book summary.** Local PDF outside git.

## Object

الوجهان لأيِّ كائنٍ صوريّ: شكلُه (syntax) ومعناه (semantics).

## Identity / Concept

```text
syntax    : what strings are well-formed (shape, built by rules)
semantics : what those strings mean under an interpretation (truth in a structure)
formula (a finite string)  ≠  its truth under interpretation
```

الجسرُ بين العمودين مبرهنةٌ مسمّاة، لا فرضيّةٌ صامتة.

## Tool

الفصلُ النحوِيّ-الدلاليّ: كائناتٌ نحويّةٌ تُعالَج بالقواعد، وكائناتٌ دلاليّةٌ تُقيَّم في البنى؛ لا خلطَ بينهما.

## Certificate Function

انضباطُ الشهادة يقتضي **ألّا يُخلَط الشكلُ الصوريُّ بالحقيقة الرياضيّة**: عبورُ العمودين يُدفَع دائمًا بمبرهنةٍ ناقلةٍ مسمّاة (soundness/completeness — مؤجَّلة v0.2-B)، لا بالادّعاء.

## PVG–ANT Use

المرصدُ (observable) دلاليّ؛ آلتُه الجبريّة (Dirichlet series / Euler product) نحويّة — لا يُخلَط الكائنُ المقيس بترميزه الجبريّ.

## Wall Prevented

**syntax–semantics gap:** يمنع قراءةَ «الحقيقة» في سلسلةٍ نحويّة، أو معالجةَ المعنى كأنّه شكلٌ يُلاعَب.

## Claim Classification

Known (إطارٌ منطقيّ) · دورُ الوحدة: Governance / Certificate Discipline. ليست New Theorem ولا Candidate Mechanism.

## Rule Candidate

`RULE-LOGIC-002` — «Syntax/Semantics Separation». حيٌّ في `registries/rules.jsonl` كقاعدةِ حوكمة (`classification=Diagnostic`, `role=Governance / Certificate Discipline`).

## No-Go Notes

```text
- certificate discipline, not a proof engine.
- no proof-system overclaim (no claim that syntax determines truth).
- no RH/GRH connection.
- no raw copyrighted text; transformed notes only.
- the syntax->semantics bridge is a named metatheorem, deferred to v0.2-B.
```

## Next Valid Action

`Mileti-001-C` — Metatheory vs Formal Theory (§1.3–1.4) → `RULE-LOGIC-004`.

## Audit Checklist

- [x] Registry ID present · classification present
- [x] §1.3 only · transformed notes (no raw text, no general summary)
- [x] No RH/GRH connection · no proof-system overclaim · no classification-system edit
- [x] RULE-LOGIC-002 promoted as governance rule (Diagnostic + role), not theorem/proof
- [x] Six guards PASS after this unit

**Ceiling:** never confuse formal shape with mathematical truth. Certificate discipline, not a proof engine. No RH/GRH progress.
