# BC forest and THLB area weights

Generated 2026-11-17T08:52:33+00:00.
Runtime: 123.8 s.

## Source and filter

- Polygon source: `BC VRI 2025 R1 VEG_COMP_LYR_R1_POLY` (EPSG:3005).
- Vintage: 2025.
- Filter: FOR_MGMT_LAND_BASE_IND = 'Y' (Crown management land base) AND BCLCS_LEVEL_1 = 'V' (vegetated) AND BCLCS_LEVEL_2 = 'T' (treed); polygon area = POLYGON_AREA (ha), validated against FEATURE_AREA_SQM/10000.
- Species: `SPECIES_CD_1..6` allocated by normalised `SPECIES_PCT_1..6`; crosswalk `bc_species_codes` -> `casfri_species_codes` -> RSYC dotted code.
- THLB: `misc.thlb.tif` sampled at each polygon label point; `thlb_area_ha = area_ha * percent / 100`.
- Spatial labels: 500 m rasterisation of current FADM TSA features and RSYC ecoregions (EPSG:3005).

## Row counts

- VRI polygons passing the filter and read: 5,057,731.
- Polygons used (positive area and species): 5,008,837.
- Polygons with zero species percentage: 45,647 (550,982 ha excluded).
- Aggregated area rows: 2,266.

## Totals

- Forest area: 56,428,146 ha.
- THLB area: 18,653,774 ha.
- THLB share: 33.1%.
- THLB raster valid pixels: 32.6% of the grid; raster total THLB: 20,032,336 ha.  The polygon-sampled total is a subset of that raster total.
- Polygons with no THLB attribution (nodata/out-of-range): 559,917 (4,953,977 ha treated as zero THLB).

### By ecoprovince

| Ecoprovince | Forest ha | THLB ha | THLB share |
|---|---|---|---|
| Northern Montane Cordillera | 9,573,421 | 4,426,792 | 46.2% |
| Columbia Montane Cordillera | 9,460,156 | 3,021,930 | 31.9% |
| Southern Coastal Mountains | 8,756,244 | 1,540,284 | 17.6% |
| Central Montane Cordillera | 7,297,621 | 4,006,627 | 54.9% |
| Southern Boreal Cordillera | 6,417,722 | 589,308 | 9.2% |
| Hay-Slave Lowlands | 4,424,001 | 1,250,624 | 28.3% |
| Southern Montane Cordillera | 4,261,536 | 2,207,188 | 51.8% |
| Boreal Foothills | 2,202,612 | 851,738 | 38.7% |
| Northern Boreal Cordillera | 1,923,020 | 356,886 | 18.6% |
| Georgia Depression | 908,842 | 163,275 | 18.0% |
| Central Boreal Plains | 608,840 | 216,451 | 35.6% |
| Northern Coastal Mountains | 538,732 | 22,652 | 4.2% |
| Wrangel Mountains | 53,061 | 0 | 0.0% |
| NO_ECOPROVINCE | 2,337 | 18 | 0.8% |

## Unmapped species

- Area with no RSYC species target: 11,007,317 ha (19.5% of forest area).

| BC code | Area ha |
|---|---|
| SX | 7,740,081 |
| S | 1,103,415 |
| YC | 704,155 |
| H | 581,589 |
| B | 459,529 |
| ACT | 144,925 |
| PA | 111,652 |
| LA | 52,011 |
| E | 43,362 |
| PW | 35,137 |
| L | 11,129 |
| BG | 7,040 |
| RA | 3,988 |
| EA | 2,699 |
| VB | 2,092 |
| W | 896 |
| QG | 672 |
| AX | 405 |
| BP | 393 |
| X | 319 |

## National batch join

- BC-relevant cells: 429; matched: 192; no area: 237.
- No-area cells: 237; species with no area anywhere in BC: ACER.RUB, ACER.SAH, BETU.ALL, BROADLEAF, CONIFEROUS, FRAX.NIG, PICE.RUB, PINU.STR, POPU.GRA, QUER.RUB, THUJ.OCC.
- Joined log volume: 8,936,253,982 m3; residue: 1,969,094,147 m3 / 722,691,931 odt; taper total: 10,905,348,129 m3.

