# National plot-to-RSYC-stratum coverage audit

**Generated:** 2026-11-16T06:26:53Z  
**Artifact version:** `0.1.0`  
**Code:** `workflows/national/assortments/national_coverage.py`  
**Inputs:** `data/derived/fvsca_calibration/v0/`; `data/raw/national/rsyc/RSYC_ecostrat.gpkg`; `data/raw/national/rsyc/RSYC_models.zip`  
**Runtime:** 454.5 s

## Scope

This is a coverage inventory, not a distribution fit. It maps every harmonized plot site with a usable coordinate to the RSYC ecodistrict hierarchy, maps source species codes to RSYC species or model groups, and counts independent site, plot, and tree support for every stratum × species cell. The thresholds are pre-registered:

- `direct_fit`: `n_trees >= 100` and `n_plots >= 5`.
- `pooled_fit`: not direct and either `30 <= n_trees < 100` or `2 <= n_plots < 5`.
- `no_data`: everything else.

`n_trees` is live trees with finite DBH in (0, 500] cm. `n_tree_rows` retains every tree record, including dead, missing, and non-positive DBH rows. `n_sites` and `n_plots` count independent support for live trees; `n_sites_all` and `n_plots_all` count any tree row. A plot is a physical plot unit: the FAIB plot prefix from `tree_id`, the MAGPlot / WFS ground-plot prefix from `visit_id`, and the QC PEP or NL FAL `site_id`. The pooled rule is applied literally, so a record with a single plot and 100+ trees, or 20 trees on six plots, remains `no_data` rather than being promoted on one dimension alone. `year_min`/`year_max`/`n_years` use the measurement year of live trees. `rsyc_strata_id` applies the single documented GeoPackage → model-table spelling correction (Betsiamiles Plateau → Betsiamites Plateau, ecodistrict 438) for RSYC model joins; `stratum_id` keeps the GeoPackage spelling.

## Mapping

Of **72,975** harmonized sites, **68,544** (93.9%) have a usable coordinate, and **67,477** (92.5%) fall inside an RSYC ecodistrict. The remaining sites are reported, not dropped: **3,404** have no coordinate, **1,027** carry the `-1/-1` sentinel, and **1,067** have a valid coordinate but fall outside the forested RSYC ecozones. The spatial join is a point-in-polygon operation in EPSG:3978; it took 0.66 s for the valid sites and produced 0 duplicate boundary matches.

### Sites and trees by source

| Source | Sites | Valid coords | Missing | Sentinel | Outside RSYC | Mapped | Remeasured | Plots | Tree rows | Live valid trees |
|---|---|---|---|---|---|---|---|---|---|---|
| faib_non_psp | 9,512 | 7,134 | 2,378 | 0 | 0 | 7,134 | 2,028 | 31,642 | 366,788 | 312,486 |
| faib_psp | 7,341 | 6,315 | 1,026 | 0 | 0 | 6,315 | 5,735 | 7,806 | 3,217,643 | 2,646,139 |
| magplot | 39,130 | 38,103 | 0 | 1,027 | 583 | 37,520 | 35,022 | 113,190 | 7,771,041 | 6,047,163 |
| magplot_wfs | 2,778 | 2,778 | 0 | 0 | 0 | 2,778 | 2,394 | 4,692 | 1,298,474 | 1,038,786 |
| nl_fal | 1,380 | 1,380 | 0 | 0 | 0 | 1,380 | 1,241 | 1,378 | 775,477 | 598,951 |
| qc_pep | 12,834 | 12,834 | 0 | 0 | 484 | 12,350 | 12,611 | 12,815 | 2,210,417 | 1,660,111 |

### Tree rows by mapping status

| Status | Sites | Plots | Tree rows | Live valid trees |
|---|---|---|---|---|
| mapped | 67,118 | 164,112 | 14,514,315 | 11,374,601 |
| outside_rsyc | 1,064 | 2,876 | 202,003 | 151,967 |
| missing_coordinates | 3,302 | 3,405 | 553,575 | 467,466 |
| sentinel_coordinates | 1,027 | 1,130 | 369,947 | 309,602 |
| out_of_bounds | 0 | 0 | 0 | 0 |

