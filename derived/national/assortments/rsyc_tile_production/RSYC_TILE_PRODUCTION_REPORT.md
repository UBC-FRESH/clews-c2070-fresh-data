# Tile-level RSYC production curve library

**Status:** generated artefact; diagnostic, not wired into the national batch.
**Generated:** 2026-11-18T18:35:23.414245+00:00. **Commit:** none.

## 1. Method

- Overlay: exact polygon intersection of the 385 published RSYC
  tiles and the 672 RSYC ecodistricts in EPSG:3978
  (Canada Atlas Lambert, metres). No centroid or representative-point
  assignment is used.
- Province overlay: each tile x ecodistrict piece is split by the 13 province
  polygons from `canada_adm1_geoboundaries_simplified.geojson`; the area is the
  exact polygon intersection. 2 invalid
  province polygons were repaired with `make_valid` before intersection.
- Area allocation: `tile x province species area = sum(scanfi district x
  province species area x fraction_of_district_province)`. Fractions are
  normalised within each district x province and within the published 385-tile
  footprint. Source rows whose province has no geographic intersection with
  any tile in the district use an explicit district fallback and are reported
  separately; they are never silently assigned to a province.
- Curve selection: tile exact species, tile species group
  (`coniferous`/`broadleaf`), tile `generic`, then the tile's dominant
  ecoregion/ecoprovince control curve. Only national, published, converged
  volume curves are eligible. Ecodistrict curves are not used for production.
- No benchmark correction factor is applied.

## 2. Tile x ecodistrict intersection

| Metric | Value |
|---|---:|
| Tiles | 385 |
| Ecodistricts | 672 |
| Intersection rows | 2,370 |
| Tiles touched | 385 |
| Ecodistricts touched | 672 |
| Total intersection area (ha) | 691,220,890.0605 |
| Tile layer area (ha) | 866,250,000.0000 |
| Ecodistrict layer area (ha) | 692,081,504.5642 |
| Intersection as share of tile area | 79.7946% |
| Intersection as share of ecodistrict area | 99.8756% |
| Tile area outside ecodistricts (ha) | 175,029,109.9395 |
| Ecodistrict area outside tiles (ha) | 860,614.5037 |
| Minimum intersection area (ha) | 0.019679 |
| Zero-area boundary contacts skipped | 0 |
| Non-polygonal parts coerced | 0 |
| Province polygons | 13 |
| Tile x ecodistrict x province rows | 2,642 |
| District x province pairs | 831 |
| Province share of tile x ecodistrict area | 93.6753% |
| Tile x ecodistrict area outside province polygons (ha) | 43,667,304.3738 |
| Province boundary-only contacts skipped | 0 |

The intersection is the forested-ecozone portion of the tile grid:
79.79% of the tile layer
area, because the RSYC ecological layers contain forested ecozones only. The
area accounting closes exactly: the pairwise intersection equals the union
intersection, and tile and ecodistrict areas each equal the intersection plus
their outside part (see §5).

Province polygons cover
93.6753% of the tile x
ecodistrict area. The remaining
43,667,304.3738 ha is coastal, offshore, or
simplified-boundary area outside the province polygons; it is retained as a
reported geometric gap and never assigned to a province. Province attribution
does not rely on this gap: SCANFI forest blocks are allocated only through
positive province intersections, except for the explicitly reported
nearest-fill fallback below.

### Partial tile coverage

`fraction_of_ecodistrict` sums to 1 for every ecodistrict after normalisation.
Raw coverage is below 1 for 10
edge ecodistricts, with
860,614.5037 ha of ecodistrict area
outside the published tile grid. Their SCANFI area
(73,055.1849 ha,
0.017292% of the national total)
is redistributed proportionally over the covered tiles, not dropped.

