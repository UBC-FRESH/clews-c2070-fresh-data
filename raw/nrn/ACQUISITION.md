# NRN (National Road Network) — BC GeoPackage Acquisition — 2026-08-10

## Identity

| Field | Value |
|-------|-------|
| Publisher | Statistics Canada / GeoBase (NRCan attribution for the GeoGratis mirror) |
| Title | National Road Network (NRN) — British Columbia |
| Catalog record | https://open.canada.ca/data/en/dataset/3d282116-e556-400c-9306-ca1a3cada77f |
| Source mirror (verified live) | `https://geo.statcan.gc.ca/nrn_rrn/bc/nrn_rrn_bc_GPKG.zip` (drawn from CKAN resource list) |
| Licence | Open Government Licence — Canada (OGL Canada) |
| Acquisition date | 2026-08-10 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | British Columbia |
| Vintage | 2026-06-26 (Server `Last-Modified`); NRN is a continuously maintained national layer |
| CRS | Statistics Canada Lambert (EPSG:3347) — typical for NRN 2.0 releases |
| Format | GeoPackage (Vector) inside ZIP wrapper |

## Source URLs (live-verified 2026-08-10)

| Artifact | URL | Bytes (Content-Length) | Last-Modified | Status |
|----------|-----|------------------------:|---------------|--------|
| NRN BC GEOPACKAGE | `https://geo.statcan.gc.ca/nrn_rrn/bc/nrn_rrn_bc_GPKG.zip` | 129,429,057 | 2026-06-26 19:31:24 UTC | Archived (this session) |

The UUID-pinned GeoGratis catalogue URLs in `metadata/source-inventory.csv`
(rows 48, 49) returned 404 as of 2026-08-10. The CKAN package_show API for
record `3d282116-...` still resolves to 30 live per-province ZIP resources
hosted at `geo.statcan.gc.ca/nrn_rrn/<prov>/...`. This acquisition uses the
BC GeoPackage ZIP (the highest-priority province for CLEWs-C2070 freight
calibration). The remaining 12 per-province ZIPs (AB, SK, MB, ON, QC, NB,
PE, NS, NL, YT, NT, NU) are recorded but not archived in this session to
respect the bounded budget.

## Local file

| Field | Value |
|-------|-------|
| Path | `data/raw/nrn/nrn_bc_gpkg.zip` |
| Bytes | 129,429,057 |
| Local SHA-256 | `9ae6fb8069a46c4a745571871bf068bdd9d978da745001fd0f8462bfb3b82842` |
| Server ETag | `04ebc5fa25dd1:0` (verbatim; x-zip-compressed) |
| Type | `Zip archive data, at least v2.0 to extract` |
| Annex status | Targeted: `git annex add` on the next DataLad commit |

## Predecessor notes

This increment updates source-inventory row 48 (`nrn_vectors`, originally
`accepted_subset_recommended`) and refines the URL pin from the dead
geogratis UUID route to a live GeoBase mirror URL.

## Acknowledgements / citation

> Statistics Canada / Natural Resources Canada. *National Road Network
> (NRN) — GeoBase Series.* Open Government Licence — Canada. Retrieved
> 2026-08-10 from the Open Canada portal
> <https://open.canada.ca/data/en/dataset/3d282116-e556-400c-9306-ca1a3cada77f>.
