# National Managed-Landbase Proxy

**Status: screening proxy. This is not a legal timber harvesting landbase (THLB), not an AAC landbase, and is not applied to the 150 Mt supply estimate.**

Grid resolution: 500 m. Tenure vintage: 2016. Protected areas: CPCAD (2026-11-18 REST snapshot).

## Method

1. Compiled GFW Canada Forest Tenures 2016 polygons were deduplicated by exact geometry, repaired, and rasterized onto a Canada Albers grid.
2. CPCAD protected and conserved areas were rasterized on the same grid and subtracted wherever they overlap tenure.
3. Each cell was assigned to a province and SCANFI ecodistrict; SCANFI ecodistrict forest area was converted to a forest fraction.
4. Class footprints overlap (nested area-based and volume-based tenures). `forest_area_ha` is gross class footprint forest; `managed_proxy_ha` is apportioned to the tenure union so class rows sum to the union and do not double count.
5. `managed_share` uses SCANFI forest area for the province or ecoprovince as denominator.

Evidence tiers: `B` = accepted national tenure compilation (2016) with CPCAD protected overlay, suitable for screening only; `missing` = no accepted tenure source and values are deliberately blank.

## Provincial coverage and proxy

| province | tenure footprint (Mha) | tenure forest (Mha) | protected excluded (Mha) | managed proxy (Mha) | managed share (%) | SCANFI forest (Mha) | coverage |
|---|---|---|---|---|---|---|---|
| AB | 27.5 | 22.98 | 1.19 | 21.79 | 56.8 | 38.35 | tenure_2016 |
| BC | 94.67 | 66.54 | 12.17 | 54.37 | 81.6 | 66.61 | tenure_2016 |
| MB | 10.34 | 7.0 | 0.1 | 6.9 | 20.5 | 33.75 | tenure_2016 |
| NB | 3.32 | 3.15 | 0.59 | 2.56 | 38.2 | 6.69 | tenure_2016 |
| NL | 1.53 | 1.11 | 0.0 | 1.11 | 4.7 | 23.53 | tenure_2016 |
| NS | 1.47 | 1.28 | 0.19 | 1.1 | 23.2 | 4.73 | tenure_2016 |
| NT | 1.59 | 0.82 | 0.0 | 0.82 | 1.9 | 43.46 | tenure_2016 |
| NU | missing | missing | missing | missing | missing | 2.83 | missing |
| ON | 43.12 | 37.13 | 3.32 | 33.81 | 49.3 | 68.52 | tenure_2016 |
| PE | missing | missing | missing | missing | missing | 0.27 | missing |
| QC | 36.42 | 29.47 | 1.21 | 28.27 | 34.6 | 81.66 | tenure_2016 |
| SK | 10.56 | 7.76 | 0.28 | 7.49 | 28.6 | 26.16 | tenure_2016 |
| YT | 13.65 | 8.32 | 0.25 | 8.07 | 31.2 | 25.91 | tenure_2016 |

## Validation

- Tenure input features: 3680; analysis features after exact-geometry deduplication: 3464; duplicates removed: 216 (mostly repeated Yukon fuel-wood polygons).
- Tenure union forest <= SCANFI forest by province: **True**.
- Protected exclusion <= tenure forest: **True**.
- Class rows sum to union proxy: **True**.
- Gross class forest / union forest ratio: 1.288 (overlap inflation before apportionment).
- National managed proxy: 166.28 Mha of 422.48 Mha SCANFI forest.
- Missing tenure jurisdictions: NU, PE.

## Gaps and caveats

- **No legal THLB**: tenure boundaries are rights areas, not operability or harvest-landbase determinations.
- **No AAC**: no growth, yield, operability, accessibility, or economic constraints.
- **British Columbia upper bound**: GFW BC volume-based Forest Licence and Pulpwood Agreement polygons cover almost the entire province. The BC proxy is therefore close to all unprotected forest and should be read as an upper bound on the tenured landbase, not a licence-specific footprint.
- **Class overlap**: `forest_area_ha` is gross class footprint and sums to more than the tenure union in provinces with nested tenures (national ratio 1.29). Only `managed_proxy_ha` is apportioned to the union and safe to sum.
- **Yukon**: the 2016 compilation contains 51 repeated fuel-wood geometries; deduplication removes the duplication, but the remaining tenure footprint remains a compilation artefact and should be treated as low confidence.
- **Low tenure coverage**: NL (4.7% of SCANFI forest) and NT (1.9%) have only fragmentary 2016 tenure polygons; their proxies are lower bounds and should not be read as the managed forest area.
- **Nunavut and Prince Edward Island**: no GFW 2016 tenure rows; reported as `coverage=missing` with blank values, not zero.
- **Treaty/Settlement Lands**: the national forest management constraint layer was not used; Treaty/Settlement and Indigenous tenure signals are not represented.
- **Protected areas**: all CPCAD polygons are excluded, including IUCN VI areas that may allow some forestry; the exclusion is conservative.
- **Forest distribution**: forest-area equivalents assume forest is uniformly distributed within each ecodistrict.

## Outputs

- `managed_landbase_by_province.csv`: province x tenure type x tenure class rows; includes all 13 jurisdictions and explicit `coverage=missing` rows.
- `managed_landbase_by_ecoprovince.csv`: same proxy aggregated to ecoprovince x province x tenure type x tenure class. It contains the 11 jurisdictions with 2016 tenure coverage; NU and PE appear only in the province file as `coverage=missing`.
- `managed_landbase_province_summary.csv`: union-based provincial totals (authoritative for no-double-counting checks).
- `manifest.json`: input sizes, SHA-256 hashes, licences, method settings, and validation results.

## Sources and licences

| source | role | size | licence |
|---|---|---|---|
| GFW Canada Forest Tenures 2016 (ArcGIS item `aa8797d31edd47209e8eabf1c7789e5c`) | tenure polygons, 3,680 features before deduplication | 302,119,304 bytes | unknown_public (compilation) |
| CPCAD ESRI REST snapshot 2026-11-18 | protected/conserved areas, 22,438 features | 408,764,416 bytes | Open Government Licence - Canada |
| SCANFI v2 national area weights | ecodistrict forest-area frame | 1,579,339 bytes (ecodistrict CSV) | Open Government Licence - Canada |
| geoBoundaries CAN ADM1 simplified | province/territory polygons | 26,022,306 bytes | CC BY 4.0 |

SHA-256 values and exact byte counts for every input are in `manifest.json`.

## If a download is incomplete

The CPCAD downloader caches every page and resumes by offset. Re-running the same command completes a partial download:

```bash
.venv/bin/python scripts/national/download_cpcad_rest.py --out-dir data/raw/cpcad
```

If the CPCAD REST service is unavailable, use the FGDB bundle from the Open Canada record, convert it to GeoPackage, and pass `--cpcad <path>` to the build script. If GFW tenure is unavailable, use the Data Basin 2012 fallback (`data/raw/tenures/databasin/`) for the nine covered provinces only; leave YT, NT, and NU as `coverage=missing` rather than fabricating coverage. The build script fails closed when a required input is absent.

## Reproduction

```bash
.venv/bin/python scripts/national/download_cpcad_rest.py --out-dir data/raw/cpcad
.venv/bin/python scripts/national/build_managed_landbase.py --out-dir data/derived/national/managed_landbase
```

Raw CPCAD and tenure payloads remain in the `data` submodule and must not be committed to the parent repository.
