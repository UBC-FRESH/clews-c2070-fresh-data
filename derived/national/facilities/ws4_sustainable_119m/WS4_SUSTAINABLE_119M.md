# Sustainable 119 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_sustainable_119m` **Version:** 1.0.0

**Status:** pass. The 118,977,339.1 m3/yr target is sustained for 100 years
with no period shortfall. The schedule is a whole-block model estimate, not an
AAC, policy result, tenure plan, or investment case.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Input and method

- Dataset: `data/derived/ws4/scanfi-national-990m/dataset`
- Schedule: `data/derived/ws4/sustainable-119m/schedule.csv`
- Run: `data/derived/ws4/sustainable-119m/run_100y`
- Horizon: 100 years, 10 periods of 10 years.
- Period target: 1,189,773,391.0 m3.
- Block volume: sum of fragment area times the block's natural RSYC yield curve at the exact fragment age.
- Block age: fragment-area-weighted age.
- Rotation: integer age of maximum MAI on the natural curve, capped to
  40-200 years and flagged outside that band. Raw peaks
  are {2: 297061, 13: 27, 24: 21732}; all blocks use {40: 318820}.
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
| 0 | 0-9 | 1189.773 | 1193.799 | 0.3384 | 9.620 | 44372 |
| 1 | 10-19 | 1189.773 | 1221.490 | 2.6658 | 8.452 | 27275 |
| 2 | 20-29 | 1189.773 | 1192.381 | 0.2192 | 8.306 | 24402 |
| 3 | 30-39 | 1189.773 | 1198.530 | 0.7360 | 8.381 | 30046 |
| 4 | 40-49 | 1189.773 | 1209.635 | 1.6694 | 8.803 | 34418 |
| 5 | 50-59 | 1189.773 | 1190.648 | 0.0735 | 8.374 | 31822 |
| 6 | 60-69 | 1189.773 | 1206.508 | 1.4066 | 7.816 | 32050 |
| 7 | 70-79 | 1189.773 | 1190.730 | 0.0804 | 8.378 | 29796 |
| 8 | 80-89 | 1189.773 | 1193.295 | 0.2960 | 8.197 | 29524 |
| 9 | 90-99 | 1189.773 | 1191.373 | 0.1344 | 8.021 | 35115 |

- Annual harvest minimum: 119,043,264.5 m3/yr.
- Annual harvest maximum: 122,161,035.7 m3/yr.
- Annual mean: 119,883,890.8 m3/yr.
- Annual CV: 0.008461.
- Period shortfall: 0.0 m3.
- 119 Mm3/yr sustained for 100 years: `True`.
- Selected blocks: 318,820
  (84.348 Mha).
- Blocks reharvested within 100 years: 0.

## 3. Harvest by province

| Province | Control share | Target Mm3/yr | Achieved Mm3/yr | 119 Mm3 basis Mm3/yr | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| BC | 33.602% | 39.978577 | 39.984194 | 39.681837 | 16.424 | 114163 |
| AB | 19.240% | 22.891404 | 22.961879 | 22.788244 | 12.196 | 31963 |
| SK | 3.652% | 4.344698 | 4.522237 | 4.488040 | 4.228 | 14500 |
| MB | 0.954% | 1.135236 | 1.220661 | 1.211430 | 1.343 | 2849 |
| ON | 11.341% | 13.493596 | 13.556790 | 13.454275 | 13.301 | 26015 |
| QC | 22.420% | 26.674334 | 26.803157 | 26.600474 | 28.981 | 96944 |
| NB | 5.240% | 6.234700 | 6.251124 | 6.203854 | 3.498 | 15941 |
| NS | 2.007% | 2.388245 | 2.729855 | 2.709213 | 1.861 | 5502 |
| PE | 0.254% | 0.302210 | 0.305126 | 0.302819 | 0.227 | 1673 |
| NL | 1.222% | 1.454038 | 1.464907 | 1.453830 | 2.189 | 8368 |
| YT | 0.037% | 0.043926 | 0.044803 | 0.044464 | 0.047 | 377 |
| NT | 0.031% | 0.036376 | 0.039157 | 0.038861 | 0.052 | 525 |
| NU | 0.000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0 |

## 4. Chain versus frozen v5.1

