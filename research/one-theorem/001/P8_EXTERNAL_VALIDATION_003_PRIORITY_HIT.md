# P8 External Validation 003 — OEIS A361430 Priority Hit

**Date:** 2026-08-04  
**Target:** `ONE-LEMMA-TARGET-001`  
**Branch:** `agent/p8-priority-hit-a361430`  
**Scope:** exact numerical-sequence identification and partial priority reclassification for the case `r = 1`  
**Classification:** partial negative priority certificate; not a complete literature-priority certificate and not a proof-referee certificate

## 1. Decision

A fifth search route, independent of the four symbolic and verbal routes recorded in `P8_EXTERNAL_VALIDATION_002`, identifies the `r = 1` observable exactly with OEIS sequence `A361430`.

```text
P8-EXTERNAL-VALIDATION-003 = PARTIAL_NEGATIVE_PRIORITY_HIT
I_1 observable priority = FAILED
r = 1, q = 1 sequence identity = KNOWN
r >= 2 family priority = UNRESOLVED
q > 1 progression theorem priority/significance = UNRESOLVED / HIGH ROUTINENESS RISK
proof correctness = NOT ASSESSED HERE
publication readiness = ABSENT
RH/GRH progress = NONE
```

This certificate supersedes the `P8_EXTERNAL_VALIDATION_002` exact-match statement only for the case `r = 1`, and only to the extent stated below.

## 2. Exact identity

The project observable is

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0).
\]

For `r = 1`,

\[
I_1(p^e)=\max(e-1,0)=e-1 \qquad (e\ge 1),
\]

and `I_1(1)=1`.

OEIS `A361430` is recorded as the multiplicative function satisfying

\[
a(p^e)=e-1,
\qquad a(1)=1.
\]

Since both functions are multiplicative and agree on every prime power,

\[
\boxed{I_1(n)=A361430(n)\quad\text{for every }n\ge1.}
\]

This is an exact identity, not a finite-prefix match.

## 3. Public prior record

The current OEIS record gives:

- sequence author: Vaclav Kotesovec;
- origin date: 2023-03-11;
- keyword set including `easy` and `mult`;
- the coreful-divisor interpretation added by Amiram Eldar in 2023;
- the support condition `a(n)>0` exactly for powerful numbers;
- the divisor interpretation later written as
  \[
  a(n)=\#\{d:d\mid n,\ \operatorname{rad}(d)=\operatorname{rad}(n/d)\};
  \]
- the Euler product
  \[
  \prod_p\left(1+\frac{1}{(p^s-1)^2}\right);
  \]
- the factorization
  \[
  \zeta(2s)\zeta(3s)^2
  \prod_p\left(
  1+2p^{-4s}+2p^{-5s}-p^{-6s}-2p^{-7s}-2p^{-8s}
  \right);
  \]
- a two-layer summatory asymptotic with a `x^{1/2}` term and an `x^{1/3}\log x` / `x^{1/3}` contribution, together with explicit numerical constants.

Primary record used in this pass:

- OEIS data export: `oeis/oeisdata`, `seq/A361/A361430.seq`, blob `b23e04d49f58b47e01246fd0d28e788f651c312d`, accessed 2026-08-04.

The local Bell series agrees exactly:

\[
1+\sum_{e\ge2}(e-1)y^e
=1+\frac{y^2}{(1-y)^2}.
\]

Also,

\[
\left(1+\frac{y^2}{(1-y)^2}\right)
(1-y^2)(1-y^3)^2
=
1+2y^4+2y^5-y^6-2y^7-2y^8,
\]

which gives the displayed `\zeta(2s)\zeta(3s)^2 H(s)` factorization in the untwisted `r=1` case.

## 4. Priority consequence

The following earlier classifications do not survive unchanged:

```text
Observable novelty: plausible, not certified.
No exact match found for I_r itself.
Possibly new PVG-derived observable.
```

They fail for `I_1`.

The exact observable, its prime-power law, its Bell series, an untwisted Euler-product layer factorization, and a two-scale summatory formula are already present in the public OEIS record.

Therefore the project may not claim novelty for:

- the observable `I_1`;
- the support of `I_1` on powerful numbers;
- the coreful-divisor count interpretation of `I_1`;
- the untwisted local Bell series for `I_1`;
- the untwisted `2` / `3` zeta-layer factorization for `I_1`;
- the existence of `x^{1/2}` and `x^{1/3}` summatory layers in the `q=1`, `r=1` case.

