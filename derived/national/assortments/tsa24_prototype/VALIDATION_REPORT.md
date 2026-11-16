# TSA24 stand-to-tree disaggregation — prototype validation

Generated: `2026-11-16T02:53:11.954240+00:00`

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
- Dropped: {'dead': 28704, 'invalid_dbh': 0, 'invalid_expansion': 0, 'missing_plot': 0, 'missing_species': 0}.

## 3. Target stand

- BTC AU `23000` / `SBS_SX` (H) at age **100**.
- Target volume: **311.6 m3/ha** × 1 ha = **311.6 m3**.
- Target ecodistrict: **Nechako Lowland**; initial TPH: **1,463.6**.
- Species weights (retained, sum=1): AT=0.116, BL=0.113, EP=0.022, FD=0.028, PL=0.102, SB=0.013, SW=0.606.
- Composition exclusions: [{'raw_share': 0.019891068855376937, 'reason': 'unsupported_by_taper_registry', 'species': 'W'}, {'raw_share': 0.0008096748197094112, 'reason': 'below_minimum_species_share', 'species': 'AC'}, {'raw_share': 0.0005964594420025007, 'reason': 'unsupported_by_taper_registry', 'species': 'DG'}, {'raw_share': 8.737202780016662e-05, 'reason': 'below_minimum_species_share', 'species': 'HW'}].
- Composition plot filter: {'fallback_to_all_plots': False, 'leading_species_group': ['S', 'SB', 'SE', 'SW'], 'n_plots_all': 118, 'n_plots_used': 77, 'target_plot_filter': 'leading_species_group'}.

## 4. DBH fits

| species | tier | level | trees | plots | limit cm | distribution | AIC | KS |
|---|---|---|---:|---:|---:|---|---:|---:|
| AT | stratum_fit | ecodistrict | 2114 | 90 | 2.0 | mixture | -316,150.4 | 0.013 |
| BL | stratum_fit | ecodistrict | 2219 | 96 | 2.0 | spike_weibull_constrained | -810,203.7 | 0.010 |
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

General all-age fits: **68** strata (`stratum_fit` 48, `pooled_fit` 20, `default` 0); selected KS median **0.025**, max **0.146**, high-KS (>0.20) **0**. The full per-candidate table is `distribution_fits.csv`; poor general strata are retained rather than hidden.

### 4b. Mixture candidates and previous-run comparison

- Switches: **14** of **73** matched strata (spike **14**; new finite mixtures **0**).
- Improved by >2 AIC: **13**; worse by >2 AIC: **1**; mixtures worse than the previous selected model: **16**.
- Unstable mixture fits reported: **99**; new-family unstable fits are not selected; degenerate rejections: **28**.
- High-KS (>0.20) selected strata before: **2**, after: **0**.

| family | attempted | ok | converged | selected |
|---|---:|---:|---:|---:|
| mixture | 75 | 75 | 18 | 18 |
| mix_weibull_2 | 75 | 61 | 51 | 10 |
| mix_weibull_gamma | 75 | 64 | 60 | 27 |
| mix_weibull_3 | 3 | 0 | 0 | 0 |
| spike_weibull | 29 | 29 | 29 | 5 |
| spike_gamma | 29 | 29 | 29 | 1 |
| spike_weibull_constrained | 29 | 16 | 29 | 4 |
| spike_gamma_constrained | 29 | 14 | 29 | 4 |

