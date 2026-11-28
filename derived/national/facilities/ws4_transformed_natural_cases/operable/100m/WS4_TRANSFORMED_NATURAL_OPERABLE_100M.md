# Sustainable operable 100 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_natural_operable_100m` **Version:** 1.0.0

**Status:** shortfall. The 100,000,000.1 m3/yr
case is not sustained on the operable mask for 100 years. This is a share-based operable proxy model
estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`, `transformed_curves=true`, `natural_5param_only=true`, `managed_basis_quarantined=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Operable screen

- Screen: `screen_core30` - SCANFI age >= 30 years, NBAC 2020 burned excluded,
  within 10 km of a public NRN road.
- Mask: 370,752 blocks /
  75.374 Mha, selected by a
  stable hash to match the published provincial operable share.
- Published screen area: 77.050 Mha.
- The mask is an area-share proxy. No legal THLB, slope DEM, or spatial road
  overlay is used.

## 2. Method

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed-natural/dataset`; schedule `data/derived/ws4/scanfi-national-990m-transformed-natural/operable-100m/schedule.csv`;
  run `data/derived/ws4/scanfi-national-990m-transformed-natural/operable-100m/run_100y`.
- Horizon: 100 years, 10 periods of 10 years.
- Eligible: operable-mask block and age at harvest >= MAI rotation
  (40-200 years).
- Selection: whole blocks, oldest-first, volume-aware, within the frozen
  100m provincial allocated shares; no block split, scaled, or harvested
  below rotation.
- If a province cannot meet its period target, the shortfall is recorded and
  the schedule continues. The cross-province national fallback is disabled.
- Annual assignment: longest-processing-time balancing over the ten offsets
  of each period.

## 3. Period harvest

| Period | Offsets | Target Mm3 | Achieved Mm3 | Delta Mm3 | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| 0 | 0-9 | 1000.000 | 826.719 | -173.281 | 4.120 | 14,973 |
| 1 | 10-19 | 1000.000 | 730.999 | -269.001 | 3.438 | 11,717 |
| 2 | 20-29 | 1000.000 | 802.471 | -197.529 | 3.934 | 13,711 |
| 3 | 30-39 | 1000.000 | 923.107 | -76.893 | 4.232 | 15,161 |
| 4 | 40-49 | 1000.000 | 947.470 | -52.530 | 4.364 | 17,952 |
| 5 | 50-59 | 1000.000 | 975.846 | -24.154 | 4.163 | 17,066 |
| 6 | 60-69 | 1000.000 | 944.898 | -55.102 | 4.100 | 21,244 |
| 7 | 70-79 | 1000.000 | 904.100 | -95.900 | 3.805 | 20,595 |
| 8 | 80-89 | 1000.000 | 842.177 | -157.823 | 3.571 | 20,761 |
| 9 | 90-99 | 1000.000 | 792.824 | -207.176 | 3.228 | 19,030 |

- Annual minimum: 73.0999 Mm3/yr.
- Annual maximum: 99.4616 Mm3/yr.
- Annual mean: 86.9061 Mm3/yr.
- Annual CV: 0.088619.
- Period shortfall (national): 1,309.3890 Mm3.
- Provincial shortfall: 1,418.8131 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 172,210
  (38.957 Mha treated over 100 years).
- Blocks reharvested within 100 years: 0.

Province shortfalls: QC: 8.4325 Mm3/yr, NB: 2.8136 Mm3/yr, SK: 1.2709 Mm3/yr, NS: 0.7928 Mm3/yr, NL: 0.6271 Mm3/yr, PE: 0.2513 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 0.0000 Mm3/yr nominal control (0.0000 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 33.2488% | 33.248823 | 33.249566 | 33.253533 | 22.116 | 7.786 | 55,069 | True |
| AB | 19.0380% | 19.038002 | 19.519351 | 19.579080 | 10.731 | 8.172 | 32,020 | True |
| SK | 3.6133% | 3.613337 | 0.507531 | 2.356263 | 2.648 | 2.248 | 10,773 | False |
| MB | 0.9441% | 0.944137 | 0.959616 | 0.997369 | 2.146 | 0.876 | 3,064 | True |
| ON | 11.2222% | 11.222165 | 11.590684 | 11.492097 | 22.317 | 7.061 | 15,718 | True |
| QC | 22.1841% | 22.184137 | 15.954002 | 13.774657 | 10.501 | 9.890 | 44,074 | False |
| NB | 6.2347% | 6.234700 | 0.001613 | 3.494505 | 1.748 | 1.486 | 6,148 | False |
| NS | 1.9862% | 1.986222 | 0.000000 | 1.229107 | 0.850 | 0.652 | 2,343 | False |
| PE | 0.2513% | 0.251338 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.2093% | 1.209274 | 0.819810 | 0.586376 | 0.673 | 0.672 | 2,648 | False |
| YT | 0.0365% | 0.036532 | 0.037432 | 0.055632 | 1.468 | 0.032 | 131 | True |
| NT | 0.0313% | 0.031333 | 0.032303 | 0.087492 | 0.177 | 0.082 | 222 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 100,000,000.100000 | 82,671,907.791379 | -17.3281 | 86,906,110.390028 | -13.0939 |
| solid_product_m3 | m3 | 31,692,807.151334 | 27,943,602.473729 | -11.8298 | 28,776,817.818074 | -9.2008 |
| sawlog_product_m3 | m3 | 28,566,198.981094 | 25,186,866.682448 | -11.8298 | 25,937,882.368973 | -9.2008 |
| panel_product_m3 | m3 | 3,126,608.170239 | 2,756,735.791281 | -11.8298 | 2,838,935.449101 | -9.2008 |
| pulp_product_odt | odt | 10,136,702.863917 | 7,998,688.852564 | -21.0918 | 8,473,203.622384 | -16.4107 |
| pellet_product_odt | odt | 4,372,287.851260 | 2,804,243.020508 | -35.8633 | 3,490,682.769296 | -20.1635 |
| bio_product_mwh | MWh | 778,318.974606 | 499,188.440129 | -35.8633 | 621,382.838024 | -20.1635 |
| process_residue_m3 | m3 | 50,358,921.112605 | 41,966,878.173495 | -16.6645 | 43,941,651.246835 | -12.7431 |
| process_residue_odt | odt | 22,661,514.500672 | 18,885,095.178082 | -16.6645 | 19,773,743.061086 | -12.7431 |
| process_residue_pj | PJ | 419.238018 | 349.374261 | -16.6645 | 365.814247 | -12.7431 |
| harvest_residue_gross_odt | odt | 20,175,347.205464 | 15,103,630.145046 | -25.1382 | 16,782,475.325416 | -16.8169 |
| harvest_residue_gross_pj | PJ | 373.243923 | 279.417158 | -25.1382 | 310.475794 | -16.8169 |
| harvest_residue_recoverable_r035_odt | odt | 7,061,371.521912 | 5,286,270.550773 | -25.1382 | 5,873,866.363903 | -16.8169 |
| harvest_residue_recoverable_r035_pj | PJ | 130.635373 | 97.796005 | -25.1382 | 108.666528 | -16.8169 |
| harvest_residue_recoverable_r060_odt | odt | 12,105,208.323278 | 9,062,178.087039 | -25.1382 | 10,069,485.195260 | -16.8169 |
| harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 167.650295 | -25.1382 | 186.285476 | -16.8169 |
| harvest_residue_recoverable_r075_odt | odt | 15,131,510.404098 | 11,327,722.608805 | -25.1382 | 12,586,856.494082 | -16.8169 |
| harvest_residue_recoverable_r075_pj | PJ | 279.932942 | 209.562868 | -25.1382 | 232.856845 | -16.8169 |
| total_residue_gross_pj | PJ | 792.481942 | 628.791418 | -20.6554 | 676.290040 | -14.6618 |
| total_residue_recoverable_r035_pj | PJ | 549.873391 | 447.170266 | -18.6776 | 474.480774 | -13.7109 |
| total_residue_recoverable_r060_pj | PJ | 643.184372 | 517.024555 | -19.6149 | 552.099723 | -14.1615 |
| total_residue_recoverable_r075_pj | PJ | 699.170961 | 558.937129 | -20.0572 | 598.671092 | -14.3741 |

The comparison reference is the frozen full-forest v5.1 case total for
`100m` in `data/derived/national/facilities/national_facility_chain_scenarios_v9/scenario_summary.csv`. The primary operable basis is
the first-period annual average; the achieved basis is the 100-year average.
Both are unscaled and use frozen v5.1 per-province coefficients.

## 6. OSeCAN handoff

The combined `osecan/` artifact applies the existing WS4 origin-province
handoff logic to this operable chain. It verifies 21/21 frozen v5.1 reference
positions and an unchanged official OSeCAN tree, and reports the modelled
tier positions against handoff v10. Tier differences are findings, not
official changes.

## 7. Caveats

- The operable landbase is a share-based area proxy built from province-level screen_core30 shares; it is not a spatial THLB, slope, tenure, or road overlay.
- The schedule is a national even-flow arithmetic model, not an AAC, policy result, tenure plan, or investment case.
- Provincial period targets use the frozen 100m allocated_share values. A province that cannot meet its target records a shortfall; the cross-province fallback is disabled.
- Rotation is the integer age of maximum MAI on the RSYC yield curve, capped to 40-200 years; the raw peak is flagged. Rotation is never relaxed to meet a target.
- Frozen chain v5.1 coefficients are applied to operable WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- The max-sustainable level is a schedule-only diagnostic with the same provincial shares and mask; it is not a WS4-simulated or policy-tested level.
- NU and PE have no 2016 tenure coverage. No operable block is selected there; their shortfalls are reported, not substituted with harvested volume.
- No legal THLB, slope screen, spatial road screen, official OSeCAN change, chain v5.1 mutation, or UI change is claimed.
