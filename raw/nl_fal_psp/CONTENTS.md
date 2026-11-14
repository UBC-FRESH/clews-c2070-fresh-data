# NL FAL Permanent Sample Plots — Table Inventory and Profiling — 2026-11-14

Source: `FAL_-_Permanent_Sample_Plots` FeatureServer, exported 2026-11-14.
Counts below are observations of this snapshot. Dates are interpreted in
`America/St_Johns` (epoch-millisecond fields are local midnight).

## 1. Layer inventory

| Archived file | Service layer | Type | Features / rows |
|---|---|---|---:|
| `mature.geojson.gz` | Mature | Point | 412 |
| `immature.geojson.gz` | Immature | Point | 968 |
| `age_group.csv.gz` | Age Group | Table | 592 |
| `disturbance_history.csv.gz` | Disturbance History | Table | 470 |
| `remeasurement.csv.gz` | Remeasurement | Table | 7,660 |
| `immature_trees_remeasurement.csv.gz` | Immature Trees Remeasurement | Table | 588,865 |
| `immature_sample_trees_remeasurement.csv.gz` | Immature Sample Trees Remeasurement | Table | 52,651 |
| `immature_trees_permanent.csv.gz` | Immature Trees Permanent | Table | 107,785 |
| `mature_trees_permanent.csv.gz` | Mature Trees Permanent | Table | 35,500 |
| `mature_trees_remeasurement.csv.gz` | Mature Trees Remeasurement | Table | 186,783 |
| `plot_layout.csv.gz` | Plot Layout | Table | 6,628 |
| `plot_location_description.csv.gz` | Plot Location Description | Table | 1,351 |
| `remeasurement_crew_date.csv.gz` | Remeasurement Crew Date | Table | 7,659 |
| `silviculture_history.csv.gz` | Silviculture History | Table | 430 |

Service metadata is in `metadata/`; every `features` count in
`metadata/export_manifest.json` matches the layer's `returnCountOnly` value.

## 2. Plots and visits

| Measure | Value |
|---|---:|
| Plots | 1,380 |
| Mature plots | 412 |
| Immature plots | 968 |
| Plots with coordinates | 1,380 |
| Distinct `PLOTKEY` | 1,380 |
| Mature/immature overlap | 0 |
| Remeasurement rows | 7,660 |
| Usable visits (non-null `PLOTKEY`) | 7,659 |
| Plots with remeasurement records | 1,379 |
| Remeasured plots (>1 visit) | 1,242 |
| Single-visit plots | 138 |
| Maximum visits per plot | 10 |
| Visit years | 1985–2026 |

One `remeasurement` row (OBJECTID 14105) has a null `PLOTKEY` and no plot
measurements. One immature plot (`5_119019`, district 05) has no
remeasurement row. The crew-date table has 7,659 rows and joins to every
usable visit.

Visits per plot:

| Visits | Plots |
|---:|---:|
| 1 | 138 |
| 2 | 160 |
| 3 | 112 |
| 4 | 147 |
| 5 | 23 |
| 6 | 151 |
| 7 | 182 |
| 8 | 263 |
| 9 | 162 |
| 10 | 42 |

Visits by plot type: mature 2,150 visits on 412 plots; immature 5,507 visits
on 967 plots; one orphan row.

Plot status (`PLOTSTATUS`):

| Status | Mature | Immature |
|---|---:|---:|
| Active (A) | 238 | 819 |
| Monitor (M) | 87 | 46 |
| Inactive (I) | 68 | 66 |
| Replaced (R) | 19 | 36 |
| Training (T) | 0 | 1 |

Recorded plot origin years: mature 1680–2010 (408 populated), immature
1880–2015 (944 populated). Some origin years predate the visit record and
should be checked before use.

## 3. Tree tallies and identity

| Measure | Mature | Immature | Total |
|---|---:|---:|---:|
| Tree measurement rows | 186,783 | 588,865 | 775,648 |
| Unique trees (`PLOTKEY`+`TREENUMBER`) | 35,671 | 107,918 | 143,589 |
| Trees in >1 visit | 33,870 | 93,785 | — |
| Trees in >1 visit (%) | 94.95% | 86.90% | — |
| Permanent-tree list rows | 35,500 | 107,785 | 143,285 |
| Remeasurement rows matched to permanent list | 186,534 (99.87%) | 588,723 (99.98%) | — |

Tree identity persists through `PLOTKEY` + `TREENUMBER`. The permanent lists
contain slightly fewer trees than the remeasurement tables (mature −171,
immature −133), consistent with ingrowth or untagged trees in later visits.

## 4. DBH, height, and status

DBH is in centimetres; height is in metres.

| Measure | Mature | Immature |
|---|---:|---:|
| DBH populated | 165,237 (88.46%) | 508,601 (86.37%) |
| DBH min / median / max | 8.0 / 13.1 / 99.0 | 0.0 / 6.0 / 85.0 |
| Height populated | 37,732 (20.20%) | 446,147 (75.76%) |
| Height min / median / max | 0.0 / 10.6 / 99.0 | 0.0 / 4.9 / 81.0 |

Status groups:

| Status | Mature rows | Immature rows |
|---|---:|---:|
| Live | 138,235 | 463,112 |
| Dead | 40,075 | 95,895 |
| Not located / missing or cut | 8,473 | 29,858 |

