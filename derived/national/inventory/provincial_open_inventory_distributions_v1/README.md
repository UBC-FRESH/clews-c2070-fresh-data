# Provincial open inventory distributions v1

Retrieval date: 2026-11-23

This artifact converts the attributes that open provincial inventories
actually publish into small, area-weighted distribution tables for E2 v2.
It does not ingest full layers into the model and does not claim that any
one inventory is complete.

## Sources and fields

| Province | Source | Fields used | Coverage |
|---|---|---|---|
| AB | AVI Crown | SP1..SP5, SP1_PER..SP5_PER, HEIGHT, ORIGIN, PHOTO_YR, Shape_Area | full 788,810-polygon FGDB |
| SK | FRI Forest Stands | CSG, HEIGHT, BA, QMD, MSTEMS, GBVOL, GMVOL8, HECTARES | checked-in 500-stand sample |
| MB | FRI 1970s | SPECIES composition string, AGE_YRPHOTO, AREA_HA | full 582,601-polygon FGDB |
| NS | Forest Inventory | SP1..SP4, SP1P..SP4P, HEIGHT, AVDI, TOTBA, TOTMRVOL, HECTARES | full 1,004,111-record DBF |
| PE | CLUI 2010 + EFI2020 | COVER1..COVER5, PER1..PER5, HEIGHT; topht, bamerch, tphmerch, gtv | checked-in 500-row samples |
| ON, NL, NT, NU | no open stand attributes | gap recorded; SCANFI composition + measured donor geometry in E2 v2 | not distribution-informed |

## Files

- `species_composition.csv`: area- or hectare-weighted species shares by province.
- `attribute_quantiles.csv`: weighted p05..p95, mean, median and SD by province, source and attribute.
- `joint_quantiles.csv`: NS species-specific joint stand quantiles (height, AVDI, volume) retained from the same polygon.
- `inference_equations.csv`: documented DBH inference equations.
- `province_summary.csv`: one row per province with the fields actually used.
- `source_provenance.csv`: source, licence, URL, retrieval date and SHA-256.

## Labels

- Area-weighted shares use polygon area/hectares times the published species proportion.
- `HEIGHT` and `AGE` are photo-interpreted stand attributes, not tree measurements.
- SK QMD is a stand quadratic mean diameter, not a tree-list joint distribution.
- PE QMD is inferred from EFI merchantable basal area and merchantable stems.
- MB has no open height or DBH; E2 v2 uses measured donor geometry for those joints.

No request, DUA, restricted data or official OSeCAN input is used.

## Summary

| Province | Composition source | Height | DBH | Age | Volume |
|---|---|---|---|---|---|
| AB | AVI SP1..SP5 x SP1_PER..SP5_PER (area weighted) | AVI HEIGHT (area weighted) | absent; inferred from height with a donor-fit H-D equation | AVI PHOTO_YR - ORIGIN | absent in AVI polygons |
| SK | FRI CSG softwood/hardwood group (hectare weighted); SCANFI resolves species inside each group | FRI HEIGHT (hectare weighted) | FRI QMD (hectare weighted) | absent | FRI GBVOL / GMVOL8 (hectare weighted) |
| MB | FRI SPECIES composition string, AREA_HA weighted | absent; donor measured height | absent; donor measured DBH | AGE_YRPHOTO (area weighted) | absent in the open 1970s stand attributes |
| NS | NS SP1..SP4 x SP1P..SP4P (hectare weighted) | NS HEIGHT (hectare weighted) | NS AVDI (hectare weighted; average total diameter) | absent | NS TOTMRVOL (hectare weighted) |
| PE | CLUI COVER1..COVER5 x PER1..PER5 (hectare weighted) | CLUI HEIGHT by species (hectare weighted); EFI topht for volume context | EFI bamerch/tphmerch QMD inference (no CLUI DBH) | absent | EFI gtv (m3/ha) |
| PE | none; species from CLUI | EFI topht (cell area weighted) | EFI QMD inferred from bamerch and tphmerch | absent | EFI gtv (cell area weighted) |
| ON | gap; SCANFI v2 composition used in E2 v2 | gap; donor measured height | gap; donor measured DBH | gap | gap |
| NL | gap; land cover has FORESTTYPE only; SCANFI composition used | gap; donor measured height | gap; donor measured DBH | gap | gap |
| NT | gap; ATLAS vegetation type only; SCANFI composition used | gap; donor measured height | gap; donor measured DBH | gap | gap |
| NU | gap; SCANFI composition used | gap; donor measured height | gap; donor measured DBH | gap | gap |

Rows written: 57 composition, 107 quantile, 15 joint, 9 provenance.