## 5. Effect on the PVG-necessity claim

The internal historical statement remains true:

```text
PVG materially generated I_r inside this project.
```

But the stronger external significance inference is weakened:

```text
The discovery of I_1 does not require PVG in any logical or historical sense.
```

A prior independent route reached the same observable without the project's divisor-box language. Thus PVG's material role is a claim about this project's discovery process, not evidence that the observable was inaccessible or unlikely without PVG.

This does not show that the full family `I_r`, or a general face/margin calculus, is non-material. It removes `I_1` as evidence for that stronger claim.

## 6. What remains unresolved

This pass does not establish prior art for:

1. the full family
   \[
   I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0),
   \qquad r\ge2;
   \]
2. the uniform geometric interpretation as a single hierarchy of margin-interior divisor-box observables;
3. the fixed-modulus arithmetic-progression theorem for `q>1` with character decomposition;
4. the exact general `2r`, `2r+1`, residual `2r+2` hierarchy;
5. the smooth remainder
   \[
   O_{q,r,W,\varepsilon}\left(x^{1/(2r+2)+\varepsilon}\right)
   \]
   in the full stated setting.

Failure to find an `r=2` OEIS entry is not a literature-priority result. OEIS is only one search surface.

The remaining search must include weighted `k`-full / powerful-number literature, prime-independent multiplicative functions, rational Bell-series classifications, Selberg--Delange frameworks, and fixed-modulus progression theorems. The neighboring function `A005361` and work attributed there to Laszlo Toth and earlier square-full-divisor literature are mandatory comparison points.

## 7. Significance warning

The OEIS keyword `easy` is weak metadata. It is not a peer-reviewed theorem, a proof, or a specialist judgment of the project's full result.

Likewise, the current OEIS record does not by itself establish:

- when each displayed formula was first added;
- whether the summatory asymptotic has a published proof;
- whether the constants and remainder were externally checked;
- whether the `r\ge2` and `q>1` extensions are formal corollaries of a named theorem.

Accordingly, this certificate records public prior art and a decisive exact match for `r=1`; it does not convert OEIS metadata into a complete research-grade literature review.

## 8. Revised scientific classification

The strongest honest classification after this hit is:

\[
\boxed{
\begin{gathered}
I_1\text{ IS A KNOWN PUBLICLY CATALOGUED OBSERVABLE;}\\
I_r\ (r\ge2)\text{ AND THE }q>1\text{ THEOREM REMAIN PRIORITY-UNRESOLVED;}\\
\text{THE SURVIVING CLAIM IS AN EXTENSION OF A KNOWN BASE CASE,}\\
\text{WITH CLASSICAL ANALYTIC MACHINERY AND HIGH ROUTINENESS RISK.}
\end{gathered}
}
\]

Machine-readable summary:

```text
Observable novelty, r=1: absent.
Observable novelty, r>=2: unresolved.
Statement novelty, q=1 r=1: absent in broad form; exact proof/remainder comparison incomplete.
Statement novelty, q>1 or r>=2: unresolved.
Method novelty: absent.
PVG role in internal discovery: material.
PVG logical necessity: weak.
External proof status: absent.
Priority gate: narrowed, not fully closed.
Proof-referee gate: still open, but the claim under review is materially smaller.
```

## 9. Governance consequence

- `P8_EXTERNAL_VALIDATION_002` remains an historical routing record.
- Its no-exact-match conclusion is superseded for `r=1` by this certificate.
- `ONE-THEOREM-PROGRAM-001` remains under external-validation hold.
- No L5 or L6 originality promotion is authorized.
- No publication claim is authorized.
- No second theorem target is authorized.
- `main` is unchanged by this certificate.

## 10. Next controlled action

```text
P8-PRIORITY-COMPARISON-004
-> retrieve the history and proof provenance of the A361430 formulas
-> search weighted k-full and powerful-number divisor functions
-> compare against general prime-independent multiplicative-function theorems
-> compare the q>1 result with standard progression and Selberg--Delange machinery
-> issue either a complete negative priority closure or a sharply narrowed surviving statement
```

**Final ceiling:** partial negative priority hit for `r=1`; no complete family-priority decision and no proof validation.
