# NRWN (National Railway Network) — BC Shapefile Acquisition — 2026-08-10

## Identity

| Field | Value |
|-------|-------|
| Publisher | Natural Resources Canada — Canada Centre for Mapping and Earth Observation |
| Title | National Railway Network (NRWN) — British Columbia — v2.0 |
| Catalogue record | https://open.canada.ca/data/en/dataset/ac26807e-a1e8-49fa-87bf-451175a859b8 |
| Source mirror (verified live) | `https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/bc/` (enumerated via HTTPS directory listing) |
| Licence | Open Government Licence — Canada |
| Acquisition date | 2026-08-10 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | British Columbia |
| Vintage | 2019-07-25 (server timestamps) |
| CRS | NRWN v2.0 (Statistics Canada Lambert conformal conic, EPSG:3347 family) |
| Format | ESRI Shapefile bundle (SHP/SHX/DBF/PRJ/SBN/SBX) ZIP-wrapped |

## Source URLs (live-verified 2026-08-10)

| Artifact | URL | Bytes | Last-Modified | Status |
|----------|-----|------:|---------------|--------|
| NRWN BC SHP (English) | `https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/bc/nrwn_rfn_bc_shp_en.zip` | 4,777,621 | 2019-07-25 00:03 UTC | Archived (this session) |
| NRWN BC GML (English) | `https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/bc/nrwn_rfn_bc_gml_en.zip` | ~4.8 MB | 2019-07-25 | Recorded URL only — not archived |
| NRWN BC KML | `https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/bc/nrwn_rfn_bc_kml_en.kmz` | ~6.0 MB | 2020-10-02 | Recorded URL only — not archived |
| Index of available files | `https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/index/nrwn_rfn_index_prov.kmz` | 552,974 | — | Recorded URL only |

The CKAN package_show API for record `ac26807e-...` returns 5 service
resources (two WMS endpoints, an FTP directory pointer, documentation,
and the KMZ index). The per-province shapefile ZIPs are hosted under
`/pub/nrcan_rncan/vector/geobase_nrwn_rfn/<prov>/` and enumerated via
HTTPS INDEX.

## Local file

| Field | Value |
|-------|-------|
| Path | `data/raw/nrwn/nrwn_rfn_bc_shp_en.zip` |
| Bytes | 4,777,621 |
| Local SHA-256 | `2ed031b9bc319ef085356e2124e16c736e225db4466dacd1c5b5ca1b9b36097a` |
| Type | `Zip archive data, at least v2.0 to extract` — confirmed ESRI shapefiles inside (`NRWN_BC_2_0_TRACK.shp`, PolyLineZ; `NRWN_BC_2_0_CROSSING/JUNCTION/MARKERPOST/STATION/STRUCTURE_{0,1}.shp`, Points) |
| Annex status | Targeted: `git annex add` on the next DataLad commit |

## Layer summary (BC NRWN v2.0 shapefile bundle)

| ESRI layer | Geometry | Records (approx, server-encoded size proxy) |
|------------|----------|---------------------------------------------|
| `NRWN_BC_2_0_TRACK` | PolyLineZ | 6.15 MB SHP (~24,000 km rail) |
| `NRWN_BC_2_0_MARKERPOST` | Point | 90.96 KB SHP |
| `NRWN_BC_2_0_CROSSING` | Point | 182.8 KB SHP |
| `NRWN_BC_2_0_JUNCTION` | Point | 219.0 KB SHP |
| `NRWN_BC_2_0_STATION` | Point | 16.45 KB SHP |
| `NRWN_BC_2_0_STRUCTURE_1` | PolyLine (bridges/tunnels extent) | 214.3 KB SHP |
| `NRWN_BC_2_0_STRUCTURE_0` | Point | 0.5 KB SHP |

## Acknowledgements / citation

> Natural Resources Canada. *National Railway Network (NRWN) — GeoBase
> Series — v2.0*. Open Government Licence — Canada. Retrieved
> 2026-08-10 from the Open Canada portal
> <https://open.canada.ca/data/en/dataset/ac26807e-a1e8-49fa-87bf-451175a859b8>
> via the NRCan GeoBase FTP mirror.
