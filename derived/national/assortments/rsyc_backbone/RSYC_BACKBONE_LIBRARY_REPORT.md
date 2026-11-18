# RSYC national volume-curve backbone

**Status:** generated artefact; no commit. **Date:** 2026-11-18T17:36:32.899209+00:00.

## 1. Selection and fallback

Target cells are positive-area SCANFI ecodistrict parts x species, with
ecoprovince residuals only where no ecodistrict area exists. Selection uses
national-scale, `publish_ok`, `fit_ok`, `converged` volume curves. Exact
species are exhausted at ecodistrict, ecoregion, ecoprovince, ecozone, and
tile before the species group (`coniferous`/`broadleaf`) and finally `generic`
are considered.

- Target cells: **5,800**
  (5,800 ecodistrict, 0 ecoprovince residual)
- Unique ecodistrict x species cells: **4,677**
  (area weights are split into province parts, so one ecodistrict can carry more than one cell)
- Unique ecodistricts: **672**
- Total target area: **422,475,762 ha**
- Curves selected: **5,800**; explicit failures: **0**

### Evidence tier

| tier | cells | area_ha | area_share_pct |
|---|---|---|---|
| rsyc_direct | 1,880 | 255,722,993.0383 | 60.5296 |
| rsyc_fallback | 1,302 | 20,092,757.0430 | 4.7560 |
| rsyc_group | 2,618 | 146,660,011.4412 | 34.7144 |

### Selected level

| selected_level | cells |
|---|---|
| ecodistrict | 4,308 |
| ecoprovince | 290 |
| ecoregion | 558 |
| ecozone | 638 |
| tile | 6 |

### Fallback depth

Depth 0-4 is exact species (ecodistrict, ecoregion, ecoprovince, ecozone,
tile); depth 5-9 is the species group at the same ladder; depth 10-14 is
`generic`. Depth -1 is an explicit failure.

| fallback_depth | cells | area_ha |
|---|---|---|
| 0 | 1,880 | 255,722,993.0383 |
| 1 | 468 | 9,692,602.3598 |
| 2 | 241 | 2,556,555.6797 |
| 3 | 587 | 7,835,877.4246 |
| 4 | 6 | 7,721.5787 |
| 5 | 2,428 | 143,200,839.2228 |
| 6 | 90 | 1,514,084.1689 |
| 7 | 49 | 1,032,589.7799 |
| 8 | 51 | 912,498.2696 |

## 2. Area coverage

| Metric | Area (ha) | Share |
|---|---:|---:|
| Total target area | 422,475,762 | 100.0% |
| Covered by a selected curve | 422,475,762 | 100.00% |
| Direct exact species | 255,722,993 | 60.53% |
| Fallback exact species | 20,092,757 | 4.76% |
| Species group | 146,660,011 | 34.71% |
| Explicit failure | 0 | 0.00% |
| Zero-area cells excluded | 0 | 0 cells, not a target |
| Unmapped area (no ecodistrict/ecoprovince join) | 0 | 0 cells, not assignable |
| Ecoprovince-only residual | 0 | 0 cells, added separately |

### By province

| province | cells | area_ha | coverage_pct | direct_pct | fallback_pct | group_pct |
|---|---|---|---|---|---|---|
| QC | 589 | 81,663,538.5592 | 100.0000 | 65.8062 | 8.7303 | 25.4636 |
| ON | 446 | 68,517,060.2271 | 100.0000 | 57.0586 | 6.7679 | 36.1735 |
| BC | 732 | 66,607,737.0507 | 100.0000 | 44.4434 | 1.8463 | 53.7103 |
| NT | 592 | 43,460,564.1586 | 100.0000 | 67.0308 | 4.5216 | 28.4477 |
| AB | 763 | 38,345,566.4687 | 100.0000 | 54.5688 | 1.7338 | 43.6974 |
| MB | 454 | 33,753,909.9768 | 100.0000 | 66.0681 | 2.4182 | 31.5138 |
| SK | 621 | 26,160,931.2754 | 100.0000 | 66.3210 | 1.9265 | 31.7525 |
| YT | 506 | 25,905,742.5886 | 100.0000 | 77.3577 | 0.6855 | 21.9569 |
| NL | 437 | 23,531,836.3298 | 100.0000 | 77.3488 | 9.9748 | 12.6763 |
| NB | 229 | 6,692,497.6592 | 100.0000 | 35.6623 | 4.5135 | 59.8243 |
| NS | 215 | 4,727,696.9422 | 100.0000 | 20.8159 | 3.2964 | 75.8877 |
| NU | 176 | 2,834,208.4557 | 100.0000 | 67.6006 | 5.6159 | 26.7835 |
| PE | 40 | 274,471.8303 | 100.0000 | 18.1767 | 1.5734 | 80.2499 |

## 3. Ecodistrict-first versus tile-first

Tile-first selects the tile exact species, then the tile group, then tile
`generic`, on the same cells and area weights. It is the control comparison,
not the backbone: the tile is a separate 150 km grid, not a parent ecological
stratum.

| Metric | Ecodistrict-first | Tile-first |
|---|---:|---:|
| Covered area | 422,475,762 ha | 422,475,762 ha |
| Coverage | 100.00% | 100.00% |
| Direct area | 255,722,993 ha | 0 ha |
| Fallback area | 20,092,757 ha | 251,999,782 ha |
| Group area | 146,660,011 ha | 170,475,980 ha |