| fit | previous | selected | delta AIC | delta AICc | previous KS | selected KS | best new flexible | best new delta AIC |
|---|---|---|---:|---:|---:|---:|---|---:|
| ecodistrict:Babine upland|AT | mixture | mixture | 0.0 | 0.0 | 0.090 | 0.090 | mix_weibull_2 | 1,534.3 |
| ecodistrict:Babine upland|EP | mixture | mixture | 0.0 | 0.0 | 0.011 | 0.011 | mix_weibull_gamma | 2,442.7 |
| ecodistrict:Babine upland|PL | mixture | mixture | 0.0 | 0.0 | 0.020 | 0.020 | mix_weibull_gamma | 93.0 |
| ecodistrict:Babine upland|SW | gamma | spike_gamma_constrained | -153.3 | -153.3 | 0.021 | 0.015 | spike_gamma_constrained | -153.3 |
| ecoprovince:Columbia Montane Cordillera|SW | mixture | mixture | 0.0 | 0.0 | 0.081 | 0.081 | mix_weibull_gamma | 11.3 |
| ecozone:Montane Cordillera|EP | weibull | weibull | 0.0 | 0.0 | 0.023 | 0.023 | mix_weibull_2 | 1,859.3 |
| ecodistrict:Bulkley Basin|FD | mixture | mixture | 0.0 | 0.0 | 0.038 | 0.038 | mix_weibull_gamma | 270.6 |
| ecodistrict:Hart Ranges|BL | mix_weibull_gamma | spike_weibull | -85.0 | -85.8 | 0.041 | 0.011 | spike_weibull | -85.0 |
| ecozone:Montane Cordillera|CW | mixture | spike_weibull | -795.2 | -796.6 | 0.221 | 0.034 | spike_weibull | -795.2 |
| ecoprovince:Northern Montane Cordillera|EP | weibull | weibull | 0.0 | 0.0 | 0.026 | 0.026 | mix_weibull_2 | 1,756.6 |
| ecodistrict:Hart Ranges|SW | mixture | spike_weibull | 8.6 | 7.6 | 0.046 | 0.023 | spike_weibull | 8.6 |
| ecoregion:Fraser Basin|AC | mix_weibull_gamma | spike_weibull_constrained | -16.7 | -18.1 | 0.041 | 0.022 | spike_weibull_constrained | -16.7 |
| ecodistrict:McGregor Plateau|EP | mixture | mixture | 0.0 | 0.0 | 0.023 | 0.023 | mix_weibull_gamma | 54.4 |
| ecodistrict:McGregor Plateau|HW | mixture | mixture | 0.0 | 0.0 | 0.082 | 0.082 | mix_weibull_gamma | 156.3 |
| ecodistrict:McGregor Plateau|PL | mixture | mixture | 0.0 | 0.0 | 0.026 | 0.026 | mix_weibull_gamma | 33.0 |
| ecozone:Montane Cordillera|AC | mix_weibull_gamma | spike_gamma_constrained | -16.7 | -18.1 | 0.040 | 0.025 | spike_gamma_constrained | -16.7 |
| ecodistrict:Nazko Upland|BL | mix_weibull_gamma | spike_gamma | -382.6 | -385.2 | 0.053 | 0.010 | spike_gamma | -382.6 |
| ecodistrict:Nazko Upland|PL | mix_weibull_gamma | spike_gamma_constrained | -1,271.5 | -1,273.5 | 0.043 | 0.010 | spike_gamma_constrained | -1,271.5 |
| ecodistrict:Nazko Upland|SB | mix_weibull_2 | spike_weibull_constrained | -81.7 | -105.7 | 0.053 | 0.056 | spike_weibull_constrained | -81.7 |
| ecodistrict:Nazko Upland|SW | weibull | spike_gamma_constrained | -170.2 | -170.2 | 0.021 | 0.007 | spike_gamma_constrained | -170.2 |
| ecodistrict:Nechako Lowland|BL | mix_weibull_gamma | spike_weibull_constrained | -1,552.5 | -1,554.3 | 0.029 | 0.011 | spike_weibull_constrained | -1,552.5 |
| ecodistrict:Nechako Lowland|PL | mixture | mixture | 0.0 | 0.0 | 0.051 | 0.051 | mix_weibull_gamma | 2,677.4 |
| ecodistrict:Northern Columbia Mountains|BL | mixture | mixture | 0.0 | 0.0 | 0.033 | 0.033 | mix_weibull_2 | 29.7 |
| ecodistrict:Northern Columbia Mountains|SE | mixture | mixture | 0.0 | 0.0 | 0.098 | 0.098 | spike_weibull_constrained | 208.2 |
| ecodistrict:Upper Fraser Trench|BL | gamma | gamma | 0.0 | 0.0 | 0.022 | 0.022 | mix_weibull_gamma | 234.6 |
| ecoprovince:Columbia Montane Cordillera|CW | mixture | spike_weibull | -271.7 | -273.2 | 0.217 | 0.036 | spike_weibull | -271.7 |
| ecodistrict:Upper Fraser Trench|SW | gamma | spike_weibull | -20.4 | -20.4 | 0.062 | 0.046 | spike_weibull | -20.4 |
| ecodistrict:Nechako Lowland|AT | mixture | mixture | 0.0 | 0.0 | 0.013 | 0.013 | mix_weibull_2 | 1,942.6 |
| ecodistrict:Nechako Lowland|BL | mix_weibull_2 | spike_weibull_constrained | -389.9 | -391.7 | 0.023 | 0.010 | spike_weibull_constrained | -389.9 |

