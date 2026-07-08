# PVG–ANT Central Mind — v0.1b Full Integration Specification

> **Reconciliation status (honest note, not part of the original spec):**
> Central Mind Integration Pass 001 (v0.1b) is implemented, and the repository has now been
> **restructured to match this spec's named layout** (`installed-skills/ ledgers/ registries/
> maps/ governance/ audits/ + central-mind-charter.md / central-mind-goals.md`), with the
> spec's skill-IDs adopted (`SKILL-GOV-BIB-001`, `SKILL-GOV-CERT-001`, `SKILL-GOV-NOGO-001`,
> `SKILL-MATH-COMP-ANT-001`). Six guards in `tools/` pass on the new layout.
> **Deviations kept (additive, no content lost):** `registries/` also holds the source-of-truth
> jsonl beyond skills/books/frontiers/queue (walls/tools/rules/observables/claims/planned/constraint);
> `ledgers/imports/` holds the sieve/spectral/computational imports; `ledgers/books/BOOK-LOGIC-MILETI-001/`
> holds the deferred Mileti (README + planned-units only); `transition-memory/` holds handoff files.
> **Honesty carry-over (overrides "installed-interface-card" wording below):** 6 of the 14 skills
> are `conceptual` (prime-valuation-geometry, numerical-assistant, computational-number-theory,
> combinatorial-sieve, operator-theory, spectral-analysis) — not installed Anthropic skills; their
> cards carry `status: conceptual` + `backed_by`. "installed-interface-card" means the *card* exists.
> Ceiling unchanged: zero RH progress · zero GRH progress · no secured path.

---

**PVG–ANT Central Mind — v0.1b Full Integration Specification — Central Mind Integration Pass 001**

تابع من مشروع:

```text
PVG–ANT Central Mind
```

نقطة البداية الحالية:

```text
Central Mind Integration Pass 001
```

المرحلة الحالية:

```text
v0.1b = Integrate Existing Skills + Overholt + Tenenbaum Partial
```

ولا نبدأ الآن:

```text
- Mileti Logic Certificate Layer
- Tenenbaum-005-A
- أي جبهة بحثية جديدة
- أي ادعاء تقدم نحو RH أو GRH
```

## 1. الهوية العامة للعقل المركزي

### 1.1 ما هو PVG–ANT Central Mind؟

PVG–ANT Central Mind هو بنية بحثية مركزية لتنظيم المهارات الرياضية، سجلات الكتب، خرائط المعرفة، قواعد الحوكمة، والأسئلة المفتوحة المرتبطة بمشروع:

```text
Prime-Valuation Geometry + Analytic Number Theory
```

اختصارًا:

```text
PVG + ANT
```

العقل المركزي ليس مجرد مجلد ملاحظات، وليس مستودع تلخيص كتب، وليس محاولة مباشرة لإثبات RH أو GRH. هو نظام تشغيل بحثي رياضي وظيفته:

```text
تحويل المعرفة الرياضية المتراكمة إلى قدرات قابلة للتشغيل، التدقيق، التوسيع، والمراجعة.
```

### 1.2 لماذا نبني هذا العقل؟

**السبب الأول: منع ضياع العمل المتراكم.** خلال المشروع تراكمت مهارات كثيرة:

```text
- نظرية الأعداد التحليلية
- هندسة التقييمات الأولية
- الغربال
- الدوال الحسابية
- سلاسل ديريشليه
- جداءات أويلر
- التحليل الطيفي
- المؤثرات
- الحساب العددي
- التحقق الببليوغرافي
- سجلات الشهادات
- حوكمة الادعاءات
```

إذا بقيت هذه المعرفة مبعثرة داخل محادثات وملفات عشوائية، فسوف تضيع أو تختلط. العقل المركزي يحولها إلى:

```text
مهارات مثبتة + سجلات + خرائط + بروتوكولات + حدود ادعاء.
```

**السبب الثاني: تحويل المهارات إلى واجهات قابلة للاستخدام.** لا نريد "طباعة العقل" كأسرار داخلية أو prompts كاملة. نريد طباعة كل مهارة كبطاقة واجهة `Skill Interface Card`: ما وظيفتها؟ متى تُستخدم؟ ما مدخلاتها ومخرجاتها وحدودها؟ ما الأشياء التي لا يجوز استخدامها فيها؟ ما التصنيفات المسموحة لادعاءاتها؟ القاعدة:

```text
Print interfaces, not internals.
Print capabilities, not hidden prompts.
Print boundaries before claims.
Print certificates before conclusions.
```

**السبب الثالث: ربط PVG بنظرية الأعداد التحليلية.** طبقة ترجمة بين `Prime-Valuation Geometry` و`Analytic Number Theory`. كل كائن يُقرأ بثلاث طرق:

```text
1. هندسيًا داخل فضاء التقييمات الأولية.
2. تحليليًا عبر المجاميع، السلاسل، جداءات أويلر، الأخطاء، والإلغاء.
3. حوكمياً عبر التصنيف والشهادة والجدار المانع.
```

قاعدة `Geometry – Analysis – Certificate Triangle`: `PVG geometry ↔ ANT analysis ↔ Certificate governance`.

**السبب الرابع: تحويل الكتب إلى مهارات لا إلى ملخصات.** لا ندخل PDF/نصوص طويلة/نسخ خام/تلخيصًا حرفيًا/ادعاء إتقان كامل. بل كل كتاب كـ `Book Skill Ledger`: Object / Identity / Tool / Main Term / Error / Wall / Certificate / PVG Connection / Claim Classification / Next Valid Action. الهدف استخراج قواعد تشغيلية ومفاهيم قابلة لإعادة الاستخدام.

**السبب الخامس: منع الخلط بين الفكرة والبرهان.** منع تحويل التشخيص إلى برهان، القياس إلى تقدم، إعادة التفسير إلى نظرية جديدة، قراءة كتاب إلى إتقان كامل. كل claim يجب أن يُصنَّف؛ لا claim بلا classification.

**السبب السادس: بناء مختبر بحثي صادق** `Mathematical Honesty Laboratory` يسأل دائمًا: ما الكائن؟ ما المعروف؟ ما الهوية؟ ما إعادة التفسير؟ ما التشخيص؟ ما الجدار؟ ما الشهادة الناقصة؟ ما الذي لا يجوز ادعاؤه؟ ما الخطوة التالية المسموحة؟

## 2. الهدف البحثي العميق

**2.1 الهدف الأعلى:** البحث العميق في علاقة هندسة التقييمات الأولية بنظرية الأعداد التحليلية. السؤال المركزي: كيف تظهر كائنات نظرية الأعداد التحليلية عندما تُقرأ هندسيًا داخل فضاء التقييمات الأولية؟

**2.2 ماذا ندرس:** المعنى الهندسي داخل PVG لـ: الدوال الحسابية/الجمعية/الضربية، موبيوس، ليوفيل، مانغولد، القواسم، أويلر، أوزان الأوليات، جداء ديريشليه، انقلاب موبيوس، هندسة القواسم، هندسة الدعم، ارتفاع التقييمات، المخروط التقييمي، الصندوق القاسمي، جداءات أويلر، سلاسل ديريشليه، الشخصيات، الأصناف الباقية، الألياف الباقية، الغربال، حواجز الغربال، حاجز التكافؤ، Type I/II/III، حدود الخطأ، الإلغاء، المتوسطات، الرتب الطبيعية، التذبذب، كثافة الأصفار، القيم الكبيرة، المؤثرات، التحليل الطيفي، التشخيصات العددية.

**2.3 ما نبحث عنه:** ليس فقط إعادة تسمية المعروف، بل: هل تكشف الهندسة بنية خفية؟ هل تساعد على تصنيف الدوال أفضل؟ هل تميّز الهوية من التقدير؟ هل تكشف سبب جدار؟ هل تعطي لغة أدق للأسئلة المفتوحة؟ هل تقترح آلية مرشحة قابلة للاختبار؟ هل تقدّم في حالات محدودة شهادة حقيقية؟ — كل ذلك تحت حوكمة صارمة.

**2.4 نكمل من حيث انتهت الأبحاث القائمة:** كل جبهة تبدأ من: ما المعروف؟ أين تقف النتائج؟ ما السؤال المفتوح؟ ما الجدار؟ ما الشهادة الناقصة؟ هل PVG تضيف لغة/تشخيصًا/آلية مرشحة؟ ما الاختبار القابل للإبطال؟ ما الذي لا يجوز ادعاؤه؟ القانون: نبدأ من حدود المعرفة القائمة، لا من التخمين المعزول.

**2.5 علاقة RH/GRH:** لا يعني ادعاء تقدم. الصياغة الصحيحة:

```text
PVG–ANT Central Mind may organize questions related to zeta, primes, L-functions, zeros,
or spectral analogies, but it does not claim RH/GRH progress without a complete proof certificate.
```

أي: لا RH progress · لا GRH progress · لا مسار مثبت · لا تحويل قياس أو تشخيص إلى برهان.

## 3. نطاق v0.1b

**3.1 ما ننجزه الآن:** إنشاء بنية installed-skills · طباعة Skill Interface Cards · إدخال Overholt كـ safe retrofitted ledger · إدخال Tenenbaum partial حتى Tenenbaum-004-Z · تحديث registries · خرائط القدرات · ملفات الحوكمة · audit checklist.

**3.2 ما لا ننجزه الآن:** Mileti · Tenenbaum-005-A · أي كتاب جديد · أي طبقة منطقية جديدة · أي ادعاء نظرية جديدة · أي تجربة RH/GRH · أي توسيع غير مطلوب.

## 4. بنية المشروع المطلوبة (spec named layout)

```text
PVG-ANT-Central-Mind/
  README.md
  central-mind-goals.md
  central-mind-charter.md
  installed-skills/
    math/{analytic-number-theory, prime-valuation-geometry, solve-math-rigorously,
          polymath-advanced-math, latex, numerical-assistant, computational-number-theory,
          combinatorial-sieve, operator-theory, spectral-analysis}.md
    governance/{bibliographic-verification, certificate-ledger,
                spectral-operator-no-go, research-release-governance}.md
  ledgers/books/
    BOOK-ANT-OVERHOLT-001/{README, ledger-summary, imported-capabilities,
                           pvg-connections, boundaries, audit}.md
    BOOK-ANT-TENENBAUM-002/{README, ledger-summary, arithmetic-observable-diagnostic-card,
                            multiplicative-function-decision-tree, observable-ladder,
                            master-diagnostic-sheet, pvg-connections, boundaries, audit}.md
  registries/{skills.jsonl, books.jsonl, research-frontiers.jsonl, open-questions-queue.jsonl}
  maps/{skill-stack-map, skill-dependency-graph, query-routing-guide, current-capabilities}.md
  governance/{claim-classification-matrix, certificate-funnel, book-import-protocol,
              what-not-to-import, no-go-memory}.md
  audits/v0.1b-audit-checklist.md
