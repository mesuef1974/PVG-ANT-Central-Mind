# P8 External Validation 002 — Framework Comparison and Significance Gate

**Date:** 2026-07-12  
**Target:** `ONE-LEMMA-TARGET-001`  
**Scope:** exact-formula search, general-framework comparison, and referee-routing decision

## 1. Target under review

For fixed `r >= 1`, define

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0)
=\mathbf 1_{\operatorname{rad}(n)^{2r}\mid n}\,
\tau\!\left(n/\operatorname{rad}(n)^{2r}\right).
\]

Its prime-power Bell series is

\[
\sum_{\alpha\ge 0} I_r(p^\alpha)y^\alpha
=1+\frac{y^{2r}}{(1-y)^2}.
\]

The internally proved fixed-parameter smooth theorem is based on

\[
D_{r,\chi}(s)=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

with `H` holomorphic for

\[
\Re(s)>\frac1{2r+2}.
\]

## 2. Search routes completed in this pass

The search was repeated using four non-equivalent descriptions:

1. the valuation formula `prod max(alpha-2r+1,0)`;
2. the radical/divisor formula `1_{rad(n)^(2r)|n} tau(n/rad(n)^(2r))`;
3. the Bell series `1+y^(2r)/(1-y)^2`;
4. the geometric description “margin-interior divisor-box lattice points”.

The search also covered nearby terminology:

- weighted squarefull / powerful / k-full numbers;
- divisor functions restricted to powerful support;
- prime-independent multiplicative functions;
- rational Bell series and rational arithmetical functions;
- Selberg–Delange transfer;
- multiplicative functions in arithmetic progressions.

## 3. What the wider literature clearly absorbs

The following parts are classical or belong to general established machinery:

1. squarefull and `k`-full support;
2. quadratic and cubic character layers in squarefull progressions;
3. Dirichlet-character decomposition of fixed reduced residue classes;
4. Euler-product extraction from a rational local Bell series;
5. Mellin inversion and contour shifting for a fixed smooth weight;
6. Selberg–Delange-type transfer from controlled singular factors to asymptotic averages;
7. general theories of multiplicative functions in arithmetic progressions.

Therefore the project must not claim:

- a new analytic method;
- a new character-torsion mechanism;
- a new general Selberg–Delange principle;
- a new theory of multiplicative functions in progressions.

## 4. Exact-match result

No exact match was located in the directed online search for the complete package:

- the function `I_r` itself;
- its margin-interior divisor-box interpretation;
- the Bell series `1+y^(2r)/(1-y)^2` for this arithmetic observable;
- the general `2r`, `2r+1`, residual `2r+2` layer hierarchy;
- the explicit fixed-modulus smooth residue-class constants.

This is evidence of possible statement novelty only. It is not a priority certificate.

## 5. Refined scientific classification

The strongest honest classification after this pass is:

\[
\boxed{
\text{POSSIBLY NEW PVG-DERIVED OBSERVABLE AND MODEST THEOREM;}
\quad
\text{ANALYTIC METHOD CLASSICAL; ORIGINALITY NOT CERTIFIED}
}
\]

More specifically:

```text
Observable novelty: plausible, not certified.
Statement novelty: plausible, not certified.
Method novelty: absent.
Character-mechanism novelty: absent.
PVG role in discovery: material.
PVG role in final proof: explanatory/organizing, not logically indispensable.
Internal proof status: complete at fixed q,r,W.
External proof status: absent.
Publication readiness: absent.
```

## 6. Significance gate

Even if the exact statement is new, a specialist may judge it to be a routine corollary of standard Euler-product and contour machinery once `I_r` is defined.

Therefore external review must answer two separate questions:

1. **Priority:** Has the observable or theorem appeared before under another notation or general theorem?
2. **Significance:** If new, is the single theorem mathematically substantial enough, or should the same target be strengthened into a coherent family of divisor-box face/margin observables?

The second question matters because a new statement is not automatically a publishable contribution.

## 7. Contingency within the same theorem program

If external review returns “correct but routine”, the project must not open an unrelated theorem target immediately.

The allowed refinement is inside the same PVG object family:

- margin profiles for several distances;
- face-enumerator polynomials of divisor boxes;
- a general local-Bell-series-to-analytic-layer transfer theorem;
- explicit identification of which geometric layers create which poles.

This is a strengthening of `ONE-LEMMA-TARGET-001`, not a second active research front.

## 8. Required external actions

Two human roles are required:

### Priority specialist

A specialist in squarefull / `k`-full numbers or multiplicative functions in arithmetic progressions should determine whether the exact weight or statement is known.

### Proof referee

An independent analytic number theorist should check:

- the local factor extraction;
- the convergence half-plane for `H`;
- all character and imprimitive-prime conventions;
- the double-pole constants;
- the contour shift and vertical growth;
- dependence of the error constant on `q,r,W,epsilon`.

## 9. Decision

```text
P8-EXTERNAL-VALIDATION-002 = COMPLETE AS AN INTERNAL ROUTING PASS.
Research-grade priority certificate = absent.
External referee certificate = absent.
Originality certification = absent.
One-Theorem Program 001 = active_external_validation_hold.
Second theorem target = forbidden.
```

## 10. Scientific ceiling

- internally proved fixed-parameter result;
- no exact match found in directed online searches;
- classical analytic machinery;
- plausible observable/statement novelty only;
- no publication claim;
- no RH progress;
- no GRH progress.

**Classification:** external-validation routing and significance audit; not an originality or publication certificate.
