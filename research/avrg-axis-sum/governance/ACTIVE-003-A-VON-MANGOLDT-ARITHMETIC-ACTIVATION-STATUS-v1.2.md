# ACTIVE-003-A — Von Mangoldt Arithmetic Activation Status

Status: `CLOSED / PASS`

## Completed

- Defined the arithmetic fiber weight
  \[
  w_N(a)=\Lambda(a)\Lambda(N-a).
  \]
- Identified the total mass with
  \[
  R_\Lambda(N)=\sum_{a=1}^{N-1}\Lambda(a)\Lambda(N-a).
  \]
- Proved the difference-channel mass identity.
- Proved channel reflection symmetry.
- Proved support on prime-power pairs.
- Decomposed the observable exactly into prime-prime, mixed, and higher-prime-power terms.
- Activated the previously proved `D`, `M`, and `J` information theory on the arithmetic weight.
- Added finite verification for `2 <= N <= 200` and `1 <= r <= 40` with zero mismatches.
- Added worked examples for `N=10,12,24,30`.

## Verification receipt

```text
mass checks          = 7,960
symmetry checks      = 163,180
support checks       = 2,315
decomposition checks = 183,080
mismatch count       = 0
status               = PASS
```

## Scientific classification

- Exact definitions: proved.
- Exact identities: proved.
- Numerical examples: finite evaluation.
- New prime estimate: none.
- Goldbach progress: none claimed.
- RH/GRH progress: none claimed.

## Central lesson

Positivity of

\[
R_\Lambda(N)
\]

is not by itself a pure Goldbach certificate because higher prime powers can contribute. The next unit must isolate

\[
R_{\mathrm{pp}}(N)
\]

or control the contamination

\[
E_{\mathrm{hpp}}(N)
=
2R_{\mathrm{ph}}(N)+R_{\mathrm{hh}}(N).
\]

## Next target

`ACTIVE-003-B — Higher-prime-power contamination bounds and prime-only channel isolation.`

The valid target is an exact decomposition plus honest upper bounds. No claim of a new lower bound for Goldbach representations is authorized unless such a bound is actually proved.
