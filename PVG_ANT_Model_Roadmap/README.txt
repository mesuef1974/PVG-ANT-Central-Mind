PVG–ANT Research System — Governing Roadmap v2.2 Dual-Track (Sync-Governed)
(supersedes v2.1, retired to historical/index-v2.1-superseded.html)

افتح index.html في Chrome أو Edge.

هذه النسخة تستبدل الخطة الأصلية وتفرض الترتيب التالي:
1) إغلاق الاستمرارية وقرار P8 قبل 19 يوليو 2026.
2) تصميم وختم Benchmark 002 A/B.
3) تشغيل A على العقل الحالي وتجميد خريطة الأخطاء قبل أي تدريب.
4) اختيار المعمارية وبناء corpus موجهة بالأخطاء فقط.
5) تدريب مترجم/ناقد/مسترجع/موجه أدوات محلي.
6) مقارنة ARM-BASE وARM-LOCAL وARM-CURRENT وARM-HYBRID.
7) الإصلاح الموجه ثم الاختبار النهائي على B.

مهم:
- النموذج المحلي عضو داخل العقل، وليس الحقيقة القانونية للعقل.
- لا تعدين كتب واسع.
- لا تسمية Researcher قبل منافسة العقل الحالي على B ومراجعة مستقلة.
- البيانات تحفظ محليًا في المتصفح؛ استخدم Export JSON بعد كل بوابة.
- لا تضع الملفات على main مباشرة؛ استخدم فرعًا وPR وبوابة governance-gate.

بروتوكول التزامن الملزم (v2.2):
- القاعدة: origin/main هو الحقيقة القانونية؛ local main نسخة تشغيلية يجب أن تطابقها؛
  الفروع مكان العمل فقط.
- قبل بدء أي مرحلة:
    git switch main
    git fetch --prune origin
    git merge --ff-only origin/main
    git status --short
    git rev-parse HEAD; git rev-parse origin/main
  لا بدء إلا إذا HEAD == origin/main والشجرة المتتبعة نظيفة،
  ويُسجل Pre-stage sync receipt في حقل المرحلة.
- بعد دمج مخرجات المرحلة: الفحص نفسه، ويُسجل Post-stage sync receipt.
- كل إيصال يشمل: timestamp، local HEAD، origin/main SHA، branch،
  ahead/behind، tracked-tree status، scheduled-task status، last sync result.
- لا تُغلق مرحلة في اللوحة دون Post-stage sync receipt (مفروض برمجيًا في v2.2).
- مهمة المزامنة المجدولة كل 15 دقيقة (fetch ثم fast-forward الآمن فقط،
  دون معالجة صامتة للتعارضات) طبقة مساعدة، وليست بديلًا عن الإيصالين.
- ممنوع دائمًا: commit مباشر على main، force push، hard reset آلي،
  stash أو حذف تلقائي.
