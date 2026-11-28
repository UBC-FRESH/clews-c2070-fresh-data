# WS4 sustainable and operable cases on natural-only RSYC curves

**Artifact:** `ws4_transformed_natural_cases` **Version:** 1.0.0

**Status:** pass. The 100, 119, and 150 Mm3/yr sustainable cases
and the 100, 119, and 150 Mm3/yr operable cases were rerun on the corrected
natural-only dataset. All outputs are model estimates, not AACs, policy
results, tenure plans, legal THLB determinations, official OSeCAN changes, or
national supply claims.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`, `transformed_curves=true`, `natural_5param_only=true`, `managed_basis_quarantined=true`, `official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Corrected dataset

- Dataset: `data/derived/ws4/scanfi-national-990m-transformed-natural/dataset`.
- Curve basis: natural 5-parameter only; the 1,926
  managed-basis cell curves are quarantined and replaced by natural donors.
- WS4 curves mapped: 718 of
  719 referenced
  (curve 1 unreferenced).
- Natural cell curves aggregated: 3,948.
- V100 max error: 0.000500 m3/ha
  (tolerance 0.01 m3/ha).
- WS4 validate: `Dataset is valid`.
- Managed tracks share the natural curve; there is no planting response.

## 2. Sustainable 100/119/150 Mm3/yr

| Case | Target Mm3/yr | Annual min Mm3/yr | Annual max Mm3/yr | Annual mean Mm3/yr | Annual CV | Period shortfall Mm3 | Sustained | Blocks | Area Mha | Reharvests | Mean rotation yr |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 100.000000 | 99.7850 | 106.7019 | 101.6670 | 0.020148 | 0.000000 | True | 164,139 | 46.813 | 0 | 109.850 |
| 119m | 118.977339 | 118.8756 | 124.6452 | 120.5726 | 0.013894 | 0.000000 | True | 204,771 | 55.071 | 0 | 110.031 |
| 150m | 150.000000 | 149.9350 | 162.5736 | 153.4328 | 0.023291 | 0.000000 | True | 245,380 | 72.380 | 0 | 110.324 |

All cases use the unchanged 100-year whole-block scheduler with the frozen
provincial allocated shares. Period shortfall is the national 10-year target
gap. Whole blocks are never split, scaled, or harvested below rotation.

## 3. Chain versus frozen v5.1

The chain applies frozen v5.1 per-province coefficients to the first-period
annual average (primary) and the 100-year achieved annual average (secondary).
Reference values are the frozen v5.1 case targets. Full metric tables are in
`comparison_sustainable_vs_v51.csv` and each case `chain` directory.

## 4. Operable 100/119/150 Mm3/yr

| Case | Target Mm3/yr | Annual min Mm3/yr | Annual max Mm3/yr | Annual mean Mm3/yr | Period shortfall Mm3 | Province shortfall Mm3 | Sustained | Covered sustained | Blocks | Area Mha | Max nominal Mm3/yr | Max operable Mm3/yr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 100.000000 | 73.0999 | 99.4616 | 86.9061 | 1309.3890 | 1418.8131 | False | False | 172,210 | 38.957 | 0.0000 | 0.0000 |
| 119m | 118.977339 | 80.5863 | 125.4384 | 100.5362 | 1844.1182 | 2056.0731 | False | False | 198,844 | 44.636 | 0.0000 | 0.0000 |
| 150m | 150.000000 | 88.1912 | 128.7428 | 111.2426 | 3875.7402 | 3957.6383 | False | False | 221,091 | 49.773 | 0.0000 | 0.0000 |

The operable landbase is the unchanged `screen_core30` province-share mask:
370,752 blocks,
75.374 Mha. It is
an area-share proxy, not a legal THLB, slope screen, or spatial road overlay.
Provincial shortfalls are retained and the cross-province fallback is disabled.
No target is forced; the schedule-only maximum sustainable level is reported.

## 5. OSeCAN handoff

