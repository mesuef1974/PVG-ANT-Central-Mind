# Channel-Paired Frequency Energy Selection — v1.2

Status: PROVED THEOREM / COMPUTATIONAL STRATEGY

## Setup

Let
\[
q=\frac r{\gcd(2,r)},\qquad u=\frac2{\gcd(2,r)},
\]
and let
\[
Z(c)=\sum_{ua\equiv c\,(\bmod q)}\Lambda(a)\Lambda(N-a).
\]
Define
\[
\widehat Z(k)=\sum_{c\bmod q}Z(c)e_q(kc).
\]
Because the fiber weight is real,
\[
\widehat Z(q-k)=\overline{\widehat Z(k)}.
\]

## Paired real decomposition

For
\[
\mathcal K_q=\{1,\ldots,\lfloor(q-1)/2\rfloor\},
\]
set
\[
P_k(c)=\frac2q\Re\bigl(\widehat Z(k)e_q(-kc)\bigr).
\]
If q is even, define the self-conjugate Nyquist term
\[
P_{q/2}(c)=\frac1q\widehat Z(q/2)(-1)^c.
\]
Then
\[
Z(c)=\frac{R_\Lambda(N)}q+P_{q/2}(c)+\sum_{k\in\mathcal K_q}P_k(c),
\]
with the Nyquist term omitted when q is odd.

Equivalently, if
\[
\widehat Z(k)=|\widehat Z(k)|e^{i\phi_k},
\]
then
\[
P_k(c)=\frac{2|\widehat Z(k)|}{q}
\cos\!\left(\phi_k-\frac{2\pi kc}{q}\right).
\]
Thus every conjugate pair becomes one real channel-dependent cosine contribution.

## Selected pairs and tail bound

For a selected set S subset of \(\mathcal K_q\), write
\[
Z(c)=M_S(c)+T_S(c),
\]
where
\[
M_S(c)=\frac{R_\Lambda(N)}q+P_{q/2}(c)+\sum_{k\in S}P_k(c)
\]
and
\[
T_S(c)=\sum_{k\in\mathcal K_q\setminus S}P_k(c).
\]
Then Cauchy-Schwarz gives
\[
|T_S(c)|\le
\frac2q\sqrt{|\mathcal K_q\setminus S|}
\left(\sum_{k\in\mathcal K_q\setminus S}|\widehat Z(k)|^2\right)^{1/2}.
\]
Call the right-hand side \(B_S\).

If \(C_{N,r}(c)\) is the local higher-prime-power contamination bound, then
\[
M_S(c)-B_S>C_{N,r}(c)
\]
implies positive prime-prime mass in channel c.

## Energy-optimal K-pair selection

For fixed K, the tail bound \(B_S\) is minimized exactly by choosing the K representatives with largest values of
\[
|\widehat Z(k)|^2.
\]
This follows because the cardinality factor is fixed and minimizing the remaining energy is equivalent to maximizing the removed energy.

This is an exact optimality statement for the declared uniform L2 tail bound. It is not a claim that the same set maximizes the number of certified channels under every possible channel-dependent bound.

## Negative-result correction

Selecting the pairs whose instantaneous contributions \(P_k(c)\) are most negative is not generally optimal. It can leave high-energy frequencies in the tail and therefore enlarge \(B_S\). The numerical verifier retains this failed heuristic as a comparison rather than silently discarding it.

## Scientific ceiling

This theorem is finite Fourier analysis and certificate design. It does not provide a new analytic estimate for \(\widehat Z(k)\), and it does not prove Goldbach.