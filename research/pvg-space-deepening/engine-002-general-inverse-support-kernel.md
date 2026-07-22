# ENGINE-002 — النواة العامة للهندسة العكسية للدعم

**ID:** `ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL`  
**Goal:** `GOAL-OP-INVERSE-SUPPORT-KERNEL-001`  
**Parent:** `GOAL-PVG-INVERSE-GEOMETRY-001`  
**Scope:** Phase A — Inverse Support only  
**Classification:** exact compression laws + finite complete certification  
**Date:** 2026-07-22

## 1. السؤال

لوجه دعم أولي مستهدف \(F\)، نريد جميع الأوجه \(E\) التي تحقق:

\[
F\in\mathcal T(E),
\qquad
\mathcal T(E)=\{\operatorname{supp}(a+b):a,b\in E,\ a<b\}.
\]

التعداد الأمامي الخام يفحص كل وجه \(E\)، ثم يفحص كل زوج داخله. ENGINE-002 تستبدله بمولد عكسي يبدأ من بنية \(F\).

## 2. الصندوق المسجل

```text
target_prime_limit = 31
predecessor_prime_limit = 31
predecessor_face_sizes = 2,3,4
max_target_face_size = 4
complete_enumeration = true
```

عالم الأوليات هو:

\[
\{2,3,5,7,11,13,17,19,23,29,31\}.
\]

عدد أوجه السوابق الممكنة:

\[
\binom{11}{2}+\binom{11}{3}+\binom{11}{4}
=55+165+330=550.
\]

## 3. قانون حافة الشاهد

### المبرهنة التعريفية

\[
\boxed{
F\in\mathcal T(E)
\iff
\exists\,a,b\in E,\ a<b,
\operatorname{supp}(a+b)=F
}
\]

نسمي الزوج \(\{a,b\}\) **حافة شاهد** للهدف \(F\).

### البرهان

الاتجاهان هما نفس تعريف \(\mathcal T(E)\): عضوية \(F\) تعني وجود زوج داخل \(E\) يولد \(F\)، ووجود الزوج يعني أن \(F\) عنصر في عائلة الخلفاء. \(\square\)

### العائد الخوارزمي

بدل فحص كل زوج داخل كل وجه:

1. نبني حواف الشهود للهدف مرة واحدة؛
2. نوسع كل حافة بإضافة محاور أخرى؛
3. نزيل التكرار عندما يحتوي الوجه أكثر من حافة شاهد.

إذن كل سابق متعدد المحاور هو ببساطة وجه يحتوي حافة شاهد واحدة على الأقل.

**التصنيف:** `Identity / exact`.

## 4. قانون ليف الدعم

إذا كانت:

\[
\operatorname{supp}(a+b)=F=\{r_1,\ldots,r_k\},
\]

فإن:

\[
a+b=\prod_{j=1}^{k}r_j^{e_j},\qquad e_j\ge1.
\]

داخل عالم الأوليات حتى \(P\):

\[
a+b\le2P.
\]

لذلك لا نولد كل المجاميع، بل فقط أعداد ليف الدعم الدقيق تحت \(2P\).

مثال عند \(P=31\):

\[
F=\{2,3\}
\]

يعطي فقط:

\[
6,12,18,24,36,48,54
\]

تحت السقف \(62\)، بدل فحص كل عدد حتى 62.

**التصنيف:** `Known unique-factorization identity / exact`.

## 5. قانون توجيه الزوجية

للأوليين المختلفين:

- إذا كان \(2\in F\)، فالمجموع زوجي، والشاهد يجب أن يكون أوليين فرديين؛
- إذا كان \(2\notin F\)، فالمجموع فردي، والشاهد يجب أن يكون من الشكل:

\[
2+q.
\]

إذن الزوجية لا تستبعد الهدف دائمًا، لكنها تقسم البحث إلى قناتين منفصلتين بلا تداخل:

```text
2 in F     → odd + odd
2 not in F → 2 + odd
```

**التصنيف:** `Known parity law / exact routing`.

## 6. قانون حد الجذر

إذا كان:

\[
\operatorname{rad}(F)=\prod_{r\in F}r>2P,
\]

فلا يوجد عدد \(n\le2P\) له الدعم الدقيق \(F\). وبالتالي لا توجد حافة شاهد داخل عالم الأوليات حتى \(P\).

كذلك إذا كان:

\[
\max(F)>2P,
\]

فالهدف غير قابل للتحقق داخل الصندوق.

مثال:

\[
F=\{2,3,11\},
\qquad
\operatorname{rad}(F)=66>62.
\]

إذن هو غير قابل للوصول داخل الصندوق المسجل دون فحص أي زوج.

**التصنيف:** `Exact finite-box exclusion`.

## 7. الخوارزمية المضغوطة