```

## 5. Registry ID System

**5.1 أنواع المعرفات:**

```text
CENTRAL-MIND-GOALS-001 / CENTRAL-MIND-CHARTER-001
SKILL-MATH-ANT-001 / PVG-001 / RIGOR-001 / POLYMATH-001 / LATEX-001 / NUMERICAL-001 /
  COMP-ANT-001 / SIEVE-001 / OPERATOR-001 / SPECTRAL-001
SKILL-GOV-BIB-001 / CERT-001 / NOGO-001 / RELEASE-001
BOOK-ANT-OVERHOLT-001 / BOOK-ANT-TENENBAUM-002
FRONTIER-ANT-PVG-001 / Q-PVG-ANT-001 / AUDIT-CM-V01B-001
```

**5.2 القاعدة:** لا يدخل شيء مهم بدون: Registry ID + Status + Version + Classification + RH/GRH status + Path.

## 6. كيف نطبع المهارات؟

نطبع المهارة كـ `Skill Interface Card`، ولا نطبع prompt كامل / تعليمات داخلية / raw internals / نصوص كتب خام / claims غير مصنفة. قالب البطاقة:

```markdown
# Skill Interface Card: <skill-name>
Registry ID / Status: Installed Interface Card / Version: v0.1b / Group: math|governance
Classification / RH/GRH Status: No progress claim
## Purpose / Inputs / Outputs / Main Capabilities / Boundaries
## Claim Classification Rules / Dependencies / Do Not Use For
## Audit Checklist
- [ ] Registry ID present  - [ ] Classification present  - [ ] Boundaries explicit
- [ ] No raw copyrighted text  - [ ] No prompt dump  - [ ] No RH/GRH progress claim
```

## 7. المهارات الرياضية (10)

- **analytic-number-theory** `SKILL-MATH-ANT-001` — تحويل أدوات ANT إلى كائنات عمل (دوال حسابية، جداء/انقلاب، سلاسل، جداءات أويلر، زيتا، L-functions بحذر، شخصيات، تقديرات، حدود رئيسية، أخطاء، Tauberian/contour/PNT). حدود: لا RH/GRH progress، لا تحسين PNT بلا برهان، لا تحويل تقدير معروف إلى نظرية.
- **prime-valuation-geometry** `SKILL-MATH-PVG-001` — قراءة الكائنات داخل فضاء التقييمات: ν(n)، support، height، divisor box، valuation cone، coordinate faces، squarefree cube، axial rays، residue fibers. حدود: إعادة التفسير ليست نظرية، التشخيص ليس برهانًا، الهندسة وحدها لا تكسر RH/GRH/parity/zero-density.
- **solve-math-rigorously** `SKILL-MATH-RIGOR-001` — حل بصرامة، فصل البرهان من الحدس؛ لا انطباع، لا نظرية بلا برهان كامل.
- **polymath-advanced-math** `SKILL-MATH-POLYMATH-001` — ربط فروع؛ التشابه يُصنَّف analogy/candidate mechanism لا برهانًا.
- **latex** `SKILL-MATH-LATEX-001` — صياغة؛ جمال الصياغة ليس صحة.
- **numerical-assistant** `SKILL-MATH-NUMERICAL-001` — تجارب عددية؛ القياس ليس برهانًا، لا claim عددي دقيق بلا حساب فعلي.
- **computational-number-theory** `SKILL-MATH-COMP-ANT-001` — خوارزميات؛ التحقق المنتهي ليس برهانًا لانهائيًّا، الدليل الحسابي diagnostic ما لم يُشهَد.
- **combinatorial-sieve** `SKILL-MATH-SIEVE-001` — غربالات كطبقات معلومات وجدران؛ الواجهة ليست غربالًا جديدًا، لا يكسر parity، لا prime detector.
- **operator-theory** `SKILL-MATH-OPERATOR-001` — أفكار مؤثرية؛ التشابه ليس تقدمًا نحو RH، self-adjoint وحده ليس شهادة Hilbert–Pólya.
- **spectral-analysis** `SKILL-MATH-SPECTRAL-001` — بنى طيفية؛ الإحصاء الطيفي لا يثبت RH، القطري لا يحدد pair correlation، الاتفاق مع GUE تشخيص.

## 8. مهارات الحوكمة (4، سلطة أعلى)

- **bibliographic-verification** `SKILL-GOV-BIB-001` — لا مصدر، لا claim قوي.
- **certificate-ledger** `SKILL-GOV-CERT-001` — لا شهادة، لا نظرية؛ Candidate يبقى Candidate حتى يُشهَد.
- **spectral-operator-no-go** `SKILL-GOV-NOGO-001` — لا شهادة مؤثر ذاتي الاقتران، لا ادعاء Hilbert–Pólya؛ لا تشابه طيفي كتقدم.
- **research-release-governance** `SKILL-GOV-RELEASE-001` — لا نشر بلا audit، لا ادعاء نظرية علنيّ بلا شهادة.

## 9. Skill Registry (registries/skills.jsonl)

```jsonl
{"id":"SKILL-MATH-ANT-001","name":"analytic-number-theory","group":"math","status":"installed-interface-card","version":"v0.1b","classification":"tool/diagnostic/known-method-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-PVG-001","name":"prime-valuation-geometry","group":"math","status":"installed-interface-card","version":"v0.1b","classification":"framework/diagnostic/reinterpretation-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-RIGOR-001","name":"solve-math-rigorously","group":"math","classification":"proof-discipline/interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-POLYMATH-001","name":"polymath-advanced-math","group":"math","classification":"cross-domain-research-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-LATEX-001","name":"latex","group":"math","classification":"mathematical-writing-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-NUMERICAL-001","name":"numerical-assistant","group":"math","classification":"numerical-diagnostic-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-COMP-ANT-001","name":"computational-number-theory","group":"math","classification":"computational-diagnostic-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-SIEVE-001","name":"combinatorial-sieve","group":"math","classification":"sieve-diagnostic/interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-OPERATOR-001","name":"operator-theory","group":"math","classification":"operator-diagnostic-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-MATH-SPECTRAL-001","name":"spectral-analysis","group":"math","classification":"spectral-diagnostic-interface","rh_grh_status":"no-progress-claim"}
{"id":"SKILL-GOV-BIB-001","name":"bibliographic-verification","group":"governance","classification":"source-verification-governance","rh_grh_status":"anti-overclaim-control"}
{"id":"SKILL-GOV-CERT-001","name":"certificate-ledger","group":"governance","classification":"certificate-control-governance","rh_grh_status":"anti-overclaim-control"}
{"id":"SKILL-GOV-NOGO-001","name":"spectral-operator-no-go","group":"governance","classification":"spectral-overclaim-prevention","rh_grh_status":"anti-overclaim-control"}
{"id":"SKILL-GOV-RELEASE-001","name":"research-release-governance","group":"governance","classification":"research-release-control","rh_grh_status":"anti-overclaim-control"}
```

## 10. Book Import Protocol (governance/book-import-protocol.md)

القواعد: (1) لا PDF داخل git. (2) لا raw copyrighted text. (3) لا نقل طويل. (4) لا ادعاء إتقان كامل. (5) لا ادعاء نظرية جديدة. (6-9) كل import يحتاج Registry ID + classification + boundaries + audit. قالب الكتاب: Book ID / Source Name / Import Status / Coverage / Purpose / Allowed Use / Forbidden Use / Extracted Capabilities / PVG Connections / Claim Classification / Missing Certificates / Next Valid Actions / Audit Status.

## 11. Overholt Ledger Import — BOOK-ANT-OVERHOLT-001

Status: safe retrofitted ledger. Classification: book-derived skill ledger / known-method interface / diagnostic support. **لا يعني:** إتقانًا/نقل محتوى/نتائج جديدة/تقدمًا نحو RH/GRH. **يعني:** إعادة تركيب آمنة لمخرجات ANT Skill Ledger السابقة. **يستخرج:** الدوال الحسابية، أوزان Chebyshev، Λ، θ/ψ، Dirichlet convolution، Möbius inversion، hyperbola، Euler products، characters، circle method as certificate assembly، contour، PNT/Siegel-Walfisz/Dedekind context — بصياغة Known/Tool/Identity/Diagnostic/Boundary لا theorem discovery. ملفات: README/ledger-summary/imported-capabilities/pvg-connections/boundaries/audit. README ينص: not full reproduction · not complete mastery · not a source of new theorem claims · no raw copyrighted text · no RH/GRH progress claim.

## 12. Tenenbaum Partial Ledger — BOOK-ANT-TENENBAUM-002

Status: partial ledger through Tenenbaum-004-Z. **لا يعني:** إكمال/إتقان/إدخال 005-A/البدء بالشخصيات/نتائج جديدة. ملفات: README/ledger-summary/arithmetic-observable-diagnostic-card/multiplicative-function-decision-tree/observable-ladder/master-diagnostic-sheet/pvg-connections/boundaries/audit.

**Arithmetic Observable Diagnostic Card** لكل observable: Name / Classical Definition / PVG Reading / Support Geometry / Mean-Average / Cancellation / Dirichlet Series or Euler Product / Main Term Status / Error Term Status / Wall / Certificate Needed / Claim Classification. أمثلة: 1(n), μ(n), |μ(n)|, λ(n), Λ(n), τ(n), φ(n), ω(n), Ω(n), P+(n), P-(n) — بلا claims جديدة بلا شهادة.

**Multiplicative Function Decision Tree:** multiplicative? → completely (signed phase λ/characters؟ size-controlled؟) / not-completely (Euler product؟ local factors؟) — additive? strongly (ω) / completely (Ω) — prime-supported? axial (Λ) — divisor-aggregate? convolutional (τ) — Classification: Known/Identity/Diagnostic/Boundary/Open Problem.

**Observable Ladder:** L0 Definition · L1 Identity · L2 Support · L3 Average · L4 Cancellation · L5 Distribution · L6 Frontier · L7 Certificate-Required.

**Master Diagnostic Sheet columns:** Object / Classical Role / PVG Geometry / Support Type / Dirichlet Series / Euler Product / Convolution Role / Mean Behavior / Cancellation Requirement / Known Theorem Context / Wall / Missing Certificate / Claim Classification / Allowed Use / Forbidden Use / Next Action.

## 13. Books Registry (registries/books.jsonl)

```jsonl
{"id":"BOOK-ANT-OVERHOLT-001","title":"A Course in Analytic Number Theory","author":"Marius Overholt","status":"safe-retrofitted-ledger","version":"v0.1b","classification":"book-derived-known-method-ledger","coverage":"prior ANT Skill Ledger outputs only","rh_grh_status":"no-progress-claim"}
{"id":"BOOK-ANT-TENENBAUM-002","title":"Introduction to Analytic and Probabilistic Number Theory","author":"Gerald Tenenbaum","status":"partial-ledger","version":"v0.1b","classification":"partial-book-derived-diagnostic-ledger","coverage":"through Tenenbaum-004-Z only","rh_grh_status":"no-progress-claim"}
```

## 14. Claim Classification Matrix (governance/)

Known (يحتاج مصدر) · Identity (تحقق رمزي/برهان قصير) · Reinterpretation (يُمنع تقديمها اكتشافًا) · Diagnostic (يُمنع تحويلها proof) · Boundary (parity/zero-density/Type-II gap/operator recoverability failure) · Open Problem (يُمنع صياغته محلولًا) · Candidate Mechanism (اختبار قابل للإبطال + شهادة ناقصة محددة + حدود) · New Theorem (تعريفات + فرضيات + برهان كامل + فحص ثغرات + شهادة + audit).

## 15. Certificate Funnel (governance/)

`Observation → Pattern → Diagnostic → Candidate Mechanism → Lemma → Theorem → Audited Result`. Candidate Mechanism يحتاج: ما الجديد؟ أين يفشل المعروف؟ ما الشهادة المطلوبة؟ ما الاختبار القابل للإبطال؟ Audited Result يحتاج: source/claim/proof/no-overclaim audit.

## 16. Research Frontier Register (registries/research-frontiers.jsonl)

كل جبهة: ID / Title / Classical Context / PVG Question / Known Status / Open Question / Wall / Missing Certificate / Classification / Allowed Next Action / RH/GRH Status.

```jsonl
{"id":"FRONTIER-ANT-PVG-001","title":"Prime-valuation geometry of arithmetic functions","open_question":"Can support geometry classify analytic behavior beyond naming?","wall":"Need theorem-level predictive gain","missing_certificate":"Structural theorem connecting PVG type to analytic behavior","classification":"Open Problem / Diagnostic","rh_grh_status":"no-progress-claim"}
{"id":"FRONTIER-ANT-PVG-002","title":"Multiplicative functions as valuation observables","open_question":"Can PVG improve classification of mean/cancellation types?","wall":"No proof of new predictive classification yet","classification":"Open Problem","rh_grh_status":"no-progress-claim"}
{"id":"FRONTIER-ANT-PVG-003","title":"Mobius and Liouville as signed valuation-cube observables","open_question":"Can PVG isolate what information is missing?","wall":"Cancellation cannot be obtained from geometry alone","classification":"Boundary / Open Problem","rh_grh_status":"no-progress-claim"}
{"id":"FRONTIER-ANT-PVG-004","title":"Sieve information through PVG support geometry","open_question":"Can PVG clarify Type-I/II/III information gaps?","wall":"Parity and missing bilinear information","classification":"Diagnostic / Boundary","rh_grh_status":"no-progress-claim"}
{"id":"FRONTIER-ANT-PVG-005","title":"Residue fibers and Dirichlet characters","known_status":"Deferred to v0.3","wall":"Not started in v0.1b","missing_certificate":"Tenenbaum-005-A import and verification","classification":"Queued","rh_grh_status":"no-progress-claim"}
{"id":"FRONTIER-ANT-PVG-006","title":"Zero-density and large values as frontier diagnostics","open_question":"Can valuation diagnostics organize obstruction types?","wall":"Requires advanced analytic estimates","classification":"Boundary / Open Problem","rh_grh_status":"no-progress-claim"}
{"id":"FRONTIER-ANT-PVG-007","title":"Spectral/operator diagnostics and recoverability","known_status":"No-go memory active","wall":"Recoverability failure","classification":"Diagnostic / Boundary","rh_grh_status":"no-progress-claim"}
{"id":"FRONTIER-ANT-PVG-008","title":"Computational diagnostics versus proof certificates","wall":"Finite data cannot prove infinite claims alone","classification":"Governance / Boundary","rh_grh_status":"no-progress-claim"}
```

## 17. Open Questions Queue (registries/open-questions-queue.jsonl)

```jsonl
{"id":"Q-PVG-ANT-001","question":"Can valuation support geometry classify analytic behavior of multiplicative functions?","status":"queued","required_skills":["analytic-number-theory","prime-valuation-geometry","certificate-ledger"],"classification":"Open Problem","next_action":"Create diagnostic comparison table for multiplicative functions","rh_grh_status":"no-progress-claim"}
{"id":"Q-PVG-ANT-002","question":"Which arithmetic observables are identity-level and which require cancellation certificates?","status":"queued","required_skills":["analytic-number-theory","solve-math-rigorously","certificate-ledger"],"classification":"Diagnostic","next_action":"Build observable ladder and classify examples","rh_grh_status":"no-progress-claim"}
{"id":"Q-PVG-ANT-003","question":"Can sieve walls be expressed as missing information shapes in valuation geometry?","status":"queued","required_skills":["combinatorial-sieve","prime-valuation-geometry","research-release-governance"],"classification":"Boundary / Diagnostic","next_action":"Map parity, Type-I, Type-II, and residue-fiber walls","rh_grh_status":"no-progress-claim"}
{"id":"Q-PVG-ANT-004","question":"What no-go rules prevent spectral diagnostics from becoming RH claims?","status":"queued","required_skills":["operator-theory","spectral-analysis","spectral-operator-no-go"],"classification":"Governance / Boundary","next_action":"Install spectral-operator-no-go card","rh_grh_status":"anti-overclaim-control"}
```

## 18. No-Go Memory (governance/no-go-memory.md)

```text
1. Measurement is not proof.
2. Book reading is not mastery.
3. PVG reinterpretation is not theorem improvement.
4. Sieve diagnostics do not break parity.
5. Local valuation geometry alone does not create Type-II information.
6. Spectral analogy is not RH progress.
7. Diagonal observables do not determine pair correlation.
8. Numerical agreement is diagnostic, not theorem.
9. A missing certificate must be named before a claim can be upgraded.
10. No RH/GRH progress claim is allowed without a complete proof certificate.
```

## 19. What Not To Import (governance/)

يمنع: PDFs · copyrighted raw text · full book passages · hidden prompt dumps · exact numerical results not produced by actual commands · speculative RH/GRH claims · unsupported theorem claims · unverified citations · "mastery"/"breakthrough"/"proof path" language unless certified.

## 20. Query Routing Guide (maps/)

arithmetic functions → analytic-number-theory + prime-valuation-geometry + certificate-ledger · PVG interpretation → prime-valuation-geometry + analytic-number-theory + claim-classification-matrix · proof → solve-math-rigorously + certificate-ledger + bibliographic-verification · book → book-import-protocol + bibliographic-verification + certificate-ledger · sieve → combinatorial-sieve + prime-valuation-geometry + research-release-governance · operators/spectra → operator-theory + spectral-analysis + spectral-operator-no-go · numerical → numerical-assistant + computational-number-theory + certificate-ledger · new claim → certificate-ledger + claim-classification-matrix + research-release-governance.

## 21. Skill Dependency Graph (maps/)

ANT ← latex, bibliographic-verification, certificate-ledger · PVG ← ANT, combinatorial-sieve, computational-number-theory, certificate-ledger · rigor ← latex, certificate-ledger, bibliographic-verification · polymath ← rigor, bibliographic-verification, certificate-ledger · numerical ← computational-number-theory, certificate-ledger · computational ← numerical, ANT, certificate-ledger · sieve ← ANT, PVG, certificate-ledger · operator ← rigor, spectral-operator-no-go · spectral ← operator, numerical, spectral-operator-no-go · bibliographic ← research-release-governance · certificate-ledger ← claim-classification-matrix · no-go ← certificate-ledger, research-release-governance · release ← claim-classification-matrix, what-not-to-import, no-go-memory.

## 22. Current Capabilities (maps/)

**يستطيع:** قراءة دالة كـ ANT object · ترجمتها PVG observable · تصنيف identity/diagnostic/open · ربطها بسلسلة/جداء أويلر · تحديد نوع الدعم · تحديد الحاجة لمتوسط/إلغاء/شهادة · قراءة الغربال طبقة معلومات · منع الادعاءات الزائدة · تسجيل قدرات الكتب · طابور أسئلة · تحديد الجدران والشهادات الناقصة.
**لا يستطيع:** إثبات RH/GRH · تحسين PNT بلا برهان · كسر parity · تحويل spectral analogy إلى Hilbert–Pólya proof · اعتبار قراءة Overholt/Tenenbaum إتقانًا كاملًا · نشر نتيجة بلا audit.

## 23. Skill Stack Map (maps/)

```text
Layer 0 Governance: bibliographic-verification, certificate-ledger, spectral-operator-no-go, research-release-governance
Layer 1 Writing/Rigor: latex, solve-math-rigorously
Layer 2 Core ANT: analytic-number-theory, computational-number-theory, numerical-assistant
Layer 3 PVG: prime-valuation-geometry, combinatorial-sieve
Layer 4 Spectral/Operator: operator-theory, spectral-analysis
Layer 5 Book Ledgers: BOOK-ANT-OVERHOLT-001, BOOK-ANT-TENENBAUM-002
Layer 6 Frontier: research-frontiers.jsonl, open-questions-queue.jsonl, no-go-memory.md
```

## 24. v0.1b Audit Checklist (audits/, AUDIT-CM-V01B-001)

Structure · 14 skill cards installed · registries updated (skills/books/research-frontiers/open-questions-queue) · Overholt safe-retrofitted + not-complete-mastery + no-new-theorem + no-RH/GRH · Tenenbaum partial through 004-Z + the four Tenenbaum diagnostic files + no-RH/GRH · governance files present · Safety (No PDFs · No raw text · No prompt dumps · No exact numbers without commands · every entry Registry ID · every claim classified · No RH/GRH · No Mileti started · No 005-A started) · Final: v0.1b PASS.

## 25. Definition of Done

14 بطاقات كلها + Registry IDs + حدود واضحة · skills.jsonl + books.jsonl مكتملان · Overholt safe-retrofitted · Tenenbaum partial حتى 004-Z + ملفاته الأربعة · ملفات الحوكمة · research-frontiers + open-questions-queue + no-go-memory + what-not-to-import · audit checklist · لا PDF/raw/prompt-dumps · لا RH/GRH progress · audit PASS.

## 26. ترتيب التنفيذ

goals → charter → claim-classification-matrix → certificate-funnel → book-import-protocol → what-not-to-import → no-go-memory → installed-skills → math cards → governance cards → skills.jsonl → Overholt ledger → Tenenbaum ledger → books.jsonl → research-frontiers → open-questions-queue → skill-stack-map → skill-dependency-graph → query-routing-guide → current-capabilities → audit checklist → audit → إغلاق إن PASS.

## 27. بعد v0.1b

`v0.2 = Mileti Logic Certificate Layer` ثم `v0.3 = Tenenbaum-005-A Dirichlet Characters as Residue-Fiber Observables`. لا انتقال قبل `v0.1b PASS`.

## 28. الخلاصة الحاكمة

نبني عقلًا رياضيًا بحثيًا قابلًا للتدقيق يعرف مهاراته وكتبه وحدوده وأسئلته المفتوحة وجدرانه وشهاداته الناقصة وما لا يجوز ادعاؤه، ويعرف متى تكون الفكرة تشخيصًا ومتى تصبح آلية مرشحة ومتى تستحق برهانًا. القانون النهائي:

```text
No registry, no entry.
No classification, no claim.
No certificate, no theorem.
No audit, no release.
No RH/GRH progress without proof certificate.
```

الالتزام: لا Mileti الآن · لا Tenenbaum-005-A الآن · لا توسع قبل إغلاق v0.1b.
