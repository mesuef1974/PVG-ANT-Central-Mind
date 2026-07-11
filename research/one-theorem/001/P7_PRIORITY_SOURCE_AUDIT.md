# One-Theorem Program 001 — P7 Source-Grounded Priority Audit

**Target:** `ONE-LEMMA-TARGET-001`  
**Date:** 2026-07-12  
**Decision:** `SURVIVES AS A MODEST WEIGHTED EXTENSION; ORIGINALITY NOT YET CERTIFIED`  
**Scope:** fixed `q`, fixed `r`, smooth compactly supported weight.

## 1. Exact object under audit

For

\[
n=\prod_{p^\alpha\parallel n}p^\alpha,
\]

define

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0).
\]

Besides the divisor-box interpretation already proved, there is an exact classical reformulation:

\[
\boxed{
I_r(n)=
\mathbf 1_{\operatorname{rad}(n)^{2r}\mid n}\,
\tau\!\left(\frac{n}{\operatorname{rad}(n)^{2r}}\right).
}
\]

Indeed, if one prime exponent is below `2r`, both sides vanish. Otherwise

\[
\frac{n}{\operatorname{rad}(n)^{2r}}
=\prod_{p^\alpha\parallel n}p^{\alpha-2r},
\]

and its divisor count is the product of `alpha-2r+1`.

This reformulation is now part of the permanent priority audit. It shows that the function is a divisor weight on `2r`-full integers, not an unrelated new species of arithmetic function.

## 2. Primary prior literature located

### 2.1 Chan and Tsang, 2013

T. H. Chan and K. M. Tsang, **Squarefull numbers in arithmetic progression**, *International Journal of Number Theory* 9 (2013), no. 4, 885–901.

The paper is identified in the reference list of Chan's sequel. It establishes an asymptotic formula for unweighted squarefull numbers in a reduced arithmetic progression.

### 2.2 Srichan, 2013

T. Srichan, **Square-full and Cube-full Numbers in Arithmetic Progressions**, *Šiauliai Mathematical Seminar* 8 (16) (2013), 223–248.

Chan's sequel states that Srichan expressed the main terms using Dirichlet characters and Dirichlet L-functions, treated non-coprime residue data, and also studied cubefull numbers.

### 2.3 Chan, 2014

T. H. Chan, **Squarefull numbers in arithmetic progression II**, arXiv:1407.0054.

This source explicitly uses

\[
G_2=\{\chi\pmod q:\chi^2=\chi_0\}
\quad\text{and}\quad
G_3=\{\chi\pmod q:\chi^3=\chi_0\}
\]

when isolating the square and cube layers. It therefore establishes that quadratic/cubic torsion-character selection is classical in the squarefull progression problem.

Primary source URL: `https://arxiv.org/abs/1407.0054`.

## 3. Claims killed by the audit

The following are **not** available as originality claims:

1. squarefull numbers have `x^(1/2)` and `x^(1/3)` layers;
2. reduced residue-class main terms can be decomposed by Dirichlet characters;
3. the square layer selects characters with `chi^2=chi_0`;
4. the cube layer selects characters with `chi^3=chi_0`;
5. Dirichlet L-functions and classical contour methods can express these layers;
6. a smooth fixed-modulus version can be obtained from a suitable meromorphic Dirichlet series by Mellin inversion.

These are classical ingredients or direct consequences of classical machinery.

## 4. Exact searches that did not locate the target

The priority audit searched for direct matches and close variants of:

- `prod(alpha_p-1)` as a divisor weight;
- `prod max(alpha_p-2r+1,0)`;
- `tau(n/rad(n)^(2r))` on `2r`-full numbers;
- weighted powerful or k-full numbers in arithmetic progressions;
- interior or margin divisors of the prime-exponent divisor box;
- the Bell series `1+y^(2r)/(1-y)^2`;
- the factorization with layers `2r` and `2r+1`.

No exact searchable match was located for the observable family or the full fixed-`r` smoothed theorem. This is evidence for continued investigation, **not** an originality certificate.

## 5. Surviving possible contribution

The only surviving possible contribution is the combination:

1. the margin-interior divisor-box observable `I_r`;
2. its equivalent weighted `2r`-full form;
3. the general layer factorization
   \[
   D_{r,\chi}(s)=
   L(2rs,\chi^{2r})
   L((2r+1)s,\chi^{2r+1})^2
   H_{r,\chi}(s);
   \]
4. the explicit smooth fixed-modulus residue-class expansion;
5. the explicit simple- and double-pole constants;
6. the uniform statement in the reduced class `a` for fixed `q,r`.

## 6. General-theorem subsumption risk

The theorem uses a classical method once the Bell series is known. A sufficiently general theorem about multiplicative weights supported on k-full integers, or a general meromorphic Dirichlet-series transfer theorem in arithmetic progressions, may subsume it.

Therefore the correct distinction is:

```text
Possible statement novelty: yes, not certified.
Method novelty: no.
Torsion-selection novelty: no.
Observable novelty: plausible, not certified.
PVG discovery value: material.
PVG necessity for the final contour proof: weak.
```

The analytic proof can be written entirely in classical language after `I_r` is defined. PVG contributes materially to the construction and interpretation of the weight, but is not logically necessary for the contour shift.

## 7. Remaining bibliographic gate

Before any certified originality statement, the following must still be checked through a research-grade bibliographic database or expert review:

- cited-by and related-item chains for Chan–Tsang and Srichan;
- older literature on weighted powerful/k-full numbers;
- named divisor functions equivalent to `tau(n/rad(n)^(2r))` on `2r`-full support;
- general results that accept arbitrary local Bell series beginning at exponent `2r`;
- whether the exact constants have appeared as a routine example in a broader theorem.

## 8. P7 priority classification

\[
\boxed{
\text{PLAUSIBLY NEW MODEST WEIGHTED STATEMENT, NOT A NEW METHOD}
}
\]

This permits the theorem program to continue to independent proof review, but not to publication or originality closure.

## 9. Scientific ceiling

```text
Complete manual proof candidate: retained.
Exact prior squarefull/cubefull mechanism: known.
Exact I_r weighted theorem: no match located.
Originality certificate: absent.
Original theorem claim: forbidden.
RH/GRH progress: none.
```
