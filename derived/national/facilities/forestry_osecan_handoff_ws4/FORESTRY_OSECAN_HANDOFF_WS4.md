# WS4-driven Forestry Residue Handoff to OSeCAN

**Artifact:** `forestry_osecan_handoff_ws4` **Version:** `1.0.0`

**Status:** `pass`. Read-only screening artifact. No official OSeCAN file, UI, candidate activity limit, or frozen v5.1 artifact is changed.

## 1. Basis and boundary

The WS4 chain applies the frozen chain-v5.1 per-province product/residue coefficients to the realised 119 Mm3 WS4 harvest. The chain and this handoff are **origin-province** based. Handoff v10 process residue is **facility-province** based. The two zone rows are therefore not compared directly; the comparison is on national totals and tier positions only.

Primary basis: `scaled_to_119m_control` (control-total basis, 118,977,339.1 m3). Secondary basis: `ws4_achieved` (realised WS4 harvest). Both are reported.

Labels on every row: `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 2. WS4 control total

| Item | Value |
|---|---:|
| Provincial control total (m3) | 118,977,339.1 |
| WS4 achieved harvest (m3) | 118,977,392.880 |
| Overshoot (m3) | 53.780 |
| Treated area (ha) | 1,083,739.05 |

## 3. National case totals

| Basis | Stream | Case | PJ |
|---|---|---|---:|
| `scaled_to_119m_control` | process | `process_availability_000` | 0.000000 |
| `scaled_to_119m_control` | process | `process_availability_025` | 124.687729 |
| `scaled_to_119m_control` | process | `process_availability_050` | 249.375457 |
| `scaled_to_119m_control` | process | `process_availability_075` | 374.063186 |
| `scaled_to_119m_control` | harvest | `harvest_recovery_035` | 155.543779 |
| `scaled_to_119m_control` | harvest | `harvest_recovery_060` | 266.646477 |
| `scaled_to_119m_control` | harvest | `harvest_recovery_075` | 333.308097 |
| `ws4_achieved` | process | `process_availability_000` | 0.000000 |
| `ws4_achieved` | process | `process_availability_025` | 124.687785 |
| `ws4_achieved` | process | `process_availability_050` | 249.375570 |
| `ws4_achieved` | process | `process_availability_075` | 374.063355 |
| `ws4_achieved` | harvest | `harvest_recovery_035` | 155.543849 |
| `ws4_achieved` | harvest | `harvest_recovery_060` | 266.646598 |
| `ws4_achieved` | harvest | `harvest_recovery_075` | 333.308247 |

## 4. Zone totals (primary basis)

| Zone | Process 0% | Process 25% | Process 50% | Process 75% | Harvest 35% | Harvest 60% | Harvest 75% |
|---|---:|---:|---:|---:|---:|---:|---:|
| B1 | 0.000000 | 3.612824 | 7.225648 | 10.838472 | 3.465794 | 5.941361 | 7.426702 |
| B2 | 0.000000 | 39.999722 | 79.999444 | 119.999165 | 38.371865 | 65.780340 | 82.225425 |
| A1 | 0.000000 | 15.193010 | 30.386019 | 45.579029 | 15.245494 | 26.135132 | 32.668915 |
| A2 | 0.000000 | 8.406160 | 16.812321 | 25.218481 | 8.435199 | 14.460342 | 18.075427 |
| S1 | 0.000000 | 3.665037 | 7.330074 | 10.995111 | 17.860941 | 30.618756 | 38.273445 |
| M1 | 0.000000 | 1.181574 | 2.363147 | 3.544721 | 1.425740 | 2.444125 | 3.055156 |
| O1 | 0.000000 | 11.749686 | 23.499372 | 35.249059 | 15.301332 | 26.230855 | 32.788569 |
| O2 | 0.000000 | 2.351765 | 4.703531 | 7.055296 | 3.062647 | 5.250252 | 6.562815 |
| Q1 | 0.000000 | 16.799342 | 33.598683 | 50.398025 | 22.942263 | 39.329593 | 49.161992 |
| Q2 | 0.000000 | 10.708878 | 21.417756 | 32.126634 | 14.624734 | 25.070972 | 31.338715 |
| T1 | 0.000000 | 9.373453 | 18.746906 | 28.120358 | 12.616470 | 21.628234 | 27.035292 |
| L1 | 0.000000 | 1.559595 | 3.119189 | 4.678784 | 2.072893 | 3.553530 | 4.441913 |
| N1 | 0.000000 | 0.086683 | 0.173367 | 0.260050 | 0.118407 | 0.202984 | 0.253730 |

Zone rows conserve the national totals for every basis/stream/case; each province's 13-zone weights sum to one.

## 5. Tier comparison with frozen v5.1

Frozen v5.1 carries 21 scenario/stream/case tier positions. Handoff v10 matches all 21/21 positions. The WS4 chain covers the 119 Mm3 control only, so only its 7 positions per basis are like-for-like; the 100/150 Mm3 positions are reported as not available rather than fabricated.

| Basis | Stream | Case | National PJ | Tier | v10 119m PJ | Delta PJ | Changed |
|---|---|---|---:|---|---:|---:|---|
| `scaled_to_119m_control` | process | `process_availability_000` | 0.000000 | T1 | 0.000000 | +0.000000000 | False |
| `scaled_to_119m_control` | process | `process_availability_025` | 124.687729 | T3 | 124.687729 | -0.000000519 | False |
| `scaled_to_119m_control` | process | `process_availability_050` | 249.375457 | above_T4 | 249.375458 | -0.000001039 | False |
| `scaled_to_119m_control` | process | `process_availability_075` | 374.063186 | above_T4 | 374.063188 | -0.000001558 | False |
| `scaled_to_119m_control` | harvest | `harvest_recovery_035` | 155.543779 | T4 | 155.543768 | +0.000010393 | False |
| `scaled_to_119m_control` | harvest | `harvest_recovery_060` | 266.646477 | above_T4 | 266.646460 | +0.000017817 | False |
| `scaled_to_119m_control` | harvest | `harvest_recovery_075` | 333.308097 | above_T4 | 333.308075 | +0.000022273 | False |
| `ws4_achieved` | process | `process_availability_000` | 0.000000 | T1 | 0.000000 | +0.000000000 | False |
| `ws4_achieved` | process | `process_availability_025` | 124.687785 | T3 | 124.687729 | +0.000055842 | False |
| `ws4_achieved` | process | `process_availability_050` | 249.375570 | above_T4 | 249.375458 | +0.000111683 | False |
| `ws4_achieved` | process | `process_availability_075` | 374.063355 | above_T4 | 374.063188 | +0.000167525 | False |
| `ws4_achieved` | harvest | `harvest_recovery_035` | 155.543849 | T4 | 155.543768 | +0.000080702 | False |
| `ws4_achieved` | harvest | `harvest_recovery_060` | 266.646598 | above_T4 | 266.646460 | +0.000138346 | False |
| `ws4_achieved` | harvest | `harvest_recovery_075` | 333.308247 | above_T4 | 333.308075 | +0.000172933 | False |

### Reference tier positions

| Scenario | Stream | Case | v10 PJ | v10 tier | Frozen v5.1 | Match |
|---|---|---|---:|---|---|---|
| 100m | process | `process_availability_000` | 0.000000 | T1 | T1 | True |
| 100m | process | `process_availability_025` | 104.809505 | T2 | T2 | True |
| 100m | process | `process_availability_050` | 209.619009 | T4 | T4 | True |
| 100m | process | `process_availability_075` | 314.428514 | above_T4 | above_T4 | True |
| 100m | harvest | `harvest_recovery_035` | 130.635373 | T3 | T3 | True |
| 100m | harvest | `harvest_recovery_060` | 223.946354 | above_T4 | above_T4 | True |
| 100m | harvest | `harvest_recovery_075` | 279.932942 | above_T4 | above_T4 | True |
| 119m | process | `process_availability_000` | 0.000000 | T1 | T1 | True |
| 119m | process | `process_availability_025` | 124.687729 | T3 | T3 | True |
| 119m | process | `process_availability_050` | 249.375458 | above_T4 | above_T4 | True |
| 119m | process | `process_availability_075` | 374.063188 | above_T4 | above_T4 | True |
| 119m | harvest | `harvest_recovery_035` | 155.543768 | T4 | T4 | True |
| 119m | harvest | `harvest_recovery_060` | 266.646460 | above_T4 | above_T4 | True |
| 119m | harvest | `harvest_recovery_075` | 333.308075 | above_T4 | above_T4 | True |
| 150m | process | `process_availability_000` | 0.000000 | T1 | T1 | True |
| 150m | process | `process_availability_025` | 156.716305 | T4 | T4 | True |
| 150m | process | `process_availability_050` | 313.432610 | above_T4 | above_T4 | True |
| 150m | process | `process_availability_075` | 470.148915 | above_T4 | above_T4 | True |
| 150m | harvest | `harvest_recovery_035` | 200.593895 | T4 | T4 | True |
| 150m | harvest | `harvest_recovery_060` | 343.875248 | above_T4 | above_T4 | True |
| 150m | harvest | `harvest_recovery_075` | 429.844060 | above_T4 | above_T4 | True |

## 6. Official OSeCAN integrity

Official OSeCAN tree: 146 files; tree SHA-256 `80caa91c3e91c89006b8d5e3ad78232eade70a298a83657510fffa26924bc64a`; changed files: 0. No candidate activity limit was written to OSeCAN.

No unexpected `D`: True.

## 7. Caveats

- The WS4 chain applies frozen chain-v5.1 coefficients to a whole-block 119 Mm3 WS4 harvest. It is not a sustainable harvest, AAC, policy result, or investment case.
- The WS4 chain is origin-province based; handoff v10 process residue is facility-province based. Zone rows are not directly comparable across the two bases. Only national totals and tier positions are compared.
- The WS4 chain covers the 119 Mm3 control only. Frozen v5.1 has 100/119/150 Mm3 tier positions; the 100 and 150 Mm3 positions are reported as not available rather than fabricated.
- Zone weights are frozen handoff-v10 screening proxies, not observed sub-provincial residue shares or policy.
- Process residue and harvest residue remain separate streams and are never summed. PJ uses the frozen 18.5 GJ/ODT lower heating value; 0.60 harvest recovery is a reference case.
- No candidate activity limit, official OSeCAN file, UI surface, or frozen v5.1 artifact is changed.
- No transport, cost, revenue, tenure, AAC, capacity-expansion, or policy claim is made.

## 8. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.forestry_osecan_handoff_ws4
```
