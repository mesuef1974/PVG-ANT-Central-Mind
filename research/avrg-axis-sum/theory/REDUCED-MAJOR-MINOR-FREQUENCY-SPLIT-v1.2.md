# Reduced Major–Minor Frequency Split

Status: `PROVED-THEOREM-v1.2`

## 1. Setting

Let

\[
q=\frac{r}{\gcd(2,r)}
\]

be the effective period, and let

\[
Z(c)=\sum_{ua\equiv c\pmod q}\Lambda(a)\Lambda(N-a),
\qquad
\widehat Z(k)=\sum_{a=1}^{N-1}\Lambda(a)\Lambda(N-a)e_q(kua).
\]

Then

\[
Z(c)=\frac1q\sum_{k\bmod q}\widehat Z(k)e_q(-kc),
\qquad
\widehat Z(0)=R_\Lambda(N).
\]

Let \(\mathcal M\subseteq\{1,\dots,q-1\}\) be a chosen set of major frequencies and let

\[
\mathcal m=\{1,\dots,q-1\}\setminus\mathcal M.
\]

## 2. Exact split

Define

\[
\Delta_{\mathcal M}(c)
=
\frac1q\sum_{k\in\mathcal M}\widehat Z(k)e_q(-kc),
\]

and

\[
\Delta_{\mathcal m}(c)
=
\frac1q\sum_{k\in\mathcal m}\widehat Z(k)e_q(-kc).
\]

Then exactly

\[
\boxed{
Z(c)=\frac{R_\Lambda(N)}q+\Delta_{\mathcal M}(c)+\Delta_{\mathcal m}(c)
}
\]

for every effective channel \(c\in\mathbb Z/q\mathbb Z\).

## 3. Minor-frequency energy bound

By Cauchy–Schwarz,

\[
\left|\sum_{k\in\mathcal m}\widehat Z(k)e_q(-kc)\right|
\le
\sqrt{|\mathcal m|}
\left(\sum_{k\in\mathcal m}|\widehat Z(k)|^2\right)^{1/2}.
\]

Therefore

\[
\boxed{
|\Delta_{\mathcal m}(c)|
\le
B_{\mathcal m}
:=
\frac{\sqrt{|\mathcal m|}}q
\left(\sum_{k\in\mathcal m}|\widehat Z(k)|^2\right)^{1/2}
}
\]

uniformly in \(c\).

This bound preserves cancellation at the energy level and is never worse than applying Cauchy–Schwarz to the same minor set after first replacing every coefficient by a common maximum.

## 4. Prime-channel certificate

Let

\[
C_{N,r}(c)
=
\log N\bigl(H(c)+H(uN-c)\bigr)
\]

be the local higher-prime-power contamination bound in effective coordinates. Then

\[
Y^{\mathrm{pp}}_{N,r}(c)
\ge
\frac{R_\Lambda(N)}q
+
\Re\Delta_{\mathcal M}(c)
-
B_{\mathcal m}
-
C_{N,r}(c).
\]

Hence

\[
\boxed{
\frac{R_\Lambda(N)}q
+
\Re\Delta_{\mathcal M}(c)
>
B_{\mathcal m}+C_{N,r}(c)
}
\]

is sufficient for a prime-prime representation in channel \(c\).

## 5. Optimal major set for fixed cardinality under the energy bound

Fix an integer \(K\). Among all major sets \(\mathcal M\) with \(|\mathcal M|=K\), the residual energy

\[
\sum_{k\notin\mathcal M,\ k\ne0}|\widehat Z(k)|^2
\]

is minimized by selecting the \(K\) nonzero frequencies with largest magnitudes \(|\widehat Z(k)|\).

Proof: removing the largest squared magnitudes from a finite nonnegative list minimizes the remaining sum.

This is an optimality statement only for the uniform \(L^2\) tail bound. It does not claim that the same set maximizes the number of successful channels, because the major phases \(e_q(-kc)\) also matter.

## 6. Parseval form

By reduced Parseval,

\[
\sum_{k=1}^{q-1}|\widehat Z(k)|^2
=
q\sum_{c\bmod q}\left|Z(c)-\frac{R_\Lambda(N)}q\right|^2.
\]

Thus the minor bound can be computed either spectrally or from channel variance after subtracting the selected major energy.

## 7. Scientific classification

- Exact split: **proved identity**.
- Uniform minor-energy bound: **proved inequality**.
- Top-\(K\) residual-energy optimality: **proved finite optimization statement**.
- Goldbach implication: **conditional sufficient certificate**.
- No global estimate for the minor energy is proved here.
- No Goldbach, RH, GRH, major-arc, or minor-arc theorem is claimed.
