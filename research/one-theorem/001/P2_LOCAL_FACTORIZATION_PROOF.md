# One-Theorem Program 001 — P2 Local Factorization Proof

**Target component:** Target Lemma A in `ONE-LEMMA-TARGET-001`  
**Decision:** manual proof complete, pending adversarial review.  
**Classification:** exact lemma for the candidate theorem; originality not assessed here.

## Lemma P2-A — geometric formula and multiplicativity

Fix an integer `r>=1`. For

\[
n=\prod_{p^a\parallel n}p^a,
\]

define

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0),
\qquad I_r(1)=1.
\]

Then `I_r(n)` equals the number of divisors `d|n` satisfying

\[
r\le v_p(d)\le v_p(n)-r
\]

for every `p|n`. In particular, `I_r` is multiplicative.

### Proof

For one coordinate of length `a=v_p(n)`, the admissible integers

\[
r,r+1,\ldots,a-r
\]

number `a-2r+1` when `a>=2r`, and there are none when `a<2r`. Choices at distinct prime coordinates are independent, so the product counts the required divisor points.

If `(m,n)=1`, the active prime coordinates of `m` and `n` are disjoint. Therefore the corresponding coordinate-choice counts multiply, giving

\[
I_r(mn)=I_r(m)I_r(n).
\]

---

## Lemma P2-B — Bell series

For a complex number `y` with `|y|<1`,

\[
\sum_{a\ge0}I_r(p^a)y^a
=
1+\frac{y^{2r}}{(1-y)^2}.
\]

### Proof

Since

\[
I_r(p^a)=
\begin{cases}
1,&a=0,\\
0,&1\le a<2r,\\
a-2r+1,&a\ge2r,
\end{cases}
\]

we have

\[
\begin{aligned}
\sum_{a\ge0}I_r(p^a)y^a
&=1+\sum_{a\ge2r}(a-2r+1)y^a\\
&=1+y^{2r}\sum_{j\ge0}(j+1)y^j\\
&=1+\frac{y^{2r}}{(1-y)^2}.
\end{aligned}
\]

---

## Lemma P2-C — residual local order

Define

\[
h_r(y)=
(1-y^{2r})(1-y^{2r+1})^2
\left(1+\frac{y^{2r}}{(1-y)^2}\right).
\]

For every fixed `r>=1`,

\[
h_r(y)=1+O_r(|y|^{2r+2})
\]

uniformly for `|y|<=1/2`.

### Proof

From the geometric-series derivative,

\[
1+\frac{y^{2r}}{(1-y)^2}
=
1+y^{2r}+2y^{2r+1}+O_r(|y|^{2r+2}).
\]

Also,

\[
(1-y^{2r})(1-y^{2r+1})^2
=
1-y^{2r}-2y^{2r+1}+O_r(|y|^{2r+2}).
\]

Indeed, every omitted monomial has degree at least `2r+2`: the smallest product term is `y^(4r)`, and `4r>=2r+2` for `r>=1`.

Multiplying the two expansions cancels the terms of degrees `2r` and `2r+1`; all remaining nonconstant terms are `O_r(|y|^(2r+2))`.

The constants are uniform on `|y|<=1/2` because the tail

\[
\sum_{j\ge2}(j+1)|y|^{2r+j}
\]

is bounded by a constant depending only on `r` times `|y|^(2r+2)`.

---

## Theorem P2-D — twisted Euler factorization

Let `chi` be a Dirichlet character modulo fixed `q`, extended by zero when `(n,q)>1`. Define the pointwise character power

\[
\chi^k(n)=\chi(n)^k.
\]

For

\[
D_{r,\chi}(s)=\sum_{n\ge1}\frac{I_r(n)\chi(n)}{n^s},
\]

we have, initially for `Re(s)>1/(2r)`,

\[
\boxed{
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
}
\]

where

\[
H_{r,\chi}(s)
=
\prod_p h_r(\chi(p)p^{-s}).
\]

Moreover, the Euler product for `H_{r,chi}` converges absolutely and locally uniformly in

\[
\Re(s)>\frac1{2r+2}.
\]

