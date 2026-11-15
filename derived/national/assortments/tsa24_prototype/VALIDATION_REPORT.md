# TSA24 stand-to-tree disaggregation — prototype validation

Generated: `2026-11-15T21:28:31.245605+00:00`

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
| BL | stratum_fit | ecodistrict | 2219 | 96 | 2.0 | gamma | -806,188.1 | 0.063 |
| EP | stratum_fit | ecodistrict | 376 | 62 | 2.0 | mixture | -63,993.3 | 0.059 |
| FD | stratum_fit | ecodistrict | 677 | 70 | 2.0 | mixture | -102,182.4 | 0.033 |
| PL | stratum_fit | ecodistrict | 1355 | 91 | 2.0 | mixture | -177,943.8 | 0.012 |
| SB | stratum_fit | ecodistrict | 148 | 18 | 2.0 | mixture | -13,252.1 | 0.022 |
| SW | stratum_fit | ecodistrict | 6477 | 117 | 2.0 | mixture | -1,236,098.8 | 0.021 |

Hierarchical threshold: at least **30 trees** and **5 plots** at the direct
ecodistrict level. The fit falls back to ecoregion, ecoprovince, ecozone, and
then the TSA24 species pool; the fallback level is recorded on every row.
Plots with a non-modal DBH limit are excluded from the shape fit to avoid
mixing different truncation points. Candidate AIC/KS are scored on one common
support-conditioned binned likelihood; native estimator metrics are also kept.

General all-age fits: **68** strata (`stratum_fit` 48, `pooled_fit` 20, `default` 0); selected KS median **0.050**, max **0.221**, high-KS (>0.20) **3**. The full per-candidate table is `distribution_fits.csv`; poor general strata are retained rather than hidden.

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

- Trees: **600**; scale factor: **0.725926**; achieved taper total: **311.600 m3**.
- TPH: **1,062.4**; basal area: **31.96 m2/ha**; QMD: **19.57 cm**.

| species | weight | trees | TPH | QMD cm | taper m3/ha |
|---|---:|---:|---:|---:|---:|
| AT | 0.116 | 70 | 123.5 | 19.72 | 29.0 |
| BL | 0.113 | 68 | 119.6 | 13.51 | 27.3 |
| EP | 0.022 | 13 | 23.7 | 10.70 | 1.0 |
| FD | 0.028 | 17 | 29.9 | 28.95 | 22.1 |
| PL | 0.102 | 61 | 108.2 | 26.37 | 62.1 |
| SB | 0.013 | 7 | 13.3 | 12.41 | 0.9 |
| SW | 0.606 | 364 | 644.1 | 18.98 | 169.2 |

## 7. Assortment matrix

- Logs: **508**; recovered: **259.96 m3**; residue: **51.64 m3**; taper total: **311.60 m3**.
- Residue: **18.70 ODT**; wood AGB proxy: **113.83 ODT**.

| product | volume m3 | share of taper |
|---|---:|---:|
| sawlog | 243.22 | 0.7806 |
| other | 16.44 | 0.0528 |
| pulpwood | 0.30 | 0.0010 |

The matrix is written as `log`, `residue`, and `total` record types. Residue
is taper total minus recovered logs; the species ledger carries density, ODT,
green tonnes, chip tonnes, and a wood-only AGB proxy. The BTC AGB target is
reported beside the wood proxy; it is not expected to match because BTC AGB
includes bark, branches, and foliage. The near-zero pulpwood share is a
property of the dimension-only sawlog rules (12.5 cm top, 5.1 m minimum),
which dominate the value objective; it is not evidence that pulp fibre is absent.
BTC mill residue columns are not logging slash.

## 8. Validation

- **dbh_fit_quantiles**: PASS — per-species weighted quantile MAE < 3.0 cm; max=2.145 cm
- **target_volume**: PASS — achieved 311.600000 m3 vs target 311.600000 m3; scale 0.725926323
- **volume_conservation**: PASS — logs 259.957881 + residue 51.642119 = 311.600000 m3 vs taper 311.600000 m3; error 0 m3
- **species_weights_sum**: PASS — sum=1.000000000000
- **no_negative_values**: PASS — checked matrix volume, residue, ODT, AGB proxy, and log counts

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

- `distribution_fits.csv`, `height_models.csv`, `height_models_general.csv`
- `synthetic_trees.csv`, `species_composition.csv`, `target_stand.json`
- `assortment_matrix.csv`, `bucked_logs.csv`, `residue_ledger.csv`
- `dbh_validation.csv`, `btc_grade_proxy.csv`, `validation_summary.json`, `manifest.json`