Differences are `ecodistrict-first minus tile-first` on cells where both
produce a curve. `p95` is the 95th percentile of absolute differences.

| age | cells | median_diff | median_abs_diff | mean_abs_diff | p95_abs_diff | area_weighted_median_abs | median_relative_abs_pct |
|---|---|---|---|---|---|---|---|
| 50 | 5,800 | 1.2457 | 13.6618 | 25.7316 | 94.0099 | 8.7009 | 15.2552 |
| 100 | 5,800 | 1.9878 | 16.9361 | 31.0552 | 110.5973 | 11.1166 | 15.0448 |
| 150 | 5,800 | 1.8494 | 17.2367 | 31.5238 | 114.3070 | 12.0304 | 15.1472 |

Cells whose selected level differs: **5,794**
(422,468,040 ha).

## 4. Species coverage and gaps

| species | cells | area_ha | direct_pct | fallback_pct | group_pct | curve |
|---|---|---|---|---|---|---|
| ABIE.BAL | 683 | 17,465,104.9793 | 75.8648 | 16.8228 | 7.3125 | species |
| BROADLEAF | 842 | 82,649,859.9346 | 0.0000 | 0.0000 | 100.0000 | group target |
| CONIFEROUS | 164 | 34,616,820.4681 | 0.0000 | 0.0000 | 100.0000 | group target |
| LARI.LAR | 814 | 27,150,318.0688 | 0.0000 | 0.0000 | 100.0000 | no species curve -> group |
| PICE.GLA | 679 | 39,033,902.5193 | 64.2868 | 34.3414 | 1.3718 | species |
| PICE.MAR | 823 | 153,682,120.5158 | 99.8586 | 0.1414 | 0.0000 | species |
| PINU.BAN | 717 | 39,126,191.3721 | 93.5525 | 6.3683 | 0.0791 | species |
| PINU.CON | 476 | 21,195,759.2992 | 97.9727 | 1.7072 | 0.3201 | species |
| PINU.PON | 59 | 211,686.4393 | 27.4074 | 72.1587 | 0.4339 | species |
| PINU.RES | 205 | 1,025,102.4655 | 59.7878 | 14.2455 | 25.9668 | species |
| PINU.STR | 205 | 1,025,102.4655 | 72.3092 | 21.5752 | 6.1156 | species |
| PSEU.MEN | 133 | 5,293,792.9949 | 96.9618 | 3.0040 | 0.0342 | species |

- Target species with no national species curve at any level:
  **LARI.LAR**
- Target cells without a direct exact-species curve:
  **3,920** (166,752,768 ha)
- Ecodistricts with at least one non-direct target cell:
  **672** of 672
- Published tiles without a `broadleaf` group curve:
  **140** of
  385 (tile `generic` remains).
- Negative `b4` coefficients in selected curves:
  **2,201** of 5,800. These are published
  RSYC fits; the sign is flagged in `coefficient_sign_flag`, not silently
  dropped. `b1`, `b2`, and `b3` are strictly positive for every selected curve.

## 5. Validation and tests

Validation summary: **PASS**.

| check | passed | detail |
|---|---|---|
| every_positive_area_target_has_a_curve | PASS | {"targets": 5800, "covered": 5800, "failed_area_ha": 0.0} |
| no_nan_coefficients | PASS | 0 |
| b1_b2_b3_strictly_positive | PASS | 0 |
| negative_b4_is_flagged | PASS | {"negative_b4": 2201, "flagged": 2201} |
| predictions_finite_and_non_negative | PASS | "ages 50/100/150" |
| area_sums_match_targets | PASS | {"library_area_ha": 422475761.52243674, "target_area_ha": 422475761.5224375} |
| no_duplicate_target_cells | PASS | 0 |
| fallback_depth_within_ladder | PASS | {"min": 0, "max": 8} |
| tile_assignment_recorded | PASS | {"centroid_within_single_tile": 5800} |
| unmapped_area_reported | PASS | 0.0 |
| province_area_sums_match_reference | PASS | {"max_abs_diff_ha": 1.043081283569336e-07, "max_rel_diff": 1.2772913125884233e-15} |
| tile_first_comparison_complete | PASS | 5800 |

Curve QC at ages 50/100/150: median volumes
93.0 / 115.2 /
119.0 m3/ha. No NaN or negative predictions.

Tests are in `workflows/national/assortments/tests/test_rsyc_backbone.py`
(ladder/fallback, evidence tiers, area join, curve evaluation). They are not
committed.

## 6. Paths and status

Outputs: `data/derived/national/assortments/rsyc_backbone/`.
The `manifest.json` records input and output SHA-256 checksums. No git commit
was made.

## 7. Method notes

- National-scale curves only. Regional-scale curves duplicate the same
  ecological strata and add a second fit; they are not used.
- The single documented catalogue/boundary mismatch (ecodistrict 438,
  `Betsiamites` versus `Betsiamiles`) is corrected explicitly and counted.
- Tile assignment uses the tile containing each ecodistrict or ecoprovince
  centroid. No nearest-tile fabrication is used. Every target centroid fell in
  exactly one published tile.
- The tile-first comparison does not upgrade any curve to `rsyc_direct`; all
  tile selections are recorded as fallback or group evidence.
