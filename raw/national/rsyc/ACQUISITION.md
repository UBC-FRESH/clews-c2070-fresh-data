# RSYC acquisition record

- **Dataset**: RSYC — Remote Sensing-Derived Yield Curves for Canada
- **Model release**: `v20260923`
- **Package release cited**: RSYC `v0.2.0` (GitHub release 2026-11-03, tag commit `27b1959b99352d877ba6408122a3276a482170e2`)
- **Package version at acquisition**: `0.2.0.9000` (`dev` branch; post-`v0.2.0` spelling correction)
- **Retrieved**: 2026-11-15T10:02:25Z to 2026-11-15T10:02:26Z (UTC)
- **Local path**: `data/raw/national/rsyc/`
- **Access**: open direct download; no credentials, no DUA, no registration

## Source artifacts

| Artifact | Source URL | Bytes | SHA-256 |
|---|---|---:|---|
| `RSYC_models.zip` | https://raw.githubusercontent.com/ptompalski/RSYC/dev/data-raw/RSYC_models.zip | 1,468,706 | `86da5737720613f686b3f14b3cdea43c18b5cde87a4b113a3cb0df6dcfe24940` |
| `RSYC_tiles.gpkg` | https://raw.githubusercontent.com/ptompalski/RSYC/dev/inst/extdata/RSYC_tiles.gpkg | 278,528 | `f61e0ec06b29146264ff676c98fcfa1e431d6ddd5f1d97d17e957d4d9e77308b` |
| `RSYC_ecostrat.gpkg` | https://github.com/ptompalski/RSYC/releases/download/ecostrat-v2/RSYC_ecostrat.gpkg | 15,421,440 | `e425818f3c1db682f21a6eec6bebf4397761db46b08b13b8c4d3c780dc0d87a4` |

The three SHA-256 values match the upstream release manifests:

- `data-raw/RSYC_models_manifest.csv`: `output_zip_sha256` = `86da5737…24940`, rows 27,208, columns 42, built 2026-11-13.
- `data-raw/tiles-manifest.csv`: `sha256` = `f61e0ec0…7308b`, 385 output features, built 2026-10-08.
- `data-raw/ecostrat-manifest.csv`: `sha256` = `e425818f…d87a4`, boundary version `v2`, built 2026-10-08.

## Reproduction

```bash
cd data/raw/national/rsyc
curl -fL --retry 4 --retry-delay 2 --connect-timeout 30 \
  -o RSYC_models.zip \
  https://raw.githubusercontent.com/ptompalski/RSYC/dev/data-raw/RSYC_models.zip
curl -fL --retry 4 --retry-delay 2 --connect-timeout 30 \
  -o RSYC_tiles.gpkg \
  https://raw.githubusercontent.com/ptompalski/RSYC/dev/inst/extdata/RSYC_tiles.gpkg
curl -fL --retry 4 --retry-delay 2 --connect-timeout 30 \
  -o RSYC_ecostrat.gpkg \
  https://github.com/ptompalski/RSYC/releases/download/ecostrat-v2/RSYC_ecostrat.gpkg
sha256sum RSYC_models.zip RSYC_tiles.gpkg RSYC_ecostrat.gpkg
```

## Integrity verification

- `unzip -t RSYC_models.zip`: `No errors detected`. One member, `RSYC_models.csv`, 16,768,740 bytes uncompressed.
- CSV parse: 27,208 data rows × 42 columns; 27,208 unique `model_id`; `model_version` = `v20260923` on every row.
- `PRAGMA integrity_check` on both GeoPackages: `ok`.
- `RSYC_tiles.gpkg`: one layer, `RSYC_tiles`; 385 Polygon features; EPSG:3978.
- `RSYC_ecostrat.gpkg`: four layers: `ecozones` 12, `ecoprovinces` 36, `ecoregions` 138, `ecodistricts` 672; EPSG:3978.
- Tile identifiers in `RSYC_tiles.gpkg` exactly match the 385 `strata_id` values in the model catalogue at `strata_level = tile` (385/385).
- Ecological `join_key` values match model `strata_id` values exactly for 12/12 ecozones, 36/36 ecoprovinces, and 138/138 ecoregions. Ecodistricts match 671/672; the single mismatch is the documented `Betsiamiles Plateau` (boundary v2) versus `Betsiamites Plateau` (corrected `0.2.0.9000` catalogue) spelling for ecodistrict 438. `rsyc_boundaries()` applies this correction at read time without changing the immutable boundary file.

