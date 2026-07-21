# PVG Pareto Explorer

صفحة ويب محلية مستقلة لعرض المستوى

\[
P=\{2,3,5\},\qquad \Omega=6
\]

وجبهة باريتو الناتجة عن تعظيم الأهداف:

\[
\left(n,\tau(n),\frac{\sigma(n)}n,\frac{\varphi(n)}n\right).
\]

## التشغيل

من PowerShell داخل الـworktree المنفصل:

```powershell
cd "D:\PVG-ANT-Inverse-Geometry-001"
powershell -ExecutionPolicy Bypass -File tools\open_pvg_pareto_explorer.ps1
```

أو افتح الملف مباشرة:

```powershell
Start-Process "D:\PVG-ANT-Inverse-Geometry-001\web\pvg-pareto-explorer\index.html"
```

الصفحة ذاتية الاكتفاء، ولا تحتاج إلى تثبيت حزم JavaScript أو تشغيل خادم محلي.

## ما تعرضه الصفحة

- جميع نقاط المستوى الـ28 داخل المثلث الشبكي.
- جبهة باريتو العالمية ذات 19 نقطة.
- حواف الجبهة الـ27 ومكوناتها الثلاثة.
- الجسور، ونقاط القطع، والنقطتان المعزولتان.
- قمم الأهداف الفردية.
- طبقات تلوين لـ `n` و`tau` و`sigma(n)/n` و`phi(n)/n`.
- تفاصيل حسابية وهندسية عند النقر على أي نقطة.

## الحد العلمي

هذا عارض بصري لتحليل منتهٍ دقيق على وجه ومستوى محددين. لا يثبت قانونًا تقاربيًا، ولا يمنح جبهة باريتو معنىً مطلقًا مستقلًا عن قائمة الأهداف المختارة.
