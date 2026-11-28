# Transformed-curve WS4 sustainable and operable cases

**Artifact:** `ws4_transformed_cases` **Version:** 1.0.0

**Status:** pass. The 100 and 150 Mm3/yr sustainable cases and
the 100, 119, and 150 Mm3/yr operable cases were rerun on the transformed
national RSYC curves. All outputs are model estimates, not AACs, policy
results, tenure plans, legal THLB determinations, official OSeCAN changes, or
national supply claims.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`transformed_curves=true`, `official_osecan_changed=false`,
`chain_v51_unchanged=true`.

## 1. Dataset

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed/dataset`.
- Curve patch: 718 WS4 curves
  mapped to 718 RSYC models from
  3948 transformed cell
  curves.
- V100 max error: 0.000500 m3/ha
  (tolerance 0.01 m3/ha).
- WS4 validate: `Dataset is valid`.

## 2. Sustainable 100/150 Mm3/yr

| Case | Target Mm3/yr | Annual min Mm3/yr | Annual max Mm3/yr | Annual mean Mm3/yr | Period shortfall Mm3 | Sustained | Blocks | Area Mha | Mean rotation yr |
|---|---|---|---|---|---|---|---|---|---|
| 100m | 100.000000 | 100.2499 | 103.1923 | 101.1221 | 0.000000 | True | 212,570 | 61.733 | 53.447 |
| 150m | 150.000000 | 150.5393 | 153.8005 | 151.6402 | 0.000000 | True | 313,862 | 93.151 | 53.748 |

Both cases use the unchanged 100-year whole-block scheduler with the frozen
provincial allocated shares. Period shortfall is the national 10-year target
gap; the annual floor is reported against the nominal annual rate.

## 3. Chain versus frozen v5.1

| Case | Metric | Unit | v5.1 | First period | Delta % | Achieved | Delta % |
|---|---|---|---|---|---|---|---|
| 100m | harvest_m3 | m3 | 100,000,000.100000 | 100,710,612.145284 | +0.7106 | 101,122,055.001091 | +1.1221 |
| 100m | solid_product_m3 | m3 | 31,692,807.151334 | 31,855,830.870359 | +0.5144 | 31,915,916.256395 | +0.7040 |
| 100m | pulp_product_odt | odt | 10,136,702.863917 | 10,220,847.937901 | +0.8301 | 10,286,376.089621 | +1.4765 |
| 100m | process_residue_pj | PJ | 419.238018 | 422.093335 | +0.6811 | 423.797376 | +1.0875 |
| 100m | harvest_residue_gross_pj | PJ | 373.243923 | 376.674317 | +0.9191 | 378.847821 | +1.5014 |
| 100m | harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 226.004590 | +0.9191 | 227.308693 | +1.5014 |
| 100m | total_residue_gross_pj | PJ | 792.481942 | 798.767652 | +0.7932 | 802.645197 | +1.2825 |
| 150m | harvest_m3 | m3 | 150,000,000.200000 | 153,800,473.489748 | +2.5336 | 151,640,202.795479 | +1.0935 |
| 150m | solid_product_m3 | m3 | 46,136,665.718213 | 46,740,796.879038 | +1.3094 | 46,496,333.428212 | +0.7796 |
| 150m | pulp_product_odt | odt | 15,550,881.011045 | 16,125,857.615050 | +3.6974 | 15,764,755.001192 | +1.3753 |
| 150m | process_residue_pj | PJ | 626.865219 | 642.494523 | +2.4932 | 633.598663 | +1.0741 |
| 150m | harvest_residue_gross_pj | PJ | 573.125413 | 593.300131 | +3.5201 | 580.444232 | +1.2770 |
| 150m | harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 355.980079 | +3.5201 | 348.266539 | +1.2770 |
| 150m | total_residue_gross_pj | PJ | 1,199.990632 | 1,235.794654 | +2.9837 | 1,214.042894 | +1.1710 |

The first-period basis applies frozen v5.1 per-province coefficients to the
annual average of offsets 0-9. The achieved basis applies them to the 100-year
annual average. Reference values are the frozen v5.1 100/150 Mm3 targets.

## 4. Operable cases 100/119/150 Mm3/yr

| Case | Target Mm3/yr | Annual min | Annual max | Annual mean | Period shortfall Mm3 | Province shortfall Mm3 | Sustained | Covered sustained | Blocks | Area Mha | Max nominal Mm3/yr | Max operable Mm3/yr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 100.000000 | 98.2434 | 102.8632 | 100.5917 | 34.6651 | 67.2620 | False | False | 251,320 | 58.370 | 76.0498 | 77.1195 |
| 119m | 118.977339 | 102.6644 | 122.8093 | 116.0305 | 377.7192 | 457.3300 | False | False | 285,948 | 66.370 | 76.2780 | 77.0942 |
| 150m | 150.000000 | 104.4241 | 150.9391 | 133.6562 | 1645.1650 | 1761.3301 | False | False | 330,938 | 76.337 | 68.4448 | 70.3013 |

The operable landbase is the existing `screen_core30` province-share mask:
370,752 blocks,
75.374 Mha.
The mask is an area-share proxy, not a legal THLB, slope screen, or spatial
road overlay. Provincial shortfalls are retained and the cross-province
fallback is disabled.

## 5. OSeCAN handoff

Sustainable 100/150: frozen v5.1 21/21; 100m primary 7/7, achieved 7/7; 150m primary 7/7, achieved 7/7. Operable 100/119/150: frozen v5.1 21/21; 100m primary 6/7, achieved 7/7; 119m primary 7/7, achieved 6/7; 150m primary 7/7, achieved 6/7. Official OSeCAN is unchanged in both builds:
`sustainable=True`,
`operable=True`.

## 6. Integrity

- Frozen chain v5.1 unchanged: `True`.
- Official OSeCAN unchanged: `True`.
- Original dataset unchanged: `True`.
- Unexpected deletion status: `True`.

## 7. Caveats

- Yield curves are the national RSYC transform v1: V100 is preserved, ages 1-200 are transformed, and ages 201-600 are held at the age-200 value. The WS4 model curve is the forest-area-weighted mean of transformed cell curves.
- The scheduler, provincial control shares, 100-year horizon, 10-year periods, MAI rotation band (40-200 years), oldest-first whole-block selection, and annual longest-processing-time assignment are unchanged.
- The full-forest sustainable cases use the whole WS4 estate. The operable cases use the existing screen_core30 province-share mask; it is not a legal THLB, a slope screen, or a spatial road overlay.
- Whole blocks are selected and never split or scaled; a final block may overshoot a provincial target. No block is harvested below rotation and rotation is never relaxed to meet a target.
- Frozen chain v5.1 coefficients are applied to WS4 harvest by origin province. Facility assignment, mill capacity, transport, and interprovincial trade are not re-run.
- The OSeCAN handoff applies frozen handoff-v10 zone weights and the official tier thresholds. It is a model estimate, not an official OSeCAN change.
- No original national 990 m dataset, original-curve case artifact, frozen chain v5.1 artifact, official OSeCAN file, or UI surface is changed.
