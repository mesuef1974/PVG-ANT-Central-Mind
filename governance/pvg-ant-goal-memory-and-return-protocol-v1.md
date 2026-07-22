# PVG–ANT Goal Memory and Return Protocol v1

**ID:** `PVG-ANT-GOAL-MEMORY-RETURN-PROTOCOL-001`  
**Authority:** subordinate to the honesty ceiling, proof certificates, and the Research Operating Charter  
**Machine truth:** `registries/program-goals.jsonl` and `registries/goal-links.jsonl`  
**Classification:** Governance / Research Program — no mathematical theorem  
**Date:** 2026-07-22

## 1. Purpose

هذا البروتوكول يمنع ضياع الأهداف عندما يظهر مسار جانبي مفيد أو تجربة مثيرة. يسمح بالاستكشاف، لكنه يفرض أن يكون الاستكشاف مرتبطًا بهدف أب، محدودًا بمعيار توقف، وأن ينتهي بعودة صريحة إلى المسار الحاكم.

## 2. Non-loss invariant

لا يُحذف هدف من الذاكرة الحاكمة لأن:

- تجربة فشلت؛
- جبهة جديدة بدت أكثر إثارة؛
- أداة جديدة أصبحت متاحة؛
- توسع الحساب أعطى أمثلة أكثر؛
- ظهرت حاجة مؤقتة إلى Lean أو كتاب أو مختبر بصري.

يُغيّر الهدف إلى حالة مسجلة، ويحتفظ بسبب الحالة ودليلها ونقطة العودة.

## 3. Goal classes

```text
strategic_goal
general_goal
operational_goal
supporting_program
```

- `strategic_goal`: واحد ثابت.
- `general_goal`: طويل المدى، ولا ينافس الجبهة النشطة.
- `operational_goal`: جبهة قابلة للإغلاق؛ واحدة فقط تبدأ حالتها بـ`active`.
- `supporting_program`: معرفة أو formalization أو عرض أو بنية تحتية، لا تفتح سؤالًا بحثيًا ثانيًا.

## 4. Required fields for every goal

```text
kind
id
title
status
deliverable
exit_criterion
maturity_target
claim_ceiling
classification
source
parent_goal_ids
return_to_goal_ids
```

وكل هدف تشغيلي يحمل أيضًا:

```text
research_front
prerequisites
blocked_by
next_review
return_gate
```

## 5. Detour card

أي خروج عن الجبهة الأصلية يجب أن يسجل قبل التنفيذ:

```text
Detour-ID:
Parent goal:
Active operational goal:
Reason:
Measurable deliverable:
Stop condition:
Claim ceiling:
Knowledge-return destination:
Return-to goal:
Return gate:
Maximum passes or time window:
```

لا يكفي القول إن المسار “قد يكون مفيدًا”. يجب تسمية الفائدة القابلة للاختبار.

## 6. Mandatory return rule

عند إغلاق هدف جانبي لا توجد ثلاثة خيارات مفتوحة بلا ضبط. يجب اختيار واحد فقط وتسجيله:

1. `return`: العودة إلى الهدف المسجل؛
2. `close_parent`: إغلاق الهدف الأب بشهادة؛
3. `bounded_extension`: تمديد محدود جديد مع سبب ودليل وشرط توقف جديد.

`bounded_extension` لا يورث نفسه تلقائيًا. لا PASS جديد بلا Stage Review.

## 7. One-active-front enforcement

يجب أن يحتوي `program-goals.jsonl` على هدف تشغيلي واحد فقط حالته تبدأ بـ`active`.

الإصلاحات الآتية يمكن أن تجري بالتوازي ولا تعد جبهة أصلية ثانية:

- CI;
- توثيق؛
- تصحيح خطأ؛
- مزامنة؛
- حفظ شهادة؛
- تنسيق عرض؛
- تدقيق هدف وذاكرة.

لكنها لا يجوز أن تولد سؤالًا رياضيًا جديدًا دون تحويل رسمي للجبهة النشطة.

## 8. Goal graph

