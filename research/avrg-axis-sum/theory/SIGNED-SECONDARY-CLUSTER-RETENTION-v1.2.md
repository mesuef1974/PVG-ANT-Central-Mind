# Signed Secondary Cluster Retention

Status: proved identity / certified lower-bound mechanism / no Goldbach claim.

Let q=r/gcd(2,r), u=2/gcd(2,r), and let Z(c) be the reduced von-Mangoldt channel indexed by c=ua mod q. Write the paired nonzero frequencies as K_q={1,...,floor((q-1)/2)} and treat k=q/2 separately when q is even.

Choose disjoint sets S (major pairs), C_1,...,C_m (secondary clusters), and R (unresolved tail) whose union is K_q. For a channel c define

M_S(c)=R_Lambda(N)/q + Nyquist(c) + (2/q) sum_{k in S} Re( Zhat(k)e_q(-kc) ),

G_j(c)=(2/q) sum_{k in C_j} Re( Zhat(k)e_q(-kc) ).

Then

Z(c)=M_S(c)+sum_j G_j(c)+T_R(c).

If the unresolved tail is bounded by any valid B_R(c)>=|T_R(c)| and the higher-prime-power contamination by C_hpp(c), then

Y_pp(c) >= M_S(c)+sum_j G_j(c)-B_R(c)-C_hpp(c).

Hence positivity of the right-hand side certifies a prime-prime representation in the channel.

## Exact-cluster invariance

If every cluster sum G_j(c) is evaluated exactly, regrouping the same retained frequencies into different clusters changes neither the reconstructed signed contribution nor the certificate. Clustering is therefore an evaluation/storage device, not a source of new information.

## Monotone retention principle

Moving a frequency pair from the unresolved absolute-value tail into an exactly evaluated signed cluster cannot weaken the lower bound. For a singleton contribution x,

signed contribution x >= -|x|.

Thus exact signed retention monotonically improves or preserves the certificate.

## Energy ordering

Under a fixed budget of retained pairs and a remaining singleton absolute bound, choosing the largest-energy pairs |Zhat(k)|^2 first minimizes the total amplitude left unresolved. This is the declared benchmark policy; it is not claimed optimal for every possible channel-dependent objective.

## Honest classification

- Decomposition: identity.
- Monotonicity: elementary inequality.
- Computational improvements: finite-range evidence.
- No new lower bound for R_Lambda(N) and no proof of Goldbach.