The new families are fitted by a left-truncated EM that delegates each component M-step to `fit_censored_inventory` (Weibull) or the documented gamma moment update. Components are sorted by scale after every update. New Weibull mixtures are synthesis-eligible only when they converged. The legacy two-gamma mixture remains available as a fallback and carries a ten-unit AIC penalty when it did not converge; non-converged legacy selections are flagged in `distribution_fits.csv`. Small AIC gains are resolved in favour of the simpler model.

### 4c. Spike (first-bin) mixtures

- Spike families are attempted only when the first 2 cm bin carries more than **20%** of the expansion-factor tally, or the best single-component KS exceeds **0.15**. Attempted fits: **116** across four families (**58** constrained); constrained boundary rejects: **28**; selected fits: **14** (**14** unique `scope`/`fit_id` pairs).
- The spike is a point mass at the plot DBH limit that carries the first bin; the continuous Weibull/gamma tail is left-truncated at the first bin upper edge. The spike weight is the first-bin share (the disjoint-support multinomial MLE), counts as one AIC parameter, and is sampled uniformly inside the first bin so synthesis keeps a physical diameter. The spike never sets the volume scale.
- Constrained `spike_weibull_constrained`/`spike_gamma_constrained` tails are fitted by a bounded grouped MLE on the bins above the first bin, with shape >= 1 and scale >= 0.1 cm. A constrained fit whose tail parameters sit on any declared bound is reported as `boundary_reject` in `distribution_fits.csv` and is never selected.
- Unconstrained `spike_weibull`/`spike_gamma` rows are also synthesis-eligible when valid. Their tails can reach the two-stage scale floor with a Weibull shape below one, so the *untruncated* mean can be infinite; `sample_spike_mixture` always draws on the finite fitted support `(first_bin_upper, support_upper]`, and the tail must not be extrapolated beyond `support_upper`.

- CW high-KS strata: `ecozone:Montane Cordillera|CW` → `spike_weibull` (spike 0.657, KS 0.221 → 0.034, ΔAIC -795.2); `ecoprovince:Columbia Montane Cordillera|CW` → `spike_weibull` (spike 0.564, KS 0.217 → 0.036, ΔAIC -271.7).

- Spike selections whose raw AIC is more than two units worse than the previous model: `ecodistrict:Hart Ranges|SW` (ΔAIC 8.6, KS 0.046 → 0.023). These reflect the documented ten-unit penalty on a non-converged legacy two-gamma fallback and are kept for audit; the KS improved in each case.

#### CW before/after (unconstrained vs constrained tail)

