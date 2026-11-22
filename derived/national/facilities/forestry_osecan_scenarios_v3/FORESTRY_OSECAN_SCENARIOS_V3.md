# Forestry Residue Scenarios to OSeCAN Zones v3

Status: **pass**. Artifact version `3.0.0`; generated 2026-11-22T22:34:36+00:00.

This is a read-only, model-estimate screening handoff. Every row is `model_estimate=true`, `observed=false`, `policy_grade=false`, and `official_osecan_changed=false`. No official OSeCAN input is written or modified.

## Method

1. Read province process residue (sum of facility classes) and gross harvest residue from `national_facility_chain_scenarios_v3`.
2. Apply the seven availability/recovery fractions from `national_residue_curve_v3` to each scenario total.
3. Split each province/case PJ total across all 13 OSeCAN zones with the published `forestry_osecan_handoff_v4` weights; the floating residual is assigned to the last zone so province totals are exactly conserved.
4. Compare national, BC, and zone totals with the adopted SUPBCW tier caps, the SUPBCWB1/SUPBCWB2 2050 zonal activity limits, and the 2050 OSeCAN stress_119m context. These references are context, not policy targets.
5. Emit a candidate activity-limit table for screening only. It is not applied to OSeCAN.

## National scenario/case PJ

| Scenario | Stream | Availability case | PJ | ODT |
|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | 0 |
| 100m | process | process_availability_025 | 110.53 | 5,974,401 |
| 100m | process | process_availability_050 | 221.05 | 11,948,802 |
| 100m | process | process_availability_075 | 331.58 | 17,923,203 |
| 100m | harvest | harvest_recovery_035 | 49.36 | 2,667,893 |
| 100m | harvest | harvest_recovery_060 | 84.61 | 4,573,531 |
| 100m | harvest | harvest_recovery_075 | 105.76 | 5,716,914 |
| 119m | process | process_availability_000 | 0.00 | 0 |
| 119m | process | process_availability_025 | 131.50 | 7,108,183 |
| 119m | process | process_availability_050 | 263.00 | 14,216,367 |
| 119m | process | process_availability_075 | 394.50 | 21,324,550 |
| 119m | harvest | harvest_recovery_035 | 58.72 | 3,174,188 |
| 119m | harvest | harvest_recovery_060 | 100.67 | 5,441,465 |
| 119m | harvest | harvest_recovery_075 | 125.83 | 6,801,832 |
| 150m | process | process_availability_000 | 0.00 | 0 |
| 150m | process | process_availability_025 | 165.79 | 8,961,602 |
| 150m | process | process_availability_050 | 331.58 | 17,923,203 |
| 150m | process | process_availability_075 | 497.37 | 26,884,805 |
| 150m | harvest | harvest_recovery_035 | 74.03 | 4,001,839 |
| 150m | harvest | harvest_recovery_060 | 126.92 | 6,860,296 |
| 150m | harvest | harvest_recovery_075 | 158.64 | 8,575,370 |

Process and harvest streams are separate and are never summed. The 119m rows reproduce `national_residue_curve_v3` exactly at the national level.

## Zone summary at the primary 119m scenario

| Zone | Zone name | Process 50% PJ | Process share | Harvest 60% PJ | Harvest share | Technology suggestion |
|---|---|---|---|---|---|---|
| B1 | South Coast / Lower Mainland | 7.32 | 2.8% | 2.80 | 2.8% | SUPBCWB1 |
| B2 | Interior & North | 81.05 | 30.8% | 31.02 | 30.8% | SUPBCWB2 |
| A1 | Calgary–Edmonton corridor | 32.58 | 12.4% | 12.47 | 12.4% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| A2 | North (oil sands) | 18.02 | 6.9% | 6.90 | 6.9% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| S1 | Saskatchewan | 9.60 | 3.7% | 3.68 | 3.7% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| M1 | Manitoba | 2.51 | 1.0% | 0.96 | 1.0% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O1 | Southern Ontario | 24.85 | 9.4% | 9.51 | 9.4% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| O2 | Northern Ontario | 4.97 | 1.9% | 1.90 | 1.9% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | Southern Quebec | 36.01 | 13.7% | 13.78 | 13.7% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | Northern Quebec (hydro) | 22.95 | 8.7% | 8.79 | 8.7% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | Atlantic | 19.73 | 7.5% | 7.55 | 7.5% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | Newfoundland & Labrador | 3.21 | 1.2% | 1.23 | 1.2% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | North (territories) | 0.18 | 0.1% | 0.07 | 0.1% | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Candidate activity-limit table

`candidate_activity_limits.csv` is read-only and not applied. Grain: scenario x stream x availability case x zone. Columns include `candidate_activity_limit_pj`, `candidate_activity_limit_odt`, `technology_suggestion`, `official_limit_reference`, `official_limit_pj`, `candidate_ratio_to_official_limit`, and `candidate_headroom_pj`. `candidate_status` is always `read_only_candidate_not_applied`.

