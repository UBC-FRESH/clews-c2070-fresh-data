# National 960 m Slope Screen

**Status:** coarse screening layer. This is **not** a 30 m operability
classification, legal timber harvesting landbase (THLB), AAC landbase, or
yield model. All slope losses are screening estimates.

## DEM and resolution

- Source: NRCan **MRDEM-30 DTM** (Medium Resolution Digital Elevation Model,
  30 m), Open Government Licence - Canada 2.0.
- VRT: `https://canelevation-dem.s3.ca-central-1.amazonaws.com/mrdem-30/mrdem-30-dtm.vrt`
- STAC: `https://datacube.services.geo.ca/stac/api/collections/mrdem-30`
- Native grid: EPSG:3979, 30 m, nodata `-32767.0`, shape
  `166668 x 185220`.
- Processing grid: **960 m** (32 x 30 m) in EPSG:3979, average elevation,
  shape `5208 x 5788`.
- Slope kernel: Horn 3x3, the default `gdaldem slope` kernel; units percent.
- The national DEM was read through windowed `/vsicurl` requests and GDAL
  overviews. No full 30 m national download was made.

## National vs subset coverage

The full national 960 m slope grid completed. There is no provincial DEM
subset gap. The 960 m grid drops a 120 m right-edge strip and a 360 m
bottom-edge strip of the VRT so that the output cells are exactly 960 m;
both are outside the Canadian landmass / SCANFI forest grid.

The **ecoprovince slope aggregation** covers 409.20 Mha of the 422.48 Mha
SCANFI treed area. The remaining **13.27 Mha (3.14%)** is SCANFI treed land
outside the RSYC ecoprovince polygons (Arctic/subarctic ecozones). Operable
proxy v2 assigns those blocks to the nearest ecoprovince; this screen does
not, so the 3.14% is recorded as a gap rather than an invented attribution.
The national slope raster still covers the full DEM extent.

## Method

1. Average MRDEM-30 DTM elevation to 960 m with GDAL average resampling.
2. Compute Horn percent slope.
3. Build an exact 990 m treed fraction from SCANFI classes 5/6/7 by summing
   33 x 33 blocks; reproject that fraction to the 960 m slope grid with
   bilinear resampling.
4. Rasterise province and ecoprovince polygons at 960 m and compute
   forest-weighted mean slope, share >15%, and share >30%.
5. Apply the observed steep shares to operable proxy v2 `base` and
   `screen_core20` operable areas.

The block-level CSV fallback is documented: a 990 m block table would have
about 3.4 million treed rows and several hundred megabytes, so the permitted
province/ecoprovince aggregation is published.

## Slope results by province

| Province | Treed (Mha) | Mean slope | >15% | >30% | Base operable (Mha) | Base lost >30% (Mha) | Core20 operable (Mha) | Core20 lost >30% (Mha) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AB | 37.15 | 1.98% | 1.8% | 0.2% | 18.40 | 0.02 | 13.76 | 0.01 |
| BC | 66.32 | 10.13% | 24.5% | 4.5% | 49.26 | 2.17 | 31.32 | 1.46 |
| MB | 32.82 | 0.40% | 0.0% | 0.0% | 5.49 | 0.00 | 3.34 | 0.00 |
| NB | 6.67 | 1.64% | 0.0% | 0.0% | 2.14 | 0.00 | 1.96 | 0.00 |
| NL | 23.34 | 2.21% | 0.2% | 0.0% | 0.88 | 0.00 | 0.82 | 0.00 |
| NS | 4.68 | 1.58% | 0.0% | 0.0% | 1.02 | 0.00 | 0.96 | 0.00 |
| NT | 40.55 | 2.16% | 2.0% | 0.1% | 0.64 | 0.00 | 0.30 | 0.00 |
| NU | 0.93 | 0.74% | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 |
| ON | 65.24 | 0.59% | 0.0% | 0.0% | 30.01 | 0.00 | 26.72 | 0.00 |
| PE | 0.27 | 0.63% | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 |
| QC | 80.11 | 1.83% | 0.1% | 0.0% | 26.16 | 0.00 | 14.54 | 0.00 |
| SK | 25.24 | 0.70% | 0.0% | 0.0% | 4.93 | 0.00 | 3.70 | 0.00 |
| YT | 25.88 | 7.12% | 8.4% | 0.2% | 5.76 | 0.01 | 2.46 | 0.00 |

National forest-weighted slope: mean **2.30%**,
median **0.52%**, p90 **6.70%**,
p99 **24.93%**, maximum **95.91%**.
All-land share >15%: **3.52%**; >30%:
**0.50%**. These all-land shares include flat non-forest
terrain and are not the forest-weighted shares in the province table.

### Steepest ecoprovinces

