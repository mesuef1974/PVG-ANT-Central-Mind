# RMG-004-D — Large Sieve, Bombieri–Vinogradov, Average Distribution, and Certificate Transfer Boundary

**Status:** COMPLETED  
**Branch:** `agent/pvg-axis-sum-continuation-002`  
**Classification:** known-theorem dependency graph + finite diagnostics + claim-boundary unit  
**Regression:** PASS 8/8

## 1. Purpose

This unit integrates the large sieve and Bombieri–Vinogradov layer into the Research Memory Graph while preserving the distinction between:

1. finite quadratic-energy identities and diagnostics;
2. known average-distribution theorems;
3. uniform pointwise distribution;
4. prime-producing transfer statements.

No new distribution theorem is claimed.

## 2. Core ANT objects

### 2.1 Large-sieve energy

The large sieve controls families of correlations of the form

\[
\sum_r \left|\sum_n a_n e(\alpha_r n)\right|^2
\]

or their character analogues by a quadratic norm depending on the coefficient length and frequency spacing/modulus range.

The exact constant and formulation depend on the chosen additive or multiplicative version. This unit records the dependency pattern, not a new proof of a sharp inequality.

### 2.2 Bombieri–Vinogradov layer

The Bombieri–Vinogradov theorem gives average distribution of primes over moduli up to near square-root scale, with logarithmic losses. It is stored as known literature and not as a project theorem.

The governing distinction is:

```text
average control over many moduli
!=
uniform pointwise control for every modulus
```

### 2.3 Distribution exponent boundary

The square-root-scale average range supplied by Bombieri–Vinogradov is not the Elliott–Halberstam conjecture and does not supply distribution exponent one.

## 3. ANT → PVG translation

For each valuation vector `v = nu(n)`:

1. decode `n`;
2. route it into residue channels modulo `q`;
3. attach additive or character phase;
4. aggregate linear correlations or squared energy.

This gives an exact finite reindexing:

\[
\sum_n a_n e(an/q)
=
\sum_v A(v)e\!\left(a\,\operatorname{decode}(v)/q\right).
\]

The translation preserves finite coefficients, phases, and energy sums. It does not create cancellation or an asymptotic theorem.

## 4. Reverse translation and loss

A PVG residue-channel energy can be decoded back to the corresponding finite ANT sum. However, after summing over moduli, the aggregate may lose:

- which modulus is exceptional;
- which residue channel causes the error;
- sign and phase structure after absolute values or squares;
- target purity;
- pointwise information.

Thus average aggregation is noninjective.

## 5. Certificate ladder

```text
finite phase-energy computation
< large-sieve theorem certificate
< average distribution certificate
< pointwise distribution certificate
< prime-producing transfer certificate
```

Each transition requires its own assumptions and proof.

In particular:

```text
large sieve inequality alone
!=
Bombieri–Vinogradov theorem
```

because the latter also uses arithmetic decompositions and prime-sensitive coefficient control.

Likewise:

```text
Bombieri–Vinogradov
!=
prime-producing theorem for an arbitrary target
```

because target weights, local obstructions, lower-bound transfer, and parity/target-purity issues remain.

## 6. Negative benchmark

Take 100 nonnegative errors with 99 equal to zero and one equal to 10. Then

\[
\frac1{100}\sum_{j=1}^{100}E_j=0.1,
\qquad
\max_j E_j=10.
\]

Therefore a small average does not imply the same pointwise bound for every modulus.

This is the finite regression witness for the average-to-pointwise failure.

## 7. Numerical verification

The public harness performs eight checks:

1. registry count;
2. unique identifiers;
3. finite large-sieve-style energy bound;
4. average-versus-pointwise counterexample;
5. computability of an average residue-discrepancy norm;
6. required registry types;
7. claim-rejection records;
8. claim-ceiling enforcement.

Numerical snapshot:

```text
phase energy                = 1987.999999999998
reference quadratic bound   = 18150
energy / bound              = 0.10953168044077123
finite residue discrepancy  = 8.55874285673049
```

These are regression diagnostics only.

## 8. Assimilation levels

```text
finite phase-energy reindexing          = L4
average aggregation-loss counterexample = L5
certificate separation                  = L5
large-sieve dependency graph             = L3
Bombieri–Vinogradov dependency graph     = L3
square-root distribution boundary        = L3
Elliott–Halberstam                       = mentioned boundary only
Lean proof added                         = none
L6 promotion                             = not authorized
```

## 9. Scientific ceiling

This unit does not claim:

- a new large-sieve inequality;
- a proof of Bombieri–Vinogradov;
- Elliott–Halberstam;
- a prime-producing asymptotic;
- progress on the parity barrier;
- progress on RH or GRH.

## 10. Artifacts

- `registry/large-sieve-bombieri-vinogradov-average-boundary.jsonl`
- `code/verify_rmg_004_d.py`
- `results/rmg_004_d_verification.json`
- `units/RMG-004-D.md`

## 11. Next unit

```text
RMG-005-A
Additive Characters, Exponential Sums,
Finite Fourier Transform, and Cancellation-Certificate Graph
```
