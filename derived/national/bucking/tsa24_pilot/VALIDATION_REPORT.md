# TSA24 bucking pilot — validation report

| Field | Value |
|---|---|
| Pilot | `tsa24_bucking_phase0` |
| TSA | 24 — Prince George |
| Generated (UTC) | 2026-11-15T20:36:11+00:00 |
| Status | pilot complete; BTC volume benchmarked; grade not validated; harvest-slash ledger reported |
| Sample | 20 plots, 300 live trees |
| Logs | 134 |
| Elapsed | 52.5 s |

> This is the Phase 0/1 pilot. It is **not** the pre-registered three-way
> validation gate. The refreshed TSA24 FEMIC BTC /TSR output exposes
> `Logs_Grade_*`, `Residual_*`, `Biomass_Live_*`, and `Carbon_Live_*`
> surfaces at each managed AU and age. Merchantable volume and harvest
> slash are reported against the BTC volume and `biomass-live` banks.
> Grade shares remain **not validated** because the pilot bucker is
> dimension-only and D/F are zero in TSA24.

## 1. Scope and contracts

- Tree list: FAIB PSP `tree_detail`, `header`, `sample_byvisit`, and
  `faib_compiled_spcsmries_siteage`; live trees only; latest visit per
  `CLSTR_ID`. `PHF_TREE` is the per-hectare expansion factor.
- Taper: nemora Kozak (2004) Version 6 parameter table, keyed by
  `(jurisdiction=BC, species, BEC zone)`. Unsupported species and zones
  fail loudly; the pilot records explicit skips.
- Sort rules: `workflows/national/bucking/rules/bc_interior.yaml`, derived
  from TIPSY 4.5 industrial interior dimensions. Geometry/dimension-based,
  **not official grade**. Defect, sweep, knot, and rot are not represented.
- Price profile: BC Interior Log Market Report, 3 months ending 2026-09-30.
  Product-level averages, not grade-specific prices. The profile is a
  placeholder for this pilot.
- Taper residue: `taper total - recovered logs`. Density, moisture, and
  chip yield are labelled assumptions.
- Harvest slash: `AGB - merchantable log biomass`, where AGB is the BTC
  `biomass-live` `Biomass_Live_Above` surface at the matched AU and age,
  and log biomass is `sum(log_volume_m3 * basic_density_odt_m3)`. This is
  **not** the BTC `Residual_*` mill-processing residue surface.

## 2. TSA24 sample

Selection method: within-BEC and within-leading-supported-species strata;
one plot per site; up to 15 trees per plot sampled across species and
DBH quantiles; seed `20261115`. The full TSA24 live tree population
is 155,903 trees on
1,318 plots.

### Stratum allocation and selected counts

| bec_zone | leading_species | quota | candidate_plots | selected_plots | n_sampled_trees |
| --- | --- | --- | --- | --- | --- |
| SBS | SW | 6 | 593 | 6 | 90 |
| SBS | BL | 3 | 317 | 3 | 45 |
| SBS | PL | 2 | 145 | 2 | 30 |
| SBS | AT | 1 | 134 | 1 | 15 |
| SBS | FD | 1 | 37 | 1 | 15 |
| SBS | EP | 1 | 35 | 1 | 15 |
| ESSF | BL | 2 | 33 | 2 | 30 |
| ESSF | SE | 1 | 4 | 1 | 15 |
| ICH | HW | 1 | 5 | 1 | 15 |
| ICH | SW | 1 | 4 | 1 | 15 |
| SBPS | PL | 1 | 3 | 1 | 15 |

### Sampled species and BEC

| species | trees |
| --- | --- |
| SW | 91 |
| BL | 67 |
| PL | 42 |
| AT | 23 |
| EP | 23 |
| SE | 23 |
| HW | 12 |
| FD | 11 |
| CW | 5 |
| AC | 3 |

| bec_zone | trees |
| --- | --- |
| SBS | 210 |
| ESSF | 45 |
| ICH | 30 |
| SBPS | 15 |

### Selected plots

| plot_id | bec_zone | leading_species | n_live_supported_all | n_sampled | stand_age | site_index | observed_merchantable_sampled_m3ha | bucked_log_m3ha | residue_m3ha | value_cad_ha_sample |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4035884-PSP1 | ICH | SW | 157 | 15 | 169.00 | 23.61 | 65.32 | 55.33 | 13.64 | 6,320.31 |
| 4035967-PSP1 | SBS | SW | 93 | 15 | 40.00 | 25.62 | 0.52 | 0.00 | 1.62 | 0.00 |
| 4036113-PSP1 | SBS | BL | 91 | 15 | 249.00 | 20.97 | 83.81 | 80.19 | 4.51 | 8,934.77 |
| 4036956-PSP1 | ICH | HW | 322 | 15 | 89.00 | 20.82 | 23.83 | 20.83 | 5.85 | 2,350.02 |
| 4037163-PSP1 | ESSF | BL | 68 | 15 | 209.00 | 13.34 | 95.51 | 91.66 | 4.59 | 10,107.17 |
| 4037899-PSP2 | SBS | SW | 90 | 15 | 14.00 | 22.71 | 36.93 | 30.90 | 7.23 | 3,105.47 |
| 4038213-PSP1 | SBS | FD | 111 | 15 | 89.00 | 25.71 | 83.16 | 70.16 | 20.42 | 8,295.98 |
| 4038237-PSP1 | SBS | EP | 200 | 15 | 69.00 | 21.29 | 1.37 | 0.00 | 5.33 | 0.00 |
| 4038318-PSP1 | SBS | SW | 47 | 15 | n/a | n/a | 124.17 | 113.09 | 15.66 | 13,288.13 |
| 4038415-PSP2 | SBS | AT | 143 | 15 | 16.00 | 22.81 | 25.92 | 19.89 | 8.46 | 2,033.54 |
| 4038551-PSP2 | SBS | PL | 121 | 15 | 97.00 | 20.26 | 25.38 | 21.51 | 5.07 | 2,451.56 |
| 4038570-PSP2 | SBS | SW | 94 | 15 | 112.00 | 23.20 | 35.30 | 29.03 | 7.56 | 2,966.85 |
| 4038614-PSP1 | SBS | BL | 95 | 15 | 6.00 | 8.88 | 18.61 | 11.02 | 9.55 | 1,189.72 |
| 4040936-PSP1 | SBPS | PL | 203 | 15 | 142.00 | 18.12 | 19.90 | 14.50 | 14.79 | 1,652.51 |
| 4045088-PSP1 | SBS | BL | 103 | 15 | 92.00 | 20.40 | 31.32 | 23.36 | 10.41 | 2,506.38 |
| 4045109-PSP1 | SBS | SW | 97 | 15 | 50.00 | 23.59 | 118.96 | 113.45 | 12.06 | 12,928.26 |
| 4045124-PSP2 | SBS | PL | 149 | 15 | 57.00 | 19.69 | 4.76 | 0.00 | 7.41 | 0.00 |
| 4045144-PSP1 | SBS | SW | 112 | 15 | 101.00 | 22.93 | 42.15 | 37.06 | 10.19 | 4,192.53 |
| 4045365-PSP2 | ESSF | BL | 155 | 15 | 134.00 | 10.35 | 18.50 | 15.31 | 3.89 | 1,712.83 |
| 4045366-PSP1 | ESSF | SE | 100 | 15 | 249.00 | 16.27 | 20.31 | 13.24 | 10.19 | 1,509.18 |

