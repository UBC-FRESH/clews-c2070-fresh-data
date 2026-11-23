# Forestry Residue Handoff to OSeCAN v5 (Measured Coefficients)

This is a read-only forestry-side screening handoff from `national_residue_curve_v4` province/case totals to every OSeCAN zone. Version 5 preserves the all-zone v2 proxy weights and refreshes the province/case totals from the measured-coefficient residue curve v4. It is not an official OSeCAN result, an operating plan, or a policy target.

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
| B1 | 0.000 | 3.733 | 7.467 | 11.200 | 0.870 | 1.492 | 1.865 |
| B2 | 0.000 | 41.334 | 82.668 | 124.003 | 9.634 | 16.515 | 20.644 |
| A1 | 0.000 | 17.181 | 34.362 | 51.542 | 7.274 | 12.469 | 15.587 |
| A2 | 0.000 | 9.506 | 19.012 | 28.518 | 4.025 | 6.899 | 8.624 |
| S1 | 0.000 | 3.161 | 6.323 | 9.484 | 2.144 | 3.676 | 4.595 |
| M1 | 0.000 | 0.857 | 1.714 | 2.571 | 0.560 | 0.961 | 1.201 |
| O1 | 0.000 | 11.903 | 23.807 | 35.710 | 5.549 | 9.513 | 11.891 |
| O2 | 0.000 | 2.383 | 4.765 | 7.148 | 1.111 | 1.904 | 2.380 |
| Q1 | 0.000 | 17.586 | 35.172 | 52.757 | 6.266 | 10.742 | 13.428 |
| Q2 | 0.000 | 11.210 | 22.420 | 33.631 | 3.995 | 6.848 | 8.560 |
| T1 | 0.000 | 9.204 | 18.407 | 27.611 | 2.553 | 4.376 | 5.470 |
| L1 | 0.000 | 0.576 | 1.151 | 1.727 | 0.718 | 1.230 | 1.538 |
| N1 | 0.000 | 0.020 | 0.040 | 0.060 | 0.053 | 0.091 | 0.113 |

National totals (PJ):

| Stream | Case | PJ |
|---|---|---:|
| process | `process_availability_000` | 0.000000 |
| process | `process_availability_025` | 128.653504 |
| process | `process_availability_050` | 257.307008 |
| process | `process_availability_075` | 385.960511 |
| harvest | `harvest_recovery_035` | 44.751081 |
| harvest | `harvest_recovery_060` | 76.716139 |
| harvest | `harvest_recovery_075` | 95.895174 |

## Supply-curve comparison

Ratios are case PJ divided by the reference. Headroom is reference minus case; a negative headroom means the case exceeds the reference. The 2050 values are context, not policy targets. Zone 2050 context uses OSeCAN zone dispatch activity and is undefined where that activity is zero.

### National

| Case | PJ | Tier | T1 headroom | T2 headroom | T3 headroom | T4 headroom | 2050 context ratio | 2050 context headroom |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | T1 | 85.007 | 109.399 | 149.273 | 213.538 | 0.000 | 152.923 |
| `process_availability_025` | 128.654 | T3 | -43.646 | -19.255 | 20.619 | 84.885 | 0.841 | 24.269 |
| `process_availability_050` | 257.307 | above_T4 | -172.300 | -147.908 | -108.034 | -43.769 | 1.683 | -104.384 |
| `process_availability_075` | 385.961 | above_T4 | -300.953 | -276.562 | -236.688 | -172.422 | 2.524 | -233.038 |
| `harvest_recovery_035` | 44.751 | T1 | 40.256 | 64.648 | 104.521 | 168.787 | 0.293 | 108.172 |
| `harvest_recovery_060` | 76.716 | T1 | 8.291 | 32.683 | 72.556 | 136.822 | 0.502 | 76.207 |
| `harvest_recovery_075` | 95.895 | T2 | -10.888 | 13.504 | 53.377 | 117.643 | 0.627 | 57.028 |

### BC

| Case | PJ | BC zonal cap ratio | BC zonal headroom | 2050 BC context ratio | 2050 BC context headroom |
|---|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | 0.000 | 43.524 | 0.000 | 43.524 |
| `process_availability_025` | 45.068 | 1.035 | -1.544 | 1.035 | -1.544 |
| `process_availability_050` | 90.135 | 2.071 | -46.611 | 2.071 | -46.611 |
| `process_availability_075` | 135.203 | 3.106 | -91.679 | 3.106 | -91.679 |
| `harvest_recovery_035` | 10.504 | 0.241 | 33.020 | 0.241 | 33.020 |
| `harvest_recovery_060` | 18.006 | 0.414 | 25.517 | 0.414 | 25.517 |
| `harvest_recovery_075` | 22.508 | 0.517 | 21.016 | 0.517 | 21.016 |

### Zone 2050 context

This table is context only. The reference is 2050 OSeCAN zone dispatch activity, not a zone supply cap and not a policy target. A blank ratio means the reference is zero.

| Zone | Reference PJ | Process 50% ratio | Harvest 60% ratio |
|---|---:|---:|---:|
| B1 | 0.969 | 7.704 | 1.539 |
| B2 | 10.731 | 7.704 | 1.539 |
| A1 | 7.160 | 4.799 | 1.742 |
| A2 | 3.962 | 4.799 | 1.742 |
| S1 | 5.859 | 1.079 | 0.627 |
| M1 | 1.385 | 1.237 | 0.693 |
| O1 | 1.091 | 21.814 | 8.717 |
| O2 | 0.218 | 21.814 | 8.717 |
| Q1 | 3.382 | 10.401 | 3.177 |
| Q2 | 2.156 | 10.401 | 3.177 |
| T1 | 3.694 | 4.983 | 1.185 |
| L1 | 0.501 | 2.297 | 2.455 |
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

Run `.venv/bin/python -m workflows.national.facilities.forestry_osecan_handoff_v5` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_forestry_osecan_handoff_v5.py -q` to run the regression tests.

No policy/AAC claim is made.