The mapped count covers **11,374,601** live valid trees; the excluded strata retain **929,035** live valid trees that cannot enter an RSYC-stratified fit without a coordinate repair or a non-RSYC pooling decision.

## Species crosswalk

The audit observed **355** distinct source species codes. **113** map directly to an RSYC scientific species (14,534,696 tree rows), **2** use a documented nearest-taxon alias (BC black cottonwood → `POPU.BAL`), **202** map only to the RSYC `coniferous`/`broadleaf` model groups (635,656 tree rows), and **38** map to `generic` (453,809 tree rows). **0** codes are unmapped.

| Source | Codes | Exact species | Alias | Group fallback | Generic | Unmapped | Tree rows | Exact-species rows | Unresolved rows |
|---|---|---|---|---|---|---|---|---|---|
| magplot | 140 | 32 | 0 | 107 | 1 | 0 | 7,771,041 | 7,314,851 | 456,190 |
| faib_psp | 45 | 17 | 1 | 11 | 16 | 0 | 3,217,643 | 3,127,747 | 78,660 |
| qc_pep | 65 | 17 | 0 | 45 | 3 | 0 | 2,210,417 | 1,758,032 | 452,385 |
| magplot_wfs | 48 | 20 | 0 | 27 | 1 | 0 | 1,298,474 | 1,212,036 | 86,438 |
| nl_fal | 15 | 10 | 0 | 3 | 2 | 0 | 775,477 | 768,692 | 6,785 |
| faib_non_psp | 42 | 17 | 1 | 9 | 15 | 0 | 366,788 | 353,338 | 9,007 |

**240** codes (1,089,465 tree rows; 376,636 live valid trees) do not resolve to an RSYC scientific species. They are retained at the functional-group or generic level rather than discarded. The largest unresolved codes by live support are:

| Source | Code | Source group | RSYC destination | Basis | Tree rows | Live trees |
|---|---|---|---|---|---|---|
| magplot | FAGU.GRA.NA | deciduous | broadleaf | functional_group | 41,370 | 25,477 |
| magplot | SALI.SPP.NA | deciduous | broadleaf | functional_group | 39,010 | 24,066 |
| magplot | PRUN.PEN.NA | deciduous | broadleaf | functional_group | 38,503 | 18,325 |
| faib_psp | W | deciduous | broadleaf | functional_group | 24,052 | 18,276 |
| qc_pep | HEG | deciduous | broadleaf | functional_group | 19,991 | 17,984 |
| magplot | PINU.MON.NA | conifer | coniferous | functional_group | 25,668 | 15,738 |
| faib_psp | PW | conifer | coniferous | functional_group | 25,294 | 14,660 |
| qc_pep | PRP | deciduous | broadleaf | functional_group | 16,128 | 13,478 |
| magplot | TSUG.CAN.NA | conifer | coniferous | functional_group | 15,303 | 12,518 |
| magplot | ALNU.SPP.NA | deciduous | broadleaf | functional_group | 13,932 | 12,458 |
| magplot | BETU.POP.NA | deciduous | broadleaf | functional_group | 14,265 | 11,482 |
| qc_pep | PRU | conifer | coniferous | functional_group | 11,838 | 11,191 |
| magplot | UNKN.SPP.NA | unknown | generic | generic | 18,770 | 9,256 |
| magplot | CHAM.NOO.NA | conifer | coniferous | functional_group | 8,754 | 7,997 |
| magplot | ACER.PEN.NA | deciduous | broadleaf | functional_group | 18,250 | 7,934 |

The QC PEP missing species code accounts for **359,645** tree rows but **0** live valid trees; it is a harmonization gap in the source, not a fitting-support gap. The next largest unresolved blocks are genuine species that lack an RSYC scientific code (for example `ACER.SPI`, `ALNU.RUG`, `FAGU.GRA`, and `PINU.MON`).

## Coverage by level

Counts are stratum × species rows. `All rows` includes RSYC strata with no plots at all; `In strata with sites` restricts to strata that contain at least one mapped site, which separates structural gaps from species gaps.

