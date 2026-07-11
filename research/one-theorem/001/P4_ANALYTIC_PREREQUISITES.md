# One-Theorem Program 001 — Analytic Prerequisites for the Contour Shift

This file isolates the two standard analytic inputs used in P3–P5.

## Lemma A — rapid Mellin decay

Let

\[
W\in C_c^\infty(0,\infty)
\]

and

\[
\widehat W(s)=\int_0^\infty W(t)t^{s-1}\,dt.
\]

Then `W-hat` is entire. For every finite real strip `A<=Re(s)<=B` and every integer `N>=0`,

\[
\widehat W(\sigma+i\tau)
\ll_{W,A,B,N}(1+|\tau|)^{-N}.
\]

### Proof

Because the support of `W` is contained in a compact interval `[u,v]` with `0<u<v<infinity`, differentiation under the integral sign is valid for every complex `s`; hence `W-hat` is entire.

Let

\[
\mathcal D=t\frac{d}{dt}.
\]

Integration by parts, with vanishing boundary terms, gives

\[
\int_0^\infty (\mathcal DW)(t)t^{s-1}\,dt
=-s\widehat W(s).
\]

Iterating,

\[
\widehat W(s)
=\frac{(-1)^N}{s^N}
\int_0^\infty (\mathcal D^NW)(t)t^{s-1}\,dt.
\]

The integral on the right is uniformly bounded for `A<=sigma<=B`, because its support is fixed away from zero and infinity. This proves rapid decay for `|s|>=1`; bounded `|s|` is absorbed into the constant.

---

## Lemma B — polynomial vertical growth of fixed-modulus Dirichlet L-functions

Fix a modulus `q`, a Dirichlet character `psi mod q`, and a finite strip

\[
A\le\Re(s)\le B.
\]

After excluding the point `s=1` when `psi` is principal, there exist constants `C,M`, depending on `q,psi,A,B`, such that

\[
|L(s,\psi)|\le C(1+|\Im s|)^M.
\]

The same holds for imprimitive character powers occurring in the target theorem.

### Proof route

1. For `Re(s)>=1+delta`, the absolutely convergent Dirichlet series is bounded.
2. For a primitive inducing character, the completed L-function satisfies its functional equation. Stirling’s formula for the gamma quotient transfers the right-half-plane bound to a polynomial bound in a left half-plane.
3. Phragmén–Lindelöf on the intervening finite strips gives polynomial growth throughout.
4. An imprimitive L-function differs from the primitive one by finitely many Euler factors. On a fixed strip away from the principal pole, these preserve polynomial growth.
5. For the principal character, remove or avoid its simple pole at `1`; the contour proof treats that pole by residues.

This is the standard fixed-conductor vertical-growth consequence of the Dirichlet-L functional equation. No subconvexity or zero-free region is required.

---

## Corollary — contour integrability

Fix the shifted line

\[
\Re(s)=\sigma_0>\frac1{2r+2}.
\]

P2 gives a uniform vertical bound for `H_{r,chi}(s)` on that line. Lemma B gives polynomial growth for

\[
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2.
\]

Lemma A supplies decay faster than any chosen polynomial for `W-hat(s)`. Therefore

\[
\int_{-\infty}^{\infty}
|D_{r,\chi}(\sigma_0+it)\widehat W(\sigma_0+it)|\,dt
<\infty.
\]

The horizontal segments in a rectangular contour tend to zero along a sequence of heights, and in fact uniformly after choosing the Mellin-decay order larger than the polynomial-growth exponent.

Consequently the shifted-line contribution is

\[
O_{q,r,W,\sigma_0}(x^{\sigma_0}).
\]

## Source routing

The final manuscript should cite a standard source for:

- the functional equation and polynomial vertical growth of fixed-conductor Dirichlet L-functions;
- Mellin inversion.

The Central Mind’s Davenport/Overholt/Iwaniec–Kowalski layers contain these prerequisites. The rapid-decay argument is included above so the proof does not depend on a hidden smoothing claim.

## Ceiling

These are classical analytic lemmas. Their use does not constitute a new method or originality claim.
