# MAGPlot v1.2 — Table Inventory and Profiling — 2026-11-14

Source package: `MAGPlot_latest_data_package.zip` (127,123,248 bytes, SHA-256 `270055bb9eeed6ccd6cbd75f6a2026b54e340c5a4938af18ad06e479792888db`), downloaded 2026-11-14 and unpacked to a scratch directory outside the repository. All row/column counts below were computed with pandas 3.0.3 from the extracted CSVs. The archive contains exactly eight CSV tables plus one PDF; there are no Parquet files.

## 1. Table inventory

| File | Rows (excl. header) | Columns | Primary key / key columns | Notes |
|------|--------------------:|--------:|---------------------------|-------|
| `magp_sites.csv` | 39,130 | 10 | `magp_site_id` | One row per site; province, coordinates, elevation, aspect/slope class, `gpp_type`, `flag_sites` |
| `magp_site_sources.csv` | 39,130 | 3 | `magp_site_id` | Source program (`sources`) and source plot identifier |
| `magp_tree_header.csv` | 257,031 | 10 | `magp_site_id`, `plot_type_id`, `plot_id`, `meas_num` | One row per plot measurement event; year/month, plot size, tagging limits, `meas_max` |
| `magp_trees.csv` | 7,771,041 | 29 | `magp_site_id`, `meas_num`, `plot_type_id`, `tree_num` | One row per tree measurement; species, DBH, height, crown class, `stem_ha`, status, condition |
| `magp_tree_condition.csv` | 1,383,908 | 11 | `magp_site_id`, `meas_num`, `plot_type_id`, `tree_num`, `condition`, `condition_location` | Multiple condition records per tree measurement |
| `magp_tree_removed.csv` | 382,012 | 9 | `magp_site_id`, `meas_num`, `plot_type_id`, `tree_num` | Trees removed from the main table; `reason` code |
| `magp_treatment.csv` | 14,362 | 6 | `magp_site_id`, `treatment_type`, `treatment_year` | Multiple treatments per site possible |
| `magp_disturbance.csv` | 5,378 | 8 | `magp_site_id`, `disturbance_type`, `disturbance_year` | Multiple disturbances per site possible; `disturbance_pct`, `mortality_pct` |
| `v1.2_FGP_magp_sites_coordinate_type_by_source.pdf` | — | — | — | Coordinate-type note by source (146,717 bytes) |

All table names match the eight tables named in `metadata/source-reviews/magplot.md`. Extensions are `.csv`.

## 2. Site, plot and tree counts

| Measure | Count |
|---------|------:|
| Distinct sites (`magp_sites`) | 39,130 |
| Distinct sites with a tree header | 38,910 |
| Sites with site record but no tree header | 220 (BC 131, NB 81, QC 7, NL 1) |
| Distinct `plot_id` values in tree header | 113,243 |
| Distinct sites in `magp_trees` | 38,895 |
| Distinct `plot_id` values in `magp_trees` | 113,190 |
| Tree measurement rows | 7,771,041 |
| Distinct tracked trees (`tree_num < 8,000,000`, keyed by site + plot + tree) | 2,866,168 |
| Distinct site + plot + tree groups (all tree records) | 3,684,955 |
| Distinct `tree_id` values | 2,866,169 (includes sentinel) |
| Tree header sites with no tree rows | 15 (all BC) |

`PLOT_ID` is a concatenation of site, plot type and ground-plot program type; it is constant across visits for a given plot. The persistent individual-tree key is `magp_site_id` + `plot_type_id` + `tree_num` for tracked trees.

## 3. Remeasurement and visit structure

Visits are counted as distinct `meas_num` per site in `magp_tree_header.csv`.

| Measure | Value |
|---------|------:|
| Sites with a tree header | 38,910 |
| Sites with >1 measurement (`meas_num`) | 20,890 (53.7% of sites with a header; 53.4% of all 39,130 sites) |
| Sites with exactly 1 measurement | 18,020 |
| Measurement year range | 1921–2024 |
| Remeasurement intervals (distinct years per site) | 62,741 intervals |
| Interval median / mean | 10.0 / 9.86 years |
| Interval range | 1–39 years |

### Visit-count distribution per site