The per-plot observed and bucked volumes in the table are paired over the
sampled trees only. `observed_merchantable_all_m3ha` (not shown) uses all
live supported trees in the plot and is used only for the secondary
ratio-expanded comparison.

## 3. Bucking results

- Taper total: **58.153 m³**
- Recovered logs: **47.864 m³**
- Residue: **10.289 m³**
- Residue share of taper: **17.7%**
- Conservation tolerance: abs 1e-07 m³ + rel 1e-05
- Bucker balance tolerance: abs 1e-06 m³ + rel 0.0001
- Max ledger balance error: **0.000000000 m³**
- Conservation pass: **True**
- Bucker-internal max balance error (all trees): **0.000011347 m³**
- Trees with no feasible log: **217**
- Reference taper warnings observed during bucking: **1** unique

  - `RuntimeWarning: invalid value encountered in power`

### Log volume and value

- Log volume: **47.864 m³**
- Priced volume: **47.785 m³**
- Unpriced volume: **0.079 m³** (0.2%)
- Total value: **$5,315 CAD**
- Value per priced m³: **$111.22/m³**
- Value per all-log m³: **$111.04/m³**
- Mean sample value: **$4,277/ha** (sampled trees; not a full-plot estimate)
- Mean ratio-expanded value: **$20,787/ha** (secondary estimate)

### Sort and product shares

| product | n_logs | volume_m3 | value_cad |
| --- | --- | --- | --- |
| sawlog | 111 | 45.256 | 5,158.677 |
| other | 22 | 2.529 | 156.111 |
| pulpwood | 1 | 0.079 | 0.000 |

| species_market_group | n_logs | volume_m3 | value_cad |
| --- | --- | --- | --- |
| SPF | 75 | 31.453 | 3,584.412 |
| Hem-Bal | 25 | 9.206 | 967.258 |
| Df-Larch | 11 | 4.558 | 584.282 |
| Deciduous | 22 | 2.529 | 156.111 |
| Cedar | 1 | 0.118 | 22.726 |

### Sort-code shares (top 20 by volume)

| sort_code | product | species_market_group | n_logs | volume_m3 | volume_share | value_cad | unpriced_volume_m3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D125L63 | sawlog | SPF | 15 | 7.161 | 0.150 | 816.050 | 0.000 |
| D125L13 | sawlog | SPF | 9 | 4.614 | 0.096 | 525.841 | 0.000 |
| D125L8 | sawlog | SPF | 15 | 4.010 | 0.084 | 456.984 | 0.000 |
| D20L8 | sawlog | SPF | 7 | 3.899 | 0.081 | 444.284 | 0.000 |
| D38L8 | sawlog | SPF | 2 | 3.734 | 0.078 | 425.534 | 0.000 |
| D30L8 | sawlog | SPF | 3 | 3.430 | 0.072 | 390.923 | 0.000 |
| D125L51 | sawlog | Hem-Bal | 7 | 2.933 | 0.061 | 310.836 | 0.000 |
| D125L51 | sawlog | SPF | 18 | 2.337 | 0.049 | 266.349 | 0.000 |
| D125L11 | sawlog | SPF | 6 | 2.268 | 0.047 | 258.446 | 0.000 |
| D125L63 | sawlog | Df-Larch | 4 | 1.854 | 0.039 | 237.663 | 0.000 |
| D20L8 | sawlog | Hem-Bal | 3 | 1.715 | 0.036 | 181.710 | 0.000 |
| D125L8 | sawlog | Hem-Bal | 7 | 1.701 | 0.036 | 180.258 | 0.000 |
| D125L13 | sawlog | Hem-Bal | 3 | 1.375 | 0.029 | 145.729 | 0.000 |
| D152 | other | Deciduous | 10 | 1.170 | 0.024 | 72.263 | 0.000 |
| D20L11 | sawlog | Df-Larch | 1 | 1.128 | 0.024 | 144.623 | 0.000 |
| D203 | other | Deciduous | 7 | 0.903 | 0.019 | 55.780 | 0.000 |
| D30L8 | sawlog | Hem-Bal | 1 | 0.865 | 0.018 | 91.719 | 0.000 |
| D125L51 | sawlog | Df-Larch | 4 | 0.725 | 0.015 | 92.978 | 0.000 |
| D125L11 | sawlog | Df-Larch | 1 | 0.477 | 0.010 | 61.125 | 0.000 |
| D125L8 | sawlog | Df-Larch | 1 | 0.374 | 0.008 | 47.892 | 0.000 |

## 4. Validation

### FAIB PSP observed merchantable volume vs bucked logs

