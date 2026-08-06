# Channel-Weighted Phase Tail Bound

Status: PROVED THEOREM — ACTIVE-003-H

## 1. Setup

Let

\[
g=\gcd(2,r),\qquad q=r/g,\qquad u=2/g.
\]

For a real additive-fiber weight \(w_a=w_{N-a}\), define the reduced channel masses

\[
Z(c)=\sum_{ua\equiv c\pmod q}w_a,
\]

and the reduced Fourier coefficients

\[
\widehat Z(k)=\sum_{c\bmod q}Z(c)e_q(kc).
\]

Since \(Z(c)\) is real,

\[
\widehat Z(q-k)=\overline{\widehat Z(k)}.
\]

Let

\[
\mathcal K_q=\{1,\ldots,\lfloor(q-1)/2\rfloor\}.
\]

The zero frequency and, when \(q\) is even, the Nyquist frequency \(q/2\), are treated exactly.

## 2. Paired real expansion

For each \(k\in\mathcal K_q\), write

\[
\widehat Z(k)=|\widehat Z(k)|e^{i\phi_k}.
\]

Then the paired contribution to channel \(c\) is

\[
P_k(c)=\frac{2}{q}\Re\!\left(\widehat Z(k)e_q(-kc)\right)
      =\frac{2|\widehat Z(k)|}{q}
       \cos\!\left(\phi_k-\frac{2\pi kc}{q}\right).
\]

Thus

\[
Z(c)=M_S(c)+T_S(c),
\]

where \(M_S(c)\) contains the zero frequency, the Nyquist frequency when present, and all paired frequencies in a selected set \(S\subseteq\mathcal K_q\), while

\[
T_S(c)=\frac{2}{q}
\sum_{k\in\mathcal K_q\setminus S}
|\widehat Z(k)|
\cos\!\left(\phi_k-\frac{2\pi kc}{q}\right).
\]

## 3. Channel-weighted Cauchy–Schwarz bound

For every channel \(c\),

\[
\boxed{
|T_S(c)|
\le
\frac{2}{q}
\left(
\sum_{k\notin S}|\widehat Z(k)|^2
\right)^{1/2}
\left(
\sum_{k\notin S}
\cos^2\!\left(\phi_k-\frac{2\pi kc}{q}\right)
\right)^{1/2}
}
\]

This follows directly from Cauchy–Schwarz applied to the vectors

\[
\bigl(|\widehat Z(k)|\bigr)_{k\notin S}
\quad\text{and}\quad
\left(
\cos\!\left(\phi_k-\frac{2\pi kc}{q}\right)
\right)_{k\notin S}.
\]

Define this bound by \(B^{\mathrm{phase}}_S(c)\).

## 4. Comparison with the previous uniform tail bound

The previous paired-energy bound was

\[
B^{\mathrm{unif}}_S
=
\frac{2}{q}
\sqrt{|\mathcal K_q\setminus S|}
\left(
\sum_{k\notin S}|\widehat Z(k)|^2
\right)^{1/2}.
\]

Since \(\cos^2\theta\le1\),

\[
\boxed{
B^{\mathrm{phase}}_S(c)
\le
B^{\mathrm{unif}}_S
}
\]

for every channel \(c\). Hence the channel-weighted bound can never be worse and is strictly better whenever the remaining phase vector is not aligned with the all-ones worst case.

## 5. Prime-channel certificate

For the von Mangoldt weight, let \(C_{N,r}(c)\) denote the local higher-prime-power contamination bound. Then

\[
Y^{\mathrm{pp}}_{N,r}(c)
\ge
M_S(c)-B^{\mathrm{phase}}_S(c)-C_{N,r}(c).
\]

Therefore

\[
\boxed{
M_S(c)>B^{\mathrm{phase}}_S(c)+C_{N,r}(c)
}
\]

is sufficient to certify a prime-prime representation in channel \(c\).

## 6. Scientific classification

- paired real expansion: proved identity;
- channel-weighted tail bound: proved theorem;
- domination of the uniform bound: proved theorem;
- numerical certificate gains: computation;
- asymptotic Goldbach consequence: not claimed;
- RH/GRH progress: none.
