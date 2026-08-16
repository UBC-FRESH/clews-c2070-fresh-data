# ERA5 Monthly Climate Normals — Acquisition Manifest

## Source
- **Provider:** Copernicus Climate Data Store (CDS)
- **Dataset:** ERA5 monthly averaged data on single levels (reanalysis-era5-single-levels-monthly-means)
- **URL:** https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-monthly-means
- **Licence:** CC-BY (accepted programmatically 2026-08-16) + licence-to-use-copernicus-products rev 12
- **Citation:** Hersbach et al. (2020), https://doi.org/10.1002/qj.3803

## Acquisition Date
2026-08-16

## Variables Acquired
| Variable | CDS Name | Units (raw) | Period | Product Type |
|---|---|---|---|---|
| 2m temperature (mean) | 2m_temperature | K | 1991–2020 | monthly_averaged_reanalysis |
| Total precipitation | total_precipitation | m | 1991–2020 | monthly_averaged_reanalysis |
| 2m dewpoint temperature | 2m_dewpoint_temperature | K | 1991–2020 | monthly_averaged_reanalysis |

## Spatial Domain
- Bounding box: 41°N to 84°N, 141°W to 52°W (Canada)
- Resolution: 0.25° × 0.25°
- CRS: EPSG:4326 (WGS 84)

## Temporal Coverage
- 1991-01 through 2020-12 (360 months)
- 3 chunks per variable: 1991–2000, 2001–2010, 2011–2020

## Processing Chain
1. Raw monthly means downloaded from CDS (9 NetCDF files)
2. Climatological normals computed: 30-year mean per calendar month
3. Annual summaries derived (MAT, MAP, annual dewpoint)
4. Bioclimatic variables derived (GDD5, FFP, VPD, Twarm, Tcold, etc.)
5. Units converted (K→°C, m→mm)
6. Exported as Cloud-Optimized GeoTIFFs
7. Clipped to Canada boundary (if boundary available)

## Known Limitations
- t2m_min / t2m_max not available in ERA5 monthly-means CDS product
- FFP is approximated from monthly means (not daily counts)
- VPD derived from monthly mean T and Td (underestimates peak VPD)
- 0.25° resolution may not capture fine-scale topographic climate variation

## Contact
Acquired via automated pipeline by gep agent