- Plots: **20** (20 with positive observed volume)
- Sum observed (sampled): **875.73 m³/ha**
- Sum bucked (sampled): **760.53 m³/ha**
- Mean bias: **-5.76 m³/ha**
- MAE: **5.76 m³/ha**
- RMSE: **6.51 m³/ha**
- Relative bias: **-13.2%**
- Mean ratio (bucked/observed): **0.702**
- Median ratio (bucked/observed): **0.832**

The primary comparison is paired over sampled trees. `VOL_MER` is the
FAIB observed merchantable volume; the bucked log volume uses the nemora
Kozak taper and dimension sorts. A difference is expected because the two
merchantability rules, taper families, and sort boundaries differ.

### VDYP7

- Status: **reported_with_join_assumptions**
- Matched plots: **14** of **20**
- Join basis: BEC + leading supported species -> managed FEMIC AU stratum (including combined-species strata) -> FEMIC AU site-index class -> VDYP stratum_code + L/M/H. This is the FEMIC AU crosswalk used as a benchmark join, not an operational AU assignment.
- Observed-all vs VDYP: n=14, bias=-42.36, MAE=113.33, rel.bias=-19.4%
- Bucked ratio-estimated vs VDYP: n=14, bias=-11.52, MAE=109.86, rel.bias=-6.1%
- Caveat: VDYP smooth volume units are assumed m3/ha; the curve may represent gross or total volume while VOL_MER is merchantable. The comparison is indicative, not a gate.

### TIPSY / FANSIER

