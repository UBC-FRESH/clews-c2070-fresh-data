# Forestry Residue Handoff to OSeCAN v8 (E1+E2c)

This is a read-only forestry-side screening handoff from `national_residue_curve_v7` province/case totals to every OSeCAN zone. Version 8 preserves the all-zone v2 proxy weights and refreshes the province/case totals from the E1+E2c residue curve v7. It is not an official OSeCAN result, an operating plan, or a policy target.

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
| B1 | 0.000 | 3.757 | 7.514 | 11.271 | 3.466 | 5.941 | 7.427 |
| B2 | 0.000 | 41.595 | 83.191 | 124.786 | 38.372 | 65.780 | 82.225 |
| A1 | 0.000 | 16.357 | 32.714 | 49.072 | 15.245 | 26.135 | 32.669 |
| A2 | 0.000 | 9.050 | 18.101 | 27.151 | 8.435 | 14.460 | 18.075 |
| S1 | 0.000 | 0.054 | 0.107 | 0.161 | 17.861 | 30.619 | 38.273 |
| M1 | 0.000 | 0.522 | 1.044 | 1.565 | 1.426 | 2.444 | 3.055 |
| O1 | 0.000 | 11.691 | 23.383 | 35.074 | 15.301 | 26.231 | 32.789 |
| O2 | 0.000 | 2.340 | 4.680 | 7.020 | 3.063 | 5.250 | 6.563 |
| Q1 | 0.000 | 17.776 | 35.553 | 53.329 | 22.942 | 39.330 | 49.162 |
| Q2 | 0.000 | 11.332 | 22.663 | 33.995 | 14.625 | 25.071 | 31.339 |
| T1 | 0.000 | 9.258 | 18.516 | 27.774 | 12.616 | 21.628 | 27.035 |
| L1 | 0.000 | 0.935 | 1.871 | 2.806 | 2.073 | 3.554 | 4.442 |
| N1 | 0.000 | 0.020 | 0.040 | 0.059 | 0.118 | 0.203 | 0.254 |

National totals (PJ):

| Stream | Case | PJ |
|---|---|---:|
| process | `process_availability_000` | 0.000000 |
| process | `process_availability_025` | 124.687729 |
| process | `process_availability_050` | 249.375458 |
| process | `process_availability_075` | 374.063188 |
| harvest | `harvest_recovery_035` | 155.543768 |
| harvest | `harvest_recovery_060` | 266.646460 |
| harvest | `harvest_recovery_075` | 333.308075 |

## Supply-curve comparison

Ratios are case PJ divided by the reference. Headroom is reference minus case; a negative headroom means the case exceeds the reference. The 2050 values are context, not policy targets. Zone 2050 context uses OSeCAN zone dispatch activity and is undefined where that activity is zero.

### National

| Case | PJ | Tier | T1 headroom | T2 headroom | T3 headroom | T4 headroom | 2050 context ratio | 2050 context headroom |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | T1 | 85.007 | 109.399 | 149.273 | 213.538 | 0.000 | 152.923 |
| `process_availability_025` | 124.688 | T3 | -39.681 | -15.289 | 24.585 | 88.850 | 0.815 | 28.235 |
| `process_availability_050` | 249.375 | above_T4 | -164.368 | -139.977 | -100.103 | -35.837 | 1.631 | -96.453 |
| `process_availability_075` | 374.063 | above_T4 | -289.056 | -264.664 | -224.791 | -160.525 | 2.446 | -221.140 |
| `harvest_recovery_035` | 155.544 | T4 | -70.537 | -46.145 | -6.271 | 57.994 | 1.017 | -2.621 |
| `harvest_recovery_060` | 266.646 | above_T4 | -181.639 | -157.248 | -117.374 | -53.108 | 1.744 | -113.724 |
| `harvest_recovery_075` | 333.308 | above_T4 | -248.301 | -223.909 | -184.035 | -119.770 | 2.180 | -180.385 |

