# Québec PEP — Table Inventory and Profiling — 2026-11-14

Source: `PEP_GPKG.zip` → `PEP.gpkg`, retrieved 2026-11-14 from Données
Québec (MRNF, Direction des inventaires forestiers). All counts below were
computed from the extracted GeoPackage; they are observations of this
snapshot, not published totals.

## 1. Database inventory

`PEP.gpkg` has 46 SQLite tables: 24 content layers plus GeoPackage system
tables, R-tree indexes, and one QGIS style row. SRS is EPSG:32198 (NAD83 /
Québec Lambert Conformal Conic).

| Layer / table | Geometry | Rows | Role |
|---|---:|---:|---|
| `placette` | Point | 12,834 | One row per permanent plot; `id_pe`, network, map sheet, coordinates, status |
| `placette_mes` | — | 53,632 | One row per plot visit; `id_pe_mes`, `no_mes`, dimension code, measurement date |
| `dendro_arbres` | — | 2,210,417 | Tally-tree measurement; `id_arbre` persistent identity, `id_arb_mes` measurement identity |
| `dendro_arbres_etudes` | — | 442,560 | Intensively measured subsample: total height, age, age-core height |
| `dendro_gaules` | — | 235,455 | Sapling tally by 2/4/6/8 cm DBH class |
| `station_pe` | — | 53,632 | Station description per visit; origin, disturbance, cover, age class, dominant height, ecological type |
| `classi_eco_pe` | — | 12,834 | Ecological classification per plot |
| `meta_notes_pe` | — | 53,632 | Plot/visit notes and abandonment reasons |
| `pee_ori_sond` | — | 53,632 | Original survey description per visit |
| `pee_essence_ori_sond` | — | 43,546 | Original survey species composition |
| `pee_etage_ori_sond` | — | 13,152 | Original survey strata |
| `station_sol` | — | 35,014 | Soil profile |
| `station_essence` | — | 63,032 | Station species composition |
| `station_etage` | — | 13,936 | Station strata |
| `station_semis` | — | 125,510 | Seedling counts |
| `station_semis_nco` | — | 78,755 | Non-commercial seedling counts |
| `station_debris_4` | — | 8,334 | Coarse woody debris, 4-class |
| `station_debris_5` | — | 3,551 | Coarse woody debris, 5-class |
| `plan_descr_type_pe` | — | 13 | Plot design catalogue: shape, radius, area, expansion factor |
| `plan_reseau` | — | 8 | Network establishment/abandonment/active counts |
| `plan_composante_factexp_region` | — | 10,569 | Plot-to-region sampling component |
| `plan_region_bas1` | MultiPolygon | 13 | BAS1 inventory regions |
| `plan_region_bas2` | MultiPolygon | 16 | BAS2 inventory regions |
| `layer_styles` | — | 1 | QGIS style metadata, not data |

## 2. Plots, visits, and remeasurement

| Measure | Value |
|---|---:|
| Distinct plots (`id_pe`) | 12,834 |
| Distinct visits (`id_pe_mes`) | 53,632 |
| Remeasured plots (>1 visit) | 12,611 (98.26%) |
| Single-visit plots | 223 |
| Maximum visits per plot | 7 |
| Measurement period | 1970-05-10 to 2025-10-02 |
| Measurement years | 1970–2025 |

Visits per plot:

| Visits | Plots |
|---:|---:|
| 1 | 223 |
| 2 | 459 |
| 3 | 3,503 |
| 4 | 2,324 |
| 5 | 5,276 |
| 6 | 1,037 |
| 7 | 12 |

Plots by network (`placette.reseau`):

| Network | Plots | Description |
|---|---:|---|
| BAS1 | 7,523 | First base network, established 1970–1977; representative of the covered forest |
| BAS2 | 3,046 | Second base network, from 1989; incomplete implementation |
| SPIM | 1,132 | Insect and disease protection service |
| FEDE | 650 | Québec wood-producer federation (private forest) |
| UNLA | 236 | Targeted network |
| SCOF | 158 | Forest accounting service |
| PACA | 89 | Parks Canada |