| fit | first-bin share | unconstrained spike | constrained spike | selected |
|---|---:|---|---|---|
| ecozone:Montane Cordillera|CW | 0.6573 | spike_weibull · w=0.6573, a=0.1658, beta=0.0000 · AIC -99,709.1 · KS 0.0337 · ok | spike_gamma_constrained · w=0.6573, p=1.0000, beta=6.8038 · AIC -98,533.4 · KS 0.0936 · boundary_reject (p) | spike_weibull · AIC -99,709.1 · KS 0.0337 |
| ecoprovince:Columbia Montane Cordillera|CW | 0.5640 | spike_weibull · w=0.5640, a=0.1280, beta=0.0000 · AIC -30,252.6 · KS 0.0357 · ok | spike_weibull_constrained · w=0.5640, a=1.0000, beta=11.1794 · AIC -29,672.8 · KS 0.1082 · boundary_reject (a) | spike_weibull · AIC -30,252.6 · KS 0.0357 |

#### Constrained boundary rejections

| fit | family | spike weight | tail parameters | AIC | KS | at bound |
|---|---|---:|---|---:|---:|---|
| ecodistrict:Babine upland|AT | spike_gamma_constrained | 0.3673 | w=0.3673, p=1.0000, beta=16.3361 | -160,695.6 | 0.0809 | p |
| ecodistrict:Hart Ranges|BL | spike_weibull_constrained | 0.3047 | w=0.3047, a=1.0000, beta=7.1741 | -685,312.4 | 0.0633 | a |
| ecodistrict:Hart Ranges|BL | spike_gamma_constrained | 0.3047 | w=0.3047, p=1.0000, beta=7.1741 | -685,312.4 | 0.0633 | p |
| ecozone:Montane Cordillera|CW | spike_weibull_constrained | 0.6573 | w=0.6573, a=1.0000, beta=6.8038 | -98,533.4 | 0.0936 | a |
| ecozone:Montane Cordillera|CW | spike_gamma_constrained | 0.6573 | w=0.6573, p=1.0000, beta=6.8038 | -98,533.4 | 0.0936 | p |
| ecozone:Montane Cordillera|CW | spike_weibull_constrained | 0.6573 | w=0.6573, a=1.0000, beta=6.8038 | -98,533.4 | 0.0936 | a |
| ecozone:Montane Cordillera|CW | spike_gamma_constrained | 0.6573 | w=0.6573, p=1.0000, beta=6.8038 | -98,533.4 | 0.0936 | p |
| ecodistrict:Hart Ranges|HW | spike_weibull_constrained | 0.2100 | w=0.2100, a=1.0000, beta=6.3700 | -5,566.9 | 0.0718 | a |
| ecodistrict:Hart Ranges|HW | spike_gamma_constrained | 0.2100 | w=0.2100, p=1.0000, beta=6.3700 | -5,566.9 | 0.0718 | p |
| ecodistrict:Hart Ranges|SW | spike_weibull_constrained | 0.2186 | w=0.2186, a=1.0000, beta=8.0902 | -217,412.6 | 0.1140 | a |
| ecodistrict:Hart Ranges|SW | spike_gamma_constrained | 0.2186 | w=0.2186, p=1.0000, beta=8.0902 | -217,412.6 | 0.1140 | p |
| ecodistrict:McGregor Plateau|BL | spike_weibull_constrained | 0.2128 | w=0.2128, a=1.0000, beta=9.3576 | -2,302,946.9 | 0.0451 | a |
| ecodistrict:McGregor Plateau|BL | spike_gamma_constrained | 0.2128 | w=0.2128, p=1.0000, beta=9.3576 | -2,302,946.9 | 0.0451 | p |
| ecodistrict:McGregor Plateau|HW | spike_weibull_constrained | 0.2688 | w=0.2688, a=1.0000, beta=5.2691 | -133,791.2 | 0.0641 | a |
| ecodistrict:McGregor Plateau|HW | spike_gamma_constrained | 0.2688 | w=0.2688, p=1.0000, beta=5.2691 | -133,791.2 | 0.0641 | p |
| ecodistrict:McGregor Plateau|SW | spike_weibull_constrained | 0.2097 | w=0.2097, a=1.0000, beta=10.9915 | -2,574,864.6 | 0.0471 | a |
| ecodistrict:McGregor Plateau|SW | spike_gamma_constrained | 0.2097 | w=0.2097, p=1.0000, beta=10.9915 | -2,574,864.6 | 0.0471 | p |
| ecodistrict:Nazko Upland|BL | spike_weibull_constrained | 0.5966 | w=0.5966, a=1.0000, beta=5.3103 | -283,086.9 | 0.0245 | a |
| ecodistrict:Nazko Upland|BL | spike_gamma_constrained | 0.5966 | w=0.5966, p=1.0000, beta=5.3103 | -283,086.9 | 0.0245 | p |
| ecodistrict:Northern Columbia Mountains|SE | spike_gamma_constrained | 0.1324 | w=0.1324, p=1.0000, beta=21.6513 | -22,338.5 | 0.0673 | p |
| ecodistrict:Upper Fraser Trench|BL | spike_weibull_constrained | 0.4046 | w=0.4046, a=1.0000, beta=5.9337 | -142,678.7 | 0.0195 | a |
| ecodistrict:Upper Fraser Trench|BL | spike_gamma_constrained | 0.4046 | w=0.4046, p=1.0000, beta=5.9337 | -142,678.7 | 0.0195 | p |
| ecoprovince:Columbia Montane Cordillera|CW | spike_weibull_constrained | 0.5640 | w=0.5640, a=1.0000, beta=11.1794 | -29,672.8 | 0.1082 | a |
| ecoprovince:Columbia Montane Cordillera|CW | spike_gamma_constrained | 0.5640 | w=0.5640, p=1.0000, beta=11.1794 | -29,672.8 | 0.1082 | p |
| ecozone:Montane Cordillera|HW | spike_weibull_constrained | 0.2324 | w=0.2324, a=1.0000, beta=4.6740 | -314,491.9 | 0.0244 | a |
| ecozone:Montane Cordillera|HW | spike_gamma_constrained | 0.2324 | w=0.2324, p=1.0000, beta=4.6740 | -314,491.9 | 0.0244 | p |
| ecodistrict:Upper Fraser Trench|SW | spike_weibull_constrained | 0.2300 | w=0.2300, a=1.0000, beta=15.4147 | -29,930.0 | 0.0561 | a |
| ecodistrict:Upper Fraser Trench|SW | spike_gamma_constrained | 0.2300 | w=0.2300, p=1.0000, beta=15.4147 | -29,930.0 | 0.0561 | p |

