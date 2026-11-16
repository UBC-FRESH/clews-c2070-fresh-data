# National hierarchical DBH/height fit

**Generated:** 2026-11-16T08:09:48Z<br>
**Target level:** `ecoregion`<br>
**Support levels:** `national`, `ecozone`, `ecoprovince`, `ecoregion`<br>
**Artifact version:** `0.1.0`<br>
**Code:** `workflows/national/assortments/national_fit.py`<br>
**Runtime:** 90.0 s (prep 1.0 s, fit 58.6 s)<br>
**Timebox:** 780 s; exhausted: `false`

## Scope and method

This pass fits DBH distributions and height–diameter models for every pre-registered coverage cell at the support levels shown above.  The coverage audit is the sampling frame: its `direct_fit` and `pooled_fit` classes are the only cells that receive a local fit.  `no_data` cells borrow the nearest ancestor shape or the national species shape; they are never labelled as local fits.

- **Coverage thresholds:** direct `n_trees >= 100` and `n_plots >= 5`; pooled otherwise when `30 <= n_trees < 100` or `2 <= n_plots < 5`.
- **Candidate set:** single Weibull and gamma; `mix_weibull_2`; `mix_weibull_gamma`; and the constrained spike families when the existing first-bin/KS gate fires.  The national pass deliberately does not attempt the legacy two-gamma fallback, generalized-beta diagnostics, three-component Weibull, or unconstrained spikes; those remain available to other callers.  The finite mixtures use one deterministic start and 80 EM iterations for this pass.  Selection follows the existing two-AIC-unit rule and excludes non-converged new mixtures.
- **Local support floor:** the candidate attempt uses the pre-limit support (direct at least `30` trees and `5` plots; pooled at least `10` trees and `2` plots).  `fit_n_trees`/`fit_n_plots` report the post-modal-limit support actually fitted; any local row below 30 trees or five plots is labelled `low_support`.
- **DBH limits:** the modal per-source limit is used inside each cell. Trees from other protocol classes are excluded and the count is recorded in `limit_excluded_trees`.  Source floors: `faib_psp` 2 cm, `faib_non_psp` 4 cm, `magplot` 2 cm, `magplot_wfs` 2 cm, `nl_fal` 1 cm, `qc_pep` 9 cm.
- **Height model:** `H = 1.3 + exp(a) * DBH^b`, fitted by log-linear least squares with at least `30` height observations.  Height models use the same parent/national fallback as the shape and are labelled separately.
- **Scale prior:** the publishable RSYC volume and AGB curve is evaluated at age `100`.  The selected model id and strata level are recorded; a missing or out-of-range prior is flagged, never silently extrapolated.
- **Resume/timebox:** each direct/pooled cell writes a JSON partial under `cells/<level>/`.  A run that exhausts the timebox rebuilds the CSV/report from completed partials and lists the exact remaining cells in `remaining_cells.csv`.

## Coverage frame

| Level | Coverage direct | Coverage pooled | Coverage no_data |
|---|---|---|---|
| national | 35 | 0 | 0 |
| ecozone | 142 | 16 | 262 |
| ecoprovince | 321 | 46 | 893 |
| ecoregion | 765 | 218 | 3847 |

## Evidence counts

| Level | Cells | direct_fit | pooled_fit | pooled_parent | species_national | no_fit |
|---|---|---|---|---|---|---|
| national | 35 | 35 | 0 | 0 | 0 | 0 |
| ecozone | 420 | 141 | 10 | 0 | 262 | 7 |
| ecoprovince | 1260 | 319 | 29 | 132 | 761 | 19 |
| ecoregion | 4830 | 757 | 154 | 1142 | 2705 | 72 |

`direct_fit`/`pooled_fit` are local fits.  `pooled_parent` is a borrowed ancestor shape.  `species_national` is the national species shape.  `no_fit` is an explicit gap.

## Top direct fits

| Level | Stratum | Species | Distribution | Trees | Plots | KS | AIC |
|---|---|---|---|---|---|---|---|
| national | Canada | PINU.CON | gamma | 1051630 | 14025 | 0.012 | -723127810.8 |
| national | Canada | PICE.MAR | weibull | 1038842 | 15451 | 0.049 | -952970998.5 |
| national | Canada | PSEU.MEN | gamma | 993212 | 12636 | 0.064 | -475380207.0 |
| national | Canada | TSUG.HET | gamma | 974033 | 11286 | 0.119 | -619475223.9 |
| ecozone | Montane Cordillera | PINU.CON | gamma | 933171 | 12265 | 0.012 | -608068803.8 |
| national | Canada | ABIE.BAL | spike_weibull_constrained | 908485 | 21121 | 0.023 | -1239947262.8 |
| ecozone | Pacific Maritime | TSUG.HET | gamma | 793795 | 7830 | 0.107 | -468650251.9 |
| ecozone | Montane Cordillera | PSEU.MEN | mix_weibull_gamma | 776830 | 9833 | 0.051 | -382514644.7 |
| national | Canada | PICE.GLA | gamma | 749527 | 23334 | 0.017 | -489478648.7 |
| ecoprovince | Pacific Maritime/Southern Coastal Mountains | TSUG.HET | gamma | 633979 | 6745 | 0.122 | -386698018.5 |
| ecozone | Boreal Shield East | PICE.MAR | weibull | 610934 | 7710 | 0.047 | -609545988.0 |
| ecozone | Boreal Shield East | ABIE.BAL | spike_weibull_constrained | 603736 | 9181 | 0.025 | -886347308.5 |

