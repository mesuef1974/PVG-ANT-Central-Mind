# ACTIVE-003-S execution receipt

Executed exact reduced-domain verification:

```text
4 <= N <= 80
3 <= r <= 20
B <= 4
optimization cases = 4,697
```

Observed wall-clock limitation:

- the naive full-domain verifier exceeded the available execution window;
- no full-domain PASS is recorded;
- no JSON for the full domain was fabricated or inferred.

Verified reduced-domain facts:

```text
optimum mismatches = 0
false certificates = 0
bound mismatches = 0
minimality failures = 0
coverage failures = 0
all forbidden families = 49,815
minimal forbidden families = 986
representation reduction = 98.0206765%
minimal size-2 edges = 954
minimal size-3 edges = 32
```

Receipt classification: `executed / validated_partial / not closed`.