```text
target support F
→ apply radical and axis bounds
→ generate exact-support sums n <= 2P
→ route by parity
→ realize n as distinct-prime witness edges
→ extend each witness edge to face sizes 2,3,4
→ deduplicate
→ attach forward certificate
```

الواجهة المنفذة:

```text
successors(face)
witness_edges(target, prime_limit)
predecessors(target, prime_limit, face_sizes)
predecessor_certificate(target, predecessor)
reachability_table(...)
```

## 8. شهادة الاكتمال

استعملنا Oracle مستقلًا:

1. تعداد جميع الأوجه الـ550؛
2. حساب جميع الأزواج داخل كل وجه؛
3. بناء \(\mathcal T(E)\) أماميًا؛
4. مقارنة قائمة السوابق لكل هدف مع المولد المضغوط.

عدد تقييمات الأزواج في التعداد الكامل:

\[
2530.
\]

المقارنة تمت لكل الأهداف الـ561 المكونة من أوليات حتى 31 وبحجم لا يتجاوز 4.

النتيجة:

```text
soundness = PASS
completeness = PASS
deduplication = PASS
determinism = PASS
multi-axis sizes 3 and 4 = PASS
```

هذا اكتمال داخل الصندوق فقط.

## 9. النتائج العددية

من بين 561 وجهًا مستهدفًا:

```text
reachable = 20
unreachable inside box = 541
```

توزيع الأهداف القابلة للوصول بحسب الحجم:

```text
size 1 = 7
size 2 = 11
size 3 = 2
size 4 = 0
```

الأهداف الثلاثية الوحيدة القابلة للوصول هي:

\[
\{2,3,5\},\qquad \{2,3,7\}.
\]

عدد علاقات السابق–الهدف بحسب حجم السابق:

```text
size 2 = 55
size 3 = 457
size 4 = 1656
```

هذه أعداد علاقات incidence، وليست أعداد أوجه فريدة في العالم كله.

## 10. مثال: الهدف {2,5}

أعداد ليف الدعم تحت 62:

\[
10,20,40,50.
\]

حواف الشهود داخل عالم الأوليات حتى 31 هي ست حواف. بعد توسيعها وإزالة التكرار نحصل على:

```text
binary predecessors = 6
ternary predecessors = 51
quaternary predecessors = 182
total = 239
```

مثلًا:

\[
\{3,7,11\}
\]

سابق للهدف لأن الحافة \(\{3,7\}\) تحقق:

\[
3+7=10,
\qquad
\operatorname{supp}(10)=\{2,5\}.
\]

## 11. معنى unreachable

عندما نسجل وجهًا `unreachable` فالمعنى الدقيق هو:

> لا يوجد وجه سابق من أوليات لا تتجاوز 31، وبحجم 2 أو 3 أو 4، يولد الهدف داخل تعريف الانتقال الحالي.

لا يعني ذلك استحالة عالمية؛ قد يظهر سابق عند أوليات أكبر أو حجم وجه أكبر.

## 12. العائد العلمي

ENGINE-002 ليست مجرد تسريع برمجي. لقد كشفت التحليل البنيوي التالي:

1. المسألة العكسية محكومة برسم حواف شاهد؛
2. السوابق متعددة المحاور هي توسعات hypergraph لحواف الشهود؛
3. ليف الدعم يفصل العامل الضربي عن اختيار الأزواج الأولية؛
4. عدم الوصول داخل صندوق يمكن أن يحمل شهادة قصيرة قبل التعداد؛
5. يمكن تخزين مولد وشهادة بدل تخزين كل الحسابات الخام.

لكننا لم ننتج بعد لمّة ANT أو تقديرًا تحليليًا جديدًا.

## 13. ما لم يُفعل

- لم نبحث عن عمق 13؛
- لم نفتح Integer Fibers بوصفها مرحلة مستقلة؛
- لم نستخدم غولدباخ؛
- لم نثبت وصولًا أو استحالة عامة؛
- لم نوسع الصندوق بعد رؤية النتائج؛
- لم نفتح ENGINE-003.

## 14. الملفات

```text
tools/pvg_inverse_support_kernel.py
tests/test_pvg_inverse_support_kernel.py
research/pvg-space-deepening/data/inverse-support-kernel-summary.json
.github/workflows/pvg-inverse-support-kernel-audit.yml
```

## 15. السقف العلمي

النتائج exact هي قوانين الضغط والتكافؤ مع حافة الشاهد. الأعداد والتصنيفات reachable/unreachable منتهية ومقيدة بالصندوق. لا توجد مبرهنة ANT أصلية، ولا تقدم في غولدباخ أو PNT أو RH أو GRH.

**Honest classification:** exact inverse-support compression laws with complete finite-box certification.
