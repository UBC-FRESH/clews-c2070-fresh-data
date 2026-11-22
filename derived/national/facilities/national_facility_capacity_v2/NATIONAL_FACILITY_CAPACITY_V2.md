# National Facility Capacity V2

Capacity v1 plus the public Canadian Biomass 2025 pellet-map values converted to finished-pellet m3 at 650 kg/m3. All values are model estimates: `observed=false`, `policy_grade=false`.

## Coverage before and after

| Measure | Capacity v1 | Capacity v2 | Delta |
|---|---|---|---|
| Records | 486 | 519 | 33 |
| Published records | 179 | 212 | 33 |
| Proxy records | 292 | 292 | 0 |
| Not published records | 15 | 15 | 0 |
| Published capacity m3/yr | 95,838,409 | 100,285,178 | 4,446,769 |
| Proxy capacity m3/yr | 120,240,586 | 120,240,586 | 0 |
| Published share of records | 36.8% | 40.8% | 4.0% |
| Proxy share of records | 60.1% | 56.3% | -3.8% |
| Published share of capacity | 44.4% | 45.5% | 1.1% |
| Proxy share of capacity | 55.6% | 54.5% | -1.1% |

## Evidence mix

| Evidence | Records | Capacity m3/yr |
|---|---|---|
| published infeed proxy (2015) | 179 | 95,838,409 |
| published converted (2025 pellet map) | 33 | 4,446,769 |
| class-median proxy | 292 | 120,240,586 |
| not published / unavailable | 15 | 0 |

## Conversion basis

`capacity_m3_y = capacity_tonnes_y / 0.65`

The 650 kg/m3 value is inside the Natural Resources Canada / CAN-CSA-ISO 17225-2 range of 600-750 kg/m3. It is finished-pellet bulk volume, not infeed-equivalent. Converted rows carry `capacity_evidence=published_capacity_converted` and `capacity_basis=published_finished_pellets_converted_650kg_m3`.

## By class

| Class | Records | Published | Proxy | Unavailable |
|---|---|---|---|---|
| SAW | 363 | 121 | 242 | 0 |
| PULP | 45 | 16 | 29 | 0 |
| PANEL | 22 | 17 | 5 | 0 |
| PELLET | 47 | 46 | 1 | 0 |
| BIO | 27 | 12 | 15 | 0 |
| OTHER | 15 | 0 | 0 | 15 |

## By province

| Province | Records | Published | Proxy | Unavailable |
|---|---|---|---|---|
| BC | 276 | 180 | 88 | 8 |
| AB | 20 | 5 | 15 | 0 |
| SK | 3 | 0 | 3 | 0 |
| MB | 5 | 2 | 3 | 0 |
| ON | 35 | 6 | 28 | 1 |
| QC | 121 | 11 | 105 | 5 |
| NB | 24 | 5 | 19 | 0 |
| NS | 20 | 2 | 18 | 0 |
| PE | 2 | 0 | 2 | 0 |
| NL | 12 | 1 | 10 | 1 |
| YT | 1 | 0 | 1 | 0 |

## Validation

- `records_match_inventory`: True
- `unique_facility_ids`: True
- `published_capacity_matches_inventory`: True
- `proxy_range_violations`: 0
- `relevant_records_without_capacity`: 0
- `all_relevant_classes_proxied`: True
- `anchor_minimum_met`: True
- `all_published_rows_have_evidence`: True
- `all_proxy_rows_have_class_median_evidence`: True
- `converted_rows_use_documented_density`: True
- `no_restricted_sources`: True

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- Published capacity is mixed-basis: 2015 Mills DB/FFCM processing-line infeed proxies for BC and converted finished-pellet bulk volume for the 2025 pellet map. The two bases are not interchangeable.
- Converted pellet-map capacities are finished-pellet volume, not infeed-equivalent. No pellet yield, moisture, bark, grade, or recovery conversion is applied.
- Class-median proxies are statistical placeholders, not facility measurements. Their p25-p75 range is reported and they remain labelled `class_median_proxy`.
- The anchor distribution is BC-only and uses infeed-proxy records; converted pellet volumes are excluded from the anchor because their basis differs. Applying BC medians to other provinces assumes comparable class structure.
- No provincial scaling is applied in v2. A province's harvest share does not change its facility proxy capacity.
- OTHER-class records have no BC anchor and no reported pellet capacity; they remain blank and are excluded from assignment.
- These capacities are planning inputs only. They are not a legal/AAC determination, a timber-supply approval, or an observed operating capacity.
- No restricted or proprietary data are used. No UI or public OSeCAN surface is changed by this artifact.