`registries/goal-links.jsonl` يسجل العلاقات:

```text
serves
returns_to
```

- `serves`: يبين الهدف الأب.
- `returns_to`: يبين المسار الذي يجب استئنافه أو تقييمه بعد الإغلاق.

كل معرف في الرسم يجب أن يوجد في `program-goals.jsonl`.

## 9. Stage Review gate

بعد كل PASS أو SYNTHESIS أو theorem attempt:

1. تحقق من المخرج ومعيار الإغلاق.
2. صنف النتائج: `Known / Identity / Reinterpretation / Diagnostic / Boundary / Candidate Mechanism / New Lemma / New Theorem`.
3. افصل exact عن finite وعن open.
4. سجل الأدلة والمسارات والحدود.
5. أعد المعرفة القابلة لإعادة الاستخدام إلى النواة.
6. حدث حالات الأهداف.
7. قرر العودة أو التمديد المحدود.
8. امنع الجبهة التالية إذا بقي الهدف الحالي بلا إغلاق.

## 10. Current controlled sequence

```text
ACTIVE:
GOAL-OP-SUPPORT-FIBER-SYNTHESIS-001

NEXT, ONLY AFTER CLOSURE:
GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001 / PASS-025

MANDATORY RETURN CHECKPOINT:
GOAL-OP-ONE-THEOREM-001
```

بعد PASS-025 لا يسمح بفتح PASS-026 تلقائيًا. يجب أن تقرر مراجعة المرحلة هل:

- النتائج ناضجة لتغذية برنامج المبرهنة؛
- يوجد امتداد محدود واحد مبرر؛
- المسار أغلق بشهادة سلبية أو حدود واضحة.

## 11. Relationship to adjacent programs

### ANT encyclopedia

برنامج معرفة داعم. يجب أن تعود المبرهنات والأدوات المستخرجة إلى العقد التشغيلية. عدد الفصول ليس مقياس تقدم بحثي.

### Lean

برنامج تحقق داعم. لا يفتح pass إلا لخدمة بنية قابلة لإعادة الاستخدام أو لمّة نشطة.

### Visual and structural laboratories

تخدم الاكتشاف والتفسير والتفنيد. لا ترفع نتيجة finite إلى theorem.

### Specialist mind and future neural system

الهدف طويل المدى هو عقل متخصص، لكن لا توجد شبكة عصبية مدربة ولا corpus معتمد حاليًا. لا يتحول جمع البيانات إلى هدف بديل عن الفجوة التحليلية.

### Outreach and narrative

التواصل والرواية والشرح مشاريع داعمة منفصلة عن سقف الادعاء الرياضي.

## 12. Memory update rule

ذاكرة المشروع الدائمة تُحدّث عبر:

1. `central-mind-goals.md`;
2. `registries/program-goals.jsonl`;
3. `registries/goal-links.jsonl`;
4. readiness card للجبهة النشطة؛
5. closure أو Stage Review عند الانتقال؛
6. CI audit.

المحادثة وحدها ليست ذاكرة حاكمة، وPR description وحده ليس مصدر الحقيقة.

## 13. Failure conditions

يفشل تدقيق الأهداف إذا:

- تعددت الأهداف التشغيلية النشطة؛
- وجد معرف مكرر؛
- أشار prerequisite أو link إلى هدف غير موجود؛
- كان هدف paused بلا `return_gate`;
- كان هدف queued بلا prerequisites؛
- غابت نقطة عودة من جبهة مؤقتة؛
- لم تكن SYNTHESIS-001 الجبهة الحالية المسجلة؛
- لم يسجل PASS-025 بوصفه التالي فقط لا النشط؛
- اختفى ONE-THEOREM-001 من نقطة العودة الإلزامية.

## 14. Scientific ceiling

هذا البروتوكول يحكم العمل ولا يثبت نتيجة رياضية. لا يمنح الأصالة، ولا يحول roadmap إلى برهان، ولا يغير سقف Goldbach أو PNT أو RH أو GRH.

**Honest classification:** Governance / Project Memory / Goal Traceability.
