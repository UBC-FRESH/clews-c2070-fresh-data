# RSYC contents and inventory

This directory contains the RSYC model catalogue, 150 km tile grid, and
ecological-strata boundaries for model release `v20260923` (RSYC package
`v0.2.0`, `dev` artifact `0.2.0.9000`). See `ACQUISITION.md` for provenance,
checksums, licensing, and reproduction commands.

## Files

| File | Bytes | SHA-256 | Contents |
|---|---:|---|---|
| `RSYC_models.zip` | 1,468,706 | `86da5737…24940` | ZIP with one member, `RSYC_models.csv` (16,768,740 bytes) |
| `RSYC_tiles.gpkg` | 278,528 | `f61e0ec0…7308b` | 385 Polygon features, layer `RSYC_tiles`, EPSG:3978 |
| `RSYC_ecostrat.gpkg` | 15,421,440 | `e425818f…d87a4` | 4 MultiPolygon/Polygon layers, EPSG:3978 |

Full hashes and per-artifact integrity notes are in `PROVENANCE.csv`.

## Spatial layers

| GeoPackage | Layer | Features | Geometry | Key fields |
|---|---|---:|---|---|
| `RSYC_tiles.gpkg` | `RSYC_tiles` | 385 | Polygon | `TileID` |
| `RSYC_ecostrat.gpkg` | `ecozones` | 12 | MultiPolygon | `ecozone`, `ecozone_id`, `join_key` |
| `RSYC_ecostrat.gpkg` | `ecoprovinces` | 36 | MultiPolygon | `ecozone`, `ecoprovince`, IDs, `join_key` |
| `RSYC_ecostrat.gpkg` | `ecoregions` | 138 | MultiPolygon | 4 hierarchy names, IDs, `join_key` |
| `RSYC_ecostrat.gpkg` | `ecodistricts` | 672 | Polygon | 4 hierarchy names, IDs, `join_key` |

All layers use Canada Atlas Lambert (EPSG:3978). The 385 tile polygons are the
tiles with published models, not the full 649-tile source grid. The ecological
layers contain the forested ecozones used by RSYC; each feature corresponds to
one national model `strata_id` through `join_key`.

## Model catalogue

`RSYC_models.csv`: **27,208 rows × 42 columns**; 27,208 unique `model_id`;
`model_version = v20260923` on every row. One row is one published curve.

### Columns

`model_id`, `model_version`, `response`, `response_units`, `strata_type`,
`strata_level`, `strata_id`, `ecozone_id`, `ecoprovince_id`, `ecoregion_id`,
`ecodistrict_id`, `scale`, `region_id`, `species`, `model_group`, `equation`,
`age_min`, `age_max`, `b1`, `b2`, `b3`, `b4`, `b1_se`, `b2_se`, `b3_se`,
`b4_se`, `sigma`, `parent_b1_random_effect`, `parent_b1_var`,
`local_b1_var`, `residual_var`, `has_cor_struct`, `has_var_struct`,
`component_ok`, `component_message`, `n_obs`, `n_units`, `converged`,
`singular_or_boundary`, `fit_ok`, `publish_ok`, `model_message`.

The curve equation is
`y = b1 * exp(-b4 * Age) * (1 - exp(-b2 * Age))^b3`, where `y` is AGB
(Mg/ha) or total volume (m3/ha). `RSYC_models.csv` stores parameters only;
the GeoPackages store boundaries only. Neither file contains plot records.

### Counts by response and spatial level

| Response | Tile | Tile-region | Ecozone | Ecoprovince | Ecoregion | Ecodistrict | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| AGB (`Mg/ha`) | 2,443 | 939 | 229 | 553 | 1,793 | 7,689 | 13,646 |
| Volume (`m3/ha`) | 2,443 | 811 | 232 | 565 | 1,809 | 7,702 | 13,562 |
| **Total** | **4,886** | **1,750** | **461** | **1,118** | **3,602** | **15,391** | **27,208** |

`scale`: 17,292 national and 9,916 regional curves. `tile` curves are national;
`tile_region` curves are the regional tile-model stratum (264 unique
`tile_region` IDs). The four ecological levels are ecozone, ecoprovince,
ecoregion, and ecodistrict.

### Unique spatial units