Sustainable 100/119/150: frozen v5.1 21/21; 100m primary 7/7, achieved 7/7; 119m primary 7/7, achieved 7/7; 150m primary 7/7, achieved 7/7. Operable 100/119/150: frozen v5.1 21/21; 100m primary 4/7, achieved 5/7; 119m primary 3/7, achieved 3/7; 150m primary 5/7, achieved 5/7. Official OSeCAN is unchanged:
`sustainable=True`,
`operable=True`.

## 6. CMAI diagnostics for the corrected natural curves

| Subset | Group | n | Area Mha | Natural CMAI median | Natural CMAI age median | Raw CMAI median | Expected floor | Natural share >= floor | Raw share >= floor |
|---|---|---|---|---|---|---|---|---|---|
| overall | conifer | 3,393 | 339.826 | 0.950 | 111 | 2.266 | 1.25 | 35.6% | 79.6% |
| area_weighted | conifer | 3,393 | 339.826 | 1.084 | 154 | 1.813 | 1.25 | 35.6% | 79.6% |
| bc | conifer | 420 | 60.088 | 2.309 | 111 | 6.000 | 1.25 | 84.5% | 99.5% |
| productive_raw | conifer | 2,700 | 241.922 | 1.175 | 111 | 2.782 | 1.25 | 44.8% | 100.0% |
| productive_v100_q50 | conifer | 1,699 | 178.027 | 1.584 | 111 | 3.867 | 1.25 | 71.2% | 100.0% |
| productive_v100_q75 | conifer | 859 | 91.019 | 2.048 | 111 | 5.107 | 1.25 | 100.0% | 100.0% |
| overall | deciduous | 555 | 82.650 | 1.114 | 119 | 2.119 | 1.75 | 26.8% | 59.5% |
| area_weighted | deciduous | 555 | 82.650 | 1.761 | 119 | 3.349 | 1.75 | 26.8% | 59.5% |
| bc | deciduous | 65 | 6.520 | 2.357 | 119 | 4.151 | 1.75 | 75.4% | 96.9% |
| productive_raw | deciduous | 330 | 73.490 | 1.641 | 119 | 3.103 | 1.75 | 45.2% | 100.0% |
| productive_v100_q50 | deciduous | 278 | 69.803 | 1.829 | 119 | 3.426 | 1.75 | 53.6% | 100.0% |
| productive_v100_q75 | deciduous | 139 | 40.185 | 2.136 | 119 | 4.024 | 1.75 | 100.0% | 100.0% |
| ws4_model_area_weighted | all | 1,575 | 422.476 | 1.217 | 130 | n/a | n/a | n/a | n/a |

`overall` is the unweighted cell-curve median, `area_weighted` weights each
cell by RSYC area, `bc` is the BC subset, `productive_raw` is the subset whose
raw RSYC CMAI is at or above the expected natural floor (conifer 1.25,
deciduous 1.75 m3/ha/yr), and `ws4_model_area_weighted` is the 718 model curves
weighted by model area. The low overall median is driven by northern
low-productivity curves; BC and productive subsets sit inside the expected
natural ranges.

## 7. Comparison to the quarantined managed-basis feed

`comparison_sustainable_natural_vs_managed_basis.csv` and
`comparison_operable_vs_managed_basis.csv` show the correction effect for the
schedule metrics. The managed-basis rows are retained, labelled, and never used
as total volume.

## 8. Integrity

- Frozen chain v5.1 unchanged: `True`.
- Official OSeCAN unchanged: `True`.
- Original dataset unchanged: `True`.
- Old transformed dataset unchanged:
  `True`.
- No unexpected deletion: `True`.

## 9. Caveats

- RSYC is a total-volume curve. The natural transform repairs shape and
  preserves V100; it is not a merchantable-volume conversion.
- Natural donor shapes are matched by ecoprovince, ecozone, then BC species
  group. For eastern provinces without a local natural donor, the BC province
  fallback is distant and flagged in provenance.
- The full-forest cases use the whole 411.25 Mha estate with no operability,
  tenure, road, slope, or mill-capacity screen. The operable cases use an
  area-share proxy with no legal THLB, national slope DEM, or spatial
  road/tenure overlay.
- Demo schedules are model estimates, not AACs, policy supply, or investment
  cases. No national supply claim is made.
