# Local-Channel Fourier Decomposition for von Mangoldt Addition Fibers

Status: `PROVED-v1.2`

## 1. Setup

Fix integers \(N\ge2\) and \(r\ge1\). Write

\[
e_r(x)=\exp(2\pi i x/r).
\]

For \(1\le a<N\), let

\[
w_N(a)=\Lambda(a)\Lambda(N-a).
\]

The von Mangoldt mass in difference channel \(d\in\mathbb Z/r\mathbb Z\) is

\[
Y_{N,r}^{\Lambda}(d)
=
\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}
\Lambda(a)\Lambda(N-a).
\]

Define the Fourier coefficient

\[
\widehat Y_{N,r}^{\Lambda}(h)
=
\sum_{a=1}^{N-1}
\Lambda(a)\Lambda(N-a)
\,e_r\!\bigl(h(2a-N)\bigr),
\qquad h\in\mathbb Z/r\mathbb Z.
\]

## 2. Exact Fourier inversion theorem

For every \(d\in\mathbb Z/r\mathbb Z\),

\[
\boxed{
Y_{N,r}^{\Lambda}(d)
=
\frac1r\sum_{h\bmod r}
\widehat Y_{N,r}^{\Lambda}(h)e_r(-hd)
}
\]

and since

\[
\widehat Y_{N,r}^{\Lambda}(0)
=
R_{\Lambda}(N)
:=
\sum_{a=1}^{N-1}\Lambda(a)\Lambda(N-a),
\]

we obtain the zero-mode/nonzero-mode decomposition

\[
\boxed{
Y_{N,r}^{\Lambda}(d)
=
\frac{R_{\Lambda}(N)}{r}
+
\Delta_{N,r}^{\Lambda}(d)
}
\]

where

\[
\Delta_{N,r}^{\Lambda}(d)
=
\frac1r\sum_{\substack{h\bmod r\\h\ne0}}
\widehat Y_{N,r}^{\Lambda}(h)e_r(-hd).
\]

Proof: insert the finite-group orthogonality identity

\[
\mathbf 1_{x\equiv d\,(r)}
=
\frac1r\sum_{h\bmod r}e_r(h(x-d))
\]

with \(x=2a-N\), then interchange the finite sums.

## 3. Reality and reflection

The involution \(a\mapsto N-a\) sends \(2a-N\) to its negative and preserves the weight. Therefore

\[
\widehat Y_{N,r}^{\Lambda}(h)
=
\widehat Y_{N,r}^{\Lambda}(-h)
=
\overline{\widehat Y_{N,r}^{\Lambda}(h)},
\]

so every Fourier coefficient is real. Consequently

\[
\Delta_{N,r}^{\Lambda}(d)
=
\Delta_{N,r}^{\Lambda}(-d)
\]

and

\[
Y_{N,r}^{\Lambda}(d)=Y_{N,r}^{\Lambda}(-d).
\]

Equivalently,

\[
\widehat Y_{N,r}^{\Lambda}(h)
=
\sum_{a=1}^{N-1}
\Lambda(a)\Lambda(N-a)
\cos\!\left(\frac{2\pi h(2a-N)}r\right).
\]

## 4. Prime-only channel and contamination

Let

\[
Y_{N,r}^{\mathrm{pp}}(d)
=
\sum_{\substack{p+q=N\\p,q\ \mathrm{prime}\\p-q\equiv d\pmod r}}
\log p\log q.
\]

Let \(E_{N,r}^{\mathrm{hpp}}(d)\) denote the contribution in channel \(d\) from pairs for which at least one summand is a higher prime power. Then

\[
Y_{N,r}^{\Lambda}(d)
=
Y_{N,r}^{\mathrm{pp}}(d)
+
E_{N,r}^{\mathrm{hpp}}(d).
\]

From the local contamination theorem,

\[
E_{N,r}^{\mathrm{hpp}}(d)
\le
C_{N,r}(d)
:=
\log N\bigl(H_{N,r}(d)+H_{N,r}(-d)\bigr).
\]

Hence

\[
\boxed{
Y_{N,r}^{\mathrm{pp}}(d)
\ge
\frac{R_{\Lambda}(N)}r
+
\Delta_{N,r}^{\Lambda}(d)
-
C_{N,r}(d)
}
\]

and therefore the exact sufficient condition

\[
\boxed{
\frac{R_{\Lambda}(N)}r
+
\Delta_{N,r}^{\Lambda}(d)
>
C_{N,r}(d)
\Longrightarrow
Y_{N,r}^{\mathrm{pp}}(d)>0.
}
\]

## 5. Uniform analytic certificate

Suppose an analytic argument proves

\[
|\Delta_{N,r}^{\Lambda}(d)|\le B_{N,r}(d).
\]

Then

\[
Y_{N,r}^{\mathrm{pp}}(d)
\ge
\frac{R_{\Lambda}(N)}r
-
B_{N,r}(d)
-
C_{N,r}(d).
\]

Thus the verifiable sufficient condition is

\[
\boxed{
\frac{R_{\Lambda}(N)}r
>
B_{N,r}(d)+C_{N,r}(d)
\Longrightarrow
\exists\ p,q\ \mathrm{prime}:
\ p+q=N,
\ p-q\equiv d\pmod r.
}
\]

A channel-uniform version follows from any bound

\[
\max_d|\Delta_{N,r}^{\Lambda}(d)|\le B_{N,r}.
\]

## 6. Exact target exposed by the framework

The framework reduces the local prime-representation problem to three terms:

1. a lower bound for the global zero mode \(R_{\Lambda}(N)\);
2. an upper bound for the nonzero Fourier deviation \(\Delta_{N,r}^{\Lambda}(d)\);
3. the explicit local higher-prime-power contamination \(C_{N,r}(d)\).

No Goldbach theorem follows from the identity alone. The genuinely analytic burden is to prove a lower bound whose zero-mode contribution dominates both the nonzero-frequency error and the local contamination.

## 7. Classification

- Fourier inversion: `Identity / proved`.
- Reality and reflection: `Proved finite symmetry`.
- Local prime-channel lower bound: `Proved consequence`.
- Uniform certificate template: `Proved conditional implication`.
- New global Goldbach result: `Not claimed`.
- RH/GRH progress: `None`.
