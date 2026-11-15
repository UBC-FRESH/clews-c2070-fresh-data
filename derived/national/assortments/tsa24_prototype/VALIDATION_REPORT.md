# TSA24 stand-to-tree disaggregation — prototype validation

Generated: `2026-11-15T23:15:30.990347+00:00`

Status: **prototype_complete**

> This is a prototype contract and a first TSA24 demonstration. It is not an
> operational national yield model. The assortment sorts are dimension-only;
> no official BC log grade is assigned.

## 1. Contract

- DBH shape comes from the selected RSYC-stratified distribution.
- Height comes from the hierarchical height-diameter model.
- Species composition comes from the TSA24 plot subset.
- Volume scale comes from the BTC managed-AU target, not from the distribution.
- The bucking layer is the existing BC interior rule set and Kozak taper.
- `StandDBHSampler` is not used for the censored fit because it has no support
  bound; the documented `sample_truncated`/`sample_mixture` samplers are used
  instead. This is a sampling-boundary adapter, not a refit.

## 2. TSA24 subset

- Sites selected: **558**; with coordinates: **491**; mapped to RSYC ecodistricts: **491**.
- Plots: **1,318**; live valid trees: **155,904**; species: **19**.
- Dropped: {'dead': 28704, 'invalid_dbh': 0, 'invalid_expansion': 0, 'missing_species': 0, 'missing_plot': 0}.

## 3. Target stand

- BTC AU `23000` / `SBS_SX` (H) at age **100**.
- Target volume: **311.6 m3/ha** × 1 ha = **311.6 m3**.
- Target ecodistrict: **Nechako Lowland**; initial TPH: **1,463.6**.
- Species weights (retained, sum=1): AT=0.116, BL=0.113, EP=0.022, FD=0.028, PL=0.102, SB=0.013, SW=0.606.
- Composition exclusions: [{'species': 'W', 'raw_share': 0.019891068855376937, 'reason': 'unsupported_by_taper_registry'}, {'species': 'AC', 'raw_share': 0.0008096748197094112, 'reason': 'below_minimum_species_share'}, {'species': 'DG', 'raw_share': 0.0005964594420025007, 'reason': 'unsupported_by_taper_registry'}, {'species': 'HW', 'raw_share': 8.737202780016662e-05, 'reason': 'below_minimum_species_share'}].
- Composition plot filter: {'leading_species_group': ['S', 'SB', 'SE', 'SW'], 'n_plots_all': 118, 'n_plots_used': 77, 'fallback_to_all_plots': False, 'target_plot_filter': 'leading_species_group'}.

## 4. DBH fits

| species | tier | level | trees | plots | limit cm | distribution | AIC | KS |
|---|---|---|---:|---:|---:|---|---:|---:|
| AT | stratum_fit | ecodistrict | 2114 | 90 | 2.0 | mixture | -316,150.4 | 0.013 |
| BL | stratum_fit | ecodistrict | 2219 | 96 | 2.0 | mix_weibull_2 | -809,813.8 | 0.023 |
| EP | stratum_fit | ecodistrict | 376 | 62 | 2.0 | mix_weibull_2 | -64,011.0 | 0.028 |
| FD | stratum_fit | ecodistrict | 677 | 70 | 2.0 | mix_weibull_gamma | -102,275.5 | 0.030 |
| PL | stratum_fit | ecodistrict | 1355 | 91 | 2.0 | mix_weibull_2 | -178,149.6 | 0.011 |
| SB | stratum_fit | ecodistrict | 148 | 18 | 2.0 | mix_weibull_gamma | -13,245.5 | 0.026 |
| SW | stratum_fit | ecodistrict | 6477 | 117 | 2.0 | mix_weibull_gamma | -1,236,592.6 | 0.009 |

Hierarchical threshold: at least **30 trees** and **5 plots** at the direct
ecodistrict level. The fit falls back to ecoregion, ecoprovince, ecozone, and
then the TSA24 species pool; the fallback level is recorded on every row.
Plots with a non-modal DBH limit are excluded from the shape fit to avoid
mixing different truncation points. Candidate AIC/KS are scored on one common
support-conditioned binned likelihood; native estimator metrics are also kept.