| Visits (`meas_num` count) | Sites |
|--------------------------:|-----:|
| 1 | 18,020 |
| 2 | 3,634 |
| 3 | 5,126 |
| 4 | 3,911 |
| 5 | 5,689 |
| 6 | 1,494 |
| 7 | 550 |
| 8 | 369 |
| 9 | 80 |
| 10 | 12 |
| 11 | 15 |
| 12 | 5 |
| 13 | 5 |

### Measurement-interval distribution (years between successive distinct measurement years per site)

| Interval (years) | Count | Interval (years) | Count |
|------------------:|------:|------------------:|------:|
| 1 | 28 | 16 | 1,375 |
| 2 | 134 | 17 | 889 |
| 3 | 531 | 18 | 1,022 |
| 4 | 4,827 | 19 | 519 |
| 5 | 7,406 | 20 | 540 |
| 6 | 3,073 | 21 | 340 |
| 7 | 4,182 | 22 | 169 |
| 8 | 3,169 | 23 | 157 |
| 9 | 3,688 | 24 | 86 |
| 10 | 10,005 | 25 | 58 |
| 11 | 5,550 | 26 | 18 |
| 12 | 5,238 | 27 | 16 |
| 13 | 4,343 | 28 | 5 |
| 14 | 3,225 | 29 | 9 |
| 15 | 2,090 | 30 | 1 |
| 31 | 10 | 34 | 9 |
| 32 | 20 | 35 | 3 |
| 33 | 5 | 39 | 1 |

The distribution is concentrated at 4–15 years, with a mode at 10 years (15.9% of intervals) and a secondary mode at 5 years. Long intervals (20+ years) are a small tail.

## 4. Provincial / territorial coverage

Counts are site records in `magp_sites.csv`; remeasurement counts use distinct `meas_num` in the tree header for that province.

| Province / territory | Sites | Sites with tree header | Sites remeasured (>1 visit) | Tree measurement rows | Tracked trees | Tracked trees remeasured | Measurement-year range |
|----------------------|------:|-----------------------:|---------------------------:|----------------------:|--------------:|-------------------------:|------------------------|
| BC | 16,517 | 16,386 | 6,880 | 3,830,172 | 1,709,928 | 907,484 | 1921–2023 |
| QC | 12,892 | 12,885 | 12,420 | 2,596,029 | 862,044 | 520,551 | 1970–2024 |
| NB | 7,609 | 7,528 | 214 | 564,150 | 141,235 | 13,530 | 2016–2023 |
| NL | 1,350 | 1,349 | 1,132 | 649,459 | 134,761 | 115,676 | 1985–2023 |
| YT | 327 | 327 | 244 | 106,663 | 18,200 | 16,520 | 1988–2024 |
| NT | 262 | 262 | 0 | 14,471 | 0 | 0 | 2023–2024 |
| SK | 171 | 171 | 0 | 10,054 | 0 | 0 | 2024 |
| MB | 2 | 2 | 0 | 43 | 0 | 0 | 2024 |
| **Total** | **39,130** | **38,910** | **20,890** | **7,771,041** | **2,866,168** | **1,573,761** | **1921–2024** |

No Alberta, Ontario, Prince Edward Island or Nova Scotia sites are present in this open package. NT, SK and MB records are single-visit NorthForM temporary sample plots (NFM_GP); they contribute no remeasurement data.

## 5. Source-program coverage

| Source program | Sites | Sites remeasured | Tree rows | Tracked trees | Tracked trees remeasured | Measurement-year range |
|----------------|------:|-----------------:|----------:|--------------:|-------------------------:|------------------------|
| `BC_FAIBGP` | 16,517 | 6,880 | 3,830,172 | 1,709,928 | 907,484 | 1921–2023 |
| `QC_PSP` | 12,827 | 12,420 | 2,594,099 | 862,044 | 520,551 | 1970–2023 |
| `NB_CLI` | 7,609 | 214 | 564,150 | 141,235 | 13,530 | 2016–2023 |
| `NL_PSP` | 1,300 | 1,132 | 647,018 | 134,761 | 115,676 | 1985–2022 |
| `NFM_GP` | 616 | 0 | 32,592 | 0 | 0 | 2023–2024 |
| `YT_PSP` | 261 | 244 | 103,010 | 18,200 | 16,520 | 1988–2019 |
| **Total** | **39,130** | **20,890** | **7,771,041** | **2,866,168** | **1,573,761** | **1921–2024** |