| fit | previous | selected | spike weight | tail component | previous AIC | selected AIC | delta AIC | previous KS | selected KS |
|---|---|---|---:|---|---:|---:|---:|---:|---:|
| ecodistrict:Babine upland|SW | gamma | spike_gamma_constrained | 0.2181 | gamma | -981,244.1 | -981,397.4 | -153.3 | 0.021 | 0.015 |
| ecodistrict:Hart Ranges|BL | mix_weibull_gamma | spike_weibull | 0.3047 | weibull | -687,712.8 | -687,797.7 | -85.0 | 0.041 | 0.011 |
| ecozone:Montane Cordillera|CW | mixture | spike_weibull | 0.6573 | weibull | -98,914.0 | -99,709.1 | -795.2 | 0.221 | 0.034 |
| ecodistrict:Hart Ranges|SW | mixture | spike_weibull | 0.2186 | weibull | -220,182.4 | -220,173.8 | 8.6 | 0.046 | 0.023 |
| ecoregion:Fraser Basin|AC | mix_weibull_gamma | spike_weibull_constrained | 0.3217 | weibull | -47,138.8 | -47,155.5 | -16.7 | 0.041 | 0.022 |
| ecozone:Montane Cordillera|AC | mix_weibull_gamma | spike_gamma_constrained | 0.3053 | gamma | -50,034.8 | -50,051.5 | -16.7 | 0.040 | 0.025 |
| ecodistrict:Nazko Upland|BL | mix_weibull_gamma | spike_gamma | 0.5966 | gamma | -282,840.1 | -283,222.7 | -382.6 | 0.053 | 0.010 |
| ecodistrict:Nazko Upland|PL | mix_weibull_gamma | spike_gamma_constrained | 0.4211 | gamma | -1,596,337.3 | -1,597,608.9 | -1,271.5 | 0.043 | 0.010 |
| ecodistrict:Nazko Upland|SB | mix_weibull_2 | spike_weibull_constrained | 0.3478 | weibull | -23,915.9 | -23,997.7 | -81.7 | 0.053 | 0.056 |
| ecodistrict:Nazko Upland|SW | weibull | spike_gamma_constrained | 0.2627 | gamma | -698,861.7 | -699,031.8 | -170.2 | 0.021 | 0.007 |
| ecodistrict:Nechako Lowland|BL | mix_weibull_gamma | spike_weibull_constrained | 0.3082 | weibull | -2,797,722.1 | -2,799,274.6 | -1,552.5 | 0.029 | 0.011 |
| ecoprovince:Columbia Montane Cordillera|CW | mixture | spike_weibull | 0.5640 | weibull | -29,980.8 | -30,252.6 | -271.7 | 0.217 | 0.036 |
| ecodistrict:Upper Fraser Trench|SW | gamma | spike_weibull | 0.2300 | weibull | -29,931.7 | -29,952.1 | -20.4 | 0.062 | 0.046 |
| ecodistrict:Nechako Lowland|BL | mix_weibull_2 | spike_weibull_constrained | 0.3150 | weibull | -809,813.8 | -810,203.7 | -389.9 | 0.023 | 0.010 |

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