## Version note: tagged `v0.2.0` versus `dev` artifact

The tagged `v0.2.0` ZIP is 1,468,625 bytes with SHA-256 `31776c6432424bb2f7a80b94046cbbcbbf4f39250acf19d73b5e89d4f7a60890`. The acquired `dev` ZIP is 1,468,706 bytes with SHA-256 `86da5737…24940`. Both contain 27,208 × 42 rows and the same `model_id` set and coefficients. They differ in 32 `strata_id` cells: the `dev` artifact applies the `0.2.0.9000` correction from `Betsiamiles Plateau` to `Betsiamites Plateau`. The NEWS entry states that model IDs, coefficients, and predictions are unchanged. The acquired artifact is the corrected `dev` artifact named in the task and in the current package README.

## Licensing and attribution

- **RSYC code and package**: GNU General Public License, version 3 or later (GPL-3.0-or-later). Copyright (C) 2025 His Majesty the King in Right of Canada, as represented by the Minister of Natural Resources Canada. See the upstream `LICENSE.md`.
- **Model catalogue** (`RSYC_models.csv`): distributed inside the GPL-3+ package. No separate licence file accompanies the CSV; treat it under the package licence and retain the Crown copyright notice. The CSV is a model-parameter table, not plot data.
- **Ecological strata** (`RSYC_ecostrat.gpkg`): Open Government Licence – Canada. Source: Agriculture and Agri-Food Canada, *National Ecological Framework for Canada* (https://open.canada.ca/data/dataset/3ef8e8a9-8d05-4fea-a8bf-7f5023d2b6e1). Attribution: “Contains information licensed under the Open Government Licence – Canada.” The boundary file retains the source spelling for ecodistrict 438.
- **Tile grid** (`RSYC_tiles.gpkg`): RSYC project artifact derived from the RSYC ecosystem model package; distributed with the GPL-3+ package.

## Citations

- Tompalski, P., Hermosilla, T., Baral, S.K., Wulder, M.A., White, J.C. 2025. National remote sensing-derived aboveground biomass yield curves for Canada. *Forestry: An International Journal of Forest Research*. https://doi.org/10.1093/forestry/cpaf067
- Tompalski, P., Wulder, M.A., White, J.C., Hermosilla, T., Riofrío, J., Kurz, W.A. 2024. Developing aboveground biomass yield curves for dominant boreal tree species from time series remote sensing data. *Forest Ecology and Management* 561, 121894. https://doi.org/10.1016/j.foreco.2024.121894
- RSYC R package, release `v0.2.0`, 2026-11-03. https://github.com/ptompalski/RSYC/releases/tag/v0.2.0

## Scope and caveats

- RSYC is a **published yield-curve benchmark/prior**, not ground-plot remeasurement data and not a bucking engine. It supplies stand-age → AGB or total-volume curves by 150 km tile and by four nested ecological levels.
- The catalogue has `age_min = 1` and `age_max = 600` for every curve. The package README describes the fitted/operational range as **1–150 years** and warns when predictions are requested outside that range. Do not interpret the 600-year catalogue bound as a recommended operating range.
- All 27,208 rows have `publish_ok = TRUE`, `fit_ok = TRUE`, and `converged = TRUE`. 88 rows carry `singular_or_boundary = TRUE`; 16,140 rows carry the message `Non-positive definite approximate variance-covariance`. These are fit-diagnostic flags, not publication exclusions.
- No package source code or documentation is vendored in this repository. Only the three published data artifacts are archived.