| Level | Strata | With sites | Rows | Direct | Pooled | No data | Direct (with sites) | Pooled (with sites) | No data (with sites) |
|---|---|---|---|---|---|---|---|---|---|
| national | 1 | 1 | 35 | 35 | 0 | 0 | 35 | 0 | 0 |
| ecodistrict | 672 | 301 | 23,520 | 2,001 | 768 | 20,751 | 2,001 | 768 | 7,766 |
| ecoregion | 138 | 91 | 4,830 | 765 | 218 | 3,847 | 765 | 218 | 2,202 |
| ecoprovince | 36 | 27 | 1,260 | 321 | 46 | 893 | 321 | 46 | 578 |
| ecozone | 12 | 10 | 420 | 142 | 16 | 262 | 142 | 16 | 192 |

At ecodistrict level, **2,001** of **23,520** stratum × species cells are direct fits (8.5%), **768** are pooled (3.3%), and **20,751** are no_data (88.2%). Restricting to the **301** ecodistricts that contain at least one site leaves **2,001** direct (19.0%), **768** pooled (7.3%), and **7,766** no_data cells (73.7%). The same pattern at coarser levels is 765/218/3,847 at ecoregion, 321/46/893 at ecoprovince, and 142/16/262 at ecozone.

### RSYC volume-model availability

The catalogue check uses national-scale, publishable volume models only. It shows where the inventory and the published curve library overlap, not whether a published curve is accurate for local use.

| Level | Direct | Direct with model | Direct without model | No data with model |
|---|---|---|---|---|
| ecodistrict | 2,001 | 1,280 | 721 | 3,072 |
| ecoregion | 765 | 498 | 267 | 521 |
| ecoprovince | 321 | 217 | 104 | 111 |
| ecozone | 142 | 108 | 34 | 30 |

## Province and source coverage

| Province | Mapped sites | Remeasured | Ecodistricts | Plots | Tree rows | Live trees | Direct | Pooled | No data (data-bearing) | Sources |
|---|---|---|---|---|---|---|---|---|---|---|
| BC | 28,840 | 17,936 | 105 | 74,304 | 6,458,100 | 5,433,478 | 773 | 276 | 2,521 | faib_non_psp;faib_psp;magplot |
| SK | 2,219 | 1,822 | 50 | 4,286 | 1,022,625 | 781,996 | 197 | 85 | 1,468 | magplot;magplot_wfs |
| MB | 2 | 2 | 1 | 4 | 43 | 38 | 0 | 0 | 0 | magplot |
| QC | 24,758 | 24,512 | 55 | 66,410 | 4,637,424 | 3,151,043 | 455 | 136 | 1,194 | magplot;qc_pep |
| NB | 7,609 | 6,948 | 27 | 14,471 | 564,150 | 495,770 | 349 | 99 | 462 | magplot |
| PE | 691 | 684 | 5 | 687 | 275,204 | 255,076 | 50 | 16 | 109 | magplot_wfs |
| NL | 2,769 | 2,457 | 33 | 2,813 | 1,435,635 | 1,153,200 | 116 | 77 | 927 | magplot;magplot_wfs;nl_fal |
| YT | 327 | 322 | 25 | 642 | 106,663 | 92,189 | 37 | 48 | 790 | magplot |
| NT | 262 | 233 | 12 | 495 | 14,471 | 11,811 | 24 | 31 | 295 | magplot |

Province class counts cover data-bearing districts only; the **12,985** no-data cells in the **371** districts with no sites are not assigned to a province.

Provinces with no mapped site: **AB, ON, NS, NU**. Manitoba is present only as **2** MAGPlot sites. The national extract is therefore concentrated in BC, QC, Atlantic Canada, and parts of the boreal and northern territories; it is not a representative national plot network.

## DBH limits

DBH statistics are unweighted over live, positive-DBH trees. `share < 5 cm` is the fraction of live trees below a common merchantability cut-off; it shows how much of the support sits in the small-tree tail that a left-truncated fit must handle explicitly. Across sources the share ranges from 0.0% to 30.4%. QC PEP has a 7.7 cm minimum and no trees below 5 cm; NL FAL has 30.4% of its live trees below 5 cm.

