# TSA24 pilot industrial-sort validation v1
| Field | Value |
|---|---|
| Validation | `industrial_sort_validation` |
| TSA | 24 — Prince George |
| Generated (UTC) | 2026-11-23T00:39:44+00:00 |
| Grade status | `not_assigned` |
| Evidence label | `industrial_sort_validation` |
| Sample | 558 plots, 38,992 logs, 20,054 bucked trees |
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

Bucked logs in the comparable set: **25,151** of **38,992**; bucked trees: **13,413** of **20,054**. Excluded bucked volume: **3,589.04 m³**.

## 2. Sort TVD and overlap

TVD is half the absolute difference between pilot and TIPSY industrial-sort share vectors; overlap is `sum(min(pilot, tipsy)) = 1 - TVD`. Shares are volume-weighted for the pilot and pilot-volume-weighted for TIPSY.

### Primary managed-AU match

| Metric | Value |
|---|---|
| Comparable plots | 341 |
| Managed AUs with comparable plots | 14 of 16 TIPSY AUs |
| Mean per-plot TVD | 0.505 |
| Median per-plot TVD | 0.480 |
| Per-plot TVD range | 0.193 to 1.000 |
| Volume-weighted per-plot TVD | 0.491 |
| Pooled-share TVD | 0.433 |
| Mean per-plot overlap | 0.495 |
| Pooled-share overlap | 0.567 |

Extended species-fallback set: 356 plots, mean per-plot TVD 0.508, pooled TVD 0.436. These rows are secondary and are not the primary AU-matched result.

### Largest pilot sort shares

| code | pilot_share | tipsy_share | difference | abs_difference |
| --- | --- | --- | --- | --- |
| D125L63 | 0.256 | 0.089 | 0.166 | 0.166 |
| D125L51 | 0.192 | 0.379 | -0.186 | 0.186 |
| D125L8 | 0.117 | 0.097 | 0.020 | 0.020 |
| D20L8 | 0.105 | 0.228 | -0.122 | 0.122 |
| D125L13 | 0.081 | 0.004 | 0.078 | 0.078 |
| D125L11 | 0.077 | 0.020 | 0.057 | 0.057 |
| D38L8 | 0.036 | 0.005 | 0.031 | 0.031 |
| D30L8 | 0.027 | 0.034 | -0.006 | 0.006 |
| D152 | 0.022 | 0.000 | 0.022 | 0.022 |
| D203 | 0.017 | 0.000 | 0.017 | 0.017 |

### Largest absolute share differences

| code | pilot_share | tipsy_share | difference | abs_difference |
| --- | --- | --- | --- | --- |
| D125L51 | 0.192 | 0.379 | -0.186 | 0.186 |
| D125L63 | 0.256 | 0.089 | 0.166 | 0.166 |
| D20L8 | 0.105 | 0.228 | -0.122 | 0.122 |
| D125L13 | 0.081 | 0.004 | 0.078 | 0.078 |
| D125L11 | 0.077 | 0.020 | 0.057 | 0.057 |
| D125L5 | 0.001 | 0.055 | -0.054 | 0.054 |

These are model-definition differences between the value-maximising dimension bucker and the TIPSY industrial-log model; they are not fitted corrections.

### Per-AU summary

| au_id | n_plots | n_logs | bucked_log_m3ha | tipsy_industrial_total_m3ha | mean_plot_tvd | pooled_tvd | mean_plot_overlap | bias_m3ha | rmse_m3ha | relative_bias |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23000 | 128 | 9778 | 32,084.442 | 35,877.520 | 0.485 | 0.429 | 0.515 | 29.633 | 119.189 | 0.118 |
| 23003 | 78 | 6565 | 27,812.151 | 27,265.700 | 0.492 | 0.440 | 0.508 | -7.006 | 109.468 | -0.020 |
| 22003 | 36 | 1855 | 9,272.258 | 7,362.690 | 0.517 | 0.456 | 0.483 | -53.044 | 120.852 | -0.206 |
| 23001 | 21 | 1204 | 5,805.089 | 4,535.220 | 0.423 | 0.374 | 0.577 | -60.470 | 99.634 | -0.219 |
| 23007 | 16 | 1589 | 3,126.983 | 6,181.990 | 0.750 | 0.772 | 0.250 | 190.938 | 298.987 | 0.977 |
| 22000 | 16 | 795 | 3,210.413 | 3,052.720 | 0.487 | 0.412 | 0.513 | -9.856 | 119.473 | -0.049 |
| 23008 | 14 | 1025 | 4,030.010 | 3,286.530 | 0.486 | 0.434 | 0.514 | -53.106 | 211.151 | -0.184 |
| 22008 | 8 | 420 | 2,049.883 | 1,233.280 | 0.520 | 0.411 | 0.480 | -102.075 | 148.726 | -0.398 |
| 23002 | 8 | 449 | 1,213.233 | 1,920.000 | 0.415 | 0.342 | 0.585 | 88.346 | 184.566 | 0.583 |
| 21008 | 5 | 293 | 1,119.396 | 638.240 | 0.497 | 0.423 | 0.503 | -96.231 | 124.705 | -0.430 |
| 21002 | 3 | 210 | 629.106 | 521.980 | 0.512 | 0.501 | 0.488 | -35.709 | 40.201 | -0.170 |
| 21007 | 3 | 33 | 47.986 | 446.720 | 0.879 | 0.816 | 0.121 | 132.911 | 135.789 | 8.309 |
| 22007 | 3 | 183 | 422.359 | 773.900 | 0.914 | 0.957 | 0.086 | 117.180 | 146.113 | 0.832 |
| 22002 | 2 | 25 | 63.377 | 323.180 | 0.423 | 0.433 | 0.577 | 129.901 | 131.299 | 4.099 |

## 3. Volume comparison

Bucked log volume is expanded with `PHF_TREE` to m³/ha and compared with the TIPSY industrial-log total at the same AU and age. Sums are m³/ha summed across plots, not absolute cubic metres. This is industrial sort recovery, not a merchantable-volume validation.

| Metric | Value |
|---|---|
| n plots | 341 |
| Bucked volume (m³/ha-sum) | 90,886.685 |
| TIPSY industrial total (m³/ha-sum) | 93,419.670 |
| Mean bias (TIPSY - bucked, m³/ha) | 7.428 |
| MAE (m³/ha) | 105.342 |
| RMSE (m³/ha) | 137.596 |
| Relative bias | 0.028 |
| Ratio (TIPSY / bucked) | 1.028 |
| Raw bucked log volume (m³) | 7,883.91 |

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
