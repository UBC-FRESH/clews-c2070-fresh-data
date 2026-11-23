# Local v6 versus Trade v5 Measured Chain Comparison

The local case is the assignment-v6 `province_capacity_floor` chain v5: capacity v3, the 1.2x provincial floor as primary, local-first allocation, and cross-border only for the local residual. The trade case is the assignment-v5 `published_plus_proxy` sensitivity rebuilt with the same measured `national_product_chain_v3` coefficients and total-residue scenarios. Both use 18.5 GJ/odt.

All values are model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The trade case is a trade-permissive counterfactual, not a forecast and not evidence of provincial self-sufficiency. No UI or public OSeCAN surface is changed.

## Assignment at 119 Mm3

| Metric | Unit | Local v6 | Trade v5 | Delta trade-local |
|---|---|---:|---:|---:|
| assigned_m3 | m3/yr | 118,977,339.100 | 118,977,339.100 | 0.000 |
| local_m3 | m3/yr | 118,940,963.100 | 97,075,401.469 | -21,865,561.631 |
| local_share | share | 1.000 | 0.816 | -0.184 |
| cross_border_m3 | m3/yr | 36,376.000 | 21,901,937.631 | 21,865,561.631 |
| cross_border_share | share | 0.000 | 0.184 | 0.184 |
| published_m3 | m3/yr | 71,513,883.308 | 78,658,347.897 | 7,144,464.589 |
| published_share | share | 0.601 | 0.661 | 0.060 |
| proxy_m3 | m3/yr | 47,463,455.792 | 40,318,991.203 | -7,144,464.589 |
| proxy_share_of_assigned | share | 0.399 | 0.339 | -0.060 |
| scaled_proxy_m3 | m3/yr | 38,034,798.631 | 0.000 | -38,034,798.631 |
| facilities_used | count | 208.000 | 263.000 | 55.000 |
| max_facility_m3 | m3/yr | 8,093,104.685 | 2,162,922.563 | -5,930,182.122 |
| max_facility_share | share | 0.068 | 0.018 | -0.050 |
| top5_share | share | 0.157 | 0.080 | -0.078 |
| hhi | index_0_1 | 0.013 | 0.008 | -0.005 |
| capacity_shortfall_before_floor_m3_y | m3/yr | 30,282,199.511 | 30,282,199.511 | 0.000 |
| capacity_shortfall_after_floor_m3_y | m3/yr | 43,651.200 | 43,651.200 | 0.000 |
| provinces_below_floor_before | count | 5.000 | 5.000 | 0.000 |
| provinces_below_floor_after | count | 1.000 | 1.000 | 0.000 |

The capacity shortfall columns are the province shortfall before and after the 1.2x floor; the trade case runs before floor scaling, which is why `capacity_shortfall_before_floor` matches while `after_floor` describes the local case.

## Chain products and residue

