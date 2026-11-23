# BC PSP TSA24 bucking validation v0

| Field | Value |
|---|---|
| Validation | `bc_psp_tsa24_bucking_validation_v0` |
| TSA | 24 — Prince George |
| Generated (UTC) | 2026-11-23T00:58:00+00:00 |
| Population | full latest live visit per site, not a sample |
| Sites / visits / plots | 558 / 558 / 558 |
| Live selected trees | 60,960 |
| Bucked trees | 59,396 |
| Logs | 35,589 |
| Elapsed | 185.2 s |
| Status | full-population dimension validation; grade not assigned |
| Bucking profile | `tipsy45` (target lengths 13, 11, 8, 6.3, 5.1, 5, 2.5 m) |

> This is a dimension-only bucking validation against the published FAIB PSP compiled volume banks. It is **not** an official BC grade validation, a national taper library, or an operational supply model. Sorts are geometry-based; defect, sweep, knot, rot, and product quality are not represented.

## 1. Sample and coverage

- TSA24 sites in the FAIB header: **558**. One latest live visit was selected per site; FAIB `CLSTR_ID` changes at remeasurement, so `CLSTR_ID` is not a site key.
- Selected plots: **558**; live trees with DBH ≥ 2 cm, height > 1.3 m, positive `PHF_TREE`, and a species code: **60,960**.
- Latest-visit fallbacks because the latest overall visit had no valid live tree: **0**.
- DBH min/median/max: **2.0 / 11.6 / 133.6 cm**; trees ≥ 7.5 cm: **42,825**; trees ≥ 12.5 cm: **28,416**.
- Exclusions from the TSA24 tree rows: dead **28,704**, invalid DBH **0**, height ≤ 1.3 m **1**, non-positive expansion **0**, missing species **0**, below 2 cm **0**, missing BEC **0**, not the site's latest live visit **94,943**.
- Taper-supported species cover **99.54%** of selected observed whole-stem volume. Unsupported species are listed in `skipped_trees.csv`; they are excluded from the matched comparison, not silently assigned a proxy taper.
- Explicitly skipped rows: unsupported taper species: 1,548; bucker volume balance failure: 16. No skip is silent.
- Of these, **16** small stems failed the reference bucker's internal integration tolerance and were left unbucked. They are retained in `skipped_trees.csv`; their observed volume share of the compiled bank is reported in `validation_summary.json`.

Skipped rows by species (unsupported taper or bucker balance):

| species | trees | observed WSV m³/ha-sum |
| --- | --- | --- |
| W | 979 | 751.660 |
| PL | 16 | 60.587 |
| DG | 378 | 55.883 |
| DM | 114 | 14.744 |
| MR | 74 | 5.172 |
| XC | 1 | 0.156 |
| M | 1 | 0.134 |
| EW | 1 | 0.077 |

### Bucking profile

Profile `tipsy45` is applied only to this run; the repository default profile is unchanged. Geometry basis: `published_tipsy45_industrial_sort_lengths`. Price basis: `published_product_class_prices_no_fansier_numeric_defaults`. 
FAN$IER 4.5 Help does not publish numeric default log prices or a sort-specific relativity; no such values are invented here. The run keeps the published BC Interior Log Market Report product-class prices.

## 2. Volume comparison

Definitions: `observed_matched_wsv` is the compiled PSP whole-stem live volume (`VHA_WSV_LIV`) summed over taper-supported species; `predicted_taper` is the Kozak total for the same trees × `PHF_TREE`; `predicted_log` is recovered dimension-log volume; `predicted_residue` is taper total minus recovered logs. All volume columns are sums of per-hectare plot values, so they are m³/ha summed across plots, not absolute cubic metres.