| ecodistrict_id | ecodistrict | ecodistrict_area_ha | covered_area_ha | covered_fraction |
|---|---|---|---|---|
| 297 | La Baleine Coastal Plain | 1,393,747.1122 | 770,646.3366 | 0.5529 |
| 516 | Atlantic | 3,051,895.1466 | 2,945,409.8169 | 0.9651 |
| 471 | Northeastern Barrens | 1,204,726.6799 | 1,168,045.7758 | 0.9696 |
| 477 | Oceanic Barrens | 1,318,427.2814 | 1,278,800.3299 | 0.9699 |
| 1,021 | York Factory | 2,924,365.2585 | 2,895,019.7736 | 0.9900 |
| 404 | Dog River | 2,203,127.5574 | 2,181,238.9454 | 0.9901 |
| 411 | Nipissing | 2,631,392.3790 | 2,628,737.8354 | 0.9990 |
| 302 | Port-Nouveau Québec Coast | 711,196.0093 | 710,821.9987 | 0.9995 |
| 937 | Alask Ranges | 255,162.6548 | 255,060.2551 | 0.9996 |
| 319 | Harbour | 1,082,797.7515 | 1,082,481.0241 | 0.9997 |

## 3. Curve selection and species coverage

| Evidence tier | Cells | Area (ha) | Area share |
|---|---:|---:|---:|
| `rsyc_tile_exact` | 1,143 | 252,102,763.5110 | 59.6727% |
| `rsyc_tile_generic` | 213 | 5,564,438.9728 | 1.3171% |
| `rsyc_tile_group` | 2,592 | 164,808,559.0386 | 39.0102% |

Total library cells: **3,948** across
**385** tiles, **12**
species targets, and **13** provinces.
Control-fallback cells: **0**; negative
`b4` published fits flagged: **872**.

### By species

| species | cells | area_ha | exact_pct | group_pct | generic_pct | fallback_pct |
|---|---|---|---|---|---|---|
| PICE.MAR | 547 | 153,682,120.5158 | 99.7235 | 0.2765 | 0.0000 | 0.0000 |
| BROADLEAF | 555 | 82,649,859.9346 | 0.0000 | 93.2675 | 6.7325 | 0.0000 |
| PINU.BAN | 500 | 39,126,191.3721 | 89.9230 | 10.0770 | 0.0000 | 0.0000 |
| PICE.GLA | 474 | 39,033,902.5193 | 61.0503 | 38.9497 | 0.0000 | 0.0000 |
| CONIFEROUS | 110 | 34,616,820.4681 | 0.0000 | 100.0000 | 0.0000 | 0.0000 |
| LARI.LAR | 547 | 27,150,318.0688 | 0.0000 | 100.0000 | 0.0000 | 0.0000 |
| PINU.CON | 277 | 21,195,759.2992 | 96.9090 | 3.0910 | 0.0000 | 0.0000 |
| ABIE.BAL | 460 | 17,465,104.9793 | 74.7517 | 25.2483 | 0.0000 | 0.0000 |
| PSEU.MEN | 81 | 5,293,792.9949 | 95.5679 | 4.4321 | 0.0000 | 0.0000 |
| PINU.RES | 179 | 1,025,102.4655 | 33.1933 | 66.8067 | 0.0000 | 0.0000 |
| PINU.STR | 179 | 1,025,102.4655 | 76.1432 | 23.8568 | 0.0000 | 0.0000 |
| PINU.PON | 39 | 211,686.4393 | 26.3609 | 73.6391 | 0.0000 | 0.0000 |

## 4. Area reconciliation and province table

| Metric | Area (ha) |
|---|---:|
| SCANFI ecodistrict source total | 422,475,761.5224 |
| Allocated tile x province x species total | 422,475,761.5224 |
| Difference | 0.000000060 |
| SCANFI area redistributed to covered tiles | 73,055.1849 |
| Redistributed share of national area | 0.017292% |
| Positive source rows | 5,800 |
| Zero-area source rows excluded | 0 |
| Tile x province x species cells | 3,948 |
| Province-intersection allocation | 422,319,381.6623 |
| Nearest-fill area with no province intersection | 156,379.8601 |
| No-intersection share of national area | 0.037015% |
| District x province x species groups | 5,800 |
| Maximum district x province x species closure error (ha) | 0.000000000 |
| Maximum province area reconciliation error (ha) | 0.000000000 |

`12` ecodistricts
carry more SCANFI forest area than their polygon area (maximum ratio
2.2497); the area
weights use 990 m blocks with nearest-unit fill. This propagates to
**1**
tile(s). `B25` has
1.2163x
its polygon area, an excess of
486,706.2072
ha. The overlay is exact; the excess is inherited from the SCANFI area layer,
not from double-counted intersection. It is reported, not capped, because
capping would break the SCANFI total reconciliation.

