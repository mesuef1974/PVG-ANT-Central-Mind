# Installed Skills — Interface Cards Index

المهاراتُ لا تدخل العقلَ كنصوصٍ خام، بل كـ **بطاقاتِ واجهة** (Skill Interface Cards): مدخلات/مخرجات/استعمال مسموح ومحظور/دورٌ في الشهادة/حدود. المصدرُ الآليّ: `registries/skills.jsonl`.

## Math layer (11)

| ID | Skill | Status |
|---|---|---|
| `SKILL-MATH-ANT-001` | analytic-number-theory | installed |
| `SKILL-MATH-PVG-001` | prime-valuation-geometry | conceptual |
| `SKILL-MATH-PVG-AXIS-ADD-001` | pvg-axis-addition-fibers | installed specialist |
| `SKILL-MATH-RIGOR-001` | solve-math-rigorously | installed |
| `SKILL-MATH-POLYMATH-001` | polymath-advanced-math | installed |
| `SKILL-MATH-LATEX-001` | latex | installed |
| `SKILL-MATH-NUMERICAL-001` | numerical-assistant | conceptual |
| `SKILL-MATH-COMP-ANT-001` | computational-number-theory | conceptual |
| `SKILL-MATH-SIEVE-001` | combinatorial-sieve | conceptual |
| `SKILL-MATH-OPERATOR-001` | operator-theory | conceptual |
| `SKILL-MATH-SPECTRAL-001` | spectral-analysis | conceptual |

### Axis-addition specialist capability

Primary interface card:

`installed-skills/pvg-axis-addition-fibers/skill.md`

Reasoning route:

`maps/pvg-axis-addition-reasoning-map.md`

Competence gate:

`benchmarks/PVG-AXIS-ADDITION-SPECIALIST-BENCHMARK-001.md`

The skill is backed by the full governed research trees `research/avrg-axis-sum/` and `research/certificate-optimization-framework/`. Its installed status means the Central Mind must route relevant questions through the exact fiber/channel/certificate protocol, not that historical novelty or Goldbach progress has been established.

## Governance layer (4) — higher authority

| ID | Skill | Status |
|---|---|---|
| `SKILL-GOV-BIB-001` | bibliographic-verification | installed |
| `SKILL-GOV-CERT-001` | certificate-ledger | installed |
| `SKILL-GOV-NOGO-001` | spectral-operator-no-go | installed |
| `SKILL-GOV-RELEASE-001` | research-release-governance | installed |

## قاعدةُ السلطة

عند التعارض، **مهاراتُ الحوكمة تعلو مهاراتِ الإبداع الرياضيّ**. مثال: إن تعارض `polymath-advanced-math` مع `certificate-ledger`، ينتصر `certificate-ledger`.

## صدقُ الحالة

`conceptual` = دورٌ/طبقةٌ في العقل لا مهارةٌ مثبَّتةٌ مستقلّة؛ الحقلُ `backed_by` في `skills.jsonl` يذكر ما يسندها. لا ندّعي وجودَ مهارةٍ غيرِ مثبَّتة.

**Honest classification:** Diagnostic (skill interface index). No Goldbach proof and no RH/GRH progress.
