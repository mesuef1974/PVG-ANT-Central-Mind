# Dataset 003 Protocol Freeze Certificate

**Certificate ID:** `CERT-PVG-LPD-DATASET003-FREEZE-001`  
**Protocol:** `PVG-LPD-DATASET-003-PROTOCOL-001`  
**Branch:** `agent/local-prime-density-dataset003-protocol`  
**Parent main commit:** `10adf018a0c96f8317897d968870216a07ba35ec`  
**Status:** `PRE-DATA FREEZE PENDING MERGE`

## Frozen elements

- independent numerical range `[10^7,10^8)`;
- three deterministic window families `theta = 1/2, 2/3, 3/4`;
- 240 windows per family;
- Dataset 002 training source only;
- classical Ridge alpha `300`;
- primary candidate Ridge alpha `3000`;
- secondary descriptive lagged-Lambda Ridge alpha `1000`;
- past-only lags `h,2h,4h`;
- character/residue moduli `3,4,5,7,8,11`;
- 10,000-replicate paired stratified bootstrap;
- bootstrap seed `20260712`;
- family-stability requirement;
- Python/R agreement requirement;
- native residue-class endpoint as secondary and non-promotional.

## Guard

No Dataset 003 data may be generated, inspected, or analyzed before this protocol is merged to `main`.

Any change after merge requires:

1. a new protocol ID;
2. a new freeze certificate;
3. a new commit made before regenerated or inspected Dataset 003 results.

## Scientific ceiling

- no theorem;
- no confirmed signal;
- no RH/GRH progress;
- no positive PVG prediction claim.

## Freeze decision

```text
PROTOCOL CONTENT: FROZEN
DATA GENERATION: BLOCKED
NEXT GATE: PROTOCOL REVIEW AND MERGE
```
