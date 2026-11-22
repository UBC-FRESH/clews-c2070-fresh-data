# National Facility Assignment V5

Rerun of the 119 Mm3 harvest assignment on capacity v3, which adds Quebec MRNF 2026 permitted mill volumes and five per-mill Ontario/Alberta company disclosures. All values are model estimates: `observed=false`, `policy_grade=false`.

## Primary scenario: published plus proxy

| Metric | V4 | V5 | Delta v5-v4 |
|---|---|---|---|
| Assigned m3 | 118,977,339 | 118,977,339 | 0 |
| Published m3 | 49,428,073 | 78,658,348 | 29,230,275 |
| Proxy m3 | 69,549,266 | 40,318,991 | -29,230,275 |
| Proxy share of assigned | 58.5% | 33.9% | -24.6% |
| Cross-border m3 | 23,689,207 | 21,901,938 | -1,787,269 |
| Cross-border share | 19.9% | 18.4% | -1.5% |
| HHI (0-1) | 0.0074 | 0.0075 | +0.0002 |
| Largest facility share | 1.82% | 1.82% | +0.00% |

## Provincial capacity v4 to v5

| Province | V4 published | V5 published | V4 proxy scale | V5 proxy scale | V4 shortfall | V5 shortfall |
|---|---|---|---|---|---|---|
| BC | 96,053,794 | 96,053,794 | 1.00 | 1.00 | 0 | 0 |
| AB | 1,161,538 | 2,159,818 | 4.51 | 4.50 | 0 | 0 |
| SK | 0 | 0 | 7.36 | 7.36 | 0 | 0 |
| MB | 21,538 | 21,538 | 1.89 | 1.89 | 0 | 0 |
| ON | 446,154 | 1,685,154 | 1.69 | 1.59 | 0 | 0 |
| QC | 1,607,692 | 65,694,025 | 1.00 | 1.00 | 0 | 0 |
| NB | 745,231 | 745,231 | 1.00 | 1.00 | 0 | 0 |
| NS | 230,769 | 230,769 | 1.00 | 1.00 | 0 | 0 |
| PE | 0 | 0 | 1.00 | 1.00 | 0 | 0 |
| NL | 18,462 | 18,462 | 1.00 | 1.00 | 0 | 0 |
| YT | 0 | 0 | 1.00 | 1.00 | 0 | 0 |
| NT | 0 | 0 | 1.00 | 1.00 | 43,651 | 43,651 |
| NU | 0 | 0 | 1.00 | 1.00 | 0 | 0 |

## Validation

- `conservation_gap_m3`: {'published_only': 0.0, 'published_plus_proxy': 0.0, 'province_capacity_floor': 0.0}
- `known_capacity_violations`: 0
- `unbounded_assignments`: 0
- `non_operating_assignments`: 0
- `max_utilization`: {'published_only': 1.0, 'published_plus_proxy': 1.0, 'province_capacity_floor': 1.0}
- `max_single_facility_share`: {'published_only': 0.02940290585133787, 'published_plus_proxy': 0.018179281698593643, 'province_capacity_floor': 0.0680222363910337}
- `capacity_evidence`: {'class_median_proxy': {'capacity_m3_y': 104733008.0, 'records': 241}, 'published_authorized_consumption': {'capacity_m3_y': 64086333.0, 'records': 216}, 'published_capacity_converted': {'capacity_m3_y': 4446769.2307710005, 'records': 33}, 'published_mills_db_2015_infeed_proxy': {'capacity_m3_y': 95838409.22565, 'records': 179}, 'published_sawn_output_converted': {'capacity_m3_y': 2237280.0, 'records': 5}}
- `published_evidence_accepted`: ['published_authorized_consumption', 'published_capacity_converted', 'published_mills_db_2015_infeed_proxy', 'published_sawn_output_converted']
- `proxy_evidence`: class_median_proxy
- `comparison_rows`: 36
- `no_unbounded_facility`: True
- `all_facilities_finite_capacity`: True
- `no_restricted_sources`: True
- `no_ui_or_public_osecan_change`: True
- `v4_baseline_scenarios`: ['province_capacity_floor', 'published_only', 'published_plus_proxy']
- `capacity_v3_record_count`: 689

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- The 119 Mm3 case is a planning allocation, not a legal AAC, a sustainable-supply determination, or an observed harvest outcome.
- Capacity is mixed-basis: 2015 Mills DB/FFCM infeed proxies, converted 2025 finished-pellet bulk volume, Quebec 2026 permitted input volume, converted company sawn-lumber output, and BC class-median proxies. The bases are not interchangeable.
- Quebec permitted consumption is a regulatory ceiling, not observed throughput. Company sawn-lumber capacities are output, not log intake, and understate roundwood consumption.
- The allocation is local-first with a 500 km cross-border penalty. Cross-border volume is a screening result, not an interprovincial trade forecast.
- The 1.2x provincial floor is a documented sensitivity assumption, not an observed capacity requirement or evidence of provincial self-sufficiency.
- No unbounded facility exists in v5: every assignment row carries a finite capacity and every relevant record has either published or proxy capacity.
- No restricted or proprietary data are used. No UI or public OSeCAN surface is changed by this artifact.
