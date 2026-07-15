# Higher-Prime-Power Contamination Bound for the von Mangoldt Additive Fiber

Status: `proved theorem / elementary bound / no Goldbach claim`

## 1. Definitions

For an integer \(N\ge 2\), define

\[
R_\Lambda(N)=\sum_{a=1}^{N-1}\Lambda(a)\Lambda(N-a).
\]

Write

\[
\Lambda=\Lambda_{\mathrm{pr}}+\Lambda_{\mathrm{hpp}},
\]

where

\[
\Lambda_{\mathrm{pr}}(n)=\begin{cases}\log n,&n\text{ prime},\\0,&\text{otherwise},\end{cases}
\]

and

\[
\Lambda_{\mathrm{hpp}}(n)=\begin{cases}\log p,&n=p^k,\ k\ge2,\\0,&\text{otherwise}.\end{cases}
\]

Define

\[
R_{\mathrm{pp}}(N)=\sum_{a=1}^{N-1}\Lambda_{\mathrm{pr}}(a)\Lambda_{\mathrm{pr}}(N-a),
\]

and the higher-prime-power contamination

\[
E_{\mathrm{hpp}}(N)=R_\Lambda(N)-R_{\mathrm{pp}}(N)\ge0.
\]

Also define the cumulative higher-prime-power von Mangoldt mass

\[
S_{\mathrm{hpp}}(x)=\sum_{n\le x}\Lambda_{\mathrm{hpp}}(n)
=\sum_{\substack{p^k\le x\\k\ge2}}\log p.
\]

## 2. Exact Chebyshev decomposition

Let

\[
\vartheta(y)=\sum_{p\le y}\log p.
\]

Then

\[
\boxed{
S_{\mathrm{hpp}}(x)=\sum_{k=2}^{\lfloor\log_2 x\rfloor}\vartheta(x^{1/k}).
}
\]

This is an identity, not an asymptotic estimate.

## 3. Elementary cumulative bound

For every prime \(p\le\sqrt x\), the number of exponents \(k\ge2\) such that \(p^k\le x\) is at most

\[
\frac{\log x}{\log p}-1.
\]

Therefore the total contribution from a fixed base prime is at most

\[
\left(\frac{\log x}{\log p}-1\right)\log p\le\log x.
\]

Summing over \(p\le\sqrt x\),

\[
S_{\mathrm{hpp}}(x)
\le \pi(\sqrt x)\log x
\le \sqrt x\log x.
\]

Hence

\[
\boxed{
S_{\mathrm{hpp}}(x)\le \sqrt x\log x.
}
\]

No prime number theorem is used.

## 4. Global contamination theorem

Every term contributing to \(E_{\mathrm{hpp}}(N)\) has at least one higher-prime-power coordinate. By a union bound over the two coordinates,

\[
E_{\mathrm{hpp}}(N)
\le
2\sum_{a=1}^{N-1}\Lambda_{\mathrm{hpp}}(a)\Lambda(N-a).
\]

Since

\[
\Lambda(N-a)\le\log N,
\]

we obtain

\[
E_{\mathrm{hpp}}(N)
\le 2\log N\,S_{\mathrm{hpp}}(N).
\]

Combining with the elementary cumulative estimate gives

\[
\boxed{
0\le E_{\mathrm{hpp}}(N)
\le 2\log N\,S_{\mathrm{hpp}}(N)
\le 2\sqrt N(\log N)^2.
}
\]

The first upper bound is sharper and computationally evaluable; the second is fully explicit.

## 5. Prime-pair lower bound

Because

\[
R_{\mathrm{pp}}(N)=R_\Lambda(N)-E_{\mathrm{hpp}}(N),
\]

we have

\[
\boxed{
R_{\mathrm{pp}}(N)
\ge R_\Lambda(N)-2\log N\,S_{\mathrm{hpp}}(N).
}
\]

In particular,

\[
\boxed{
R_{\mathrm{pp}}(N)
\ge R_\Lambda(N)-2\sqrt N(\log N)^2.
}
\]

## 6. Conditional Goldbach certificate

If \(N\) is even and

\[
R_\Lambda(N)>2\log N\,S_{\mathrm{hpp}}(N),
\]

then

\[
R_{\mathrm{pp}}(N)>0,
\]

so there exists at least one ordered pair of primes \(p,q\) such that

\[
p+q=N.
\]

A simpler sufficient condition is

\[
\boxed{
R_\Lambda(N)>2\sqrt N(\log N)^2.
}
\]

This is a reduction criterion only. No lower bound of this strength for all even \(N\) is proved here, so this does not prove Goldbach.

## 7. Channelwise consequence

Let

\[
Y_{N,r}^{\Lambda}(d)
=\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}
\Lambda(a)\Lambda(N-a),
\]

and define \(Y_{N,r}^{\mathrm{pp}}(d)\) analogously with \(\Lambda_{\mathrm{pr}}\). Then

\[
0\le
Y_{N,r}^{\Lambda}(d)-Y_{N,r}^{\mathrm{pp}}(d)
\le E_{\mathrm{hpp}}(N)
\le2\log N\,S_{\mathrm{hpp}}(N).
\]

Thus every residue channel inherits the same rigorous global contamination envelope. A useful local theory would require sharper residue-sensitive bounds.

## 8. Interpretation for PVG–ANT

The theorem creates the first explicit bridge of the form

\[
\text{von Mangoldt additive mass}
-\text{controlled prime-power contamination}
\Longrightarrow
\text{prime-pair mass}.
\]

The remaining analytic burden is now precise:

1. produce a lower bound for \(R_\Lambda(N)\), globally or in selected channels;
2. improve the contamination estimate, preferably residue by residue;
3. compare the lower bound with the contamination envelope.

## 9. Scientific ceiling

Classification:

- decomposition: `identity`;
- contamination estimate: `proved elementary theorem`;
- Goldbach implication: `conditional certificate`;
- Goldbach theorem: `not proved`;
- novelty or priority: `not assessed`.
