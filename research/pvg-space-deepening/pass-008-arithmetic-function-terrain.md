# PASS-008 — Arithmetic-Function Terrain on PVG Levels

**Program:** `PVG-INVERSE-GEOMETRY-001`  
**Status:** exact local identities; no asymptotic or originality claim

Let

\[
N=\prod_r r^{a_r}
\]

and perform one horizontal transfer from prime axis \(p\) to prime axis \(q\):

\[
N'=N\frac qp,
\qquad a_p>0.
\]

Equivalently,

\[
a_p' = a_p-1,\qquad a_q'=a_q+1.
\]

This preserves total valuation mass:

\[
\Omega(N')=\Omega(N).
\]

The purpose of this pass is to treat arithmetic functions as scalar fields on a fixed PVG level and to compute their exact edge gradients.

---

## 1. Four transfer classes

Write \(a=a_p\) and \(b=a_q\) before the move.

1. **Interior transfer:** \(a>1,b>0\). Support is unchanged.
2. **Boundary contraction:** \(a=1,b>0\). Axis \(p\) disappears and \(\omega\) drops by one.
3. **Boundary expansion:** \(a>1,b=0\). Axis \(q\) appears and \(\omega\) rises by one.
4. **Support swap:** \(a=1,b=0\). Axis \(p\) is replaced by \(q\), so \(\omega\) is unchanged.

Thus the same horizontal root-lattice move can be interior, boundary-losing, boundary-gaining, or support-swapping depending on the point.

---

## 2. Functions constant on every fixed-\(\Omega\) level

The Liouville function satisfies

\[
\lambda(N)=(-1)^{\Omega(N)}.
\]

Therefore every horizontal edge obeys

\[
\boxed{\lambda(N')=\lambda(N).}
\]

This makes \(\lambda\) a shell-constant field: it alternates only when moving vertically between consecutive \(\Omega\)-levels.

The function \(\Omega\) itself is also constant on every horizontal level.

---

## 3. Arithmetic size field

The ordinary integer value changes by

\[
\boxed{\frac{N'}N=\frac qp.}
\]

Hence

\[
\log N'-\log N=\log q-\log p.
\]

The log-size field has constant directional gradient on every edge class \(p\to q\), independent of the base point.

---

## 4. Divisor-count terrain

Since

\[
\tau(N)=\prod_r(a_r+1),
\]

the exact edge ratio is

\[
\boxed{
\frac{\tau(N')}{\tau(N)}
=
\frac{a}{a+1}\frac{b+2}{b+1}.
}
\]

Therefore

\[
\tau(N')>\tau(N)
\iff
\frac{b+2}{b+1}>\frac{a+1}{a}
\iff a>b+1.
\]

Similarly,

\[
\tau(N')=\tau(N)\iff a=b+1,
\]

and

\[
\tau(N')<\tau(N)\iff a<b+1.
\]

So a unit transfer increases \(\tau\) precisely when it moves valuation mass from a sufficiently larger exponent to a smaller exponent. This gives an exact balancing principle:

\[
\boxed{\tau\text{ rises when the exponent vector becomes more balanced.}}
\]

On a fixed support and fixed \(\Omega\), repeated balancing leads toward the maximizers of \(\tau\), while concentration near vertices lowers \(\tau\).

---

## 5. Sum-of-divisors terrain

For

\[
\sigma(r^c)=1+r+\cdots+r^c=\frac{r^{c+1}-1}{r-1},
\]
we obtain

\[
\boxed{
\frac{\sigma(N')}{\sigma(N)}
=
\frac{p^a-1}{p^{a+1}-1}
\frac{q^{b+2}-1}{q^{b+1}-1}.
}
\]

Unlike \(\tau\), this field depends both on exponent shape and on the labels of the prime axes. Two combinatorially identical moves on different prime pairs need not have the same \(\sigma\)-gradient.

This makes \(\sigma\) a genuinely weighted terrain on the abstract simplex.

---

## 6. Euler-totient terrain

The ratio is piecewise because support may change.

### Interior transfer: \(a>1,b>0\)

\[
\boxed{\frac{\varphi(N')}{\varphi(N)}=\frac qp.}
\]

### Boundary contraction: \(a=1,b>0\)

\[
\boxed{\frac{\varphi(N')}{\varphi(N)}=\frac q{p-1}.}
\]

### Boundary expansion: \(a>1,b=0\)

\[
\boxed{\frac{\varphi(N')}{\varphi(N)}=\frac{q-1}{p}.}
\]

### Support swap: \(a=1,b=0\)

\[
\boxed{\frac{\varphi(N')}{\varphi(N)}=\frac{q-1}{p-1}.}
\]

Thus \(\varphi\) detects the support boundary: the interior formula is a pure axis ratio, while boundary crossing replaces a prime by its reduced factor \(p-1\) or \(q-1\).

---

## 7. Möbius terrain

\[
\mu(N)=0
\]
whenever some exponent exceeds one. Therefore \(\mu\) is concentrated on the squarefree skeleton.

A horizontal transfer can:

- remain between nonsquarefree points: \(0\to0\);
- land on the squarefree skeleton: \(0\to\pm1\);
- leave the squarefree skeleton: \(\pm1\to0\);
- move within it by a support swap: \(\pm1\to\pm1\).

Hence \(\mu\) is not a smooth field on the simplex. It is a boundary-sensitive field supported on the Boolean squarefree layer.

---

## 8. Radical and support dimension

The radical changes according to the four transfer classes:

- interior: unchanged;
- contraction: divided by \(p\);
- expansion: multiplied by \(q\);
- support swap: multiplied by \(q/p\).

Likewise,

\[
\Delta\omega\in\{-1,0,+1\}.
\]

This separates two notions that ordinary size hides:

- redistribution of multiplicity inside a fixed face;
- actual movement between support faces.

---

## 9. Example: \(60\to90\)

\[
60=2^2\cdot3\cdot5,
\qquad
90=2\cdot3^2\cdot5.
\]

This is the move \(2\to3\) with \(a=2,b=1\).

\[
\frac{90}{60}=\frac32.
\]

For \(\tau\):

\[
\frac{\tau(90)}{\tau(60)}
=
\frac23\frac32=1.
\]

Indeed:

\[
\tau(60)=12=\tau(90).
\]

The exponent vectors \((2,1,1)\) and \((1,2,1)\) are permutations, so the unlabeled shape terrain is unchanged even though the labeled arithmetic point moves.

---

## 10. Central interpretation

Arithmetic functions split into geometric classes:

1. **Shell fields:** depend only on \(\Omega\), such as \(\lambda\).
2. **Shape fields:** depend only on the exponent partition, such as \(\tau\).
3. **Label-weighted fields:** depend on exponents and prime names, such as \(\sigma\) and \(\varphi\).
4. **Skeleton fields:** supported on special strata, such as \(\mu\) on squarefree points.
5. **Support fields:** detect entry to or exit from faces, such as \(\omega\) and `rad`.

This classification is more important than any single formula: it tells us which arithmetic observables live on levels, shapes, labels, boundaries, or support strata.

---

## 11. Scientific boundary

All formulas above are elementary exact identities recast in PVG language. This pass establishes a reusable local-gradient grammar and executable verification. It does not claim new asymptotic estimates, algorithmic speedups, originality, or progress on a major conjecture.
