# National Facility Capacity V3

Capacity v2 plus Quebec MRNF 2026 permitted mill volumes and five per-mill Ontario/Alberta company disclosures. All values are model estimates: `observed=false`, `policy_grade=false`.

## Extraction and match

- Quebec source rows: 242 (19 category-8 rows without a volume excluded)
- Quebec matched to inventory v1: 49
- Quebec new records: 167
- Company source rows: 5
- Company matched to inventory v1: 2
- Company new records: 3

## Coverage v2 to v3

| Measure | Capacity v2 | Capacity v3 | Delta |
|---|---|---|---|
| Records | 519 | 689 | 170 |
| Published records | 212 | 433 | 221 |
| Proxy records | 292 | 241 | -51 |
| Not published records | 15 | 15 | 0 |
| Published capacity m3/yr | 100,285,178 | 166,608,791 | 66,323,613 |
| Proxy capacity m3/yr | 120,240,586 | 104,733,008 | -15,507,578 |
| Total capacity m3/yr | 220,525,764 | 271,341,799 | 50,816,035 |
| Published share of records | 40.8% | 62.8% | +22.0% |
| Proxy share of records | 56.3% | 35.0% | -21.3% |
| Published share of capacity | 45.5% | 61.4% | +15.9% |
| Proxy share of capacity | 54.5% | 38.6% | -15.9% |

## Published evidence mix

| Evidence | Records | Capacity m3/yr |
|---|---:|---:|
| class_median_proxy | 241 | 104,733,008 |
| published_authorized_consumption | 216 | 64,086,333 |
| published_capacity_converted | 33 | 4,446,769 |
| published_mills_db_2015_infeed_proxy | 179 | 95,838,409 |
| published_sawn_output_converted | 5 | 2,237,280 |

## Validation

- `unique_facility_ids`: True
- `all_published_rows_have_accepted_evidence`: True
- `all_proxy_rows_have_class_median_evidence`: True
- `all_capacities_non_negative`: True
- `all_new_rows_are_published`: True
- `record_conservation`: True
- `no_restricted_sources`: True

## Caveats

- All values are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- Capacity remains mixed-basis: BC 2015 infeed proxies, converted 2025 finished-pellet bulk volume, Quebec 2026 permitted input volume, and converted company sawn-lumber output. The bases are not interchangeable.
- Quebec permitted consumption is a regulatory ceiling, not observed throughput, and a permit does not prove current operation.
- The Ontario and Alberta company capacities are sawn-lumber output converted at 2.36 m3/Mfbm. They are not log-intake equivalents and understate the roundwood a sawmill can consume.
- Ontario's public 2026 mill list has no facility capacity; it is used only for names, types, cities, and coordinates. Alberta's public mill directory is historical and was not used for current capacity.
- Class-median proxies remain statistical placeholders for blank relevant-class records, not facility measurements.
- No legal/AAC determination, timber-supply approval, or observed operating capacity is made.
- No restricted or proprietary data are used. No UI or public OSeCAN surface is changed.
