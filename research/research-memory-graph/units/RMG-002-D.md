# RMG-002-D — von Mangoldt / Logarithmic Derivative / Chebyshev Observable Graph

Status: completed / finite computational certificate PASS 10/10

Classification: Known identities / PVG translation / certificate discipline

Branch: `agent/pvg-axis-sum-continuation-002`

## Mission

Connect the von Mangoldt function to the logarithmic derivative of zeta and to the Chebyshev observables without collapsing finite identities, half-plane analytic identities, explicit-formula machinery, or RH into one claim.

## Delivered artifacts

- `registry/von-mangoldt-log-derivative-chebyshev.jsonl`
- `code/verify_rmg_002_d.py`
- `results/rmg_002_d_verification.json`

## Core identities

For `Re(s)>1`,

\[
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=\sum_p\frac{\log p}{p^s-1}.
\]

For finite `x`,

\[
\psi(x)=\sum_{n\le x}\Lambda(n),
\qquad
\theta(x)=\sum_{p\le x}\log p,
\]

and

\[
\psi(x)=\sum_{k\ge1}\theta(x^{1/k}),
\]

where the last sum is finite because only `k` with `2^k<=x` contribute.

The prime-power contamination is exactly

\[
\psi(x)-\theta(x)
=
\sum_{p^k\le x,\,k\ge2}\log p.
\]

## PVG translation

`Lambda` is the exact single-axis observable

\[
\Lambda_{PVG}(v)=
\begin{cases}
\log p,&v=k e_p,\ k\ge1,\\
0,&|\operatorname{supp}(v)|\ne1.
\end{cases}
\]

Thus `theta` aggregates only unit-axis points, while `psi` aggregates all positive points on each prime axis. The difference `psi-theta` is therefore the contribution of axis heights at least two.

This geometric reading is exact as a reindexing. It does not produce analytic continuation, a zero-free region, an explicit formula, zero recovery, or RH progress.

## Verification

The stdlib-only harness records PASS 10/10, including:

- exact support of `Lambda` on prime powers for `1<=n<=1000`;
- `psi` from `Lambda` and `theta` from primes;
- `psi=sum_k theta(x^(1/k))` for `x=10,30,100,300,1000`;
- exact prime-power contamination decomposition;
- at `s=2`, cutoff `5000`:

```text
Lambda series   = 0.5697609831853476
prime-power sum = 0.5697621521507613
absolute gap    = 1.1689654136892713e-06
```

- ANT/PVG log-height reindexing equality within floating tolerance;
- rejection of finite-psi-implies-RH;
- rejection of single-axis-observable-implies-zero-recovery.

## Assimilation state

```text
VON_MANGOLDT_OBSERVABLE = L5_COMPUTATIONALLY_REGRESSION_TESTED
THETA_PSI_FINITE_IDENTITIES = L5_COMPUTATIONALLY_REGRESSION_TESTED
LOGARITHMIC_DERIVATIVE_IDENTITY = L4_NUMERICALLY_VERIFIED within Re(s)>1
EXPLICIT_FORMULA = linked but not assimilated by this unit
ZERO_RECOVERY = absent
RH_PROGRESS = none
LEAN_PROOF_ADDED = none
L6_PROMOTION = not authorized
```

## Scientific ceiling

```text
KNOWN IDENTITIES + FINITE COMPUTATION
NO NEW PRIME NUMBER THEOREM
NO NEW ZERO-FREE REGION
NO ZERO RECOVERY
NO RH OR GRH PROGRESS
```

## Acceptance

```text
DEPENDENCY_REGISTRY = PASS
FINITE_CHEBYSHEV_IDENTITIES = PASS
LOG_DERIVATIVE_HALF_PLANE_CHECK = PASS
PVG_SINGLE_AXIS_TRANSLATION = PASS
ANTI_COLLAPSE_GUARDS = PASS
RMG-002-D = COMPLETED
```

## Next governed step

`RMG-002-E — Prime Number Theorem Equivalence Graph and Error-Term Certificate Ladder`.
