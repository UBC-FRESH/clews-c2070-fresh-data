# Forestry Residue Scenarios to OSeCAN Zones v6 (E1+E2)

Status: **pass**. Artifact version `6.0.0`; generated 2026-11-23T04:04:34+00:00.

This is a read-only, model-estimate screening handoff. Every row is `model_estimate=true`, `observed=false`, `policy_grade=false`, and `official_osecan_changed=false`. No official OSeCAN input is written or modified.

## Method

1. Read province process residue (sum of facility classes) and gross harvest residue from `national_facility_chain_scenarios_v6`.
2. Apply the seven availability/recovery fractions from `national_residue_curve_v6` to each scenario total.
3. Split each province/case PJ total across all 13 OSeCAN zones with the published `forestry_osecan_handoff_v7` weights; the floating residual is assigned to the last zone so province totals are exactly conserved.
4. Compare national, BC, and zone totals with the adopted SUPBCW tier caps, the SUPBCWB1/SUPBCWB2 2050 zonal activity limits, and the 2050 OSeCAN stress_119m context. These references are context, not policy targets.
5. Emit a candidate activity-limit table for screening only. It is not applied to OSeCAN.

## National scenario/case PJ

| Scenario | Stream | Availability case | PJ | ODT |
|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | 0 |
| 100m | process | process_availability_025 | 106.18 | 5,739,352 |
| 100m | process | process_availability_050 | 212.36 | 11,478,705 |
| 100m | process | process_availability_075 | 318.53 | 17,218,057 |
| 100m | harvest | harvest_recovery_035 | 114.92 | 6,211,833 |
| 100m | harvest | harvest_recovery_060 | 197.00 | 10,648,856 |
| 100m | harvest | harvest_recovery_075 | 246.25 | 13,311,070 |
| 119m | process | process_availability_000 | 0.00 | 0 |
| 119m | process | process_availability_025 | 126.33 | 6,828,824 |
| 119m | process | process_availability_050 | 252.67 | 13,657,648 |
| 119m | process | process_availability_075 | 379.00 | 20,486,471 |
| 119m | harvest | harvest_recovery_035 | 136.65 | 7,386,282 |
| 119m | harvest | harvest_recovery_060 | 234.25 | 12,662,198 |
| 119m | harvest | harvest_recovery_075 | 292.81 | 15,827,747 |
| 150m | process | process_availability_000 | 0.00 | 0 |
| 150m | process | process_availability_025 | 159.03 | 8,596,469 |
| 150m | process | process_availability_050 | 318.07 | 17,192,938 |
| 150m | process | process_availability_075 | 477.10 | 25,789,407 |
| 150m | harvest | harvest_recovery_035 | 173.19 | 9,361,649 |
| 150m | harvest | harvest_recovery_060 | 296.90 | 16,048,542 |
| 150m | harvest | harvest_recovery_075 | 371.12 | 20,060,677 |

Process and harvest streams are separate and are never summed. The 119m rows reproduce `national_residue_curve_v6` exactly at the national level.

## Zone summary at the primary 119m scenario

| Zone | Zone name | Process 50% PJ | Process share | Harvest 60% PJ | Harvest share | Technology suggestion |
|---|---|---|---|---|---|---|
| B1 | South Coast / Lower Mainland | 7.23 | 2.9% | 5.94 | 2.5% | SUPBCWB1 |
| B2 | Interior & North | 80.00 | 31.7% | 65.78 | 28.1% | SUPBCWB2 |
| A1 | Calgary–Edmonton corridor | 31.35 | 12.4% | 21.68 | 9.3% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | North (oil sands) | 17.34 | 6.9% | 11.99 | 5.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | Saskatchewan | 9.09 | 3.6% | 8.14 | 3.5% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | Manitoba | 2.42 | 1.0% | 2.75 | 1.2% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | Southern Ontario | 23.49 | 9.3% | 25.92 | 11.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | Northern Ontario | 4.70 | 1.9% | 5.19 | 2.2% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | Southern Quebec | 33.60 | 13.3% | 39.33 | 16.8% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | Northern Quebec (hydro) | 21.42 | 8.5% | 25.07 | 10.7% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | Atlantic | 18.74 | 7.4% | 18.72 | 8.0% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | Newfoundland & Labrador | 3.12 | 1.2% | 3.55 | 1.5% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | North (territories) | 0.17 | 0.1% | 0.20 | 0.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Candidate activity-limit table