| Case | Metric | Local v6 | Trade v5 | Delta |
|---|---|---:|---:|---:|
| 100m | assigned_m3 | 100,000,000.100 | 100,000,000.100 | 0.000 |
| 100m | cross_border_m3 | 31,333.500 | 14,849,602.931 | 14,818,269.431 |
| 100m | proxy_share_of_assigned | 0.397 | 0.344 | -0.053 |
| 100m | published_m3 | 60,293,932.308 | 65,562,036.480 | 5,268,104.173 |
| 100m | proxy_m3 | 39,706,067.792 | 34,437,963.620 | -5,268,104.173 |
| 100m | sawlog_product_m3 | 35,687,931.347 | 35,687,931.347 | 0.000 |
| 100m | panel_product_m3 | 3,906,091.175 | 3,906,091.175 | 0.000 |
| 100m | pulp_product_odt | 8,024,826.826 | 8,024,826.826 | 0.000 |
| 100m | pellet_product_odt | 3,492,914.219 | 3,492,914.219 | 0.000 |
| 100m | bio_product_mwh | 621,780.062 | 621,780.062 | 0.000 |
| 100m | process_residue_pj | 432.431 | 432.431 | 0.000 |
| 100m | harvest_residue_gross_pj | 264.485 | 264.485 | 0.000 |
| 100m | harvest_residue_recoverable_pj | 164.719 | 164.719 | 0.000 |
| 100m | total_residue_gross_pj | 696.915 | 696.915 | 0.000 |
| 100m | total_residue_recoverable_pj | 597.150 | 597.150 | 0.000 |
| 119m | assigned_m3 | 118,977,339.100 | 118,977,339.100 | 0.000 |
| 119m | cross_border_m3 | 36,376.000 | 21,901,937.631 | 21,865,561.631 |
| 119m | proxy_share_of_assigned | 0.399 | 0.339 | -0.060 |
| 119m | published_m3 | 71,513,883.308 | 78,658,347.897 | 7,144,464.589 |
| 119m | proxy_m3 | 47,463,455.792 | 40,318,991.203 | -7,144,464.589 |
| 119m | sawlog_product_m3 | 42,520,151.761 | 42,520,151.761 | 0.000 |
| 119m | panel_product_m3 | 4,653,886.714 | 4,653,886.714 | 0.000 |
| 119m | pulp_product_odt | 9,526,992.918 | 9,526,992.918 | 0.000 |
| 119m | pellet_product_odt | 4,172,333.553 | 4,172,333.553 | 0.000 |
| 119m | bio_product_mwh | 742,724.744 | 742,724.744 | 0.000 |
| 119m | process_residue_pj | 514.614 | 514.614 | 0.000 |
| 119m | harvest_residue_gross_pj | 313.640 | 313.640 | 0.000 |
| 119m | harvest_residue_recoverable_pj | 195.433 | 195.433 | 0.000 |
| 119m | total_residue_gross_pj | 828.254 | 828.254 | 0.000 |
| 119m | total_residue_recoverable_pj | 710.047 | 710.047 | 0.000 |
| 150m | assigned_m3 | 150,000,000.200 | 150,000,000.200 | 0.000 |
| 150m | cross_border_m3 | 36,376.000 | 38,348,850.731 | 38,312,474.731 |
| 150m | proxy_share_of_assigned | 0.439 | 0.308 | -0.131 |
| 150m | published_m3 | 84,200,050.308 | 103,798,530.395 | 19,598,480.087 |
| 150m | proxy_m3 | 65,799,949.892 | 46,201,469.805 | -19,598,480.087 |
| 150m | sawlog_product_m3 | 53,646,106.873 | 53,646,106.873 | 0.000 |
| 150m | panel_product_m3 | 5,871,637.181 | 5,871,637.181 | 0.000 |
| 150m | pulp_product_odt | 12,006,097.141 | 12,006,097.141 | 0.000 |
| 150m | pellet_product_odt | 5,353,798.761 | 5,353,798.761 | 0.000 |
| 150m | bio_product_mwh | 953,039.531 | 953,039.531 | 0.000 |
| 150m | process_residue_pj | 649.260 | 649.260 | 0.000 |
| 150m | harvest_residue_gross_pj | 385.199 | 385.199 | 0.000 |
| 150m | harvest_residue_recoverable_pj | 241.251 | 241.251 | 0.000 |
| 150m | total_residue_gross_pj | 1,034.459 | 1,034.459 | 0.000 |
| 150m | total_residue_recoverable_pj | 890.512 | 890.512 | 0.000 |

National products and residue are unchanged by construction; the trade case moves the same national totals across facilities and provinces.

## Process residue by facility province (119 Mm3)

| Province | Local PJ | Trade PJ | Delta PJ | Local odt | Trade odt |
|---|---:|---:|---:|---:|---:|
| BC | 180.270 | 254.958 | 74.687 | 9,744,336 | 13,781,489 |
| AB | 106.747 | 41.207 | -65.540 | 5,770,121 | 2,227,432 |
| SK | 12.645 | 2.062 | -10.584 | 683,522 | 111,437 |
| MB | 3.428 | 2.226 | -1.202 | 185,286 | 120,306 |
| ON | 57.143 | 48.559 | -8.584 | 3,088,824 | 2,624,823 |
| QC | 115.184 | 126.431 | 11.247 | 6,226,162 | 6,834,108 |
| NB | 25.811 | 25.749 | -0.061 | 1,395,163 | 1,391,852 |
| NS | 10.124 | 10.103 | -0.021 | 547,247 | 546,122 |
| PE | 0.880 | 0.879 | -0.000 | 47,545 | 47,532 |
| NL | 2.302 | 2.254 | -0.048 | 124,450 | 121,835 |
| YT | 0.080 | 0.186 | 0.106 | 4,318 | 10,038 |
| NT | 0.000 | 0.000 | 0.000 | 0 | 0 |
| NU | 0.000 | 0.000 | 0.000 | 0 | 0 |

## Residue curve cases

| Stream | Case | Local v6 PJ | Trade v5 PJ | Delta PJ |
|---|---|---:|---:|---:|
| process | process_availability_000 | 0.000 | 0.000 | 0.000 |
| process | process_availability_025 | 128.654 | 128.654 | 0.000 |
| process | process_availability_050 | 257.307 | 257.307 | 0.000 |
| process | process_availability_075 | 385.961 | 385.961 | 0.000 |
| harvest | harvest_recovery_035 | 109.774 | 109.774 | 0.000 |
| harvest | harvest_recovery_060 | 188.184 | 188.184 | 0.000 |
| harvest | harvest_recovery_075 | 235.230 | 235.230 | 0.000 |

The province-level curve table is in `curve_case_comparison.csv`.

## OSeCAN handoff

Process-residue zone PJ differs; harvest-residue zone PJ is identical because harvest residue is origin-province only.

