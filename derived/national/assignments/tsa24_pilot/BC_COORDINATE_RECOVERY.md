# BC facility coordinate recovery and diagnostic contract evidence

> Diagnostic/project-legacy evidence.  The Mills DB 2015 and FFCM 2018 facility
> code systems collide: eight identical codes refer to different mills.  A code
> match is therefore only accepted when name, city, or coordinate evidence
> corroborates it.  No match is forced.

## 1. Coverage improvement

| Source | Previous all BC | New all BC | Previous Stage A scope | New Stage A scope |
| --- | ---: | ---: | ---: | ---: |
| `mills_db_2015` | 8 | 98 | 7 | 88 |
| `suppliers_dbf` | 0 | 0 | 0 | 0 |
| `tl_anchor_proxy` | 126 | 65 | 113 | 58 |
| `missing` | 45 | 16 | 41 | 15 |

The Stage A scope is the 161 BC SAW/PAP/PEL/BIO facilities.  The recovered
input table has 98 corroborated Mills DB matches; 16 remain missing before the
hub-proxy fallback, and 65 receive a low-confidence TL hub proxy.

## 2. Matching method and confidence

All 179 BC facilities:

| Match method | Facilities |
| --- | ---: |
| company_city_class | 47 |
| coordinate_corroborated | 5 |
| coordinate_named | 1 |
| mill_name_class | 45 |
| unmatched | 76 |
| unmatched_no_registry | 5 |

| Match confidence | Facilities |
| --- | ---: |
| high | 55 |
| low | 1 |
| medium | 42 |
| missing | 81 |

Stage A scope only (161 facilities):

| Match method | Facilities |
| --- | ---: |
| company_city_class | 46 |
| coordinate_corroborated | 5 |
| coordinate_named | 1 |
| mill_name_class | 36 |
| unmatched | 68 |
| unmatched_no_registry | 5 |

| Match confidence | Facilities |
| --- | ---: |
| high | 51 |
| low | 1 |
| medium | 36 |
| missing | 73 |

## 3. Rejected code collisions

The eight legacy exact-code matches are collisions, not the same mills:

| FFCM facility | Mills DB code | FFCM site | Mills operator | Mills city | Distance km |
| --- | --- | --- | --- | --- | ---: |
| BC-SAW-308 | BC-SAW308 | Confederate Shake & Shingle Ltd. | Silvermere Forest Products | Maple Ridge | 123.531 |
| BC-SAW-309 | BC-SAW309 | Western Forest Products Inc.-Western FP Inc | Wynndel Box & Lumber | Wynndel sawmill | 578.009 |
| BC-SAW-383 | BC-SAW383 | Canfor Corporation-Fort St. John Division | Beaver Forest Products | Campbell River | 748.655 |
| BC-SAW-384 | BC-SAW384 | Tl'oh Forest Products Inc. | Ardew | Merrit | 533.988 |
| BC-SAW-389 | BC-SAW389 | West Fraser Timber Co. Ltd.-Fraser Lake Mills | Canfor | Canal Flats | 749.477 |
| BC-SAW-418 | BC-SAW418 | InterFor-Grand Forks Sawmill | Downie Timber Ltd. and Selkirk Cedar | Revelstoke | 219.092 |
| BC-SAW-488 | BC-SAW488 | Canfor Corporation-Houston Division | Canfor | Prince George sawmill | 266.079 |
| BC-PLY-410 | BC-PLY410 | Louisiana-Pacific Canada Ltd.-Golden | Savona Specialty Plywood Co. | Savona | 274.815 |

The TSA24 supply anchor also changed from `BC-SAW-488` to `BC-SAW-506`.
`BC-SAW-488` is the FFCM Canfor Houston mill, not the Prince George mill that
the old exact-code join had assumed; `BC-SAW-506` is the FFCM Canfor Prince
George mill at the documented 53.99, -122.69 proxy coordinate.

## 4. Facilities changed by recovered coordinates

### 4.1 Fallback to real NRN road path (65)

These facilities gained a real road path because their recovered coordinate
snapped to the NRN graph.  The previous FFCM TL fallback was still a network
path, not a Euclidean guess.

