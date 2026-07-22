# PVG–ANT Central Mind — Research Operating Charter v1.0

مستودع عقل رياضي تراكمي وبحثي. المعرفة لا تدخل بوصفها رصيدًا ساكنًا، بل تتحول عند الحاجة إلى **لغة + جسر + أداة + لمّة + شهادة + معرفة تشغيلية قابلة لإعادة الاستخدام**.

## Supreme law

\[
\boxed{
\text{Geometry}
\leftrightarrow
\text{Analysis}
\leftrightarrow
\text{Certificate}
}
\]

ويضاف إليها مسار البحث الحاكم:

\[
\boxed{
\text{Translation}
\rightarrow
\text{Original Question}
\rightarrow
\text{Lemma}
\rightarrow
\text{Proof/Test}
\rightarrow
\text{Certificate}
\rightarrow
\text{Reusable Knowledge}
}
\]

## Strategic identity

هذا المشروع ليس مشروع تلخيص كتب، ولا تجميع أدوات، ولا formalization لذاته، ولا مختبر تعلم آلي عام.

هدفه:

> تطوير هندسة التقييمات الأولية إلى لغة بحثية تشغيلية ثنائية الاتجاه مع نظرية الأعداد التحليلية، ثم استعمالها لاكتشاف وإثبات مساهمات أصلية صحيحة — ولو صغيرة — في ANT.

## Testable strategic hypothesis

قد تبسط PVG أجزاء من البنية الضربية عبر linearization، decomposition، localization، أو transfer principles. هذه فرضية برنامج تُختبر في كل جسر، ولا تُفترض صحيحة في كل مسألة.

كل ترجمة تسجل مكسبها:

```text
none | expository | structural | analytic | proof-producing
```

إعادة التسمية أو الصورة الأوضح ليست مبرهنة ولا أصالة.

## Task-first operation

لا يبدأ كتاب، تعدين معرفة، Lean pass، تجربة، Python، R، أو بحث أدبي بلا مهمة بحثية مسماة.

كل مهمة تمر عبر:

1. `Research Readiness Card`؛
2. prerequisite audit؛
3. targeted knowledge activation؛
4. execution؛
5. certificate؛
6. knowledge return.

وجود المصدر محليًا لا يعني دمجه، ودمجه لا يعني أنه `operationally_ready` للمهمة الحالية.

## One active research front

جبهة بحث أصلية واحدة فقط تكون نشطة في كل وقت. يجوز بالتوازي إصلاح حوكمة أو CI أو مصدر، بشرط ألا ينشئ سؤالًا بحثيًا ثانيًا.

## Goal memory and mandatory return

لا يُحذف هدف سابق بسبب ظهور مسار جديد. كل انحراف مؤقت يسجل الهدف الأب، المخرج، شرط التوقف، سقف الادعاء، ونقطة العودة.

بعد كل PASS أو SYNTHESIS أو محاولة مبرهنة يجب تنفيذ `Stage Review` يقرر واحدًا من:

```text
return | close_parent | bounded_extension
```

لا يفتح امتداد جديد تلقائيًا. الحقيقة الآلية للأهداف في `registries/program-goals.jsonl`، وعلاقات الخدمة والعودة في `registries/goal-links.jsonl`.

## Language kernel

يبني العقل `PVG–ANT Language Kernel` مرة واحدة ويعيد استعماله. الجسر المعتمد لا يعاد بناؤه من الصفر. كل جسر جديد يسجل الخريطة الأمامية، العكس أو فقد المعلومات، التحويل التحليلي، المكسب، الأدبيات، والتصنيف.

## Knowledge and tools on demand

- الكتب والمصادر: للحد الأدنى الكافي للمهمة؛
- Lean: للمّات النشطة والبنى القابلة لإعادة الاستخدام؛
- Python: للبناء والتحقق والتفنيد وإعادة الإنتاج؛
- R: لتنفيذ إحصائي مستقل عندما تتطلبه الشهادة؛
- الأدبيات: للأولوية والشروط وأفضل النطاقات؛
- التجربة: لاكتشاف أو تفنيد نمط، لا لتعويض البرهان.

