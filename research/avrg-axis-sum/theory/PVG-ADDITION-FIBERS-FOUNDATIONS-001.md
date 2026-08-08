# PVG Addition Fibers — Foundations 001

Status: theory intake / exact identities plus clearly labeled research program

Scientific ceiling: no asymptotic proof, no Goldbach proof, and no RH/GRH progress.

## 1. Prime-valuation encoding

For \(n\ge 1\), let

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}\in \mathbb N_0^{(\mathbb P)}.
\]

Define the recovery map

\[
\rho(x)=\prod_p p^{x_p}.
\]

By unique factorization,

\[
\rho(\nu(n))=n,
\]

so \(\nu\) is injective on positive integers. Therefore the passage from \(n\) to \(\nu(n)\) loses no arithmetic information.

## 2. Positive addition fiber

For \(N\ge2\), define

\[
\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}.
\]

Its prime-valuation image is

\[
\mathcal G_N=\{(\nu(a),\nu(b)):a+b=N,\ a,b\ge1\}.
\]

The map

\[
\iota_N:\mathcal F_N^+\to\mathcal G_N,
\qquad
(a,b)\mapsto(\nu(a),\nu(b))
\]

is a bijection.

### Theorem 1 — no-loss translation

\[
\boxed{\iota_N\text{ is bijective}.}
\]

Proof: surjectivity is by definition. If

\[
(\nu(a),\nu(b))=(\nu(c),\nu(d)),
\]

then unique factorization gives \(a=c\) and \(b=d\).

Hence every point \((x,y)\in\mathcal G_N\) satisfies the nonlinear fiber equation

\[
\boxed{\rho(x)+\rho(y)=N.}
\]

The additive constraint is therefore a nonlinear surface in valuation coordinates:

\[
\prod_p p^{x_p}+\prod_p p^{y_p}=N.
\]

## 3. Symmetry and orbit structure

Define

\[
\sigma(x,y)=(y,x).
\]

Then

\[
\sigma(\mathcal G_N)=\mathcal G_N,
\qquad
\sigma^2=\operatorname{id}.
\]

Thus \(\mathbb Z/2\mathbb Z\) acts on the addition fiber.

- If \(N\) is odd, every orbit has size \(2\).
- If \(N\) is even, there is one fixed point:

\[
(\nu(N/2),\nu(N/2)).
\]

The number of unordered orbits is

\[
\boxed{|\mathcal G_N/\langle\sigma\rangle|=\left\lfloor\frac N2\right\rfloor.}
\]

## 4. Counting measure on the fiber

Define

\[
\mu_N=\sum_{a=1}^{N-1}\delta_{(\nu(a),\nu(N-a))}.
\]

For any function \(W\) on the valuation-pair space,

\[
\int W(x,y)\,d\mu_N(x,y)
=
\sum_{a=1}^{N-1}W(\nu(a),\nu(N-a)).
\]

This is the canonical counting measure for the positive addition fiber.

## 5. Fiber convolution theorem

Let \(f,g:\mathbb N\to\mathbb C\). Define their lifts

\[
\widehat f(x)=f(\rho(x)),
\qquad
\widehat g(y)=g(\rho(y)).
\]

Then the additive convolution

\[
(f*_+g)(N)=\sum_{a+b=N}f(a)g(b)
\]

satisfies

\[
\boxed{
(f*_+g)(N)
=
\int_{\mathcal G_N}\widehat f(x)\widehat g(y)\,d\mu_N(x,y).
}
\]

This is an exact identity, not a heuristic.

## 6. Prime and prime-power loci

Define

\[
\mathcal P_1=\{e_p:p\in\mathbb P\},
\]

where \(e_p\) is the unit vector on the \(p\)-axis. These are exactly the valuation vectors of prime numbers.

Define

\[
\mathcal A_1=\{k e_p:p\in\mathbb P,\ k\ge1\}.
\]

These are exactly the valuation vectors of prime powers.

The von Mangoldt lift satisfies

\[
\widehat\Lambda(x)\neq0
\iff
x\in\mathcal A_1,
\]

and if \(x=k e_p\), then

\[
\widehat\Lambda(x)=\log p.
\]

The prime-indicator lift satisfies

\[
\widehat{\mathbf1_{\mathbb P}}(x)=1
\iff
x\in\mathcal P_1.
\]

## 7. Goldbach as a fiber-intersection statement

The ordered prime-pair count is

\[
G(N)=
\int_{\mathcal G_N}
\widehat{\mathbf1_{\mathbb P}}(x)
\widehat{\mathbf1_{\mathbb P}}(y)
\,d\mu_N.
\]

Hence binary Goldbach is equivalent to

\[
\boxed{
\mathcal G_N\cap(\mathcal P_1\times\mathcal P_1)\neq\varnothing
\quad\text{for every even }N\ge4.
}
\]

The weighted von Mangoldt count is

\[
R_\Lambda(N)=
\int_{\mathcal G_N}
\widehat\Lambda(x)\widehat\Lambda(y)\,d\mu_N.
\]

It counts prime-axis pairs with prime-power weights.

## 8. Residue subfibers

For a modulus \(r\), define

\[
\mathcal G_{N;r}^{a,b}
=
\{(x,y)\in\mathcal G_N:
\rho(x)\equiv a\pmod r,
\rho(y)\equiv b\pmod r\}.
\]

Such a subfiber can be nonempty only if

\[
a+b\equiv N\pmod r.
\]

Therefore

\[
\boxed{
\mathcal G_N
=
\bigsqcup_{a\bmod r}
\mathcal G_{N;r}^{a,N-a}.
}
\]

## 9. Dirichlet-character fields

For a Dirichlet character \(\chi\bmod r\), define

\[
\widehat\chi(x)=\chi(\rho(x)).
\]

Then

\[
T_\chi(N)=
\sum_{a+b=N}\chi(a)\Lambda(a)\Lambda(b)
\]

becomes

\[
\boxed{
T_\chi(N)=
\int_{\mathcal G_N}
\widehat\chi(x)
\widehat\Lambda(x)
\widehat\Lambda(y)
\,d\mu_N.
}
\]

Thus Dirichlet characters act as phase/color fields on the fiber.

## 10. Honest classification

- Injectivity of \(\nu\): known theorem from unique factorization.
- Fiber bijection and convolution identity: exact identities.
- Goldbach intersection form: exact reformulation.
- Residue-fiber decomposition: exact identity.
- Geometric interpretation and proposed invariants: research framework.
- No theorem here proves nonemptiness of prime-prime intersections for all even fibers.
