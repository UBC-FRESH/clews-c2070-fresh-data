# Forestry Residue Scenarios to OSeCAN Zones v7 (E1+E2c)

Status: **pass**. Artifact version `7.0.0`; generated 2026-11-23T05:38:50+00:00.

This is a read-only, model-estimate screening handoff. Every row is `model_estimate=true`, `observed=false`, `policy_grade=false`, and `official_osecan_changed=false`. No official OSeCAN input is written or modified.

## Method

1. Read province process residue (sum of facility classes) and gross harvest residue from `national_facility_chain_scenarios_v7`.
2. Apply the seven availability/recovery fractions from `national_residue_curve_v7` to each scenario total.
3. Split each province/case PJ total across all 13 OSeCAN zones with the published `forestry_osecan_handoff_v8` weights; the floating residual is assigned to the last zone so province totals are exactly conserved.
4. Compare national, BC, and zone totals with the adopted SUPBCW tier caps, the SUPBCWB1/SUPBCWB2 2050 zonal activity limits, and the 2050 OSeCAN stress_119m context. These references are context, not policy targets.
5. Emit a candidate activity-limit table for screening only. It is not applied to OSeCAN.

## National scenario/case PJ

| Scenario | Stream | Availability case | PJ | ODT |
|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | 0 |
| 100m | process | process_availability_025 | 104.81 | 5,665,379 |
| 100m | process | process_availability_050 | 209.62 | 11,330,757 |
| 100m | process | process_availability_075 | 314.43 | 16,996,136 |
| 100m | harvest | harvest_recovery_035 | 130.64 | 7,061,372 |
| 100m | harvest | harvest_recovery_060 | 223.95 | 12,105,208 |
| 100m | harvest | harvest_recovery_075 | 279.93 | 15,131,510 |
| 119m | process | process_availability_000 | 0.00 | 0 |
| 119m | process | process_availability_025 | 124.69 | 6,739,877 |
| 119m | process | process_availability_050 | 249.38 | 13,479,755 |
| 119m | process | process_availability_075 | 374.06 | 20,219,632 |
| 119m | harvest | harvest_recovery_035 | 155.54 | 8,407,771 |
| 119m | harvest | harvest_recovery_060 | 266.65 | 14,413,322 |
| 119m | harvest | harvest_recovery_075 | 333.31 | 18,016,653 |
| 150m | process | process_availability_000 | 0.00 | 0 |
| 150m | process | process_availability_025 | 156.72 | 8,471,152 |
| 150m | process | process_availability_050 | 313.43 | 16,942,303 |
| 150m | process | process_availability_075 | 470.15 | 25,413,455 |
| 150m | harvest | harvest_recovery_035 | 200.59 | 10,842,913 |
| 150m | harvest | harvest_recovery_060 | 343.88 | 18,587,851 |
| 150m | harvest | harvest_recovery_075 | 429.84 | 23,234,814 |

Process and harvest streams are separate and are never summed. The 119m rows reproduce `national_residue_curve_v7` exactly at the national level.

## Zone summary at the primary 119m scenario

| Zone | Zone name | Process 50% PJ | Process share | Harvest 60% PJ | Harvest share | Technology suggestion |
|---|---|---|---|---|---|---|
| B1 | South Coast / Lower Mainland | 7.23 | 2.9% | 5.94 | 2.2% | SUPBCWB1 |
| B2 | Interior & North | 80.00 | 32.1% | 65.78 | 24.7% | SUPBCWB2 |
| A1 | Calgary–Edmonton corridor | 30.39 | 12.2% | 26.14 | 9.8% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | North (oil sands) | 16.81 | 6.7% | 14.46 | 5.4% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | Saskatchewan | 7.33 | 2.9% | 30.62 | 11.5% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | Manitoba | 2.36 | 0.9% | 2.44 | 0.9% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | Southern Ontario | 23.50 | 9.4% | 26.23 | 9.8% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | Northern Ontario | 4.70 | 1.9% | 5.25 | 2.0% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | Southern Quebec | 33.60 | 13.5% | 39.33 | 14.7% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | Northern Quebec (hydro) | 21.42 | 8.6% | 25.07 | 9.4% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | Atlantic | 18.75 | 7.5% | 21.63 | 8.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | Newfoundland & Labrador | 3.12 | 1.3% | 3.55 | 1.3% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | North (territories) | 0.17 | 0.1% | 0.20 | 0.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Candidate activity-limit table

