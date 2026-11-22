# National Facility Inventory V1

Inventory v0 plus the public Canadian Biomass 2025 pellet-map current producers, deduped against existing pellet records. All values are model estimates: `observed=false`, `policy_grade=false`.

## Headline

- Records: **519** (v0: 486; new: 33).
- Published-capacity records: **212**.
- New published pellet records: **32** carrying **4,292,923 m3/yr** of converted finished-pellet volume.
- Pellet-map rows accounted for: **43 / 43**; matched existing: **10**; new: **33**.
- Existing published capacities preserved: **9**; existing unpublished pellet records upgraded: **1**.

## Conversion

`capacity_m3_y = capacity_tonnes_y / 0.65`

The 650 kg/m3 value is inside the Natural Resources Canada / CAN-CSA-ISO 17225-2 graded-wood-pellet bulk-density range of 600-750 kg/m3. The result is finished-pellet bulk volume; no pellet yield or infeed conversion is applied. Converted rows are labelled `published_capacity_converted`.

## Coverage by province

| Province | Records | Published | Unknown | Coordinates | Pellet | New pellet |
|---|---|---|---|---|---|---|
| BC | 276 | 180 | 96 | 195 | 15 | 2 |
| AB | 20 | 5 | 15 | 20 | 5 | 5 |
| SK | 3 | 0 | 3 | 3 | 0 | 0 |
| MB | 5 | 2 | 3 | 5 | 2 | 2 |
| ON | 35 | 6 | 29 | 35 | 6 | 6 |
| QC | 121 | 11 | 110 | 121 | 11 | 10 |
| NB | 24 | 5 | 19 | 24 | 5 | 5 |
| NS | 20 | 2 | 18 | 20 | 2 | 2 |
| PE | 2 | 0 | 2 | 2 | 0 | 0 |
| NL | 12 | 1 | 11 | 12 | 1 | 1 |
| YT | 1 | 0 | 1 | 1 | 0 | 0 |

## Dedupe crosswalk

Every pellet-map row is mapped in `dedup_crosswalk.csv`, including plants that matched an existing pellet record and were not added again. Co-located sawmill and pulp records stay separate because the inventory convention is one record per product line.

## Validation

- `unique_facility_ids`: True
- `base_records_preserved`: True
- `no_duplicate_normalised_pellet_names`: True
- `published_rows_have_capacity`: True
- `unpublished_rows_blank`: True
- `all_capacities_positive`: True
- `all_converted_values_labelled`: True
- `no_restricted_sources`: True
- `pellet_map_rows_accounted`: True

## Caveats

- All values are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- Pellet-map capacities are published finished-pellet tonnes/yr, converted at 650 kg/m3 to finished-pellet bulk volume. They are not infeed-equivalent, observed throughput, or a legal/AAC determination.
- Existing BC published infeed-proxy capacities are preserved even when the pellet map reports a different finished-product value; the two values use different bases.
- There is no legal, AAC, timber-supply, or operating-status claim. Most inventory statuses remain unknown.
- City-centroid coordinates are not plant-gate coordinates; distance-based assignment for those records carries location uncertainty.
- No restricted or proprietary data are used. The public PDF is not redistributed; only the factual extract is stored.
- No UI or public OSeCAN surface is changed by this artifact.
