# Claim Classification Matrix

كل claim يُصنَّف بواحدٍ من هذه؛ لا claim بلا classification. (تعريفات الختوم الكاملة في `governance/classification-system.md`.)

| Class | يعني | يحتاج |
|---|---|---|
| **Known** | نتيجة/أداة معروفة | مصدر أو إسناد |
| **Identity** | هوية جبريّة/تعريفية | تحقق رمزي أو برهان قصير |
| **Reinterpretation** | قراءة PVG لكائن معروف | يُمنع تقديمها اكتشافًا |
| **Diagnostic** | أداة تشخيص بنية/جدار/نمط | يُمنع تحويلها proof |
| **Boundary** | جدار أو حدُّ طريقة (parity, zero-density, Type-II gap, operator recoverability failure) | — |
| **Open Problem** | سؤال مفتوح/جبهة | يُمنع صياغته محلولًا |
| **Candidate Mechanism** | آلية مرشحة غير مثبتة | اختبار قابل للإبطال + شهادة ناقصة محددة + حدود |
| **New Theorem** | نتيجة كاملة | تعريفات + فرضيات + برهان كامل + فحص ثغرات + شهادة + audit |
| **Missing Certificate** | شهادة ناقصة | ليست نتيجة |
| **Forbidden Claim** | ادّعاء محظور | يُوثَّق منفيًّا فقط |

**Honest classification:** Governance / Diagnostic. No RH/GRH progress.