General all-age fits: **68** strata (`stratum_fit` 48, `pooled_fit` 20, `default` 0); selected KS median **0.031**, max **0.221**, high-KS (>0.20) **3**. The full per-candidate table is `distribution_fits.csv`; poor general strata are retained rather than hidden.

### 4b. Mixture candidates and previous-run comparison

- New Weibull mixture selections: **45** of **75** matched strata.
- Improved by >2 AIC: **42**; worse by >2 AIC: **1**; mixtures worse than the previous selected model: **23**.
- Unstable mixture fits reported: **99**; new-family unstable fits are not selected; degenerate rejections: **28**.
- High-KS (>0.20) selected strata before: **3**, after: **3**.

| family | attempted | ok | converged | selected |
|---|---:|---:|---:|---:|
| mixture | 75 | 75 | 18 | 22 |
| mix_weibull_2 | 75 | 61 | 51 | 12 |
| mix_weibull_gamma | 75 | 64 | 60 | 33 |
| mix_weibull_3 | 3 | 0 | 0 | 0 |

| fit | previous | selected | delta AIC | delta AICc | previous KS | selected KS | best new mixture | best new delta AIC |
|---|---|---|---:|---:|---:|---:|---|---:|
| ecodistrict:Babine upland|AT | mixture | mixture | 0.0 | 0.0 | 0.090 | 0.090 | mix_weibull_2 | 1,534.3 |
| ecodistrict:Babine upland|BL | gamma | mix_weibull_gamma | -44.9 | -43.0 | 0.008 | 0.011 | mix_weibull_gamma | -44.9 |
| ecoregion:Fraser Basin|DG | mixture | mix_weibull_gamma | -1,492.8 | -1,492.8 | 0.156 | 0.065 | mix_weibull_gamma | -1,492.8 |
| ecodistrict:Babine upland|EP | mixture | mixture | 0.0 | 0.0 | 0.011 | 0.011 | mix_weibull_gamma | 2,442.7 |
| ecodistrict:Babine upland|FD | mixture | mix_weibull_gamma | -572.0 | -572.0 | 0.054 | 0.022 | mix_weibull_gamma | -572.0 |
| ecodistrict:Babine upland|PL | mixture | mixture | 0.0 | 0.0 | 0.020 | 0.020 | mix_weibull_gamma | 93.0 |
| ecodistrict:Babine upland|SW | gamma | gamma | 0.0 | 0.0 | 0.021 | 0.021 | mix_weibull_2 | 199.3 |
| ecoregion:Columbia Mountains and Highlands|BL | gamma | mix_weibull_2 | -198.4 | -197.0 | 0.015 | 0.022 | mix_weibull_2 | -198.4 |
| ecozone:Montane Cordillera|FD | mixture | mix_weibull_gamma | -3,631.5 | -3,631.5 | 0.074 | 0.011 | mix_weibull_gamma | -3,631.5 |
| ecoprovince:Columbia Montane Cordillera|SW | mixture | mixture | 0.0 | 0.0 | 0.081 | 0.081 | mix_weibull_gamma | 11.3 |
| ecoregion:Fraser Plateau|AT | mixture | mix_weibull_gamma | -112.6 | -112.6 | 0.029 | 0.019 | mix_weibull_gamma | -112.6 |
| ecodistrict:Bulkley Basin|BL | weibull | mix_weibull_2 | -244.8 | -241.2 | 0.021 | 0.026 | mix_weibull_2 | -244.8 |
| ecozone:Montane Cordillera|EP | weibull | weibull | 0.0 | 0.0 | 0.023 | 0.023 | mix_weibull_2 | 1,859.3 |
| ecodistrict:Bulkley Basin|FD | mixture | mixture | -0.0 | -0.0 | 0.038 | 0.038 | mix_weibull_gamma | 270.6 |
| ecodistrict:Bulkley Basin|PL | gamma | mix_weibull_gamma | -3,669.9 | -3,666.3 | 0.048 | 0.040 | mix_weibull_gamma | -3,669.9 |
| ecodistrict:Bulkley Basin|SW | weibull | mix_weibull_gamma | -3.0 | 1.0 | 0.038 | 0.040 | mix_weibull_gamma | -3.0 |
| ecodistrict:Hart Ranges|BL | mixture | mix_weibull_gamma | -938.2 | -938.2 | 0.068 | 0.041 | mix_weibull_gamma | -938.2 |
| ecozone:Montane Cordillera|CW | mixture | mixture | -0.0 | 0.0 | 0.221 | 0.221 | mix_weibull_2 | 6,479.6 |
| ecoprovince:Northern Montane Cordillera|EP | weibull | weibull | 0.0 | 0.0 | 0.026 | 0.026 | mix_weibull_2 | 1,756.6 |
| ecodistrict:Hart Ranges|HW | mixture | mix_weibull_2 | -18.7 | -18.7 | 0.124 | 0.089 | mix_weibull_2 | -18.7 |
| ecodistrict:Hart Ranges|SE | mixture | mix_weibull_gamma | -65.8 | -65.8 | 0.046 | 0.031 | mix_weibull_gamma | -65.8 |
| ecodistrict:Hart Ranges|SW | mixture | mixture | 0.0 | 0.0 | 0.046 | 0.046 | mix_weibull_gamma | 227.0 |
| ecoregion:Fraser Basin|AC | gamma | mix_weibull_gamma | -1,148.0 | -1,146.6 | 0.099 | 0.041 | mix_weibull_gamma | -1,148.0 |
| ecodistrict:McGregor Plateau|AT | mixture | mix_weibull_2 | -1.9 | -1.9 | 0.065 | 0.050 | mix_weibull_2 | -1.9 |
| ecodistrict:McGregor Plateau|BL | mixture | mix_weibull_2 | -1,809.3 | -1,809.3 | 0.046 | 0.021 | mix_weibull_2 | -1,809.3 |
| ecozone:Montane Cordillera|CW | mixture | mixture | -0.0 | 0.0 | 0.221 | 0.221 | mix_weibull_2 | 6,479.6 |
| ecodistrict:McGregor Plateau|DG | mixture | mix_weibull_gamma | -377.5 | n/a | 0.142 | 0.010 | mix_weibull_gamma | -377.5 |
| ecodistrict:McGregor Plateau|DM | mixture | mix_weibull_gamma | -106.0 | n/a | 0.046 | 0.010 | mix_weibull_gamma | -106.0 |
| ecodistrict:McGregor Plateau|EP | mixture | mixture | 0.0 | 0.0 | 0.023 | 0.023 | mix_weibull_gamma | 54.4 |
| ecodistrict:McGregor Plateau|HW | mixture | mixture | 0.0 | 0.0 | 0.082 | 0.082 | mix_weibull_gamma | 156.3 |
| ecodistrict:McGregor Plateau|MR | mixture | mix_weibull_gamma | -112.8 | n/a | 0.106 | 0.010 | mix_weibull_gamma | -112.8 |
| ecodistrict:McGregor Plateau|PL | mixture | mixture | 0.0 | 0.0 | 0.026 | 0.026 | mix_weibull_gamma | 33.0 |
| ecodistrict:McGregor Plateau|SE | gamma | mix_weibull_gamma | -138.3 | -137.3 | 0.055 | 0.039 | mix_weibull_gamma | -138.3 |
| ecodistrict:McGregor Plateau|SW | weibull | mix_weibull_gamma | -2,538.7 | -2,537.8 | 0.031 | 0.014 | mix_weibull_gamma | -2,538.7 |
| ecozone:Montane Cordillera|AC | mixture | mix_weibull_gamma | -1,255.4 | -1,255.4 | 0.184 | 0.040 | mix_weibull_gamma | -1,255.4 |
| ecodistrict:Nazko Upland|AT | mixture | mix_weibull_2 | -132.5 | -132.5 | 0.024 | 0.017 | mix_weibull_2 | -132.5 |
| ecodistrict:Nazko Upland|BL | weibull | mix_weibull_gamma | -656.2 | -653.6 | 0.077 | 0.053 | mix_weibull_gamma | -656.2 |
| ecodistrict:Nazko Upland|DG | mixture | mix_weibull_gamma | -295.5 | n/a | 0.099 | 0.009 | mix_weibull_gamma | -295.5 |
| ecodistrict:Nazko Upland|PL | gamma | mix_weibull_gamma | -14,583.5 | -14,581.4 | 0.094 | 0.043 | mix_weibull_gamma | -14,583.5 |
| ecodistrict:Nazko Upland|SB | mixture | mix_weibull_2 | -337.3 | -337.3 | 0.131 | 0.053 | mix_weibull_2 | -337.3 |
| ecozone:Montane Cordillera|SE | weibull | mix_weibull_gamma | -133.2 | -132.2 | 0.022 | 0.032 | mix_weibull_gamma | -133.2 |
| ecoregion:Fraser Plateau|W | mixture | mix_weibull_gamma | 0.5 | 0.5 | 0.024 | 0.024 | mix_weibull_gamma | 0.5 |
| ecodistrict:Nechako Lowland|AC | mixture | mix_weibull_gamma | -365.2 | -365.2 | 0.103 | 0.033 | mix_weibull_gamma | -365.2 |
| ecodistrict:Nechako Lowland|AT | mixture | mix_weibull_gamma | -488.3 | -488.3 | 0.013 | 0.006 | mix_weibull_gamma | -488.3 |
| ecodistrict:Nechako Lowland|BL | gamma | mix_weibull_gamma | -1,046.6 | -1,044.8 | 0.024 | 0.029 | mix_weibull_2 | -1,099.8 |
| ecodistrict:Nechako Lowland|DG | mixture | mix_weibull_gamma | -746.2 | n/a | 0.140 | 0.132 | mix_weibull_gamma | -746.2 |
| ecoregion:Fraser Basin|DM | mixture | mix_weibull_gamma | -210.4 | n/a | 0.069 | 0.013 | mix_weibull_gamma | -210.4 |
| ecodistrict:Nechako Lowland|EP | weibull | mix_weibull_2 | -811.9 | -810.0 | 0.025 | 0.014 | mix_weibull_2 | -811.9 |
| ecodistrict:Nechako Lowland|FD | weibull | mix_weibull_gamma | -1,985.3 | -1,984.6 | 0.049 | 0.015 | mix_weibull_gamma | -1,985.3 |
| ecoregion:Fraser Basin|MR | mixture | mix_weibull_gamma | -119.7 | n/a | 0.057 | 0.010 | mix_weibull_gamma | -119.7 |
| ecodistrict:Nechako Lowland|PL | mixture | mixture | 0.0 | 0.0 | 0.051 | 0.051 | mix_weibull_gamma | 2,677.4 |
| ecodistrict:Nechako Lowland|SB | mixture | mix_weibull_2 | -49.9 | -49.9 | 0.038 | 0.010 | mix_weibull_2 | -49.9 |
| ecodistrict:Nechako Lowland|W | mixture | mix_weibull_gamma | -656.9 | -656.9 | 0.052 | 0.068 | mix_weibull_gamma | -656.9 |
| ecodistrict:Northern Columbia Mountains|BL | mixture | mixture | 0.0 | 0.0 | 0.033 | 0.033 | mix_weibull_2 | 29.7 |
| ecodistrict:Northern Columbia Mountains|SE | mixture | mixture | 0.0 | 0.0 | 0.098 | 0.098 | mix_weibull_2 | 229.4 |
| ecodistrict:Upper Fraser Trench|BL | gamma | gamma | 0.0 | 0.0 | 0.022 | 0.022 | mix_weibull_gamma | 234.6 |
| ecoprovince:Columbia Montane Cordillera|CW | mixture | mixture | 0.0 | 0.0 | 0.217 | 0.217 | mix_weibull_2 | 24,652.4 |
| ecozone:Montane Cordillera|EP | weibull | weibull | 0.0 | 0.0 | 0.023 | 0.023 | mix_weibull_2 | 1,859.3 |
| ecozone:Montane Cordillera|HW | mixture | mix_weibull_gamma | -193.6 | -193.6 | 0.060 | 0.017 | mix_weibull_gamma | -193.6 |
| ecodistrict:Upper Fraser Trench|SW | gamma | gamma | 0.0 | 0.0 | 0.062 | 0.062 | mix_weibull_gamma | 123.4 |
| ecodistrict:Nechako Lowland|AT | mixture | mixture | 0.0 | 0.0 | 0.013 | 0.013 | mix_weibull_2 | 1,942.6 |
| ecodistrict:Nechako Lowland|BL | gamma | mix_weibull_2 | -3,625.7 | -3,623.9 | 0.063 | 0.023 | mix_weibull_2 | -3,625.7 |
| ecodistrict:Nechako Lowland|EP | mixture | mix_weibull_2 | -17.7 | -17.7 | 0.059 | 0.028 | mix_weibull_2 | -17.7 |
| ecodistrict:Nechako Lowland|FD | mixture | mix_weibull_gamma | -93.1 | -93.1 | 0.033 | 0.030 | mix_weibull_gamma | -93.1 |
| ecodistrict:Nechako Lowland|PL | mixture | mix_weibull_2 | -205.7 | -205.7 | 0.012 | 0.011 | mix_weibull_2 | -205.7 |
| ecodistrict:Nechako Lowland|SB | mixture | mix_weibull_gamma | 6.7 | 6.7 | 0.022 | 0.026 | mix_weibull_gamma | 6.7 |
| ecodistrict:Nechako Lowland|SW | mixture | mix_weibull_gamma | -493.8 | -493.8 | 0.021 | 0.009 | mix_weibull_gamma | -493.8 |

