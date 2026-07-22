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
CLOSED:
GOAL-OP-SUPPORT-FIBER-SYNTHESIS-001
GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001 / PASS-025

PASS-025 OUTCOME:
DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS
source pair = {2,27397961}

STAGE DECISION:
return

RETURNED ACTIVE GOAL:
GOAL-OP-ONE-THEOREM-001 = active_external_validation_hold

NO AUTHORIZED NEXT PASS:
PASS-026 = NOT AUTHORIZED
```

حقق PASS-025 مخرجه المحدد وأغلق بشهادة. لا يوجد امتداد حسابي تلقائي بعده. تعود الجبهة الحاكمة إلى برنامج المبرهنة، الذي يبقى في انتظار التحقق الخارجي وفق بروتوكول P8.

النتيجة المعادة إلى العقل هي:

- مولد السوابق العكسية؛
- الربط الأحادي بين وجه السلف وبذرة مجموعه؛
- شاهد منتهٍ للعمق 12؛
- فصل واضح بين آلية توليد المرشحين وبين لمّة ANT التحليلية المفقودة؛
- منع الانتقال إلى PASS-026 لمجرد نجاح البحث المنتهي.

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
- لم تكن SYNTHESIS-001 مغلقة بشهادة؛
- لم تكن PASS-025 مغلقة بشهادة وشاهد مسجل؛
- لم تعد الجبهة إلى ONE-THEOREM-001؛
- ظهر PASS-026 بوصفه مخططًا أو مصرحًا؛
- اختفت حالة P8 الخارجية أو جرى إرسال حزمة جديدة دون تفويض المالك.

## 14. Scientific ceiling

هذا البروتوكول يحكم العمل ولا يثبت نتيجة رياضية. شاهد العمق 12 نتيجة منتهية داخل فئة بحث مجمدة ومعلومة التلوث، وليس مبرهنة في عدم محدودية الأعماق أو انتهاء المدارات. لا يمنح البروتوكول الأصالة، ولا يحول roadmap إلى برهان، ولا يغير سقف Goldbach أو PNT أو RH أو GRH.

**Honest classification:** Governance / Project Memory / Goal Traceability.
