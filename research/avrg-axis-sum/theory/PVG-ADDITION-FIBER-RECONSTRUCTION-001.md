# PVG Addition-Fiber Reconstruction 001

## Status

- Layer: exact finite reconstruction theory.
- Scope: one positive addition fiber \(\mathcal G_N\) with \(N\ge2\).
- Classification: exact definitions and elementary theorems unless explicitly marked as a research question.
- Scientific ceiling: no Goldbach proof, no asymptotic estimate, and no RH/GRH progress.

## 1. Fiber weight space

For \(1\le a\le N-1\), write

\[
P_a=(\nu(a),\nu(N-a))\in\mathcal G_N.
\]

The no-loss valuation map makes the points \(P_a\) pairwise distinct. Define

\[
V_N=\{w:\mathcal G_N\to\mathbb C\}\cong\mathbb C^{N-1},
\qquad
w_a=w(P_a).
\]

All additive observables considered below are linear maps on \(V_N\).

## 2. Exact difference coordinates

Define the exact difference label

\[
d_N(a)=a-(N-a)=2a-N.
\]

The set of realized differences is

\[
D_N=\{2-N,4-N,\ldots,N-4,N-2\}.
\]

### Theorem 2.1 — Exact-difference injectivity

The map

\[
d_N:\{1,\ldots,N-1\}\to D_N
\]

is bijective.

### Proof

If \(d_N(a)=d_N(b)\), then \(2a-N=2b-N\), hence \(a=b\). Surjectivity onto \(D_N\) holds by definition. \(\square\)

For \(d\in D_N\), define the exact difference channel

\[
M_{N,w}(d)=\sum_{\substack{1\le a\le N-1\\2a-N=d}}w_a.
\]

### Corollary 2.2 — Trivial exact reconstruction

For every \(a\in\{1,\ldots,N-1\}\),

\[
w_a=M_{N,w}(2a-N).
\]

Therefore the exact-difference channel operator

\[
\mathcal D_N:V_N\to\mathbb C^{D_N},
\qquad
w\mapsto(M_{N,w}(d))_{d\in D_N},
\]

is an isomorphism and

\[
\operatorname{rank}(\mathcal D_N)=N-1,
\qquad
\ker(\mathcal D_N)=\{0\}.
\]

This establishes a complete reconstruction theorem. It also shows that the nontrivial research problem is not whether all exact channels recover the fiber weight, but how much compression is possible using periodic, character, orbit, or symmetry observables.

## 3. Periodic difference channels

For a modulus \(r\ge1\), define

\[
M_{N,r,w}(c)
=
\sum_{\substack{1\le a\le N-1\\2a-N\equiv c\pmod r}}w_a,
\qquad c\in\mathbb Z/r\mathbb Z.
\]

Let

\[
\mathcal D_{N,r}:V_N\to\mathbb C^r
\]

be the corresponding periodic channel operator.

### Theorem 3.1 — Odd-modulus complete reconstruction

If \(r\) is odd and \(r\ge N\), then \(a\mapsto2a-N\pmod r\) is injective on \(1\le a\le N-1\). Consequently,

\[
\operatorname{rank}(\mathcal D_{N,r})=N-1,
\qquad
\ker(\mathcal D_{N,r})=\{0\}.
\]

### Proof

Suppose

\[
2a-N\equiv2b-N\pmod r.
\]

Because \(r\) is odd, \(2\) is invertible modulo \(r\), so \(a\equiv b\pmod r\). Since \(1\le a,b\le N-1<r\), it follows that \(a=b\). Each occupied residue channel therefore contains one coordinate \(w_a\). \(\square\)

### Remark 3.2 — Why \(r>N\) alone was insufficient without parity

For even \(r\), multiplication by \(2\) is not invertible modulo \(r\). Collisions can occur when

\[
a-b\equiv r/2\pmod r.
\]

Thus an oddness or a stronger collision-free condition is required.

### Theorem 3.3 — General collision criterion

The operator \(\mathcal D_{N,r}\) is injective if and only if no distinct \(a,b\in\{1,\ldots,N-1\}\) satisfy

\[
r\mid2(a-b).
\]

Equivalently,

\[
\frac r{\gcd(r,2)}>N-2
\]

is a sufficient and necessary numerical condition for injectivity on the full interval.

### Proof

A collision occurs exactly when \(2a-N\equiv2b-N\pmod r\), i.e. \(r\mid2(a-b)\). Dividing by \(\gcd(r,2)\), this is equivalent to

\[
\frac r{\gcd(r,2)}\mid(a-b).
\]

The nonzero differences \(a-b\) have absolute value at most \(N-2\). Hence no collision exists exactly when the least positive possible multiple \(r/\gcd(r,2)\) exceeds \(N-2\). \(\square\)

## 4. Finite Fourier reconstruction

Define the discrete Fourier transform of the periodic channels:

\[
\widehat M_{N,r,w}(k)
=
\sum_{c\bmod r}
M_{N,r,w}(c)e\!\left(\frac{kc}{r}\right),
\qquad k\in\mathbb Z/r\mathbb Z.
\]

Then

\[
\widehat M_{N,r,w}(k)
=
\sum_{a=1}^{N-1}
w_a e\!\left(\frac{k(2a-N)}r\right).
\]

By finite Fourier inversion,

