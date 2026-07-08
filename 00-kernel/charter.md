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
00-kernel/            الدستور، الصدق، التصنيف، القواعد المركزية
01-registries/        مصدر الحقيقة (JSONL، canonical IDs): walls/tools/rules/books/observables/claims
02-diagnostic-cards/  بطاقات القرار والتشخيص
03-skill-ledgers/     سجلات الكتب مصنّفة بالطبقة (ant/logic/sieve/spectral/computational/ant-algebraic/proof-assistant)
04-bridges/           قواميس الترجمة بين اللغات
05-certificate-ledger/ known/identities/diagnostics/boundaries/missing/forbidden
06-book-pipeline/     قوالب الإدخال والإغلاق
tools/                الحراس الآليون
99-transition-memory/ الحالة والفعل التالي
```

**المبدأ الحاكم:** الـmarkdown للعرض، والـJSONL للحقيقة، والحارس للإنفاذ.

## Sub-minds (صلاحيات وحدود)

ثمانيةُ عقولٍ فرعيّة، لكلٍّ حدُّه: Logic · ANT · PVG · Sieve · Spectral · Computational · Bibliographic · Release-Governance. أمثلةُ الحدّ: **Computational** يعطي evidence لا مبرهنة؛ **Spectral** لا يعلن آليّةَ Hilbert–Pólya بلا operator certificate؛ **PVG** يشخّص الجدار لا يكسر parity.

## Governance

مستودعٌ مستقلٌّ في `D:\PVG-ANT-Central-Mind` (git خاصّ به). لا يتعقّب git أيَّ PDF (`Books_others/` مستبعَدٌ عبر `.gitignore`؛ يفرضه `no_pdf_audit`). لا tag للمسوّدات. النضج بمعايير `99-transition-memory` لا بالإعلان.

## Invariants (تُفحَص آليًّا)

1. كلُّ بطاقة/سجلٍّ يحمل تصنيفًا من `classification-system.md` (`honesty_audit`).
2. لا عبارةَ ترقيةٍ محظورة كتوكيدٍ إيجابيّ (`honesty_audit`، `forbidden_promotion_audit`).
3. لا ترقيةَ إلى Candidate/Theorem بلا `Certificate:` (`forbidden_promotion_audit`).
4. مصدرُ الحقيقة `01-registries/*.jsonl`؛ كلُّ ID في markdown موجودٌ فيه (`registry_sync_audit`).
5. لا PDF متعقَّب (`no_pdf_audit`). لا مفهومٌ مكرَّر (`duplicate_concept_audit`). كلُّ كتابٍ موثَّقُ المصدر (`citation_audit`).
