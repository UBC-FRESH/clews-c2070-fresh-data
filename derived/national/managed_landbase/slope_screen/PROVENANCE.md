# Provenance - National 960 m Slope Screen

## Source

- **NRCan MRDEM-30 DTM**, Medium Resolution Digital Elevation Model, 30 m.
- Licence: **Open Government Licence - Canada 2.0**.
- VRT: `https://canelevation-dem.s3.ca-central-1.amazonaws.com/mrdem-30/mrdem-30-dtm.vrt`
- COG DTM: `https://canelevation-dem.s3.ca-central-1.amazonaws.com/mrdem-30/mrdem-30-dtm.tif`
- STAC collection: `https://datacube.services.geo.ca/stac/api/collections/mrdem-30`
- STAC search: `https://datacube.services.geo.ca/stac/api/search?collections=mrdem-30`
- MRDEM-30 is described by NRCan as a mosaic of the HRDEM lidar mosaic and
  the Copernicus GLO-30 DEM. The DTM is a terrain model, not a canopy/DSM.

## Inputs

- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/managed_landbase/slope_screen/inputs/mrdem-30-dtm.vrt` - MRDEM-30 DTM VRT - https://canelevation-dem.s3.ca-central-1.amazonaws.com/mrdem-30/mrdem-30-dtm.vrt - sha256 `b8405a01dcf2b2cb0dac5d18f5a20b2dc571187ec4f694b78b5763747a85d04f`
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/managed_landbase/slope_screen/inputs/stac_collection_mrdem-30.json` - MRDEM-30 STAC collection - https://datacube.services.geo.ca/stac/api/collections/mrdem-30 - sha256 `0fd4df5cf9916c994a0923a7dbc86620191570b76efacfb1611cd8683ceaf051`
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/managed_landbase/slope_screen/inputs/stac_search_mrdem-30.json` - MRDEM-30 STAC search - https://datacube.services.geo.ca/stac/api/search?collections=mrdem-30 - sha256 `9927d8202e4a6e6e136622738bcc8913ba60af22bc01d5920ad0d56a77e10c7b`
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/raw/scanfi/v2/SCANFI_att_nfiLandcover_2025_v2_20260119.tif` - SCANFI v2 land cover - sha256 `668438f6388731a1cf6a9e899a3d7aeb8a998e35c97e5199007db9da03ef46b2`
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/raw/national/rsyc/RSYC_ecostrat.gpkg` - RSYC ecostratification - sha256 `e425818f3c1db682f21a6eec6bebf4397761db46b08b13b8c4d3c780dc0d87a4`
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/raw/boundaries/canada_adm1_geoboundaries_simplified.geojson` - Province boundaries - sha256 `0c9e4fc56c8b9ce958960ffabd1556fbe7c3ec0deeea346a2b5b7dff05e35449`
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/managed_landbase/operable_proxy_v2/operable_proxy_v2_by_ecoprovince.csv` - Operable proxy v2 ecoprovince table - sha256 `68dc1f197f34a8c324dc473669f938f40158ae1d0972fe839fe0bd7f30e945ae`

## Processing

1. Read the VRT at 32x decimation (960 m) with average resampling through
   GDAL `/vsicurl` and the published overview chain. No full 30 m national
   download was made.
2. Compute Horn 3x3 slope in percent.
3. Read SCANFI land cover classes 5/6/7 in 33-block strips and sum exact
   33 x 33 treed counts. Reproject the 990 m treed fraction to the 960 m
   EPSG:3979 slope grid with bilinear resampling.
4. Rasterise province and ecoprovince polygons at 960 m with the pixel-centre
   rule and aggregate forest-weighted slope statistics.
5. Apply the observed >15% and >30% slope shares to operable proxy v2 `base`
   and `screen_core20` operable areas.

## Software

- Python `3.12.3`
- rasterio `1.5.0` / GDAL `3.12.1`
- numpy `2.5.0`
- pandas `3.0.3`
- geopandas `1.1.4`

## Reproduce

```bash
.venv/bin/python scripts/national/build_slope_screen.py \
    --out-dir data/derived/national/managed_landbase/slope_screen
```

## Caveats

- 960 m average slope is a screening surface, not a 30 m operability class.
- The DTM does not represent canopy, roads, or landings.
- MRDEM-30 source accuracy is not uniform across lidar and modelled areas.
- The overlay applies treed-area slope shares to v2 operable areas; it assumes
  the v2 screens are independent of slope within a province/ecoprovince.
- No legal THLB, AAC, or operability determination is made.