`BC-BIO-4010`, `BC-BIO-4011`, `BC-BIO-4015`, `BC-BIO-4016`, `BC-BIO-4018`, `BC-BIO-4022`, `BC-BIO-4023`, `BC-PAP-1007`, `BC-PAP-1008`, `BC-PAP-1319`, `BC-PAP-679`, `BC-PAP-938`, `BC-PAP-957`, `BC-PAP-963`, `BC-PAP-964`, `BC-PEL-1141`, `BC-PEL-1650`, `BC-PEL-1653`, `BC-PEL-1654`, `BC-PEL-1655`, `BC-PEL-1657`, `BC-PEL-1658`, `BC-PEL-210`, `BC-PEL-383`, `BC-SAW-1009`, `BC-SAW-1011`, `BC-SAW-1026`, `BC-SAW-114`, `BC-SAW-1253`, `BC-SAW-1276`, `BC-SAW-1287`, `BC-SAW-1288`, `BC-SAW-131`, `BC-SAW-132`, `BC-SAW-1377`, `BC-SAW-1383`, `BC-SAW-1386`, `BC-SAW-1387`, `BC-SAW-141`, `BC-SAW-1437`, `BC-SAW-1467`, `BC-SAW-1692`, `BC-SAW-1703`, `BC-SAW-1708`, `BC-SAW-1740`, `BC-SAW-208`, `BC-SAW-210`, `BC-SAW-242`, `BC-SAW-275`, `BC-SAW-281`, `BC-SAW-284`, `BC-SAW-379`, `BC-SAW-381`, `BC-SAW-383`, `BC-SAW-611`, `BC-SAW-680`, `BC-SAW-682`, `BC-SAW-697`, `BC-SAW-74`, `BC-SAW-904`, `BC-SAW-905`, `BC-SAW-940`, `BC-SAW-977`, `BC-SAW-979`, `BC-SAW-981`

### 4.2 Real path to fallback (10)

These facilities had a real path under the legacy code-collision coordinate;
the corrected coordinate no longer supports the same snap.  They keep the
flagged FFCM TL fallback.

`BC-BIO-4007`, `BC-SAW-1707`, `BC-SAW-1714`, `BC-SAW-1725`, `BC-SAW-1732`, `BC-SAW-2013`, `BC-SAW-551`, `BC-SAW-708`, `BC-SAW-711`, `BC-SAW-730`

### 4.3 Real path to missing (5)

These facilities had a real path under the legacy code-collision coordinate;
the corrected coordinate has no accepted road/TL path and is excluded rather
than given a fabricated distance.

`BC-BIO-4017`, `BC-PAP-591`, `BC-SAW-308`, `BC-SAW-309`, `BC-SAW-945`

## 5. Diagnostic contract evidence

The BC Fibre Database workbooks were parsed as evidence, not as facility
contracts:

- `Sawmill Fibre Allocation Input V3.xls`: 596 source-to-destination residue
  allocation shares across Chips, SawShav, Hog, and Other Biomass.  The values
  are dimensionless shares in [0, 1]; the workbook contains no residue volume.
- `TSA Tenure Apportionment V5.xls`: 40 TSA sheets parsed (32 with positive 2018 apportionment rows), 2018 apportionment classes,
  and licence-level volumes.  The 2018 positive apportionment-class rows total
  38,726,439 m3/y.  The workbook has no facility identifier.
- `contracts_bc_diagnostic.csv`: 146 TSA rows with real volumes and no facility
  ID, 596 residue rows with real shares and no volume, and 6 uniquely matched
  destination facilities.  No row has both a facility ID and a volume.
- Stage A therefore keeps `min=0`, `max=nameplate`, and
  `contract_source=diagnostic_absent` for all 161 facilities.  The table is
  diagnostic/project-legacy evidence, not a set of real supply agreements.

## 6. Caveats

- The Mills DB `facility_n` field is a city or mill-locale label, not a legal
  facility name; matching uses it as evidence only.
- `coordinate_corroborated` and `coordinate_named` matches are medium/low
  confidence and are flagged in `facilities_bc_recovered.csv`.
- The 2018 TSA apportionment is an AAC/tenure benchmark, not a mill contract
  ledger.  Its volumes must not be interpreted as facility supply contracts.
- The sawmill allocation shares are residue-routing shares, not log or residue
  volumes.
