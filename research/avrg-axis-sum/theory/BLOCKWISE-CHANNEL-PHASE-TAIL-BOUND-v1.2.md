# Blockwise Channel-Phase Tail Bound v1.2

Status: proved finite-dimensional inequality.

Let the reduced effective period be q=r/gcd(2,r), let u=2/gcd(2,r), and index effective channels by c=ua mod q. For the von Mangoldt channel mass Z(c), write

Z(c)=R_Lambda(N)/q + P_Nyq(c) + sum_{k in K_q} P_k(c),

where K_q={1,...,floor((q-1)/2)} and

P_k(c)=(2/q) Re( Zhat(k) exp(-2 pi i k c/q) ).

Choose a principal set S subset K_q and partition the remaining frequencies into disjoint nonempty blocks

K_q \ S = B_1 disjoint-union ... disjoint-union B_m.

For each block define

A_j = sum_{k in B_j} |Zhat(k)|^2,

Q_j(c)=sum_{k in B_j} cos^2(phi_k-2 pi k c/q),

where Zhat(k)=|Zhat(k)| exp(i phi_k). Then the tail satisfies

|T_S(c)| <= B_P(c),

B_P(c) := (2/q) sum_{j=1}^m sqrt(A_j Q_j(c)).

Proof: apply Cauchy-Schwarz separately inside each block and then the triangle inequality across blocks.

## Refinement monotonicity

If a block B is split into B' and B'', then

sqrt((A'+A'')(Q'+Q'')) >= sqrt(A'Q')+sqrt(A''Q'')

by Cauchy-Schwarz. Therefore every refinement of the partition weakly decreases the blockwise bound. In particular,

singleton bound <= any blockwise bound <= one-block channel-phase bound.

The singleton endpoint is

B_single(c)=(2/q) sum_{k notin S} |Zhat(k)| |cos(phi_k-2 pi k c/q)|.

This is still an upper bound on the absolute tail; it uses no cancellation between different remaining frequencies.

## Prime-channel certificate

Let C_hpp(N,r,c) be the local higher-prime-power contamination bound. If

R_Lambda(N)/q + P_Nyq(c) + sum_{k in S} P_k(c) > B_P(c)+C_hpp(N,r,c),

then the prime-prime channel mass is positive. Hence there exist primes p,p' with p+p'=N in that effective channel.

## Honest classification

- Blockwise bound and refinement monotonicity: proved identity/inequality.
- Numerical certificate gains: computational evidence only.
- No Goldbach theorem, asymptotic estimate, RH/GRH claim, or novelty claim is made.
- The effective channel coordinate is c=ua mod q; reflection is c -> uN-c mod q, not generally c -> -c.
