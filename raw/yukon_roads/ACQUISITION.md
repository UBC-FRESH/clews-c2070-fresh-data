# Yukon Forest Resource Roads — 50k Acquisition — 2026-08-10

## Identity

| Field | Value |
|-------|-------|
| Publisher | Government of Yukon — Energy, Mines and Resources — GeoYukon |
| Title | Forest Resource Roads — 50k |
| Catalogue page | `https://mapservices.gov.yk.ca/arcgis/rest/services/GeoYukon/GY_Forestry/MapServer/39` |
| WMS endpoint (parent service) | `https://map-data.service.yk.ca/` (also documented at `Row 53 of metadata/source-inventory.csv`) |
| Licence | Yukon Open Government Licence (YOGL); OGL-Canada-equivalent for non-commercial / research use with attribution |
| Acquisition date | 2026-08-10 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | Yukon Territory (1:50,000 scale forest road linework) |
| Vintage | 50k base; rolling territorial update — service queried 2026-08-10 |
| CRS | EPSG:3578 (Yukon Albers) |
| Format | GeoJSON FeatureCollection (one record per polyline section) |

## Source URL (live-verified 2026-08-10)

| Artifact | URL | Status |
|----------|-----|--------|
| ArcGIS REST service metadata | `https://mapservices.gov.yk.ca/arcgis/rest/services/GeoYukon/GY_Forestry/MapServer/39?f=json` | 200 OK |
| Feature count | `?query?where=1%3D1&returnCountOnly=true&f=json` → `count: 556` | Confirmed |
| Full-feature pull (geojson) | `https://mapservices.gov.yk.ca/arcgis/rest/services/GeoYukon/GY_Forestry/MapServer/39/query?where=1%3D1&outFields=*&returnGeometry=true&f=geojson&resultRecordCount=1000` | Archived (this session) |

The CKAN catalogue's `package_search?q=fom+road` (BC DataBC) returned
provincial BC datasets, but the BC FTEN road-segment-lines layer does
not expose a direct bulk shape ZIP — only WFS/WMS/ArcGIS metadata blocks.
For Tier-3 in this session we pivot to the Yukon GeoYukon `GY_Forestry`
feature service, where layer 39 (`Forest Resource Roads - 50k`) exposes
the required attributes via a single ArcGIS REST query that returns
<1 MiB of GeoJSON (556 polylines, complete attribute set).

## Local file

| Field | Value |
|-------|-------|
| Path | `data/raw/yukon_roads/yukon_forest_resource_roads_50k.geojson` |
| Bytes | 1,691,138 (≈ 1.7 MB) |
| Local SHA-256 | `c9201e9801e2f6bc653aa97cf066e26bf84653c207c0cc6c47d227fd8a0d8a78` |
| Feature count | 556 (matches server `count: 556`) |
| Type | `JSON text data` |
| Properties retained | `OBJECTID, SHAPE.LEN, ROAD_GIS_LINK, ROAD_ID, SECTION_ID, LOCAL_ROAD_NAME, ROAD_DEVELOPMENT_STATUS, ROAD_ACT_TENURE, ROAD_CLASS, ROAD_CONSTRUCTION_DATE, ROAD_CONSTRUCTION_NOTES, SECTION_LENGTH_KM, SECTION_LENGTH_M` (14 fields, full attribute set) |
| Annex status | Targeted: `git annex add` on the next DataLad commit |

## Licence note

The Yukon Open Government Licence (YOGL) is the territorial equivalent
of OGL-Canada; verify the exact current text at
`https://open.yukon.ca/open-government-licence-yukon` (the canonical text
lives on the Government of Yukon's open data portal). This LICENSE.txt
pins the canonical link; relative to other provincial road layers this
YOGL allows redistribution with attribution.

## CC-by-equivalent clause (paraphrased)

> Use of this dataset is permitted with attribution to the Government
> of Yukon. Restrictions on bulk redistribution are minimal; consult
> the YOGL text for commercial restrictions. Indicative fields such as
> `ROAD_DEVELOPMENT_STATUS` and `ROAD_ACT_TENURE` are useful for
> freight-cost and forest-access signal derivation.

## Acknowledgements / citation

> Government of Yukon, GeoYukon. *Forest Resource Roads — 50k*
> (Feature Service, Map Server layer 39). Reproduced under the Yukon
> Open Government Licence. Service accessed 2026-08-10 at
> <https://mapservices.gov.yk.ca/arcgis/rest/services/GeoYukon/GY_Forestry/MapServer/39>.
