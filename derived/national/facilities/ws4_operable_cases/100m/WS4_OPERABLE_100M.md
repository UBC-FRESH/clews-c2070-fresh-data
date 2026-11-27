# Sustainable operable 100 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_operable_100m` **Version:** 1.0.0

**Status:** shortfall. The 100,000,000.1 m3/yr
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

- Dataset: `data/derived/ws4/scanfi-national-990m/dataset`; schedule `data/derived/ws4/operable-100m/schedule.csv`;
  run `data/derived/ws4/operable-100m/run_100y`.
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
| 0 | 0-9 | 1000.000 | 1025.384 | +25.384 | 7.066 | 25,739 |
| 1 | 10-19 | 1000.000 | 1001.009 | +1.009 | 6.490 | 25,111 |
| 2 | 20-29 | 1000.000 | 1002.465 | +2.465 | 6.499 | 28,394 |
| 3 | 30-39 | 1000.000 | 1000.367 | +0.367 | 6.702 | 31,665 |
| 4 | 40-49 | 1000.000 | 975.925 | -24.075 | 6.800 | 31,957 |
| 5 | 50-59 | 1000.000 | 996.759 | -3.241 | 7.738 | 33,039 |
| 6 | 60-69 | 1000.000 | 944.441 | -55.559 | 6.449 | 30,785 |
| 7 | 70-79 | 1000.000 | 971.009 | -28.991 | 6.446 | 34,712 |
| 8 | 80-89 | 1000.000 | 973.196 | -26.804 | 6.609 | 34,875 |
| 9 | 90-99 | 1000.000 | 978.249 | -21.751 | 7.434 | 34,473 |

- Annual minimum: 94.4141 Mm3/yr.
- Annual maximum: 105.4949 Mm3/yr.
- Annual mean: 98.6880 Mm3/yr.
- Annual CV: 0.022061.
- Period shortfall (national): 160.4216 Mm3.
- Provincial shortfall: 259.6635 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 310,750
  (68.234 Mha treated over 100 years).
- Blocks reharvested within 100 years: 71,311.

Province shortfalls: QC: 1.3221 Mm3/yr, NB: 0.6886 Mm3/yr, NL: 0.3285 Mm3/yr, PE: 0.2513 Mm3/yr, NS: 0.0061 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 68.4570 Mm3/yr nominal control (69.3438 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 33.2488% | 33.248823 | 33.468990 | 33.273228 | 22.116 | 14.075 | 99,676 | True |
| AB | 19.0380% | 19.038002 | 19.043423 | 19.062309 | 10.731 | 11.004 | 48,790 | True |
| SK | 3.6133% | 3.613337 | 3.626499 | 3.692417 | 2.648 | 4.738 | 22,389 | True |
| MB | 0.9441% | 0.944137 | 1.041802 | 0.968374 | 2.146 | 1.149 | 4,305 | True |
| ON | 11.2222% | 11.222165 | 11.263703 | 11.846598 | 22.317 | 9.225 | 16,391 | True |
| QC | 22.1841% | 22.184137 | 24.502435 | 21.233945 | 10.501 | 21.371 | 91,420 | False |
| NB | 6.2347% | 6.234700 | 6.291800 | 5.572656 | 1.748 | 3.563 | 15,800 | False |
| NS | 1.9862% | 1.986222 | 2.006001 | 2.018965 | 0.850 | 1.609 | 6,115 | True |
| PE | 0.2513% | 0.251338 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.2093% | 1.209274 | 1.225001 | 0.897845 | 0.673 | 1.367 | 5,413 | False |
| YT | 0.0365% | 0.036532 | 0.037070 | 0.044252 | 1.468 | 0.045 | 208 | True |
| NT | 0.0313% | 0.031333 | 0.031691 | 0.077449 | 0.177 | 0.088 | 243 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 100,000,000.100000 | 102,538,416.376373 | +2.5384 | 98,688,038.668833 | -1.3120 |
| solid_product_m3 | m3 | 31,692,807.151334 | 32,338,131.012287 | +2.0362 | 31,341,215.312687 | -1.1094 |
| sawlog_product_m3 | m3 | 28,566,198.981094 | 29,147,859.347474 | +2.0362 | 28,249,292.928092 | -1.1094 |
| panel_product_m3 | m3 | 3,126,608.170239 | 3,190,271.664813 | +2.0362 | 3,091,922.384595 | -1.1094 |
| pulp_product_odt | odt | 10,136,702.863917 | 10,448,990.662907 | +3.0808 | 9,970,253.391789 | -1.6420 |
| pellet_product_odt | odt | 4,372,287.851260 | 4,478,559.723540 | +2.4306 | 4,370,710.461142 | -0.0361 |
| bio_product_mwh | MWh | 778,318.974606 | 797,236.625382 | +2.4306 | 778,038.180500 | -0.0361 |
| process_residue_m3 | m3 | 50,358,921.112605 | 51,625,600.892936 | +2.5153 | 49,695,540.063828 | -1.3173 |
| process_residue_odt | odt | 22,661,514.500672 | 23,231,520.401834 | +2.5153 | 22,362,993.028734 | -1.3173 |
| process_residue_pj | PJ | 419.238018 | 429.783127 | +2.5153 | 413.715371 | -1.3173 |
| harvest_residue_gross_odt | odt | 20,175,347.205464 | 20,712,499.524689 | +2.6624 | 19,930,145.494163 | -1.2154 |
| harvest_residue_gross_pj | PJ | 373.243923 | 383.181241 | +2.6624 | 368.707692 | -1.2154 |
| harvest_residue_recoverable_r035_odt | odt | 7,061,371.521912 | 7,249,374.833648 | +2.6624 | 6,975,550.922965 | -1.2154 |
| harvest_residue_recoverable_r035_pj | PJ | 130.635373 | 134.113434 | +2.6624 | 129.047692 | -1.2154 |
| harvest_residue_recoverable_r060_odt | odt | 12,105,208.323278 | 12,427,499.714821 | +2.6624 | 11,958,087.296507 | -1.2154 |
| harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 229.908745 | +2.6624 | 221.224615 | -1.2154 |
| harvest_residue_recoverable_r075_odt | odt | 15,131,510.404098 | 15,534,374.643535 | +2.6624 | 14,947,609.120641 | -1.2154 |
| harvest_residue_recoverable_r075_pj | PJ | 279.932942 | 287.385931 | +2.6624 | 276.530769 | -1.2154 |
| total_residue_gross_pj | PJ | 792.481942 | 812.964369 | +2.5846 | 782.423063 | -1.2693 |
| total_residue_recoverable_r035_pj | PJ | 549.873391 | 563.896562 | +2.5503 | 542.763063 | -1.2931 |
| total_residue_recoverable_r060_pj | PJ | 643.184372 | 659.691872 | +2.5665 | 634.939986 | -1.2818 |
| total_residue_recoverable_r075_pj | PJ | 699.170961 | 717.169058 | +2.5742 | 690.246140 | -1.2765 |

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