`plan_reseau` reports 12,353 initial plots, 535 abandoned, 481 re-established,
104 deferred, and 12,195 active plots across all networks.

## 3. Measurement intervals

40,798 consecutive-visit intervals; median 11.05 years, mean 11.15 years,
5th–95th percentile 5.94–17.11 years.

| Interval (years) | Intervals |
|---|---:|
| <1 | 2 |
| 1–2 | 2 |
| 2–3 | 6 |
| 3–4 | 14 |
| 4–5 | 785 |
| 5–6 | 1,497 |
| 6–8 | 6,255 |
| 8–10 | 6,321 |
| 10–12 | 10,112 |
| 12–15 | 10,896 |
| 15–20 | 4,396 |
| 20–25 | 459 |
| 25–30 | 23 |
| 30–40 | 30 |

Median interval by network: BAS1 11.01, BAS2 12.01, FEDE 11.03, PACA 10.89,
SCOF 11.25, SPIM 11.07, UNLA 5.00 years.

## 4. Tree tallies and identity

| Measure | Value |
|---|---:|
| Tally-tree rows (`dendro_arbres`) | 2,210,417 |
| Plots with tally trees | 12,815 |
| Distinct measurements (`id_arb_mes`) | 2,210,417 |
| Unique trees (`id_arbre`) | 843,175 |
| Trees measured on >1 visit | 683,328 (81.04%) |
| Sapling rows (`dendro_gaules`) | 235,455 |
| Plots with sapling tallies | 12,702 |

`id_arbre` is constructed from `id_pe` plus a zero-padded tree number and is
stable across visits; `id_arb_mes` appends the measurement number and is
unique. Tree identity therefore persists across visits, subject to the
`etat` renumbering codes (50–56) and terminal states.

## 5. DBH and live/dead status

DBH `dhp` is in millimetres and is populated for 1,872,255 of 2,210,417 tally
rows (84.70%). Overall min/median/max: 0 / 133 / 1,089 mm. The 0 values are
concentrated in dead, removed, and regeneration rows; live tally trees start
at 77 mm.

Status groups derived from `etat` and the `ETAT` dictionary:

| Group | Codes | Rows | DBH non-null | DBH median (mm) |
|---|---|---:|---:|---:|
| Live | 10, 12, 30, 40, 42, 50, 52, 58 | 1,660,115 | 1,660,111 | 136 |
| Dead | 14–18, 20–24, 29, 34–36, 44–46, 54–56, 68, 78, 88, 98 | 346,589 | 143,543 | 134 |
| Removed / intruder | 25, 26 | 107,073 | 31 | — |
| Sapling state codes | GA, GM, GV | 27,842 | 2 | — |
| Missing `etat` | — | 68,723 | 68,493 | 61 |
| Other | 32 | 75 | 75 | 141 |

Live tally DBH: min 77 mm, median 136 mm, max 1,089 mm. Dead tally DBH
(non-null): 0–990 mm, median 134 mm.

## 6. Height, age, and site productivity

Height and age are measured on the study-tree subsample:

| Measure | Rows | Percent of study rows | Unique trees |
|---|---:|---:|---:|
| Study-tree measurements | 442,560 | 100% | 193,463 |
| Total height `haut_arbre` | 372,225 | 84.11% | 193,420 (99.98% of study trees) |
| Age `age` | 303,233 | 68.52% | 157,394 |
| Tally height `hauteurdef` | 43,559 | 1.97% of tally rows | — |

Of all 843,175 unique tally trees, 415,108 (49.23%) have at least one total
height in either the tally or study table. Age range 1–368 years, median
59 years.

Site productivity is not stored as a site-index column. Available proxies:

