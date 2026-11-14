# BC FAIB Non-PSP Compilation — Table Inventory and Profiling — 2026-11-14

Source: `non_psp/` tables from the anonymous BC FAIB FTP publication tree,
retrieved 2026-11-14. Compilation files are dated 2026-04-20/21; the data
dictionary is `non_PSP_data_dictionary_2026Apr20.xlsx`. All CSVs are archived
gzipped; row counts below were computed from the decompressed files.

## 1. Table inventory — province-wide

| Archived file | Rows | Columns | Key columns | Notes |
|---------------|-----:|--------:|-------------|-------|
| `publish_province/faib_header.csv.gz` | 9,512 | 24 | `SITE_IDENTIFIER` | One row per site. TSA/TFL, BEC zone/subzone/variant, ownership, coordinates, establishment type, grid base/size. |
| `publish_province/faib_plot_header.csv.gz` | 37,547 | 20 | `SITE_IDENTIFIER`, `VISIT_NUMBER`, `PLOT` | One row per plot within a visit. Plot area, shape, radius/width/length, BAF, slope/aspect/elevation. |
| `publish_province/faib_sample_byvisit.csv.gz` | 11,951 | 32 | `CLSTR_ID` | One row per site visit. Measurement date/year, period, plot count, sample type, purpose, visit type, DBH limits. |
| `publish_province/faib_compiled_smries.csv.gz` | 59,755 | 30 | `CLSTR_ID`, `UTIL` | Stand-level summary per visit at five utilization limits (2, 4, 7.5, 12.5, 17.5 cm). |
| `publish_province/faib_compiled_smries_wk.csv.gz` | 1,115 | 30 | `CLSTR_ID`, `UTIL` | Walkthrough stand summary subset. |
| `publish_province/faib_compiled_smeries_ht.csv.gz` | 11,951 | 10 | `CLSTR_ID` | Visit-level height summary: Lorey, mean, and all-live heights. |
| `publish_province/faib_compiled_spcsmries.csv.gz` | 148,840 | 33 | `CLSTR_ID`, `UTIL`, `SPECIES` | Species-level summary per visit and utilization limit. |
| `publish_province/faib_compiled_spcsmries_wk.csv.gz` | 2,855 | 33 | `CLSTR_ID`, `UTIL`, `SPECIES` | Walkthrough species summary subset. |
| `publish_province/faib_compiled_spcsmries_siteage.csv.gz` | 19,843 | 11 | `CLSTR_ID`, `SPECIES` | Species-by-visit site index, BH age, total age, top height, and sample counts. |
| `publish_province/faib_smltree_smries_cl.csv.gz` | 9,617 | 16 | `SITE_IDENTIFIER`, `VISIT_NUMBER` | Small-tree summary by count/plot. |
| `publish_province/faib_smltree_smries_clsp.csv.gz` | 15,790 | 13 | `SITE_IDENTIFIER`, `VISIT_NUMBER`, `SPECIES` | Small-tree summary by species. |
| `publish_province/faib_tree_detail.csv.gz` | 367,096 | 52 | `CLSTR_ID`, `PLOT`, `TREE_NO` | Tree measurement record. Species, DBH, height, live/dead, damage, age, site index, expansion, volumes. |

The `_wk` tables are walkthrough subsets of the corresponding full summary
tables. Use the non-`_wk` tables unless a walkthrough-specific analysis is
intended.

## 2. Per-TSA publication tree

`publish_by_tsa/` contains 37 directories, each with the same 12 CSV table
names as `publish_province/`. Directory names preserve upstream spelling and
spaces (for example `100 Mile House TSA`, `Prince George TSA`).

The per-TSA files are exact subsets of the province-wide tables:

| Check | Per-TSA total | Province-wide |
|-------|--------------:|--------------:|
| Site rows | 9,512 | 9,512 |
| Visit rows | 11,951 | 11,951 |
| Tree rows | 367,096 | 367,096 |
| Union of site identifiers | 9,512 | 9,512 |
| Province-only sites | 0 | — |
| TSA-only sites | 0 | — |

Do not sum `publish_province/` and `publish_by_tsa/`; that would double-count
every row. The per-TSA tree is retained because it is the upstream publication
partition and preserves the FAIB delivery structure.

## 3. Site, visit, and tree counts

| Measure | Value |
|---------|------:|
| Distinct sites | 9,512 |
| Distinct visits (`CLSTR_ID`) | 11,951 |
| Sites with one visit | 7,484 (78.7%) |
| Remeasured sites (>1 visit) | 2,028 (21.3%) |
| Maximum visits per site | 5 |
| Tree measurement rows | 367,096 |
| Unique trees | 275,264 |
| Remeasured trees (>1 visit) | 76,667 (27.9% of unique trees) |
| Maximum measurements per tree | 4 |
| Mean measurements per tree | 1.33 |
| Live tree rows | 321,421 |
| Dead tree rows | 45,364 |
| Missing live/dead status | 311 |
| Measurement years | 1995–2025 |