## Top pooled fits

| Level | Stratum | Species | Distribution | Trees | Plots | KS |
|---|---|---|---|---|---|---|
| ecoregion | Boreal Cordillera/Southern Boreal Cordillera/Yukon-Stikine Highlands | PINU.CON | mix_weibull_gamma | 612 | 3 | 0.017 |
| ecoregion | Boreal Shield East/Newfoundland/Central Newfoundland | PINU.BAN | mix_weibull_gamma | 421 | 2 | 0.018 |
| ecoprovince | Boreal Shield East/Newfoundland | PINU.BAN | mix_weibull_gamma | 421 | 2 | 0.018 |
| ecoregion | Montane Cordillera/Columbia Montane Cordillera/Northern Continental Divide | PINU.PON | weibull | 420 | 4 | 0.041 |
| ecoregion | Taiga Plains/Hay-Slave Lowlands/Northern Alberta Uplands | PINU.BAN | gamma | 241 | 4 | 0.040 |
| ecoregion | Boreal Cordillera/Northern Boreal Cordillera/Hyland Highland | BETU.PAP | mix_weibull_gamma | 188 | 3 | 0.015 |
| ecoregion | Taiga Shield East/Labrador Uplands/Kingarutuk-Fraser River | ABIE.BAL | mix_weibull_gamma | 173 | 2 | 0.046 |
| ecoregion | Boreal Plains/Eastern Boreal Plains/Interlake Plain | POPU.TRE | spike_weibull_constrained | 150 | 4 | 0.054 |
| ecoregion | Boreal Shield East/Eastern Boreal Shield/Lake Melville | PINU.BAN | weibull | 138 | 2 | 0.014 |
| ecoregion | Atlantic Maritime/Northumberland Lowlands/Maritime Lowlands | PICE.ABI | spike_weibull_constrained | 138 | 4 | 0.080 |
| ecoregion | Taiga Plains/Hay-Slave Lowlands/Hay River Lowland | ABIE.BAL | mix_weibull_gamma | 127 | 4 | 0.036 |
| ecoregion | Boreal Cordillera/Wrangel Mountains/St.Elias Mountains | PICE.GLA | mix_weibull_gamma | 107 | 4 | 0.039 |

## Validation

- Support-level direct fits: 1252; median KS 0.040; p90 KS 0.138; 67 flagged with KS > 0.20; 10 flagged low_support.
- Support-level pooled fits: 193; 110 flagged low_support.
- Borrowed shapes: 1274 parent and 3728 national species.
- Explicit gaps: 98 cells labelled `no_fit`.
- RSYC prior: 6510/6545 rows have an RSYC prior; 1755 are exact-species; 0 fall outside the published age range.
- No-data RSYC priors: {'group': 3967, 'species': 667, 'parent_group': 274, 'parent_species': 94}; 0 no-data cells have no prior.
- Height models: 1337 local, 5208 borrowed, 0 missing height models; median local RMSE 2.765 m.

## Caveats

- A borrowed shape is a scale-compatible stand shape, not local evidence.  The `fit_scope` and `borrowed_from_*` columns are the authoritative provenance.
- The national plot frame is uneven.  Alberta, Ontario, Nova Scotia, and Nunavut have no mapped plots in the coverage audit; Manitoba has two sites.  Coarse-level fits are dominated by BC, QC, NB, NL, SK, PE, YT, and NT support.
- Pooled cells are fitted on small local samples by design.  They are flagged by `fit_quality_flag`/low support and should not be read as equivalent to direct cells.  A pooled cell with fewer than ten trees or fewer than three populated DBH bins remains `no_fit`; the coverage class is a sampling-support label, not a guarantee that a distribution can be estimated.
- The harmonized tree table does not carry the source `DBH_LIMIT_TAG` for every plot.  The per-source floor is a documented approximation; mixed-protocol cells lose the non-modal protocol trees.
- NL FAL publishes no expansion factor, so its trees carry unit weights.  The shape likelihood is invariant to a constant weight, but NL FAL cannot contribute a calibrated TPH scale from this table.
- Height models are unweighted least squares on the available height measurements.  Sources with sparse height tallies borrow a parent or national height model; the `n_height_obs` column records local availability.
- The RSYC curves are published ecological-stratum curves, not local re-fits.  The reference-age value is a scale prior; it does not override the fitted shape or imply that the stand is 100 years old.

