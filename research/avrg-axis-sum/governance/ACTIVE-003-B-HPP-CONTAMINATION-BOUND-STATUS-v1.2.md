# ACTIVE-003-B — Higher-Prime-Power Contamination Bound Status

Status: `CLOSED-PROVED-v1.2`

## Scope

Bound the difference between the von Mangoldt additive mass

\[
R_\Lambda(N)=\sum_{a=1}^{N-1}\Lambda(a)\Lambda(N-a)
\]

and its prime-prime component

\[
R_{\mathrm{pp}}(N).
\]

## Proved results

1. Exact cumulative identity:

   \[
   S_{\mathrm{hpp}}(x)
   =\sum_{k=2}^{\lfloor\log_2x\rfloor}\vartheta(x^{1/k}).
   \]

2. Elementary bound:

   \[
   S_{\mathrm{hpp}}(x)\le\sqrt x\log x.
   \]

3. Computable contamination bound:

   \[
   0\le E_{\mathrm{hpp}}(N)
   \le2\log N\,S_{\mathrm{hpp}}(N).
   \]

4. Fully explicit bound:

   \[
   E_{\mathrm{hpp}}(N)
   \le2\sqrt N(\log N)^2.
   \]

5. Prime-prime lower bound:

   \[
   R_{\mathrm{pp}}(N)
   \ge R_\Lambda(N)-2\log N\,S_{\mathrm{hpp}}(N).
   \]

6. Conditional Goldbach certificate:

   \[
   R_\Lambda(N)>2\log N\,S_{\mathrm{hpp}}(N)
   \Longrightarrow
   R_{\mathrm{pp}}(N)>0.
   \]

## Verification

Verifier:

`code/verify_higher_prime_power_contamination_bound.py`

Result:

`results/higher_prime_power_contamination_bound_verification_v1.2.json`

Range:

- \(2\le N\le5000\);
- decomposition mismatches: 0;
- cumulative-bound mismatches: 0;
- computable-bound mismatches: 0;
- explicit-bound mismatches: 0.

Finite certificate summary over the tested even integers:

- even cases: 2500;
- certificate successes: 2489;
- certificate failures: 11.

This is finite computation only and is not a proof for untested values.

## Scientific classification

- decomposition: `identity`;
- cumulative bound: `proved elementary theorem`;
- contamination bound: `proved elementary theorem`;
- positivity implication: `conditional certificate`;
- Goldbach: `not proved`;
- new lower bound for \(R_\Lambda\): `absent`;
- novelty/priority: `not assessed`.

## Main gain

The analytic threshold is now explicit:

\[
\text{lower bound for }R_\Lambda(N)
>
\text{higher-prime-power envelope}
\]

is sufficient to force prime-prime mass.

## Next target

`ACTIVE-003-C — residue-sensitive higher-prime-power contamination`.

Replace the global envelope shared by every residue channel with bounds depending on

\[
2a-N\equiv d\pmod r.
\]

This is necessary before the marginal/joint measurement geometry can contribute more than a global scalar inequality.
