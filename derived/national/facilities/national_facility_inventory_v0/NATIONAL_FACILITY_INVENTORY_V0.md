# National Facility Inventory v0

Generated 2026-11-22T20:08:57+00:00.

Scope: Canadian forest-product and wood-biomass facilities assembled from the project BC derived facility layer and OpenStreetMap. The inventory is a mapped-record inventory, not a complete national census. Capacity is reported only where the input publishes it; OSM capacity is left blank.

## Record counts by province and class

| Province | Records | Classes | Capacity known | Coordinates | Sources |
|---|---:|---|---:|---:|---|
| BC (British Columbia) | 274 | SAW:194;PULP:24;PANEL:18;PELLET:13;BIO:17;OTHER:8 | 179 | 193/274 | bc_mills_db_2015:179;osm_overpass_canada:95 |
| AB (Alberta) | 15 | SAW:10;PULP:1;PANEL:2;BIO:2 | 0 | 15/15 | osm_overpass_canada:15 |
| SK (Saskatchewan) | 3 | SAW:3 | 0 | 3/3 | osm_overpass_canada:3 |
| MB (Manitoba) | 3 | SAW:3 | 0 | 3/3 | osm_overpass_canada:3 |
| ON (Ontario) | 29 | SAW:24;PULP:1;BIO:3;OTHER:1 | 0 | 29/29 | osm_overpass_canada:29 |
| QC (Quebec) | 111 | SAW:89;PULP:12;PANEL:2;PELLET:1;BIO:2;OTHER:5 | 0 | 111/111 | osm_overpass_canada:111 |
| NB (New Brunswick) | 19 | SAW:16;PULP:3 | 0 | 19/19 | osm_overpass_canada:19 |
| NS (Nova Scotia) | 18 | SAW:12;PULP:3;BIO:3 | 0 | 18/18 | osm_overpass_canada:18 |
| PE (Prince Edward Island) | 2 | SAW:2 | 0 | 2/2 | osm_overpass_canada:2 |
| NL (Newfoundland and Labrador) | 11 | SAW:9;PULP:1;OTHER:1 | 0 | 11/11 | osm_overpass_canada:11 |
| YT (Yukon) | 1 | SAW:1 | 0 | 1/1 | osm_overpass_canada:1 |
| NT (Northwest Territories) | 0 | none | 0 | 0/0 | none |
| NU (Nunavut) | 0 | none | 0 | 0/0 | none |

Total records: **486** across 11 of 13 jurisdictions.

## Capacity coverage

- Capacity known: 179 of 486 records (36.8%).
- All known capacities are BC source proxies; every OSM record is blank with `capacity_status=not_published`.
- Missing capacity is never replaced by zero or a class average.
- Unnamed OSM features retained explicitly: 124 (25.5%); `name` is blank rather than invented.

## Sources and evidence tiers

| Source | Licence | Records |
|---|---|---:|
| `bc_mills_db_2015` | Project-derived BC chain layer; upstream ISED Mills DB 2015 / FFCM proxies. Upstream source is not relicensed here. | 179 |
| `osm_overpass_canada` | ODbL-1.0 | 307 |

Evidence tiers: A = BC record with validated coordinate; B = BC record with missing/invalid coordinate; C = OSM feature with a direct facility tag; D = OSM feature inferred from a mill-like name only.

Tier counts: `{"A": 98, "B": 81, "C": 303, "D": 4}`.

## Deduplication and validation

- OSM features merged into BC records: 32.
- OSM elements discarded as outside Canada or not a Canadian province: 780.
- OSM elements not relevant after tag/name screening: 3356.
- OSM duplicate OSM IDs: 168; duplicate names within 250 m: 3.
- BC coordinates validated: 98 (2 within the 5 km coastal tolerance); missing: 81; dropped after BC polygon check: 0.
- Coordinates must fall inside the named province/territory polygon. BC source points within 5 km of the simplified BC coastline are accepted with a note; BC records with missing coordinates are retained, not dropped.

## Caveats

- No capacity is imputed: OSM records have blank capacity and capacity_status=not_published.
- BC capacities are 2015 Mills DB/FFCM processing-line infeed proxies, not licensed or current operating capacity.
- OSM presence does not establish operating status; status is unknown unless explicit lifecycle tags exist.
- Province/territory coverage is a count of mapped records, not a complete census of Canadian facilities.
- BC source coordinates within 5 km of the simplified BC boundary are accepted with a note; all other coordinates must fall inside the named province or territory.
- No UI or public OSeCAN surface is changed by this artifact.

## Reproduce and verify

```bash
.venv/bin/python -m workflows.national.facilities.national_facility_inventory
.venv/bin/pytest tests/test_national_facility_inventory.py
.venv/bin/ruff check workflows/national/facilities tests/test_national_facility_inventory.py
```

Overpass responses are cached under `tmp/national_facility_inventory/osm_cache/` for this build. The OSM snapshot timestamp is recorded in `summary.json` and `manifest.json`.
