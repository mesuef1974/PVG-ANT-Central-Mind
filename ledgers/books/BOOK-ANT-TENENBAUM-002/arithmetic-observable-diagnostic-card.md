# Arithmetic Observable — Master Diagnostic Sheet

أيُّ دالةٍ حسابيّةٍ تدخل العقلَ تمرُّ عبر هذه البطاقة. الحقولُ الفارغةُ تُذكَر فارغةً صراحةً (لا حذف).

```text
Name:
Type:                    (multiplicative / additive / completely-* / neither)
Local data f(p^a):
PVG geometry:            (support omega / height Omega / phase / residue fiber)
Dirichlet series F(s):
Euler product:
Pole structure:          (أين القطب؟ ما البقايا؟)
Main term:               (من أيّ قطب؟)
Average order:
Normal order:
Limiting law:
Tail / large deviations:
Moments:
Maximal order:
Error source:            (zeros / truncation / minor arcs / conductor-gamma)
Main wall:               (WALL-ID من registries/walls.jsonl)
Registry IDs:            (TOOL-* / OBS-* المستعملة)
Known certificates:
Missing certificates:    (→ governance/missing-certificates.md)
Allowed claims:
Forbidden claims:
Honest classification:   (Known/Identity/Reinterpretation/Diagnostic/Boundary/Open Problem/Candidate Mechanism/New Theorem/Missing Certificate/Forbidden Claim)
Next action:
```

## قواعد الاستعمال

- كلُّ `Main term:` يستلزم `Pole structure:` غيرَ فارغ (لا حدَّ رئيسيًّا بلا قطب).
- كلُّ `Error source:` قويٍّ يستلزم معلومةَ أصفارٍ صريحة (zero-free / zero-density / فرضيّة مصرَّح بها).
- `Main wall:` يجب أن يكون ID من `registries/walls.jsonl`.

**Honest classification:** Diagnostic (template). No RH/GRH progress.