Consequently, the displayed right-hand side gives a meromorphic continuation of `D_{r,chi}` to that half-plane.

### Proof

Because `I_r` and `chi` are multiplicative, the Dirichlet series has an Euler product in its absolute-convergence region. The Bell series at `p` is, with

\[
y_p=\chi(p)p^{-s},
\]

\[
1+\frac{y_p^{2r}}{(1-y_p)^2}.
\]

For primes `p|q`, `chi(p)=0`, so `y_p=0` and every local factor below equals `1`.

For `p` not dividing `q`, the local Euler factors of the two L-functions are

\[
(1-y_p^{2r})^{-1}
\]

and

\[
(1-y_p^{2r+1})^{-2}.
\]

Therefore, prime by prime,

\[
1+\frac{y_p^{2r}}{(1-y_p)^2}
=
(1-y_p^{2r})^{-1}
(1-y_p^{2r+1})^{-2}
h_r(y_p),
\]

which proves the factorization wherever all products converge absolutely.

The original Dirichlet series converges absolutely for `sigma=Re(s)>1/(2r)`: its local nonconstant contribution is

\[
\sum_{a\ge2r}(a-2r+1)p^{-a\sigma}
\ll_{r,\sigma}p^{-2r\sigma},
\]

and the prime sum converges when `2r sigma>1`.

Now let `K` be a compact subset of

\[
\{s:\Re(s)>1/(2r+2)\}.
\]

Choose `sigma_0>1/(2r+2)` such that `Re(s)>=sigma_0` on `K`. For all sufficiently large primes and every `s in K`,

\[
|y_p|\le p^{-\sigma_0}\le\frac12.
\]

By Lemma P2-C,

\[
|h_r(y_p)-1|
\ll_{r,K}p^{-(2r+2)\sigma_0}.
\]

Since

\[
(2r+2)\sigma_0>1,
\]

the series

\[
\sum_p|h_r(y_p)-1|
\]

converges uniformly on `K`. Hence the Euler product for `H_{r,chi}` converges absolutely and locally uniformly there. Its limit is holomorphic; finite exceptional prime factors are harmless.

Dirichlet L-functions are meromorphic on the complex plane, with a simple pole only when the character is principal and the argument equals `1`. Thus the right-hand side is meromorphic for `Re(s)>1/(2r+2)` and agrees with the original series on the nonempty half-plane `Re(s)>1/(2r)`. It is therefore a meromorphic continuation of `D_{r,chi}`.

---

## Corollary P2-E — possible singular layers

In the half-plane

\[
\Re(s)>\frac1{2r+2},
\]

the only possible singularities of the factorized expression are:

1. a simple pole at
   \[
   s=\frac1{2r}
   \]
   when
   \[
   \chi^{2r}=\chi_0;
   \]
2. a double pole at
   \[
   s=\frac1{2r+1}
   \]
   when
   \[
   \chi^{2r+1}=\chi_0.
   \]

They are distinct. If both character conditions hold, then `chi=chi_0` because `gcd(2r,2r+1)=1`, but the poles still occur at different points.

### Proof

The residual product `H_{r,chi}` is holomorphic in the stated half-plane. A Dirichlet L-function can have a pole only for the principal character at argument `1`. Applying this to the arguments `2rs` and `(2r+1)s` yields the two listed points and orders.

---

## P2 status

```text
Geometric interpretation: proved.
Multiplicativity: proved.
Bell series: proved.
Twisted Euler factorization: proved.
Absolute/local uniform convergence of H: proved.
Possible pole set and orders: proved.
Smoothed residue-class theorem: not yet proved.
Originality: not certified.
```

## Remaining concern for review

The phrase “absolute convergence of the Euler product” is used in the standard sense

\[
\sum_p|h_r(y_p)-1|<\infty.
\]

The product may have zeros from finitely many local factors; nonvanishing is neither required nor claimed.

## Ceiling

This completes a prerequisite lemma of the frozen candidate theorem. It is not yet the theorem’s smoothed asymptotic, and it carries no RH/GRH implication.
