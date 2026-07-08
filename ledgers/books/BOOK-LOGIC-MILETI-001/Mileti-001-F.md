# Mileti-001-F — Soundness

**Registry ID:** MILETI-001-F
**Status:** Ingested (v0.2-B)
**Classification:** Known logic framework + **Governance / Certificate Discipline** (not theorem, not proof machinery)

**Source Coverage:** Mileti, *Modern Mathematical Logic*, §3.6 Soundness and Completeness (p86) — **soundness half of §3.6 only** (completeness → 001-G). Book ID `BOOK-LOGIC-MILETI-001`. **Transformed notes only — no raw text, no general book summary.** Local PDF outside git.

## Object

المبرهنةُ الناقلةُ من النحو إلى الدلالة في اتّجاهٍ واحد: `⊢ ⟹ ⊨`.

## Identity / Concept

```text
Soundness: if a statement is derivable inside the formal system,
           then it is true under the certified semantics.
formal:    Gamma ⊢ phi  ⟹  Gamma ⊨ phi.
```

بلغة الشهادة: **الاشتقاقُ الصحيحُ لا يشهد لباطلٍ أبدًا** تحت الدلالة المُعتمَدة.

## Tool

الجسرُ الأحاديّ `⊢→⊨`. الأداةُ الحاكمة: مبدأُ «لا شهادةَ كاذبة».

## Certificate Function

الصوتيّةُ هي **ضمانُ سلامة الشهادة**: ما يُشتَقُّ بالقواعد صادقٌ في كلّ نموذجٍ للفرضيّات. لذا الاشتقاقُ المنتهي القابلُ للفحص شهادةٌ يُوثَق بها — لكن بشرطِ اعتمادِ الدلالة.

## Certificate-discipline checklist (governing)

```text
Checking soundness requires verifying:
1. the formal system   : اللغة والبديهيّات محدَّدة.
2. the rules           : قواعدُ الاستدلال محفوظةٌ للصدق.
3. the derivation      : كلُّ خطوةٍ مبرَّرة.
4. the interpretation  : الدلالةُ المُعتمَدة (النماذج) محدَّدة.
5. the soundness bridge: أنّ كلَّ قاعدةٍ تحفظ الصدق ⟹ ⊢ ⟹ ⊨.
```

## PVG–ANT Use

شهادةُ PVG/ANT «سليمة» فقط ضمن دلالةٍ معتمَدة: لا يُنقَل اشتقاقٌ خارج نموذجه دون إعلانِ الدلالة؛ الصوتيّةُ تُبرِّر الوثوقَ بالاشتقاق لا بالخلاصة المعزولة.

## Wall Prevented

**unstated-semantics wall:** يمنع ادّعاءَ «صدقٍ» من اشتقاقٍ دون اعتمادِ التأويل؛ ويمنع خلطَ ⊢ بـ⊨ قبل الجسر.

## Claim Classification

Known (مبرهنةٌ منطقيّةٌ كلاسيكيّة) · دورُ الوحدة: Governance / Certificate Discipline. ليست New Theorem ولا Candidate Mechanism.

## Rule / Tool Candidate

`RULE-CERT-SOUNDNESS-001` — «No-false-certificate (soundness)». حيٌّ في `registries/rules.jsonl` كقاعدةِ حوكمة (`classification=Diagnostic`, `role=Governance / Certificate Discipline`). لم تُمَسّ أهدافُ Completeness/Compactness.

## No-Go Notes

```text
- soundness is the ⊢→⊨ bridge, not RH and not a proof engine.
- soundness certifies only relative to the certified semantics; unstated semantics = no certificate.
- completeness (⊨→⊢) is the reverse bridge, deferred to 001-G.
- no proof-system overclaim.  - no RH/GRH connection.
- no raw copyrighted text; transformed notes only.
```

## Next Valid Action

`Mileti-001-G` — Completeness (§3.6, reverse bridge ⊨→⊢) → `TOOL-COMPLETENESS-001`.

## Audit Checklist

- [x] Registry ID present · classification present
- [x] §3.6 soundness half only · transformed notes (no raw text, no general summary)
- [x] No RH/GRH connection · no proof-system overclaim · no classification-system edit · no theorem claim
- [x] RULE-CERT-SOUNDNESS-001 promoted as governance rule (Diagnostic + role); Completeness/Compactness kept planned
- [x] Six guards PASS after this unit

**Ceiling:** soundness = derivable inside ⟹ true under certified semantics; check the system, rules, derivation, interpretation, and the bridge. Certificate discipline, not a proof engine. No RH/GRH progress.