### BC

| Case | PJ | BC zonal cap ratio | BC zonal headroom | 2050 BC context ratio | 2050 BC context headroom |
|---|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | 0.000 | 43.524 | 0.000 | 43.524 |
| `process_availability_025` | 45.352 | 1.042 | -1.829 | 1.042 | -1.829 |
| `process_availability_050` | 90.705 | 2.084 | -47.181 | 2.084 | -47.181 |
| `process_availability_075` | 136.057 | 3.126 | -92.533 | 3.126 | -92.533 |
| `harvest_recovery_035` | 41.838 | 0.961 | 1.686 | 0.961 | 1.686 |
| `harvest_recovery_060` | 71.722 | 1.648 | -28.198 | 1.648 | -28.198 |
| `harvest_recovery_075` | 89.652 | 2.060 | -46.128 | 2.060 | -46.128 |

### Zone 2050 context

This table is context only. The reference is 2050 OSeCAN zone dispatch activity, not a zone supply cap and not a policy target. A blank ratio means the reference is zero.

| Zone | Reference PJ | Process 50% ratio | Harvest 60% ratio |
|---|---:|---:|---:|
| B1 | 0.969 | 7.753 | 6.130 |
| B2 | 10.731 | 7.753 | 6.130 |
| A1 | 7.160 | 4.569 | 3.650 |
| A2 | 3.962 | 4.569 | 3.650 |
| S1 | 5.859 | 0.018 | 5.226 |
| M1 | 1.385 | 0.753 | 1.764 |
| O1 | 1.091 | 21.426 | 24.035 |
| O2 | 0.218 | 21.426 | 24.035 |
| Q1 | 3.382 | 10.514 | 11.631 |
| Q2 | 2.156 | 10.514 | 11.631 |
| T1 | 3.694 | 5.012 | 5.855 |
| L1 | 0.501 | 3.732 | 7.091 |
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

Run `.venv/bin/python -m workflows.national.facilities.forestry_osecan_handoff_v8` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_forestry_osecan_handoff_v8.py -q` to run the regression tests.

No policy/AAC claim is made.

## Stem-only versus total residue tier positions

| Stream | Case | Stem-only v5 | Total residue v6 | Changed |
|---|---|---|---|---|
| harvest | harvest_recovery_035 | T1 | T4 | True |
| harvest | harvest_recovery_060 | T1 | above_T4 | True |
| harvest | harvest_recovery_075 | T2 | above_T4 | True |
| process | process_availability_000 | T1 | T1 | False |
| process | process_availability_025 | T3 | T3 | False |
| process | process_availability_050 | above_T4 | above_T4 | False |
| process | process_availability_075 | above_T4 | above_T4 | False |

## Prior donor-product versus E2 tier positions

| Stream | Case | Donor product v6 | E2c v8 | Changed |
|---|---|---|---|---|
| harvest | harvest_recovery_035 | T3 | T4 | True |
| harvest | harvest_recovery_060 | above_T4 | above_T4 | False |
| harvest | harvest_recovery_075 | above_T4 | above_T4 | False |
| process | process_availability_000 | T1 | T1 | False |
| process | process_availability_025 | T3 | T3 | False |
| process | process_availability_050 | above_T4 | above_T4 | False |
| process | process_availability_075 | above_T4 | above_T4 | False |

## Frozen v3.2 versus E2c tier positions

| Stream | Case | v3.2 v7 | E2c v8 | Changed |
|---|---|---|---|---|
| harvest | harvest_recovery_035 | T3 | T4 | True |
| harvest | harvest_recovery_060 | above_T4 | above_T4 | False |
| harvest | harvest_recovery_075 | above_T4 | above_T4 | False |
| process | process_availability_000 | T1 | T1 | False |
| process | process_availability_025 | T3 | T3 | False |
| process | process_availability_050 | above_T4 | above_T4 | False |
| process | process_availability_075 | above_T4 | above_T4 | False |
