# PVG Addition-Fiber Operator 001

Status: exact operator identities and symmetry decomposition.

Scientific ceiling: operator construction only; no spectral gap, asymptotic estimate, or Goldbach proof.

## 1. Why the symmetric phase is trivial

On the exact fiber \(\mathcal G_N\),

\[
\rho(x)+\rho(y)=N.
\]

Hence

\[
\mathcal E_\alpha(x)\mathcal E_\alpha(y)
=e(\alpha N),
\]

which is constant across the fiber. Therefore the symmetric product phase carries no internal fiber geometry.

## 2. Ambient pair space and fiber projection

Let

\[
\mathcal X=\mathbb N_0^{(\mathbb P)}
\]

be the positive valuation space. On the ambient pair space \(\mathcal X\times\mathcal X\), define the fiber projector

\[
(P_NF)(x,y)
=
\mathbf1_{\rho(x)+\rho(y)=N}F(x,y).
\]

For finitely supported \(F\), define the fiber summation functional

\[
\Sigma_N(F)
=
\sum_{x,y}(P_NF)(x,y)
=
\int_{\mathcal G_N}F(x,y)\,d\mu_N.
\]

Thus additive convolution is obtained by taking

\[
F(x,y)=\widehat f(x)\widehat g(y).
\]

## 3. Difference phase

Define the nontrivial internal phase

\[
\boxed{
\mathcal D_\alpha(x,y)
=
e\bigl(\alpha(\rho(x)-\rho(y))\bigr).
}
\]

On the fiber,

\[
\rho(x)-\rho(y)=2\rho(x)-N,
\]

so

\[
\mathcal D_\alpha(x,y)
=e(-\alpha N)e(2\alpha\rho(x)).
\]

Unlike the symmetric product phase, \(\mathcal D_\alpha\) varies along the fiber.

## 4. Difference-phase fiber transform

For a weight \(W\) on the ambient pair space, define

\[
\boxed{
\mathcal A_\alpha W(N)
=
\int_{\mathcal G_N}
W(x,y)\mathcal D_\alpha(x,y)\,d\mu_N.
}
\]

Equivalently,

\[
\mathcal A_\alpha W(N)
=
\sum_{a+b=N}
W(\nu(a),\nu(b))e(\alpha(a-b)).
\]

Using \(b=N-a\),

\[
\boxed{
\mathcal A_\alpha W(N)
=
e(-\alpha N)
\sum_{a=1}^{N-1}
W(\nu(a),\nu(N-a))e(2\alpha a).
}
\]

Thus the internal difference transform is an ordinary Fourier transform along the ordered fiber path, up to the global phase \(e(-\alpha N)\).

## 5. Reflection action

Let

\[
(\sigma W)(x,y)=W(y,x).
\]

Then

\[
\mathcal D_\alpha(y,x)=\mathcal D_{-\alpha}(x,y)
=\overline{\mathcal D_\alpha(x,y)}.
\]

Decompose

\[
W=W^++W^-,
\]

where

\[
W^+(x,y)=\frac{W(x,y)+W(y,x)}2,
\]

\[
W^-(x,y)=\frac{W(x,y)-W(y,x)}2.
\]

Then

\[
\sigma W^+=W^+,
\qquad
\sigma W^-=-W^-.
\]

## 6. Cosine/sine decomposition

For real-valued \(W^+\), pairing each orbit \((x,y)\leftrightarrow(y,x)\) gives

\[
\boxed{
\mathcal A_\alpha W^+(N)
=
\int_{\mathcal G_N}
W^+(x,y)
\cos\bigl(2\pi\alpha(\rho(x)-\rho(y))\bigr)
\,d\mu_N,
}
\]

with the natural counting convention over ordered pairs.

For real-valued antisymmetric \(W^-\),

\[
\boxed{
\mathcal A_\alpha W^-(N)
=
i
\int_{\mathcal G_N}
W^-(x,y)
\sin\bigl(2\pi\alpha(\rho(x)-\rho(y))\bigr)
\,d\mu_N.
}
\]

Therefore:

- symmetric fiber information lives in cosine modes;
- antisymmetric fiber information lives in sine modes.

At \(\alpha=0\), every antisymmetric weight vanishes after fiber summation:

\[
\mathcal A_0W^-(N)=0.
\]

## 7. Residue-difference fibers

Fix a modulus \(r\). For \(d\bmod r\), define

\[
\mathcal H_{N,r,d}
=
\{(x,y)\in\mathcal G_N:
\rho(x)-\rho(y)\equiv d\pmod r\}.
\]

For a weight \(W\), define its difference-channel mass

\[
M_{N,r,W}(d)
=
\int_{\mathcal H_{N,r,d}}W(x,y)\,d\mu_N.
\]

