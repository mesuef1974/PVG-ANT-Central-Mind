# One-Theorem Program 001 — P0 Priority Audit

**Target:** `ONE-LEMMA-TARGET-001`  
**Working title:** Smoothed torsion layers of margin-interior divisor boxes in arithmetic progressions  
**Status:** priority audit in progress; originality not certified.

## 1. Exact proposed object

For fixed `r>=1`,

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0)
\]

counts divisor-box points satisfying

\[
r\le v_p(d)\le v_p(n)-r
\]

at every active coordinate.

The proposed theorem is a smoothed fixed-modulus asymptotic for

\[
\sum_{n\equiv a\pmod q} I_r(n)W(n/x),
\]

with character layers selected by `chi^(2r)=chi_0` and `chi^(2r+1)=chi_0`.

## 2. Known surrounding theory

### Powerful and k-full support

Powerful (square-full) integers are classical. They admit the representation `n=u^2v^3` with `v` squarefree, and their counting function has square and cube scales. Modern references continue the classical theory of powerful and `k`-full numbers.

Relevant primary sources:

- T. H. Chan, *Spectrum of multiplicative functions over powerful numbers*, arXiv:2303.01168.
- T. H. Chan, *A note on powerful numbers in short intervals*, arXiv:2207.08874.
- P. Bajpai, M. A. Bennett, T. H. Chan, *Arithmetic Progressions in Squarefull Numbers*, arXiv:2302.03113.

### Square-full numbers in arithmetic progressions

T. H. Chan, *Squarefull numbers in arithmetic progression II*, arXiv:1407.0054, improves the error term in an earlier asymptotic for square-full numbers in a reduced residue class.

The paper explicitly introduces:

```text
G_2 = {chi mod q : chi^2 = chi_0}
G_3 = {chi mod q : chi^3 = chi_0}
```

for the square and cube main-term layers. Therefore the general idea

```text
square layer ↔ quadratic torsion characters
cube layer   ↔ cubic torsion characters
```

is known in the unweighted `r=1` square-full counting problem.

This corrects the preliminary originality impression: the target may not claim discovery of torsion-character selection as a mechanism.

### Character-based main terms

Chan also records that Srichan expressed square-full progression main terms using Dirichlet characters and L-functions and treated cubefull numbers. Thus character/L-function packaging is established prior art.

### General multiplicative-function machinery

R. de la Bretèche and G. Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929, supplies broad mean-value machinery for suitable multiplicative functions. The selected proof, however, is smoothed and has multiple singular layers, so Mellin inversion and residue calculus are the direct route.

## 3. Exact novelty still under consideration

The following components were not located in the initial and deep searchable audit:

1. the geometric weight
   \[
   I_r(n)=\prod_{p^a\parallel n}(a-2r+1)_+;
   \]
2. its interpretation as the number of divisor-box points at margin at least `r`;
3. the exact factorization
   \[
   L(2rs,\chi^{2r})L((2r+1)s,\chi^{2r+1})^2H_{r,\chi}(s);
   \]
4. the general `2r`/`2r+1` layer rule for this weight;
5. the explicit smoothed fixed-modulus expansion with both residue constants and remainder at the next local layer.

Search failure is not an originality certificate. These items may be unnamed consequences of a general theorem on weighted `k`-full numbers.

## 4. Reclassified contribution hierarchy

### Known

- powerful/k-full support;
- square and cube scales for square-full numbers;
- quadratic/cubic torsion-character selection in the unweighted square-full progression problem;
- character orthogonality, Euler products, Mellin inversion, and contour shifting.

### Potentially new but methodologically classical

- the margin-interior divisor-box weight;
- its general layer factorization;
- the weighted smoothed progression formula and explicit constants;
- the geometric explanation of why the exponent layers are `2r` and `2r+1`.

### Not claimed

- a new L-function method;
- a new torsion-character principle in general;
- improved distribution ranges in the modulus;
- an unsmoothed error improvement;
- any RH/GRH consequence.

## 5. Priority risk assessment

| Component | Risk that it is already known | Current classification |
|---|---:|---|
| divisor-box interpretation of `I_r` | medium | plausible new formulation |
| local Bell series | high | elementary once weight is defined |
| `2r`/`2r+1` L-factor extraction | medium-high | likely routine but exact weight may be new |
| torsion selection mechanism | certain prior art in `r=1` unweighted case | known mechanism |
| general weighted smoothed AP formula | medium | plausible new specialization |
| explicit constants | medium | may be absent from prior literature but routine residue calculus |
| remainder `x^(1/(2r+2)+epsilon)` | medium | plausible standard smooth-contour consequence |

## 6. Additional sources still required

Before an originality certificate, inspect or independently verify:

1. Chan–Tsang’s first square-full progression paper cited by Chan 2014;
2. Srichan’s character/L-function formulation and cubefull extension;
3. Liu–Zhang and later distribution results cited in modern square-full AP literature;
4. older weighted powerful-number mean-value literature;
5. databases or surveys of Dirichlet series for multiplicative exponent weights.

## 7. P0 decision

```text
TARGET SURVIVES P0, WITH NARROWED ORIGINALITY CLAIM
```

The target remains worth proving because the exact geometric weight and its full smoothed weighted theorem were not located. The contribution must be described, at most, as:

> a new or apparently new divisor-box weight and a classical-method theorem describing its torsion layers.

Final originality remains open until the proof and older-literature audit are complete.

## 8. Sources

- T. H. Chan, *Squarefull numbers in arithmetic progression II*, arXiv:1407.0054.
- T. H. Chan, *Spectrum of multiplicative functions over powerful numbers*, arXiv:2303.01168.
- P. Bajpai, M. A. Bennett, T. H. Chan, *Arithmetic Progressions in Squarefull Numbers*, arXiv:2302.03113.
- M. Munsch, I. E. Shparlinski, K. H. Yau, *Smooth square-free and square-full integers in arithmetic progressions*, arXiv:1810.02573.
- R. de la Bretèche, G. Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929.

## 9. Ceiling

```text
Priority audit only.
Originality plausible, narrowed, and unconfirmed.
No lemma or theorem certified.
No RH/GRH progress.
```