### Visits per site

| Visits | Sites |
|-------:|-----:|
| 1 | 7,484 |
| 2 | 1,642 |
| 3 | 363 |
| 4 | 21 |
| 5 | 2 |

### Establishment type

| Establishment type | Sites | Visits | Remeasured sites | Year range |
|--------------------|------:|-------:|-----------------:|------------|
| VRI | 6,684 | 7,200 | 497 | 1995–2022 |
| YSM | 1,129 | 2,205 | 832 | 2005–2025 |
| CMI | 995 | 1,506 | 446 | 2009–2025 |
| SUP | 387 | 393 | 6 | 2015–2025 |
| NFI | 254 | 584 | 247 | 2000–2025 |
| VLT | 63 | 63 | 0 | 2011 |

`VRI`, `CMI`, and `YSM` are predominantly single-visit. Remeasurement is
concentrated in `YSM` (832 sites), `VRI` (497), `CMI` (446), and `NFI` (247).

### Visit type and sample design

| Field | Value | Count |
|-------|-------|------:|
| `VISIT_TYPE` | `TMP` (temporary) | 7,581 |
| `VISIT_TYPE` | `REP` (repeat) | 4,370 |
| `SAMP_TYP` | `V` (variable radius) | 6,930 |
| `SAMP_TYP` | `F` (fixed area) | 5,021 |
| `SAMPLE_SITE_PURPOSE_TYPE_CODE` | `Q` | 4,372 |
| | `Y` | 2,047 |
| | `M` | 1,760 |
| | `D` | 1,685 |
| | `T` | 582 |
| | `F` | 563 |
| | `O` | 550 |
| | `Z` | 329 |
| | `B` | 63 |

## 4. Coverage

### TSAs

All 37 TSA directories contain sites; the province-wide `TSA_DESC` field has
37 distinct non-empty values.

| TSA | Sites | TSA | Sites |
|-----|------:|-----|------:|
| Prince George | 1,243 | Fort Nelson | 193 |
| Williams Lake | 845 | Boundary | 188 |
| Okanagan | 475 | Sunshine Coast | 176 |
| Arrow | 438 | Revelstoke | 174 |
| Kamloops | 420 | Morice | 171 |
| North Island | 395 | Invermere | 150 |
| Fraser | 380 | Bulkley | 146 |
| Quesnel | 376 | Cranbrook | 140 |
| Dawson Creek | 374 | Golden | 115 |
| 100 Mile House | 340 | Cascadia | 111 |
| Lakes | 330 | Robson Valley | 96 |
| GBR South | 321 | GBR North | 88 |
| MacKenzie | 266 | Kootenay Lake | 76 |
| Fort St. John | 246 | Pacific | 72 |
| Kalum | 227 | Cassiar | 46 |
| Merritt | 223 | Kispiox | 43 |
| Arrowsmith | 205 | Soo | 20 |
| Lillooet | 199 | Nass | 7 |
| Haida Gwaii | 197 | | |

### BEC zones

16 BEC zones are represented:

| BEC zone | Sites |
|----------|-----:|
| ESSF | 1,851 |
| SBS | 1,828 |
| CWH | 1,749 |
| ICH | 1,129 |
| IDF | 886 |
| BWBS | 653 |
| MS | 613 |
| SBPS | 391 |
| MH | 200 |
| SWB | 105 |
| CMA | 49 |
| PP | 15 |
| IMA | 14 |
| BAFA | 10 |
| BG | 10 |
| CDF | 9 |

Latitude/longitude are present and non-zero for 7,134 of 9,512 sites (75.0%);
2,378 sites (25.0%) lack usable coordinates.

## 5. Species and sizes

42 species codes occur, plus 308 tree rows with missing species. Top fifteen
by tree-measurement count:

| Species | Tree rows |
|---------|----------:|
| PL | 93,837 |
| BL | 58,554 |
| SW | 41,866 |
| HW | 40,265 |
| FD | 34,032 |
| CW | 21,210 |
| SE | 14,946 |
| AT | 12,722 |
| BA | 8,717 |
| SB | 7,862 |
| EP | 5,390 |
| AC | 4,443 |
| YC | 4,334 |
| HM | 4,001 |
| SS | 3,796 |

DBH (`DBH`, cm):

| Statistic | Value |
|-----------|------:|
| Non-null rows | 357,845 (97.5%) |
| Minimum | 0.1 |
| 1st percentile | 4.2 |
| Median | 15.4 |
| 99th percentile | 100.0 |
| Maximum | 450.0 |
| Mean | 21.65 |

Height (`HEIGHT`, m):