`candidate_activity_limits.csv` is read-only and not applied. Grain: scenario x stream x availability case x zone. Columns include `candidate_activity_limit_pj`, `candidate_activity_limit_odt`, `technology_suggestion`, `official_limit_reference`, `official_limit_pj`, `candidate_ratio_to_official_limit`, and `candidate_headroom_pj`. `candidate_status` is always `read_only_candidate_not_applied`.

| Zone | Scenario | Stream | Case | Candidate PJ | Technology suggestion |
|---|---|---|---|---|---|
| B1 | 119m | process | process_availability_050 | 7.23 | SUPBCWB1 |
| B1 | 119m | harvest | harvest_recovery_060 | 5.94 | SUPBCWB1 |
| B2 | 119m | process | process_availability_050 | 80.00 | SUPBCWB2 |
| B2 | 119m | harvest | harvest_recovery_060 | 65.78 | SUPBCWB2 |
| A1 | 119m | process | process_availability_050 | 30.39 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A1 | 119m | harvest | harvest_recovery_060 | 26.14 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | 119m | process | process_availability_050 | 16.81 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | 119m | harvest | harvest_recovery_060 | 14.46 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | 119m | process | process_availability_050 | 7.33 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | 119m | harvest | harvest_recovery_060 | 30.62 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | 119m | process | process_availability_050 | 2.36 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | 119m | harvest | harvest_recovery_060 | 2.44 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | 119m | process | process_availability_050 | 23.50 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | 119m | harvest | harvest_recovery_060 | 26.23 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | 119m | process | process_availability_050 | 4.70 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | 119m | harvest | harvest_recovery_060 | 5.25 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | 119m | process | process_availability_050 | 33.60 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | 119m | harvest | harvest_recovery_060 | 39.33 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | process | process_availability_050 | 21.42 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | harvest | harvest_recovery_060 | 25.07 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | process | process_availability_050 | 18.75 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | harvest | harvest_recovery_060 | 21.63 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | process | process_availability_050 | 3.12 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | harvest | harvest_recovery_060 | 3.55 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | process | process_availability_050 | 0.17 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | harvest | harvest_recovery_060 | 0.20 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Supply-curve and 2050 context comparison

Ratios above 1.0 mean the scenario/case PJ exceeds the reference; negative headroom is the excess. References are context only.

| Scenario | Stream | Case | National PJ | Tier | T4 ratio | 2050 national ratio | BC PJ | BC zonal ratio | BC 2050 ratio |
|---|---|---|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 100m | process | process_availability_025 | 104.81 | T2 | 0.491 | 0.685 | 36.27 | 0.833 | 0.833 |
| 100m | process | process_availability_050 | 209.62 | T4 | 0.982 | 1.371 | 72.54 | 1.667 | 1.667 |
| 100m | process | process_availability_075 | 314.43 | above_T4 | 1.472 | 2.056 | 108.81 | 2.500 | 2.500 |
| 100m | harvest | harvest_recovery_035 | 130.64 | T3 | 0.612 | 0.854 | 34.79 | 0.799 | 0.799 |
| 100m | harvest | harvest_recovery_060 | 223.95 | above_T4 | 1.049 | 1.464 | 59.65 | 1.370 | 1.370 |
| 100m | harvest | harvest_recovery_075 | 279.93 | above_T4 | 1.311 | 1.831 | 74.56 | 1.713 | 1.713 |
| 119m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 119m | process | process_availability_025 | 124.69 | T3 | 0.584 | 0.815 | 43.61 | 1.002 | 1.002 |
| 119m | process | process_availability_050 | 249.38 | above_T4 | 1.168 | 1.631 | 87.23 | 2.004 | 2.004 |
| 119m | process | process_availability_075 | 374.06 | above_T4 | 1.752 | 2.446 | 130.84 | 3.006 | 3.006 |
| 119m | harvest | harvest_recovery_035 | 155.54 | T4 | 0.728 | 1.017 | 41.84 | 0.961 | 0.961 |
| 119m | harvest | harvest_recovery_060 | 266.65 | above_T4 | 1.249 | 1.744 | 71.72 | 1.648 | 1.648 |
| 119m | harvest | harvest_recovery_075 | 333.31 | above_T4 | 1.561 | 2.180 | 89.65 | 2.060 | 2.060 |
| 150m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 150m | process | process_availability_025 | 156.72 | T4 | 0.734 | 1.025 | 49.33 | 1.134 | 1.134 |
| 150m | process | process_availability_050 | 313.43 | above_T4 | 1.468 | 2.050 | 98.67 | 2.267 | 2.267 |
| 150m | process | process_availability_075 | 470.15 | above_T4 | 2.202 | 3.074 | 148.00 | 3.401 | 3.401 |
| 150m | harvest | harvest_recovery_035 | 200.59 | T4 | 0.939 | 1.312 | 47.33 | 1.087 | 1.087 |
| 150m | harvest | harvest_recovery_060 | 343.88 | above_T4 | 1.610 | 2.249 | 81.13 | 1.864 | 1.864 |
| 150m | harvest | harvest_recovery_075 | 429.84 | above_T4 | 2.013 | 2.811 | 101.41 | 2.330 | 2.330 |

