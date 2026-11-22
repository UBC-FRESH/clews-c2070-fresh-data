# Forestry Residue Handoff to OSeCAN v4

This is a read-only forestry-side screening handoff from `national_residue_curve_v3` province/case totals to every OSeCAN zone. Version 4 preserves the all-zone v2 proxy weights and refreshes the province/case totals from the assignment-v6 residue curve. It is not an official OSeCAN result, an operating plan, or a policy target.

All values are model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`, and `official_osecan_changed=false`. Process and harvest residue remain separate streams and are never summed into a combined row.

## Zone weight method

The allocation hierarchy is: OSeCAN zonal supply dispatch; OSeCAN zonal dispatch activity; operable-area weights where a defensible ecoprovince-to-zone mapping exists; otherwise an explicit equal split. No observed sub-provincial residue split is available, so every multi-zone allocation is labelled `proxy_share=true`.

| Province | Zone | Weight | Method | Evidence tier | Source value | Unit |
|---|---|---:|---|---|---:|---|
| BC | B1 | 0.082839 | osecan_zonal_supply_dispatch | tier_1_osecan_zonal_supply_model | 3.605470 | PJ_2050_supply |
| BC | B2 | 0.917161 | osecan_zonal_supply_dispatch | tier_1_osecan_zonal_supply_model | 39.918300 | PJ_2050_supply |
| AB | A1 | 0.643794 | osecan_zonal_dispatch_proxy | tier_2_osecan_zonal_dispatch_model | 7.160096 | PJ_2050_dispatch |
| AB | A2 | 0.356206 | osecan_zonal_dispatch_proxy | tier_2_osecan_zonal_dispatch_model | 3.961619 | PJ_2050_dispatch |
| SK | S1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| MB | M1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| ON | O1 | 0.833225 | osecan_zonal_dispatch_proxy | tier_2_osecan_zonal_dispatch_model | 1.091346 | PJ_2050_dispatch |
| ON | O2 | 0.166775 | osecan_zonal_dispatch_proxy | tier_2_osecan_zonal_dispatch_model | 0.218439 | PJ_2050_dispatch |
| QC | Q1 | 0.610703 | osecan_zonal_dispatch_proxy | tier_2_osecan_zonal_dispatch_model | 3.381588 | PJ_2050_dispatch |
| QC | Q2 | 0.389297 | osecan_zonal_dispatch_proxy | tier_2_osecan_zonal_dispatch_model | 2.155621 | PJ_2050_dispatch |
| NB | T1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| NS | T1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| PE | T1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| NL | L1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| YT | N1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| NT | N1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |
| NU | N1 | 1.000000 | single_zone_crosswalk | tier_0_crosswalk_membership | 1.000000 | unit_weight |

Single-zone jurisdictions use their code-defined crosswalk membership with weight 1.0. BC uses OSeCAN `SUPBCWB1`/`SUPBCWB2` 2050 supply. AB, ON, and QC use OSeCAN `PWRBCW<zone>` 2050 dispatch because OSeCAN has no zone-specific supply row for those provinces. Those dispatch shares are zonal activity proxies, not harvest observations.

## Handoff by zone

| Zone | Process 0% | Process 25% | Process 50% | Process 75% | Harvest 35% | Harvest 60% | Harvest 75% |
|---|---:|---:|---:|---:|---:|---:|---:|
| B1 | 0.000 | 3.784 | 7.568 | 11.352 | 1.635 | 2.802 | 3.503 |
| B2 | 0.000 | 41.896 | 83.792 | 125.688 | 18.097 | 31.024 | 38.780 |
| A1 | 0.000 | 17.201 | 34.402 | 51.603 | 7.274 | 12.469 | 15.587 |
| A2 | 0.000 | 9.517 | 19.034 | 28.551 | 4.025 | 6.899 | 8.624 |
| S1 | 0.000 | 3.161 | 6.323 | 9.484 | 2.144 | 3.676 | 4.595 |
| M1 | 0.000 | 0.857 | 1.714 | 2.571 | 0.560 | 0.961 | 1.201 |
| O1 | 0.000 | 11.902 | 23.804 | 35.707 | 5.549 | 9.513 | 11.891 |
| O2 | 0.000 | 2.382 | 4.765 | 7.147 | 1.111 | 1.904 | 2.380 |
| Q1 | 0.000 | 18.810 | 37.620 | 56.429 | 8.040 | 13.783 | 17.229 |
| Q2 | 0.000 | 11.990 | 23.981 | 35.971 | 5.125 | 8.786 | 10.983 |
| T1 | 0.000 | 9.394 | 18.787 | 28.181 | 4.405 | 7.552 | 9.440 |
| L1 | 0.000 | 0.575 | 1.150 | 1.725 | 0.718 | 1.230 | 1.538 |
| N1 | 0.000 | 0.032 | 0.064 | 0.096 | 0.040 | 0.068 | 0.085 |

National totals (PJ):

| Stream | Case | PJ |
|---|---|---:|
| process | `process_availability_000` | 0.000000 |
| process | `process_availability_025` | 131.501392 |
| process | `process_availability_050` | 263.002784 |
| process | `process_availability_075` | 394.504175 |
| harvest | `harvest_recovery_035` | 58.722480 |
| harvest | `harvest_recovery_060` | 100.667108 |
| harvest | `harvest_recovery_075` | 125.833885 |

## Supply-curve comparison

Ratios are case PJ divided by the reference. Headroom is reference minus case; a negative headroom means the case exceeds the reference. The 2050 values are context, not policy targets. Zone 2050 context uses OSeCAN zone dispatch activity and is undefined where that activity is zero.

### National

| Case | PJ | Tier | T1 headroom | T2 headroom | T3 headroom | T4 headroom | 2050 context ratio | 2050 context headroom |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | T1 | 85.007 | 109.399 | 149.273 | 213.538 | 0.000 | 152.923 |
| `process_availability_025` | 131.501 | T3 | -46.494 | -22.103 | 17.771 | 82.037 | 0.860 | 21.421 |
| `process_availability_050` | 263.003 | above_T4 | -177.996 | -153.604 | -113.730 | -49.465 | 1.720 | -110.080 |
| `process_availability_075` | 394.504 | above_T4 | -309.497 | -285.105 | -245.232 | -180.966 | 2.580 | -241.581 |
| `harvest_recovery_035` | 58.722 | T1 | 26.285 | 50.676 | 90.550 | 154.816 | 0.384 | 94.200 |
| `harvest_recovery_060` | 100.667 | T2 | -15.660 | 8.732 | 48.605 | 112.871 | 0.658 | 52.256 |
| `harvest_recovery_075` | 125.834 | T3 | -40.827 | -16.435 | 23.439 | 87.704 | 0.823 | 27.089 |

### BC

| Case | PJ | BC zonal cap ratio | BC zonal headroom | 2050 BC context ratio | 2050 BC context headroom |
|---|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | 0.000 | 43.524 | 0.000 | 43.524 |
| `process_availability_025` | 45.680 | 1.050 | -2.156 | 1.050 | -2.156 |
| `process_availability_050` | 91.360 | 2.099 | -47.836 | 2.099 | -47.836 |
| `process_availability_075` | 137.040 | 3.149 | -93.516 | 3.149 | -93.516 |
| `harvest_recovery_035` | 19.732 | 0.453 | 23.792 | 0.453 | 23.792 |
| `harvest_recovery_060` | 33.826 | 0.777 | 9.698 | 0.777 | 9.698 |
| `harvest_recovery_075` | 42.283 | 0.971 | 1.241 | 0.971 | 1.241 |

### Zone 2050 context

This table is context only. The reference is 2050 OSeCAN zone dispatch activity, not a zone supply cap and not a policy target. A blank ratio means the reference is zero.

| Zone | Reference PJ | Process 50% ratio | Harvest 60% ratio |
|---|---:|---:|---:|
| B1 | 0.969 | 7.809 | 2.891 |
| B2 | 10.731 | 7.809 | 2.891 |
| A1 | 7.160 | 4.805 | 1.742 |
| A2 | 3.962 | 4.805 | 1.742 |
| S1 | 5.859 | 1.079 | 0.627 |
| M1 | 1.385 | 1.237 | 0.693 |
| O1 | 1.091 | 21.812 | 8.717 |
| O2 | 0.218 | 21.812 | 8.717 |
| Q1 | 3.382 | 11.125 | 4.076 |
| Q2 | 2.156 | 11.125 | 4.076 |
| T1 | 3.694 | 5.086 | 2.044 |
| L1 | 0.501 | 2.294 | 2.455 |
| N1 | 0.000 | — | — |

## Proxy and uncertainty

4 provinces are allocated across two zones each and 9 provinces use a single zone. Every multi-zone weight is a proxy, not an observed share. The same province-level shares are applied to process and harvest residue; no stream-specific sub-provincial evidence is available.

- BC shares use 2050 OSeCAN zonal supply dispatch (`SUPBCWB1`/`SUPBCWB2`).
- AB, ON, and QC shares use 2050 OSeCAN zonal dispatch (`PWRBCW<zone>`); this is zonal energy activity, not harvest volume.
- Operable-area weights were considered for BC using the crosswalk B1 ecoprovince definition; they were not activated because zonal supply dispatch is available.
- No defensible ecoprovince-to-zone mapping exists for A1/A2, O1/O2, or Q1/Q2 in the published crosswalk, so operable-area weights were not applied there.
- Equal split was implemented as the final fallback but was not activated because dispatch weights are positive.
- Zone shares are stable across all process and harvest cases; only the province total changes by case.

## Caveats

- Zone allocation is screening-only; no published sub-provincial residue polygon or observed split is used.
- Process residue is facility-province based; harvest residue is origin-province based. They are separate and not summed.
- Process rows use the `TOTAL` class row only; harvest rows use the `ALL` row only.
- SUPBCW technology strings are candidate mappings, not operating assignments or official OSeCAN technology choices.
- The 2050 OSeCAN national (152.923 PJ) and BC (43.524 PJ) values are model context, not policy targets.
- The 213.54 PJ national supply-curve top is an adopted model bound, not a policy target.
- No transport, cost, revenue, capacity-expansion, tenure, AAC, or policy claim is made.
- No UI or public OSeCAN surface is changed.

## Validation and status

Build status: `pass`. Validation checks: 20, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.forestry_osecan_handoff_v4` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_forestry_osecan_handoff_v4.py -q` to run the regression tests.

No policy/AAC claim is made.
