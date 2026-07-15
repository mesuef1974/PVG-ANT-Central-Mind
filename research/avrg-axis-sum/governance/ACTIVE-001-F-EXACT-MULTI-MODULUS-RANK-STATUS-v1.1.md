# ACTIVE-001-F — Exact Multi-Modulus Rank Status v1.1

## Decision

`CLOSED — PROVED AND VERIFIED`

## Result

For a modulus family

\[
\mathbf r=(r_1,\dots,r_k),
\qquad
q_j=\frac{r_j}{\gcd(2,r_j)},
\qquad
L=\operatorname{lcm}(q_1,\dots,q_k),
\]

define the Fourier subgroups

\[
H_j=\{m\in\mathbb Z/L\mathbb Z:m\equiv0\pmod{L/q_j}\}.
\]

Then

\[
\operatorname{rank}M_{N;\mathbf r}
=
\min\!\left(N-1,\left|\bigcup_{j=1}^kH_j\right|\right).
\]

By inclusion-exclusion,

\[
\left|\bigcup_{j=1}^kH_j\right|
=
\sum_{\varnothing\ne S\subseteq[k]}
(-1)^{|S|+1}\gcd(q_j:j\in S).
\]

Therefore the exact arbitrary-family formula is

\[
\boxed{
\operatorname{rank}M_{N;\mathbf r}
=
\min\!\left(
N-1,
\sum_{\varnothing\ne S\subseteq[k]}
(-1)^{|S|+1}\gcd(q_j:j\in S)
\right).
}
\]

## Consequences

1. Exact injectivity criterion:

   \[
   M_{N;\mathbf r}\text{ injective}
   \iff
   N-1\le\left|\bigcup_jH_j\right|.
   \]

2. Exact joint-versus-marginal rank gap:

   \[
   \operatorname{rank}J_{N;\mathbf r}
   -
   \operatorname{rank}M_{N;\mathbf r}
   =
   \min(N-1,L)-\min(N-1,|\cup_jH_j|).
   \]

3. A modulus with effective period dividing that of another contributes no new marginal rank.

4. The previous statement that exact rank for three or more marginals was open is superseded by this theorem.

## Evidence

Verifier:

`research/avrg-axis-sum/code/verify_multi_modulus_exact_rank_fourier_union.py`

Result:

`research/avrg-axis-sum/results/multi_modulus_exact_rank_fourier_union_verification_v1.1.json`

Verification scope:

```text
families of size 2 through 5
cases checked = 5,220
mismatch count = 0
maximum rank error = 0
status = PASS
```

## Classification

- theorem: `PROVED`;
- finite verification: `PASS`;
- originality/priority: `NOT AUTHORIZED` pending deeper literature review;
- Goldbach/RH/GRH progress: `NONE`.

## Next target

`ACTIVE-001-G — optimal modulus selection and conditioning under a fixed measurement budget`.