The new families are fitted by a left-truncated EM that delegates each component M-step to `fit_censored_inventory` (Weibull) or the documented gamma moment update. Components are sorted by scale after every update. New Weibull mixtures are synthesis-eligible only when they converged. The legacy two-gamma mixture remains available as a fallback and carries a ten-unit AIC penalty when it did not converge; non-converged legacy selections are flagged in `distribution_fits.csv`. Small AIC gains are resolved in favour of the simpler model.

| unstable fit | family | status | converged | iterations |
|---|---|---|---:|---:|
| ecodistrict:Babine upland|BL | mixture | ok | False | 200 |
| ecodistrict:Babine upland|BL | mix_weibull_2 | failed | False | 0 |
| ecoregion:Fraser Basin|DG | mixture | ok | False | 200 |
| ecoregion:Fraser Basin|DG | mix_weibull_2 | ok | False | 250 |
| ecodistrict:Babine upland|EP | mixture | ok | False | 200 |
| ecodistrict:Babine upland|EP | mix_weibull_2 | failed | False | 0 |
| ecodistrict:Babine upland|FD | mixture | ok | False | 200 |
| ecodistrict:Babine upland|PL | mix_weibull_gamma | ok | False | 250 |
| ecodistrict:Babine upland|SW | mixture | ok | False | 200 |
| ecodistrict:Babine upland|W | mixture | ok | False | 200 |
| ecodistrict:Babine upland|W | mix_weibull_2 | failed | False | 0 |
| ecodistrict:Babine upland|W | mix_weibull_gamma | failed | False | 0 |