| Zone | Scenario | Stream | Case | Candidate PJ | Technology suggestion |
|---|---|---|---|---|---|
| B1 | 119m | process | process_availability_050 | 7.32 | SUPBCWB1 |
| B1 | 119m | harvest | harvest_recovery_060 | 2.80 | SUPBCWB1 |
| B2 | 119m | process | process_availability_050 | 81.05 | SUPBCWB2 |
| B2 | 119m | harvest | harvest_recovery_060 | 31.02 | SUPBCWB2 |
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
| Q1 | 119m | process | process_availability_050 | 36.01 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q1 | 119m | harvest | harvest_recovery_060 | 13.78 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | process | process_availability_050 | 22.95 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| Q2 | 119m | harvest | harvest_recovery_060 | 8.79 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | process | process_availability_050 | 19.73 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| T1 | 119m | harvest | harvest_recovery_060 | 7.55 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | process | process_availability_050 | 3.21 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| L1 | 119m | harvest | harvest_recovery_060 | 1.23 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | process | process_availability_050 | 0.18 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |
| N1 | 119m | harvest | harvest_recovery_060 | 0.07 | SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4 |

## Supply-curve and 2050 context comparison

Ratios above 1.0 mean the scenario/case PJ exceeds the reference; negative headroom is the excess. References are context only.

| Scenario | Stream | Case | National PJ | Tier | T4 ratio | 2050 national ratio | BC PJ | BC zonal ratio | BC 2050 ratio |
|---|---|---|---|---|---|---|---|---|---|
| 100m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 100m | process | process_availability_025 | 110.53 | T3 | 0.518 | 0.723 | 36.75 | 0.844 | 0.844 |
| 100m | process | process_availability_050 | 221.05 | above_T4 | 1.035 | 1.446 | 73.50 | 1.689 | 1.689 |
| 100m | process | process_availability_075 | 331.58 | above_T4 | 1.553 | 2.168 | 110.25 | 2.533 | 2.533 |
| 100m | harvest | harvest_recovery_035 | 49.36 | T1 | 0.231 | 0.323 | 16.41 | 0.377 | 0.377 |
| 100m | harvest | harvest_recovery_060 | 84.61 | T1 | 0.396 | 0.553 | 28.13 | 0.646 | 0.646 |
| 100m | harvest | harvest_recovery_075 | 105.76 | T2 | 0.495 | 0.692 | 35.16 | 0.808 | 0.808 |
| 119m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 119m | process | process_availability_025 | 131.50 | T3 | 0.616 | 0.860 | 44.19 | 1.015 | 1.015 |
| 119m | process | process_availability_050 | 263.00 | above_T4 | 1.232 | 1.720 | 88.37 | 2.030 | 2.030 |
| 119m | process | process_availability_075 | 394.50 | above_T4 | 1.847 | 2.580 | 132.56 | 3.046 | 3.046 |
| 119m | harvest | harvest_recovery_035 | 58.72 | T1 | 0.275 | 0.384 | 19.73 | 0.453 | 0.453 |
| 119m | harvest | harvest_recovery_060 | 100.67 | T2 | 0.471 | 0.658 | 33.83 | 0.777 | 0.777 |
| 119m | harvest | harvest_recovery_075 | 125.83 | T3 | 0.589 | 0.823 | 42.28 | 0.971 | 0.971 |
| 150m | process | process_availability_000 | 0.00 | - | 0.000 | 0.000 | 0.00 | 0.000 | 0.000 |
| 150m | process | process_availability_025 | 165.79 | T4 | 0.776 | 1.084 | 49.98 | 1.148 | 1.148 |
| 150m | process | process_availability_050 | 331.58 | above_T4 | 1.553 | 2.168 | 99.97 | 2.297 | 2.297 |
| 150m | process | process_availability_075 | 497.37 | above_T4 | 2.329 | 3.252 | 149.95 | 3.445 | 3.445 |
| 150m | harvest | harvest_recovery_035 | 74.03 | T1 | 0.347 | 0.484 | 22.32 | 0.513 | 0.513 |
| 150m | harvest | harvest_recovery_060 | 126.92 | T3 | 0.594 | 0.830 | 38.26 | 0.879 | 0.879 |
| 150m | harvest | harvest_recovery_075 | 158.64 | T4 | 0.743 | 1.037 | 47.83 | 1.099 | 1.099 |

## Caveats

- All values are model estimates; observed=false and policy_grade=false.
- The 100/119/150 Mm3 cases are planning allocations, not legal AACs, sustainable-supply determinations, or observed harvest outcomes.
- Zone splits are explicit forestry_osecan_handoff_v4 proxy weights; no observed sub-provincial residue split exists.
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
.venv/bin/python -m workflows.national.facilities.forestry_osecan_scenarios_v3
.venv/bin/python -m pytest tests/test_forestry_osecan_scenarios_v3.py -q
```

Validation: True; failed checks: 0. OSeCAN tree hash unchanged: True.
