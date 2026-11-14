# BC FAIB PSP Compilation — Table Inventory and Profiling — 2026-11-14

Source: `psp/` tables from the anonymous BC FAIB FTP publication tree,
retrieved 2026-11-14. Compilation files are dated 2026-04-16/20; the data
dictionary is `PSP_data_dictionary_2026Apr20.xlsx`. All CSVs are archived
gzipped; row counts below were computed from the decompressed files and match
the original CSV line counts.

## 1. Table inventory

| Archived file | Rows | Columns | Key columns | Notes |
|---------------|-----:|--------:|-------------|-------|
| `psp/faib_header.csv.gz` | 7,341 | 26 | `SITE_IDENTIFIER` | One row per site. BEC zone/subzone/variant, TSA/TFL, ownership, coordinates, establishment type, site status. |
| `psp/faib_plot_header.csv.gz` | 24,974 | 19 | `SITE_IDENTIFIER`, `CLSTR_ID`, `PLOT` | One row per plot within a visit. Plot area, shape, radius/width/length, BAF, slope/aspect/elevation. |
| `psp/faib_sample_byvisit.csv.gz` | 23,956 | 29 | `CLSTR_ID` | One row per site visit. Measurement date/year, period, plot count, sample type, purpose, visit type, DBH limits. |
| `psp/faib_compiled_smries.csv.gz` | 119,780 | 36 | `CLSTR_ID`, `UTIL` | Stand-level summary per visit at five utilization limits (2, 4, 7.5, 12.5, 17.5 cm). BA, stems/ha, volume/ha, QMD, species composition. |
| `psp/faib_compiled_smeries_ht.csv.gz` | 23,956 | 8 | `CLSTR_ID` | Visit-level height summary: mean live, ingrowth, veteran, live+ingrowth, and Lorey height. |
| `psp/faib_compiled_spcsmries.csv.gz` | 416,570 | 34 | `CLSTR_ID`, `UTIL`, `SPECIES` | Species-level summary per visit and utilization limit. |
| `psp/faib_compiled_spcsmries_siteage.csv.gz` | 86,468 | 16 | `CLSTR_ID`, `SPECIES` | Species-level site index and age: `SI1`–`SI3`, `AGE_BH1`–`AGE_BH3`, `AGE_TOT1`–`AGE_TOT3`, `HTOP1`–`HTOP3`. |
| `psp/faib_smltree_smries_cl.csv.gz` | 14,911 | 15 | `SITE_IDENTIFIER`, `VISIT_NUMBER` | Small-tree summary by count/plot. |
| `psp/faib_smltree_smries_clsp.csv.gz` | 21,111 | 12 | `SITE_IDENTIFIER`, `VISIT_NUMBER`, `SPECIES` | Small-tree summary by species. |
| `psp/faib_tree_detail.csv.gz` | 3,217,648 | 50 | `CLSTR_ID`, `PLOT`, `TREE_NO` | Tree measurement record. Species, DBH, height and height source, live/dead, damage, age, site index, expansion, volumes. |

## 2. Site, visit, and tree counts

| Measure | Value |
|---------|------:|
| Distinct sites | 7,341 |
| Distinct visits (`CLSTR_ID`) | 23,956 |
| Remeasured sites (>1 visit) | 5,735 (78.1%) |
| Maximum visits per site | 13 |
| Tree measurement rows | 3,217,648 |
| Unique trees | 1,138,768 |
| Remeasured trees (>1 visit) | 803,868 (70.6%) |
| Mean measurements per tree | 2.83 |
| Live tree rows | 2,646,320 |
| Dead tree rows | 571,323 |
| Measurement years | 1921–2025 |
| Measurement dates | 1921-10-24 to 2025-09-10 |

All 23,956 visits are `VISIT_TYPE = REP`, `SAMP_TYP = F` (fixed area), and
`SAMPLE_SITE_PURPOSE_TYPE_CODE = PSP`.

### Visits per site

| Visits | Sites |
|-------:|-----:|
| 1 | 1,606 |
| 2 | 1,341 |
| 3 | 1,254 |
| 4 | 1,322 |
| 5 | 991 |
| 6 | 453 |
| 7 | 197 |
| 8 | 106 |
| 9 | 33 |
| 10 | 13 |
| 11 | 15 |
| 12 | 4 |
| 13 | 6 |

## 3. Coverage and attributes

### BEC zones

| BEC zone | Sites |
|----------|-----:|
| CWH | 2,335 |
| ICH | 1,269 |
| SBS | 1,206 |
| IDF | 973 |
| BWBS | 534 |
| ESSF | 420 |
| MS | 376 |
| SBPS | 170 |
| CDF | 26 |
| PP | 16 |
| MH | 13 |
| CMA | 3 |

`TSA` has 40 distinct values; `TFL` has 26. Latitude/longitude are present for
6,315 of 7,341 sites (86.0%); 1,026 sites lack coordinates.

### Species

45 species codes are present, plus 5 tree rows with missing species. The top
ten by tree-measurement count:

| Species | Tree rows |
|---------|----------:|
| HW | 688,291 |
| FD | 619,648 |
| PL | 583,856 |
| CW | 260,930 |
| SW | 222,068 |
| BL | 200,782 |
| AT | 136,074 |
| LW | 75,959 |
| SS | 73,456 |
| EP | 71,726 |

### Diameter and height

| Attribute | Population | Min | Median | Max |
|-----------|-----------:|----:|-------:|----:|
| DBH (`DBH`, cm) | 3,217,462 non-null | 0.5 | 12.4 | 401.7 |
| Height (`HEIGHT`, m) | 3,217,457 non-null | 0.37 | 13.4 | 73.3 |

DBH 1st/99th percentiles: 2.9 / 59.9 cm. Height availability is 99.99%;
`HEIGHT_SOURCE` records 788,305 field-measured heights (24.5%), 2,429,152
DBH-estimated heights (75.5%), and 191 missing (0.006%).

### Age and site index

- `faib_compiled_spcsmries_siteage.csv` contains 86,468 species-by-visit rows.
- 21,639 of 23,956 visits (90.3%) have at least one site-index method.
- 21,976 visits (91.7%) have at least one BH-age or total-age value.
- Tree-level `SI_TREE` is populated for 296,482 rows (9.2%); `AGE_BH` and
  `AGE_TOT` are populated for 304,185 rows (9.5%).
- Site index is expressed by three methods, matching BC SINDEX conventions:
  `SI1` (largest suitable DBH site tree per 0.01 ha), `SI2` (largest DBH
  suitable site trees at 100/ha), and `SI3` (average age/height of aged
  largest-DBH trees).

### Plot design

| Measure | Value |
|---------|------:|
| Plot-header rows | 24,974 |
| Visits with 1 plot | 23,446 |
| Visits with 2 plots | 2 |
| Visits with 3 plots | 508 |
| Main plot area, median | 0.0809 ha |
| Main plot area, range | 0.0050–0.81 ha |
| Plot shapes | CI 15,812; SQ 6,427; RE 2,735 |
| `V_BAF` | 84 rows with 0.0; otherwise null |

The corpus is fixed-area PSP; `V_BAF` is not a usable variable-radius BAF
field. Per-hectare expansion is carried by `PHF_TREE` and the plot-area fields.

### Compiled summaries

- `faib_compiled_smries.csv`: 119,780 rows = 23,956 visits × 5 utilization
  limits (`UTIL` = 2, 4, 7.5, 12.5, 17.5 cm).
- `faib_compiled_spcsmries.csv`: 416,570 rows = species × visit × utilization.
- `faib_compiled_smeries_ht.csv`: 23,956 rows; mean live height present for
  23,948 visits; Lorey height for 20,861 visits.

## 4. Schema notes for calibration

- **Tree key:** `SITE_IDENTIFIER` + `PLOT` + `TREE_NO` identifies a tree across
  visits; `CLSTR_ID` identifies a site visit. `TREE_NO` is unique within a
  plot. There are no duplicate `(CLSTR_ID, PLOT, TREE_NO)` rows.
- **Expansion:** `PHF_TREE` is the per-hectare expansion factor; `PLOT_WT`,
  `TREE_WT`, `PLOT_AREA_MAIN`, and `BLOWUP_MAIN` document plot weighting.
- **Heights:** use `HEIGHT` with `HEIGHT_SOURCE`; do not treat DBH-estimated
  heights as field observations.
- **Utilization:** filter `UTIL` before aggregating. Summing across `UTIL`
  multiplies each visit five times.
- **Species:** BC provincial codes (`HW`, `FD`, `PL`, `CW`, ...) require a
  crosswalk to FVS species. Five tree rows have missing species.
- **Age/SI:** tree-level age and site index are sparse (about 9% of tree rows);
  use the species-by-visit siteage table for stand-level SI/age coverage.
- **Coordinates:** 1,026 sites lack latitude/longitude. BEC and TSA/TFL
  attributes are available for all sites in `faib_header`.

## 5. Data quality observations

- DBH maximum is 401.7 cm; the 99th percentile is 59.9 cm. Extreme stems
  should be checked before fitting diameter distributions.
- There are 5 tree rows with missing `LV_D` and 5 with missing `SPECIES`.
- Height is missing for 191 tree rows; all other heights are either field
  measured or DBH-estimated.
- `PERIOD` between visits has a median of 6 years and a maximum of 35 years;
  growth increments must be normalized by the actual interval.
- `faib_header.SITE_STATUS_CODE` has only `IA` (4,298) and `A` (3,043);
  `SAMPLE_ESTABLISHMENT_TYPE` has `PSP_G` (5,289) and `PSP_R` (2,052).

## 6. Companion non-PSP corpus (not archived)

The sibling `non_psp/` directory contains the province-wide VRI/CMI/YSM/NFI
compilation and a `publish_by_tsa/` tree with 37 TSA directories. The
province-wide files include `faib_tree_detail.csv` (92,488,343 bytes),
`faib_compiled_spcsmries.csv` (22,866,655 bytes), and the same header/visit/
summary table family. It was not downloaded in this pass; the access route is
identical (`ftp://ftp.for.gov.bc.ca/HTS/external/!publish/ground_plot_compilations/non_psp/`).