Program types (`gpp_type`) by site: PSP `01` (23,402), VRI `03` (6,800), CMI `04` (920), YSM `05` (1,014), SUP `06` (387), VLT `07` (63), RPN `08` (236), TSP `11` (6,308). The TSP total is 616 NFM_GP sites plus 5,692 NB_CLI temporary sample plots.

## 6. Species

- Distinct `species_gsv` codes: **140**
- Distinct genera (`species_g`): **47**

Top 15 species codes by tree-measurement rows (all statuses):

| Rank | `species_gsv` | Rows | Share |
|-----:|---------------|-----:|------:|
| 1 | `ABIE.BAL.NA` (balsam fir) | 1,256,775 | 16.2% |
| 2 | `PICE.MAR.NA` (black spruce) | 997,083 | 12.8% |
| 3 | `PINU.CON.NA` (jack pine) | 787,343 | 10.1% |
| 4 | `TSUG.HET.NA` (western hemlock) | 752,663 | 9.7% |
| 5 | `PSEU.MEN.NA` (Douglas-fir) | 711,385 | 9.2% |
| 6 | `PICE.GLA.NA` (white spruce) | 421,318 | 5.4% |
| 7 | `BETU.PAP.NA` (paper birch) | 392,049 | 5.0% |
| 8 | `THUJ.PLI.NA` (western redcedar) | 336,068 | 4.3% |
| 9 | `POPU.TRE.NA` (trembling aspen) | 291,942 | 3.8% |
| 10 | `ABIE.LAS.NA` (subalpine fir) | 263,799 | 3.4% |
| 11 | `ACER.RUB.NA` (red maple) | 192,821 | 2.5% |
| 12 | `ACER.SAH.NA` (sugar maple) | 142,868 | 1.8% |
| 13 | `PINU.BAN.NA` (jack pine, variety) | 104,095 | 1.3% |
| 14 | `LARI.OCC.NA` (western larch) | 94,692 | 1.2% |
| 15 | `PICE.SIT.NA` (Sitka spruce) | 75,329 | 1.0% |

Unknown or hybrid codes are present in the 140-code list and must be handled explicitly in a species crosswalk. The live-tree top 15 is similar but ranks `PICE.GLA` above `TSUG.HET` by live-row count; dead-tree records are dominated by `TSUG.HET` (144,477), `ABIE.BAL` (124,953) and `PINU.CON` (114,477).

## 7. DBH, height and status

### DBH (`dbh`, cm)

| Measure | Value |
|---------|------:|
| Rows with DBH >0 | 7,705,604 (99.16%) |
| `-1` missing sentinel | 65,437 (0.84%) |
| Minimum >0 | 0.1 |
| Median >0 | 10.8 |
| Mean >0 | 13.13 |
| 95th percentile >0 | 32.6 |
| 99th percentile >0 | 53.1 |
| 99.9th percentile >0 | 96.9 |
| Maximum | 450.0 |

The maximum and the 272 records >200 cm (20 >300 cm) are implausible for standing-tree DBH and should be treated as data-quality outliers, not calibration values.

### Height (`height`, m)

| Measure | Value |
|---------|------:|
| Rows with height >0 | 4,716,644 (60.70%) |
| `-1` missing sentinel | 3,054,397 (39.30%) |
| Minimum >0 | 0.1 |
| Median >0 | 11.1 |
| 99th percentile >0 | 40.0 |
| Maximum | 74.5 |

Height coverage differs sharply by status: live standing 72.6%, dead standing 67.8%, live (unspecified) 48.3%, status missing 0.5%, live fallen 30.7%.

### Tree status (`tree_status`)

| Status | Meaning | Rows | Share |
|--------|---------|-----:|------:|
| `LS` | Live standing | 4,994,364 | 64.3% |
| `L` | Live (standing/unspecified) | 1,062,978 | 13.7% |
| `-1` | Missing status | 863,596 | 11.1% |
| `DS` | Dead standing | 838,651 | 10.8% |
| `LF` | Live fallen | 11,452 | 0.1% |

Live records total 6,068,794 (78.1%); dead standing is 838,651 (10.8%); status is missing for 11.1%.

### Stem expansion (`stem_ha`)

| Measure | Value |
|---------|------:|
| Rows with `stem_ha` >0 | 7,754,049 (99.78%) |
| Minimum >0 | 0.99 stems/ha |
| Median >0 | 25 stems/ha |
| 99th percentile >0 | 250 stems/ha |
| 99.9th percentile >0 | 1,500 stems/ha |
| Maximum | 18,444 stems/ha |
| Rows >1,000 stems/ha | 11,991 |
| Rows >500 stems/ha | 24,684 |