### Allocation basis

| allocation_basis | cells | area_ha | area_share_pct |
|---|---|---|---|
| district_fallback_no_province_intersection | 169 | 99,475.2300 | 0.0235 |
| mixed_province_intersection_and_district_fallback | 85 | 2,757,637.2462 | 0.6527 |
| province_intersection | 3,694 | 419,618,649.0462 | 99.3237 |

### Nearest-fill area with no valid geographic intersection

| ecodistrict_id | ecodistrict | province | target_species | area_ha | reason |
|---|---|---|---|---|---|
| 192 | MacKenzie Delta West | YT | BROADLEAF | 0.3512 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 192 | MacKenzie Delta West | YT | LARI.LAR | 1.2197 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 192 | MacKenzie Delta West | YT | PICE.GLA | 0.1088 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 192 | MacKenzie Delta West | YT | PICE.MAR | 3.5000 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 192 | MacKenzie Delta West | YT | PINU.CON | 0.1303 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 202 | Deese Arm | NU | BROADLEAF | 301.1645 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 202 | Deese Arm | NU | LARI.LAR | 165.6009 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 202 | Deese Arm | NU | PICE.GLA | 383.6007 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 202 | Deese Arm | NU | PICE.MAR | 842.6831 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 202 | Deese Arm | NU | PINU.CON | 0.7508 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 214 | Aubry Lake | NU | BROADLEAF | 6.8466 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 214 | Aubry Lake | NU | LARI.LAR | 19.3058 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 214 | Aubry Lake | NU | PICE.GLA | 5.0218 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 214 | Aubry Lake | NU | PICE.MAR | 70.6768 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 214 | Aubry Lake | NU | PINU.CON | 0.0290 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 258 | Walmesley - Warburton | NU | BROADLEAF | 172.7283 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 258 | Walmesley - Warburton | NU | LARI.LAR | 7,238.3525 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 258 | Walmesley - Warburton | NU | PICE.GLA | 5,826.1929 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 258 | Walmesley - Warburton | NU | PICE.MAR | 42,517.4996 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 258 | Walmesley - Warburton | NU | PINU.BAN | 362.4001 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 258 | Walmesley - Warburton | NU | PINU.CON | 34.9066 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 259 | Whitefish Lake | NU | BROADLEAF | 4.3218 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 259 | Whitefish Lake | NU | LARI.LAR | 42.9667 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 259 | Whitefish Lake | NU | PICE.GLA | 110.0189 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 259 | Whitefish Lake | NU | PICE.MAR | 351.7163 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 259 | Whitefish Lake | NU | PINU.BAN | 2.8964 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 266 | Beaverhill Lake | NU | BROADLEAF | 5.4518 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 266 | Beaverhill Lake | NU | LARI.LAR | 11.5364 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 266 | Beaverhill Lake | NU | PICE.GLA | 6.6039 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 266 | Beaverhill Lake | NU | PICE.MAR | 79.6112 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 266 | Beaverhill Lake | NU | PINU.BAN | 0.9268 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 298 | Lac aux Feuilles Hills | NU | ABIE.BAL | 7.7600 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 298 | Lac aux Feuilles Hills | NU | BROADLEAF | 3,247.5266 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 298 | Lac aux Feuilles Hills | NU | LARI.LAR | 6,839.3716 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 298 | Lac aux Feuilles Hills | NU | PICE.GLA | 922.9189 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 298 | Lac aux Feuilles Hills | NU | PICE.MAR | 8,970.6791 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 298 | Lac aux Feuilles Hills | NU | PINU.BAN | 1.6883 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 298 | Lac aux Feuilles Hills | NU | PINU.CON | 0.0453 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 302 | Port-Nouveau Québec Coast | NL | ABIE.BAL | 409.9687 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 302 | Port-Nouveau Québec Coast | NL | BROADLEAF | 56.6618 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 302 | Port-Nouveau Québec Coast | NL | LARI.LAR | 164.8411 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 302 | Port-Nouveau Québec Coast | NL | PICE.GLA | 347.5647 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 302 | Port-Nouveau Québec Coast | NL | PICE.MAR | 2,390.8728 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 302 | Port-Nouveau Québec Coast | NL | PINU.BAN | 161.0608 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 303 | George River Lower Plateau | NL | ABIE.BAL | 399.9565 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 303 | George River Lower Plateau | NL | BROADLEAF | 64.7108 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 303 | George River Lower Plateau | NL | LARI.LAR | 188.0590 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 303 | George River Lower Plateau | NL | PICE.GLA | 748.8779 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 303 | George River Lower Plateau | NL | PICE.MAR | 2,097.3413 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 303 | George River Lower Plateau | NL | PINU.BAN | 122.3846 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 304 | George Rriver Upper Plateau | NL | ABIE.BAL | 40.4716 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 304 | George Rriver Upper Plateau | NL | BROADLEAF | 9.5664 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 304 | George Rriver Upper Plateau | NL | LARI.LAR | 12.8990 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 304 | George Rriver Upper Plateau | NL | PICE.GLA | 108.0783 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 304 | George Rriver Upper Plateau | NL | PICE.MAR | 284.8565 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 304 | George Rriver Upper Plateau | NL | PINU.BAN | 30.3082 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 305 | Central Ranges | QC | BROADLEAF | 0.0065 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 305 | Central Ranges | QC | LARI.LAR | 0.1018 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 305 | Central Ranges | QC | PICE.GLA | 0.1385 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 305 | Central Ranges | QC | PICE.MAR | 1.2190 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 305 | Central Ranges | QC | PINU.BAN | 0.1542 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 509 | North Mountain | NB | ABIE.BAL | 0.0139 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 509 | North Mountain | NB | BROADLEAF | 0.0746 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 509 | North Mountain | NB | CONIFEROUS | 0.1163 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 509 | North Mountain | NB | LARI.LAR | 0.2086 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 509 | North Mountain | NB | PINU.BAN | 0.0367 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 695 | Turtle River Plain | AB | ABIE.BAL | 1.9336 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 695 | Turtle River Plain | AB | BROADLEAF | 41,511.2056 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 695 | Turtle River Plain | AB | LARI.LAR | 125.7593 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 695 | Turtle River Plain | AB | PICE.GLA | 1,186.9690 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 695 | Turtle River Plain | AB | PICE.MAR | 84.3501 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 695 | Turtle River Plain | AB | PINU.BAN | 113.0932 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 695 | Turtle River Plain | AB | PINU.CON | 6.3193 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 857 | Babbage River | NT | BROADLEAF | 16.9616 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 857 | Babbage River | NT | LARI.LAR | 4.2677 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 857 | Babbage River | NT | PICE.GLA | 19.6771 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 857 | Babbage River | NT | PICE.MAR | 12.1523 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 857 | Babbage River | NT | PINU.BAN | 0.4913 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | ABIE.BAL | 659.6127 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | BROADLEAF | 15,679.6063 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | CONIFEROUS | 6,283.7637 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | LARI.LAR | 21.1164 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | PICE.MAR | 4.3400 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | PINU.BAN | 36.4518 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | PINU.CON | 4,410.7480 | province has no geographic intersection with any tile in this district; district-wide tile share used |
| 1,018 | Blairmore Foothills | SK | PSEU.MEN | 1.3811 | province has no geographic intersection with any tile in this district; district-wide tile share used |

