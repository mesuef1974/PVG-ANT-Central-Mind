# Book Import Protocol

كيف تدخل الكتب بأمان. القوالبُ التشغيليّة: `governance/section-extraction-template.md` و`governance/book-ingestion-template.md`.

## القواعد

```text
1. لا PDF داخل git.
2. لا raw copyrighted text.
3. لا نقل طويل من الكتاب.
4. لا claim بأن القراءة تعني إتقانًا كاملًا.
5. لا claim بأن الكتاب أعطى نظرية جديدة.
6. كل book import يحتاج Registry ID.
7. كل book import يحتاج classification.
8. كل book import يحتاج boundaries.
9. كل book import يحتاج audit.
```

## قالب الكتاب

```text
Book ID / Source Name / Import Status / Coverage / Purpose /
Allowed Use / Forbidden Use / Extracted Capabilities / PVG Connections /
Claim Classification / Missing Certificates / Next Valid Actions / Audit Status
```

كل كتابٍ في `ledgers/books/<BOOK-ID>/` بـ README.md يبدأ بكتلة Source (اسم الكتاب + Book ID + الملف المحلّيّ خارج git + استبعاد PDF + ملاحظات محوَّلة فقط). يفرضه `tools/no_pdf_audit.py` و`tools/citation_audit.py`.

**Honest classification:** Governance / Diagnostic. No RH/GRH progress.
