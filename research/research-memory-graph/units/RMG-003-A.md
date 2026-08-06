# RMG-003-A — Dirichlet Characters, Residue-Phase Observables, and L-Function Translation Registry

Status: completed / finite computational certificate PASS 7/7

Classification: Knowledge Architecture / Computational Verification / Diagnostic

Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Extend the Research Memory Graph from zeta-centered objects to Dirichlet characters, reduced residue classes, phase-weighted PVG observables, and Dirichlet L-functions.

## 2. Delivered artifacts

```text
research/research-memory-graph/registry/dirichlet-characters-residue-phase-lfunctions.jsonl
research/research-memory-graph/code/verify_rmg_003_a.py
research/research-memory-graph/results/rmg_003_a_verification.json
```

## 3. ANT objects

A Dirichlet character modulo `q` is periodic modulo `q`, completely multiplicative, and vanishes on integers not coprime to `q`.

For `Re(s)>1`,

\[
L(s,\chi)=\sum_{n\ge1}\frac{\chi(n)}{n^s}
=\prod_p\left(1-\frac{\chi(p)}{p^s}\right)^{-1}.
\]

The reduced-residue indicator is recovered through character orthogonality:

\[
1_{n\equiv a\pmod q}
=\frac1{\varphi(q)}\sum_\chi \overline{\chi(a)}\chi(n)
\]

for reduced residues.

## 4. PVG translation

For a valuation vector `v=nu(n)`, the character phase is read after decoding the integer modulo `q`:

```text
v -> n -> n mod q -> chi(n)
```

This gives:

- residue-channel phase labels;
- character-weighted log-height transforms;
- phase-weighted von Mangoldt observables;
- exact finite Fourier recovery on the reduced residue group.

The translation is exact at the coefficient and residue-channel level. It does not produce analytic continuation, a functional equation, a zero-free region, PNT in arithmetic progressions, or GRH.

## 5. Numerical verification

The harness uses all four characters modulo `5` and verifies:

1. periodicity;
2. complete multiplicativity;
3. character orthogonality;
4. residue-indicator recovery;
5. agreement between a truncated L-series and truncated Euler product at `s=2`;
6. registry uniqueness;
7. explicit rejection of two inflated claims.

Observed Euler-product comparison:

```text
series cutoff = 4999
prime cutoff  = 47
absolute gap  = 0.0003340151692380499
```

Result:

```text
PASS 7/7
```

## 6. Assimilation state

```text
DIRICHLET_CHARACTER = L4_NUMERICALLY_VERIFIED
CHARACTER_ORTHOGONALITY = L5_COMPUTATIONALLY_REGRESSION_TESTED
RESIDUE_INDICATOR_RECOVERY = L5_COMPUTATIONALLY_REGRESSION_TESTED
DIRICHLET_L_FUNCTION_IN_Re(s)>1 = L4_NUMERICALLY_VERIFIED
ANALYTIC_CONTINUATION = linked known ANT result, not established here
FUNCTIONAL_EQUATION = not assimilated in this unit
ZERO_DISTRIBUTION = not recovered
GRH = open / no progress
LEAN_PROOF_ADDED = none
L6_PROMOTION = not authorized
```

## 7. Scientific ceiling

```text
FINITE CHARACTER AND L-SERIES VERIFICATION
NOT A NEW CHARACTER THEOREM
NOT PNT IN ARITHMETIC PROGRESSIONS
NO NEW ZERO-FREE REGION
NO GRH PROGRESS
NO TRAINING CORPUS AUTHORIZATION
```

## 8. Acceptance decision

```text
CHARACTER_REGISTRY = PASS
RESIDUE_PHASE_TRANSLATION = PASS
ORTHOGONALITY_REGRESSION = PASS
L_SERIES_EULER_PRODUCT_FINITE_CHECK = PASS
CLAIM_BOUNDARY = PASS
RMG-003-A = COMPLETED
```

## 9. Next governed step

```text
RMG-003-B — Prime Distribution in Arithmetic Progressions,
Character-Weighted Chebyshev Observables,
and Zero-Free Certificate Ladder
```