- Status: **reported_with_join_assumptions**
- Matched plots: **14** of **20**
- TIPSY AU coverage: **16** of **27** mapped AU combinations
- Join basis: BEC + leading species -> managed FEMIC AU stratum (including combined-species strata such as SBS_SX+AT) -> FEMIC AU site-index class -> managed source AU in au_table -> TIPSY curve at FAIB stand age.
- Observed-all vs TIPSY: n=14, bias=-22.32, MAE=125.75, rel.bias=-10.2%
- Bucked ratio-estimated vs TIPSY: n=14, bias=8.52, MAE=124.32, rel.bias=4.5%
- Grade/residue/value inspection: {"status": "inspected", "n_columns": 685, "grade_columns": ["Logs_Grade_D_0", "Logs_Grade_D_10", "Logs_Grade_D_20", "Logs_Grade_D_30", "Logs_Grade_D_40", "Logs_Grade_D_50", "Logs_Grade_D_60", "Logs_Grade_D_70", "Logs_Grade_D_80", "Logs_Grade_D_90", "Logs_Grade_D_100", "Logs_Grade_D_110", "Logs_Grade_D_120", "Logs_Grade_D_130", "Logs_Grade_D_140", "Logs_Grade_D_150", "Logs_Grade_D_160", "Logs_Grade_D_170", "Logs_Grade_D_180", "Logs_Grade_D_190", "Logs_Grade_D_200", "Logs_Grade_D_210", "Logs_Grade_D_220", "Logs_Grade_D_230", "Logs_Grade_D_240", "Logs_Grade_D_250", "Logs_Grade_D_260", "Logs_Grade_D_270", "Logs_Grade_D_280", "Logs_Grade_D_290", "Logs_Grade_D_300", "Logs_Grade_D_310", "Logs_Grade_D_320", "Logs_Grade_D_330", "Logs_Grade_D_340", "Logs_Grade_D_350", "Logs_Grade_F_0", "Logs_Grade_F_10", "Logs_Grade_F_20", "Logs_Grade_F_30", "Logs_Grade_F_40", "Logs_Grade_F_50", "Logs_Grade_F_60", "Logs_Grade_F_70", "Logs_Grade_F_80", "Logs_Grade_F_90", "Logs_Grade_F_100", "Logs_Grade_F_110", "Logs_Grade_F_120", "Logs_Grade_F_130", "Logs_Grade_F_140", "Logs_Grade_F_150", "Logs_Grade_F_160", "Logs_Grade_F_170", "Logs_Grade_F_180", "Logs_Grade_F_190", "Logs_Grade_F_200", "Logs_Grade_F_210", "Logs_Grade_F_220", "Logs_Grade_F_230", "Logs_Grade_F_240", "Logs_Grade_F_250", "Logs_Grade_F_260", "Logs_Grade_F_270", "Logs_Grade_F_280", "Logs_Grade_F_290", "Logs_Grade_F_300", "Logs_Grade_F_310", "Logs_Grade_F_320", "Logs_Grade_F_330", "Logs_Grade_F_340", "Logs_Grade_F_350", "Logs_Grade_H_0", "Logs_Grade_H_10", "Logs_Grade_H_20", "Logs_Grade_H_30", "Logs_Grade_H_40", "Logs_Grade_H_50", "Logs_Grade_H_60", "Logs_Grade_H_70", "Logs_Grade_H_80", "Logs_Grade_H_90", "Logs_Grade_H_100", "Logs_Grade_H_110", "Logs_Grade_H_120", "Logs_Grade_H_130", "Logs_Grade_H_140", "Logs_Grade_H_150", "Logs_Grade_H_160", "Logs_Grade_H_170", "Logs_Grade_H_180", "Logs_Grade_H_190", "Logs_Grade_H_200", "Logs_Grade_H_210", "Logs_Grade_H_220", "Logs_Grade_H_230", "Logs_Grade_H_240", "Logs_Grade_H_250", "Logs_Grade_H_260", "Logs_Grade_H_270", "Logs_Grade_H_280", "Logs_Grade_H_290", "Logs_Grade_H_300", "Logs_Grade_H_310", "Logs_Grade_H_320", "Logs_Grade_H_330", "Logs_Grade_H_340", "Logs_Grade_H_350", "Logs_Grade_I_0", "Logs_Grade_I_10", "Logs_Grade_I_20", "Logs_Grade_I_30", "Logs_Grade_I_40", "Logs_Grade_I_50", "Logs_Grade_I_60", "Logs_Grade_I_70", "Logs_Grade_I_80", "Logs_Grade_I_90", "Logs_Grade_I_100", "Logs_Grade_I_110", "Logs_Grade_I_120", "Logs_Grade_I_130", "Logs_Grade_I_140", "Logs_Grade_I_150", "Logs_Grade_I_160", "Logs_Grade_I_170", "Logs_Grade_I_180", "Logs_Grade_I_190", "Logs_Grade_I_200", "Logs_Grade_I_210", "Logs_Grade_I_220", "Logs_Grade_I_230", "Logs_Grade_I_240", "Logs_Grade_I_250", "Logs_Grade_I_260", "Logs_Grade_I_270", "Logs_Grade_I_280", "Logs_Grade_I_290", "Logs_Grade_I_300", "Logs_Grade_I_310", "Logs_Grade_I_320", "Logs_Grade_I_330", "Logs_Grade_I_340", "Logs_Grade_I_350", "Logs_Grade_J_0", "Logs_Grade_J_10", "Logs_Grade_J_20", "Logs_Grade_J_30", "Logs_Grade_J_40", "Logs_Grade_J_50", "Logs_Grade_J_60", "Logs_Grade_J_70", "Logs_Grade_J_80", "Logs_Grade_J_90", "Logs_Grade_J_100", "Logs_Grade_J_110", "Logs_Grade_J_120", "Logs_Grade_J_130", "Logs_Grade_J_140", "Logs_Grade_J_150", "Logs_Grade_J_160", "Logs_Grade_J_170", "Logs_Grade_J_180", "Logs_Grade_J_190", "Logs_Grade_J_200", "Logs_Grade_J_210", "Logs_Grade_J_220", "Logs_Grade_J_230", "Logs_Grade_J_240", "Logs_Grade_J_250", "Logs_Grade_J_260", "Logs_Grade_J_270", "Logs_Grade_J_280", "Logs_Grade_J_290", "Logs_Grade_J_300", "Logs_Grade_J_310", "Logs_Grade_J_320", "Logs_Grade_J_330", "Logs_Grade_J_340", "Logs_Grade_J_350", "Logs_Grade_U_0", "Logs_Grade_U_10", "Logs_Grade_U_20", "Logs_Grade_U_30", "Logs_Grade_U_40", "Logs_Grade_U_50", "Logs_Grade_U_60", "Logs_Grade_U_70", "Logs_Grade_U_80", "Logs_Grade_U_90", "Logs_Grade_U_100", "Logs_Grade_U_110", "Logs_Grade_U_120", "Logs_Grade_U_130", "Logs_Grade_U_140", "Logs_Grade_U_150", "Logs_Grade_U_160", "Logs_Grade_U_170", "Logs_Grade_U_180", "Logs_Grade_U_190", "Logs_Grade_U_200", "Logs_Grade_U_210", "Logs_Grade_U_220", "Logs_Grade_U_230", "Logs_Grade_U_240", "Logs_Grade_U_250", "Logs_Grade_U_260", "Logs_Grade_U_270", "Logs_Grade_U_280", "Logs_Grade_U_290", "Logs_Grade_U_300", "Logs_Grade_U_310", "Logs_Grade_U_320", "Logs_Grade_U_330", "Logs_Grade_U_340", "Logs_Grade_U_350", "Logs_Grade_X_0", "Logs_Grade_X_10", "Logs_Grade_X_20", "Logs_Grade_X_30", "Logs_Grade_X_40", "Logs_Grade_X_50", "Logs_Grade_X_60", "Logs_Grade_X_70", "Logs_Grade_X_80", "Logs_Grade_X_90", "Logs_Grade_X_100", "Logs_Grade_X_110", "Logs_Grade_X_120", "Logs_Grade_X_130", "Logs_Grade_X_140", "Logs_Grade_X_150", "Logs_Grade_X_160", "Logs_Grade_X_170", "Logs_Grade_X_180", "Logs_Grade_X_190", "Logs_Grade_X_200", "Logs_Grade_X_210", "Logs_Grade_X_220", "Logs_Grade_X_230", "Logs_Grade_X_240", "Logs_Grade_X_250", "Logs_Grade_X_260", "Logs_Grade_X_270", "Logs_Grade_X_280", "Logs_Grade_X_290", "Logs_Grade_X_300", "Logs_Grade_X_310", "Logs_Grade_X_320", "Logs_Grade_X_330", "Logs_Grade_X_340", "Logs_Grade_X_350", "Logs_Grade_Y_0", "Logs_Grade_Y_10", "Logs_Grade_Y_20", "Logs_Grade_Y_30", "Logs_Grade_Y_40", "Logs_Grade_Y_50", "Logs_Grade_Y_60", "Logs_Grade_Y_70", "Logs_Grade_Y_80", "Logs_Grade_Y_90", "Logs_Grade_Y_100", "Logs_Grade_Y_110", "Logs_Grade_Y_120", "Logs_Grade_Y_130", "Logs_Grade_Y_140", "Logs_Grade_Y_150", "Logs_Grade_Y_160", "Logs_Grade_Y_170", "Logs_Grade_Y_180", "Logs_Grade_Y_190", "Logs_Grade_Y_200", "Logs_Grade_Y_210", "Logs_Grade_Y_220", "Logs_Grade_Y_230", "Logs_Grade_Y_240", "Logs_Grade_Y_250", "Logs_Grade_Y_260", "Logs_Grade_Y_270", "Logs_Grade_Y_280", "Logs_Grade_Y_290", "Logs_Grade_Y_300", "Logs_Grade_Y_310", "Logs_Grade_Y_320", "Logs_Grade_Y_330", "Logs_Grade_Y_340", "Logs_Grade_Y_350"], "residue_columns": ["Residual_Chips_0", "Residual_Chips_10", "Residual_Chips_20", "Residual_Chips_30", "Residual_Chips_40", "Residual_Chips_50", "Residual_Chips_60", "Residual_Chips_70", "Residual_Chips_80", "Residual_Chips_90", "Residual_Chips_100", "Residual_Chips_110", "Residual_Chips_120", "Residual_Chips_130", "Residual_Chips_140", "Residual_Chips_150", "Residual_Chips_160", "Residual_Chips_170", "Residual_Chips_180", "Residual_Chips_190", "Residual_Chips_200", "Residual_Chips_210", "Residual_Chips_220", "Residual_Chips_230", "Residual_Chips_240", "Residual_Chips_250", "Residual_Chips_260", "Residual_Chips_270", "Residual_Chips_280", "Residual_Chips_290", "Residual_Chips_300", "Residual_Chips_310", "Residual_Chips_320", "Residual_Chips_330", "Residual_Chips_340", "Residual_Chips_350", "Residual_Sawdust_0", "Residual_Sawdust_10", "Residual_Sawdust_20", "Residual_Sawdust_30", "Residual_Sawdust_40", "Residual_Sawdust_50", "Residual_Sawdust_60", "Residual_Sawdust_70", "Residual_Sawdust_80", "Residual_Sawdust_90", "Residual_Sawdust_100", "Residual_Sawdust_110", "Residual_Sawdust_120", "Residual_Sawdust_130", "Residual_Sawdust_140", "Residual_Sawdust_150", "Residual_Sawdust_160", "Residual_Sawdust_170", "Residual_Sawdust_180", "Residual_Sawdust_190", "Residual_Sawdust_200", "Residual_Sawdust_210", "Residual_Sawdust_220", "Residual_Sawdust_230", "Residual_Sawdust_240", "Residual_Sawdust_250", "Residual_Sawdust_260", "Residual_Sawdust_270", "Residual_Sawdust_280", "Residual_Sawdust_290", "Residual_Sawdust_300", "Residual_Sawdust_310", "Residual_Sawdust_320", "Residual_Sawdust_330", "Residual_Sawdust_340", "Residual_Sawdust_350", "Residual_Shavings_0", "Residual_Shavings_10", "Residual_Shavings_20", "Residual_Shavings_30", "Residual_Shavings_40", "Residual_Shavings_50", "Residual_Shavings_60", "Residual_Shavings_70", "Residual_Shavings_80", "Residual_Shavings_90", "Residual_Shavings_100", "Residual_Shavings_110", "Residual_Shavings_120", "Residual_Shavings_130", "Residual_Shavings_140", "Residual_Shavings_150", "Residual_Shavings_160", "Residual_Shavings_170", "Residual_Shavings_180", "Residual_Shavings_190", "Residual_Shavings_200", "Residual_Shavings_210", "Residual_Shavings_220", "Residual_Shavings_230", "Residual_Shavings_240", "Residual_Shavings_250", "Residual_Shavings_260", "Residual_Shavings_270", "Residual_Shavings_280", "Residual_Shavings_290", "Residual_Shavings_300", "Residual_Shavings_310", "Residual_Shavings_320", "Residual_Shavings_330", "Residual_Shavings_340", "Residual_Shavings_350", "Residual_Trim_0", "Residual_Trim_10", "Residual_Trim_20", "Residual_Trim_30", "Residual_Trim_40", "Residual_Trim_50", "Residual_Trim_60", "Residual_Trim_70", "Residual_Trim_80", "Residual_Trim_90", "Residual_Trim_100", "Residual_Trim_110", "Residual_Trim_120", "Residual_Trim_130", "Residual_Trim_140", "Residual_Trim_150", "Residual_Trim_160", "Residual_Trim_170", "Residual_Trim_180", "Residual_Trim_190", "Residual_Trim_200", "Residual_Trim_210", "Residual_Trim_220", "Residual_Trim_230", "Residual_Trim_240", "Residual_Trim_250", "Residual_Trim_260", "Residual_Trim_270", "Residual_Trim_280", "Residual_Trim_290", "Residual_Trim_300", "Residual_Trim_310", "Residual_Trim_320", "Residual_Trim_330", "Residual_Trim_340", "Residual_Trim_350", "Residual_Bark_0", "Residual_Bark_10", "Residual_Bark_20", "Residual_Bark_30", "Residual_Bark_40", "Residual_Bark_50", "Residual_Bark_60", "Residual_Bark_70", "Residual_Bark_80", "Residual_Bark_90", "Residual_Bark_100", "Residual_Bark_110", "Residual_Bark_120", "Residual_Bark_130", "Residual_Bark_140", "Residual_Bark_150", "Residual_Bark_160", "Residual_Bark_170", "Residual_Bark_180", "Residual_Bark_190", "Residual_Bark_200", "Residual_Bark_210", "Residual_Bark_220", "Residual_Bark_230", "Residual_Bark_240", "Residual_Bark_250", "Residual_Bark_260", "Residual_Bark_270", "Residual_Bark_280", "Residual_Bark_290", "Residual_Bark_300", "Residual_Bark_310", "Residual_Bark_320", "Residual_Bark_330", "Residual_Bark_340", "Residual_Bark_350"], "value_columns": [], "has_grade_or_residue_or_value": true, "note": "The refreshed TSA24 BTC /TSR output now exposes Logs_Grade_D/F/H/I/J/U/X/Y and Residual_Chips/Sawdust/Shavings/Trim/Bark by age. It still has no value, price, or sort columns."}
- Caveat: TIPSY Yield is treated as m3/ha. Grade and residue surfaces are reported separately by the TSA24 grade benchmark; this volume join does not assert grade equivalence. The sort and price profile is a placeholder.

