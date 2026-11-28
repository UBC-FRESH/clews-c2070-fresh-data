# Sustainable operable 150 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_operable_150m` **Version:** 1.0.0

**Status:** shortfall. The 150,000,000.2 m3/yr
case is not sustained on the operable mask for 100 years. This is a share-based operable proxy model
estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`share_based_operable_proxy=true`, `legal_thlb=false`, `slope_screen=false`,
`transformed_curves=true`, `official_osecan_changed=false`,
`chain_v51_unchanged=true`.

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

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed/dataset`; schedule `data/derived/ws4/scanfi-national-990m-transformed/operable-150m/schedule.csv`;
  run `data/derived/ws4/scanfi-national-990m-transformed/operable-150m/run_100y`.
- Horizon: 100 years, 10 periods of 10 years.
- Eligible: operable-mask block and age at harvest >= MAI rotation
  (40-200 years).
- Selection: whole blocks, oldest-first, volume-aware, within the frozen
  150m provincial allocated shares; no block split, scaled, or harvested
  below rotation.
- If a province cannot meet its period target, the shortfall is recorded and
  the schedule continues. The cross-province national fallback is disabled.
- Annual assignment: longest-processing-time balancing over the ten offsets
  of each period.

## 3. Period harvest

| Period | Offsets | Target Mm3 | Achieved Mm3 | Delta Mm3 | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| 0 | 0-9 | 1500.000 | 1501.392 | +1.392 | 9.610 | 32,420 |
| 1 | 10-19 | 1500.000 | 1509.391 | +9.391 | 8.912 | 31,075 |
| 2 | 20-29 | 1500.000 | 1442.056 | -57.944 | 8.047 | 34,690 |
| 3 | 30-39 | 1500.000 | 1200.152 | -299.848 | 6.151 | 30,299 |
| 4 | 40-49 | 1500.000 | 1172.715 | -327.285 | 5.710 | 24,568 |
| 5 | 50-59 | 1500.000 | 1469.408 | -30.592 | 9.443 | 39,048 |
| 6 | 60-69 | 1500.000 | 1483.359 | -16.641 | 8.659 | 40,983 |
| 7 | 70-79 | 1500.000 | 1413.671 | -86.329 | 7.985 | 35,752 |
| 8 | 80-89 | 1500.000 | 1044.262 | -455.738 | 5.658 | 28,304 |
| 9 | 90-99 | 1500.000 | 1129.212 | -370.788 | 6.161 | 33,799 |

- Annual minimum: 104.4241 Mm3/yr.
- Annual maximum: 150.9391 Mm3/yr.
- Annual mean: 133.6562 Mm3/yr.
- Annual CV: 0.126796.
- Period shortfall (national): 1,645.1650 Mm3.
- Provincial shortfall: 1,761.3301 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 330,938
  (76.337 Mha treated over 100 years).
- Blocks reharvested within 100 years: 89,953.

Province shortfalls: QC: 10.2235 Mm3/yr, SK: 2.9499 Mm3/yr, AB: 1.7828 Mm3/yr, NS: 1.1804 Mm3/yr, NL: 1.0236 Mm3/yr, PE: 0.4494 Mm3/yr, NB: 0.0038 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 68.4448 Mm3/yr nominal control (70.3013 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 30.1493% | 45.223878 | 45.228064 | 45.228659 | 22.116 | 10.783 | 75,551 | True |
| AB | 20.0667% | 30.100000 | 30.447230 | 28.542553 | 10.731 | 15.402 | 67,676 | False |
| SK | 4.3068% | 6.460155 | 6.473716 | 3.511786 | 2.648 | 3.906 | 18,843 | False |
| MB | 1.1253% | 1.687988 | 1.753117 | 1.829290 | 2.146 | 2.065 | 8,871 | True |
| ON | 13.3758% | 20.063703 | 20.075113 | 20.848094 | 22.317 | 15.847 | 39,529 | True |
| QC | 22.7435% | 34.115200 | 34.115809 | 23.904287 | 10.501 | 21.558 | 92,269 | False |
| NB | 4.1565% | 6.234700 | 6.235853 | 6.240167 | 1.748 | 3.528 | 15,511 | True |
| NS | 2.3674% | 3.551095 | 3.551510 | 2.371621 | 0.850 | 1.728 | 6,755 | False |
| PE | 0.2996% | 0.449358 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.3415% | 2.012233 | 2.150908 | 1.004992 | 0.673 | 1.382 | 5,451 | False |
| YT | 0.0435% | 0.065314 | 0.070053 | 0.083371 | 1.468 | 0.048 | 223 | True |
| NT | 0.0243% | 0.036376 | 0.037825 | 0.091359 | 0.177 | 0.090 | 259 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 150,000,000.200000 | 150,139,197.455525 | +0.0928 | 133,656,178.228273 | -10.8959 |
| solid_product_m3 | m3 | 46,136,665.718213 | 46,225,635.529205 | +0.1928 | 43,151,853.409751 | -6.4695 |
| sawlog_product_m3 | m3 | 41,585,119.517419 | 41,665,312.140053 | +0.1928 | 38,894,769.561431 | -6.4695 |
| panel_product_m3 | m3 | 4,551,546.200794 | 4,560,323.389152 | +0.1928 | 4,257,083.848320 | -6.4695 |
| pulp_product_odt | odt | 15,550,881.011045 | 15,551,206.202699 | +0.0021 | 13,363,103.575321 | -14.0685 |
| pellet_product_odt | odt | 7,038,938.165569 | 7,038,462.424450 | -0.0068 | 5,541,985.173475 | -21.2667 |
| bio_product_mwh | MWh | 1,253,014.284904 | 1,252,929.597355 | -0.0068 | 986,538.938935 | -21.2667 |
| process_residue_m3 | m3 | 75,299,125.458469 | 75,373,707.581278 | +0.0990 | 67,455,641.286615 | -10.4164 |
| process_residue_odt | odt | 33,884,606.456311 | 33,918,168.411590 | +0.0990 | 30,355,038.578991 | -10.4164 |
| process_residue_pj | PJ | 626.865219 | 627.486116 | +0.0990 | 561.568214 | -10.4164 |
| harvest_residue_gross_odt | odt | 30,979,752.054305 | 30,985,148.389007 | +0.0174 | 26,168,369.031024 | -15.5307 |
| harvest_residue_gross_pj | PJ | 573.125413 | 573.225245 | +0.0174 | 484.114827 | -15.5307 |
| harvest_residue_recoverable_r035_odt | odt | 10,842,913.219007 | 10,844,801.936166 | +0.0174 | 9,158,929.160871 | -15.5307 |
| harvest_residue_recoverable_r035_pj | PJ | 200.593895 | 200.628836 | +0.0174 | 169.440189 | -15.5307 |
| harvest_residue_recoverable_r060_odt | odt | 18,587,851.232583 | 18,591,089.033418 | +0.0174 | 15,701,021.418630 | -15.5307 |
| harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 343.935147 | +0.0174 | 290.468896 | -15.5307 |
| harvest_residue_recoverable_r075_odt | odt | 23,234,814.040728 | 23,238,861.291786 | +0.0174 | 19,626,276.773298 | -15.5307 |
| harvest_residue_recoverable_r075_pj | PJ | 429.844060 | 429.918934 | +0.0174 | 363.086120 | -15.5307 |
| total_residue_gross_pj | PJ | 1,199.990632 | 1,200.711361 | +0.0601 | 1,045.683041 | -12.8591 |
| total_residue_recoverable_r035_pj | PJ | 827.459114 | 828.114951 | +0.0793 | 731.008403 | -11.6563 |
| total_residue_recoverable_r060_pj | PJ | 970.740467 | 971.421263 | +0.0701 | 852.037110 | -12.2281 |
| total_residue_recoverable_r075_pj | PJ | 1,056.709279 | 1,057.405050 | +0.0658 | 924.654334 | -12.4968 |

The comparison reference is the frozen full-forest v5.1 case total for
`150m` in `data/derived/national/facilities/national_facility_chain_scenarios_v9/scenario_summary.csv`. The primary operable basis is
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
- Provincial period targets use the frozen 150m allocated_share values. A province that cannot meet its target records a shortfall; the cross-province fallback is disabled.
- Rotation is the integer age of maximum MAI on the RSYC yield curve, capped to 40-200 years; the raw peak is flagged. Rotation is never relaxed to meet a target.
- Frozen chain v5.1 coefficients are applied to operable WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- The max-sustainable level is a schedule-only diagnostic with the same provincial shares and mask; it is not a WS4-simulated or policy-tested level.
- NU and PE have no 2016 tenure coverage. No operable block is selected there; their shortfalls are reported, not substituted with harvested volume.
- No legal THLB, slope screen, spatial road screen, official OSeCAN change, chain v5.1 mutation, or UI change is claimed.
