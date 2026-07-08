# Mileti-001-A — Mathematical Logic as Formalization

**Registry ID:** MILETI-001-A
**Status:** Ingested (v0.2-A)
**Classification:** Known logic framework + **Governance / Certificate Discipline** (not theorem, not proof machinery)

**Source Coverage:** Mileti, *Modern Mathematical Logic*, §1.1 The Nature of Mathematical Logic (p17), §1.2 The Language of Mathematics (p18). Book ID `BOOK-LOGIC-MILETI-001`. **Transformed notes only — no raw text, no general book summary.** Local PDF outside git.

## Object

الصورنة (formalization): تدوينُ لغةِ الرياضيّات وفرضيّاتها وقواعدِ برهانها المسموحة **ككائناتٍ صريحة** يمكن التعامل معها.

## Identity / Concept

الفصلُ الخماسيّ للمستويات:

```text
claim  ≠  formula  ≠  semantic truth  ≠  deduction  ≠  certificate
```

الصورنة = تثبيتُ (اللغة + الفرضيّات + قواعد الاستدلال) كأشياء، فيصير الحديثُ عنها منضبطًا لا انطباعيًّا.

## Tool

تمييزُ اللغةِ-الموضوع عن ما-وراء-النظريّة (formal-language ↔ metatheory)؛ معاملةُ القواعد كأشياء.

## Certificate Function

الصورنةُ هي **شرطُ إمكان الشهادة**: لا شهادةَ قابلةً للفحص قبل تثبيت «الادّعاء» و«القواعد» ككائنات. هذه الوحدةُ تُرسي دلالةَ كلمة «certificate» على مستوى الانضباط، لا تبرهن شيئًا.

## PVG–ANT Use

كلُّ ادّعاء PVG/ANT يُرمَّز عند مستواه الصحيح (statement / identity / theorem / certificate / missing-certificate) **قبل** الاستدلال؛ يُطبَّق انضباطُ الصورنة على المراصد قبل أيِّ حكم.

## Wall Prevented

**proof-object wall / level-confusion:** يمنع معاملةَ حجّةٍ غيرِ رسميّةٍ أو قياسٍ عدديٍّ كأنّه شهادة.

## Claim Classification

Known (إطارٌ منطقيٌّ كلاسيكيّ) · دورُ الوحدة: Governance / Certificate Discipline. ليست New Theorem ولا Candidate Mechanism.

## Rule Candidate

`RULE-LOGIC-001` — «Claim/Formalization Separation». رُقِّي إلى `registries/rules.jsonl` **كقاعدةِ حوكمة** (`classification=Diagnostic`, `role=Governance / Certificate Discipline`) لا كنظريّةٍ ولا آلةِ برهان.

## No-Go Notes

```text
- logic here = certificate discipline, not a proof engine.
- no proof-system overclaim.
- no RH/GRH connection.
- no raw copyrighted text; transformed notes only.
- formalization is not automatic rigor.
```

## Next Valid Action

`Mileti-001-B` — Syntax vs Semantics (§1.3) → `RULE-LOGIC-002`.

## Audit Checklist

- [x] Registry ID present · classification present
- [x] Transformed notes only (no raw text, no general summary)
- [x] No RH/GRH connection · no proof-system overclaim
- [x] Rule promoted as governance discipline, not theorem/proof machinery
- [x] Six guards PASS after this unit

**Ceiling:** Mileti-001-A = logic as certificate discipline, not logic as proof engine. No RH/GRH progress.
