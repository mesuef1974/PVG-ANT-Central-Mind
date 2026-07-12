# Appendix C — The I_r File

## 1. Exact objects and statement

For integer \(r\ge 1\) define the multiplicative observable

\[
I_r(n)=\prod_{p^{\alpha}\parallel n}\max(\alpha-2r+1,\,0)
=\mathbf 1_{\operatorname{rad}(n)^{2r}\mid n}\;
\tau\!\bigl(n/\operatorname{rad}(n)^{2r}\bigr),
\]

geometrically the number of margin-\(r\) interior lattice points of the
divisor box of \(n\).

**Hypotheses (all fixed):** modulus \(q\ge 1\); margin \(r\ge 1\); reduced
residue class \(a\) with \((a,q)=1\); smooth compactly supported weight
\(W\); \(x\to\infty\). No uniformity in \(q\), \(r\), or \(W\) is claimed.

**Internally proved statement (smoothed, fixed parameters):** a two-term
asymptotic expansion for \(\sum_{n\equiv a\,(q)} I_r(n)\,W(n/x)\) with
explicit constants from the simple pole at \(s=\tfrac1{2r}\) and the double
pole at \(s=\tfrac1{2r+1}\), and remainder
\(O_{q,r,W,\varepsilon}\!\bigl(x^{1/(2r+2)+\varepsilon}\bigr)\).

## 2. Proof route

Divisor-box interpretation → multiplicativity → Bell series
\(1+\frac{y^{2r}}{(1-y)^2}\) → character decomposition of the class →
twisted Dirichlet-series factorization
\(D_{r,\chi}(s)=L(2rs,\chi^{2r})L((2r+1)s,\chi^{2r+1})^{2}H_{r,\chi}(s)\),
\(H\) absolutely and locally uniformly convergent in
\(\Re(s)>\frac1{2r+2}\) → smooth Mellin inversion and contour shift →
Laurent data at the two poles → remainder bound. Verified by symbolic
local-factor and Laurent checks, an internal adversarial review, an
independent reconstruction, and CI consistency audits.

## 3. Neutral classification (exact wording)

```text
Internally proved fixed-parameter weighted ANT result.
Exact prior-art status unresolved.
PVG materially contributed to discovery and formulation.
PVG necessity in the final proof is weak or not established.
```

Classical and excluded from any novelty discussion: squarefull/k-full
support phenomena; \(x^{1/2}\)/\(x^{1/3}\) squarefull layers;
quadratic/cubic torsion-character selection; character decomposition;
L-function factorization; smooth Mellin technique.

## 4. PVG role, separated (assess each independently)

1. observable selection — geometric (margin-interior counting);
2. formula discovery — geometric reading of the divisor box;
3. local-factor identification — guided by the valuation-axis germ;
4. proof steering — weak; the final contour argument is classical;
5. generalization proposal — geometric (general margin \(r\), consecutive
   \(2r\)/\(2r{+}1\) layers).

## 5. Prior-art search state at packet time

Directed audit found no exact match for the weight or the full package;
adjacent literature: multiplicative functions on powerful numbers,
squarefull integers in arithmetic progressions (Chan–Tsang; Srichan), and
general weighted k-full / Selberg–Delange frameworks. A research-grade
database sweep (MathSciNet/zbMATH) and cited-by chains are precisely what
this review requests; the internal search is not treated as sufficient.

## 6. Review questions and terminal protocol

The four pre-registered review questions (plus the memo's open fifth,
"what is missing") and the five materiality roles are listed in the memo; the pre-registered stopping protocol
(`../P8_STOPPING_PROTOCOL.md`) fixes one terminal classification per
outcome: known result / known machinery-new specialization / repairable
defect / structural defect / novel with separately-classified PVG
materiality.

```text
zero RH progress · zero GRH progress · no secured path
```

**Classification:** Result file for external review. Internally proved only; originality not claimed.