| Source | Live trees | Min cm | P05 cm | Median cm | P95 cm | Max cm | % < 5 cm |
|---|---|---|---|---|---|---|---|
| faib_non_psp | 312,486 | 0.10 | 5.00 | 15.10 | 58.20 | 450.00 | 4.9 |
| faib_psp | 2,646,139 | 0.50 | 4.40 | 13.00 | 39.40 | 401.70 | 8.2 |
| magplot | 6,047,163 | 0.10 | 2.70 | 11.90 | 34.40 | 450.00 | 11.6 |
| magplot_wfs | 1,038,786 | 0.10 | 2.30 | 11.60 | 26.20 | 133.20 | 15.3 |
| nl_fal | 598,951 | 0.02 | 1.30 | 8.60 | 19.70 | 85.00 | 30.4 |
| qc_pep | 1,660,111 | 7.70 | 9.40 | 13.60 | 30.10 | 108.90 | 0.0 |

## Data gaps

- **371 of 672** RSYC ecodistricts contain no mapped site.
- **2 of 12** ecozones contain no mapped site: Taiga Cordillera, Taiga Shield West.
- **34** of the **301** data-bearing ecodistricts have no species with a direct fit.
- Species with no direct fit in any ecodistrict: **none**.

### Largest species gaps at ecodistrict level

| Species | Districts with data | Direct | Pooled | No data in data-bearing districts | No data (all districts) | Live trees |
|---|---|---|---|---|---|---|
| POPU.BAL | 175 | 67 | 73 | 35 | 532 | 50,674 |
| LARI.LAR | 155 | 55 | 68 | 32 | 549 | 42,046 |
| generic | 138 | 59 | 53 | 26 | 560 | 28,856 |
| coniferous | 115 | 51 | 38 | 26 | 583 | 73,377 |
| broadleaf | 195 | 124 | 45 | 26 | 503 | 233,053 |
| BETU.PAP | 232 | 172 | 38 | 22 | 462 | 560,362 |
| PICE.GLA | 262 | 189 | 55 | 18 | 428 | 846,048 |
| POPU.TRE | 229 | 155 | 58 | 16 | 459 | 660,173 |
| ACER.RUB | 96 | 63 | 19 | 14 | 590 | 222,445 |
| PICE.MAR | 212 | 174 | 24 | 14 | 474 | 1,736,172 |

### Data-bearing ecodistricts with the largest species gaps

| Ecodistrict | Ecozone | Species with data | Direct | Pooled | No data in data-bearing species | No data (all species) | Sites | Live trees |
|---|---|---|---|---|---|---|---|---|
| Bulkley | Montane Cordillera | 14 | 6 | 2 | 6 | 27 | 74 | 6,573 |
| Petitot Plain | Taiga Plains | 13 | 5 | 3 | 5 | 27 | 14 | 3,958 |
| Western Chilcotin Upland | Montane Cordillera | 8 | 2 | 1 | 5 | 32 | 195 | 14,767 |
| Saskatchewan Delta | Boreal Plains | 6 | 0 | 1 | 5 | 34 | 2 | 342 |
| Boundary Ranges | Pacific Maritime | 5 | 0 | 0 | 5 | 35 | 1 | 274 |
| Bald Mountains | Atlantic Maritime | 19 | 14 | 1 | 4 | 20 | 498 | 41,588 |
| Plaster Rock | Atlantic Maritime | 18 | 11 | 3 | 4 | 21 | 53 | 3,560 |
| Southern Pacific Ranges | Pacific Maritime | 17 | 11 | 2 | 4 | 22 | 347 | 86,425 |
| Etdyuk Lake | Montane Cordillera | 15 | 4 | 7 | 4 | 24 | 175 | 43,856 |
| Nechako Lowland | Montane Cordillera | 15 | 11 | 0 | 4 | 24 | 1,073 | 239,577 |

## What can be fit now

- **National audit rollup:** all **35** species or model groups have at least 100 live trees and 5 plots. This is not an RSYC stratum and should not be used as a replacement for stratified fits.
- **Ecodistrict:** 2,001 direct stratum × species cells; these are the only cells that meet the pre-registered direct threshold without pooling.
- **Ecoregion:** 765 direct cells; **ecoprovince:** 321; **ecozone:** 142.
- **RSYC overlap:** 1,280 direct ecodistrict cells also have a national RSYC volume model; 721 have inventory support but no national RSYC species curve, so they are calibration opportunities rather than published-curve replacements.

