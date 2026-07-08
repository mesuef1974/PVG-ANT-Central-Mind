# PVG–ANT Central Mind — Charter (v0.2)

مستودعُ عقلٍ رياضيّ تراكميّ. كلُّ كتابٍ يدخل لا كملخّص، بل كـ **أدوات + قواعد + جدران + شهادات + بطاقات تشغيل**.

## Supreme law

\[
\boxed{\ \text{Geometry}\ \leftrightarrow\ \text{Analysis}\ \leftrightarrow\ \text{Certificate}\ }
\]

الجملةُ الحاكمة: كلُّ معرفةٍ تدخل العقلَ يجب أن تتحوّل إلى هندسةٍ، تحليلٍ، شهادةٍ، وحدِّ ادّعاء.

## Ceiling (السقف — نافذٌ)

```text
This project does not claim RH/GRH progress.
Reading, diagnostics, experiments, analogies, or PVG/logic reformulations are NOT proofs.
Every output is classified. No result is upgraded without an external certificate.
```

## Seven layers

```text
central-mind-charter.md / central-mind-goals.md   الدستور والهدف الأعلى
governance/          الصدق، التصنيف، القواعد، المصفوفة، القمع، بروتوكول الكتب، no-go، missing/forbidden
registries/          مصدر الحقيقة (JSONL): skills/books/frontiers/queue/walls/tools/rules/observables/claims/planned
installed-skills/    14 بطاقة واجهة مهارة (math/governance)
ledgers/books/       سجلات الكتب (Overholt/Tenenbaum/Mileti-planned)  +  ledgers/imports/
maps/                skill-stack / dependency-graph / query-routing / current-capabilities / pvg-to-ant
audits/              v0.1b-audit-checklist
tools/               الحراس الآليون الستة
transition-memory/   الحالة والفعل التالي و compressed-prompt
```

**المبدأ الحاكم:** الـmarkdown للعرض، والـJSONL للحقيقة، والحارس للإنفاذ.

## Sub-minds (صلاحيات وحدود)

ثمانيةُ عقولٍ فرعيّة، لكلٍّ حدُّه: Logic · ANT · PVG · Sieve · Spectral · Computational · Bibliographic · Release-Governance. أمثلةُ الحدّ: **Computational** يعطي evidence لا مبرهنة؛ **Spectral** لا يعلن آليّةَ Hilbert–Pólya بلا operator certificate؛ **PVG** يشخّص الجدار لا يكسر parity.

## Governance

مستودعٌ مستقلٌّ في `D:\PVG-ANT-Central-Mind` (git خاصّ به). لا يتعقّب git أيَّ PDF (`Books_others/` مستبعَدٌ عبر `.gitignore`؛ يفرضه `no_pdf_audit`). لا tag للمسوّدات. النضج بمعايير `transition-memory/` و`audits/` لا بالإعلان.

## Invariants (تُفحَص آليًّا)

1. كلُّ بطاقة/سجلٍّ يحمل تصنيفًا من `classification-system.md` (`honesty_audit`).
2. لا عبارةَ ترقيةٍ محظورة كتوكيدٍ إيجابيّ (`honesty_audit`، `forbidden_promotion_audit`).
3. لا ترقيةَ إلى Candidate/Theorem بلا `Certificate:` (`forbidden_promotion_audit`).
4. مصدرُ الحقيقة `registries/*.jsonl`؛ كلُّ ID في markdown موجودٌ فيه (`registry_sync_audit`).
5. لا PDF متعقَّب (`no_pdf_audit`). لا مفهومٌ مكرَّر (`duplicate_concept_audit`). كلُّ كتابٍ موثَّقُ المصدر (`citation_audit`).
