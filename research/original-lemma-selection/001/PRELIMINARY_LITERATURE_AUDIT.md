# Preliminary Literature Audit — Original Lemma Selection 001

**Scope:** first-pass priority and method audit for the three preliminary finalists.  
**Status:** incomplete / not an originality certificate.  
**Search date:** 2026-07-12.

## 1. Search target

The search focused on the exact multiplicative observables

\[
\Phi_z(n)=\prod_{p^a\parallel n}(a-1+2z)
\]

and

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0),
\]

plus their Dirichlet-series factorizations, weighted powerful-number averages, and residue-class twists.

No exact match for the displayed face-enumerator family or the weight `prod(a-1)` was located in the initial searches. This absence is weak evidence only: terminology may differ, older non-digitized literature may contain the result, and general multiplicative-function theorems may subsume it without naming the observable.

## 2. Method-level prior art

### Selberg–Delange

R. de la Bretèche and G. Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929.

This supplies general asymptotic machinery for multiplicative functions whose Dirichlet series has the form `zeta(s)^rho G(s)`. It is the nearest general method for `OLS-CAND-001`. Therefore a proof obtained by direct substitution into Selberg–Delange is methodologically classical even if the geometric observable is new.

### Powerful and square-full numbers

Relevant modern sources located in the initial pass include:

- T. H. Chan, *A note on powerful numbers in short intervals*, arXiv:2207.08874;
- T. H. Chan, *Arithmetic progressions among powerful numbers*, arXiv:2210.00281;
- P. Bajpai, M. A. Bennett, T. H. Chan, *Arithmetic Progressions in Squarefull Numbers*, arXiv:2302.03113;
- M. Munsch, I. E. Shparlinski, K. H. Yau, *Smooth square-free and square-full integers in arithmetic progressions*, arXiv:1810.02573.

These papers show that powerful/square-full support and arithmetic progressions are active classical subjects. They do not, from the abstracts and searchable text inspected, state the same weighted interior-box asymptotic or the proposed torsion-character expansion.

## 3. Candidate-specific audit

### OLS-CAND-001 — Face-enumerator mean

Nearest framework: Selberg–Delange for `zeta(s)^(2z) G_z(s)`.

Potentially new component:

- the divisor-box face enumerator as a natural PVG observable;
- a uniform complex-parameter theorem stated directly for all face strata.

Risk:

- the asymptotic may be a routine corollary of a general theorem;
- novelty may be primarily the observable and interpretation, not the analytic argument.

**Preliminary verdict:** retain, but not preferred as the first theorem unless the parameter-uniformity or a face-stratum consequence adds substance.

### OLS-CAND-002 — Interior two-scale asymptotic

Nearest framework:

- classical counting of powerful/square-full numbers;
- Euler-product extraction at `2s` and `3s`;
- Perron/contour or a suitable general theorem for multiple singularities.

Potentially new component:

- the weight `I(n)=prod(a_p-1)`, counting strict interior divisor-box points;
- explicit simultaneous square-layer and cube-layer terms;
- geometric interpretation of the secondary scale.

Risk:

- a general theorem on weighted powerful numbers may already imply the formula;
- the proposed `O_epsilon(x^(1/4+epsilon))` error may require substantially more work or may be false at that strength;
- constants and pole interactions need a full derivation.

**Preliminary verdict:** strongest bounded candidate; retain as leading finalist.

### OLS-CAND-005 — Torsion-character residue bias

Nearest framework:

- character decomposition in arithmetic progressions;
- twisted Euler products;
- existing work on square-full numbers in arithmetic progressions.

Potentially new component:

- the explicit rule that geometric exponent layers `2r` and `2r+1` select torsion characters satisfying `chi^(2r)=chi_0` or `chi^(2r+1)=chi_0`;
- a weighted divisor-box observable rather than the unweighted indicator of powerful numbers.

Risk:

- for fixed modulus the result may be a direct consequence of standard character decomposition plus residue calculus;
- existing square-full AP literature may contain an equivalent expansion under different notation;
- uniformity in `q` would greatly increase difficulty and is not part of the current candidate.

**Preliminary verdict:** retain as the most conceptually PVG-dependent finalist, but require the deepest priority audit.

## 4. Killed candidates and known frameworks

- `OLS-CAND-007`: elementary triangular incidence-matrix rank.
- `OLS-CAND-008`: finite Möbius inversion.
- `OLS-CAND-009`: likely consequence of the Poisson–Dirichlet limit for normalized logarithmic prime factors; exact citation still required for the stated moment.
- `OLS-CAND-010`: direct character orthogonality/Parseval for an arbitrary weight.

## 5. Current evidence table

| Candidate | Exact searchable match found? | General method known? | PVG necessity | Current rank |
|---|---:|---:|---:|---:|
| OLS-CAND-001 | no | yes, Selberg–Delange | medium-high | 2 |
| OLS-CAND-002 | no | yes, weighted powerful-number/Euler-product methods | high | 1 |
| OLS-CAND-005 | no | yes, characters and AP methods | very high | 3 pending deep audit |

## 6. Required deeper audit before freezing

1. Search MathSciNet/zbMATH-style terminology for weighted powerful numbers, exponent weights, and divisor-lattice interior points.
2. Inspect classical powerful-number counting papers, not only recent abstracts.
3. Derive the exact constants and feasible error for `OLS-CAND-002`.
4. Compare `OLS-CAND-005` with explicit formulas for square-full numbers in fixed residue classes.
5. Decide whether the first theorem should optimize originality, tractability, or PVG necessity.

## 7. Ceiling

```text
No candidate is certified original.
No proof has begun.
No theorem is claimed.
No RH/GRH progress.
```