| Metric | Unit | v5.1 | 119 Mm3 basis | Delta % | Achieved basis | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 118977339.100000 | 118977339.100000 | -0.0000 | 119883890.801341 | 0.7620 |
| solid_product_m3 | m3 | 37673626.761068 | 37538258.610910 | -0.3593 | 37824282.592170 | 0.3999 |
| sawlog_product_m3 | m3 | 33956989.460016 | 33834975.859433 | -0.3593 | 34092782.557433 | 0.3999 |
| panel_product_m3 | m3 | 3716637.301052 | 3703282.751477 | -0.3593 | 3731500.034737 | 0.3999 |
| pulp_product_odt | odt | 12066311.269557 | 12098448.390798 | 0.2663 | 12190632.911441 | 1.0303 |
| pellet_product_odt | odt | 5229686.166845 | 5291017.027964 | 1.1727 | 5331332.104136 | 1.9436 |
| bio_product_mwh | MWh | 930946.020335 | 941863.639339 | 1.1727 | 949040.199944 | 1.9436 |
| process_residue_m3 | m3 | 59910020.050475 | 59889085.530416 | -0.0349 | 60345412.363660 | 0.7267 |
| process_residue_odt | odt | 26959509.022728 | 26950088.488701 | -0.0349 | 27155435.563662 | 0.7267 |
| process_residue_pj | PJ | 498.750917 | 498.576637 | -0.0349 | 502.375558 | 0.7267 |
| harvest_residue_gross_odt | odt | 24022203.571695 | 24129276.278561 | 0.4457 | 24313130.083226 | 1.2111 |
| harvest_residue_gross_pj | PJ | 444.410766 | 446.391611 | 0.4457 | 449.792907 | 1.2111 |
| harvest_residue_recoverable_r035_odt | odt | 8407771.250102 | 8445246.697505 | 0.4457 | 8509595.529138 | 1.2111 |
| harvest_residue_recoverable_r035_pj | PJ | 155.543768 | 156.237064 | 0.4457 | 157.427517 | 1.2111 |
| harvest_residue_recoverable_r060_odt | odt | 14413322.143027 | 14477565.767147 | 0.4457 | 14587878.049946 | 1.2111 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 267.834967 | 0.4457 | 269.875744 | 1.2111 |
| harvest_residue_recoverable_r075_odt | odt | 18016652.678794 | 18096957.208943 | 0.4457 | 18234847.562442 | 1.2111 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308075 | 334.793708 | 0.4457 | 337.344680 | 1.2111 |
| total_residue_gross_pj | PJ | 943.161683 | 944.968248 | 0.1915 | 952.168464 | 0.9550 |
| total_residue_recoverable_r035_pj | PJ | 654.294685 | 654.813701 | 0.0793 | 659.803075 | 0.8419 |
| total_residue_recoverable_r060_pj | PJ | 765.397377 | 766.411604 | 0.1325 | 772.251302 | 0.8955 |
| total_residue_recoverable_r075_pj | PJ | 832.058991 | 833.370345 | 0.1576 | 839.720238 | 0.9208 |

The `sustainable_119m` basis applies one national factor
(0.992438085757133) to the 100-year annual
average so the total is exactly 118,977,339.1 m3. The
`sustainable_achieved` basis is the unscaled WS4 average
(119,883,890.8 m3/yr).

## 5. National oldest-first free-run sensitivity

The same scheduler without provincial allocation selects
363,447 blocks /
66.710 Mha and sustains the period
target (`True`), but the 100-year harvest is
78.60% BC because BC holds
the oldest inventory. That concentration would change the frozen v5.1
province-weighted residue mix and is therefore reported as a diagnostic, not
used as the chain basis. The province-allocated schedule is the chain basis.

## 6. OSeCAN handoff

The separate `osecan/` artifact applies the existing WS4 origin-province
handoff logic to this chain. It verifies 21/21 frozen v5.1 reference positions,
7/7 119 Mm3 tier positions on both bases, and an unchanged official OSeCAN
tree. See `osecan/FORESTRY_OSECAN_HANDOFF_WS4_SUSTAINABLE.md`.

## 7. Caveats

- The schedule is a national even-flow arithmetic model, not an AAC, policy result, tenure plan, or investment case.
- The full forest estate is used; no operability, tenure, road, slope, or mill-capacity screen is applied.
- Provincial period targets use the frozen 119 Mm3 control shares so the chain and OSeCAN handoff remain comparable with the existing WS4 119 Mm3 lane. A national oldest-first free run is reported as a sensitivity in the report and is not the chain basis.
- Rotation is the integer age of maximum MAI on the RSYC yield curve, capped to 40-200 years; the raw peak is below 40 for these curves and is flagged.
- Whole blocks are selected. Provincial achieved volume can overshoot the target by the final block because no block is split or scaled.
- Frozen chain v5.1 coefficients are applied to the WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- No official OSeCAN file, frozen chain v5.1 artifact, or UI surface is changed.