### BTC merchantable volume

- Status: **reported_with_join_assumptions**
- Matched plots: **14** of **20** have a managed AU; **12** have a positive BTC volume and enter the comparison; **2** match an AU but have zero BTC volume at the plot age; **6** have no AU match.
- Match tiers: **au_curve**=12, **no_au_match**=6, **zero_btc_volume**=2.
- Join basis: FAIB plot -> BEC + leading species -> managed FEMIC AU stratum (including combined-species strata) -> FEMIC AU site-index class -> managed AU; BTC /TSR volume interpolated at FAIB stand age. This is the same benchmark join as the grade table, not an operational AU assignment.

| comparison | n | mean_value | mean_btc | bias_value_minus_btc | mae | rmse | relative_bias_value_vs_btc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Observed PSP VOL_MER*PHF (all live trees) | 12 | 231.27 | 229.21 | 2.06 | 122.72 | 148.27 | 0.01 |
| Pilot bucked logs (ratio-expanded) | 12 | 201.09 | 229.21 | -28.12 | 126.86 | 151.08 | -0.12 |
| Pilot bucked logs (sampled trees only) | 12 | 41.80 | 229.21 | -187.41 | 196.27 | 231.71 | -0.82 |

Plot-level volume join:

| plot_id | leading species | stand age | au_id | match_tier | BTC m3/ha | observed m3/ha | pilot m3/ha (ratio est.) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4035884-PSP1 | SW | 169.00 | n/a | no_au_match | n/a | 482.08 | 408.37 |
| 4035967-PSP1 | SW | 40.00 | 23,000.00 | au_curve | 27.50 | 1.88 | 0.00 |
| 4036113-PSP1 | BL | 249.00 | 23,003.00 | au_curve | 458.35 | 505.13 | 483.29 |
| 4036956-PSP1 | HW | 89.00 | n/a | no_au_match | n/a | 192.84 | 168.52 |
| 4037163-PSP1 | BL | 209.00 | 23,001.00 | au_curve | 267.96 | 303.04 | 290.84 |
| 4037899-PSP2 | SW | 14.00 | 23,000.00 | zero_btc_volume | 0.00 | 194.75 | 162.97 |
| 4038213-PSP1 | FD | 89.00 | 23,008.00 | au_curve | 211.99 | 422.89 | 356.80 |
| 4038237-PSP1 | EP | 69.00 | n/a | no_au_match | n/a | 46.82 | 0.00 |
| 4038318-PSP1 | SW | n/a | n/a | no_au_match | n/a | 309.09 | 281.51 |
| 4038415-PSP2 | AT | 16.00 | 23,007.00 | au_curve | 0.06 | 167.68 | 128.70 |
| 4038551-PSP2 | PL | 97.00 | 23,002.00 | au_curve | 404.49 | 201.74 | 170.99 |
| 4038570-PSP2 | SW | 112.00 | 23,000.00 | au_curve | 338.40 | 201.82 | 165.94 |
| 4038614-PSP1 | BL | 6.00 | 22,003.00 | zero_btc_volume | 0.00 | 93.05 | 55.09 |
| 4040936-PSP1 | PL | 142.00 | n/a | no_au_match | n/a | 188.72 | 137.51 |
| 4045088-PSP1 | BL | 92.00 | 23,003.00 | au_curve | 278.34 | 147.55 | 110.04 |
| 4045109-PSP1 | SW | 50.00 | 23,000.00 | au_curve | 80.10 | 368.39 | 351.32 |
| 4045124-PSP2 | PL | 57.00 | 23,002.00 | au_curve | 200.07 | 43.10 | 0.00 |
| 4045144-PSP1 | SW | 101.00 | 23,000.00 | au_curve | 313.90 | 276.17 | 242.84 |
| 4045365-PSP2 | BL | 134.00 | 23,001.00 | au_curve | 169.38 | 135.82 | 112.37 |
| 4045366-PSP1 | SE | 249.00 | n/a | no_au_match | n/a | 126.67 | 82.59 |

