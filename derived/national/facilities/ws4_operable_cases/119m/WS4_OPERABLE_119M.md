# Sustainable operable 119 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_operable_119m` **Version:** 1.0.0

**Status:** shortfall. The 118,977,339.1 m3/yr
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

- Dataset: `data/derived/ws4/scanfi-national-990m/dataset`; schedule `data/derived/ws4/operable-119m/schedule.csv`;
  run `data/derived/ws4/operable-119m/run_100y`.
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
| 0 | 0-9 | 1189.773 | 1191.450 | +1.677 | 8.113 | 29,994 |
| 1 | 10-19 | 1189.773 | 1191.292 | +1.518 | 7.768 | 32,088 |
| 2 | 20-29 | 1189.773 | 1229.596 | +39.823 | 8.182 | 32,715 |
| 3 | 30-39 | 1189.773 | 1182.395 | -7.379 | 7.841 | 38,824 |
| 4 | 40-49 | 1189.773 | 987.508 | -202.265 | 6.561 | 32,835 |
| 5 | 50-59 | 1189.773 | 1138.112 | -51.661 | 8.364 | 39,772 |
| 6 | 60-69 | 1189.773 | 1147.671 | -42.103 | 7.587 | 34,426 |
| 7 | 70-79 | 1189.773 | 1121.225 | -68.548 | 7.983 | 37,891 |
| 8 | 80-89 | 1189.773 | 1144.506 | -45.267 | 7.645 | 40,703 |
| 9 | 90-99 | 1189.773 | 983.732 | -206.042 | 6.739 | 33,014 |

- Annual minimum: 97.9475 Mm3/yr.
- Annual maximum: 123.0149 Mm3/yr.
- Annual mean: 113.1749 Mm3/yr.
- Annual CV: 0.069965.
- Period shortfall (national): 623.2648 Mm3.
- Provincial shortfall: 752.8481 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 352,262
  (76.783 Mha treated over 100 years).
- Blocks reharvested within 100 years: 82,582.

Province shortfalls: QC: 5.3432 Mm3/yr, NB: 0.6402 Mm3/yr, NL: 0.5483 Mm3/yr, SK: 0.4109 Mm3/yr, PE: 0.3022 Mm3/yr, NS: 0.2836 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 67.8543 Mm3/yr nominal control (69.2302 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 33.6018% | 39.978577 | 40.058378 | 40.029576 | 22.116 | 16.815 | 119,671 | True |
| AB | 19.2401% | 22.891404 | 22.950805 | 23.044638 | 10.731 | 13.189 | 56,210 | True |
| SK | 3.6517% | 4.344698 | 4.390361 | 3.960007 | 2.648 | 5.374 | 24,425 | False |
| MB | 0.9542% | 1.135236 | 1.205733 | 1.147589 | 2.146 | 1.401 | 5,634 | True |
| ON | 11.3413% | 13.493596 | 13.584388 | 14.807142 | 22.317 | 11.344 | 25,163 | True |
| QC | 22.4197% | 26.674334 | 26.716361 | 21.396317 | 10.501 | 21.791 | 92,495 | False |
| NB | 5.2402% | 6.234700 | 6.286513 | 5.623695 | 1.748 | 3.601 | 15,840 | False |
| NS | 2.0073% | 2.388245 | 2.411311 | 2.118856 | 0.850 | 1.733 | 6,766 | False |
| PE | 0.2540% | 0.302210 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.2221% | 1.454038 | 1.456935 | 0.907504 | 0.673 | 1.381 | 5,462 | False |
| YT | 0.0369% | 0.043926 | 0.047461 | 0.055736 | 1.468 | 0.056 | 266 | True |
| NT | 0.0306% | 0.036376 | 0.036793 | 0.083812 | 0.177 | 0.096 | 330 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 118,977,339.100000 | 119,145,039.011526 | +0.1410 | 113,174,872.830592 | -4.8770 |
| solid_product_m3 | m3 | 37,673,626.761068 | 37,753,282.564585 | +0.2114 | 36,488,810.460976 | -3.1449 |
| sawlog_product_m3 | m3 | 33,956,989.460016 | 34,028,786.935147 | +0.2114 | 32,889,059.502823 | -3.1449 |
| panel_product_m3 | m3 | 3,716,637.301052 | 3,724,495.629438 | +0.2114 | 3,599,750.958153 | -3.1449 |
| pulp_product_odt | odt | 12,066,311.269557 | 12,071,929.346576 | +0.0466 | 11,277,577.630878 | -6.5367 |
| pellet_product_odt | odt | 5,229,686.166845 | 5,249,762.719172 | +0.3839 | 4,910,875.088361 | -6.0962 |
| bio_product_mwh | MWh | 930,946.020335 | 934,519.884214 | +0.3839 | 874,193.875888 | -6.0962 |
| process_residue_m3 | m3 | 59,910,020.050504 | 59,995,390.437027 | +0.1425 | 57,064,482.404177 | -4.7497 |
| process_residue_odt | odt | 26,959,509.022727 | 26,997,925.696677 | +0.1425 | 25,679,017.081893 | -4.7497 |
| process_residue_pj | PJ | 498.750917 | 499.461625 | +0.1425 | 475.061816 | -4.7497 |
| harvest_residue_gross_odt | odt | 24,022,203.571695 | 24,061,778.038307 | +0.1647 | 22,566,116.603281 | -6.0614 |
| harvest_residue_gross_pj | PJ | 444.410766 | 445.142894 | +0.1647 | 417.473157 | -6.0614 |
| harvest_residue_recoverable_r035_odt | odt | 8,407,771.250093 | 8,421,622.313416 | +0.1647 | 7,898,140.811158 | -6.0614 |
| harvest_residue_recoverable_r035_pj | PJ | 155.543768 | 155.800013 | +0.1647 | 146.115605 | -6.0614 |
| harvest_residue_recoverable_r060_odt | odt | 14,413,322.143017 | 14,437,066.822994 | +0.1647 | 13,539,669.961980 | -6.0614 |
| harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 267.085736 | +0.1647 | 250.483894 | -6.0614 |
| harvest_residue_recoverable_r075_odt | odt | 18,016,652.678771 | 18,046,333.528753 | +0.1647 | 16,924,587.452484 | -6.0614 |
| harvest_residue_recoverable_r075_pj | PJ | 333.308075 | 333.857170 | +0.1647 | 313.104868 | -6.0614 |
| total_residue_gross_pj | PJ | 943.161683 | 944.604519 | +0.1530 | 892.534973 | -5.3678 |
| total_residue_recoverable_r035_pj | PJ | 654.294685 | 655.261638 | +0.1478 | 621.177421 | -5.0615 |
| total_residue_recoverable_r060_pj | PJ | 765.397377 | 766.547362 | +0.1502 | 725.545710 | -5.2067 |
| total_residue_recoverable_r075_pj | PJ | 832.058991 | 833.318796 | +0.1514 | 788.166684 | -5.2751 |

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