كل معرفة مكتسبة تعود إلى العقل بصيغة تشغيلية.

## Maturity ladder

```text
L0 Vocabulary
L1 Exact translation
L2 Structural simplification
L3 Transfer principle
L4 Research mechanism
L5 Original lemma
L6 Original theorem
L7 Reusable research program
```

بعد إغلاق مستوى، يرتفع سقف المطلوب. تكرار مخرجات المستوى نفسه لا يعد تقدمًا استراتيجيًا إلا إذا كان جزءًا من kernel release محدد مسبقًا.

## Goal architecture

- **Strategic:** ثابتة ولا تتغير إلا بقرار صريح.
- **General:** طويلة المدى.
- **Operational:** مرنة، قابلة للإضافة والتحديث بعد Stage Review.
- **Supporting:** معرفة أو تحقق أو عرض يخدم الجبهة ولا ينافسها.

كل هدف تشغيلي يحمل مخرجًا قابلًا للقياس، معيار إغلاق، prerequisites، claim ceiling، maturity target، حالة، هدفًا أبويًا، ونقطة عودة في `registries/program-goals.jsonl`.

## Stage review

بعد كل مرحلة لا يعاد تعريف المشروع. تُراجع فقط:

- المعرفة التشغيلية الجديدة؛
- الجسور القابلة لإعادة الاستخدام؛
- ما كان مجرد reinterpretation؛
- ما صمد كلمّة أو آلية؛
- ما فشل وشهادته؛
- prerequisites المرحلة التالية؛
- السقف الأعلى التالي؛
- حالة الهدف ونقطة العودة.

## Strategic success criterion

\[
\boxed{
\text{One original, correct, modest ANT theorem in which PVG contributes materially}
}
\]

تسبق ذلك نتائج أصغر مقبولة: هوية، متباينة، لمّة نقل، نتيجة متوسطية، تصنيف، أو شهادة استحالة أصلية.

## Ceiling

```text
No RH/GRH progress without a complete proof certificate.
Translation is not proof.
Experiment is not proof.
Formalization does not create originality.
A book count is not a research metric.
A Candidate Mechanism requires literature and certificate gates.
A deeper finite orbit is not a global depth theorem.
A prime-sum representation is not Goldbach progress by itself.
```

## Governing references

- `central-mind-goals.md`
- `governance/pvg-ant-research-compass-v1.md`
- `governance/pvg-ant-goal-memory-and-return-protocol-v1.md`
- `maps/pvg-ant-language-kernel-v1.md`
- `governance/task-triggered-knowledge-activation-policy.md`
- `governance/stage-review-and-ceiling-escalation-policy.md`
- `governance/templates/research-readiness-card.md`
- `registries/program-goals.jsonl`
- `registries/goal-links.jsonl`

## Repository invariants

1. Markdown للعرض، JSONL للحقيقة، والحراس للإنفاذ.
2. لا ID بلا سجل، ولا ادعاء بلا تصنيف، ولا ترقية بلا شهادة.
3. لا PDF متعقب.
4. لا مفهوم مكرر.
5. لا مصدر كتاب غير موثق.
6. هدف بحث أصلي نشط واحد فقط.
7. لا مهمة بحثية بلا readiness gate ومعيار إغلاق.
8. لا معرفة جديدة بلا عودة تشغيلية إلى العقل.
9. لا هدف مؤجل بلا نقطة عودة.
10. لا PASS جديد بلا Stage Review أو إغلاق مسجل.
11. لا حذف لهدف؛ يستخدم `closed` أو `blocked` أو `superseded_with_reason`.
12. لا تتقدم الأدوات أو التصورات بوصفها بديلًا عن اللمّة أو البرهان.

**Honest classification:** Governance / Research Program. No theorem. No RH/GRH progress.
