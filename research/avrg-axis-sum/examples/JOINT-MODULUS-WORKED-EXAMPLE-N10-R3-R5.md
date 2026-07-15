# Joint-Modulus Worked Example: \(N=10\), moduli \((3,5)\)

Status: hand-checkable evidence under `THEORY-FREEZE-v1.0`

Purpose: verify the joint-modulus rank theorem, the joint reconstruction criterion, and the conditioning statement without adding any new definition or theorem.

## 1. Setup

For \(N=10\), the fiber weight space is

\[
V_{10}=\mathbb C^9,
\qquad
w=(w_1,\dots,w_9).
\]

Choose the modulus family

\[
\mathbf r=(3,5).
\]

Its least common multiple is

\[
L=\operatorname{lcm}(3,5)=15.
\]

Because \(L\) is odd,

\[
\frac{L}{\gcd(2,L)}=15.
\]

Therefore the joint-modulus rank theorem predicts

\[
\operatorname{rank}J_{10;(3,5)}
=
\min(9,15)
=
9.
\]

Hence the joint operator is injective.

## 2. Why the individual channels are insufficient

For modulus \(3\),

\[
\operatorname{rank}D_{10,3}
=
\min(9,3)
=
3.
\]

For modulus \(5\),

\[
\operatorname{rank}D_{10,5}
=
\min(9,5)
=
5.
\]

Thus neither individual operator is injective.

This example therefore tests the genuinely joint statement: two incomplete residue observations can become complete when their full coupled signature is retained.

## 3. Joint residue signatures

For each \(a=1,\dots,9\), define

\[
\sigma(a)
=
\bigl(2a-10\pmod 3,\;2a-10\pmod 5\bigr).
\]

The signatures are:

| \(a\) | \(2a-10\) | modulo \(3\) | modulo \(5\) | joint signature \(\sigma(a)\) |
|---:|---:|---:|---:|---|
| 1 | \(-8\) | 1 | 2 | \((1,2)\) |
| 2 | \(-6\) | 0 | 4 | \((0,4)\) |
| 3 | \(-4\) | 2 | 1 | \((2,1)\) |
| 4 | \(-2\) | 1 | 3 | \((1,3)\) |
| 5 | \(0\) | 0 | 0 | \((0,0)\) |
| 6 | \(2\) | 2 | 2 | \((2,2)\) |
| 7 | \(4\) | 1 | 4 | \((1,4)\) |
| 8 | \(6\) | 0 | 1 | \((0,1)\) |
| 9 | \(8\) | 2 | 3 | \((2,3)\) |

All nine joint signatures are distinct.

Therefore every column of the joint-signature matrix occupies a different row, and

\[
\operatorname{rank}J_{10;(3,5)}=9.
\]

## 4. Equivalence with a single modulus \(15\)

By the Chinese remainder theorem, each compatible pair

\[
(d_3,d_5)\in\mathbb Z/3\mathbb Z\times\mathbb Z/5\mathbb Z
\]

corresponds to a unique residue modulo \(15\).

The difference residues modulo \(15\) are:

| \(a\) | \(2a-10\pmod{15}\) |
|---:|---:|
| 1 | 7 |
| 2 | 9 |
| 3 | 11 |
| 4 | 13 |
| 5 | 0 |
| 6 | 2 |
| 7 | 4 |
| 8 | 6 |
| 9 | 8 |

They are again all distinct. Thus the joint operator is, up to relabeling of its rows, exactly the same incidence operator as \(D_{10,15}\).

This directly illustrates

\[
\operatorname{rank}J_{N;\mathbf r}
=
\operatorname{rank}D_{N,L}.
\]

## 5. Explicit reconstruction

Let

\[
y=J_{10;(3,5)}w.
\]

Since every signature occurs at most once,

\[
\begin{aligned}
w_1&=y_{(1,2)},&
w_2&=y_{(0,4)},&
w_3&=y_{(2,1)},\\
w_4&=y_{(1,3)},&
w_5&=y_{(0,0)},&
w_6&=y_{(2,2)},\\
w_7&=y_{(1,4)},&
w_8&=y_{(0,1)},&
w_9&=y_{(2,3)}.
\end{aligned}
\]

Therefore

\[
J_{10;(3,5)}w=0
\quad\Longrightarrow\quad
w=0.
\]

This verifies the joint reconstruction criterion in this case.

## 6. Conditioning

Delete the unused signature rows and order the nine used rows as

\[
\sigma(1),\sigma(2),\dots,\sigma(9).
\]

The resulting matrix is exactly the \(9\times9\) identity matrix. Consequently all singular values are equal to \(1\), and

\[
\kappa_2\bigl(J_{10;(3,5)}\bigr)=1.
\]

This verifies the joint-modulus conditioning theorem in the injective case.

## 7. Joint operator versus marginal stack

The joint operator records the coupled pair

\[
(d_3,d_5).
\]

The marginal stack

\[
M_{10;(3,5)}
=
\begin{pmatrix}
D_{10,3}\\
D_{10,5}
\end{pmatrix}
\]

records the two channel totals separately and does not label which modulus-3 residue is paired with which modulus-5 residue inside an individual fiber contribution.

No rank claim about the marginal stack is made here. This distinction is included only to prevent replacing \(J_{10;(3,5)}\) by \(M_{10;(3,5)}\).

## 8. Checklist

- T6, joint-modulus rank theorem: verified with rank \(9\).
- C2, joint reconstruction criterion: verified explicitly.
- T7, injective conditioning theorem: verified with all singular values equal to \(1\).
- Neither \(D_{10,3}\) nor \(D_{10,5}\) is injective.
- The full coupled signature is equivalent to the residue modulo \(15\).
- No statement about Goldbach, asymptotics, or the marginal-rank open problem is introduced.