- Trees: **600**; scale factor: **0.812674**; achieved taper total: **311.600 m3**.
- TPH: **1,189.4**; basal area: **33.17 m2/ha**; QMD: **18.84 cm**.

| species | weight | trees | TPH | QMD cm | taper m3/ha |
|---|---:|---:|---:|---:|---:|
| AT | 0.116 | 70 | 138.3 | 19.60 | 31.9 |
| BL | 0.113 | 68 | 133.9 | 11.07 | 11.5 |
| EP | 0.022 | 13 | 26.5 | 21.68 | 9.3 |
| FD | 0.028 | 17 | 33.5 | 17.61 | 5.2 |
| PL | 0.102 | 61 | 121.2 | 25.43 | 63.2 |
| SB | 0.013 | 7 | 14.9 | 14.27 | 1.5 |
| SW | 0.606 | 364 | 721.1 | 18.57 | 189.0 |

## 7. Assortment matrix

- Logs: **515**; recovered: **253.16 m3**; residue: **58.44 m3**; taper total: **311.60 m3**.
- Residue: **21.40 ODT**; wood AGB proxy: **114.10 ODT**.

| product | volume m3 | share of taper |
|---|---:|---:|
| sawlog | 228.72 | 0.7340 |
| other | 24.11 | 0.0774 |
| pulpwood | 0.33 | 0.0010 |

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
- **no_negative_values**: PASS — checked matrix volume, residue, ODT, AGB proxy, and log counts
- **selected_mixtures_converged**: PASS — every selected Weibull mixture and spike model converged; a non-converged legacy two-gamma fallback may remain selected and is flagged in distribution_fits.csv
- **species_weights_sum**: PASS — sum=1.000000000000
- **target_volume**: PASS — achieved 311.600000 m3 vs target 311.600000 m3; scale 0.812673820
- **volume_conservation**: PASS — logs 253.156976 + residue 58.443024 = 311.600000 m3 vs taper 311.600000 m3; error 0 m3

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

