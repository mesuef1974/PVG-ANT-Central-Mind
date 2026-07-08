# Central Rules

قواعدُ التشغيل المركزيّة. تنمو مع الكتب؛ لا عددَ مُعلَنٌ مسبقًا، ولا «Operating Rule 313». الصيغةُ البشريّة: «PVG–ANT Rule 001». المصدرُ الآليّ: `registries/rules.jsonl`.

## RULE-PVG-001 — Geometry / Analysis / Certificate

\[
\boxed{\ \text{Every phenomenon is read through: Geometry }\to\text{ Analysis }\to\text{ Certificate.}\ }
\]

الهندسة (support/height/phase/residue-fiber) → التحليل (ANT/Logic/Sieve) → الشهادة. **Diagnostic.** بطاقةٌ تدّعي نتيجةً بحقلِ `Certificate:` فارغ → تُرفَض.

## طبقة ANT (من Tenenbaum حتى 004-Z)

| ID | العنوان | المضمون | المصدر |
|---|---|---|---|
| `RULE-OBSERVABLE-ANATOMY-001` | Observable anatomy | كلُّ دالّةٍ تُفحَص عبر: بنية/هندسة/متوسّط/رتبة طبيعيّة/قانون نهائيّ/ذيل/عزوم/رتبة قصوى/جدار/شهادة | Tenenbaum 003-Z |
| `RULE-PHASE-TEST-001` | Test phase before randomness | اختبر الطورَ (Halász/pretentious) قبل ادّعاء الإلغاء/العشوائيّة | Tenenbaum 004-B |
| `RULE-AVERAGE-NORMAL-001` | Average ≠ normal order | المتوسّط والرتبةُ الطبيعيّة والتركيزُ والإلغاءُ اختباراتٌ متمايزة | Tenenbaum 004-H |
| `RULE-LOGIC-001` | Claim/Formalization Separation (Governance / Certificate Discipline) | الادّعاءُ ليس صورنتَه؛ رمِّز اللغةَ والفرضيّاتِ والقواعدَ قبل الاستدلال | Mileti 001-A (§1.1–1.2) |
| `RULE-LOGIC-002` | Syntax/Semantics Separation (Governance / Certificate Discipline) | الصيغةُ (نحو) ليست حقيقتَها (دلالة)؛ العبورُ بمبرهنةٍ مسمّاة | Mileti 001-B (§1.3) |
| `RULE-LOGIC-004` | Metatheory Awareness (Governance / Certificate Discipline) | ادّعاءٌ داخلَ نظامٍ ≠ ادّعاءٌ مُتحقَّقٌ عن النظام؛ صرِّح بالمستوى | Mileti 001-C (§1.3–1.4) |
| `RULE-LOGIC-003` | Proof/Deduction/Certificate Separation (Governance / Certificate Discipline) | برهانٌ ≠ استنتاج ≠ تحقّقٌ آليّ ≠ شهادةٌ بحثيّة؛ افحص الاشتقاقَ لا معقوليّةَ الخلاصة | Mileti 001-E (§3.5) |

| `RULE-CERT-SOUNDNESS-001` | No-false-certificate / Soundness (Governance / Certificate Discipline) | `⊢ ⟹ ⊨` تحت الدلالة المعتمَدة؛ الاشتقاقُ لا يشهد لباطل | Mileti 001-F (§3.6) |

**أدواتُ المنطق الحيّة (في `tools.jsonl`):** `TOOL-GENERATION-001` (001-D) · `TOOL-DEDUCTION-SYSTEM-001` (001-E) · `TOOL-COMPLETENESS-001` (Completeness ⊨→⊢، 001-G، §3.6). كلُّها حوكمة/شهادة.

**planned (`planned.jsonl`، v0.2-B):** `TOOL-COMPACTNESS-001` (001-H، §3.7) — يُرقَّى عند كتابة وحدته. لا توسّعَ بلا وحدة.

## بروتوكول الإضافة

قاعدةٌ تُشتقُّ من قسمٍ مقروءٍ فعليًّا، تحمل تصنيفًا، تُسجَّل في `rules.jsonl` بـID، وتُدمَج لا تُكرَّر.