\[
M_{N,r,w}(c)
=
\frac1r\sum_{k\bmod r}
\widehat M_{N,r,w}(k)e\!\left(-\frac{kc}{r}\right).
\]

### Theorem 4.1 — Fourier-complete reconstruction

Whenever \(\mathcal D_{N,r}\) is injective, the full frequency vector

\[
\bigl(\widehat M_{N,r,w}(k)\bigr)_{k\bmod r}
\]

recovers \(w\) uniquely.

Thus, for odd \(r\ge N\), the \(r\) difference frequencies form an overcomplete measurement system of rank \(N-1\).

## 5. Direct additive-frequency reconstruction

Define

\[
F_{N,r,w}(k)
=
\sum_{a=1}^{N-1}w_a e\!\left(\frac{ka}{r}\right).
\]

### Theorem 5.1 — Interval Fourier reconstruction

If \(r\ge N\), then the full vector \((F_{N,r,w}(k))_{k\bmod r}\) recovers \(w\) uniquely.

### Proof

Extend \(w\) to a function on \(\mathbb Z/r\mathbb Z\) by zero outside \(\{1,\ldots,N-1\}\). The displayed measurements are its complete discrete Fourier transform. Fourier inversion recovers the extension and therefore all \(w_a\). \(\square\)

For odd \(r\), the difference-frequency and additive-frequency systems differ only by a fixed phase and a permutation of frequencies:

\[
\widehat M_{N,r,w}(k)
=
e\!\left(-\frac{kN}{r}\right)F_{N,r,w}(2k).
\]

## 6. Symmetry-reduced reconstruction

Let \(\sigma(a)=N-a\). Decompose

\[
w_a^+=\frac{w_a+w_{N-a}}2,
\qquad
w_a^-=\frac{w_a-w_{N-a}}2.
\]

Then

\[
w=w^++w^-,
\qquad
w_{N-a}^+=w_a^+,
\qquad
w_{N-a}^-=-w_a^-.
\]

The exact difference coordinates satisfy

\[
d_N(N-a)=-d_N(a).
\]

Therefore symmetric weights correspond to even channel data,

\[
M_{N,w^+}(-d)=M_{N,w^+}(d),
\]

and antisymmetric weights correspond to odd channel data,

\[
M_{N,w^-}(-d)=-M_{N,w^-}(d).
\]

This gives exact cosine/sine splitting of the Fourier measurements. The symmetric subspace has dimension \(\lfloor N/2\rfloor\), and the antisymmetric subspace has dimension \(\lfloor(N-1)/2\rfloor\).

## 7. Character observables and their limitation

For a Dirichlet character \(\chi\pmod r\), define

\[
T_{N,r,\chi}(w)=\sum_{a=1}^{N-1}\chi(a)w_a.
\]

Characters vanish on nonunits modulo \(r\), so the complete character family modulo \(r\) sees only the unit-residue aggregation of \(w\). In general it cannot recover arbitrary \(w\in V_N\) unless all occupied residues are units and are separated by the chosen modulus.

When \(r>N-1\) is prime, every \(1\le a\le N-1\) is a unit modulo \(r\). The multiplicative characters then form an orthogonal basis for functions on \((\mathbb Z/r\mathbb Z)^\times\), but their restrictions to the shorter interval \(\{1,\ldots,N-1\}\) constitute an overcomplete system rather than a square basis.

### Research question 7.1 — Minimal character reconstruction

Determine the smallest sets of moduli and characters whose restricted evaluation rows

\[
(\chi(1),\ldots,\chi(N-1))
\]

span \(V_N^*\), possibly after adjoining the constant row, difference-orbit rows, or additive frequencies.

## 8. Universal translation matrix

Given a finite observable family \(\mathcal O=\{L_1,\ldots,L_s\}\subset V_N^*\), define

\[
A_{N,\mathcal O}
=
\begin{pmatrix}
L_1\\
\vdots\\
L_s
\end{pmatrix}.
\]

The associated universal translation operator is

\[
\mathfrak T_{N,\mathcal O}:V_N\to\mathbb C^s,
\qquad
w\mapsto A_{N,\mathcal O}w.
\]

Reconstruction is possible exactly when

\[
\operatorname{rank}(A_{N,\mathcal O})=N-1.
\]

The invisible information is exactly

\[
\ker(A_{N,\mathcal O}).
\]

## 9. Main conceptual conclusion

Complete reconstruction is elementary with exact differences or a sufficiently large Fourier modulus. The substantive research program is therefore a compressed-observability problem:

> Which analytically natural observables—Dirichlet characters, residue channels, difference orbits, low frequencies, and symmetry sectors—recover a specified class of arithmetic fiber weights using far fewer than \(N-1\) measurements?

For unrestricted weights, no linear measurement system with fewer than \(N-1\) scalar measurements can be injective. Compression can only arise by restricting the weight class, exploiting symmetry, sparsity, arithmetic support, positivity, or approximate low-dimensional structure.

This reframes PASS029–PASS035: their low-dimensional amplitude structure and separate cancellation coordinate are evidence about restricted arithmetic weight classes, not about injectivity on all of \(V_N\).

## 10. Literature-status discipline

A preliminary search did not locate this exact PVG addition-fiber packaging or the named universal translation matrix. However, all component tools—finite Fourier inversion, character orthogonality, rank/nullity, additive convolution, and residue decomposition—are standard. No priority or novelty claim should be made until a systematic bibliographic review is completed.