Mature `TREESTATUS` uses ten states: live 0, 3, 4, 6, 7, 8; dead 1, 2, 5;
not located 9. Immature uses 0 live, 1 dead, 9 missing or cut. Do not treat
the raw code as a binary live/dead flag.

Live-tree DBH and height:

| Group | DBH median (cm) | Height populated | Height median (m) |
|---|---:|---:|---:|
| Mature live | 13.2 | 36,641 (26.51%) | 10.6 |
| Mature dead | 12.8 | 1,088 (2.71%) | 10.4 |
| Immature live | 6.4 | 417,841 (90.22%) | 5.1 |
| Immature dead | 3.5 | 28,168 (29.37%) | 2.5 |

One mature dead-tree height of 99 (the field maximum) is a sentinel, not a
credible metre value. Immature DBH has 5 zero values; no mature DBH is zero.
DBH 99 occurs once in mature dead trees and should also be treated with
caution.

## 5. Species

The permanent-tree lists carry 14 simplified species codes (mature 11,
immature 14). Overall counts:

| Code | Rows | Mature | Immature |
|---|---:|---:|---:|
| bF | 71,494 | 15,076 | 56,418 |
| bS | 54,567 | 18,476 | 36,091 |
| wB | 9,332 | 1,117 | 8,215 |
| wS | 4,490 | 390 | 4,100 |
| tL | 746 | 216 | 530 |
| OH | 735 | 19 | 716 |
| tA | 603 | 74 | 529 |
| rM | 384 | 29 | 355 |
| 9 | 320 | 92 | 228 |
| yB | 287 | 5 | 282 |
| jP | 218 | 0 | 218 |
| nS | 57 | 0 | 57 |
| wP | 50 | 6 | 44 |
| OP | 2 | 0 | 2 |

Interpreted composition strings (`INTERPSPEC`) are richer: 25 distinct values
on mature plots and 39 on immature plots, dominated by `bS`, `bF`, `bSbF`,
and `bFbS`. These are stand-level composition labels, not tree-level species.

## 6. Age, site, and productivity

| Measure | Rows | Coverage | Range / notes |
|---|---:|---|---|
| Age Group `SAMPLEAGE` | 592 | all 412 mature plots | 34–279 years, median 95 |
| Age Group `DBH` | 592 | 100% | 3.4–40.9 cm, median 15.7 |
| Age Group `TREEHEIGHT` | 592 | 100% | 2.4–21.7 m, median 11.0 |
| Sample-tree `TREEAGE` | 52,640 | 99.98% of 52,651 rows | 1–179 years, median 43 |
| Sample-tree `CROWNHEIGHT` | 52,651 | 100% | 0–63 m, median 3.8 |

No numeric site index is stored. Plot attributes provide `INTERPSITE`
(H/G/M/P; 409 mature and 961 immature plots), `INTERPAGE` and
`INTERPHEIGHT` classes (all plots), `DAMMONSITETYPE`, `SLOPE`, `ASPECT`, and
`YEAROFORIGIN`. `ACTUALSITE` and `STANDSTATUS` are repeated per visit in the
remeasurement table. Site index must be derived.

## 7. Disturbance and silviculture

Disturbance History: 470 rows on 361 plots, years 1950–2020, severity 1–100
(median 20). Types:

| Code | Meaning | Rows |
|---|---|---:|
| X / x | Harvest | 145 |
| W / w | Wind | 137 |
| Z | Insect | 108 |
| M | Mechanical / misc. | 57 |
| Y | Fire | 14 |
| B | Severe browsing | 5 |
| P | Plantation | 3 |
| V | Vegetation | 1 |

Silviculture History: 430 rows on 410 plots, years 1965–2018. Types:

| Code | Rows |
|---|---:|
| PCT | 287 |
| P | 122 |
| PB | 7 |
| CT | 6 |
| GP | 4 |
| PM | 2 |
| AS | 1 |
| DLT | 1 |

## 8. Plot design, layout, and access

`PLOTSIZE` (no coded domain; interpreted as m²) distribution across the 7,660
remeasurement rows:

| PLOTSIZE | Rows |
|---:|---:|
| 2 | 309 |
| 4 | 626 |
| 7 | 586 |
| 10 | 1,001 |
| 20 | 1,181 |
| 25 | 651 |
| 40 | 3,052 |
| 50 | 129 |
| 67 | 88 |
| 100 | 37 |

Mature plots are predominantly 40 m²; immature plots use smaller nested
plots. `PLOTLENGTH` and `PLOTWIDTH` are recorded per visit.

- `plot_layout`: 6,628 subplot records on 1,326 plots (direction, azimuth,
  distance).
- `plot_location_description`: 1,351 text records on 1,342 plots; 39 plots
  lack location text. Some plots have more than one descriptive record.

## 9. Interpretation cautions

- The service is live and unversioned. Re-run `returnCountOnly` and re-hash
  before reuse; 2026 visits make this snapshot newer than a typical annual
  release.
- Dates are local-midnight epoch milliseconds. UTC conversion moves
  New Year's Day visits into the previous year.
- The `remeasurement` table has one null-`PLOTKEY` row and one immature plot
  has no visit record. Do not assume every plot in the point layers has a
  matching visit.
- Species are broad codes; `9` is unknown and `OH`/`OP` are "other" classes.
  The permanent list is the species key for the remeasurement tables.
- DBH and height are incomplete, especially height on dead trees. The 99
  values are sentinels.
- Disturbance and silviculture records are sparse and plot-level, not
  tree-level treatments.
