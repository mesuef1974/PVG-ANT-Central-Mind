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
| `ledgers/books/` | مُعدَّنة (treasure overlay مُغلَق): Overholt · Tenenbaum · Mileti · IK · Harman · **Montgomery MNT-II (v0.6، source-grounding-corrected؛ book_overlay_closed وmastery مؤجَّلة: الموثوقُ C/D/E/F/G/H مُغلَقةً · المحجورُ A/B/legacy-E)**؛ + **Opera de Cribro (v0.7 · partial_overlay: OPERA-004-A CLOSED)** + 7 كتب `available_not_imported` |
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

**Now (v0.6-H CLOSED — ستُّ وحداتٍ موثوقةٍ مُغلَقة، فصولُ المحتوى 16–22 كاملة):** خمسةُ كتبٍ مُعدَّنة (treasure overlay مُغلَق): Overholt · Tenenbaum · Mileti · IK · Harman. **Montgomery MNT-II (v0.6)** = **book_overlay_closed** (AUDIT-CM-MONTGOMERY-OVERLAY-008؛ mastery مؤجَّلة)، **source-grounding-corrected**، Level 2: **الموثوقُ المؤصَّلُ بالمصدر (الستّةُ مُراجَعةُ إغلاق)** = G (Ch16 Van der Corput دعمًا؛ v0.6-g PASS) · F (Ch17 مجاميعُ الأوّليّات / Type I-II؛ v0.6-f PASS) · **H (Ch18 الجمعيّات / طريقةُ الدائرة؛ v0.6-h PASS — Goldbach الثنائيُّ مفتوحٌ لا يُدَّعى)** · C (Ch19-20 الغربال الكبير/BV) · D (Ch21 غرابيل) · E (Ch22 الفجوات المحدودة؛ v0.6-e PASS). **المحجورُ (source-mismatch/cross-volume، غيرُ موثوق)** = A · B · legacy off-diagonal E (مراجعاتُ إغلاقِ A/B القديمةُ SUPERSEDED). الحرّاسُ سبعة (+ `state_coherence` بمسحٍ شامل، وآلاتِ حالةِ إغلاق، وحقيقةِ الفصل↔الوحدة، ومصدرٍ واحدٍ للحالة الحيّة).

**Now also (v0.7 — Opera de Cribro، أوّلُ وحدةٍ مُغلَقة):** بأمرٍ مستقلٍّ فُتِح **Opera de Cribro** (Friedlander–Iwaniec، AMS Colloquium 57، 2010؛ هويّةٌ متحقّقة)، ونُفِّذت ثمّ أُغلقت أوّلُ وحدة: **`OPERA-004-A`** (Sifting Sequences as Main-Term/Remainder Certificates) من `OPERA-TREASURE-PACKET-001` (Ch1 §§1.1-1.4) = **CLOSED، v0.7-A Closure Review PASS** (`AUDIT-CM-V07-A-CLOSURE-001`؛ `packet_mismatch=true routing_split`: `core_certificate_theory` أساسًا + `reference_integration` ثانويًّا؛ **ثلاثُ مراجعاتٍ عدائيّةٍ مستقلّة، الثالثةُ SAFE على a319df4** · 7 بطاقات closure_approved · لا TOOL-ID جديد · **صفرُ WALL جديد** — ثلاثةُ boundaries تبقى Boundaries، لا ربطَ مبكرًا بـWALL-PARITY). النطاقُ مُجمَّد والعقيدةُ مزروعة (الهدف · LB-01..06 · فئاتُ الوحدات · تعديلاتُ النطاق/الديون/سجلُّ `C_sieve` في `governance/scope-amendment-and-debt-policy.md`). **الحالة partial_overlay (وحدةٌ واحدةٌ مُغلَقة)؛ التالي NONE بانتظار حزمةٍ مستقلّةٍ تالية؛ حالةُ Montgomery لم تُمَسّ.**

**Next:** لا وحدةَ ولا كتابَ ولا تدقيقَ جديدًا بلا إذنٍ مستقلّ — **طبقةُ Montgomery مُغلَقة (book_overlay_closed، تدقيق 008) وmastery مؤجَّلة؛ الإغلاقُ تغطيةٌ لا رياضيّات: Goldbach الثنائيُّ مفتوح · MC-001..005 unsolved · الجدرانُ uncrossed · zero RH/GRH**؛ لا MNTII-006-I بلا packet وإذن · الملاحقُ E–H دعمٌ مؤجَّلٌ لا يُرقّى بلا packet · لا إعادةَ ثقةٍ بـA/B/legacy-E بلا Packet مؤصَّل. (سجلُّ المراجعات: v0.6-E Closure Review PASS · v0.6-F Closure Review PASS · v0.6-G Closure Review PASS · v0.6-H Closure Review PASS · Overlay Audit 008.)

**Roles:** ChatGPT = محلّلُ الكنوز الرياضيّة؛ العميلُ المحلّيُّ = مهندسُ المستودع والحوكمة (`governance/state-coherence-policy.md`).

المسار: `v0.1b` → v0.2 Mileti → v0.3 Tenenbaum-005 → v0.4 IK → v0.5 Harman → treasure retrofit → v0.6 Montgomery → **v0.7 Opera de Cribro (OPERA-004-A CLOSED)**. بلا tag · لا merge إلّا بمراجعة. المواصفةُ الكاملة: `PVG-ANT-Central-Mind-v0.1b-full-spec.md`.