## 5. Height models

| species | tier | level | n | a | b | RMSE m | bias m |
|---|---|---|---:|---:|---:|---:|---:|
| AT | stratum_fit | ecodistrict | 2114 | 0.97547 | 0.6300 | 2.08 | 0.10 |
| BL | stratum_fit | ecodistrict | 2219 | -1.07799 | 1.3042 | 2.86 | -0.11 |
| EP | stratum_fit | ecodistrict | 376 | 0.62603 | 0.7738 | 3.12 | 0.08 |
| FD | stratum_fit | ecodistrict | 677 | -0.43483 | 1.0487 | 3.82 | -0.19 |
| PL | stratum_fit | ecodistrict | 1355 | 0.98861 | 0.6382 | 2.79 | 0.08 |
| SB | stratum_fit | ecodistrict | 148 | -0.26585 | 1.0086 | 1.81 | -0.01 |
| SW | stratum_fit | ecodistrict | 6477 | -0.47464 | 1.0861 | 3.00 | -0.12 |

## 6. Synthetic tree list

- Trees: **600**; scale factor: **0.837134**; achieved taper total: **311.600 m3**.
- TPH: **1,225.2**; basal area: **33.72 m2/ha**; QMD: **18.72 cm**.

| species | weight | trees | TPH | QMD cm | taper m3/ha |
|---|---:|---:|---:|---:|---:|
| AT | 0.116 | 70 | 142.4 | 19.60 | 32.8 |
| BL | 0.113 | 68 | 137.9 | 12.20 | 13.7 |
| EP | 0.022 | 13 | 27.3 | 15.96 | 4.3 |
| FD | 0.028 | 17 | 34.5 | 23.00 | 12.8 |
| PL | 0.102 | 61 | 124.8 | 25.25 | 64.7 |
| SB | 0.013 | 7 | 15.4 | 12.69 | 1.0 |
| SW | 0.606 | 364 | 742.8 | 18.23 | 182.3 |

