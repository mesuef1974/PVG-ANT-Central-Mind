# One-Theorem Program 001 — P6 Adversarial Proof Review

**Reviewed files:** P2 and P3–P5 manual proofs.  
**Decision:** `PASS MANUAL LOGIC / SOURCE AND PRIORITY GATES REMAIN`.

## 1. Adversarial questions

### A. Is the arithmetic function actually multiplicative?

**Pass.** The local count factors over disjoint prime coordinates. `I_r(1)=1` is explicitly declared.

### B. Is the Bell series correct at the threshold exponent?

**Pass.** At `a=2r`, exactly one coordinate value `v_p(d)=r` is allowed, and the coefficient is `1`. The series begins with `y^(2r)`.

### C. Does extraction of the L-factors work at bad primes?

**Pass.** Characters are extended by zero. At `p|q`, `y_p=0`; the Bell, L, and residual local factors are all `1`.

### D. Is the residual order genuinely `2r+2`?

**Pass.** The coefficients at degrees `2r` and `2r+1` cancel. Symbolic checks for `r=1,...,8` agree. P2 supplies the general big-O proof.

### E. Is the original series absolutely convergent on the starting line?

**Pass.** Its prime-local nonconstant mass is `O(p^(-2r sigma))`, so `sigma>1/(2r)` suffices.

### F. Does the residual Euler product converge on the claimed half-plane?

**Pass.** On compact subsets of `sigma>1/(2r+2)`, the local deviations have summable majorant `p^(-(2r+2)sigma_0)`. The proof correctly claims holomorphy, not nonvanishing.

### G. Are there hidden poles besides `1/(2r)` and `1/(2r+1)`?

**Pass.** The residual product is holomorphic. Dirichlet L-functions can have a pole only for a principal character at argument `1`. Zeros do not create singularities because no reciprocal L-factor remains.

### H. Can both torsion conditions hold?

**Pass with clarification.** If both hold, `chi=chi_0` since `gcd(2r,2r+1)=1`. The two poles remain distinct, so their residues are simply added.

### I. Is character orthogonality valid for non-coprime `n`?

**Pass.** The right side vanishes because every character is zero there. The left side also vanishes because `n` cannot be congruent to reduced `a` modulo `q`.

### J. Is there an accidental Perron factor `1/s`?

**Pass.** No. The theorem uses Mellin inversion of `W(n/x)`, whose integrand is `D(s) W-hat(s) x^s`; there is no `1/s`. The residue constants were derived accordingly.

### K. Is the Mellin transform entire and rapidly decreasing?

**Pass under the stated hypothesis.** `W` has compact support contained in `(0,infinity)`, so repeated integration by parts gives rapid decay in every fixed vertical strip.

### L. Is the contour line actually left of both poles?

**Pass after the explicit epsilon reduction.** The proof first handles small epsilon with

\[
1/(2r+2)+\varepsilon<1/(2r+1),
\]

then obtains the statement for arbitrary larger epsilon by monotonic weakening of the error exponent.

### M. Are horizontal contour segments controlled?

**Pass at standard fixed-parameter level.** `H` is vertically bounded on the shifted line; fixed-modulus L-functions have polynomial vertical growth; `W-hat` decays faster than every power.

**Source gate remains:** cite an exact fixed-strip L-growth theorem in the final proof certificate.

### N. Are the simple-pole constants correct?

**Pass.** Scaling `u=2rs` contributes `1/(2r)` to the residue.

### O. Are the double-pole constants correct?

**Pass.** Independent symbolic expansion confirms both the logarithmic coefficient and the derivative/finite-part constant. No `1/s` derivative is present.

### P. Is the finite part of the principal character correct?

**Pass.** Differentiating

\[
\prod_{p|q}(1-p^{-s})
\]

gives the positive correction

\[
\sum_{p|q}\log p/(p-1).
\]

High-precision checks at `q=1,2,6,30` agree.

### Q. Is the error uniform in the residue class?

**Pass for fixed q.** The dependence on `a` is only through `conj(chi(a))`, of modulus one. No uniformity in growing `q` or `r` is claimed.

### R. Does the proof establish an original result?

**No.** It establishes a logically complete candidate theorem using classical methods. Priority remains unresolved for the exact weighted statement.

### S. Is the claimed torsion mechanism itself new?

**No.** Quadratic/cubic torsion layers already occur in classical square-full progression work. The possible contribution is the margin-interior weight, general layer hierarchy, and explicit smoothed weighted formula.

## 2. Corrections forced by review

No mathematical formula in the current frozen target requires correction.

The originality description is narrowed permanently:

```text
Not new: torsion selection as a general square/cube phenomenon.
Potentially new: the divisor-box margin weight and its complete weighted smoothed expansion.
```

## 3. Remaining gates

1. exact citation for polynomial vertical growth of fixed-modulus L-functions;
2. exact citation for Mellin inversion/rapid decay, or include its elementary proof;
3. inspect older square-full progression references named by Chan;
4. independent line-by-line human review of the full manuscript proof;
5. determine whether a general weighted k-full theorem subsumes the statement.

## 4. Current classification

```text
Local factorization lemma: proved manually.
Smoothed theorem: complete manual proof candidate.
Symbolic constants: independently verified.
Adversarial logical review: PASS.
Source-grounded analytic review: pending exact citations.
Originality: plausible but unconfirmed.
Certified original theorem: NO.
RH/GRH progress: NONE.
```