### BC totals by species

| Species | Log m3 | Residue m3 | Residue odt | Taper m3 |
|---|---|---|---|---|
| ABIE.AMA | 360,663,032 | 31,773,434 | 11,115,713 | 392,436,465 |
| ABIE.BAL | 21,373 | 2,470 | 864 | 23,843 |
| ABIE.LAS | 1,313,115,371 | 408,962,046 | 126,695,215 | 1,722,077,416 |
| ACER.MAC | 14,101,937 | 371,804 | 130,073 | 14,473,741 |
| ALNU.RUB | 52,051,509 | 5,987,037 | 2,094,523 | 58,038,546 |
| BETU.PAP | 74,097,019 | 25,216,579 | 12,097,729 | 99,313,597 |
| LARI.LAR | 24,989,436 | 5,172,250 | 2,481,403 | 30,161,686 |
| LARI.OCC | 238,487,324 | 8,933,138 | 4,285,700 | 247,420,462 |
| PICE.ABI | 1,956 | 510 | 183 | 2,466 |
| PICE.ENG | 626,858,571 | 45,226,176 | 14,916,497 | 672,084,747 |
| PICE.GLA | 294,273,666 | 42,083,963 | 15,140,758 | 336,357,629 |
| PICE.MAR | 192,562,424 | 155,843,640 | 59,189,103 | 348,406,065 |
| PICE.SIT | 118,482,259 | 3,706,383 | 1,222,439 | 122,188,642 |
| PINU.BAN | 17,189 | 19,511 | 7,410 | 36,700 |
| PINU.CON | 1,371,399,757 | 645,030,735 | 244,981,383 | 2,016,430,492 |
| PINU.PON | 31,712,561 | 1,682,472 | 638,999 | 33,395,033 |
| PINU.RES | 30,499 | 973 | 370 | 31,472 |
| POPU.BAL | 84,615,736 | 11,150,882 | 3,454,510 | 95,766,618 |
| POPU.TRE | 608,847,373 | 228,232,016 | 79,845,373 | 837,079,389 |
| PSEU.MEN | 1,447,689,409 | 130,434,954 | 58,669,381 | 1,578,124,363 |
| THUJ.PLI | 657,780,448 | 57,539,276 | 17,825,495 | 715,319,725 |
| TSUG.HET | 1,331,245,089 | 148,934,208 | 62,529,134 | 1,480,179,297 |
| TSUG.MER | 93,210,044 | 12,789,692 | 5,369,676 | 105,999,736 |

## Validation and caveats

- Total forest area 56,428,146 ha and THLB 18,653,774 ha are reported as computed.  Working order-of-magnitude references are roughly 50-60 million ha of BC forest land base and 20-25 million ha of THLB; these are checks, not calibration targets.
- `UNMAPPED_BC` is not redistributed.  Hybrid spruce (`SX`), paper birch (`EA`), and other codes whose CASFRI target has no RSYC species remain explicit gaps.
- `LAND_COVER_CLASS_CD_1` was inspected but is null for roughly a quarter of treed polygons in this release; `BCLCS_LEVEL_2 = 'T'` is the reliable treed discriminator and is used in the filter.
- The 500 m TSA/ecoregion label raster is an approximation.  It is used only to assign polygon labels; area and THLB come from the polygon and the 1 ha THLB raster.
- Cross-border ecoprovinces (Boreal Cordillera, Boreal Plains, Taiga Plains) receive BC-only area.  Joined totals are BC partials, not full ecoprovince supply.
- The batch matrix contains `total` and `residue` streams that duplicate log totals.  Only `log` rows are summed for product volumes, and only `residue` rows for residue.

## Gaps and next steps

- TSA label gaps: 739,372 ha. Ecoregion gaps: 2,337 ha.
- Add documented aliases for unresolved BC commercial codes after review; do not silently fold them into a species.
- THLB nodata is dominated by forest outside the raster's TSA coverage (parks, private land, and other non-TSA tenure); it is kept at zero, not imputed from a TSA mean.
- Replace the 500 m label raster with exact polygon assignment if the FADM TSA geometry repair is completed.