The primary comparison is the ratio-expanded pilot bucked volume against
the BTC `volume` at the same AU and FAIB stand age. The observed PSP
`VOL_MER*PHF` comparison is a sanity check on the same join. The
sampled-tree comparison is shown only to make the expansion explicit; it
is not a stand-level estimate.

- Caveat: The comparison is a benchmark, not a validation gate. The FAIB stand age and the managed AU age origin are not guaranteed to be the same clock; young plots can show near-zero BTC volume and are reported as unmatched by volume rather than silently clipped.

### TSA24 grade benchmark (BTC /TSR) — not validated

- Status: **not validated** (grade shares are a model-output proxy, not a field-grade check).
- Compiled curves: `data/derived/national/bucking/tsa24_grade_curves`
- Match tiers: **14** AU-curve, **3** species-curve, **3** no-match; **12** grade-comparable.
- TIPSY grade shares (proxy; `Logs_Grade_*`): D=0.0%, F=0.0%, H=2.6%, I=0.2%, J=58.0%, U=29.9%, X=6.9%, Y=2.4%
- TIPSY grade-group proxy: high_grade_D_F_H_I=2.8%, sawlog_group_D_F_H_I_J=60.8%, low_grade_U_X_Y=39.2%
- Pilot product shares (comparable plots): sawlog=96.9%, other=3.1%, pulpwood=0.0%
- Value: **not_computed_no_same_basis_grade_prices** — The pilot uses product-level BC Interior log prices.  No same-basis interior grade price vector is available, so only shares are reported.
- Join basis: FAIB plot -> BEC + leading species -> managed FEMIC AU stratum (including combined-species strata) -> FEMIC AU site-index class -> managed AU; BTC /TSR curve interpolated at FAIB stand age. Species fallback uses a mean of the same-species managed AU curves and is labelled separately.
- Why this is not validated: the pilot bucker assigns dimension-only
  industrial sorts (`bc_interior.yaml`), not BC log grades. `Logs_Grade_*`
  is BTC /TSR model output at its own interior rules, not a measured field
  grade. The two surfaces do not share a grade definition.
- D/F status: `Logs_Grade_D` and `Logs_Grade_F` are zero for every TSA24
  AU in this run. Any comparison is therefore limited to H/I/J/U/X/Y and
  cannot validate premium-grade shares.
- Caveat: Pilot sort codes are dimension-only industrial sorts, not BC log grades.  TIPSY Logs_Grade_* values are BTC model output, not field grades; compare grade groups only as a proxy.

### RSYC

