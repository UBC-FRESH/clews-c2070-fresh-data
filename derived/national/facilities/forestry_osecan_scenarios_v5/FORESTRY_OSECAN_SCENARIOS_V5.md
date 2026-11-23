# Forestry Residue Scenarios to OSeCAN Zones v5 (Total Residue)

Status: **pass**. Artifact version `5.0.0`; generated 2026-11-23T02:00:06+00:00.

This is a read-only, model-estimate screening handoff. Every row is `model_estimate=true`, `observed=false`, `policy_grade=false`, and `official_osecan_changed=false`. No official OSeCAN input is written or modified.

## Method

1. Read province process residue (sum of facility classes) and gross harvest residue from `national_facility_chain_scenarios_v5`.
2. Apply the seven availability/recovery fractions from `national_residue_curve_v5` to each scenario total.
3. Split each province/case PJ total across all 13 OSeCAN zones with the published `forestry_osecan_handoff_v6` weights; the floating residual is assigned to the last zone so province totals are exactly conserved.
4. Compare national, BC, and zone totals with the adopted SUPBCW tier caps, the SUPBCWB1/SUPBCWB2 2050 zonal activity limits, and the 2050 OSeCAN stress_119m context. These references are context, not policy targets.
5. Emit a candidate activity-limit table for screening only. It is not applied to OSeCAN.

## National scenario/case PJ

| Scenario | Stream | Availability case | PJ | ODT |
|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | 0 |
| 100m | process | process_availability_025 | 108.11 | 5,843,661 |
| 100m | process | process_availability_050 | 216.22 | 11,687,322 |
| 100m | process | process_availability_075 | 324.32 | 17,530,982 |
| 100m | harvest | harvest_recovery_035 | 92.57 | 5,003,762 |
| 100m | harvest | harvest_recovery_060 | 158.69 | 8,577,877 |
| 100m | harvest | harvest_recovery_075 | 198.36 | 10,722,346 |
| 119m | process | process_availability_000 | 0.00 | 0 |
| 119m | process | process_availability_025 | 128.65 | 6,954,243 |
| 119m | process | process_availability_050 | 257.31 | 13,908,487 |
| 119m | process | process_availability_075 | 385.96 | 20,862,730 |
| 119m | harvest | harvest_recovery_035 | 109.77 | 5,933,735 |
| 119m | harvest | harvest_recovery_060 | 188.18 | 10,172,117 |
| 119m | harvest | harvest_recovery_075 | 235.23 | 12,715,146 |
| 150m | process | process_availability_000 | 0.00 | 0 |
| 150m | process | process_availability_025 | 162.32 | 8,773,788 |
| 150m | process | process_availability_050 | 324.63 | 17,547,576 |
| 150m | process | process_availability_075 | 486.95 | 26,321,364 |
| 150m | harvest | harvest_recovery_035 | 134.82 | 7,287,550 |
| 150m | harvest | harvest_recovery_060 | 231.12 | 12,492,943 |
| 150m | harvest | harvest_recovery_075 | 288.90 | 15,616,179 |

Process and harvest streams are separate and are never summed. The 119m rows reproduce `national_residue_curve_v5` exactly at the national level.

## Zone summary at the primary 119m scenario

| Zone | Zone name | Process 50% PJ | Process share | Harvest 60% PJ | Harvest share | Technology suggestion |
|---|---|---|---|---|---|---|
| B1 | South Coast / Lower Mainland | 7.23 | 2.8% | 5.94 | 3.2% | SUPBCWB1 |
| B2 | Interior & North | 80.00 | 31.1% | 65.78 | 35.0% | SUPBCWB2 |
| A1 | Calgary–Edmonton corridor | 32.58 | 12.7% | 12.47 | 6.6% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | North (oil sands) | 18.02 | 7.0% | 6.90 | 3.7% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | Saskatchewan | 9.60 | 3.7% | 3.68 | 2.0% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | Manitoba | 2.51 | 1.0% | 0.96 | 0.5% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | Southern Ontario | 24.85 | 9.7% | 9.51 | 5.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | Northern Ontario | 4.97 | 1.9% | 1.90 | 1.0% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | Southern Quebec | 33.60 | 13.1% | 39.33 | 20.9% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | Northern Quebec (hydro) | 21.42 | 8.3% | 25.07 | 13.3% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | Atlantic | 19.13 | 7.4% | 15.25 | 8.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | Newfoundland & Labrador | 3.21 | 1.2% | 1.23 | 0.7% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | North (territories) | 0.17 | 0.1% | 0.16 | 0.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Candidate activity-limit table