The high tail is consistent with scaling from very small subplots (0.0005–0.005 ha), not necessarily error, but it must be handled in expansion and yield calculations.

## 8. Tree identity across visits

The `tree_num` range is the control:

- `< 8,000,000`: tracked, permanently tagged trees; the same `tree_num` is the same tree across measurements.
- `8,000,000–8,999,999`: untracked regeneration trees; `tree_num` is reassigned across measurements.
- `9,000,000–99,999,999`: untracked small trees and duplicate/anomalous records; not unique across measurements.

| Measure | Value |
|---------|------:|
| Tracked tree rows (`tree_num < 8M`) | 6,526,753 (84.0% of tree rows) |
| Untracked 8M-series rows | 678,154 (8.7%) |
| Untracked 9M-series rows | 566,134 (7.3%) |
| Distinct tracked trees | 2,866,168 |
| Tracked trees observed at >1 measurement | 1,573,761 (54.9%) |
| Tracked trees observed once | 1,292,407 (45.1%) |
| Maximum measurements per tracked tree | 13 |
| `tree_id` collisions within a tracked site/plot/tree group | 0 |
| Tracked rows with `tree_id = -9` | 0 |

Tracked-tree measurement-count distribution:

| Measurements per tree | Trees |
|----------------------:|------:|
| 1 | 1,292,407 |
| 2 | 667,877 |
| 3 | 378,221 |
| 4 | 231,788 |
| 5 | 127,138 |
| 6 | 68,572 |
| 7 | 50,420 |
| 8 | 30,772 |
| 9 | 7,763 |
| 10 | 5,138 |
| 11 | 4,214 |
| 12 | 1,216 |
| 13 | 642 |

Tree identity therefore persists across visits for the tracked subset (84% of rows), which is the subset usable for individual-tree growth and mortality calibration. Untracked records can only support stand-level or count-based analyses.

## 9. Plot design and expansion factors

| Field | Availability |
|-------|--------------|
| `meas_plot_size` (ha) | 227,538 tree-header rows with a positive value (88.5%); `-9` for 29,169 rows (all V1 and B1 variable-radius/buffer plots); `-1` missing for 324 rows |
| Positive `meas_plot_size` range | 0.0005–0.81 ha; median 0.005 ha; common values 0.004 ha (111,719 rows), 0.04 ha (68,142), 0.0625 ha (11,423) |
| `taglimit_dbh` (cm) | Present for all rows; common limits 1.1, 9.1, 4.0, 2.0 cm; `-1` missing 39,215; `-9` not applicable when trees <1.3 m were measured |
| `taglimit_height` (m) | Present for all rows; typically 1.3 m |
| `stem_ha` | Supplied per tree row; derived as 1/plot area for fixed-area plots |
| PHF (plot expansion factor) | **Not present** as a named field |
| BAF (basal area factor) | **Not present** as a named field |
| Plot radius | **Not present** as a named field |

All plots are fixed-radius except BC VRI (`gpp_type 03`), SUP (`06`) and VLT (`07`), which include variable-radius plots. Variable-radius plots have `meas_plot_size = -9` and no BAF, so per-hectare expansion for those plots cannot be reconstructed from the package alone; `stem_ha` is `-9` for non-area-based designs.

## 10. Disturbance, treatment and removals

### Disturbance (`magp_disturbance.csv`)

5,378 records on 3,850 sites; disturbance years 1890–2023 (5 records with missing year sentinel). Top codes (Appendix B):

| Code | Meaning | Records |
|------|---------|--------:|
| `DBIL` | Disease/insect — light epidemic | 2,007 |
| `FT` | Total burn | 1,818 |
| `AWWP` | Windthrow — partial/light | 473 |
| `DBIS` | Disease/insect — severe epidemic | 392 |
| `C` | Cutting (general) | 142 |
| `AWW` | Windthrow/wind | 137 |
| `AWWT` | Windthrow — total | 115 |
| `BI` | Insect | 108 |
| `CM` | Mechanical damage from forestry operations | 57 |
| `UDP` | Dieback/decline — partial/light | 55 |
| `FP` | Partial/light burn | 45 |
| `F` | Burning | 14 |
| `AWIP` | Ice/frost — partial damage | 6 |
| `BA` | Animal | 5 |
| `AWF` | Flood/water | 2 |
| `UDT` | Dieback/decline — total | 1 |
| `BPC` | Plant competition | 1 |

