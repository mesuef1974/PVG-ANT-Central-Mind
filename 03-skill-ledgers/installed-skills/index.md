# Installed Skills — Interface Cards Index

المهاراتُ لا تدخل العقلَ كنصوصٍ خام، بل كـ **بطاقاتِ واجهة** (Skill Interface Cards): مدخلات/مخرجات/استعمال مسموح ومحظور/دورٌ في الشهادة/حدود. المصدرُ الآليّ: `01-registries/skills.jsonl`.

## Math layer (10)

| ID | Skill | Status |
|---|---|---|
| `SKILL-MATH-ANT-001` | analytic-number-theory | installed |
| `SKILL-MATH-PVG-001` | prime-valuation-geometry | conceptual |
| `SKILL-MATH-RIGOR-001` | solve-math-rigorously | installed |
| `SKILL-MATH-POLYMATH-001` | polymath-advanced-math | installed |
| `SKILL-MATH-LATEX-001` | latex | installed |
| `SKILL-MATH-NUMERICAL-001` | numerical-assistant | conceptual |
| `SKILL-MATH-COMPUTATIONAL-NT-001` | computational-number-theory | conceptual |
| `SKILL-MATH-SIEVE-001` | combinatorial-sieve | conceptual |
| `SKILL-MATH-OPERATOR-001` | operator-theory | conceptual |
| `SKILL-MATH-SPECTRAL-001` | spectral-analysis | conceptual |

## Governance layer (4) — higher authority

| ID | Skill | Status |
|---|---|---|
| `SKILL-GOV-BIBLIO-001` | bibliographic-verification | installed |
| `SKILL-GOV-CERTIFICATE-001` | certificate-ledger | installed |
| `SKILL-GOV-SPECTRAL-NOGO-001` | spectral-operator-no-go | installed |
| `SKILL-GOV-RELEASE-001` | research-release-governance | installed |

## قاعدةُ السلطة

عند التعارض، **مهاراتُ الحوكمة تعلو مهاراتِ الإبداع الرياضيّ**. مثال: إن تعارض `polymath-advanced-math` مع `certificate-ledger`، ينتصر `certificate-ledger`.

## صدقُ الحالة

`conceptual` = دورٌ/طبقةٌ في العقل لا مهارةٌ مثبَّتةٌ مستقلّة؛ الحقلُ `backed_by` في `skills.jsonl` يذكر ما يسندها. لا ندّعي وجودَ مهارةٍ غيرِ مثبَّتة.

**Honest classification:** Diagnostic (skill interface index). No RH/GRH progress.
