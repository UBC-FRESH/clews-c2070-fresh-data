# Sustainable 119 Mm3/yr WS4 schedule and chain with transformed RSYC curves

**Artifact:** `ws4_transformed_119m` **Version:** 1.0.0

**Status:** pass. The 118,977,339.1 m3/yr target is sustained for 100 years
with no period shortfall. The schedule is a whole-block model estimate, not an
AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`, `transformed_curves=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed/dataset`
- Curve patch: 718 WS4 curves mapped to 718 RSYC models from 3948 transformed cell curves; V100 max error 0.000500 m3/ha (tolerance 0.01 m3/ha).
- Schedule: `data/derived/ws4/scanfi-national-990m-transformed/sustainable-119m/schedule.csv`
- Run: `data/derived/ws4/scanfi-national-990m-transformed/sustainable-119m/run_100y`
- Horizon: 100 years, 10 periods of 10 years.
- Period target: 1,189,773,391.0 m3.
- Block volume: sum of fragment area times the block's transformed RSYC yield curve (V100-preserved, age 201-600 held flat) at the exact fragment age.
- Block age: fragment-area-weighted age.
- Rotation: integer age of maximum MAI on the transformed RSYC yield curve (V100-preserved, age 201-600 held flat), capped to
  40-200 years and flagged outside that band. Raw peaks
  are {13: 157895, 17: 24, 18: 18258, 76: 517, 77: 1, 96: 35313, 101: 2, 102: 43, 105: 3, 106: 5, 107: 70, 109: 2551, 110: 744, 111: 9947, 116: 4314, 117: 7, 118: 280, 119: 7670, 120: 7092, 121: 7848, 127: 814, 140: 46, 153: 31, 174: 1}; all blocks use {40: 176177, 76: 517, 77: 1, 96: 35313, 101: 2, 102: 43, 105: 3, 106: 5, 107: 70, 109: 2551, 110: 744, 111: 9947, 116: 4314, 117: 7, 118: 280, 119: 7670, 120: 7092, 121: 7848, 127: 814, 140: 46, 153: 31, 174: 1}.
- Eligible blocks: natural/unmanaged with age >= rotation, or managed with age
  since last harvest >= rotation.
- Selection: whole blocks, oldest-first, volume-aware, within provincial
  period targets set by the frozen 119 Mm3 control shares. The national target
  is the sum of the provincial targets. No block is split, scaled, or
  harvested below rotation.
- Annual assignment: selected blocks are assigned to the ten offsets of each
  period by longest-processing-time balancing of exact annual volumes.

## 2. Period harvest

| Period | Offsets | Target Mm3 | Achieved Mm3 | Overshoot % | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| 0 | 0-9 | 1189.773 | 1198.792 | 0.7580 | 8.583 | 38595 |
| 1 | 10-19 | 1189.773 | 1216.089 | 2.2118 | 7.440 | 23005 |
| 2 | 20-29 | 1189.773 | 1197.191 | 0.6235 | 7.346 | 19234 |
| 3 | 30-39 | 1189.773 | 1195.517 | 0.4828 | 7.370 | 23448 |
| 4 | 40-49 | 1189.773 | 1217.776 | 2.3536 | 7.766 | 28009 |
| 5 | 50-59 | 1189.773 | 1196.314 | 0.5498 | 7.093 | 22221 |
| 6 | 60-69 | 1189.773 | 1193.174 | 0.2858 | 6.480 | 22851 |
| 7 | 70-79 | 1189.773 | 1204.183 | 1.2111 | 7.154 | 25596 |
| 8 | 80-89 | 1189.773 | 1192.540 | 0.2325 | 6.624 | 21978 |
| 9 | 90-99 | 1189.773 | 1194.029 | 0.3577 | 6.532 | 28539 |

- Annual harvest minimum: 119,254,007.7 m3/yr.
- Annual harvest maximum: 121,777,630.2 m3/yr.
- Annual mean: 120,056,052.5 m3/yr.
- Annual CV: 0.007310.
- Period shortfall: 0.0 m3.
- 119 Mm3/yr sustained for 100 years: `True`.
- Selected blocks: 253,476
  (72.388 Mha).
- Blocks reharvested within 100 years: 0.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | Achieved Mm3/yr | 119 Mm3 basis Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 33.602% | 39.978577 | 39.995826 | 39.636460 | 8.357 | 55341 |
| AB | 19.240% | 22.891404 | 23.200779 | 22.992318 | 9.046 | 29336 |
| SK | 3.652% | 4.344698 | 4.477219 | 4.436991 | 3.471 | 9274 |
| MB | 0.954% | 1.135236 | 1.170356 | 1.159840 | 1.171 | 2583 |
| ON | 11.341% | 13.493596 | 13.600609 | 13.478407 | 13.372 | 26036 |
| QC | 22.420% | 26.674334 | 26.784760 | 26.544096 | 29.111 | 98845 |
| NB | 5.240% | 6.234700 | 6.245190 | 6.189077 | 3.516 | 15958 |
| NS | 2.007% | 2.388245 | 2.723917 | 2.699443 | 1.867 | 5520 |
| PE | 0.254% | 0.302210 | 0.304975 | 0.302235 | 0.226 | 1668 |
| NL | 1.222% | 1.454038 | 1.464602 | 1.451443 | 2.186 | 8364 |
| YT | 0.037% | 0.043926 | 0.045284 | 0.044877 | 0.026 | 209 |
| NT | 0.031% | 0.036376 | 0.042536 | 0.042154 | 0.039 | 342 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | 119 Mm3 basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 118977339.100000 | 118977339.100000 | 0.0000 | 120056052.538964 | 0.9067 |
| solid_product_m3 | m3 | 37673626.761068 | 37547496.540087 | -0.3348 | 37887922.619739 | 0.5688 |
| sawlog_product_m3 | m3 | 33956989.460016 | 33843302.434034 | -0.3348 | 34150144.269888 | 0.5688 |
| panel_product_m3 | m3 | 3716637.301052 | 3704194.106054 | -0.3348 | 3737778.349851 | 0.5688 |
| pulp_product_odt | odt | 12066311.269557 | 12099425.851807 | 0.2744 | 12209125.844838 | 1.1836 |
| pellet_product_odt | odt | 5229686.166845 | 5270273.302532 | 0.7761 | 5318056.474365 | 1.6898 |
| bio_product_mwh | MWh | 930946.020335 | 938171.010753 | 0.7761 | 946676.980755 | 1.6898 |
| process_residue_m3 | m3 | 59910020.050475 | 59892123.250134 | -0.0299 | 60435137.900880 | 0.8765 |
| process_residue_odt | odt | 26959509.022728 | 26951455.462575 | -0.0299 | 27195812.055410 | 0.8765 |
| process_residue_pj | PJ | 498.750917 | 498.601926 | -0.0299 | 503.122523 | 0.8765 |
| harvest_residue_gross_odt | odt | 24022203.571695 | 24099302.177191 | 0.3209 | 24317799.592958 | 1.2305 |
| harvest_residue_gross_pj | PJ | 444.410766 | 445.837090 | 0.3209 | 449.879292 | 1.2305 |
| harvest_residue_recoverable_r035_odt | odt | 8407771.250102 | 8434755.762026 | 0.3209 | 8511229.857544 | 1.2305 |
| harvest_residue_recoverable_r035_pj | PJ | 155.543768 | 156.042982 | 0.3209 | 157.457752 | 1.2305 |
| harvest_residue_recoverable_r060_odt | odt | 14413322.143027 | 14459581.306325 | 0.3209 | 14590679.755785 | 1.2305 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 267.502254 | 0.3209 | 269.927575 | 1.2305 |
| harvest_residue_recoverable_r075_odt | odt | 18016652.678794 | 18074476.632916 | 0.3209 | 18238349.694741 | 1.2305 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308075 | 334.377818 | 0.3209 | 337.409469 | 1.2305 |
| total_residue_gross_pj | PJ | 943.161683 | 944.439016 | 0.1354 | 953.001815 | 1.0433 |
| total_residue_recoverable_r035_pj | PJ | 654.294685 | 654.644908 | 0.0535 | 660.580275 | 0.9607 |
| total_residue_recoverable_r060_pj | PJ | 765.397377 | 766.104180 | 0.0923 | 773.050099 | 0.9998 |
| total_residue_recoverable_r075_pj | PJ | 832.058991 | 832.979744 | 0.1107 | 840.531992 | 1.0183 |

The `sustainable_119m` basis applies one national factor
(0.991014918313974) to the 100-year annual
average so the total is exactly 118,977,339.1 m3. The
`sustainable_achieved` basis is the unscaled WS4 average
(120,056,052.5 m3/yr).

## 4b. First-period annual-average chain

| Metric | Unit | v5.1 | First period 119 Mm3 basis | Delta % | First period achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 118977339.100000 | 118977339.100000 | 0.0000 | 119879195.350079 | 0.7580 |
| solid_product_m3 | m3 | 37673626.761068 | 37538173.831836 | -0.3595 | 37822715.719752 | 0.3957 |
| pulp_product_odt | odt | 12066311.269557 | 12088679.871614 | 0.1854 | 12180312.879882 | 0.9448 |
| process_residue_pj | PJ | 498.750917 | 498.451203 | -0.0601 | 502.229497 | 0.6975 |
| harvest_residue_gross_pj | PJ | 444.410766 | 446.765843 | 0.5299 | 450.152358 | 1.2920 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 268.059506 | 0.5299 | 270.091415 | 1.2920 |
| total_residue_gross_pj | PJ | 943.161683 | 945.217046 | 0.2179 | 952.381855 | 0.9776 |

The first-period basis applies the same frozen v5.1 coefficients to the first-period annual average. The 119 Mm3 basis scales that average by one national factor; the achieved basis is unscaled.

## 4c. Comparison with the original RSYC 119 Mm3 case

| Metric | Unit | Original RSYC 119m | Transformed 119m | Delta |
|---|---|---|---|---|
| annual_min_m3 | m3/yr | 1.19043e+08 | 1.19254e+08 | 210743 |
| annual_max_m3 | m3/yr | 1.22161e+08 | 1.21778e+08 | -383405 |
| annual_mean_m3 | m3/yr | 1.19884e+08 | 1.20056e+08 | 172162 |
| annual_cv | fraction | 0.00846067 | 0.00730967 | -0.001151 |
| period_shortfall_m3 | m3 | 0 | 0 | 0 |
| selected_blocks | blocks | 318820 | 253476 | -65344 |
| selected_area_ha | ha | 8.43481e+07 | 7.23883e+07 | -1.19598e+07 |
| blocks_reharvested | blocks | 0 | 0 | 0 |
| mean_rotation_years_area_weighted | years | 40 | 53.9705 | 13.9705 |
| curve_count | curves | 719 | 719 | 0 |
| max_mai_m3_per_ha_year_median | m3/ha/yr | 2.60915 | 3.25541 | 0.646263 |
| rotation_raw_years_median | years | 2 | 18 | 16 |
| out_of_range_curves | curves | 719 | 391 | -328 |

The transformed case selects fewer blocks and hectares because the transformed curves carry more volume per hectare at the same rotation cap; the area-weighted mean rotation rises while the 100-year even-flow target is still met.

## 5. National oldest-first free-run sensitivity

The same scheduler without provincial allocation selects
220,651 blocks /
31.388 Mha and sustains the period
target (`True`), but the 100-year harvest is
95.84% BC because BC holds
the oldest inventory. That concentration would change the frozen v5.1
province-weighted residue mix and is therefore reported as a diagnostic, not
used as the chain basis. The province-allocated schedule is the chain basis.

## 6. OSeCAN handoff

The separate `osecan/` artifact applies the existing WS4 origin-province
handoff logic to this chain. It verifies 21/21 frozen v5.1 reference positions,
7/7 119 Mm3 tier positions on both bases, and an unchanged official OSeCAN
tree. See `osecan/FORESTRY_OSECAN_HANDOFF_WS4_SUSTAINABLE.md`.

## 7. Caveats

- Yield curves are the national RSYC transform v1: V100 is preserved, ages 1-200 are transformed, and ages 201-600 are held at the age-200 value. The model curve is the forest-area-weighted mean of transformed cell curves for each WS4 model.
- The transformed curves shift rotation ages and harvest timing. This is a whole-block national even-flow model estimate, not an AAC, policy result, tenure plan, or investment case.
- The full forest estate is used; no operability, tenure, road, slope, or mill-capacity screen is applied.
- Provincial period targets use the frozen 119 Mm3 control shares so the chain and OSeCAN handoff remain comparable with the original RSYC 119 Mm3 case. The national oldest-first free run is a sensitivity, not the chain basis.
- Whole blocks are selected. Provincial achieved volume can overshoot the target by the final block because no block is split or scaled.
- Frozen chain v5.1 coefficients are applied to the WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- No original national 990 m dataset, frozen chain v5.1 artifact, official OSeCAN file, or UI surface is changed. Transformed curves are not official OSeCAN curves.
