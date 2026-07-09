# PVG–ANT Central Mind

> **Canonical repository:** `D:\PVG-ANT-Central-Mind`.
> **Legacy duplicate:** the "The All" in-repo copy (`1b51886`) is **do-not-edit** unless explicitly reactivated.

مستودعُ عقلٍ رياضيّ تراكميّ حيّ. كلُّ كتابٍ أو مهارةٍ يدخل لا كنصٍّ خام، بل كـ **أدوات + قواعد + جدران + شهادات + بطاقاتِ واجهة**. طبقةٌ تشخيصيّة/تعليميّة: zero RH progress · zero GRH progress · no secured path.

المبدأ الحاكم: **الـmarkdown للعرض، والـJSONL للحقيقة، والحارس للإنفاذ** (graph لا pile).

## البنية (v0.1b — spec layout)

| مسار | المحتوى |
|---|---|
| `central-mind-charter.md`, `central-mind-goals.md` | الدستور والهدف الأعلى |
| `installed-skills/{math,governance}` | 14 بطاقةَ واجهةِ مهارة (الحوكمة أعلى سلطة) |
| `ledgers/books/` | مُعدَّنة (treasure overlay مُغلَق): Overholt · Tenenbaum · Mileti · IK · Harman · **Montgomery MNT-II (v0.6، source-grounding-corrected: الموثوقُ C/D/E-intake · المحجورُ A/B/legacy-E)**؛ + 8 كتب `available_not_imported` |
| `ledgers/imports/` | sieve · spectral-no-go · computational |
| `registries/` | مصدرُ الحقيقة (JSONL): skills · books · research-frontiers · open-questions-queue · walls · tools · rules · observables · claims · planned · registry(constraint) |
| `maps/` | skill-stack-map · skill-dependency-graph · query-routing-guide · current-capabilities · pvg-to-ant |
| `governance/` | claim-classification-matrix · certificate-funnel · book-import-protocol · what-not-to-import · no-go-memory · classification-system · honesty-policy · central-rules · missing/forbidden · templates |
| `audits/` | v0.1b-audit-checklist |
| `transition-memory/` | latest-state · next-action · compressed-prompt |
| `tools/` | سبعةُ حرّاس (+ `state_coherence`) |
| `Books_others/` | **مكتبةُ PDF محلّيّة — مستبعَدةٌ من git** |

## الحرّاس

```bash
python tools/honesty_audit.py             # تصنيف + عبارات محظورة + سلامة السجلّات
python tools/registry_sync_audit.py       # كل ID في md موجود في السجلّ، لا تكرار
python tools/no_pdf_audit.py              # لا PDF متعقَّب
python tools/forbidden_promotion_audit.py # لا ترقية بلا شهادة
python tools/duplicate_concept_audit.py   # لا مفهوم مكرَّر
python tools/citation_audit.py            # كل سجلِّ كتابٍ موثَّقُ المصدر
python tools/state_coherence_audit.py     # حالةُ العقل صادقةٌ ومحدَّثة (repository-truth)
```

## القانون النهائي

```text
No registry, no entry.  No classification, no claim.  No certificate, no theorem.
No audit, no release.  No RH/GRH progress without proof certificate.
```

## Current state & roadmap

**Now (Montgomery Source-Grounding Correction 006 + State-Repair 006-B/C):** خمسةُ كتبٍ مُعدَّنة (treasure overlay مُغلَق): Overholt · Tenenbaum · Mileti · IK · Harman. **Montgomery MNT-II (v0.6)** = partial overlay، **source-grounding-corrected**، Level 2: **الموثوقُ المؤصَّلُ بالمصدر** = C (Ch19-20 الغربال الكبير/BV، مُغلَقة) · D (Ch21 غرابيل، مُغلَقة) · E (Ch22 الفجوات المحدودة GPY/Maynard، **validated_intake — غيرُ مُغلَقةٍ بعدُ**، بانتظار v0.6-E Closure Review). **المحجورُ (source-mismatch/cross-volume، غيرُ موثوق)** = A · B · legacy off-diagonal E (المصدرُ يؤجّل zero-density/large-values/pair-correlation لمجلّدٍ لاحق؛ مراجعاتُ إغلاقِ A/B القديمةُ SUPERSEDED). الحرّاسُ سبعة (+ `state_coherence` بمسحٍ شامل).

**Next:** v0.6-E Closure Review فقط. لا MNTII-006-F · لا كتابٌ جديد · لا وحدةٌ جديدة بلا Treasure Packet · لا إعادةَ ثقةٍ بـA/B/legacy-E بلا Packet مؤصَّل.

**Roles:** ChatGPT = محلّلُ الكنوز الرياضيّة؛ العميلُ المحلّيُّ = مهندسُ المستودع والحوكمة (`governance/state-coherence-policy.md`).

المسار: `v0.1b` → v0.2 Mileti → v0.3 Tenenbaum-005 → v0.4 IK → v0.5 Harman → treasure retrofit → v0.6 Montgomery. بلا tag · لا merge إلّا بمراجعة. المواصفةُ الكاملة: `PVG-ANT-Central-Mind-v0.1b-full-spec.md`.