| Statistic | Value |
|-----------|------:|
| Non-null rows | 285,584 (77.8%) |
| Minimum | 0.0 |
| 1st percentile | 2.3 |
| Median | 11.5 |
| 99th percentile | 37.9 |
| Maximum | 74.5 |
| Mean | 13.25 |

There is no `HEIGHT_SOURCE` column in the non-PSP tree table. Unlike the PSP
tables, field-measured versus estimated heights cannot be separated from the
tree record alone.

## 6. Age and site index

Site index and age are present, but coverage is lower than in the PSP corpus.

- `faib_compiled_spcsmries_siteage.csv` has 19,843 species-by-visit rows and
  covers all 11,951 visits.
- 9,318 visits (78.0%) have at least one `SI_M_TLSO` site-index value.
- 11,286 visits (94.4%) have at least one BH-age (`AGEB_TLSO`) or total-age
  (`AGET_TLSO`) value.
- Tree-level `SI_TREE` is populated for 51,832 of 367,096 rows (14.1%).
- Tree-level `AGE_BH` and `AGE_TOT` are populated for 59,248 and 59,249 rows
  (16.1%).
- Site index is carried as a species-level mean (`SI_M_TLSO`) plus sample
  counts (`N_AG_TLSO`, `N_HT_TLSO`), not as the three-method PSP `SI1`–`SI3`
  fields.

## 7. Plot design

| Measure | Value |
|---------|------:|
| Plot-header rows | 37,547 |
| Visits with 1 plot | 4,468 |
| Visits with 2 plots | 284 |
| Visits with 3 plots | 1,086 |
| Visits with 4 plots | 1,312 |
| Visits with 5 plots | 4,801 |
| `PLOT_AREA_MAIN` populated | 7,193 rows (19.2%) |
| Main plot area, median | 0.0400 ha |
| Main plot area, range | 0.0100–0.0400 ha |

Most visits use five plots and are variable-radius. `PLOT_AREA_MAIN` is
populated mainly for fixed-area plots; variable-radius expansion must use the
BAF/prism fields or the compiled per-hectare summaries.

## 8. Schema notes for calibration

- **Tree key:** `SITE_IDENTIFIER` + `PLOT` + `TREE_NO` identifies a tree across
  visits; `CLSTR_ID` identifies a site visit. There are no duplicate
  `(CLSTR_ID, PLOT, TREE_NO)` rows.
- **Expansion:** `PHF_TREE` is the per-hectare expansion factor; `PLOT_WT`,
  `TREE_WT`, `PLOT_AREA_MAIN`, `BLOWUP_MAIN`, and `V_BAF` document plot
  weighting. Check `SAMP_TYP` before applying an expansion method.
- **Heights:** the non-PSP tree table has `HEIGHT` but no `HEIGHT_SOURCE`;
  provenance of estimated heights is not distinguishable at tree level.
- **Utilization:** filter `UTIL` before aggregating. Summing across `UTIL`
  multiplies each visit five times.
- **Species:** 42 BC provincial codes need a crosswalk to FVS species; 308
  tree rows have missing species.
- **Age/SI:** use `faib_compiled_spcsmries_siteage.csv` for stand-level SI and
  age; tree-level fields are sparse (about 14–16%).
- **Coordinates:** 2,378 sites lack usable coordinates. TSA and BEC attributes
  are available for all sites in `faib_header`.
- **Duplicate scopes:** `publish_by_tsa/` duplicates `publish_province/` rows;
  pick one scope.

## 9. Relationship to the PSP corpus

The non-PSP and PSP site identifiers are disjoint:

| Corpus | Sites | Visits | Remeasured sites | Tree rows |
|--------|------:|-------:|-----------------:|----------:|
| PSP | 7,341 | 23,956 | 5,735 | 3,217,648 |
| Non-PSP | 9,512 | 11,951 | 2,028 | 367,096 |
| **Combined** | **16,853** | **35,907** | **7,763** | **3,584,744** |

The non-PSP corpus therefore adds 9,512 sites and 2,028 remeasured sites to
the BC FAIB archive. It does not replace the PSP corpus: PSP supplies the
bulk of remeasurement intervals, fixed-area plot areas, and the richer
three-method site-index fields. Use PSP for growth-and-yield calibration and
non-PSP for spatial coverage, single-visit initial conditions, and the
additional YSM/CMI/NFI remeasurement sites.

## 10. Data quality observations

- 311 tree rows have missing `LV_D`; 308 have missing `SPECIES`.
- DBH maximum is 450.0 cm and the 99th percentile is 100.0 cm; extreme stems
  should be checked before fitting diameter distributions.
- Height minimum is 0.0 m; the 1st percentile is 2.3 m. Zero heights should be
  treated as missing or checked against the source.
- 25.0% of sites lack usable coordinates; spatial joins must handle missing
  locations.
- The `publish_by_tsa/` tree has the same 12 table names in every directory;
  no TSA directory is empty.
