# Sustainable operable 150 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_operable_150m` **Version:** 1.0.0

**Status:** shortfall. The 150,000,000.2 m3/yr
case is not sustained on the operable mask for 100 years. This is a share-based operable proxy model
estimate, not an AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`share_based_operable_proxy=true`, `legal_thlb=false`, `slope_screen=false`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

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

- Dataset: `data/derived/ws4/scanfi-national-990m/dataset`; schedule `data/derived/ws4/operable-150m/schedule.csv`;
  run `data/derived/ws4/operable-150m/run_100y`.
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
| 0 | 0-9 | 1500.000 | 1500.962 | +0.962 | 10.470 | 36,398 |
| 1 | 10-19 | 1500.000 | 1542.673 | +42.673 | 10.444 | 41,789 |
| 2 | 20-29 | 1500.000 | 1480.180 | -19.820 | 9.919 | 46,625 |
| 3 | 30-39 | 1500.000 | 1161.172 | -338.828 | 7.113 | 36,853 |
| 4 | 40-49 | 1500.000 | 1117.221 | -382.779 | 6.632 | 32,644 |
| 5 | 50-59 | 1500.000 | 1375.323 | -124.677 | 10.675 | 47,597 |
| 6 | 60-69 | 1500.000 | 1420.821 | -79.179 | 9.704 | 46,540 |
| 7 | 70-79 | 1500.000 | 1396.508 | -103.492 | 9.826 | 44,849 |
| 8 | 80-89 | 1500.000 | 1140.257 | -359.743 | 7.364 | 31,931 |
| 9 | 90-99 | 1500.000 | 1133.636 | -366.364 | 7.628 | 44,860 |

- Annual minimum: 111.6734 Mm3/yr.
- Annual maximum: 154.4895 Mm3/yr.
- Annual mean: 132.6875 Mm3/yr.
- Annual CV: 0.121519.
- Period shortfall (national): 1,774.8825 Mm3.
- Provincial shortfall: 1,896.9787 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 410,086
  (89.775 Mha treated over 100 years).
- Blocks reharvested within 100 years: 105,174.

Province shortfalls: QC: 12.7716 Mm3/yr, SK: 2.5073 Mm3/yr, NS: 1.4602 Mm3/yr, NL: 1.1185 Mm3/yr, NB: 0.6628 Mm3/yr, PE: 0.4494 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 61.4868 Mm3/yr nominal control (62.7054 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 30.1493% | 45.223878 | 45.224345 | 45.227525 | 22.116 | 18.744 | 136,934 | True |
| AB | 20.0667% | 30.100000 | 30.136081 | 30.590016 | 10.731 | 18.795 | 78,168 | True |
| SK | 4.3068% | 6.460155 | 6.496565 | 3.966089 | 2.648 | 5.446 | 24,721 | False |
| MB | 1.1253% | 1.687988 | 1.767256 | 1.737952 | 2.146 | 2.102 | 9,130 | True |
| ON | 13.3758% | 20.063703 | 20.133015 | 20.966845 | 22.317 | 15.853 | 39,531 | True |
| QC | 22.7435% | 34.115200 | 34.200553 | 21.419291 | 10.501 | 21.944 | 92,762 | False |
| NB | 4.1565% | 6.234700 | 6.289339 | 5.602403 | 1.748 | 3.578 | 15,799 | False |
| NS | 2.3674% | 3.551095 | 3.583627 | 2.110089 | 0.850 | 1.749 | 6,843 | False |
| PE | 0.2996% | 0.449358 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.3415% | 2.012233 | 2.163253 | 0.910556 | 0.673 | 1.394 | 5,497 | False |
| YT | 0.0435% | 0.065314 | 0.065314 | 0.072948 | 1.468 | 0.075 | 371 | True |
| NT | 0.0243% | 0.036376 | 0.036814 | 0.083812 | 0.177 | 0.096 | 330 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 150,000,000.200000 | 150,096,161.415197 | +0.0641 | 132,687,525.202585 | -11.5416 |
| solid_product_m3 | m3 | 46,136,665.718213 | 46,205,915.906538 | +0.1501 | 42,859,441.424691 | -7.1033 |
| sawlog_product_m3 | m3 | 41,585,119.517419 | 41,647,537.928313 | +0.1501 | 38,631,205.058931 | -7.1033 |
| panel_product_m3 | m3 | 4,551,546.200794 | 4,558,377.978225 | +0.1501 | 4,228,236.365760 | -7.1033 |
| pulp_product_odt | odt | 15,550,881.011045 | 15,546,309.670058 | -0.0294 | 13,228,147.127068 | -14.9363 |
| pellet_product_odt | odt | 7,038,938.165569 | 7,054,192.315608 | +0.2167 | 5,577,640.400815 | -20.7602 |
| bio_product_mwh | MWh | 1,253,014.284904 | 1,255,729.704112 | +0.2167 | 992,885.991308 | -20.7602 |
| process_residue_m3 | m3 | 75,299,125.458469 | 75,351,580.646809 | +0.0697 | 66,923,813.586343 | -11.1227 |
| process_residue_odt | odt | 33,884,606.456311 | 33,908,211.291079 | +0.0697 | 30,115,716.113868 | -11.1227 |
| process_residue_pj | PJ | 626.865219 | 627.301909 | +0.0697 | 557.140748 | -11.1227 |
| harvest_residue_gross_odt | odt | 30,979,752.054305 | 31,003,495.235589 | +0.0766 | 26,028,468.471963 | -15.9823 |
| harvest_residue_gross_pj | PJ | 573.125413 | 573.564662 | +0.0766 | 481.526667 | -15.9823 |
| harvest_residue_recoverable_r035_odt | odt | 10,842,913.219007 | 10,851,223.332470 | +0.0766 | 9,109,963.965201 | -15.9823 |
| harvest_residue_recoverable_r035_pj | PJ | 200.593895 | 200.747632 | +0.0766 | 168.534333 | -15.9823 |
| harvest_residue_recoverable_r060_odt | odt | 18,587,851.232583 | 18,602,097.141367 | +0.0766 | 15,617,081.083194 | -15.9823 |
| harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 344.138797 | +0.0766 | 288.916000 | -15.9823 |
| harvest_residue_recoverable_r075_odt | odt | 23,234,814.040728 | 23,252,621.426722 | +0.0766 | 19,521,351.354003 | -15.9823 |
| harvest_residue_recoverable_r075_pj | PJ | 429.844060 | 430.173496 | +0.0766 | 361.145000 | -15.9823 |
| total_residue_gross_pj | PJ | 1,199.990632 | 1,200.866571 | +0.0730 | 1,038.667415 | -13.4437 |
| total_residue_recoverable_r035_pj | PJ | 827.459114 | 828.049541 | +0.0714 | 725.675081 | -12.3008 |
| total_residue_recoverable_r060_pj | PJ | 970.740467 | 971.440706 | +0.0721 | 846.056748 | -12.8442 |
| total_residue_recoverable_r075_pj | PJ | 1,056.709279 | 1,057.475405 | +0.0725 | 918.285748 | -13.0995 |

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
