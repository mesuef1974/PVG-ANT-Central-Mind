# Effective-Period Reduced Fourier Theorem

Status: `PROVED-v1.2`

## 1. Setting

Fix integers `N >= 2` and `r >= 1`. Put

\[
g=\gcd(2,r),\qquad q=\frac r g,\qquad u=\frac2g.
\]

Then `g` is either `1` or `2`, and

\[
\gcd(u,q)=1.
\]

For an arbitrary weight vector `w=(w_a)_{1\le a<N}`, define the full difference-channel observable

\[
Y_{N,r}(d)=\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}w_a,
\qquad d\in\mathbb Z/r\mathbb Z.
\]

The results apply in particular to

\[
w_a=\Lambda(a)\Lambda(N-a).
\]

## 2. Admissible channel coset

The congruence

\[
2a-N\equiv d\pmod r
\]

can hold only when

\[
d+N\equiv0\pmod g.
\]

Thus the support of `Y_{N,r}` is contained in the coset

\[
\mathcal C_{N,r}=\{d\bmod r:d\equiv-N\pmod g\},
\]

which has exactly `q=r/g` elements.

For each admissible `d`, define its reduced coordinate

\[
c(d)=\frac{d+N}{g}\pmod q.
\]

This is a bijection

\[
\mathcal C_{N,r}\longrightarrow\mathbb Z/q\mathbb Z.
\]

## 3. Reduced channel observable

Define

\[
Z_{N,q}(c)
=
\sum_{\substack{1\le a<N\\ua\equiv c\pmod q}}w_a,
\qquad c\in\mathbb Z/q\mathbb Z.
\]

Since `u` is invertible modulo `q`, this is simply the aggregation of `w_a` by the effective residue class of `a`.

### Theorem 3.1 — exact channel reduction

For every `d mod r`,

\[
Y_{N,r}(d)
=
\begin{cases}
Z_{N,q}(c(d)),&d\in\mathcal C_{N,r},\\
0,&d\notin\mathcal C_{N,r}.
\end{cases}
\]

### Proof

If `d` is admissible, write `d+N=gc` modulo `r=gq`. Then

\[
2a-N\equiv d\pmod r
\iff
2a\equiv d+N\pmod{gq}
\iff
gua\equiv gc\pmod{gq}
\iff
ua\equiv c\pmod q.
\]

If `d` is not admissible, the original congruence has no solution. ∎

## 4. Reduced Fourier transform

Define

\[
\widehat Z_{N,q}(k)
=
\sum_{c\bmod q}Z_{N,q}(c)e_q(kc)
=
\sum_{a=1}^{N-1}w_a e_q(kua).
\]

Fourier inversion gives

\[
\boxed{
Z_{N,q}(c)
=
\frac1q\sum_{k\bmod q}\widehat Z_{N,q}(k)e_q(-kc)
}.
\]

The zero frequency is

\[
\widehat Z_{N,q}(0)=\sum_{a=1}^{N-1}w_a.
\]

For the von Mangoldt weight this equals `R_Λ(N)`.

Hence every admissible channel has the exact decomposition

\[
\boxed{
Y_{N,r}(d)
=
\frac{R_\Lambda(N)}q
+
\Delta^{\mathrm{red}}_{N,r}(d)
}
\]

with

\[
\Delta^{\mathrm{red}}_{N,r}(d)
=
\frac1q\sum_{k=1}^{q-1}
\widehat Z_{N,q}(k)e_q(-k c(d)).
\]

This is the effective-period decomposition.

## 5. Relation to the length-r Fourier transform

Define the full transform

\[
\widehat Y_{N,r}(h)
=
\sum_{d\bmod r}Y_{N,r}(d)e_r(hd).
\]

Then

\[
\boxed{
\widehat Y_{N,r}(h)
=
e_r(-hN)\widehat Z_{N,q}(h\bmod q)
}.
\]

Therefore the `r` full-frequency coefficients contain only `q` independent coefficients. They satisfy

\[
\widehat Y_{N,r}(h+q)
=
e^{-2\pi iN/g}\widehat Y_{N,r}(h).
\]

For odd `r`, `g=1` and `q=r`, so no reduction occurs. For even `r`, `g=2`, `q=r/2`, and

\[
\widehat Y_{N,r}(h+q)=(-1)^N\widehat Y_{N,r}(h).
\]

Thus the second half of the full spectrum is completely determined by the first half.

## 6. Correct effective mean

The identity

\[
Y_{N,r}(d)=\frac{R_\Lambda(N)}r+\Delta_{N,r}(d)
\]

on all `r` formal channels remains algebraically correct. However, for even `r`, half of those channels are structurally impossible and equal zero. On the actually realizable channel coset, the natural mean is

\[
\boxed{
\frac{R_\Lambda(N)}q
}
\]

rather than `R_Λ(N)/r`.

This distinction matters in any positivity certificate.

## 7. Reduced local prime certificate

Let

\[
C_{N,r}(d)
=
\log N\bigl(H_{N,r}(d)+H_{N,r}(-d)\bigr)
\]

be the local higher-prime-power contamination bound from ACTIVE-003-C.

For every admissible channel,

\[
Y^{\mathrm{pp}}_{N,r}(d)
\ge
\frac{R_\Lambda(N)}q
+
\Delta^{\mathrm{red}}_{N,r}(d)
-
C_{N,r}(d).
\]

Consequently, if

\[
\boxed{
\frac{R_\Lambda(N)}q
+
\Delta^{\mathrm{red}}_{N,r}(d)
>
C_{N,r}(d)
}
\]

then there are primes `p,q'` such that

\[
p+q'=N,
\qquad
p-q'\equiv d\pmod r.
\]

A conservative sufficient condition is

\[
\boxed{
\frac{R_\Lambda(N)}q
>
\frac1q\sum_{k=1}^{q-1}|\widehat Z_{N,q}(k)|
+
C_{N,r}(d)
}.
\]

This reduced bound never repeats dependent frequencies.

## 8. Parseval on the effective period

The exact energy identity is

\[
\sum_{c\bmod q}
\left|Z_{N,q}(c)-\frac{R_\Lambda(N)}q\right|^2
=
\frac1q\sum_{k=1}^{q-1}|\widehat Z_{N,q}(k)|^2.
\]

This is the correct variance identity over realizable channels.

## 9. Classification

- Effective support coset: **proved theorem**.
- Exact reduction `Y ↔ Z`: **proved theorem**.
- Full/reduced Fourier relation: **proved theorem**.
- Effective mean `R_Λ(N)/q`: **proved theorem**.
- Reduced positivity certificate: **proved conditional certificate**.
- Any uniform analytic bound on nonzero reduced frequencies: **open analytical input**.
- No Goldbach, RH, or GRH progress is claimed from the finite identities alone.