These rows are allocated with the district-wide tile share because the
province label has no positive intersection with any tile in the district.
They are flagged in the library by `allocation_basis` and
`no_province_intersection_area_ha`; they are not treated as spatially
constrained province attribution.

### Province table

| province | cells | area_ha | area_share_pct | exact_pct | group_pct | generic_pct | fallback_pct |
|---|---|---|---|---|---|---|---|
| QC | 674 | 81,663,538.5592 | 19.3298 | 64.2601 | 34.9905 | 0.7494 | 0.0000 |
| ON | 470 | 68,517,060.2271 | 16.2180 | 54.5813 | 44.8150 | 0.6038 | 0.0000 |
| BC | 485 | 66,607,737.0507 | 15.7660 | 43.4616 | 55.9287 | 0.6097 | 0.0000 |
| NT | 434 | 43,460,564.1586 | 10.2871 | 67.4558 | 30.6845 | 1.8597 | 0.0000 |
| AB | 300 | 38,345,566.4687 | 9.0764 | 54.5342 | 45.4658 | 0.0000 | 0.0000 |
| MB | 285 | 33,753,909.9768 | 7.9895 | 65.6434 | 32.8849 | 1.4717 | 0.0000 |
| SK | 225 | 26,160,931.2754 | 6.1923 | 66.2031 | 33.3561 | 0.4409 | 0.0000 |
| YT | 260 | 25,905,742.5886 | 6.1319 | 76.9146 | 17.3249 | 5.7605 | 0.0000 |
| NL | 265 | 23,531,836.3298 | 5.5700 | 78.2792 | 16.9479 | 4.7729 | 0.0000 |
| NB | 88 | 6,692,497.6592 | 1.5841 | 36.0764 | 63.9236 | 0.0000 | 0.0000 |
| NS | 80 | 4,727,696.9422 | 1.1190 | 23.7256 | 76.2744 | 0.0000 | 0.0000 |
| NU | 334 | 2,834,208.4557 | 0.6709 | 57.9696 | 38.6127 | 3.4176 | 0.0000 |
| PE | 48 | 274,471.8303 | 0.0650 | 18.1767 | 81.8233 | 0.0000 | 0.0000 |

