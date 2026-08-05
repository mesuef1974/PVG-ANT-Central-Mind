# ENGINE-002 — General Inverse Support Kernel Readiness Card

```text
TASK-ID: ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL
Operational goal: GOAL-OP-INVERSE-SUPPORT-KERNEL-001
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Return goal: GOAL-OP-ONE-THEOREM-001
Date/version: 2026-07-22 / v1
Decision: READY
```

## 1. Purpose

العودة إلى محرك الهندسة العكسية ببناء نواة عامة للمرحلة A، بدل فتح بحث جديد عن عمق أكبر. يجب أن تستقبل النواة وجه دعم مستهدفًا \(F\)، وتولد سوابق دعم \(E\) تحقق:

\[
F\in\mathcal T(E),
\qquad
\mathcal T(E)=\{\operatorname{supp}(a+b):a,b\in E,\ a<b\}.
\]

PASS-025 أثبتت صلاحية خط أنابيب خاص بسوابق ثنائية ضمن فئة مجمدة. ENGINE-002 تعمم واجهة السوابق نفسها وتدقق اكتمالها داخل صناديق منتهية صغيرة.

## 2. Scope

```text
Phase A only: Inverse Support
binary and multi-axis predecessor faces
finite prime universe
finite predecessor-face cardinality
exact forward verification
reachable / unreachable classification inside the frozen box
```

خارج النطاق:

- البحث عن عمق 13؛
- رفع سقف PASS-025؛
- ألياف أعداد كبيرة؛
- ألياف أولية أو غولدباخ؛
- Phase E التحليلية؛
- مبرهنة انتهاء أو وصول عام؛
- PASS-026 بالمعنى القديم.

## 3. Frozen first box

يجب أن يبدأ التنفيذ المسجل الأول بالصندوق:

```text
target_prime_limit = 31
predecessor_prime_limit = 31
predecessor_face_sizes = 2,3,4
max_target_face_size = 4
complete_enumeration = true
```

لا تعدل الحدود بعد رؤية النتائج داخل التشغيل المسجل.

## 4. Deliverables

- `tools/pvg_inverse_support_kernel.py`؛
- API موحد:

```text
successors(face)
predecessors(target, prime_limit, face_sizes)
predecessor_certificate(target, predecessor)
reachability_table(prime_limit, face_sizes)
```

- اختبارات brute-force مستقلة تقارن المولد العكسي بالتعداد الأمامي الكامل؛
- جدول درجات الدخول والتفرع؛
- تصنيف reachable / unreachable داخل الصندوق فقط؛
- شهادات لكل سابق مولد؛
- مذكرة `engine-002-general-inverse-support-kernel.md`؛
- JSON مسجل قابل لإعادة التوليد؛
- CI وStage Review.

## 5. Success criteria

1. **Soundness:** كل سابق مولد يحقق \(F\in\mathcal T(E)\).
2. **Completeness inside box:** تتطابق قائمة المولد مع brute-force enumeration تمامًا.
3. **Deduplication:** لا سابق مكرر.
4. **Determinism:** ترتيب ثابت ومخرجات JSON متطابقة.
5. **Multi-axis evidence:** وجود اختبارات فعلية لوجوه بحجم 3 و4، لا واجهة شكلية فقط.
6. **Negative certificates:** كل وجه مصنف unreachable داخل الصندوق يحمل حدود الصندوق صراحة.

## 6. Stop rule

تغلق ENGINE-002 بعد نجاح الصندوق الأول وشهادة الاكتمال، سواء كشفت بنية مثيرة أم لا. لا توسع الحدود تلقائيًا ولا تنتقل إلى Phase B دون Stage Review وreadiness card جديد.

## 7. Return gate

بعد الإغلاق يجب اختيار أحد الآتي:

```text
return to GOAL-OP-ONE-THEOREM-001
close Phase A as sufficient foundation
open one bounded Phase B task only if a named theorem/transfer need exists
```

لا يفتح بحث عمق جديد تلقائيًا.

## 8. Claim ceiling

الاكتمال يعني الاكتمال داخل الصندوق المجمد فقط. unreachable يعني عدم وجود سابق ضمن عالم الأوليات وأحجام الوجوه المحددة، وليس استحالة عالمية. المحرك أداة هندسية؛ لا ينتج وحده مبرهنة ANT أو تقدمًا في غولدباخ أو PNT أو RH أو GRH.

**Honest classification:** bounded inverse-support infrastructure and finite exact certification.