- Status: **reported_with_join_assumptions**
- TSA centroid tile: **J4**; ecodistrict: **Montane Cordillera/Northern Montane Cordillera/Fraser Basin/Nechako Lowland**
- Curve join: TSA24 centroid -> RSYC tile and ecodistrict; volume curves at ages 20-140
- Plot join: sample plot coordinates -> RSYC ecodistrict; plot-level volume at stand age
- Curve rows: **130**; plot matches: **13**
- Observed-all vs RSYC: n=13, bias=44.15, MAE=115.13, rel.bias=20.0%
- Bucked ratio-estimated vs RSYC: n=13, bias=82.01, MAE=119.18, rel.bias=44.9%
- Caveat: RSYC is a stand-level remote-sensing yield product. Its volume response is total volume, not merchantable volume, and it has no tree lists, diameter distribution, grade, or residue. This is a coarse sanity check, not a bucking calibration.
- Next step: If the plot-level ecodistrict join is sparse, join all TSA24 VRI polygons to RSYC tiles/ecodistricts and compare area-weighted curves rather than using a centroid-only check.

## 5. Residue ledgers

### Taper residue (pilot bucker)

- Residue volume: **10.289 m³**
- Residue ODT: **4.630 ODT**
- Green tonnes at 45% moisture: **8.418 t**
- Green tonnes at 30% moisture: **6.614 t**
- Chip green tonnes at 45% and 0.90 yield: **7.576 t**
- Mean residue: **8.921 m³/ha**; **4.014 ODT/ha**
- Mean green tonnes/ha (45% / 30%): **7.299** / **5.735**

Taper residue is `taper total - recovered logs` over the sampled stems.
It covers the stump-height section, top, and unmerchantable stem
sections. It does **not** include branches, foliage, or bark.

### Harvest slash (AGB - merchantable log biomass)

- Status: **reported_with_mass_balance_screen**
- Primary plots: **8** of **20**; **12** excluded by the mass-balance / volume-ratio screen.
- Status counts: **no_au_match**=6, **ok**=8, **volume_ratio_out_of_range**=4, **zero_btc_volume**=2.

