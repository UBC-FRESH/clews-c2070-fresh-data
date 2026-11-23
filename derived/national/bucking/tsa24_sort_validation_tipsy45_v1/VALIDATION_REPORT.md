# TSA24 pilot industrial-sort validation tipsy45_v1
| Field | Value |
|---|---|
| Validation | `industrial_sort_validation` |
| TSA | 24 — Prince George |
| Generated (UTC) | 2026-11-23T00:58:07+00:00 |
| Grade status | `not_assigned` |
| Evidence label | `industrial_sort_validation` |
| Sample | 558 plots, 35,589 logs, 20,053 bucked trees |
| Status | industrial sort recovery reported; no pre-registered tolerance |

> This is an **industrial sort recovery** check, not an official BC log-grade validation. The bucker is dimension-only; defect, sweep, knot, rot, and product quality are not represented. Every output row is labelled `grade_status=not_assigned`.

## 1. Join and sample

Primary join: FAIB plot -> BEC + supported leading species -> managed FEMIC AU stratum (including combined-species strata) -> FEMIC site-index class -> managed AU -> TIPSY industrial-log curve interpolated at the FAIB stand age. This is the pilot benchmark join, not an operational AU assignment.

Documented fallbacks:

- `pilot grade_benchmark.csv` AU/stratum/SI/age when the primary join does not resolve a plot;
- species-mean TIPSY industrial curve when no AU is available but the leading species has a TIPSY curve. This is reported separately and never mixed into the primary AU-matched metrics.

- TIPSY industrial-sort source: `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/bucking/tsa24_sort_validation_v0/tipsy_industrial_sorts.csv` (`regenerated_btc_industrial_logs`).
- Sort-code contract: 20 TIPSY industrial codes; the only accepted spelling difference is `D125L50` -> `D125L5`. Any other unexpected code fails closed.

### Plot status

| Status | Plots |
|---|---|
| Comparable (managed AU + age) | 341 |
| Comparable (species fallback) | 15 |
| Excluded: no bucked logs | 44 |
| Excluded: no stand age | 71 |
| Excluded: no AU/species match | 22 |
| Excluded: TIPSY industrial total is zero | 65 |
| Excluded: pilot log volume is zero | 0 |
| **Total** | **558** |

Comparable AU-matched plots: **341**; species-fallback plots: **15**; total comparable: **356**.

Bucked logs in the comparable set: **23,054** of **35,589**; bucked trees: **13,412** of **20,053**. Excluded bucked volume: **3,588.85 m³**.

## 2. Sort TVD and overlap

TVD is half the absolute difference between pilot and TIPSY industrial-sort share vectors; overlap is `sum(min(pilot, tipsy)) = 1 - TVD`. Shares are volume-weighted for the pilot and pilot-volume-weighted for TIPSY.

### Primary managed-AU match

| Metric | Value |
|---|---|
| Comparable plots | 341 |
| Managed AUs with comparable plots | 14 of 16 TIPSY AUs |
| Mean per-plot TVD | 0.535 |
| Median per-plot TVD | 0.518 |
| Per-plot TVD range | 0.193 to 1.000 |
| Volume-weighted per-plot TVD | 0.527 |
| Pooled-share TVD | 0.440 |
| Mean per-plot overlap | 0.465 |
| Pooled-share overlap | 0.560 |

Extended species-fallback set: 356 plots, mean per-plot TVD 0.538, pooled TVD 0.443. These rows are secondary and are not the primary AU-matched result.

### Largest pilot sort shares

| code | pilot_share | tipsy_share | difference | abs_difference |
| --- | --- | --- | --- | --- |
| D125L51 | 0.175 | 0.378 | -0.204 | 0.204 |
| D125L63 | 0.131 | 0.089 | 0.042 | 0.042 |
| D125L13 | 0.123 | 0.004 | 0.120 | 0.120 |
| D125L8 | 0.105 | 0.097 | 0.008 | 0.008 |
| D20L8 | 0.088 | 0.228 | -0.140 | 0.140 |
| D125L11 | 0.080 | 0.020 | 0.061 | 0.061 |
| D30L13 | 0.053 | 0.004 | 0.049 | 0.049 |
| D20L11 | 0.044 | 0.041 | 0.004 | 0.004 |
| D152 | 0.038 | 0.000 | 0.038 | 0.038 |
| D30L11 | 0.030 | 0.005 | 0.025 | 0.025 |

### Largest absolute share differences

| code | pilot_share | tipsy_share | difference | abs_difference |
| --- | --- | --- | --- | --- |
| D125L51 | 0.175 | 0.378 | -0.204 | 0.204 |
| D20L8 | 0.088 | 0.228 | -0.140 | 0.140 |
| D125L13 | 0.123 | 0.004 | 0.120 | 0.120 |
| D125L11 | 0.080 | 0.020 | 0.061 | 0.061 |
| D125L5 | 0.001 | 0.055 | -0.054 | 0.054 |
| D30L13 | 0.053 | 0.004 | 0.049 | 0.049 |

