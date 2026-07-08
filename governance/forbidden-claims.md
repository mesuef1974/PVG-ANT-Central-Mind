# Forbidden Claims

عباراتٌ ممنوعةٌ كتوكيدٍ إيجابيّ داخل العقل. الحارسُ `tools/honesty_audit.py` يمسكها. تُذكَر فقط منفيّةً (كجدارٍ/سقف) أو داخل هذا الملفِّ التوثيقيّ.

## قائمة الحظر

- "proves RH" / "proof of RH" / "يبرهن RH"
- "progress toward RH/GRH" / "تقدّم نحو RH/GRH"
- "approaching RH" / "اقتراب من RH"
- "breakthrough" / "اختراق"
- "new theorem" بلا حقلِ `Certificate:` غيرِ فارغٍ ومراجعةٍ خارجيّة
- "secured path to RH" / "مسار مؤمَّن"
- معاملةُ قياسٍ أو تشخيصٍ كأنّه تقدّمٌ برهانيّ
- خلطُ جدارين من `CONSTRAINT-NO-CONFLATION` كجدارٍ واحد

## البديل المسموح

- "RH is a wall / equivalent criterion / hypothesis here."
- "This is a Diagnostic; the wall stands."
- "Candidate Mechanism — needs a certificate and a test."
- "No RH progress. No GRH progress. No secured path."

## استثناءُ الحارس

النفيُ مسموح: سطرٌ يحوي «no RH progress» أو «does not claim» أو «لا تقدّم» لا يُعَدُّ مخالفة. الحارسُ heuristic لا برهان — الحكمُ النهائيُّ بشريّ.
