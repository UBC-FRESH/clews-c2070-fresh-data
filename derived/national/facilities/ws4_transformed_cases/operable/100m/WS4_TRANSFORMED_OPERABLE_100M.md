# Sustainable operable 100 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_operable_100m` **Version:** 1.0.0

**Status:** shortfall. The 100,000,000.1 m3/yr
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

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed/dataset`; schedule `data/derived/ws4/scanfi-national-990m-transformed/operable-100m/schedule.csv`;
  run `data/derived/ws4/scanfi-national-990m-transformed/operable-100m/run_100y`.
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
| 0 | 0-9 | 1000.000 | 1023.368 | +23.368 | 6.331 | 22,584 |
| 1 | 10-19 | 1000.000 | 1001.053 | +1.053 | 5.826 | 19,963 |
| 2 | 20-29 | 1000.000 | 1008.846 | +8.846 | 5.652 | 21,928 |
| 3 | 30-39 | 1000.000 | 994.165 | -5.835 | 5.653 | 23,612 |
| 4 | 40-49 | 1000.000 | 982.434 | -17.566 | 5.609 | 26,656 |
| 5 | 50-59 | 1000.000 | 1004.639 | +4.639 | 6.161 | 22,885 |
| 6 | 60-69 | 1000.000 | 1000.786 | +0.786 | 5.782 | 26,194 |
| 7 | 70-79 | 1000.000 | 1026.699 | +26.699 | 5.595 | 26,210 |
| 8 | 80-89 | 1000.000 | 1028.445 | +28.445 | 5.757 | 29,745 |
| 9 | 90-99 | 1000.000 | 988.735 | -11.265 | 6.005 | 31,543 |

- Annual minimum: 98.2434 Mm3/yr.
- Annual maximum: 102.8632 Mm3/yr.
- Annual mean: 100.5917 Mm3/yr.
- Annual CV: 0.015116.
- Period shortfall (national): 34.6651 Mm3.
- Provincial shortfall: 67.2620 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 251,320
  (58.370 Mha treated over 100 years).
- Blocks reharvested within 100 years: 62,330.

Province shortfalls: PE: 0.2513 Mm3/yr, NL: 0.2394 Mm3/yr, SK: 0.1693 Mm3/yr, NB: 0.0126 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 76.0498 Mm3/yr nominal control (77.1195 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 33.2488% | 33.248823 | 33.249566 | 33.253533 | 22.116 | 7.786 | 55,069 | True |
| AB | 19.0380% | 19.038002 | 19.388902 | 19.337881 | 10.731 | 9.735 | 43,143 | True |
| SK | 3.6133% | 3.613337 | 3.624824 | 3.460427 | 2.648 | 3.863 | 18,520 | False |
| MB | 0.9441% | 0.944137 | 0.958245 | 0.964680 | 2.146 | 1.017 | 3,741 | True |
| ON | 11.2222% | 11.222165 | 11.237764 | 11.774483 | 22.317 | 9.221 | 16,386 | True |
| QC | 22.1841% | 22.184137 | 24.371838 | 22.447528 | 10.501 | 20.289 | 87,607 | True |
| NB | 6.2347% | 6.234700 | 6.235853 | 6.231228 | 1.748 | 3.528 | 15,581 | False |
| NS | 1.9862% | 1.986222 | 1.986357 | 1.991794 | 0.850 | 1.458 | 5,522 | True |
| PE | 0.2513% | 0.251338 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.2093% | 1.209274 | 1.213288 | 0.986648 | 0.673 | 1.360 | 5,398 | False |
| YT | 0.0365% | 0.036532 | 0.037531 | 0.055564 | 1.468 | 0.032 | 131 | True |
| NT | 0.0313% | 0.031333 | 0.032622 | 0.087949 | 0.177 | 0.082 | 222 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 100,000,000.100000 | 102,336,789.973684 | +2.3368 | 100,591,714.079084 | +0.5917 |
| solid_product_m3 | m3 | 31,692,807.151334 | 32,246,568.280373 | +1.7473 | 31,915,227.415936 | +0.7018 |
| sawlog_product_m3 | m3 | 28,566,198.981094 | 29,065,329.604791 | +1.7473 | 28,766,676.695351 | +0.7018 |
| panel_product_m3 | m3 | 3,126,608.170239 | 3,181,238.675582 | +1.7473 | 3,148,550.720585 | +0.7018 |
| pulp_product_odt | odt | 10,136,702.863917 | 10,437,511.951396 | +2.9675 | 10,195,064.815553 | +0.5757 |
| pellet_product_odt | odt | 4,372,287.851260 | 4,460,660.452067 | +2.0212 | 4,358,016.392056 | -0.3264 |
| bio_product_mwh | MWh | 778,318.974606 | 794,050.343258 | +2.0212 | 775,778.485994 | -0.3264 |
| process_residue_m3 | m3 | 50,358,921.112605 | 51,518,000.502186 | +2.3016 | 50,669,123.321611 | +0.6160 |
| process_residue_odt | odt | 22,661,514.500672 | 23,183,100.225997 | +2.3016 | 22,801,105.494738 | +0.6160 |
| process_residue_pj | PJ | 419.238018 | 428.887354 | +2.3016 | 421.820452 | +0.6160 |
| harvest_residue_gross_odt | odt | 20,175,347.205464 | 20,662,503.599711 | +2.4146 | 20,211,627.261785 | +0.1798 |
| harvest_residue_gross_pj | PJ | 373.243923 | 382.256317 | +2.4146 | 373.915104 | +0.1798 |
| harvest_residue_recoverable_r035_odt | odt | 7,061,371.521912 | 7,231,876.259906 | +2.4146 | 7,074,069.541632 | +0.1798 |
| harvest_residue_recoverable_r035_pj | PJ | 130.635373 | 133.789711 | +2.4146 | 130.870287 | +0.1798 |
| harvest_residue_recoverable_r060_odt | odt | 12,105,208.323278 | 12,397,502.159835 | +2.4146 | 12,126,976.357080 | +0.1798 |
| harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 229.353790 | +2.4146 | 224.349063 | +0.1798 |
| harvest_residue_recoverable_r075_odt | odt | 15,131,510.404098 | 15,496,877.699802 | +2.4146 | 15,158,720.446358 | +0.1798 |
| harvest_residue_recoverable_r075_pj | PJ | 279.932942 | 286.692237 | +2.4146 | 280.436328 | +0.1798 |
| total_residue_gross_pj | PJ | 792.481942 | 811.143671 | +2.3548 | 795.735556 | +0.4106 |
| total_residue_recoverable_r035_pj | PJ | 549.873391 | 562.677065 | +2.3285 | 552.690738 | +0.5124 |
| total_residue_recoverable_r060_pj | PJ | 643.184372 | 658.241144 | +2.3410 | 646.169514 | +0.4641 |
| total_residue_recoverable_r075_pj | PJ | 699.170961 | 715.579592 | +2.3469 | 702.256780 | +0.4414 |

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