| Province | Ecoprovince | Treed (Mha) | Mean slope | >30% |
|---|---|---:|---:|---:|
| BC | Northern Coastal Mountains | 0.69 | 20.65% | 22.3% |
| BC | Wrangel Mountains | 0.05 | 14.58% | 12.8% |
| BC | Southern Coastal Mountains | 11.04 | 15.88% | 12.7% |
| BC | Columbia Montane Cordillera | 9.78 | 15.85% | 9.3% |
| YT | Southern Boreal Cordillera | 0.24 | 13.03% | 4.9% |
| BC | Southern Montane Cordillera | 4.46 | 11.25% | 3.6% |
| YT | Wrangel Mountains | 0.18 | 11.67% | 3.1% |
| BC | Georgia Depression | 1.50 | 10.10% | 2.5% |
| AB | Columbia Montane Cordillera | 2.82 | 10.57% | 2.2% |
| NT | Mackenzie-Selwyn Mountains | 1.56 | 12.00% | 2.2% |

### Largest core20 slope losses

| Province | Ecoprovince | Core20 (Mha) | Lost >30% (Mha) | Remaining (Mha) |
|---|---|---:|---:|---:|
| BC | Southern Coastal Mountains | 4.72 | 0.60 | 4.12 |
| BC | Columbia Montane Cordillera | 6.13 | 0.57 | 5.56 |
| BC | Southern Montane Cordillera | 2.97 | 0.11 | 2.86 |
| BC | Northern Coastal Mountains | 0.26 | 0.06 | 0.20 |
| BC | Northern Montane Cordillera | 5.93 | 0.05 | 5.88 |
| BC | Central Montane Cordillera | 4.10 | 0.03 | 4.07 |
| BC | Georgia Depression | 1.07 | 0.03 | 1.04 |
| BC | Southern Boreal Cordillera | 1.45 | 0.02 | 1.42 |
| AB | Columbia Montane Cordillera | 0.64 | 0.01 | 0.62 |
| YT | Northern Boreal Cordillera | 1.81 | 0.00 | 1.80 |

## Operable overlay / 150M implications

| Case | Operable before (Mha) | Lost >30% (Mha) | Operable after (Mha) | Lost share |
|---|---:|---:|---:|---:|
| v2 base | 144.69 | 2.19 | 142.50 | 1.51% |
| v2 core20 | 99.87 | 1.48 | 98.39 | 1.48% |

Sensitivity at >15%:

| Case | Lost >15% (Mha) | Operable after (Mha) | Lost share |
|---|---:|---:|---:|
| v2 base | 12.52 | 132.17 | 8.66% |
| v2 core20 | 8.27 | 91.60 | 8.28% |

The 150,000,000 m3/yr path is an upper scenario bound, not a forecast or
AAC. On the post-slope core20 area the implied intensity is
**1.525 m3/ha/yr**
(0.135 odt/ha/yr). On the post-slope
base area it is **1.053 m3/ha/yr**.
These are target-volume / area arithmetic, not growth estimates.

## Validation

- Slope range: **0.000% to 95.910%**;
  no negative values and no NaN in the slope grid.
- Finite slope cells: **14,902,202**; nodata cells:
  **15,241,702**.
- Treed area vs v2: **409,203,743 ha**
  vs **422,475,761 ha**
  (difference **-3.14%**,
  tolerance 5%).
- Base operable area vs v2: **144,689,810 ha**
  vs **144,689,810 ha**.
- Province rollups sum to the national total.
- Core20 <= base for every province/ecoprovince row.
- No independent provincial slope statistic was present in the workspace.
  The qualitative check is that steep shares are highest in the western
  cordillera and lowest in prairie/lowland ecoprovinces.

## Caveats and gaps

- **1 km smoothing:** local 30 m slopes can be much steeper; this layer cannot
  classify harvest systems, cable/ground operability, or site degradation.
- **DTM, not DSM:** MRDEM-30 DTM is a terrain model. It does not measure
  canopy height or closure; forest canopy and roads are not represented.
- **Mixed source:** MRDEM-30 mosaics HRDEM lidar with Copernicus GLO-30.
  Non-lidar areas are modelled and may have larger vertical error. The public
  STAC item does not publish a source-class legend; the per-pixel source
  counts are reported without interpretation.
- **Overlay assumption:** steep shares measured on the treed landbase are
  applied to v2 operable areas; v2 screens are assumed independent of slope
  inside a province/ecoprovince. This is not a pixel-exact intersection.
- **No legal claim:** slope >15% and >30% are screening thresholds, not
  provincial rules, legal exclusions, or an AAC determination.

## Files

- `slope_960m_epsg3979.tif` - national 960 m Horn slope, uint16 scale 0.01,
  nodata 65535.
- `slope_by_ecoprovince.csv` - forest-weighted slope distribution.
- `slope_operable_overlay.csv` - v2 base/core20 overlay by province/ecoprovince.
- `slope_operable_overlay_by_province.csv` - province rollup.
- `slope_screen_summary.json` - machine-readable summary and validation.
- `manifest.json` - inputs, outputs, hashes, software versions.
- `PROVENANCE.md` - source, licence, and method lineage.