## What needs pooling

- **768** ecodistrict cells are pooled (3.3% of all cells; 7.3% of data-bearing cells).
- Pooling should follow the nesting ecodistrict → ecoregion → ecoprovince → ecozone, but the coarser level is not automatically better: ecozone still has **262** no_data cells and **16** pooled cells.
- The largest pooled species buckets at ecodistrict level are `POPU.BAL` (73), `LARI.LAR` (68), `POPU.TRE` (58), `PICE.GLA` (55), `generic` (53).
- The largest pooled count is at ecodistrict level (**768** cells), which is where the hierarchical pooling rule has the most work to do.

## What is missing

- **Alberta, Ontario, Nova Scotia, and Nunavut have no plots** in the harmonized extract. Manitoba has two MAGPlot sites. The national coverage claim is therefore conditional on future AB/ON/NS/NU data.
- **371** ecodistricts have no plots, including all of Nova Scotia and large parts of the Atlantic Maritime, Boreal Shield, and Taiga ecozones.
- **240** source codes (1,089,465 tree rows; 376,636 live valid trees) are not resolved to an RSYC scientific species. Species-specific fits for those live trees are not defensible; they can support functional-group fits only. The QC PEP missing code is a source harmonization gap, not live support.
- The MAGPlot `approx_10km` coordinate class is adequate for ecodistrict joins but not for tile-level or fine-scale spatial claims.

## Implications for the RSYC-stratified pipeline

1. **Use the hierarchy as a fallback ladder, not a single key.** Direct fits exist for only a minority of ecodistrict × species cells. A pipeline that refuses to pool will produce almost no national species coverage; a pipeline that pools blindly will mix ecologically different strata. The coverage table supplies the explicit ladder and the counts needed to justify each step.
2. **Keep species and functional-group fits separate.** The crosswalk resolves most tree rows to species, but a material tail is only `coniferous`, `broadleaf`, or `generic`. A group fit is not a species fit and should not be relabelled as one downstream.
3. **Treat RSYC curves as a prior, not a substitute.** 3,072 ecodistrict cells are `no_data` yet have a national RSYC volume model. They are the natural gap-fill surface, but the RSYC validation bias and RMSE ranges must travel with the curve.
4. **Carry DBH limits explicitly.** The share of live trees below 5 cm ranges from 0.0% to 30.4% across sources. Unweighted fits that ignore the small-tree tail will not be comparable across sources, and the QC PEP minimum of 7.7 cm means QC PEP cannot contribute to the small-tree tail at all.
5. **Do not call this national yet.** BC and QC dominate the support; AB, ON, NS, and NU are absent. Any national supply result must carry a coverage flag per stratum and species, and must fail closed where the flag is `no_data`.

## Artifacts

- `coverage.csv`: one row per level × stratum × species with counts, DBH limits, year range, province/source provenance, class, and RSYC model availability.
- `coverage_summary.json`: machine-readable mapping, level, province, source, DBH, and gap summaries.
- `species_crosswalk_national.csv`: every observed source species code and its RSYC destination, basis, and note.
- `coverage_heatmap.png`: 200 dpi heatmap of ecodistrict support classes.
- `manifest.json`: input/output hashes, code commit, and runtime.

## Limitations

- The join is a point-in-polygon assignment. A site on a boundary or with an approximate coordinate can be assigned to the wrong ecodistrict; the audit reports the unmatched count but does not impute a nearest stratum.
- `n_plots` depends on the physical-plot derivation. FAIB plot prefixes come from `tree_id`; if a source changes its tree-id convention, the plot count will change.
- The coverage class is a support threshold, not a goodness-of-fit or a representativeness statement. A direct cell can still fail a distribution fit for reasons outside this inventory.
- The species crosswalk uses a nearest-taxon alias for BC black cottonwood and functional-group fallbacks elsewhere. It is not a taxonomic revision.

_Generated by `workflows/national/assortments/national_coverage.py` at 2026-11-16T06:26:53Z._