`candidate_activity_limits.csv` is read-only and not applied. Grain: scenario x stream x availability case x zone. Columns include `candidate_activity_limit_pj`, `candidate_activity_limit_odt`, `technology_suggestion`, `official_limit_reference`, `official_limit_pj`, `candidate_ratio_to_official_limit`, and `candidate_headroom_pj`. `candidate_status` is always `read_only_candidate_not_applied`.

| Zone | Scenario | Stream | Case | Candidate PJ | Technology suggestion |
|---|---|---|---|---|---|
| B1 | 119m | process | process_availability_050 | 7.23 | SUPBCWB1 |
| B1 | 119m | harvest | harvest_recovery_060 | 5.94 | SUPBCWB1 |
| B2 | 119m | process | process_availability_050 | 80.00 | SUPBCWB2 |
| B2 | 119m | harvest | harvest_recovery_060 | 65.78 | SUPBCWB2 |
| A1 | 119m | process | process_availability_050 | 31.35 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A1 | 119m | harvest | harvest_recovery_060 | 21.68 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | 119m | process | process_availability_050 | 17.34 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | 119m | harvest | harvest_recovery_060 | 11.99 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | 119m | process | process_availability_050 | 9.09 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | 119m | harvest | harvest_recovery_060 | 8.14 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | 119m | process | process_availability_050 | 2.42 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | 119m | harvest | harvest_recovery_060 | 2.75 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | 119m | process | process_availability_050 | 23.49 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | 119m | harvest | harvest_recovery_060 | 25.92 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | 119m | process | process_availability_050 | 4.70 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | 119m | harvest | harvest_recovery_060 | 5.19 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | 119m | process | process_availability_050 | 33.60 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | 119m | harvest | harvest_recovery_060 | 39.33 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | process | process_availability_050 | 21.42 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | harvest | harvest_recovery_060 | 25.07 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | process | process_availability_050 | 18.74 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | harvest | harvest_recovery_060 | 18.72 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | process | process_availability_050 | 3.12 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | harvest | harvest_recovery_060 | 3.55 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | process | process_availability_050 | 0.17 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | harvest | harvest_recovery_060 | 0.20 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Supply-curve and 2050 context comparison

Ratios above 1.0 mean the scenario/case PJ exceeds the reference; negative headroom is the excess. References are context only.

| Scenario | Stream | Case | National PJ | Tier | T4 ratio | 2050 national ratio | BC PJ | BC zonal ratio | BC 2050 ratio |
|---|---|---|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 100m | process | process_availability_025 | 106.18 | T2 | 0.497 | 0.694 | 36.27 | 0.833 | 0.833 |
| 100m | process | process_availability_050 | 212.36 | T4 | 0.994 | 1.389 | 72.54 | 1.667 | 1.667 |
| 100m | process | process_availability_075 | 318.53 | above_T4 | 1.492 | 2.083 | 108.81 | 2.500 | 2.500 |
| 100m | harvest | harvest_recovery_035 | 114.92 | T3 | 0.538 | 0.751 | 34.79 | 0.799 | 0.799 |
| 100m | harvest | harvest_recovery_060 | 197.00 | T4 | 0.923 | 1.288 | 59.65 | 1.370 | 1.370 |
| 100m | harvest | harvest_recovery_075 | 246.25 | above_T4 | 1.153 | 1.610 | 74.56 | 1.713 | 1.713 |
| 119m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 119m | process | process_availability_025 | 126.33 | T3 | 0.592 | 0.826 | 43.61 | 1.002 | 1.002 |
| 119m | process | process_availability_050 | 252.67 | above_T4 | 1.183 | 1.652 | 87.23 | 2.004 | 2.004 |
| 119m | process | process_availability_075 | 379.00 | above_T4 | 1.775 | 2.478 | 130.84 | 3.006 | 3.006 |
| 119m | harvest | harvest_recovery_035 | 136.65 | T3 | 0.640 | 0.894 | 41.84 | 0.961 | 0.961 |
| 119m | harvest | harvest_recovery_060 | 234.25 | above_T4 | 1.097 | 1.532 | 71.72 | 1.648 | 1.648 |
| 119m | harvest | harvest_recovery_075 | 292.81 | above_T4 | 1.371 | 1.915 | 89.65 | 2.060 | 2.060 |
| 150m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 150m | process | process_availability_025 | 159.03 | T4 | 0.745 | 1.040 | 49.33 | 1.134 | 1.134 |
| 150m | process | process_availability_050 | 318.07 | above_T4 | 1.490 | 2.080 | 98.67 | 2.267 | 2.267 |
| 150m | process | process_availability_075 | 477.10 | above_T4 | 2.234 | 3.120 | 148.00 | 3.401 | 3.401 |
| 150m | harvest | harvest_recovery_035 | 173.19 | T4 | 0.811 | 1.133 | 47.33 | 1.087 | 1.087 |
| 150m | harvest | harvest_recovery_060 | 296.90 | above_T4 | 1.390 | 1.941 | 81.13 | 1.864 | 1.864 |
| 150m | harvest | harvest_recovery_075 | 371.12 | above_T4 | 1.738 | 2.427 | 101.41 | 2.330 | 2.330 |