| plot_id | leading_species | stand_age | au_id | AGB ODT/ha | log ODT/ha | slash ODT/ha | taper ODT/ha | branch+foliage+bark ODT/ha | slash ODT/m3 log | recoverable ODT/ha | recoverable green t/ha (45%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4036113-PSP1 | BL | 249.000 | 23,003.000 | 323.060 | 166.199 | 156.861 | 12.229 | 57.429 | 0.325 | 94.117 | 171.122 |
| 4037163-PSP1 | BL | 209.000 | 23,001.000 | 199.800 | 93.228 | 106.572 | 6.551 | 41.143 | 0.366 | 63.943 | 116.261 |
| 4038213-PSP1 | FD | 89.000 | 23,008.000 | 439.625 | 162.087 | 277.538 | 46.722 | 142.572 | 0.778 | 166.523 | 302.769 |
| 4038551-PSP2 | PL | 97.000 | 23,002.000 | 122.279 | 64.421 | 57.858 | 18.132 | 20.963 | 0.338 | 34.715 | 63.118 |
| 4038570-PSP2 | SW | 112.000 | 23,000.000 | 130.643 | 60.211 | 70.433 | 19.461 | 25.740 | 0.424 | 42.260 | 76.836 |
| 4045088-PSP1 | BL | 92.000 | 23,003.000 | 109.095 | 35.225 | 73.870 | 22.062 | 24.819 | 0.671 | 44.322 | 80.585 |
| 4045144-PSP1 | SW | 101.000 | 23,000.000 | 181.176 | 88.343 | 92.833 | 30.049 | 37.039 | 0.382 | 55.700 | 101.272 |
| 4045365-PSP2 | BL | 134.000 | 23,001.000 | 101.692 | 36.474 | 65.218 | 12.858 | 25.563 | 0.580 | 39.131 | 71.147 |

Excluded plots (retained in the CSV with a reason):

| plot_id | BEC | leading species | stand age | status | reason |
| --- | --- | --- | --- | --- | --- |
| 4035884-PSP1 | ICH | SW | 169.00 | no_au_match | no managed FEMIC AU for BEC + leading species + SI class |
| 4035967-PSP1 | SBS | SW | 40.00 | volume_ratio_out_of_range | observed/BTC volume ratio 0.068 outside 0.40-2.50 |
| 4036956-PSP1 | ICH | HW | 89.00 | no_au_match | no managed FEMIC AU for BEC + leading species + SI class |
| 4037899-PSP2 | SBS | SW | 14.00 | zero_btc_volume | BTC volume is zero or non-finite at the plot age |
| 4038237-PSP1 | SBS | EP | 69.00 | no_au_match | no managed FEMIC AU for BEC + leading species + SI class |
| 4038318-PSP1 | SBS | SW | n/a | no_au_match | no managed FEMIC AU for BEC + leading species + SI class |
| 4038415-PSP2 | SBS | AT | 16.00 | volume_ratio_out_of_range | observed/BTC volume ratio 2794.671 outside 0.40-2.50 |
| 4038614-PSP1 | SBS | BL | 6.00 | zero_btc_volume | BTC volume is zero or non-finite at the plot age |
| 4040936-PSP1 | SBPS | PL | 142.00 | no_au_match | no managed FEMIC AU for BEC + leading species + SI class |
| 4045109-PSP1 | SBS | SW | 50.00 | volume_ratio_out_of_range | observed/BTC volume ratio 4.599 outside 0.40-2.50 |
| 4045124-PSP2 | SBS | PL | 57.00 | volume_ratio_out_of_range | observed/BTC volume ratio 0.215 outside 0.40-2.50 |
| 4045366-PSP1 | ESSF | SE | 249.00 | no_au_match | no managed FEMIC AU for BEC + leading species + SI class |

Summary over the primary plots (each plot treated as one hectare):

| metric | n | mean | median | min | max |
| --- | --- | --- | --- | --- | --- |
| agb_odt_ha (ODT/ha) | 8 | 200.921 | 155.910 | 101.692 | 439.625 |
| agb_odt_ha_unscaled (ODT/ha) | 8 | 211.621 | 212.495 | 126.820 | 293.140 |
| merchantable_log_odt_ha (ODT/ha) | 8 | 88.274 | 76.382 | 35.225 | 166.199 |
| harvest_residue_odt_ha (ODT/ha) | 8 | 112.648 | 83.351 | 57.858 | 277.538 |
| taper_residue_odt_ha (ODT/ha) | 8 | 21.008 | 18.797 | 6.551 | 46.722 |
| non_taper_residue_odt_ha (ODT/ha) | 8 | 91.640 | 57.572 | 39.726 | 230.816 |
| branch_foliage_bark_odt_ha (ODT/ha) | 8 | 46.909 | 31.390 | 20.963 | 142.572 |
| unmerchantable_wood_odt_ha (ODT/ha) | 8 | 65.730 | 52.427 | 36.931 | 134.786 |
| recoverable_residue_odt_ha (ODT/ha) | 8 | 67.589 | 50.011 | 34.715 | 166.523 |
| green_tonnes_45_ha (green t/ha) | 8 | 204.814 | 151.548 | 105.197 | 504.614 |
| green_tonnes_30_ha (green t/ha) | 8 | 160.926 | 119.074 | 82.655 | 396.483 |
| recoverable_green_tonnes_45_ha (green t/ha) | 8 | 122.889 | 90.929 | 63.118 | 302.769 |
| recoverable_chip_green_tonnes_ha (green t/ha) | 8 | 110.600 | 81.836 | 56.806 | 272.492 |
| harvest_residue_odt_per_m3_log (ODT/m3 log) | 8 | 0.483 | 0.403 | 0.325 | 0.778 |
| taper_residue_odt_per_m3_taper_total (ODT/m3 taper total) | 8 | 0.082 | 0.092 | 0.021 | 0.139 |

Assumptions:

- AGB: BTC `biomass-live` `Biomass_Live_Above`, ODT/ha, at the matched
  managed AU and FAIB stand age. The stand-level value is applied to the
  plot on a per-hectare basis and scaled by the plot's observed/BTC
  merchantable-volume ratio, so AGB and pilot logs share a productivity
  basis; no per-tree AGB is invented. The unscaled AGB is retained in the
  ledger CSV as `agb_odt_ha_unscaled`.
- Merchantable log biomass: `sum(log_volume_m3 * basic_density_odt_m3)`.
  Log volume is expanded by `PHF_TREE` and then by the observed all-tree
  / sampled-tree merchantable-volume ratio.
- Basic density: species-specific defaults in
  `workflows/national/bucking/rules/bc_basic_density.csv`. The table is
  derived from the FVS-BC variant NBEL/FIA wood dry-weight table
  (Smith & Miles 2009), converted at 16.01846 kg/m³ per lb/ft³. It is a
  species default, **not** a BC-local sampled value.
- Roadside recovery: **60%** of the AGB-based
  slash is assumed recoverable at roadside.
- Moisture: **45%** wet basis green, **30%**
  seasoned; chip yield **90%** of green residue tonnes.
- Volume-ratio screen: plots outside **0.40-2.50** observed/BTC volume, or with AGB not above log biomass, are reported but
  excluded from the primary ledger. This prevents a bad AU/age join from
  being presented as negative slash.
- Why AGB-based slash exceeds taper residue: AGB includes bark, branches,
  and foliage, while the taper ledger only covers top, stump, and
  unmerchantable stem sections. The per-plot table reports both, plus the
  branch+foliage+bark and unmerchantable-wood components.

**Not mill residue.** BTC `Residual_Chips`, `Residual_Sawdust`,
`Residual_Shavings`, `Residual_Trim`, and `Residual_Bark` are
mill-processing residues. They are not harvest slash and are deliberately
not used as a validation target for this ledger.

## 6. Evidence and provenance

| Item | Evidence tier |
|---|---|
| FAIB PSP tree list | measured plot data |
| Kozak 2004 taper | published_table |
| TIPSY interior dimension sorts | published_table, adapted to geometry-only |
| TSA24 BTC /TSR volume and grade | model_output; AU and site-index specific |
| TSA24 BTC `biomass-live` AGB | model_output; AU and age specific |
| Species basic density | species_default_not_bc_local (FVS-BC NBEL/FIA) |
| BC Interior log prices | published product averages; placeholder for grade value |
| Recovery / moisture / chip yield | assumption |
| Grade assignment | none (`not_assigned`); grade shares not validated |

Input and output hashes are in `manifest.json`.

## 7. Gaps and next steps

- No official grade benchmark: the pilot is dimension-only, so its sort
  shares are not BC log grades. The BTC `Logs_Grade_*` shares are a
  model-output proxy, not a field-grade gate. Grade shares are explicitly
  **not validated**.
- Logs_Grade_D and Logs_Grade_F are zero for every TSA24 AU in this run.
  The grade comparison therefore covers the H/I/J/U/X/Y surface only.
- BTC `Residual_*` is mill-processing residue (chips/sawdust/shavings/
  trim/bark), not harvest slash. It is deliberately excluded from the
  harvest-slash ledger.
- The BTC volume join matches 14 of 20 pilot plots. The six unmatched
  plots are reported with reasons; three have a species-curve grade
  fallback but no managed AU and therefore no BTC volume or AGB join.
- The harvest-slash ledger is a stand-level AGB model comparison, not a
  per-tree biomass audit. It is screened to plots whose observed/BTC
  volume ratio is within the documented band and whose AGB exceeds log
  biomass. Expand the sample and refine the AU/age clock before using it
  as an operational slash supply estimate.
- The VDYP and TIPSY joins use the FEMIC AU crosswalk (BEC + species
  + FEMIC site-index class), including combined-species AUs. The join is
  still a benchmark mapping, not an operational AU assignment.
- The price profile has no pulpwood price for Hem-Bal or Cedar and no prices
  for White Pine or Yellow Pine. Unpriced volume is reported separately.
- Basic density is a species-specific default table (FVS-BC NBEL/FIA),
  not a BC-local sample. Recovery, moisture, and chip yield are assumptions.
  Replace them with species- and product-specific values before publishing
  a residue supply offer.
- The sample is 20 plots and 300 trees. It is a pilot, not a TSA-wide
  estimate. Expand to all TSA24 plots and add a proper design-based
  expansion before operational use.
- RSYC is a stand-level total-volume/AGB check, not a bucking calibration.