### Province attribution change versus the district-wide allocation

National province totals are unchanged because each district x province x species
source row still closes to its own province; what changes is which tile receives
the area. 672
tile x province cells move by more than 0.001 ha; the maximum
absolute move is 976,472.0789 ha.

| tile_id | province | legacy_area_ha | constrained_area_ha | difference_ha |
|---|---|---|---|---|
| D23 | ON | 1,032,372.2023 | 2,008,844.2812 | 976,472.0789 |
| D23 | QC | 894,476.0059 | 0.0000 | -894,476.0059 |
| G30 | QC | 1,208,672.0409 | 433,174.6846 | -775,497.3563 |
| L8 | AB | 1,047,778.0616 | 1,765,337.7162 | 717,559.6546 |
| E23 | ON | 1,107,466.5872 | 1,798,558.6727 | 691,092.0854 |
| F17 | ON | 1,125,020.8005 | 1,784,314.0938 | 659,293.2932 |
| F17 | MB | 659,125.3096 | 25,630.0398 | -633,495.2698 |
| L8 | BC | 583,310.5976 | 0.0000 | -583,310.5976 |
| F23 | ON | 973,699.5606 | 399,369.8916 | -574,329.6690 |
| I17 | MB | 417,310.3458 | 989,792.6170 | 572,482.2712 |

B25 province split (legacy district-wide -> province-constrained):
| tile_id | province | legacy_area_ha | constrained_area_ha | difference_ha |
|---|---|---|---|---|
| B25 | ON | 2,177,791.7814 | 2,292,578.1142 | 114,786.3328 |
| B25 | QC | 449,158.5501 | 444,128.0930 | -5,030.4571 |

## 5. Validation

Validation summary: **PASS**.