## Caveats

- All values are model estimates; observed=false and policy_grade=false.
- The 100/119/150 Mm3 cases are planning allocations, not legal AACs, sustainable-supply determinations, or observed harvest outcomes.
- Zone splits are explicit forestry_osecan_handoff_v7 proxy weights; no observed sub-provincial residue split exists.
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
.venv/bin/python -m workflows.national.facilities.forestry_osecan_scenarios_v6
.venv/bin/python -m pytest tests/test_forestry_osecan_scenarios_v6.py -q
```

Validation: True; failed checks: 0. OSeCAN tree hash unchanged: True.

## Prior donor-product versus E2 tier positions

| Scenario | Stream | Case | Prior v5 PJ | E2 v6 PJ | Prior tier | E2 tier | Changed |
|---|---|---|---:|---:|---|---|---|
| 100m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 100m | process | process_availability_025 | 108.107725 | 106.178019 | T2 | T2 | False |
| 100m | process | process_availability_050 | 216.215450 | 212.356037 | above_T4 | T4 | True |
| 100m | process | process_availability_075 | 324.323176 | 318.534056 | above_T4 | above_T4 | False |
| 100m | harvest | harvest_recovery_035 | 92.569590 | 114.918902 | T2 | T3 | True |
| 100m | harvest | harvest_recovery_060 | 158.690726 | 197.003831 | T4 | T4 | False |
| 100m | harvest | harvest_recovery_075 | 198.363407 | 246.254789 | T4 | above_T4 | True |
| 119m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 119m | process | process_availability_025 | 128.653504 | 126.333239 | T3 | T3 | False |
| 119m | process | process_availability_050 | 257.307008 | 252.666479 | above_T4 | above_T4 | False |
| 119m | process | process_availability_075 | 385.960511 | 378.999718 | above_T4 | above_T4 | False |
| 119m | harvest | harvest_recovery_035 | 109.774098 | 136.646218 | T3 | T3 | False |
| 119m | harvest | harvest_recovery_060 | 188.184168 | 234.250660 | T4 | above_T4 | True |
| 119m | harvest | harvest_recovery_075 | 235.230210 | 292.813324 | above_T4 | above_T4 | False |
| 150m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 150m | process | process_availability_025 | 162.315077 | 159.034676 | T4 | T4 | False |
| 150m | process | process_availability_050 | 324.630155 | 318.069352 | above_T4 | above_T4 | False |
| 150m | process | process_availability_075 | 486.945232 | 477.104027 | above_T4 | above_T4 | False |
| 150m | harvest | harvest_recovery_035 | 134.819676 | 173.190515 | T3 | T4 | True |
| 150m | harvest | harvest_recovery_060 | 231.119444 | 296.898025 | above_T4 | above_T4 | False |
| 150m | harvest | harvest_recovery_075 | 288.899306 | 371.122531 | above_T4 | above_T4 | False |
