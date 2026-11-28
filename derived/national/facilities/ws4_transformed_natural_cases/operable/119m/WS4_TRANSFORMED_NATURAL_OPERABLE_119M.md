# Sustainable operable 119 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_natural_operable_119m` **Version:** 1.0.0

**Status:** shortfall. The 118,977,339.1 m3/yr
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

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed-natural/dataset`; schedule `data/derived/ws4/scanfi-national-990m-transformed-natural/operable-119m/schedule.csv`;
  run `data/derived/ws4/scanfi-national-990m-transformed-natural/operable-119m/run_100y`.
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
| 0 | 0-9 | 1189.773 | 957.514 | -232.259 | 4.675 | 16,549 |
| 1 | 10-19 | 1189.773 | 861.883 | -327.891 | 4.027 | 13,244 |
| 2 | 20-29 | 1189.773 | 933.218 | -256.556 | 4.515 | 16,678 |
| 3 | 30-39 | 1189.773 | 1053.962 | -135.812 | 4.745 | 17,574 |
| 4 | 40-49 | 1189.773 | 1084.316 | -105.458 | 4.665 | 18,151 |
| 5 | 50-59 | 1189.773 | 1106.451 | -83.322 | 4.827 | 23,693 |
| 6 | 60-69 | 1189.773 | 1081.758 | -108.015 | 4.639 | 27,025 |
| 7 | 70-79 | 1189.773 | 1112.045 | -77.729 | 4.821 | 25,625 |
| 8 | 80-89 | 1189.773 | 1011.754 | -178.020 | 4.355 | 22,775 |
| 9 | 90-99 | 1189.773 | 850.715 | -339.058 | 3.367 | 17,530 |

- Annual minimum: 80.5863 Mm3/yr.
- Annual maximum: 125.4384 Mm3/yr.
- Annual mean: 100.5362 Mm3/yr.
- Annual CV: 0.102492.
- Period shortfall (national): 1,844.1182 Mm3.
- Provincial shortfall: 2,056.0731 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 198,844
  (44.636 Mha treated over 100 years).
- Blocks reharvested within 100 years: 952.

Province shortfalls: QC: 12.8870 Mm3/yr, NB: 2.8159 Mm3/yr, SK: 1.9885 Mm3/yr, NS: 0.9941 Mm3/yr, NL: 0.8676 Mm3/yr, AB: 0.6890 Mm3/yr, PE: 0.3022 Mm3/yr, MB: 0.0165 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 0.0000 Mm3/yr nominal control (0.0000 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 33.6018% | 39.978577 | 39.982585 | 39.982853 | 22.116 | 9.489 | 66,358 | True |
| AB | 19.2401% | 22.891404 | 23.461926 | 22.842152 | 10.731 | 10.545 | 45,871 | False |
| SK | 3.6517% | 4.344698 | 0.501117 | 2.356245 | 2.648 | 2.248 | 10,773 | False |
| MB | 0.9542% | 1.135236 | 0.970247 | 1.153869 | 2.146 | 1.041 | 3,807 | True |
| ON | 11.3413% | 13.493596 | 13.979540 | 14.747393 | 22.317 | 8.368 | 15,912 | True |
| QC | 22.4197% | 26.674334 | 15.950187 | 13.787319 | 10.501 | 9.890 | 44,074 | False |
| NB | 5.2402% | 6.234700 | 0.001706 | 3.498045 | 1.748 | 1.486 | 6,148 | False |
| NS | 2.0073% | 2.388245 | 0.000000 | 1.432728 | 0.850 | 0.774 | 2,856 | False |
| PE | 0.2540% | 0.302210 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.2221% | 1.454038 | 0.821170 | 0.586451 | 0.673 | 0.672 | 2,648 | False |
| YT | 0.0369% | 0.043926 | 0.045119 | 0.057210 | 1.468 | 0.033 | 138 | True |
| NT | 0.0306% | 0.036376 | 0.037839 | 0.091890 | 0.177 | 0.090 | 259 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 118,977,339.100000 | 95,751,436.494809 | -19.5213 | 100,536,156.637608 | -15.4997 |
| solid_product_m3 | m3 | 37,673,626.761068 | 32,783,706.615421 | -12.9797 | 33,759,553.155724 | -10.3894 |
| sawlog_product_m3 | m3 | 33,956,989.460016 | 29,549,477.332258 | -12.9797 | 30,429,053.139861 | -10.3894 |
| panel_product_m3 | m3 | 3,716,637.301052 | 3,234,229.283162 | -12.9797 | 3,330,500.015863 | -10.3894 |
| pulp_product_odt | odt | 12,066,311.269557 | 9,138,811.020378 | -24.2618 | 9,674,252.544352 | -19.8243 |
| pellet_product_odt | odt | 5,229,686.166845 | 3,189,004.780499 | -39.0211 | 3,950,568.757250 | -24.4588 |
| bio_product_mwh | MWh | 930,946.020335 | 567,680.586276 | -39.0211 | 703,247.985689 | -24.4588 |
| process_residue_m3 | m3 | 59,910,020.050504 | 48,656,861.341286 | -18.7834 | 50,910,567.412984 | -15.0216 |
| process_residue_odt | odt | 26,959,509.022727 | 21,895,587.603589 | -18.7834 | 22,909,755.335854 | -15.0216 |
| process_residue_pj | PJ | 498.750917 | 405.068371 | -18.7834 | 423.830474 | -15.0216 |
| harvest_residue_gross_odt | odt | 24,022,203.571695 | 17,324,349.637760 | -27.8819 | 19,170,965.552423 | -20.1948 |
| harvest_residue_gross_pj | PJ | 444.410766 | 320.500468 | -27.8819 | 354.662863 | -20.1948 |
| harvest_residue_recoverable_r035_odt | odt | 8,407,771.250093 | 6,063,522.373225 | -27.8819 | 6,709,837.943357 | -20.1948 |
| harvest_residue_recoverable_r035_pj | PJ | 155.543768 | 112.175164 | -27.8819 | 124.132002 | -20.1948 |
| harvest_residue_recoverable_r060_odt | odt | 14,413,322.143017 | 10,394,609.782671 | -27.8819 | 11,502,579.331467 | -20.1948 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 192.300281 | -27.8819 | 212.797718 | -20.1948 |
| harvest_residue_recoverable_r075_odt | odt | 18,016,652.678771 | 12,993,262.228345 | -27.8819 | 14,378,224.164341 | -20.1948 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308075 | 240.375351 | -27.8819 | 265.997147 | -20.1948 |
| total_residue_gross_pj | PJ | 943.161683 | 725.568839 | -23.0706 | 778.493336 | -17.4592 |
| total_residue_recoverable_r035_pj | PJ | 654.294685 | 517.243535 | -20.9464 | 547.962476 | -16.2514 |
| total_residue_recoverable_r060_pj | PJ | 765.397377 | 597.368652 | -21.9531 | 636.628191 | -16.8238 |
| total_residue_recoverable_r075_pj | PJ | 832.058991 | 645.443722 | -22.4281 | 689.827621 | -17.0939 |

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