## 7. Assortment matrix

- Logs: **489**; recovered: **252.58 m3**; residue: **59.02 m3**; taper total: **311.60 m3**.
- Residue: **21.43 ODT**; wood AGB proxy: **114.08 ODT**.

| product | volume m3 | share of taper |
|---|---:|---:|
| sawlog | 231.74 | 0.7437 |
| other | 20.49 | 0.0658 |
| pulpwood | 0.35 | 0.0011 |

The matrix is written as `log`, `residue`, and `total` record types. Residue
is taper total minus recovered logs; the species ledger carries density, ODT,
green tonnes, chip tonnes, and a wood-only AGB proxy. The BTC AGB target is
reported beside the wood proxy; it is not expected to match because BTC AGB
includes bark, branches, and foliage. The near-zero pulpwood share is a
property of the dimension-only sawlog rules (12.5 cm top, 5.1 m minimum),
which dominate the value objective; it is not evidence that pulp fibre is absent.
BTC mill residue columns are not logging slash.

## 8. Validation

- **dbh_fit_quantiles**: PASS — per-species weighted quantile MAE < 3.0 cm; max=0.775 cm
- **target_volume**: PASS — achieved 311.600000 m3 vs target 311.600000 m3; scale 0.837133819
- **volume_conservation**: PASS — logs 252.582033 + residue 59.017967 = 311.600000 m3 vs taper 311.600000 m3; error 0 m3
- **species_weights_sum**: PASS — sum=1.000000000000
- **no_negative_values**: PASS — checked matrix volume, residue, ODT, AGB proxy, and log counts
- **selected_mixtures_converged**: PASS — every selected Weibull mixture converged; a non-converged legacy two-gamma fallback may remain selected and is flagged in distribution_fits.csv

DBH quantile validation is in `dbh_validation.csv`; conservation is in
`validation_summary.json`. The optional BTC grade proxy is **not** a grade
validation: BTC TIPSY grades and dimension-only sorts are different objects.

## 9. Evidence tiers

| tier | use in this run |
|---|---|
| `stratum_fit` | direct ecodistrict/species DBH or height fit |
| `pooled_fit` | ecoregion/ecoprovince/ecozone fallback |
| `default` | TSA24 species-only fallback |

## 10. Artifacts

- `distribution_fits.csv`, `dbh_mixture_comparison.csv`, `height_models.csv`, `height_models_general.csv`
- `synthetic_trees.csv`, `species_composition.csv`, `target_stand.json`
- `assortment_matrix.csv`, `bucked_logs.csv`, `residue_ledger.csv`
- `dbh_validation.csv`, `btc_grade_proxy.csv`, `validation_summary.json`, `manifest.json`