| Zone | Stream | Case | Local v6 PJ | Trade v5 PJ | Delta PJ |
|---|---|---|---:|---:|---:|
| A1 | process | process_availability_025 | 17.181 | 6.632 | -10.549 |
| A1 | process | process_availability_050 | 34.362 | 13.265 | -21.097 |
| A1 | process | process_availability_075 | 51.542 | 19.897 | -31.646 |
| A2 | process | process_availability_025 | 9.506 | 3.670 | -5.836 |
| A2 | process | process_availability_050 | 19.012 | 7.339 | -11.673 |
| A2 | process | process_availability_075 | 28.518 | 11.009 | -17.509 |
| B1 | process | process_availability_025 | 3.733 | 5.280 | 1.547 |
| B1 | process | process_availability_050 | 7.467 | 10.560 | 3.094 |
| B1 | process | process_availability_075 | 11.200 | 15.840 | 4.640 |
| B2 | process | process_availability_025 | 41.334 | 58.459 | 17.125 |
| B2 | process | process_availability_050 | 82.668 | 116.919 | 34.250 |
| B2 | process | process_availability_075 | 124.003 | 175.378 | 51.375 |
| L1 | process | process_availability_025 | 0.576 | 0.563 | -0.012 |
| L1 | process | process_availability_050 | 1.151 | 1.127 | -0.024 |
| L1 | process | process_availability_075 | 1.727 | 1.690 | -0.036 |
| M1 | process | process_availability_025 | 0.857 | 0.556 | -0.301 |
| M1 | process | process_availability_050 | 1.714 | 1.113 | -0.601 |
| M1 | process | process_availability_075 | 2.571 | 1.669 | -0.902 |
| N1 | process | process_availability_025 | 0.020 | 0.046 | 0.026 |
| N1 | process | process_availability_050 | 0.040 | 0.093 | 0.053 |
| N1 | process | process_availability_075 | 0.060 | 0.139 | 0.079 |
| O1 | process | process_availability_025 | 11.903 | 10.115 | -1.788 |
| O1 | process | process_availability_050 | 23.807 | 20.230 | -3.576 |
| O1 | process | process_availability_075 | 35.710 | 30.346 | -5.364 |
| O2 | process | process_availability_025 | 2.383 | 2.025 | -0.358 |
| O2 | process | process_availability_050 | 4.765 | 4.049 | -0.716 |
| O2 | process | process_availability_075 | 7.148 | 6.074 | -1.074 |
| Q1 | process | process_availability_025 | 17.586 | 19.303 | 1.717 |
| Q1 | process | process_availability_050 | 35.172 | 38.606 | 3.434 |
| Q1 | process | process_availability_075 | 52.757 | 57.909 | 5.151 |
| Q2 | process | process_availability_025 | 11.210 | 12.305 | 1.095 |
| Q2 | process | process_availability_050 | 22.420 | 24.610 | 2.189 |
| Q2 | process | process_availability_075 | 33.631 | 36.914 | 3.284 |
| S1 | process | process_availability_025 | 3.161 | 0.515 | -2.646 |
| S1 | process | process_availability_050 | 6.323 | 1.031 | -5.292 |
| S1 | process | process_availability_075 | 9.484 | 1.546 | -7.938 |
| T1 | process | process_availability_025 | 9.204 | 9.183 | -0.021 |
| T1 | process | process_availability_050 | 18.407 | 18.366 | -0.041 |
| T1 | process | process_availability_075 | 27.611 | 27.549 | -0.062 |

### BC zonal process comparison (PJ)

| Case | Local v6 | Trade v5 | Delta |
|---|---:|---:|---:|
| process_availability_000 | 0.000 | 0.000 | 0.000 |
| process_availability_025 | 45.068 | 63.739 | 18.672 |
| process_availability_050 | 90.135 | 127.479 | 37.344 |
| process_availability_075 | 135.203 | 191.218 | 56.015 |

## Validation

| Check | Status | Detail |
|---|---|---|
| assigned_volume_equal | PASS | local and trade assignment totals match |
| cross_border_trade_higher | PASS | trade 21,901,938 m3 > local 36,376 m3 |
| national_products_residue_equal | PASS | all three harvest cases share national products and residue totals |
| province_process_conserves | PASS | sum of province process deltas = 2.17603712827e-14 PJ |
| harvest_handoff_identical | PASS | harvest-residue handoff is origin-province only and unchanged |
| process_handoff_conserves | PASS | sum of process zone deltas = 3.92832572027e-11 PJ |
| osecan_tree_unchanged | PASS | official OSeCAN tree hash unchanged before and after both builds |
| labels | PASS | no official OSeCAN change is claimed |

## Labels and caveats

- `model_estimate=true`, `observed=false`, `policy_grade=false`; no national supply, policy, AAC, tenure, or investment claim.
- The trade case is an upper-bound cross-border counterfactual, not a trade forecast.
- Process and harvest residue remain separate streams; no combined OSeCAN row is written.
- Capacity status mixes published and class-median proxy capacity; the bases are not interchangeable.
- The official OSeCAN tree is read-only and unchanged.

Run `.venv/bin/python -m workflows.national.facilities.national_facility_chain_v5_trade_comparison` to reproduce the comparison.

No policy/AAC claim is made.