| utilization_cm | n_plots | n_trees | n_logs | observed_matched_wsv_m3ha_sum | predicted_taper_m3ha_sum | predicted_log_m3ha_sum | predicted_residue_m3ha_sum | taper_bias_m3ha | taper_rmse_m3ha | taper_relative_bias | log_bias_m3ha | log_rmse_m3ha | log_relative_bias |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7.50 | 558 | 42825 | 35589 | 191,915.72 | 183,915.60 | 147,249.17 | 36,666.44 | -8,000.12 | 16.12 | -4.17 | -22,319.23 | 48.46 | -13.16 |
| 12.50 | 558 | 28416 | 35589 | 183,226.85 | 176,014.23 | 147,249.17 | 28,765.07 | -7,212.61 | 14.95 | -3.94 | -20,736.43 | 45.15 | -12.34 |

Primary taper comparison: predicted taper (recovered + stem residue) against compiled gross whole-stem volume at the matching utilization. Primary recovery comparison: recovered logs against compiled gross merchantable volume (`VHA_MER_LIV`, 10 cm top). The net merchantable bank (`VHA_DWB_LIV`, BEC decay/waste) is reported as a secondary check; the taper ledger is gross, so positive bias against the net bank is expected.

At 12.5 cm utilization: taper bias **-7,212.61 m³/ha-sum** (-3.94%), taper RMSE **14.95**; recovered-log bias **-20,736.43** (-12.34%), log RMSE **45.15**.

### Species comparison at 12.5 cm

| species | n_plots | n_trees | observed_wsv_m3ha | predicted_taper_m3ha | bias_m3ha | plot_rmse_m3ha | relative_bias | ratio | bucking_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SW | 480 | 11113 | 80,976.97 | 77,673.96 | -3,303.02 | 9.19 | -4.08 | 0.96 | bucked |
| PL | 269 | 4177 | 30,078.26 | 28,861.33 | -1,216.94 | 6.41 | -4.05 | 0.96 | bucked |
| BL | 343 | 5604 | 28,622.34 | 27,590.17 | -1,032.17 | 4.99 | -3.61 | 0.96 | bucked |
| FD | 185 | 1958 | 18,727.48 | 18,190.06 | -537.42 | 4.47 | -2.87 | 0.97 | bucked |
| AT | 209 | 3008 | 13,339.95 | 12,940.00 | -399.95 | 3.72 | -3.00 | 0.97 | bucked |
| EP | 216 | 1648 | 6,822.92 | 6,410.79 | -412.13 | 4.57 | -6.04 | 0.94 | bucked |
| SE | 22 | 345 | 2,970.93 | 2,812.02 | -158.90 | 8.67 | -5.35 | 0.95 | bucked |
| AC | 30 | 74 | 734.50 | 659.99 | -74.51 | 3.65 | -10.14 | 0.90 | bucked |
| W | 105 | 263 | 488.88 | 0.00 | -488.88 | 10.25 | -100.00 | 0.00 | not_bucked_unsupported_species |
| HW | 19 | 108 | 420.07 | 394.16 | -25.91 | 3.25 | -6.17 | 0.94 | bucked |
| CW | 4 | 18 | 372.88 | 335.37 | -37.51 | 16.36 | -10.06 | 0.90 | bucked |
| SB | 26 | 97 | 159.99 | 146.02 | -13.98 | 0.83 | -8.74 | 0.91 | bucked |
| DG | 1 | 2 | 2.49 | 0.00 | -2.49 | 2.49 | -100.00 | 0.00 | not_bucked_unsupported_species |
| HM | 1 | 1 | 0.55 | 0.38 | -0.17 | 0.17 | -30.97 | 0.69 | bucked |

Full plot and species tables are in `plot_comparison.csv`, `plot_species_comparison.csv`, and `species_comparison.csv`. No threshold was tuned to improve these statistics.

## 3. Residue

- Bucked trees: **59,396**; taper total **14,174.965 m³**; recovered logs **11,727.117 m³**; stem residue **2,447.848 m³** (**17.3%** of taper).
- Residue ODT at species basic density: **898.84 ODT**; green tonnes (45% moisture) **1,634.25**; chip green tonnes at 90% yield **1,470.82**.
- Residue is **stem residue only**: taper total minus recovered logs. It includes stump, top above the log top, and stem sections that do not meet a sort length/top limit. Branches and foliage are outside FAIB `VOL_WSV` and are **not estimated**; `residue_components.csv` records that component explicitly as not available, not as zero biomass.

