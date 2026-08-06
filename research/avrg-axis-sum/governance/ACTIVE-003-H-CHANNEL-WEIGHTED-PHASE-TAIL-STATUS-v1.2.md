# ACTIVE-003-H — Channel-Weighted Phase Tail Bound Status

Status: `CLOSED-PASS`

## Completed

- Reduced paired-frequency expansion retained.
- Channel-dependent phase vector introduced.
- Channel-weighted Cauchy–Schwarz tail bound proved.
- Pointwise domination over the previous uniform paired-energy bound proved.
- Prime-channel certificate updated with the channel-weighted tail.
- Independent finite verifier added.
- Verification completed for `2 <= N <= 300`, `1 <= r <= 20`, and `K = 0,1,2,3`.

## Verification summary

```text
effective channels       = 46,345
prime-positive channels  = 15,833
bound mismatches         = 0
false certificates       = 0
```

Certificate comparison:

```text
K=0: uniform 1,316  -> phase-weighted 2,260
K=1: uniform 5,634  -> phase-weighted 7,358
K=2: uniform 8,471  -> phase-weighted 9,813
K=3: uniform 10,319 -> phase-weighted 11,177
```

At `K=3`, the phase-weighted certificate covers about `70.60%` of the prime-positive channels in the declared finite sample.

## Classification

- algebraic decomposition: proved;
- channel-weighted tail inequality: proved;
- domination over uniform bound: proved;
- finite certificate gain: computation;
- asymptotic estimate for the Fourier tail: open;
- Goldbach theorem: not claimed;
- RH/GRH progress: none.

## Remaining wall

The new bound still treats the entire unselected tail through one Cauchy–Schwarz inequality. It sees the channel phases, but it does not exploit correlations or cancellation between neighboring frequency blocks.

## Next target

`ACTIVE-003-I` — partition the remaining frequencies into blocks and derive a blockwise channel-dependent lower bound. Compare:

1. one global phase-weighted tail bound;
2. divisor/gcd-structured frequency blocks;
3. contiguous-energy blocks;
4. exact treatment of a small number of dangerous blocks.

No novelty or priority claim is authorized without literature review.