## Caveats

- All values are model estimates; observed=false and policy_grade=false.
- The 100/119/150 Mm3 cases are planning allocations, not legal AACs, sustainable-supply determinations, or observed harvest outcomes.
- Zone splits are explicit forestry_osecan_handoff_v8 proxy weights; no observed sub-provincial residue split exists.
- BC zone weights are proportional to the 2050 SUPBCWB1/SUPBCWB2 zonal supply limits, so B1 and B2 candidate ratios to their own limits are identical by construction.
- The national supply-curve tier caps are rest-of-Canada RSYC-only; national comparisons that include BC are a context screen, not a like-for-like capacity test.
- Process residue is facility-assigned by receiving facility province; its provincial distribution differs from the province-basis national residue curve even though the national 119m totals reconcile.
- Harvest residue is province-only gross residue multiplied by a recovery fraction; it is never facility-assigned.
- Process and harvest residue are separate streams and are never summed.
- Candidate activity limits are read-only screening values; they are not applied to any OSeCAN technology, region, or input file.
- Official zone-specific limits exist only for SUPBCWB1 and SUPBCWB2; other zones have no official zone-specific activity limit in the adopted curve.
- Supply-curve and 2050 OSeCAN values are context, not policy targets, and the comparison is not a capacity-adequacy or sustainability test.
- No UI or public OSeCAN surface is changed by this artifact.

## Reproduction and verification

```bash
.venv/bin/python -m workflows.national.facilities.forestry_osecan_scenarios_v7
.venv/bin/python -m pytest tests/test_forestry_osecan_scenarios_v7.py -q
```

Validation: True; failed checks: 0. OSeCAN tree hash unchanged: True.

## Frozen v3.2 versus E2c tier positions

| Scenario | Stream | Case | v3.2 v7 PJ | E2c v8 PJ | v3.2 tier | E2c tier | Changed |
|---|---|---|---:|---:|---|---|---|
| 100m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 100m | process | process_availability_025 | 106.178019 | 104.809505 | T2 | T2 | False |
| 100m | process | process_availability_050 | 212.356037 | 209.619009 | T4 | T4 | False |
| 100m | process | process_availability_075 | 318.534056 | 314.428514 | above_T4 | above_T4 | False |
| 100m | harvest | harvest_recovery_035 | 114.918902 | 130.635373 | T3 | T3 | False |
| 100m | harvest | harvest_recovery_060 | 197.003831 | 223.946354 | T4 | above_T4 | True |
| 100m | harvest | harvest_recovery_075 | 246.254789 | 279.932942 | above_T4 | above_T4 | False |
| 119m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 119m | process | process_availability_025 | 126.333239 | 124.687729 | T3 | T3 | False |
| 119m | process | process_availability_050 | 252.666479 | 249.375458 | above_T4 | above_T4 | False |
| 119m | process | process_availability_075 | 378.999718 | 374.063188 | above_T4 | above_T4 | False |
| 119m | harvest | harvest_recovery_035 | 136.646218 | 155.543768 | T3 | T4 | True |
| 119m | harvest | harvest_recovery_060 | 234.250660 | 266.646460 | above_T4 | above_T4 | False |
| 119m | harvest | harvest_recovery_075 | 292.813324 | 333.308075 | above_T4 | above_T4 | False |
| 150m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 150m | process | process_availability_025 | 159.034676 | 156.716305 | T4 | T4 | False |
| 150m | process | process_availability_050 | 318.069352 | 313.432610 | above_T4 | above_T4 | False |
| 150m | process | process_availability_075 | 477.104027 | 470.148915 | above_T4 | above_T4 | False |
| 150m | harvest | harvest_recovery_035 | 173.190515 | 200.593895 | T4 | T4 | False |
| 150m | harvest | harvest_recovery_060 | 296.898025 | 343.875248 | above_T4 | above_T4 | False |
| 150m | harvest | harvest_recovery_075 | 371.122531 | 429.844060 | above_T4 | above_T4 | False |
