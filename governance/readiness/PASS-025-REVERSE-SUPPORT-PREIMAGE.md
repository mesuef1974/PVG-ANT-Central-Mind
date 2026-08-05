# PASS-025 — Reverse Support-Preimage Generator Readiness Card

```text
TASK-ID: PASS-025-REVERSE-SUPPORT-PREIMAGE
Title: Generate reverse support preimages and run one bounded depth-12 search
Research front: PVG-REVERSE-SUPPORT-PREIMAGE-001
Strategic-goal link: GOAL-PVG-ANT-STRATEGIC-001
Parent goals: GOAL-PVG-ADDITIVE-DYNAMICS-001; GOAL-PVG-ANT-ADDITIVE-BRIDGE-001
Owner/status: project owner / READY and active_current
Date/version: 2026-07-22 / v1
```

## 1. Research question

هل يمكن بناء مولد عكسي من وجه دعم مستهدف إلى أوجه وأعداد سابقة، ثم استعماله في بحث منتهٍ موجه لاستخراج أول شاهد مسجل لعمق الإغلاق 12، أو شهادة غياب منتهية داخل سقف ثابت معلن؟

## 2. Required output

```text
reverse generator
+ ranked support candidates
+ fixed-cap realization search
+ depth-12 witness OR finite negative certificate
+ Stage Review
```

## 3. Exact starting point

SYNTHESIS-001 ثبت من التعريف:

\[
\mathcal T(\{p,q\})=\{\operatorname{supp}(p+q)\}.
\]

ولوجه دعم:

\[
F=\{r_1,\ldots,r_k\},
\]

تكون الأعداد ذات الدعم الدقيق \(F\) من الشكل:

\[
n=\prod_{j=1}^{k}r_j^{e_j},\qquad e_j\ge1.
\]

PASS-025 يجب أن يستعمل هاتين الهويتين عكسيًا بدل رفع سقف المجاميع خطيًا.

## 4. Success and stop rules

- **Success A:** العثور على زوج أوليين مختلفين ذي عمق إغلاق 12، مع شهادة المدار كاملة وأصغر حد أولي داخل النطاق المسجل.
- **Success B:** عدم العثور عليه، مع شهادة غياب منتهية توضح جميع أوجه الدعم والأعداد والتمثيلات المفحوصة والسقوف.
- **Stop condition:** تشغيل واحد بعد تجميد السقوف داخل الأداة والملخص المسجل. لا تمدد تكيفي للسقف في المرور نفسه.
- **Claim ceiling:** نتيجة منتهية فقط؛ لا انتهاء عام، ولا عدم انتهاء، ولا قانون نمو، ولا تقدم غولدباخ.
- **Out of scope:** PASS-026، formalization، broad literature mining، تدريب نموذج، أو تغيير تعريف الإغلاق.

## 5. Required frozen configuration

قبل التشغيل المسجل يجب أن يحفظ الملخص:

```text
target_prime_pair_closure_depth = 12
reverse_support_depth_budget
candidate_support_node_cap
candidate_integer_cap
prime_pair_realization_cap
orbit_verification_depth_cap
ranking_rule
pruning_rules
```

لا يجوز تعديل هذه القيم بعد رؤية النتائج إلا في PASS جديد يمر عبر Stage Review.

## 6. Reverse-generation route

```text
target deep support face
← support predecessors E with target in T(E)
← integers n with supp(n)=E
← distinct-prime representations p+q=n
← exact forward orbit verification
← earliest exposing prime limit
```

## 7. Ranking rules

ترتب المرشحات مبدئيًا بحسب:

1. العمق المتبقي المتوقع من الذيل المعروف؛
2. حجم الوجه السابق؛
3. radical وكتلة الأعداد الأصغر داخل ليف الدعم؛
4. وجود تمثيل أولي مختلف داخل السقف؛
5. أصغر حد أولي يكشف المرشح؛
6. عدم تكرار ذيل مداري مخزن.

الترتيب أداة كفاءة، وليس ادعاءً احتماليًا أو مبرهنة.

## 8. Prerequisites

| Prerequisite | State | Source |
|---|---|---|
| SYNTHESIS-001 definitions and closure | ready | `governance/closures/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS-CLOSURE.md` |
| PASS-024 support-fiber cache and depth-11 witness | ready | PASS-024 tool, tests, summary |
| exact factorization/support routines | ready | existing Python tools |
| prime-pair realization search | ready | PASS-024 sieve and closest-pair logic |
| fixed-cap configuration | must be frozen before registered run | PASS-025 tool output |
| historical originality audit | not required for finite search | deferred |

## 9. Verification package

PASS-025 must include:

- Python tool;
- dedicated unit tests;
- registered JSON summary;
- research note;
- CI regeneration equality;
- forward-orbit verification of every promoted witness;
- comparison with PASS-024 depth ladder;
- detached-worktree integration;
- closure or negative-certificate review.

## 10. Return gate

After PASS-025:

```text
PASS-026 = NOT AUTHORIZED
```

The Stage Review must choose:

1. return to `GOAL-OP-ONE-THEOREM-001`;
2. close the additive-dynamics parent with a certificate;
3. authorize one bounded extension with new evidence, fixed cap, and stop rule.

## 11. Readiness decision

```text
READY
```

Reason: the exact reverse identities, forward verifier, support-fiber cache, and bounded-governance structure are installed. The first implementation action is to freeze the configuration, not to run an open-ended search.

## 12. Scientific ceiling

PASS-025 can produce only a finite witness or finite absence certificate. It cannot by itself prove general termination, unbounded depth, an asymptotic law, Goldbach, PNT, RH, GRH, or historical originality.

**Honest classification:** task-specific readiness for a bounded computational diagnostic.
