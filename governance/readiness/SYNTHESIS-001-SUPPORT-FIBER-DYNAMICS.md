# SYNTHESIS-001 — Support-Fiber Dynamics Readiness Card

```text
TASK-ID: SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS
Title: Synthesize support-fiber dynamics before further search
Research front: PVG-SUPPORT-FIBER-DYNAMICS-SYNTHESIS-001
Strategic-goal link: GOAL-PVG-ANT-STRATEGIC-001
Parent goals: GOAL-PVG-ADDITIVE-DYNAMICS-001; GOAL-PVG-ANT-ADDITIVE-BRIDGE-001
Owner/status: project owner / READY and active_current
Date/version: 2026-07-22 / v1
```

## 1. Research question

ما النظرية المنتهية النظيفة التي أنتجتها PASS-013–024 حول ديناميكيات أوجه الدعم وألياف المجموع، وما الفرق بين القضايا الناتجة مباشرة من التعريف، والنتائج الحسابية المحدودة، والأسئلة المفتوحة، وكيف تترجم هذه البنية عكسيًا إلى لغة ANT؟

## 2. Required output

```text
identity + structural synthesis + finite certificate map + open-question map
```

## 3. Success and stop rules

- **Success criterion:** وثيقة تركيب واحدة توحد التعريفات والقضايا exact والأمثلة وفقد المعلومات والنتائج finite والأسئلة المفتوحة، مع ربط واضح بالملفات والشهادات.
- **Negative/blocked criterion:** إذا تعذر توحيد المصطلحات دون تناقض، يسجل التعارض ويوقف PASS-025 حتى الإصلاح.
- **Claim ceiling:** لا ادعاء أصالة تاريخية، ولا انتهاء عام، ولا حد عالمي للعمق، ولا قانون نمو، ولا تقدم في غولدباخ أو PNT أو RH أو GRH.
- **Out of scope:** رفع سقف الحساب، البحث عن عمق 12، فتح PASS-025، كتابة ورقة نشر، أو formalization جديد.

## 4. PVG–ANT route

- **Classical ANT object:** تمثيلات عدد كمجموع أوليين، دوال التمثيل، دعم الأعداد، والتحليل الجمعي.
- **Multiplicative core:** تحليل `p+q` إلى عوامله الأولية ودعمه.
- **PVG encoding:** الوجه الثنائي `{p,q}`، إسقاط دعم المجموع، والمدار في فضاء الوجوه.
- **Geometric decomposition sought:** ألياف المجموع، ألياف الدعم، أحواض الجذب، شجرة السوابق، وعمق الإغلاق.
- **Analytic transform:** غير مطلوب لإغلاق التركيب؛ يجب فقط تسمية الجسور الممكنة إلى الالتفاف وفورييه والشخصيات ودوال التمثيل.
- **Candidate transfer lemma:** مؤجل؛ التركيب يجب أن يحدد أين يمكن صياغته دون ادعاء إثبات.
- **Reverse translation to ANT:** كل ليف دعم يجمع أعدادًا وتمثيلات أولية ذات ذيل مداري واحد.
- **PVG-necessity test:** تحديد ما إذا كانت لغة الألياف/الدعم تعطي ضغطًا أو تصنيفًا لا يظهر بوضوح في الصياغة الزوجية الخام.

## 5. Prerequisite graph

| Prerequisite | Load-bearing? | State | Exact version needed | Source | Acquisition action |
|---|---:|---|---|---|---|
| PASS-013–019 definitions and finite dynamics | yes | A | branch evidence | `research/pvg-space-deepening/` | reuse |
| PASS-020–021 visual explanation | no | A | current pages | `web/pvg-pareto-explorer/` | use examples only |
| PASS-022–024 depth and support-fiber results | yes | A | registered summaries | data and pass docs | reuse and cross-check |
| Full PVG versus support projection distinction | yes | B | explicit loss map | goals and synthesis | write precisely |
| ANT reverse bridge | yes | B | bounded formulation | addition-fiber and language-kernel work | integrate, do not overclaim |
| Historical originality | no for synthesis | D | independent literature audit | future | defer and label |

States:

```text
A operationally_ready
B known_but_needs_activation
C source_available_not_extracted
D missing
```

## 6. Tool activation

| Tool | Required? | Scientific function | Output/certificate |
|---|---:|---|---|
| Lean | no | no new proof target | none |
| Python | yes, bounded | regenerate examples and consistency checks | synthesis audit |
| R | no | no statistical claim | none |
| literature search | later | originality and related work | deferred audit |
| symbolic/numerical experiment | no new experiment | use registered evidence only | cited summaries |

## 7. Knowledge acquisition package

No new book or broad mining pass is authorized. Only targeted retrieval is permitted if a definition or known antecedent must be checked during the synthesis.

## 8. Readiness decision

```text
READY
```

Reason: all load-bearing finite evidence exists, local PASS-023 tests were reproduced by the owner, PASS-024 CI passed, and the remaining work is consolidation, loss auditing, and reverse-link organization rather than new computation.

## 9. Execution plan

1. Freeze a common notation for valuation vector, support, face, transition, orbit, closure, sum fiber, and support fiber.
2. State and prove from definitions the exact two-axis and fiber identities.
3. Give simple examples: `10,20,24,706,1774`.
4. Separate full PVG from support-projected dynamics and record lost exponents.
5. Register finite findings through PASS-024 with explicit bounds.
6. Translate the objects back to ANT representation language.
7. Produce an `exact / finite / reinterpretation / candidate / open` matrix.
8. Run consistency and goal-memory audits.
9. Close SYNTHESIS-001 before activating PASS-025.

## 10. Failure points

- confusing `ν(n)` with `supp(n)`;
- treating an observed depth ladder as a growth law;
- treating prime-pair representations as Goldbach progress;
- claiming historical novelty without literature search;
- opening PASS-025 before the synthesis closure review.

## 11. Deliverables

- `research/pvg-space-deepening/synthesis-001-support-fiber-dynamics.md`
- exact proposition and example registry inside the document;
- loss map: full valuation versus support projection;
- finite/open classification matrix;
- closure review and knowledge-return links.

## 12. Closure review

- **Result class:** pending.
- **Maturity before/after:** L2–L4 consolidation.
- **Reusable bridge or lemma produced:** pending exact fiber propositions and reverse ANT bridge.
- **Knowledge returned to mind:** language kernel, goal registry, and additive-dynamics map.
- **Next ceiling:** PASS-025 targeted reverse-preimage search only after closure.
- **Work stopped or superseded:** blind sum-cap expansion is stopped.

**Honesty note:** readiness is a task-specific operational judgment, not a claim of mastery or originality.
