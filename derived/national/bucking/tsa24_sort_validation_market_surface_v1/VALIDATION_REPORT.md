# TSA24 pilot industrial-sort validation market_surface_v1
| Field | Value |
|---|---|
| Validation | `industrial_sort_validation` |
| TSA | 24 — Prince George |
| Generated (UTC) | 2026-11-23T07:49:08+00:00 |
| Grade status | `not_assigned` |
| Evidence label | `industrial_sort_validation` |
| Sample | 558 plots, 32,366 logs, 20,054 bucked trees |
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

Bucked logs in the comparable set: **20,947** of **32,366**; bucked trees: **13,413** of **20,054**. Excluded bucked volume: **3,559.29 m³**.

## 2. Sort TVD and overlap

TVD is half the absolute difference between pilot and TIPSY industrial-sort share vectors; overlap is `sum(min(pilot, tipsy)) = 1 - TVD`. Shares are volume-weighted for the pilot and pilot-volume-weighted for TIPSY.

### Primary managed-AU match

| Metric | Value |
|---|---|
| Comparable plots | 341 |
| Managed AUs with comparable plots | 14 of 16 TIPSY AUs |
| Mean per-plot TVD | 0.661 |
| Median per-plot TVD | 0.656 |
| Per-plot TVD range | 0.193 to 1.000 |
| Volume-weighted per-plot TVD | 0.666 |
| Pooled-share TVD | 0.597 |
| Mean per-plot overlap | 0.339 |
| Pooled-share overlap | 0.403 |

Extended species-fallback set: 356 plots, mean per-plot TVD 0.663, pooled TVD 0.598. These rows are secondary and are not the primary AU-matched result.

### Largest pilot sort shares

| code | pilot_share | tipsy_share | difference | abs_difference |
| --- | --- | --- | --- | --- |
| D125L63 | 0.213 | 0.089 | 0.124 | 0.124 |
| D125L13 | 0.152 | 0.004 | 0.149 | 0.149 |
| D125L8 | 0.128 | 0.097 | 0.031 | 0.031 |
| D20L8 | 0.090 | 0.228 | -0.138 | 0.138 |
| D125L11 | 0.081 | 0.020 | 0.062 | 0.062 |
| D30L13 | 0.051 | 0.004 | 0.047 | 0.047 |
| D20L11 | 0.048 | 0.041 | 0.007 | 0.007 |
| D152 | 0.036 | 0.000 | 0.036 | 0.036 |
| D30L11 | 0.034 | 0.005 | 0.029 | 0.029 |
| D38L11 | 0.032 | 0.002 | 0.031 | 0.031 |

### Largest absolute share differences

| code | pilot_share | tipsy_share | difference | abs_difference |
| --- | --- | --- | --- | --- |
| D125L51 | 0.014 | 0.378 | -0.364 | 0.364 |
| D125L13 | 0.152 | 0.004 | 0.149 | 0.149 |
| D20L8 | 0.090 | 0.228 | -0.138 | 0.138 |
| D125L63 | 0.213 | 0.089 | 0.124 | 0.124 |
| D125L11 | 0.081 | 0.020 | 0.062 | 0.062 |
| D125L5 | 0.001 | 0.055 | -0.054 | 0.054 |

These are model-definition differences between the value-maximising dimension bucker and the TIPSY industrial-log model; they are not fitted corrections.

### Per-AU summary

| au_id | n_plots | n_logs | bucked_log_m3ha | tipsy_industrial_total_m3ha | mean_plot_tvd | pooled_tvd | mean_plot_overlap | bias_m3ha | rmse_m3ha | relative_bias |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23000 | 128 | 8176 | 31,745.926 | 35,877.520 | 0.650 | 0.590 | 0.350 | 32.278 | 119.065 | 0.130 |
| 23003 | 78 | 5466 | 27,630.811 | 27,265.700 | 0.658 | 0.619 | 0.342 | -4.681 | 109.009 | -0.013 |
| 22003 | 36 | 1618 | 9,191.659 | 7,362.690 | 0.656 | 0.607 | 0.344 | -50.805 | 119.683 | -0.199 |
| 23001 | 21 | 1028 | 5,749.853 | 4,535.220 | 0.612 | 0.565 | 0.388 | -57.840 | 97.591 | -0.211 |
| 23007 | 16 | 1203 | 3,157.911 | 6,181.990 | 0.800 | 0.794 | 0.200 | 189.005 | 297.638 | 0.958 |
| 22000 | 16 | 644 | 3,185.202 | 3,052.720 | 0.649 | 0.611 | 0.351 | -8.280 | 118.537 | -0.042 |
| 23008 | 14 | 839 | 3,986.833 | 3,286.530 | 0.672 | 0.593 | 0.328 | -50.022 | 209.894 | -0.176 |
| 22008 | 8 | 347 | 2,023.737 | 1,233.280 | 0.704 | 0.589 | 0.296 | -98.807 | 145.619 | -0.391 |
| 23002 | 8 | 379 | 1,192.530 | 1,920.000 | 0.570 | 0.636 | 0.430 | 90.934 | 185.522 | 0.610 |
| 21008 | 5 | 262 | 1,104.937 | 638.240 | 0.658 | 0.591 | 0.342 | -93.339 | 122.428 | -0.422 |
| 21002 | 3 | 179 | 613.159 | 521.980 | 0.674 | 0.671 | 0.326 | -30.393 | 35.904 | -0.149 |
| 21007 | 3 | 25 | 49.306 | 446.720 | 0.880 | 0.818 | 0.120 | 132.471 | 135.423 | 8.060 |
| 22007 | 3 | 126 | 439.338 | 773.900 | 0.914 | 0.958 | 0.086 | 111.521 | 144.101 | 0.762 |
| 22002 | 2 | 25 | 63.052 | 323.180 | 0.422 | 0.431 | 0.578 | 130.064 | 131.436 | 4.126 |

## 3. Volume comparison

Bucked log volume is expanded with `PHF_TREE` to m³/ha and compared with the TIPSY industrial-log total at the same AU and age. Sums are m³/ha summed across plots, not absolute cubic metres. This is industrial sort recovery, not a merchantable-volume validation.

| Metric | Value |
|---|---|
| n plots | 341 |
| Bucked volume (m³/ha-sum) | 90,134.254 |
| TIPSY industrial total (m³/ha-sum) | 93,419.670 |
| Mean bias (TIPSY - bucked, m³/ha) | 9.635 |
| MAE (m³/ha) | 104.962 |
| RMSE (m³/ha) | 136.910 |
| Relative bias | 0.036 |
| Ratio (TIPSY / bucked) | 1.036 |
| Raw bucked log volume (m³) | 7,825.43 |

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
