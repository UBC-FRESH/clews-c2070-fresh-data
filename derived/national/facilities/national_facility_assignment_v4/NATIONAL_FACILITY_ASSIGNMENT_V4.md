# National Facility Assignment V4

Updated-evidence rerun of the 119 Mm3 harvest assignment on inventory v1 / capacity v2. All values are model estimates: `observed=false`, `policy_grade=false`. No legal/AAC claim is made.

## Primary scenario: published plus updated proxies

| Metric | V3 | V4 | Delta v4-v3 |
|---|---|---|---|
| Assigned m3 | 118,977,339 | 118,977,339 | 0 |
| Published m3 | 46,122,056 | 49,428,073 | 3,306,017 |
| Proxy m3 | 72,855,283 | 69,549,266 | -3,306,017 |
| Proxy share of assigned | 61.2% | 58.5% | -2.8% |
| Cross-border m3 | 25,318,437 | 23,689,207 | -1,629,231 |
| Cross-border share | 21.3% | 19.9% | -1.4% |
| Max facility share | 1.82% | 1.82% | -0.00% |
| HHI | 0.00757 | 0.00737 | -0.00020 |

## All scenarios

| Scenario | Assigned m3 | Cross-border m3 | Proxy share | Max facility share | HHI | Facilities |
|---|---|---|---|---|---|---|
| published_only | 72,983,367 | 28,773,405 | 0.0% | 4.79% | 0.01707 | 131 |
| published_plus_proxy | 118,977,339 | 23,689,207 | 58.5% | 1.82% | 0.00737 | 289 |
| province_capacity_floor | 118,977,339 | 36,376 | 62.8% | 6.81% | 0.01273 | 231 |

## Capacity coverage

| Measure | Capacity v1 | Capacity v2 |
|---|---|---|
| Published records | 179 | 212 |
| Proxy records | 292 | 292 |
| Published capacity m3/yr | 95,838,409 | 100,285,178 |
| Proxy capacity m3/yr | 120,240,586 | 120,240,586 |
| Published share of capacity | 44.4% | 45.5% |

## Province capacity comparison

| Province | V3 published | V4 published | V3 proxy scale | V4 proxy scale | V3 shortfall | V4 shortfall |
|---|---|---|---|---|---|---|
| BC | 95,838,409 | 96,053,794 | 1.00 | 1.00 | 0 | 0 |
| AB | 0 | 1,161,538 | 4.71 | 4.51 | 0 | 0 |
| SK | 0 | 0 | 7.36 | 7.36 | 0 | 0 |
| MB | 0 | 21,538 | 1.92 | 1.89 | 0 | 0 |
| ON | 0 | 446,154 | 1.73 | 1.69 | 0 | 0 |
| QC | 0 | 1,607,692 | 1.00 | 1.00 | 0 | 0 |
| NB | 0 | 745,231 | 1.00 | 1.00 | 0 | 0 |
| NS | 0 | 230,769 | 1.00 | 1.00 | 0 | 0 |
| PE | 0 | 0 | 1.00 | 1.00 | 0 | 0 |
| NL | 0 | 18,462 | 1.00 | 1.00 | 0 | 0 |
| YT | 0 | 0 | 1.00 | 1.00 | 0 | 0 |
| NT | 0 | 0 | 1.00 | 1.00 | 43,651 | 43,651 |
| NU | 0 | 0 | 1.00 | 1.00 | 0 | 0 |

## Validation

- `conservation_gap_m3`: {'published_only': 0.0, 'published_plus_proxy': 0.0, 'province_capacity_floor': 0.0}
- `known_capacity_violations`: 0
- `unbounded_assignments`: 0
- `non_operating_assignments`: 0
- `max_utilization`: {'published_only': 1.0, 'published_plus_proxy': 1.0, 'province_capacity_floor': 1.0}
- `max_single_facility_share`: {'published_only': 0.04793255853750423, 'published_plus_proxy': 0.018179281698593643, 'province_capacity_floor': 0.0681126794815744}
- `capacity_evidence`: {'not_published_records': 15, 'proxy_capacity_m3_y': 120240586.0, 'proxy_records': 292, 'published_converted_capacity_m3_y': 4446769.2307710005, 'published_converted_records': 33, 'published_infeed_proxy_capacity_m3_y': 95838409.22565, 'published_infeed_proxy_records': 179}
- `published_evidence_accepted`: ['published_capacity_converted', 'published_mills_db_2015_infeed_proxy']
- `proxy_evidence`: class_median_proxy
- `v3_baseline_scenarios`: ['province_capacity_floor', 'published_only', 'published_plus_proxy']
- `comparison_rows`: 36
- `no_unbounded_facility`: True
- `all_facilities_finite_capacity`: True
- `no_restricted_sources`: True
- `no_ui_or_public_osecan_change`: True

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- The 119 Mm3 case is a planning allocation, not a legal AAC, a sustainable-supply determination, or an observed harvest outcome. No legal/AAC claim is made.
- Capacity is mixed-basis: 2015 Mills DB/FFCM infeed proxies, converted 2025 pellet-map finished-pellet bulk volume, and BC class-median proxies. The bases are not interchangeable.
- Converted pellet capacity is finished-product volume, not infeed-equivalent; no pellet yield, moisture, bark, grade, or recovery conversion is modelled.
- New pellet facilities without a plant-gate coordinate use city centroids; their distance-based assignment carries location uncertainty.
- The allocation is local-first with a 500 km cross-border penalty. Cross-border volume is a screening result, not an interprovincial trade forecast.
- The 1.2x provincial floor is a documented sensitivity assumption, not an observed capacity requirement or evidence of provincial self-sufficiency.
- No unbounded facility exists in v4: every assignment row carries a finite capacity and every relevant record has either published or proxy capacity.
- No restricted or proprietary data are used. No UI or public OSeCAN surface is changed by this artifact.