These are model-definition differences between the value-maximising dimension bucker and the TIPSY industrial-log model; they are not fitted corrections.

### Per-AU summary

| au_id | n_plots | n_logs | bucked_log_m3ha | tipsy_industrial_total_m3ha | mean_plot_tvd | pooled_tvd | mean_plot_overlap | bias_m3ha | rmse_m3ha | relative_bias |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23000 | 128 | 8988 | 32,033.001 | 35,877.520 | 0.513 | 0.431 | 0.487 | 30.035 | 119.065 | 0.120 |
| 23003 | 78 | 6073 | 27,775.942 | 27,265.700 | 0.527 | 0.466 | 0.473 | -6.542 | 109.714 | -0.018 |
| 22003 | 36 | 1763 | 9,244.318 | 7,362.690 | 0.543 | 0.465 | 0.457 | -52.267 | 120.472 | -0.204 |
| 23001 | 21 | 1155 | 5,788.854 | 4,535.220 | 0.449 | 0.389 | 0.551 | -59.697 | 99.109 | -0.217 |
| 23007 | 16 | 1249 | 3,176.484 | 6,181.990 | 0.762 | 0.779 | 0.238 | 187.844 | 298.578 | 0.946 |
| 22000 | 16 | 723 | 3,206.246 | 3,052.720 | 0.535 | 0.436 | 0.465 | -9.595 | 119.400 | -0.048 |
| 23008 | 14 | 929 | 4,020.449 | 3,286.530 | 0.534 | 0.451 | 0.466 | -52.423 | 211.069 | -0.183 |
| 22008 | 8 | 389 | 2,041.615 | 1,233.280 | 0.569 | 0.422 | 0.431 | -101.042 | 147.680 | -0.396 |
| 23002 | 8 | 436 | 1,208.616 | 1,920.000 | 0.442 | 0.411 | 0.558 | 88.923 | 185.015 | 0.589 |
| 21008 | 5 | 287 | 1,115.456 | 638.240 | 0.532 | 0.447 | 0.468 | -95.443 | 124.053 | -0.428 |
| 21002 | 3 | 201 | 623.861 | 521.980 | 0.540 | 0.538 | 0.460 | -33.960 | 39.270 | -0.163 |
| 21007 | 3 | 25 | 49.306 | 446.720 | 0.880 | 0.818 | 0.120 | 132.471 | 135.423 | 8.060 |
| 22007 | 3 | 122 | 439.485 | 773.900 | 0.914 | 0.958 | 0.086 | 111.472 | 144.090 | 0.761 |
| 22002 | 2 | 25 | 63.052 | 323.180 | 0.422 | 0.431 | 0.578 | 130.064 | 131.436 | 4.126 |

## 3. Volume comparison

Bucked log volume is expanded with `PHF_TREE` to m³/ha and compared with the TIPSY industrial-log total at the same AU and age. Sums are m³/ha summed across plots, not absolute cubic metres. This is industrial sort recovery, not a merchantable-volume validation.

| Metric | Value |
|---|---|
| n plots | 341 |
| Bucked volume (m³/ha-sum) | 90,786.684 |
| TIPSY industrial total (m³/ha-sum) | 93,419.670 |
| Mean bias (TIPSY - bucked, m³/ha) | 7.721 |
| MAE (m³/ha) | 105.203 |
| RMSE (m³/ha) | 137.448 |
| Relative bias | 0.029 |
| Ratio (TIPSY / bucked) | 1.029 |
| Raw bucked log volume (m³) | 7,876.48 |

The ratio is not interpreted as a recovery factor because the two surfaces use different minimum top diameters, length rules, and utilisation assumptions.

## 4. Evidence and caveats

| Element | Evidence tier |
|---|---|
| Pilot sort codes | `dimension_only` |
| TIPSY industrial-log curves | `model_output` |
| Comparison | `derived` |

- No pre-existing industrial-sort TVD/overlap tolerance was found. The result is reported as metrics only; `pass_fail = not_assessed_no_pre_registered_tolerance`.
- The TIPSY industrial-log curves are model output from the TSA24 BTC /TSR run, not field grade. They carry no defect, sweep, knot, rot, or value information.
- Multiple PSP plots can share one managed AU curve, so per-plot RMSE is not an independent model-error estimate.
- The canonical `tsa24_grade_curves/managed_au_industrial_sorts.csv` is empty in the current checkout because the refreshed BTC compile requested only log-grades and residual-fibre. The validation used the separately compiled industrial-logs table recorded in the manifest and fails closed if no table is available.
- No age is imputed. Plots without a stand age remain excluded; the pilot benchmark age is used only where that plot is explicitly present in the pilot table.

## 5. Artifacts

- `plot_sort_comparison.csv`
- `au_sort_summary.csv`
- `sort_comparison.csv`
- `metrics.json`
- `summary.json`
- `manifest.json`
- `VALIDATION_REPORT.md`

Inputs and hashes are recorded in `manifest.json`.