| utilization_cm | n_trees | n_plots | taper_total_m3 | recovered_log_m3 | stem_residue_m3 | residue_share | residue_odt | green_tonnes_45 | chip_green_tonnes_45 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7.500 | 42152 | 554 | 14,095.716 | 11,727.117 | 2,368.599 | 0.168 | 870.745 | 1,583.172 | 1,424.855 |
| 12.500 | 28135 | 543 | 13,652.913 | 11,727.117 | 1,925.796 | 0.141 | 709.841 | 1,290.619 | 1,161.557 |

## 4. Grade and taper evidence

- Taper: **BC Kozak (2004) Version 6**, published parameter table `kozak_parameters_v94.csv`, applied by species and BEC zone through `nemora`. Trees outside a supported species or zone are skipped and reported; no curve is averaged, interpolated, or silently substituted.
- Sorts: **TIPSY 4.5 interior industrial dimensions** (`rules/bc_interior.yaml`). Logs are selected by minimum top diameter and minimum length. This is dimension-only geometry, **not official BC grade**; `grade_status = not_assigned` and `sort_basis = dimension_only` on every log.
- Evidence tiers: taper and volume rows are `published_table`; residue density/moisture/chip conversions are `assumption`; no tree carries `measured_taper` because the FAIB PSP data do not include stem analysis. `HEIGHT_SOURCE` is retained so DBH-estimated heights are distinguishable from field-measured heights.
- No official grade, sort recovery, or national claim is made from this validation.

## 5. RSYC secondary check

- Status: **reported_with_join_assumptions**; curve rows **143**; plot matches **293**.
- Observed merchantable vs RSYC: n=293, relative bias 9.2%, RMSE 196.93 m³/ha.
- RSYC is a stand-level remote-sensing yield product with no tree lists, diameter distribution, grade, or residue. It is a coarse secondary sanity check, **not** a calibration target.

## 6. Validation checks

- Tree × expansion reproduces compiled PSP banks: **PASS** (tolerance 0.01 m³/ha per plot).
- Compiled stand and species banks agree: **PASS** (max difference 1.14e-13 m³/ha).
- Ledger conservation (recovered + residue = taper): **PASS**; max balance error **1.78e-15 m³**; trees without a feasible log **39,343**.
- Reference bucker internal balance: **PASS**; max error **2.67e-05 m³**.
- Output tables are checked for NaN and negative values in key volume, dimension, count, and residue columns before writing.

## 7. Caveats

- The comparison tests the *combination* of the nemora Kozak (2004) taper, FAIB tree list, expansion factors, and dimension sorts. It does not isolate taper error from compiled-volume error.
- FAIB `VOL_WSV` includes stump and top and is based on Kozak (2002) with mixed-model volumes for unenhanced trees; the nemora taper starts at 0.3 m stump height. A small negative taper bias is therefore expected.
- FAIB `VOL_MER` is gross merchantable volume to a 10 cm top. The sort rules use a 12.5 cm minimum top and minimum lengths, so recovered log volume is expected to be below gross merchantable volume. This is a definition difference, not a fitted correction.
- Species basic density is a reference default table (FVS-BC NBEL/FIA), not a BC-local sample. Moisture and chip yield are labelled assumptions.
- There is no official grade validation in this dataset because FAIB PSP tree records do not carry the defect, knot, sweep, rot, or product-quality information required for BC log grades.

## 8. Artifacts

- `selected_trees.csv`
- `tree_ledger.csv`
- `bucked_logs.csv`
- `residue.csv`
- `skipped_trees.csv`
- `plot_comparison.csv`
- `plot_species_comparison.csv`
- `species_comparison.csv`
- `utilization_comparison.csv`
- `residue_summary.csv`
- `residue_components.csv`
- `rsyc_benchmark.csv`
- `rsyc_curves.csv`
- `validation_summary.json`
- `manifest.json`

Input and output hashes, git state, and the no-deletion check are in `manifest.json`.
