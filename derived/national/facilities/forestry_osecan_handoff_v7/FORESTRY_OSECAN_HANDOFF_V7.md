# Forestry Residue Handoff to OSeCAN v7 (E1+E2)

This is a read-only forestry-side screening handoff from `national_residue_curve_v6` province/case totals to every OSeCAN zone. Version 7 preserves the all-zone v2 proxy weights and refreshes the province/case totals from the E1+E2 residue curve v6. It is not an official OSeCAN result, an operating plan, or a policy target.

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
| B1 | 0.000 | 3.721 | 7.443 | 11.164 | 3.466 | 5.941 | 7.427 |
| B2 | 0.000 | 41.200 | 82.400 | 123.601 | 38.372 | 65.780 | 82.225 |
| A1 | 0.000 | 16.665 | 33.330 | 49.995 | 12.645 | 21.678 | 27.097 |
| A2 | 0.000 | 9.221 | 18.441 | 27.662 | 6.997 | 11.994 | 14.993 |
| S1 | 0.000 | 2.162 | 4.323 | 6.485 | 4.749 | 8.141 | 10.176 |
| M1 | 0.000 | 0.663 | 1.325 | 1.988 | 1.603 | 2.748 | 3.435 |
| O1 | 0.000 | 11.577 | 23.154 | 34.732 | 15.117 | 25.915 | 32.394 |
| O2 | 0.000 | 2.317 | 4.634 | 6.952 | 3.026 | 5.187 | 6.484 |
| Q1 | 0.000 | 17.595 | 35.190 | 52.785 | 22.942 | 39.330 | 49.162 |
| Q2 | 0.000 | 11.216 | 22.432 | 33.648 | 14.625 | 25.071 | 31.339 |
| T1 | 0.000 | 9.089 | 18.179 | 27.268 | 10.919 | 18.718 | 23.397 |
| L1 | 0.000 | 0.887 | 1.775 | 2.662 | 2.068 | 3.546 | 4.432 |
| N1 | 0.000 | 0.020 | 0.040 | 0.059 | 0.118 | 0.202 | 0.252 |

National totals (PJ):

| Stream | Case | PJ |
|---|---|---:|
| process | `process_availability_000` | 0.000000 |
| process | `process_availability_025` | 126.333239 |
| process | `process_availability_050` | 252.666479 |
| process | `process_availability_075` | 378.999718 |
| harvest | `harvest_recovery_035` | 136.646218 |
| harvest | `harvest_recovery_060` | 234.250660 |
| harvest | `harvest_recovery_075` | 292.813324 |

## Supply-curve comparison

Ratios are case PJ divided by the reference. Headroom is reference minus case; a negative headroom means the case exceeds the reference. The 2050 values are context, not policy targets. Zone 2050 context uses OSeCAN zone dispatch activity and is undefined where that activity is zero.

### National

| Case | PJ | Tier | T1 headroom | T2 headroom | T3 headroom | T4 headroom | 2050 context ratio | 2050 context headroom |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | T1 | 85.007 | 109.399 | 149.273 | 213.538 | 0.000 | 152.923 |
| `process_availability_025` | 126.333 | T3 | -41.326 | -16.934 | 22.939 | 87.205 | 0.826 | 26.590 |
| `process_availability_050` | 252.666 | above_T4 | -167.659 | -143.268 | -103.394 | -39.128 | 1.652 | -99.744 |
| `process_availability_075` | 379.000 | above_T4 | -293.993 | -269.601 | -229.727 | -165.462 | 2.478 | -226.077 |
| `harvest_recovery_035` | 136.646 | T3 | -51.639 | -27.247 | 12.626 | 76.892 | 0.894 | 16.277 |
| `harvest_recovery_060` | 234.251 | above_T4 | -149.244 | -124.852 | -84.978 | -20.713 | 1.532 | -81.328 |
| `harvest_recovery_075` | 292.813 | above_T4 | -207.806 | -183.414 | -143.541 | -79.275 | 1.915 | -139.891 |

### BC

| Case | PJ | BC zonal cap ratio | BC zonal headroom | 2050 BC context ratio | 2050 BC context headroom |
|---|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | 0.000 | 43.524 | 0.000 | 43.524 |
| `process_availability_025` | 44.921 | 1.032 | -1.398 | 1.032 | -1.398 |
| `process_availability_050` | 89.843 | 2.064 | -46.319 | 2.064 | -46.319 |
| `process_availability_075` | 134.764 | 3.096 | -91.240 | 3.096 | -91.241 |
| `harvest_recovery_035` | 41.838 | 0.961 | 1.686 | 0.961 | 1.686 |
| `harvest_recovery_060` | 71.722 | 1.648 | -28.198 | 1.648 | -28.198 |
| `harvest_recovery_075` | 89.652 | 2.060 | -46.128 | 2.060 | -46.128 |

### Zone 2050 context

This table is context only. The reference is 2050 OSeCAN zone dispatch activity, not a zone supply cap and not a policy target. A blank ratio means the reference is zero.

| Zone | Reference PJ | Process 50% ratio | Harvest 60% ratio |
|---|---:|---:|---:|
| B1 | 0.969 | 7.679 | 6.130 |
| B2 | 10.731 | 7.679 | 6.130 |
| A1 | 7.160 | 4.655 | 3.028 |
| A2 | 3.962 | 4.655 | 3.028 |
| S1 | 5.859 | 0.738 | 1.389 |
| M1 | 1.385 | 0.956 | 1.983 |
| O1 | 1.091 | 21.216 | 23.746 |
| O2 | 0.218 | 21.216 | 23.746 |
| Q1 | 3.382 | 10.406 | 11.631 |
| Q2 | 2.156 | 10.406 | 11.631 |
| T1 | 3.694 | 4.921 | 5.067 |
| L1 | 0.501 | 3.541 | 7.075 |
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

Run `.venv/bin/python -m workflows.national.facilities.forestry_osecan_handoff_v7` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_forestry_osecan_handoff_v7.py -q` to run the regression tests.

No policy/AAC claim is made.

## Stem-only versus total residue tier positions

| Stream | Case | Stem-only v5 | Total residue v6 | Changed |
|---|---|---|---|---|
| harvest | harvest_recovery_035 | T1 | T3 | True |
| harvest | harvest_recovery_060 | T1 | above_T4 | True |
| harvest | harvest_recovery_075 | T2 | above_T4 | True |
| process | process_availability_000 | T1 | T1 | False |
| process | process_availability_025 | T3 | T3 | False |
| process | process_availability_050 | above_T4 | above_T4 | False |
| process | process_availability_075 | above_T4 | above_T4 | False |

## Prior donor-product versus E2 tier positions

| Stream | Case | Donor product v6 | E2 v7 | Changed |
|---|---|---|---|---|
| harvest | harvest_recovery_035 | T3 | T3 | False |
| harvest | harvest_recovery_060 | T4 | above_T4 | True |
| harvest | harvest_recovery_075 | above_T4 | above_T4 | False |
| process | process_availability_000 | T1 | T1 | False |
| process | process_availability_025 | T3 | T3 | False |
| process | process_availability_050 | above_T4 | above_T4 | False |
| process | process_availability_075 | above_T4 | above_T4 | False |
