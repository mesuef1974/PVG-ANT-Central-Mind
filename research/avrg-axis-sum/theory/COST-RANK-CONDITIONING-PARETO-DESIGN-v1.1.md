# Cost–Rank–Conditioning Pareto Design — v1.1

Status: `PROVED DEFINITIONS + EXACT FINITE OPTIMIZATION FRAMEWORK`

## 1. Object

For a reduced-period family \(S\subseteq Q\), define the marginal operator

\[
M_{N;S}=\begin{pmatrix}D_{N,q_1}\\ \vdots \\ D_{N,q_s}\end{pmatrix}.
\]

Its design metrics are

\[
C(S)=\sum_{q\in S}c(q),\qquad R_N(S)=\operatorname{rank}M_{N;S},
\]

and, for nonzero rank,

\[
\sigma_{\min}^+(S)=\min\{\sigma>0:\sigma\text{ is a singular value of }M_{N;S}\},
\]

\[
\kappa_2^+(S)=\frac{\sigma_{\max}(M_{N;S})}{\sigma_{\min}^+(M_{N;S})}.
\]

Rank-zero designs are assigned \(\kappa_2^+=+\infty\).

## 2. Dominance

A design \(T\) dominates \(S\) when

\[
C(T)\le C(S),\qquad R_N(T)\ge R_N(S),\qquad \kappa_2^+(T)\le\kappa_2^+(S),
\]

with at least one strict inequality.

The three-objective Pareto frontier is the set of undominated designs.

## 3. Exact finite optimizer

For a finite candidate pool \(Q\), exhaustive enumeration over \(2^{|Q|}\) designs is an exact certificate procedure. For each design it computes:

1. cost;
2. exact numerical matrix rank under a declared tolerance;
3. positive singular spectrum;
4. \(\sigma_{\min}^+\);
5. \(\kappa_2^+\);
6. Pareto dominance.

The procedure is exponential and is not claimed to be scalable.

## 4. Design rule

Minimum-cost full rank and best-conditioned full rank are different optimization problems. A minimum-cost full-rank design may be strongly ill-conditioned. Therefore no design is accepted from rank alone when numerical reconstruction is intended.

## 5. Example

For candidate reduced periods \(Q=\{2,\ldots,12\}\), cost \(c(q)=q\), and \(N=24\):

- minimum-cost full-rank design: \(\{5,9,11\}\), cost \(25\);
- best-conditioned full-rank design in this candidate pool: \(\{7,9,11\}\), cost \(27\).

Thus paying two additional cost units improves stability in the tested pool.

## 6. Scientific classification

- Pareto definitions: `DEFINITION`.
- Exhaustive finite output: `COMPUTATIONAL CERTIFICATE`.
- No universal closed formula for optimal conditioning is claimed.
- No large-scale polynomial optimizer is claimed.
- No Goldbach, RH, GRH, sieve, or prime-distribution consequence is implied.
