# National Facility Assignment v2

Generated 2026-11-22T20:31:03+00:00.

**Labels:** `model_estimate`; `observed=false`; `policy_grade=false`.

This artifact replaces the v1 unbounded-unknown diagnostic with two bounded scenarios: published capacity only, and published plus class-median proxy capacity. Every assignment row has a finite capacity. It is not a legal AAC, not an observed allocation, and not policy-grade. No UI or public OSeCAN surface is changed.

## Method

1. Read capacity v1, which carries 179 published values and 292 labelled class-median proxies.
2. Build one ungraded supply offer per province from `119m.csv` (118,977,339 m3 nationally).
3. Scenario A (`published_only`) admits only published-capacity facilities. Scenario B (`published_plus_proxy`) admits published and proxy facilities.
4. Local province first. Within a province, published capacity is filled before proxy capacity, nearest road-adjusted facility first.
5. Cross-border facilities are considered only after local capacity is exhausted, ranked by road distance plus a 500 km penalty.
6. Every facility capacity is finite. There is no unbounded sink and no facility-level capacity is fabricated.

## Capacity basis

| Measure | Records | Capacity m3/yr |
|---|---|---|
| Relevant facility records | 471 |  |
| Published, all | 179 | 95,838,409 |
| Published, located and screenable | 98 | 68,536,598 |
| Published, unlocated and excluded | 81 | 27,301,812 |
| Class-median proxy, all | 292 | 120,240,586 |
| Class-median proxy, located and screenable | 292 | 120,240,586 |
| Class-median proxy, unlocated | 0 | 0 |
| OTHER-class records (excluded) | 15 |  |
| Relevant records without capacity | 0 |  |

The unlocated published capacity is excluded from the spatial screen. Scenario A is therefore a lower bound on placement in published capacity.

## Scenario comparison

| Scenario | Assigned m3 | Unassigned m3 | Published m3 | Proxy m3 | Cross-border m3 | Facilities | Max facility share | HHI |
|---|---|---|---|---|---|---|---|---|
| published_only | 68,536,598 | 50,440,742 | 68,536,598 | 0 | 28,558,021 | 98 | 5.10% | 0.0191 |
| published_plus_proxy | 118,977,339 | 0 | 46,122,056 | 72,855,283 | 25,318,437 | 262 | 1.82% | 0.0076 |

Scenario B assigns 50,440,742 m3 more than scenario A. Proxy capacity supplies 61.2% of scenario B's assigned volume.

Scenario B uses less published capacity than scenario A. Local proxy capacity absorbs demand that would otherwise cross a border in scenario A, and cross-border candidates are ranked by distance rather than capacity status. Scenario B is a bounded-absorption screening run, not a published-capacity-maximizing run.

## Province totals

### `published_only`

| Province | Offer m3 | Assigned m3 | Local m3 | Cross-border m3 | Published m3 | Proxy m3 | Unassigned m3 |
|---|---|---|---|---|---|---|---|
| AB | 22,891,404 | 1,883,687 | 0 | 1,883,687 | 1,883,687 | 0 | 21,007,717 |
| BC | 39,978,577 | 39,978,577 | 39,978,577 | 0 | 39,978,577 | 0 | 0 |
| MB | 1,135,236 | 0 | 0 | 0 | 0 | 0 | 1,135,236 |
| NB | 6,234,700 | 0 | 0 | 0 | 0 | 0 | 6,234,700 |
| NL | 1,454,038 | 0 | 0 | 0 | 0 | 0 | 1,454,038 |
| NS | 2,388,245 | 0 | 0 | 0 | 0 | 0 | 2,388,245 |
| NT | 36,376 | 0 | 0 | 0 | 0 | 0 | 36,376 |
| NU | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ON | 13,493,596 | 0 | 0 | 0 | 0 | 0 | 13,493,596 |
| PE | 302,210 | 0 | 0 | 0 | 0 | 0 | 302,210 |
| QC | 26,674,334 | 26,674,334 | 0 | 26,674,334 | 26,674,334 | 0 | 0 |
| SK | 4,344,698 | 0 | 0 | 0 | 0 | 0 | 4,344,698 |
| YT | 43,926 | 0 | 0 | 0 | 0 | 0 | 43,926 |

### `published_plus_proxy`

| Province | Offer m3 | Assigned m3 | Local m3 | Cross-border m3 | Published m3 | Proxy m3 | Unassigned m3 |
|---|---|---|---|---|---|---|---|
| AB | 22,891,404 | 22,891,404 | 5,832,026 | 17,059,378 | 5,092,208 | 17,799,196 | 0 |
| BC | 39,978,577 | 39,978,577 | 39,978,577 | 0 | 39,978,577 | 0 | 0 |
| MB | 1,135,236 | 1,135,236 | 708,513 | 426,723 | 0 | 1,135,236 | 0 |
| NB | 6,234,700 | 6,234,700 | 6,234,700 | 0 | 0 | 6,234,700 | 0 |
| NL | 1,454,038 | 1,454,038 | 1,454,038 | 0 | 0 | 1,454,038 | 0 |
| NS | 2,388,245 | 2,388,245 | 2,388,245 | 0 | 0 | 2,388,245 | 0 |
| NT | 36,376 | 36,376 | 0 | 36,376 | 0 | 36,376 | 0 |
| NU | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ON | 13,493,596 | 13,493,596 | 9,333,820 | 4,159,776 | 0 | 13,493,596 | 0 |
| PE | 302,210 | 302,210 | 302,210 | 0 | 0 | 302,210 | 0 |
| QC | 26,674,334 | 26,674,334 | 26,674,334 | 0 | 0 | 26,674,334 | 0 |
| SK | 4,344,698 | 4,344,698 | 708,513 | 3,636,185 | 1,051,271 | 3,293,427 | 0 |
| YT | 43,926 | 43,926 | 43,926 | 0 | 0 | 43,926 | 0 |

