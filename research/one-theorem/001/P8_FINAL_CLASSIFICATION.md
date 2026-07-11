# P8 Final Internal Classification — ONE-LEMMA-TARGET-001

**Date:** 2026-07-12  
**Scope:** internal mathematical closure and honest originality classification  
**Target:** smoothed torsion layers of margin-interior divisor boxes in fixed arithmetic progressions

## 1. Mathematical status

The project has established, for fixed `q>=1`, fixed `r>=1`, a reduced residue class `(a,q)=1`, a fixed smooth compactly supported weight `W`, and `x tending to infinity`, the smoothed expansion attached to

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0).
\]

The proof package contains:

1. the exact divisor-box interpretation;
2. multiplicativity;
3. the Bell series
   \[
   1+\frac{y^{2r}}{(1-y)^2};
   \]
4. the twisted factorization
   \[
   D_{r,\chi}(s)=
   L(2rs,\chi^{2r})
   L((2r+1)s,\chi^{2r+1})^2
   H_{r,\chi}(s);
   \]
5. absolute and locally uniform convergence of `H` for
   \[
   \Re(s)>\frac1{2r+2};
   \]
6. character decomposition of reduced residue classes;
7. smooth Mellin inversion and contour shifting;
8. explicit simple- and double-pole constants;
9. the fixed-parameter remainder
   \[
   O_{q,r,W,\varepsilon}
   \left(x^{1/(2r+2)+\varepsilon}\right).
   \]

The proof has passed:

- symbolic local-factor and Laurent checks;
- an internal adversarial review;
- a second independent mathematical reconstruction;
- CI consistency checks.

## 2. Internal correctness decision

\[
\boxed{\text{INTERNALLY PROVED AT FIXED PARAMETERS}}
\]

This means that no mathematical gap is currently identified in the stated smooth fixed-parameter theorem.

It does **not** replace external peer review.

## 3. Classical overlap

The following are classical and excluded from novelty claims:

- squarefull and k-full support phenomena;
- the `x^(1/2)` and `x^(1/3)` layers for squarefull numbers;
- quadratic and cubic torsion-character selection;
- Dirichlet-character decomposition in progressions;
- Dirichlet `L`-function factorization methods;
- smooth Mellin inversion and contour shifting.

The 2013–2014 squarefull-progression literature already contains the quadratic/cubic character mechanism.

## 4. Surviving possible contribution

The part that remains plausibly distinctive is the package:

1. the PVG-derived margin-interior observable
   \[
   I_r(n)=
   \mathbf1_{\operatorname{rad}(n)^{2r}\mid n}
   \tau\!\left(n/\operatorname{rad}(n)^{2r}\right);
   \]
2. its geometric interpretation as interior divisor-box lattice points at margin `r`;
3. the general consecutive `2r` and `2r+1` analytic layers;
4. the explicit weighted smooth fixed-modulus formula and constants;
5. the residual threshold `2r+2` and corresponding smooth remainder.

## 5. PVG necessity classification

```text
PVG role in discovering the observable: material.
PVG role in explaining the layer structure: material.
PVG logical necessity in the final contour proof: weak.
New analytic method: no.
New geometric observable: plausible, not externally certified.
```

Thus the result is a genuine output of the PVG research flow, but the final analytic proof can be expressed in classical ANT once the observable has been defined.

## 6. Originality decision

The directed literature audit found no exact match for the weight or the full theorem. However, a research-grade bibliographic database search and external expert review have not been completed.

Therefore:

\[
\boxed{
\text{PLAUSIBLY NEW MODEST WEIGHTED THEOREM, ORIGINALITY NOT CERTIFIED}
}
\]

The project must not use the stronger labels:

- `certified original theorem`;
- `publication-ready theorem`;
- `new torsion mechanism`;
- `new contour method`.

## 7. Maturity classification

```text
Exact PVG–ANT translation: certified.
Structural simplification: certified.
Transfer principle: internally proved for this observable.
Mathematical theorem proof: internally complete.
External proof certification: absent.
Originality certification: absent.
Publication readiness: absent.
RH progress: none.
GRH progress: none.
```

The bridge may be recorded internally as an **L3 proved transfer principle**, but not as an L5 certified original lemma or L6 certified original theorem.

## 8. One-Theorem Program decision

`GOAL-OP-ONE-THEOREM-001` is not closed as a certified original-theorem success.

It enters a final external-validation hold with only two remaining gates:

1. research-grade priority search / expert bibliographic review;
2. external line-by-line mathematical referee review.

Possible final outcomes after those gates:

- original modest theorem;
- new application of a general known theorem;
- known result in different notation;
- corrected theorem after referee findings.

## 9. Next action

Do not open a second theorem target yet.

The next controlled action is:

```text
P8-EXTERNAL-VALIDATION-001
→ complete cited-by and related-item chains for Chan–Tsang and Srichan
→ compare against general weighted k-full and Selberg–Delange theorems
→ obtain an independent mathematical referee report
→ issue final originality/publication classification
```

## 10. Final honest statement

The project has, for the first time, moved from a PVG geometric construction through a complete ANT proof. That is substantive progress in the project’s research method.

The scientific claim remains deliberately narrower:

> We have an internally proved smoothed weighted theorem generated by divisor-box geometry, with plausible but uncertified statement novelty.