`candidate_activity_limits.csv` is read-only and not applied. Grain: scenario x stream x availability case x zone. Columns include `candidate_activity_limit_pj`, `candidate_activity_limit_odt`, `technology_suggestion`, `official_limit_reference`, `official_limit_pj`, `candidate_ratio_to_official_limit`, and `candidate_headroom_pj`. `candidate_status` is always `read_only_candidate_not_applied`.

| Zone | Scenario | Stream | Case | Candidate PJ | Technology suggestion |
|---|---|---|---|---|---|
| B1 | 119m | process | process_availability_050 | 7.23 | SUPBCWB1 |
| B1 | 119m | harvest | harvest_recovery_060 | 5.94 | SUPBCWB1 |
| B2 | 119m | process | process_availability_050 | 80.00 | SUPBCWB2 |
| B2 | 119m | harvest | harvest_recovery_060 | 65.78 | SUPBCWB2 |
| A1 | 119m | process | process_availability_050 | 32.58 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A1 | 119m | harvest | harvest_recovery_060 | 12.47 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | 119m | process | process_availability_050 | 18.02 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | 119m | harvest | harvest_recovery_060 | 6.90 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | 119m | process | process_availability_050 | 9.60 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | 119m | harvest | harvest_recovery_060 | 3.68 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | 119m | process | process_availability_050 | 2.51 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | 119m | harvest | harvest_recovery_060 | 0.96 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | 119m | process | process_availability_050 | 24.85 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | 119m | harvest | harvest_recovery_060 | 9.51 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | 119m | process | process_availability_050 | 4.97 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | 119m | harvest | harvest_recovery_060 | 1.90 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | 119m | process | process_availability_050 | 33.60 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | 119m | harvest | harvest_recovery_060 | 39.33 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | process | process_availability_050 | 21.42 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | harvest | harvest_recovery_060 | 25.07 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | process | process_availability_050 | 19.13 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | harvest | harvest_recovery_060 | 15.25 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | process | process_availability_050 | 3.21 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | harvest | harvest_recovery_060 | 1.23 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | process | process_availability_050 | 0.17 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | harvest | harvest_recovery_060 | 0.16 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Supply-curve and 2050 context comparison

Ratios above 1.0 mean the scenario/case PJ exceeds the reference; negative headroom is the excess. References are context only.

| Scenario | Stream | Case | National PJ | Tier | T4 ratio | 2050 national ratio | BC PJ | BC zonal ratio | BC 2050 ratio |
|---|---|---|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 100m | process | process_availability_025 | 108.11 | T2 | 0.506 | 0.707 | 36.27 | 0.833 | 0.833 |
| 100m | process | process_availability_050 | 216.22 | above_T4 | 1.013 | 1.414 | 72.54 | 1.667 | 1.667 |
| 100m | process | process_availability_075 | 324.32 | above_T4 | 1.519 | 2.121 | 108.81 | 2.500 | 2.500 |
| 100m | harvest | harvest_recovery_035 | 92.57 | T2 | 0.434 | 0.605 | 34.79 | 0.799 | 0.799 |
| 100m | harvest | harvest_recovery_060 | 158.69 | T4 | 0.743 | 1.038 | 59.65 | 1.370 | 1.370 |
| 100m | harvest | harvest_recovery_075 | 198.36 | T4 | 0.929 | 1.297 | 74.56 | 1.713 | 1.713 |
| 119m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 119m | process | process_availability_025 | 128.65 | T3 | 0.602 | 0.841 | 43.61 | 1.002 | 1.002 |
| 119m | process | process_availability_050 | 257.31 | above_T4 | 1.205 | 1.683 | 87.23 | 2.004 | 2.004 |
| 119m | process | process_availability_075 | 385.96 | above_T4 | 1.807 | 2.524 | 130.84 | 3.006 | 3.006 |
| 119m | harvest | harvest_recovery_035 | 109.77 | T3 | 0.514 | 0.718 | 41.84 | 0.961 | 0.961 |
| 119m | harvest | harvest_recovery_060 | 188.18 | T4 | 0.881 | 1.231 | 71.72 | 1.648 | 1.648 |
| 119m | harvest | harvest_recovery_075 | 235.23 | above_T4 | 1.102 | 1.538 | 89.65 | 2.060 | 2.060 |
| 150m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 150m | process | process_availability_025 | 162.32 | T4 | 0.760 | 1.061 | 49.33 | 1.134 | 1.134 |
| 150m | process | process_availability_050 | 324.63 | above_T4 | 1.520 | 2.123 | 98.67 | 2.267 | 2.267 |
| 150m | process | process_availability_075 | 486.95 | above_T4 | 2.280 | 3.184 | 148.00 | 3.401 | 3.401 |
| 150m | harvest | harvest_recovery_035 | 134.82 | T3 | 0.631 | 0.882 | 47.33 | 1.087 | 1.087 |
| 150m | harvest | harvest_recovery_060 | 231.12 | above_T4 | 1.082 | 1.511 | 81.13 | 1.864 | 1.864 |
| 150m | harvest | harvest_recovery_075 | 288.90 | above_T4 | 1.353 | 1.889 | 101.41 | 2.330 | 2.330 |