## Class totals

Recipient facility classes, not feedstock grades. The 119 Mm3 offer is ungraded; no sawlog/pulp/panel/pellet/biomass split is inferred.

| Facility class | `published_only` m3 | `published_plus_proxy` m3 |
|---|---|---|
| SAW | 35,420,846 | 65,322,641 |
| PULP | 16,939,282 | 32,308,342 |
| PANEL | 3,343,592 | 3,866,758 |
| PELLET | 5,395,600 | 5,625,200 |
| BIO | 7,437,278 | 11,854,398 |

## Concentration and overflow

| Scenario | Facilities used | Top-1 share | Top-5 share | HHI | Unassigned provinces |
|---|---|---|---|---|---|
| published_only | 98 | 5.10% | 20.77% | 0.0191 | 10 |
| published_plus_proxy | 262 | 1.82% | 7.89% | 0.0076 | 0 |

HHI is the sum of squared facility shares of assigned volume (0-1 scale). No single facility can absorb unbounded volume because every facility has a finite capacity.

### Unassigned and overflow

| Scenario | Province | Unassigned m3 | Share of offer |
|---|---|---|---|
| published_only | AB | 21,007,717 | 91.8% |
| published_only | MB | 1,135,236 | 100.0% |
| published_only | NB | 6,234,700 | 100.0% |
| published_only | NL | 1,454,038 | 100.0% |
| published_only | NS | 2,388,245 | 100.0% |
| published_only | NT | 36,376 | 100.0% |
| published_only | ON | 13,493,596 | 100.0% |
| published_only | PE | 302,210 | 100.0% |
| published_only | SK | 4,344,698 | 100.0% |
| published_only | YT | 43,926 | 100.0% |

Overflow is demand that no eligible located facility could take under the scenario's capacity rule. It is not a statement that the province lacks physical wood or legal harvest rights.

## Largest assignments in `published_plus_proxy`

| Facility | Province | Class | Capacity status | Capacity m3 | Assigned m3 | Utilization |
|---|---|---|---|---|---|---|
| BC-BIO-4011 | BC | BIO | published | 2,162,923 | 2,162,923 | 100.0% |
| BC-SAW-1387 | BC | SAW | published | 1,822,248 | 1,822,248 | 100.0% |
| BC-SAW-1253 | BC | SAW | published | 1,811,424 | 1,811,424 | 100.0% |
| OSM-AB-N11413751583 | AB | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% |
| OSM-NB-W687974759 | NB | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% |
| OSM-ON-W299165594 | ON | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% |
| OSM-QC-N12499086803 | QC | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% |
| OSM-QC-N7791815148 | QC | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% |
| OSM-QC-N8743600291 | QC | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% |
| OSM-QC-N7781923282 | QC | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% |

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- The 119 Mm3 case is a planning allocation, not a legal AAC, a sustainable-supply determination, or an observed harvest outcome. No legal/AAC claim is made.
- Published capacity is the 2015 Mills DB/FFCM processing-line infeed proxy carried by national_facility_inventory_v0, not licensed, current, or verified operating capacity.
- Class-median proxies cover 292 relevant records (120.24 Mm3/yr). Each proxy is a BC class median with a p25-p75 range, not a facility measurement.
- 81 published-capacity records (27.30 Mm3/yr) have no coordinate and are excluded from the spatial screen. `published_only` is therefore a lower bound on placement in published capacity, not a full use of it.
- 15 OTHER-class records are excluded before capacity screening. No unbounded facility exists in v2: every assignment row carries a finite capacity, and no relevant record is left without one.
- The allocation remains local-first with a 500 km cross-border ranking penalty. Cross-border volume is a screening result, not an interprovincial trade forecast.
- The 119 Mm3 provincial volume is one ungraded offer per province. No sawlog/pulp/panel/pellet/biomass split is inferred; class totals are recipient facility classes, not feedstock grades.
- Harvest volume is treated one-to-one as facility infeed volume. Moisture, bark, oversize, grade, and recovery conversions are not modelled.
- Distances are haversine from an unweighted ADM1 polygon centroid to the facility coordinate, multiplied by a 1.3 road factor for ranking. No routing, road network, travel time, or cost model is used.
- OSM presence does not establish operating status. Non-operating records are excluded; all other inventory statuses are unknown.
- The class-median proxy assumes BC class structure is transferable to other provinces. That assumption is untested and is a first-order uncertainty, not an observed capacity.
- Scenario B is not a published-capacity-maximizing run. Local proxies displace some cross-border published volume because the rule fills local capacity first and ranks cross-border candidates by distance.
- No UI or public OSeCAN surface is changed by this artifact.

## Verification

```bash
.venv/bin/python -m workflows.national.facilities.national_facility_assignment_v2
.venv/bin/pytest tests/test_national_facility_assignment_v2.py
.venv/bin/ruff check workflows/national/facilities/national_facility_assignment_v2.py tests/test_national_facility_assignment_v2.py
```