## Remaining cells

0 direct/pooled cells are pending (resumable), and 98 are local fit failures (not resumable without a data or support change).  The exact list is in `remaining_cells.csv`; the first rows are:

| Level | Stratum | Species | Class | Trees | Plots | Reason | Resumable |
|---|---|---|---|---|---|---|---|
| ecoregion | Atlantic Maritime/Fundy Uplands/Fundy Coast | GENERIC | direct_fit | 125 | 19 | local_fit_failed | no |
| ecoregion | Atlantic Maritime/Fundy Uplands/Saint John River Valley | PICE.ABI | pooled_fit | 31 | 1 | local_fit_failed | no |
| ecoregion | Atlantic Maritime/Fundy Uplands/Southern New Brunswick Uplands | PICE.ABI | pooled_fit | 8 | 2 | local_fit_failed | no |
| ecoregion | Atlantic Maritime/Northumberland Lowlands/Prince Edward Island | GENERIC | pooled_fit | 9 | 4 | local_fit_failed | no |
| ecoregion | Boreal Cordillera/Northern Boreal Cordillera/Hyland Highland | ABIE.LAS | pooled_fit | 78 | 1 | local_fit_failed | no |
| ecoregion | Boreal Cordillera/Northern Boreal Cordillera/Pelly Mountains | BROADLEAF | pooled_fit | 9 | 3 | local_fit_failed | no |
| ecoregion | Boreal Cordillera/Northern Boreal Cordillera/Yukon Plateau-Central | GENERIC | pooled_fit | 47 | 3 | local_fit_failed | no |
| ecoregion | Boreal Cordillera/Northern Boreal Cordillera/Yukon Plateau-North | PINU.CON | pooled_fit | 9 | 2 | local_fit_failed | no |
| ecoregion | Boreal Cordillera/Northern Boreal Cordillera/Yukon Southern Lakes | BETU.PAP | pooled_fit | 7 | 2 | local_fit_failed | no |
| ecoregion | Boreal Cordillera/Southern Boreal Cordillera/Boreal Mountains and Plateaus | GENERIC | pooled_fit | 7 | 2 | local_fit_failed | no |
| ecoregion | Boreal Cordillera/Southern Boreal Cordillera/Yukon-Stikine Highlands | ABIE.LAS | direct_fit | 146 | 5 | local_fit_failed | no |
| ecoregion | Boreal Plains/Boreal Foothills/Clear Hills Upland | ALNU.RUB | pooled_fit | 9 | 4 | local_fit_failed | no |
| ecoregion | Boreal Plains/Boreal Foothills/Western Alberta Upland | ALNU.RUB | pooled_fit | 40 | 3 | local_fit_failed | no |
| ecoregion | Boreal Plains/Central Boreal Plains/Western Boreal | PICE.GLA | pooled_fit | 2 | 2 | local_fit_failed | no |
| ecoregion | Boreal Plains/Central Boreal Plains/Western Boreal | POPU.BAL | pooled_fit | 9 | 4 | local_fit_failed | no |
| ecoregion | Boreal Plains/Eastern Boreal Plains/Interlake Plain | POPU.BAL | pooled_fit | 9 | 3 | local_fit_failed | no |
| ecoregion | Boreal Shield East/Eastern Boreal Shield/Anticosti Island | BROADLEAF | pooled_fit | 4 | 2 | local_fit_failed | no |
| ecoregion | Boreal Shield East/Eastern Boreal Shield/Mecatina Plateau | PICE.RUB | pooled_fit | 2 | 2 | local_fit_failed | no |
| ecoregion | Boreal Shield East/Mid-Boreal Shield/Abitibi Plains | PINU.RES | pooled_fit | 4 | 2 | local_fit_failed | no |
| ecoregion | Boreal Shield East/Mid-Boreal Shield/Abitibi Plains | POPU.GRA | pooled_fit | 7 | 3 | local_fit_failed | no |

## Outputs

- `national_distribution_parameters.csv` — one row per support-level cell.
- `national_height_models.csv` — height model per support-level cell.
- `national_evidence_summary.json` — counts, runtime, inputs, validation.
- `evidence_map.png` — evidence tiers at the target level.
- `remaining_cells.csv` — resumable work list.
- `manifest.json` — input/output hashes and code/data commit ids.