| check | passed | detail |
|---|---|---|
| tile_layer_has_no_overlaps | PASS | {'sum_feature_area_minus_union_area_ha': 0.0} |
| ecodistrict_layer_has_no_overlaps | PASS | {'sum_feature_area_minus_union_area_ha': 4.172325134277344e-06} |
| pairwise_intersection_equals_union_intersection | PASS | {'pair_area_ha': 691220890.0605261, 'union_intersection_ha': 691220890.0605223, 'abs_error_ha': 3.814697265625e-06} |
| tile_area_closes_with_intersection_and_outside_part | PASS | {'tile_area_ha': 866250000.0, 'intersection_plus_tile_only_ha': 866249999.9999995, 'abs_error_ha': 4.76837158203125e-07} |
| ecodistrict_area_closes_with_intersection_and_outside_part | PASS | {'ecodistrict_area_ha': 692081504.5642028, 'intersection_plus_ecodistrict_only_ha': 692081504.5641987, 'abs_error_ha': 4.0531158447265625e-06} |
| union_area_closes_with_three_components | PASS | {'union_area_ha': 867110614.5036722, 'components_ha': 867110614.5036721, 'abs_error_ha': 1.1920928955078125e-07} |
| ecodistrict_fractions_sum_to_one | PASS | {'max_abs_deviation': 2.220446049250313e-16} |
| raw_ecodistrict_fractions_sum_to_covered_fraction | PASS | {'max_abs_deviation': 2.220446049250313e-16} |
| tile_fractions_do_not_exceed_one | PASS | {'max_tile_fraction_sum': 1.000000000000001} |
| no_duplicate_tile_ecodistrict_pairs | PASS | {'duplicates': 0} |
| all_intersection_areas_positive | PASS | {'min_intersection_area_ha': 0.019678794098820635} |
| all_intersection_geometries_polygonal | PASS | {'geometry_types': ['MultiPolygon', 'Polygon']} |
| province_layer_has_no_overlaps | PASS | {'sum_feature_area_minus_union_area_ha': -2.86102294921875e-06} |
| province_district_fractions_sum_to_one | PASS | {'max_abs_deviation': 2.220446049250313e-16} |
| province_tile_fractions_do_not_exceed_one | PASS | {'max_tile_fraction_sum': 1.000000000000002} |
| province_intersections_are_polygonal_and_positive | PASS | {'min_intersection_area_ha': 0.9773301779606569} |
| province_cover_share_recorded | PASS | {'province_cover_share_of_intersection': 0.9367534352652593, 'note': 'coastal and offshore tile/ecodistrict area is outside simplified province polygons'} |
| every_positive_tile_species_cell_has_a_curve | PASS | {'cells': 3948, 'missing': 0} |
| library_area_equals_tile_species_area | PASS | {'library_area_ha': 422475761.5224368, 'tile_species_area_ha': 422475761.5224368, 'abs_difference_ha': 0.0} |
| library_area_reconciles_to_scanfi | PASS | {'library_area_ha': 422475761.5224368, 'scanfi_area_ha': 422475761.52243674, 'abs_difference_ha': 5.960464477539063e-08} |
| source_keys_are_complete_and_canonical | PASS | {'blank_keys': 0, 'cell_key_mismatches': 0} |
| no_duplicate_library_cells | PASS | {'duplicate_cell_keys': 0, 'duplicate_tile_province_species': 0} |
| all_numeric_values_finite | PASS | {'non_finite_values': 0, 'columns_with_nan': []} |
| all_areas_strictly_positive | PASS | {'non_positive_cells': 0} |
| b1_b2_b3_strictly_positive_b4_finite | PASS | {'non_positive_coefficients': 0} |
| predictions_finite_and_non_negative | PASS | {'ages': [50.0, 100.0, 150.0], 'invalid_predictions': 0} |
| negative_b4_is_flagged_not_dropped | PASS | {'negative_b4': 872, 'flagged': 872} |
| province_area_sums_reconcile_to_source | PASS | {'max_abs_difference_ha': 0.0, 'extra_provinces': []} |
| species_area_sums_reconcile_to_source | PASS | {'max_abs_difference_ha': 1.1641532182693481e-10, 'species': 12} |
| district_province_species_allocation_closes | PASS | {'groups': 5800, 'max_abs_error_ha': 4.656612873077393e-10} |
| no_province_intersection_area_is_reported | PASS | {'fallback_area_ha': 156379.86011338176, 'reported_fallback_area_ha': 156379.86011338176, 'fallback_groups': 86} |
| evidence_tiers_are_known | PASS | {'tiers': ['rsyc_tile_exact', 'rsyc_tile_generic', 'rsyc_tile_group']} |
| allocation_bases_are_known | PASS | {'bases': ['district_fallback_no_province_intersection', 'mixed_province_intersection_and_district_fallback', 'province_intersection']} |

## 6. Paths and status

Outputs are under `data/derived/national/assortments/rsyc_tile_production/`:

- `rsyc_tile_production_library.csv`
- `tile_ecodistrict_weights.csv`
- `tile_ecodistrict_province_weights.csv`
- `rsyc_tile_production_summary.json`
- `RSYC_TILE_PRODUCTION_REPORT.md`
- `manifest.json`

No git commit was made. The national batch is unchanged and remains
diagnostic. The existing ecodistrict-first library is not replaced.

## 7. Next

Wire this library into a tile-level batch with one control cell per
`tile x province x species`, then reconcile the ecodistrict composition
diagnostic against the tile totals. The batch must carry `evidence_tier`,
`selected_level`, `model_id`, `control_total_source`, and `weight_source`.
Until the G1/G2 decisions in `planning/national-rsyc-backbone.md` are made,
this library is not a national supply estimate.
