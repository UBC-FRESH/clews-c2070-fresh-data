# Sustainable operable 119 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_operable_119m` **Version:** 1.0.0

**Status:** shortfall. The 118,977,339.1 m3/yr
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

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed/dataset`; schedule `data/derived/ws4/scanfi-national-990m-transformed/operable-119m/schedule.csv`;
  run `data/derived/ws4/scanfi-national-990m-transformed/operable-119m/run_100y`.
- Horizon: 100 years, 10 periods of 10 years.
- Eligible: operable-mask block and age at harvest >= MAI rotation
  (40-200 years).
- Selection: whole blocks, oldest-first, volume-aware, within the frozen
  119m provincial allocated shares; no block split, scaled, or harvested
  below rotation.
- If a province cannot meet its period target, the shortfall is recorded and
  the schedule continues. The cross-province national fallback is disabled.
- Annual assignment: longest-processing-time balancing over the ten offsets
  of each period.

## 3. Period harvest

| Period | Offsets | Target Mm3 | Achieved Mm3 | Delta Mm3 | Area Mha | Blocks |
|---|---|---|---|---|---|---|
| 0 | 0-9 | 1189.773 | 1191.105 | +1.332 | 7.304 | 25,530 |
| 1 | 10-19 | 1189.773 | 1189.951 | +0.177 | 6.890 | 25,639 |
| 2 | 20-29 | 1189.773 | 1214.799 | +25.026 | 6.954 | 24,676 |
| 3 | 30-39 | 1189.773 | 1157.017 | -32.756 | 6.282 | 30,193 |
| 4 | 40-49 | 1189.773 | 1036.255 | -153.519 | 5.423 | 24,474 |
| 5 | 50-59 | 1189.773 | 1207.973 | +18.200 | 7.521 | 31,859 |
| 6 | 60-69 | 1189.773 | 1228.002 | +38.229 | 6.760 | 30,022 |
| 7 | 70-79 | 1189.773 | 1189.845 | +0.072 | 6.908 | 33,532 |
| 8 | 80-89 | 1189.773 | 1161.150 | -28.623 | 6.674 | 32,137 |
| 9 | 90-99 | 1189.773 | 1026.952 | -162.821 | 5.654 | 27,886 |

- Annual minimum: 102.6644 Mm3/yr.
- Annual maximum: 122.8093 Mm3/yr.
- Annual mean: 116.0305 Mm3/yr.
- Annual CV: 0.058267.
- Period shortfall (national): 377.7192 Mm3.
- Provincial shortfall: 457.3300 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 285,948
  (66.370 Mha treated over 100 years).
- Blocks reharvested within 100 years: 72,515.

Province shortfalls: QC: 2.8732 Mm3/yr, SK: 0.8936 Mm3/yr, NL: 0.4583 Mm3/yr, PE: 0.3022 Mm3/yr, NS: 0.0432 Mm3/yr, NB: 0.0028 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 76.2780 Mm3/yr nominal control (77.0942 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 33.6018% | 39.978577 | 39.982585 | 39.982853 | 22.116 | 9.489 | 66,358 | True |
| AB | 19.2401% | 22.891404 | 23.254873 | 23.173125 | 10.731 | 12.217 | 50,775 | True |
| SK | 3.6517% | 4.344698 | 4.357740 | 3.467942 | 2.648 | 3.867 | 18,551 | False |
| MB | 0.9542% | 1.135236 | 1.154337 | 1.165293 | 2.146 | 1.254 | 4,997 | True |
| ON | 11.3413% | 13.493596 | 13.499592 | 14.703738 | 22.317 | 11.330 | 25,129 | True |
| QC | 22.4197% | 26.674334 | 26.681339 | 23.802491 | 10.501 | 21.477 | 92,080 | False |
| NB | 5.2402% | 6.234700 | 6.235853 | 6.241530 | 1.748 | 3.530 | 15,522 | True |
| NS | 2.0073% | 2.388245 | 2.406863 | 2.349213 | 0.850 | 1.715 | 6,699 | False |
| PE | 0.2540% | 0.302210 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.2221% | 1.454038 | 1.454763 | 0.996070 | 0.673 | 1.370 | 5,440 | False |
| YT | 0.0369% | 0.043926 | 0.045008 | 0.057100 | 1.468 | 0.033 | 138 | True |
| NT | 0.0306% | 0.036376 | 0.037588 | 0.091155 | 0.177 | 0.090 | 259 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 118,977,339.100000 | 119,110,540.863327 | +0.1120 | 116,030,509.304327 | -2.4768 |
| solid_product_m3 | m3 | 37,673,626.761068 | 37,734,656.240074 | +0.1620 | 37,293,264.823729 | -1.0096 |
| sawlog_product_m3 | m3 | 33,956,989.460016 | 34,011,998.163811 | +0.1620 | 33,614,151.580905 | -1.0096 |
| panel_product_m3 | m3 | 3,716,637.301052 | 3,722,658.076264 | +0.1620 | 3,679,113.242824 | -1.0096 |
| pulp_product_odt | odt | 12,066,311.269557 | 12,073,987.345619 | +0.0636 | 11,641,636.822471 | -3.5195 |
| pellet_product_odt | odt | 5,229,686.166845 | 5,228,555.772710 | -0.0216 | 4,875,404.738156 | -6.7744 |
| bio_product_mwh | MWh | 930,946.020335 | 930,744.796803 | -0.0216 | 867,879.733832 | -6.7744 |
| process_residue_m3 | m3 | 59,910,020.050504 | 59,977,499.538074 | +0.1126 | 58,532,124.457155 | -2.2999 |
| process_residue_odt | odt | 26,959,509.022727 | 26,989,874.792148 | +0.1126 | 26,339,456.005733 | -2.2999 |
| process_residue_pj | PJ | 498.750917 | 499.312684 | +0.1126 | 487.279936 | -2.2999 |
| harvest_residue_gross_odt | odt | 24,022,203.571695 | 24,030,174.915663 | +0.0332 | 22,976,998.539917 | -4.3510 |
| harvest_residue_gross_pj | PJ | 444.410766 | 444.558236 | +0.0332 | 425.074473 | -4.3510 |
| harvest_residue_recoverable_r035_odt | odt | 8,407,771.250093 | 8,410,561.220491 | +0.0332 | 8,041,949.488980 | -4.3510 |
| harvest_residue_recoverable_r035_pj | PJ | 155.543768 | 155.595383 | +0.0332 | 148.776066 | -4.3510 |
| harvest_residue_recoverable_r060_odt | odt | 14,413,322.143017 | 14,418,104.949408 | +0.0332 | 13,786,199.123962 | -4.3510 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 266.734942 | +0.0332 | 255.044684 | -4.3510 |
| harvest_residue_recoverable_r075_odt | odt | 18,016,652.678771 | 18,022,631.186770 | +0.0332 | 17,232,748.904961 | -4.3510 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308075 | 333.418677 | +0.0332 | 318.805855 | -4.3510 |
| total_residue_gross_pj | PJ | 943.161683 | 943.870920 | +0.0752 | 912.354409 | -3.2664 |
| total_residue_recoverable_r035_pj | PJ | 654.294685 | 654.908066 | +0.0937 | 636.056002 | -2.7875 |
| total_residue_recoverable_r060_pj | PJ | 765.397377 | 766.047625 | +0.0850 | 742.324620 | -3.0145 |
| total_residue_recoverable_r075_pj | PJ | 832.058991 | 832.731361 | +0.0808 | 806.085791 | -3.1216 |

The comparison reference is the frozen full-forest v5.1 case total for
`119m` in `data/derived/national/facilities/national_facility_chain_scenarios_v9/scenario_summary.csv`. The primary operable basis is
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
- Provincial period targets use the frozen 119m allocated_share values. A province that cannot meet its target records a shortfall; the cross-province fallback is disabled.
- Rotation is the integer age of maximum MAI on the RSYC yield curve, capped to 40-200 years; the raw peak is flagged. Rotation is never relaxed to meet a target.
- Frozen chain v5.1 coefficients are applied to operable WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- The max-sustainable level is a schedule-only diagnostic with the same provincial shares and mask; it is not a WS4-simulated or policy-tested level.
- NU and PE have no 2016 tenure coverage. No operable block is selected there; their shortfalls are reported, not substituted with harvested volume.
- No legal THLB, slope screen, spatial road screen, official OSeCAN change, chain v5.1 mutation, or UI change is claimed.