| Level | Unique `strata_id` values | Notes |
|---|---:|---|
| Tile | 385 | Exact match to `RSYC_tiles.gpkg` `TileID` |
| Tile-region | 264 | Regional tile-model stratum |
| Ecozone | 12 | Exact match to `ecozones.join_key` |
| Ecoprovince | 36 | Exact match to `ecoprovinces.join_key` |
| Ecoregion | 138 | Exact match to `ecoregions.join_key` |
| Ecodistrict | 672 | 671 exact; one known spelling mismatch for ecodistrict 438 |

### Species and model groups

- **32 scientific species codes**: `ABIE.AMA`, `ABIE.BAL`, `ABIE.LAS`,
  `ACER.MAC`, `ACER.RUB`, `ACER.SAH`, `ALNU.RUB`, `BETU.ALL`, `BETU.PAP`,
  `FRAX.NIG`, `LARI.LAR`, `LARI.OCC`, `PICE.ABI`, `PICE.ENG`, `PICE.GLA`,
  `PICE.MAR`, `PICE.RUB`, `PICE.SIT`, `PINU.BAN`, `PINU.CON`, `PINU.PON`,
  `PINU.RES`, `PINU.STR`, `POPU.BAL`, `POPU.GRA`, `POPU.TRE`, `PSEU.MEN`,
  `QUER.RUB`, `THUJ.OCC`, `THUJ.PLI`, `TSUG.HET`, `TSUG.MER`.
- **3 model groups**: `generic`, `coniferous`, `broadleaf`.
- The `species` column therefore has **35 distinct values** (32 scientific
  codes + 3 group labels).
- Curves by model group: species 16,511; generic 4,016; coniferous 3,602;
  broadleaf 3,079.

### Age range

- Catalogue bounds: `age_min = 1` and `age_max = 600` for all 27,208 rows.
- Package README and `predict_rsyc()` documentation describe the fitted /
  operational range as **1–150 years** and warn outside it. Use 1–150 for
  production screening; the 600-year value is the catalogue bound, not a
  recommended operating range.

### Fit and publication flags

- `publish_ok = TRUE`, `fit_ok = TRUE`, and `converged = TRUE` for all 27,208
  rows.
- `singular_or_boundary = TRUE` for 88 rows (ecodistrict 53, ecoregion 21,
  ecoprovince 9, ecozone 5; no tile or tile-region rows).
- `model_message = "Non-positive definite approximate variance-covariance"`
  for 16,140 rows; the remaining 11,068 are null.
- `component_ok = TRUE` for all rows; `has_cor_struct` and `has_var_struct`
  are `FALSE` for all rows.

## Validation metrics published with RSYC

The package's *Model validation* article compares each curve with independent
MAGPlot weighted plot means by 20-year age class, excluding plots older than
150 years. For each age class, the weighted plot mean and its 95% CI are
compared with the mean RSYC prediction. See
https://ptompalski.github.io/RSYC/articles/validation.html and Tompalski et
al. (2025), https://doi.org/10.1093/forestry/cpaf067.

The article reports 60 summary rows covering 6,434 validated curves. Across
all 60 rows:

- median R²: **0.57–0.80**
- median bias: **−31.4% to +9.3%**
- median RMSE: **31.3%–53.3%**

The complete published summary is reproduced below. Values are the medians
reported for each level × model group; `Models` is the number of validated
curves, not the number of catalogue rows.

