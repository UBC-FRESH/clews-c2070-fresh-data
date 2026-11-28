# Sustainable operable 150 Mm3/yr WS4 Schedule and Chain

**Artifact:** `ws4_transformed_natural_operable_150m` **Version:** 1.0.0

**Status:** shortfall. The 150,000,000.2 m3/yr
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

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed-natural/dataset`; schedule `data/derived/ws4/scanfi-national-990m-transformed-natural/operable-150m/schedule.csv`;
  run `data/derived/ws4/scanfi-national-990m-transformed-natural/operable-150m/run_100y`.
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
| 0 | 0-9 | 1500.000 | 1120.080 | -379.920 | 5.497 | 19,011 |
| 1 | 10-19 | 1500.000 | 881.912 | -618.088 | 4.058 | 14,477 |
| 2 | 20-29 | 1500.000 | 1124.869 | -375.131 | 5.645 | 18,496 |
| 3 | 30-39 | 1500.000 | 1255.732 | -244.268 | 5.430 | 19,296 |
| 4 | 40-49 | 1500.000 | 1287.428 | -212.572 | 5.805 | 29,330 |
| 5 | 50-59 | 1500.000 | 1210.378 | -289.622 | 5.264 | 25,981 |
| 6 | 60-69 | 1500.000 | 1156.932 | -343.068 | 4.834 | 23,390 |
| 7 | 70-79 | 1500.000 | 1097.652 | -402.348 | 4.907 | 24,137 |
| 8 | 80-89 | 1500.000 | 1020.307 | -479.693 | 4.479 | 23,026 |
| 9 | 90-99 | 1500.000 | 968.969 | -531.031 | 3.853 | 23,947 |

- Annual minimum: 88.1912 Mm3/yr.
- Annual maximum: 128.7428 Mm3/yr.
- Annual mean: 111.2426 Mm3/yr.
- Annual CV: 0.108385.
- Period shortfall (national): 3,875.7402 Mm3.
- Provincial shortfall: 3,957.6383 Mm3.
- Sustained (all 13 targets): `False`.
- Sustained on covered provinces: `False`.
- Selected blocks: 221,091
  (49.773 Mha treated over 100 years).
- Blocks reharvested within 100 years: 1,762.

Province shortfalls: QC: 20.3139 Mm3/yr, AB: 7.8321 Mm3/yr, SK: 4.1050 Mm3/yr, NB: 2.8162 Mm3/yr, NS: 2.0517 Mm3/yr, NL: 1.4246 Mm3/yr, ON: 0.5096 Mm3/yr, PE: 0.4494 Mm3/yr, MB: 0.0739 Mm3/yr.

The same provincial shares and mask reach a schedule-only maximum of 0.0000 Mm3/yr nominal control (0.0000 Mm3/yr operable harvest) when jurisdictions without operable coverage are excluded from the adequacy test.

## 4. Harvest by province

| Province | Control share | Target Mm3/yr | First period Mm3/yr | 100-year Mm3/yr | Mask Mha | Area Mha | Blocks | 100-year target met |
|---|---|---|---|---|---|---|---|---|
| BC | 30.1493% | 45.223878 | 45.228064 | 45.228659 | 22.116 | 10.783 | 75,551 | True |
| AB | 20.0667% | 30.100000 | 30.037402 | 22.485903 | 10.731 | 10.767 | 46,681 | False |
| SK | 4.3068% | 6.460155 | 0.500943 | 2.355105 | 2.648 | 2.248 | 10,773 | False |
| MB | 1.1253% | 1.687988 | 0.965134 | 1.748159 | 2.146 | 1.618 | 6,377 | True |
| ON | 13.3758% | 20.063703 | 18.385483 | 19.861778 | 22.317 | 11.331 | 25,133 | False |
| QC | 22.7435% | 34.115200 | 15.962329 | 13.801348 | 10.501 | 9.890 | 44,074 | False |
| NB | 4.1565% | 6.234700 | 0.001654 | 3.496448 | 1.748 | 1.486 | 6,148 | False |
| NS | 2.3674% | 3.551095 | 0.000000 | 1.502647 | 0.850 | 0.840 | 3,224 | False |
| PE | 0.2996% | 0.449358 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | False |
| NL | 1.3415% | 2.012233 | 0.819530 | 0.587667 | 0.673 | 0.672 | 2,648 | False |
| YT | 0.0435% | 0.065314 | 0.070148 | 0.083166 | 1.468 | 0.048 | 223 | True |
| NT | 0.0243% | 0.036376 | 0.037308 | 0.091718 | 0.177 | 0.090 | 259 | True |
| NU | 0.0000% | 0.000000 | 0.000000 | 0.000000 | 0.000 | 0.000 | 0 | True |

## 5. Chain versus frozen v5.1 full-forest case

| Metric | Unit | v5.1 full-forest | Operable first period | Delta % | Operable achieved | Delta % |
|---|---|---|---|---|---|---|
| harvest_m3 | m3 | 150,000,000.200000 | 112,007,995.218803 | -25.3280 | 111,242,597.954570 | -25.8383 |
| solid_product_m3 | m3 | 46,136,665.718213 | 38,249,335.872960 | -17.0956 | 37,747,732.310001 | -18.1828 |
| sawlog_product_m3 | m3 | 41,585,119.517419 | 34,475,902.819980 | -17.0956 | 34,023,784.232924 | -18.1828 |
| panel_product_m3 | m3 | 4,551,546.200794 | 3,773,433.052980 | -17.0956 | 3,723,948.077077 | -18.1828 |
| pulp_product_odt | odt | 15,550,881.011045 | 10,720,969.013452 | -31.0588 | 10,575,457.846391 | -31.9945 |
| pellet_product_odt | odt | 7,038,938.165569 | 3,695,580.909713 | -47.4980 | 4,466,628.837593 | -36.5440 |
| bio_product_mwh | MWh | 1,253,014.284904 | 657,857.131568 | -47.4980 | 795,112.786506 | -36.5440 |
| process_residue_m3 | m3 | 75,299,125.458469 | 56,890,869.354219 | -24.4468 | 56,403,389.833263 | -25.0942 |
| process_residue_odt | odt | 33,884,606.456311 | 25,600,891.209409 | -24.4468 | 25,381,525.424979 | -25.0942 |
| process_residue_pj | PJ | 626.865219 | 473.616487 | -24.4468 | 469.558220 | -25.0942 |
| harvest_residue_gross_odt | odt | 30,979,752.054305 | 20,156,549.277005 | -34.9364 | 21,182,110.528562 | -31.6260 |
| harvest_residue_gross_pj | PJ | 573.125413 | 372.896162 | -34.9364 | 391.869045 | -31.6260 |
| harvest_residue_recoverable_r035_odt | odt | 10,842,913.219007 | 7,054,792.246964 | -34.9364 | 7,413,738.685006 | -31.6260 |
| harvest_residue_recoverable_r035_pj | PJ | 200.593895 | 130.513657 | -34.9364 | 137.154166 | -31.6260 |
| harvest_residue_recoverable_r060_odt | odt | 18,587,851.232583 | 12,093,929.566222 | -34.9364 | 12,709,266.317151 | -31.6260 |
| harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 223.737697 | -34.9364 | 235.121427 | -31.6260 |
| harvest_residue_recoverable_r075_odt | odt | 23,234,814.040728 | 15,117,411.957786 | -34.9364 | 15,886,582.896447 | -31.6260 |
| harvest_residue_recoverable_r075_pj | PJ | 429.844060 | 279.672121 | -34.9364 | 293.901784 | -31.6260 |
| total_residue_gross_pj | PJ | 1,199.990632 | 846.512649 | -29.4567 | 861.427265 | -28.2138 |
| total_residue_recoverable_r035_pj | PJ | 827.459114 | 604.130144 | -26.9897 | 606.712386 | -26.6777 |
| total_residue_recoverable_r060_pj | PJ | 970.740467 | 697.354184 | -28.1627 | 704.679647 | -27.4080 |
| total_residue_recoverable_r075_pj | PJ | 1,056.709279 | 753.288609 | -28.7137 | 763.460004 | -27.7512 |

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