Grouped: fire codes (`F`, `FT`, `FP`) = 1,877 records; insect/disease codes (`BI`, `DBIL`, `DBIS`) = 2,507; wind codes (`AWW`, `AWWP`, `AWWT`) = 725; harvest/cutting (`C`, `CC`, `CM`) = 256 (no `CC` records in this package); other abiotic/biotic codes account for the remainder.

### Treatment (`magp_treatment.csv`)

14,362 records on 10,381 sites; treatment years 1933–2023 (1,075 records with missing year sentinel). Top codes (Appendix A):

| Code | Meaning | Records |
|------|---------|--------:|
| `CLR` | Partial cutting | 4,504 |
| `CC` | Clearcut | 4,003 |
| `TTP` | Pre-commercial thinning/spacing | 1,705 |
| `CLE` | Regeneration protection | 1,248 |
| `RP` | Planting (general) | 766 |
| `RPF` | Full planting | 548 |
| `CL` | Selection cutting (general) | 529 |
| `TC` | Cleaning (brushing/weeding) | 301 |
| `RNF` | Natural regeneration — fallow land | 128 |
| `RPFS` | Full planting — containerized seedlings | 104 |
| `TTM` | Commercial thinning | 86 |
| `RPIR` | Regenerated forests | 53 |
| `CLS` | Strip selection cutting | 50 |
| `CP` | Pre-selection cutting | 39 |
| `CLA` | Sanitation cutting | 38 |

### Removed trees (`magp_tree_removed.csv`)

382,012 records on 17,707 sites. Reasons:

| Code | Meaning | Records |
|------|---------|--------:|
| `U` | Tree cannot be found at remeasurement | 189,104 |
| `C` | Tree was cut | 98,337 |
| `F` | Tree is dead and has fallen | 61,072 |
| `D` | Disqualified for not meeting agency requirements | 28,823 |
| `O` | Other reason | 4,676 |

Harvest, fire, insect and wind disturbance fields therefore exist and are codified. They are site-level event records, not necessarily linked to a specific measurement interval; interval assignment must be explicit in any calibration build.

## 11. Feasibility assessment for fresh-FVS-CA calibration

**Verdict: usable as a Tier-1 regional calibration source for BC, QC, NL and YT (plus a small NB remeasurement subset), but not sufficient on its own for a national FVS-CA calibration.**

Supporting evidence:

- **Growth increments:** 1,573,761 tracked trees have ≥2 measurements; 20,890 sites are remeasured. The 10-year median interval matches typical FVS cycle lengths, though intervals range 1–39 years and must be normalized to annual increments.
- **Species:** 140 `species_gsv` codes with 47 genera provide broad conifer and hardwood coverage, but codes must be crosswalked to FVS species; unknown/hybrid codes and the BC/QC code conventions need explicit mapping.
- **Size and status:** DBH is 99.2% populated; live/dead status is present for 88.9% of rows; dead standing (838,651 rows) and removed-tree records support mortality calibration. Height is only 60.7% populated, so height-diameter and height-growth fitting must handle missingness (live-standing coverage is 72.6%).
- **Plot design:** fixed-area plot size is present for 88.5% of plot visits; `STEM_HA` supplies expansion for fixed-area plots. Variable-radius BC VRI/SUP/VLT plots lack BAF/plot area and cannot support per-hectare calibration without external plot-design information.
- **Disturbance:** harvest, fire, insect/disease, wind and removals are coded, enabling disturbance-aware calibration and mortality attribution, but events are site-level and not interval-keyed.
- **Critical gaps:** no age, site-index, soil or ecological tables in v1.2; no Alberta, Ontario, PEI or Nova Scotia records; all coordinates are approximate (±10 km) and 1,027 BC sites have no coordinates; NFM TSP records are single-visit. A national FVS-CA calibration still requires the NFI DUA data (and provincial supplements for AB/ON/PE/NS) plus a site-index/age source.
- **Immediate next step:** build a calibration extract restricted to tracked trees with ≥2 measurements and fixed-area plots, pair consecutive measurements by `tree_id`/`tree_id_meas`, compute annual DBH and height increments, and preserve `tree_status`, `tree_removed.reason`, `magp_treatment`, and `magp_disturbance` as event covariates. Do not use the 8M/9M untracked records for individual-tree growth.