## Caveats

- All values are model estimates; observed=false and policy_grade=false.
- The 100/119/150 Mm3 cases are planning allocations, not legal AACs, sustainable-supply determinations, or observed harvest outcomes.
- Zone splits are explicit forestry_osecan_handoff_v6 proxy weights; no observed sub-provincial residue split exists.
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
.venv/bin/python -m workflows.national.facilities.forestry_osecan_scenarios_v5
.venv/bin/python -m pytest tests/test_forestry_osecan_scenarios_v5.py -q
```

Validation: True; failed checks: 0. OSeCAN tree hash unchanged: True.

## Stem-only versus total residue tier positions

| Scenario | Stream | Case | Stem v4 PJ | Total v5 PJ | Stem tier | Total tier | Changed |
|---|---|---|---:|---:|---|---|---|
| 100m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 100m | process | process_availability_025 | 108.107725 | 108.107725 | T2 | T2 | False |
| 100m | process | process_availability_050 | 216.215450 | 216.215450 | above_T4 | above_T4 | False |
| 100m | process | process_availability_075 | 324.323176 | 324.323176 | above_T4 | above_T4 | False |
| 100m | harvest | harvest_recovery_035 | 37.424673 | 92.569590 | T1 | T2 | True |
| 100m | harvest | harvest_recovery_060 | 64.156582 | 158.690726 | T1 | T4 | True |
| 100m | harvest | harvest_recovery_075 | 80.195727 | 198.363407 | T1 | T4 | True |
| 119m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 119m | process | process_availability_025 | 128.653504 | 128.653504 | T3 | T3 | False |
| 119m | process | process_availability_050 | 257.307008 | 257.307008 | above_T4 | above_T4 | False |
| 119m | process | process_availability_075 | 385.960511 | 385.960511 | above_T4 | above_T4 | False |
| 119m | harvest | harvest_recovery_035 | 44.751081 | 109.774098 | T1 | T3 | True |
| 119m | harvest | harvest_recovery_060 | 76.716139 | 188.184168 | T1 | T4 | True |
| 119m | harvest | harvest_recovery_075 | 95.895174 | 235.230210 | T2 | above_T4 | True |
| 150m | process | process_availability_000 | 0.000000 | 0.000000 | T1 | T1 | False |
| 150m | process | process_availability_025 | 162.315077 | 162.315077 | T4 | T4 | False |
| 150m | process | process_availability_050 | 324.630155 | 324.630155 | above_T4 | above_T4 | False |
| 150m | process | process_availability_075 | 486.945232 | 486.945232 | above_T4 | above_T4 | False |
| 150m | harvest | harvest_recovery_035 | 58.048199 | 134.819676 | T1 | T3 | True |
| 150m | harvest | harvest_recovery_060 | 99.511199 | 231.119444 | T2 | above_T4 | True |
| 150m | harvest | harvest_recovery_075 | 124.388999 | 288.899306 | T3 | above_T4 | True |