The reflection sends

\[
d\longleftrightarrow-d\pmod r.
\]

Thus the natural difference orbits are

\[
\{d,-d\}.
\]

The fixed channels satisfy

\[
2d\equiv0\pmod r.
\]

For odd prime \(r\), the only fixed channel is \(d=0\).

## 8. Finite Fourier transform across difference channels

For \(k\bmod r\), define

\[
\widehat M_{N,r,W}(k)
=
\sum_{d\bmod r}
e\left(\frac{kd}{r}\right)M_{N,r,W}(d).
\]

Then exactly

\[
\boxed{
\widehat M_{N,r,W}(k)
=
\int_{\mathcal G_N}
W(x,y)
e\left(\frac{k(\rho(x)-\rho(y))}{r}\right)
\,d\mu_N.
}
\]

This is the discrete difference-phase transform of the fiber.

Fourier inversion gives

\[
\boxed{
M_{N,r,W}(d)
=
\frac1r\sum_{k\bmod r}
e\left(-\frac{kd}{r}\right)
\widehat M_{N,r,W}(k).
}
\]

Hence the difference-channel masses and their phase modes contain exactly the same information.

## 9. Symmetric and antisymmetric channel content

If \(W\) is symmetric, then

\[
M_{N,r,W}(d)=M_{N,r,W}(-d).
\]

Consequently,

\[
\widehat M_{N,r,W}(k)
=
M(0)+
2\sum_{d\in\mathcal O_r^+}
M(d)
\cos\left(\frac{2\pi kd}{r}\right),
\]

where \(\mathcal O_r^+\) contains one representative from each nonzero orbit \(\{d,-d\}\).

If \(W\) is antisymmetric, then

\[
M_{N,r,W}(-d)=-M_{N,r,W}(d),
\]

and only sine modes remain.

This provides the exact algebraic basis for orbit-amplitude and cancellation-coordinate decompositions.

## 10. Relation to residue-pair channels

On the fiber \(a+b\equiv N\pmod r\), the difference \(d=a-b\) determines the residue pair when \(2\) is invertible modulo \(r\):

\[
a\equiv\frac{N+d}{2}\pmod r,
\qquad
b\equiv\frac{N-d}{2}\pmod r.
\]

Therefore, for odd \(r\), residue-pair fibers and difference fibers are equivalent coordinate systems.

This explains why previous AVRG computations organized by residue differences can be reinterpreted as a finite Fourier analysis of the addition fiber.

## 11. Weighted Goldbach specialization

Take

\[
W_\Lambda(x,y)=\widehat\Lambda(x)\widehat\Lambda(y).
\]

Then

\[
\mathcal A_\alpha W_\Lambda(N)
=
\sum_{a+b=N}
\Lambda(a)\Lambda(b)e(\alpha(a-b)).
\]

At \(\alpha=0\),

\[
\mathcal A_0W_\Lambda(N)=R_\Lambda(N).
\]

At rational frequencies \(\alpha=k/r\), the transform resolves the weighted Goldbach mass by residue-difference channels modulo \(r\).

## 12. Dirichlet characters versus additive difference phases

These two decompositions must not be conflated.

- A Dirichlet character gives the multiplicative phase
  \[
  \chi(a)=\chi(\rho(x)).
  \]
- A difference Fourier mode gives the additive phase
  \[
  e(k(a-b)/r).
  \]

Both act on the same fiber, but they diagonalize different structures.

Their joint transform is

\[
\mathcal J_{\chi,k}(N)
=
\sum_{a+b=N}
\chi(a)
W(\nu(a),\nu(b))
e\left(\frac{k(a-b)}r\right).
\]

This joint character/difference transform is a candidate bridge between PASS013 character decompositions and PASS028–PASS035 difference-orbit geometry.

## 13. What is genuinely new here

The identities are elementary once the fiber is defined. The potentially useful content is the organization:

1. ambient pair space;
2. exact fiber projection;
3. nontrivial difference-phase transform;
4. reflection parity decomposition;
5. residue-difference DFT;
6. joint multiplicative-character/additive-difference analysis.

A future theorem must demonstrate that this organization yields a new estimate, invariant, compression law, or obstruction not visible from ordinary residue bookkeeping alone.

## 14. Next pass

Construct and test the joint matrix

\[
\mathcal J_{\chi,k}(N)
\]

for the seven locked prime moduli and the existing AVRG windows. Determine exactly which prior quantities are recovered by:

- \(k=0\);
- the principal character;
- even/odd character parity;
- cosine/sine orbit modes;
- the zero-difference channel.

The first goal is an exact reconstruction theorem, not a predictive claim.
