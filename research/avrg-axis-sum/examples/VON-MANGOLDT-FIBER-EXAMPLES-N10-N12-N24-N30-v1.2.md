# Von Mangoldt Additive-Fiber Examples — N=10,12,24,30

Status: `NUMERICAL EXAMPLES / EXACT FINITE EVALUATION`

Define

\[
R_\Lambda(N)=\sum_{a=1}^{N-1}\Lambda(a)\Lambda(N-a)
\]

and decompose

\[
R_\Lambda(N)=R_{\mathrm{pp}}(N)+2R_{\mathrm{ph}}(N)+R_{\mathrm{hh}}(N),
\]

where `pp` means prime-prime, `ph` means prime-higher-prime-power, and `hh` means higher-prime-power/higher-prime-power.

## N=10

Nonzero pairs:

\[
(2,8),(3,7),(5,5),(7,3),(8,2).
\]

The pair `(2,8)` and its reflection are prime/higher-prime-power terms.

\[
R_{\mathrm{pp}}(10)=6.865891998772556,
\]

\[
R_{\mathrm{ph}}(10)=0.4804530139182014,
\qquad
R_{\mathrm{hh}}(10)=0,
\]

so

\[
R_\Lambda(10)=7.826798026608959.
\]

Higher-prime-power contamination:

\[
R_\Lambda(10)-R_{\mathrm{pp}}(10)
=0.9609060278364028.
\]

## N=12

Nonzero pairs:

\[
(3,9),(4,8),(5,7),(7,5),(8,4),(9,3).
\]

Here `(5,7)` and `(7,5)` are prime-prime; `(3,9)` and `(9,3)` are mixed; `(4,8)` and `(8,4)` are higher-prime-power pairs.

\[
R_{\mathrm{pp}}(12)=6.263643136159825,
\]

\[
R_{\mathrm{ph}}(12)=1.206948960812582,
\]

\[
R_{\mathrm{hh}}(12)=0.9609060278364028,
\]

and

\[
R_\Lambda(12)=9.638447085621392.
\]

## N=24

Nonzero pairs:

\[
(5,19),(7,17),(8,16),(11,13),(13,11),(16,8),(17,7),(19,5).
\]

All pairs except `(8,16)` and `(16,8)` are prime-prime.

\[
R_{\mathrm{pp}}(24)=32.8051005275628,
\]

\[
R_{\mathrm{ph}}(24)=0,
\qquad
R_{\mathrm{hh}}(24)=0.9609060278364028,
\]

so

\[
R_\Lambda(24)=33.7660065553992.
\]

## N=30

Nonzero pairs:

\[
(3,27),(5,25),(7,23),(11,19),(13,17),
(17,13),(19,11),(23,7),(25,5),(27,3).
\]

The pairs involving `25` or `27` are mixed prime/higher-prime-power terms. The remaining six are prime-prime.

\[
R_{\mathrm{pp}}(30)=40.85779014531134,
\]

\[
R_{\mathrm{ph}}(30)=3.7972393547928167,
\qquad
R_{\mathrm{hh}}(30)=0,
\]

and

\[
R_\Lambda(30)=48.45226885489697.
\]

## Channel example: N=24, r=3

The difference-channel coordinates are

\[
Y_{24,3}(0)=0,
\]

\[
Y_{24,3}(1)=Y_{24,3}(2)=16.8830032776996.
\]

Thus

\[
Y_{24,3}(0)+Y_{24,3}(1)+Y_{24,3}(2)
=33.7660065553992
=R_\Lambda(24),
\]

and the reflection law appears as

\[
Y_{24,3}(1)=Y_{24,3}(-1)=Y_{24,3}(2).
\]

## Interpretation

These examples show that positivity of `R_Lambda(N)` is not identical to a pure prime-prime Goldbach certificate: prime powers can contribute. A valid Goldbach-facing use of the observable must either isolate `R_pp(N)` directly or control and subtract the higher-prime-power terms.