| Field | Table | Populated | Coverage |
|---|---|---:|---:|
| Dominant height `haut_domi` | `station_pe` | 11,247 | 20.97% of visits |
| Age class `cl_age` | `station_pe` | 35,613 | 66.40% of visits |
| Potential vegetation `veg_pot` | `station_pe` | 32,592 | 60.77% of visits (43 classes) |
| Ecological type `type_eco` | `station_pe` | 29,627 | 55.24% of visits (272 classes) |
| Ecological classification | `classi_eco_pe` | 12,834 | 100% of plots |

`classi_eco_pe` fully populates `zone_veg` (2 classes), `dom_bio` (8),
`reg_eco` (51), and `dis_eco` (1,926); `eta_veg` is populated for 5,257 plots
(41.0%) and has four classes (`Moyen` 4,606; `Supérieur` 422; `Inférieur`
201; `Montagnard` 28). Site index must be derived from age/height or from an
external model.

## 7. Species

64 species codes occur in the tally-tree table and 80 in the sapling table;
the union is 86 codes. Top 15 tally species:

| Code | Species | Tally rows |
|---|---|---:|
| SAB | Sapin baumier | 509,854 |
| EPN | Épinette noire | 495,125 |
| BOP | Bouleau à papier (blanc) | 179,465 |
| ERS | Érable à sucre | 97,283 |
| ERR | Érable rouge | 92,375 |
| PIG | Pin gris | 82,534 |
| PET | Peuplier faux-tremble | 76,898 |
| EPB | Épinette blanche | 64,155 |
| BOJ | Bouleau jaune | 48,700 |
| THO | Thuya occidental | 47,115 |
| HEG | Hêtre à grandes feuilles | 19,991 |
| PRP | Cerisier de Pennsylvanie | 16,128 |
| EPR | Épinette rouge | 15,229 |
| PRU | Pruche de l'Est | 11,838 |
| PIB | Pin blanc | 11,515 |

Top sapling species are the same dominant conifers: SAB 63,016, EPN 45,140,
BOP 21,305, ERR 13,602, ERS 11,665, ERE 9,136, EPB 5,988, PET 5,933,
AUR 5,073, BOJ 4,706.

## 8. Plot design and expansion factors

PEP uses fixed-area circular plots; there is no BAF.

| Dimension code | Visits | Design components (`plan_descr_type_pe`) | Area (m²) | Expansion (stems/ha) |
|---|---:|---|---:|---:|
| 04 | 30,069 | 3 | 4, 40, 400 | 2,500 / 250 / 25 |
| 10 | 12,977 | 5 | 4, 40, 400, 625 | 2,500 / 250 / 25 / 16 |
| 20 | 10,586 | 5 | 4, 40, 400, 625 | 2,500 / 250 / 25 / 16 |

`plan_descr_type_pe` lists 13 design components with plots of 4, 40, 400,
and 625 m² and expansion factors 2,500, 250, 25, and 16 stems/ha.
`dendro_arbres.tige_ha` stores the applied expansion (25 for 400 m², 250 for
40 m², 16 for 625 m²); `st_ha` stores per-tree basal area per hectare. Both
are populated for 1,872,097 tally rows. 338,320 tally rows lack `tige_ha`,
corresponding mainly to dead/removed trees and non-tally states.

## 9. Interpretation cautions

- The database is a network mosaic, not a single equal-probability sample.
  `BAS1` is the only network described as representative of the full covered
  forest; `BAS2` is incomplete; `FEDE` represents only some private-forest
  syndicate territories; the remaining networks are targeted.
- `etat` is a state machine, not a binary live/dead flag. Recruits (40–46),
  renumbered trees (50–56), remnants (58–98), and cut/intruder codes (25, 26)
  need explicit handling before growth analysis. The grouping in §5 is a
  documented convenience, not an upstream classification.
- Dead and removed rows often have DBH 0 or missing; height is measured on a
  subsample. Do not treat missing DBH or height as random.
- Coordinates are present for all 12,834 plots in `placette.latitude` /
  `longitude`; geometry is EPSG:32198.
