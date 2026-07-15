# Local Channel Higher-Prime-Power Contamination Bound v1.2

Status: PROVED
Classification: arithmetic activation / local sufficient certificate

## 1. Setup

For fixed `N >= 2`, modulus `r >= 1`, and residue channel `d mod r`, define

\[
Y_{N,r}^{\Lambda}(d)
=
\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}
\Lambda(a)\Lambda(N-a).
\]

Let `Lambda_pr` be the von Mangoldt weight restricted to primes, and let `Lambda_hpp` be the restriction to higher prime powers `p^k`, `k>=2`.

Define the prime-prime channel mass

\[
Y_{N,r}^{pp}(d)
=
\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}
\Lambda_{pr}(a)\Lambda_{pr}(N-a),
\]

and the higher-prime-power contamination

\[
E_{N,r}^{hpp}(d)
=
Y_{N,r}^{\Lambda}(d)-Y_{N,r}^{pp}(d).
\]

Also define the local higher-prime-power mass

\[
H_{N,r}(d)
=
\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}
\Lambda_{hpp}(a).
\]

## 2. Reflection identity

Under `a -> N-a`, the difference channel changes sign:

\[
2(N-a)-N=-(2a-N).
\]

Therefore

\[
\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}
\Lambda_{hpp}(N-a)
=
H_{N,r}(-d).
\]

## 3. Local contamination theorem

For every `N,r,d`,

\[
\boxed{
0\le E_{N,r}^{hpp}(d)
\le
\log N\bigl(H_{N,r}(d)+H_{N,r}(-d)\bigr).
}
\]

### Proof

For each channel index `a`, write `b=N-a`. If neither `a` nor `b` is a higher prime power, the contamination contribution is zero. Otherwise,

\[
\Lambda(a)\Lambda(b)-\Lambda_{pr}(a)\Lambda_{pr}(b)
\le
\log N\bigl(\Lambda_{hpp}(a)+\Lambda_{hpp}(b)\bigr),
\]

because every von Mangoldt value appearing for an integer below `N` is at most `log N`. Summing over the channel and using the reflection identity gives the result.

## 4. Local prime-prime lower bound

Consequently,

\[
\boxed{
Y_{N,r}^{pp}(d)
\ge
Y_{N,r}^{\Lambda}(d)
-
\log N\bigl(H_{N,r}(d)+H_{N,r}(-d)\bigr).
}
\]

## 5. Local Goldbach certificate

If `N` is even and, for some residue channel `d mod r`,

\[
\boxed{
Y_{N,r}^{\Lambda}(d)
>
\log N\bigl(H_{N,r}(d)+H_{N,r}(-d)\bigr),
}
\]

then

\[
Y_{N,r}^{pp}(d)>0.
\]

Hence there exist primes `p,q` such that

\[
p+q=N,
\qquad
p-q\equiv d\pmod r.
\]

This is a sufficient certificate, not a necessary condition.

## 6. Relation to the global bound

Summing over all channels gives

\[
\sum_d H_{N,r}(d)=S_{hpp}(N-1),
\]

so the local theorem implies

\[
E_{hpp}(N)
\le
2\log N\,S_{hpp}(N-1),
\]

recovering the earlier global estimate up to the harmless endpoint convention.

## 7. Scientific ceiling

This theorem does not prove Goldbach for all even `N`. It converts any sufficiently strong lower bound for one local von Mangoldt channel into a prime-prime representation in that same channel. The unresolved analytic task is to obtain such lower bounds uniformly or on useful families of channels.