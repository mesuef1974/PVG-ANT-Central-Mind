# Independent Proof-Referee Request

**Suggested subject:** Request for an independent proof check of a smoothed weighted arithmetic-progression theorem

Dear Professor [Name],

I am seeking an independent line-by-line check of a theorem developed in a research project linking prime-valuation geometry with analytic number theory.

For fixed `q>=1`, fixed `r>=1`, a reduced residue class `a mod q`, and a fixed smooth compactly supported weight `W`, define

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0).
\]

The project derives a smooth asymptotic expansion for

\[
\sum_{n\equiv a\pmod q} I_r(n)W(n/x)
\]

from the twisted factorization

\[
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

where `H` is shown to be holomorphic for

\[
\Re(s)>\frac1{2r+2}.
\]

The claimed fixed-parameter smooth remainder is

\[
O_{q,r,W,\varepsilon}
\left(x^{1/(2r+2)+\varepsilon}\right).
\]

The proof has passed symbolic checks and two internal reviews, but it has not received an external mathematical referee report. I am therefore not asking for an originality judgment. I am asking only whether the argument is mathematically correct as stated.

The most important points to check are:

1. the local Bell series and extraction of the two `L`-factors;
2. the residual local order and the half-plane of absolute/local uniform convergence for `H`;
3. the treatment of characters and primes dividing `q`;
4. the character decomposition of reduced residue classes;
5. Mellin inversion and contour shifting;
6. the simple-pole and double-pole constants;
7. vertical growth and truncation arguments;
8. dependence of the implied constant on fixed `q`, `r`, `W`, and `epsilon`.

I can provide a compact referee packet and the complete proof. A report classifying the argument as pass, pass with minor repairs, major repair required, statement requires weakening, or proof failure would be sufficient.

The project explicitly makes no claim of a new analytic method, no claim of certified originality, and no claim related to RH or GRH.

Thank you for considering the request.

Sincerely,

[Name]
[Affiliation or “Independent researcher”]
[Contact information]

---

## Internal sending checklist

- Replace all placeholders.
- Attach the exact theorem statement and complete proof packet.
- State clearly that priority/originality is being reviewed separately.
- Do not request endorsement of the broader PVG program.
- Ask permission before quoting or naming the referee publicly.
- Record only the resulting classification and required repairs in Issue #15 unless the reviewer authorizes more.

## Neutral external classification (Stage Review 001)

State to reviewers exactly:

```text
Internally proved fixed-parameter weighted ANT result.
Exact prior-art status unresolved.
PVG materially contributed to discovery and formulation.
PVG necessity in the final proof is weak or not established.
```

Referee questions are separated; answer each independently:

1. Is the statement correct as written?
2. Is the proof correct?
3. Is the result known (priority / literature)?
4. Was the geometric layer (PVG) material - and in which roles?

For question 4, assess each role separately:
observable selection; formula discovery; local-factor identification;
proof steering; generalization proposal.

The post-review decision tree is pre-registered in
`P8_STOPPING_PROTOCOL.md`; no outcome renegotiation.