| Response | Scale | Level | Generic R² | Generic bias % | Generic RMSE % | Species-group R² | Species-group bias % | Species-group RMSE % | Species R² | Species bias % | Species RMSE % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGB | national | Tile | 0.63 | -15.4 | 42.1 | 0.60 | -15.2 | 44.7 | 0.59 | -9.7 | 45.1 |
| AGB | national | Ecozone | 0.79 | -30.5 | 35.7 | 0.76 | -31.4 | 36.7 | 0.66 | -23.3 | 36.7 |
| AGB | national | Ecoprovince | 0.72 | -21.4 | 36.4 | 0.73 | -20.0 | 35.9 | 0.62 | -21.6 | 42.4 |
| AGB | national | Ecoregion | 0.73 | -31.0 | 47.5 | 0.67 | -27.0 | 50.1 | 0.60 | -22.3 | 46.9 |
| AGB | national | Ecodistrict | 0.67 | -15.2 | 46.5 | 0.61 | -11.8 | 45.5 | 0.61 | -6.8 | 44.5 |
| AGB | regional | Tile | 0.64 | -15.1 | 41.8 | 0.64 | -15.2 | 44.0 | 0.59 | +0.2 | 44.8 |
| AGB | regional | Ecozone | 0.80 | -28.4 | 32.2 | 0.67 | -28.4 | 35.5 | 0.66 | -23.2 | 38.2 |
| AGB | regional | Ecoprovince | 0.73 | -19.9 | 36.4 | 0.71 | -19.3 | 35.1 | 0.63 | -21.1 | 42.2 |
| AGB | regional | Ecoregion | 0.74 | -29.5 | 45.2 | 0.66 | -27.3 | 46.4 | 0.64 | -21.9 | 47.6 |
| AGB | regional | Ecodistrict | 0.65 | -17.0 | 46.6 | 0.62 | -10.7 | 43.6 | 0.60 | -6.7 | 45.3 |
| Volume | national | Tile | 0.61 | -8.0 | 48.7 | 0.58 | -7.1 | 48.1 | 0.57 | -1.0 | 48.4 |
| Volume | national | Ecozone | 0.80 | -22.9 | 31.3 | 0.73 | -20.0 | 34.5 | 0.66 | -18.9 | 37.4 |
| Volume | national | Ecoprovince | 0.74 | -16.1 | 36.4 | 0.70 | -13.1 | 37.4 | 0.64 | -15.3 | 41.6 |
| Volume | national | Ecoregion | 0.72 | -25.9 | 45.5 | 0.64 | -18.5 | 51.3 | 0.62 | -14.4 | 45.6 |
| Volume | national | Ecodistrict | 0.64 | -7.7 | 50.0 | 0.58 | -6.3 | 49.1 | 0.60 | +1.9 | 48.4 |
| Volume | regional | Tile | 0.60 | -3.1 | 48.0 | 0.60 | -5.0 | 45.3 | 0.58 | +9.3 | 48.2 |
| Volume | regional | Ecozone | 0.78 | -20.6 | 33.1 | 0.67 | -22.1 | 37.4 | 0.63 | -16.4 | 40.6 |
| Volume | regional | Ecoprovince | 0.73 | -16.4 | 35.9 | 0.67 | -15.6 | 37.1 | 0.64 | -15.5 | 40.8 |
| Volume | regional | Ecoregion | 0.73 | -21.0 | 44.8 | 0.64 | -14.8 | 49.5 | 0.62 | -15.2 | 46.6 |
| Volume | regional | Ecodistrict | 0.63 | -9.5 | 50.1 | 0.58 | -5.8 | 53.3 | 0.59 | -1.7 | 50.5 |

Publication-scale counts from the same article: 4,098 age-class points from
634 curves (AGB national tile), 514/73 (AGB national ecozone), 1,002/142
(AGB national ecoprovince), 2,116/319 (AGB national ecoregion), 4,207/673
(AGB national ecodistrict); 4,255/641 (volume national tile), 553/75
(volume national ecozone), 1,054/144 (volume national ecoprovince),
2,224/320 (volume national ecoregion), 4,410/683 (volume national
ecodistrict). Regional equivalents are listed in `validation.md`.

## Interpretation for the national bucking architecture

RSYC is a **benchmark/prior layer**, not a bucking tool:

- It supplies a defensible stand-age → AGB or total-volume curve for each
  150 km tile and for nested ecological strata.
- It does **not** supply tree lists, diameter distributions, taper, log grades,
  or product prices. Those must come from the bucking references recorded in
  `../bucking/REFERENCES.md` and from the plot/calibration data.
- Use it to sanity-check modelled stand-level volume/AGB, to fill age–yield
  priors where plot coverage is thin, and to compare national versus regional
  curve behaviour. Do not use it as an observation-level calibration target
  without accounting for the validation bias and RMSE ranges above.
- The 385-tile and 12/36/138/672 ecological joins are complete except for the
  documented ecodistrict-438 spelling. Join on `join_key`/`strata_id` and apply
  the one correction explicitly.

## Citation and licence

- Tompalski, P., Hermosilla, T., Baral, S.K., Wulder, M.A., White, J.C. 2025.
  National remote sensing-derived aboveground biomass yield curves for Canada.
  *Forestry: An International Journal of Forest Research*.
  https://doi.org/10.1093/forestry/cpaf067
- RSYC R package `v0.2.0` (2026-11-03),
  https://github.com/ptompalski/RSYC/releases/tag/v0.2.0
- Code/package and model catalogue: GPL-3.0-or-later, Crown copyright
  Natural Resources Canada.
- Ecological boundaries: Open Government Licence – Canada; source Agriculture
  and Agri-Food Canada, *National Ecological Framework for Canada*. Attribution:
  “Contains information licensed under the Open Government Licence – Canada.”
