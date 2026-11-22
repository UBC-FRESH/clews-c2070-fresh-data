# National Facility Assignment v3

Generated 2026-11-22T20:51:10+00:00.

**Labels:** `model_estimate`; `observed=false`; `policy_grade=false`.

This artifact adds a provincial capacity-floor sensitivity to assignment v2. Where published plus proxy capacity is below 1.2x the provincial harvest, proxy capacities are scaled proportionally and labelled. Published capacity is never altered. It is not a legal AAC, not an observed allocation, and not policy-grade. No UI or public OSeCAN surface is changed.

## Method

1. Reuse capacity v1 and the v2 local-first allocation rule: local capacity before cross-border, published before proxy, nearest road-adjusted facility first, 500 km cross-border penalty.
2. For each province, compute total finite capacity as published plus proxy over relevant-class records.
3. Compute the floor as provincial harvest x 1.2.
4. If total capacity is below the floor and proxy capacity exists, scale every proxy capacity, including its p25-p75 range, by `(floor - published) / proxy`; leave published capacity unchanged. If no proxy exists, leave capacity unchanged and report the shortfall.
5. Rerun assignment with the floor capacities. There is no unbounded facility; every assignment is bounded by its own finite capacity.

## Floor scaling

| Province | Harvest m3 | Floor m3 | Published m3 | Proxy before m3 | Total before m3 | Scale | Proxy after m3 | Total after m3 | Shortfall m3 | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| BC | 39,978,577 | 47,974,292 | 95,838,409 | 34,941,531 | 130,779,940 | 1.0000 | 34,941,531 | 130,779,940 | 0 | floor_met_no_scaling |
| AB | 22,891,404 | 27,469,685 | 0 | 5,832,026 | 5,832,026 | 4.7101 | 27,469,685 | 27,469,685 | 0 | proxy_scaled_to_floor |
| SK | 4,344,698 | 5,213,637 | 0 | 708,513 | 708,513 | 7.3586 | 5,213,637 | 5,213,637 | 0 | proxy_scaled_to_floor |
| MB | 1,135,236 | 1,362,283 | 0 | 708,513 | 708,513 | 1.9227 | 1,362,283 | 1,362,283 | 0 | proxy_scaled_to_floor |
| ON | 13,493,596 | 16,192,315 | 0 | 9,333,820 | 9,333,820 | 1.7348 | 16,192,315 | 16,192,315 | 0 | proxy_scaled_to_floor |
| QC | 26,674,334 | 32,009,201 | 0 | 44,824,771 | 44,824,771 | 1.0000 | 44,824,771 | 44,824,771 | 0 | floor_met_no_scaling |
| NB | 6,234,700 | 7,481,640 | 0 | 9,168,164 | 9,168,164 | 1.0000 | 9,168,164 | 9,168,164 | 0 | floor_met_no_scaling |
| NS | 2,388,245 | 2,865,894 | 0 | 10,092,720 | 10,092,720 | 1.0000 | 10,092,720 | 10,092,720 | 0 | floor_met_no_scaling |
| PE | 302,210 | 362,652 | 0 | 472,342 | 472,342 | 1.0000 | 472,342 | 472,342 | 0 | floor_met_no_scaling |
| NL | 1,454,038 | 1,744,845 | 0 | 3,922,015 | 3,922,015 | 1.0000 | 3,922,015 | 3,922,015 | 0 | floor_met_no_scaling |
| YT | 43,926 | 52,711 | 0 | 236,171 | 236,171 | 1.0000 | 236,171 | 236,171 | 0 | floor_met_no_scaling |
| NT | 36,376 | 43,651 | 0 | 0 | 0 | 1.0000 | 0 | 0 | 43,651 | shortfall_no_proxy_capacity |
| NU | 0 | 0 | 0 | 0 | 0 | 1.0000 | 0 | 0 | 0 | floor_met_no_scaling |

Scaled records: **49** proxies in AB, SK, MB, ON. Floor shortfall before scaling: **33,698,699 m3/yr** across 5 provinces. Residual after scaling: **43,651 m3/yr** across 1 province.

## Assignment v2 vs v3

| Metric | v2 `published_plus_proxy` | v3 `province_capacity_floor` | Delta v3 - v2 |
|---|---|---|---|
| assigned_m3 | 118,977,339 | 118,977,339 | 0 |
| unassigned_m3 | 0 | 0 | 0 |
| published_m3 | 46,122,056 | 39,978,577 | -6,143,479 |
| proxy_m3 | 72,855,283 | 78,998,762 | 6,143,479 |
| cross_border_m3 | 25,318,437 | 36,376 | -25,282,061 |
| facilities_used | 262 | 201 | -61 |
| max_facility_m3 | 2,162,923 | 8,461,661 | 6,298,739 |
| province_capacity_shortfall_before_m3_y | 33,698,699 | 33,698,699 | 0 |
| province_capacity_shortfall_after_m3_y | 33,698,699 | 43,651 | -33,655,048 |
| provinces_below_floor_before | 5 | 5 | 0 |
| provinces_below_floor_after | 5 | 1 | -4 |
| scaled_proxy_records | 0 | 49 | 49 |

| Share / index | v2 | v3 | Delta |
|---|---|---|---|
| assigned_share | 1.0000 | 1.0000 | 0.0000 |
| proxy_share_of_assigned | 0.6123 | 0.6640 | 0.0516 |
| cross_border_share | 0.2128 | 0.0003 | -0.2125 |
| max_facility_share | 0.0182 | 0.0711 | 0.0529 |
| top5_share | 0.0789 | 0.1648 | 0.0859 |
| hhi | 0.0076 | 0.0135 | 0.0059 |

v3 floor assigns 118,977,339 m3 (100.0% of the offer) with 0 m3 unassigned. v2 assigned 118,977,339 m3 and left 0 m3 unassigned.

## Cross-border and proxy concentration

| Scenario | Assigned m3 | Cross-border m3 | Cross-border share | Proxy m3 | Proxy share | Max facility share | HHI |
|---|---|---|---|---|---|---|---|
| published_only | 68,536,598 | 28,558,021 | 41.7% | 0 | 0.0% | 5.10% | 0.0191 |
| published_plus_proxy | 118,977,339 | 25,318,437 | 21.3% | 72,855,283 | 61.2% | 1.82% | 0.0076 |
| province_capacity_floor | 118,977,339 | 36,376 | 0.0% | 78,998,762 | 66.4% | 7.11% | 0.0135 |

v2 cross-border volume was 25,318,437 m3 (21.3% of assigned). v3 floor cross-border volume is 36,376 m3 (0.0%).

v3 proxy share rises because local proxy capacity replaces cross-border published capacity and because scaled proxies are larger. Max facility share and HHI describe the resulting facility mix; they are not welfare or market-power measures.

## Province totals in `province_capacity_floor`

| Province | Offer m3 | Assigned m3 | Local m3 | Cross-border m3 | Published m3 | Proxy m3 | Unassigned m3 |
|---|---|---|---|---|---|---|---|
| AB | 22,891,404 | 22,891,404 | 22,891,404 | 0 | 0 | 22,891,404 | 0 |
| BC | 39,978,577 | 39,978,577 | 39,978,577 | 0 | 39,978,577 | 0 | 0 |
| MB | 1,135,236 | 1,135,236 | 1,135,236 | 0 | 0 | 1,135,236 | 0 |
| NB | 6,234,700 | 6,234,700 | 6,234,700 | 0 | 0 | 6,234,700 | 0 |
| NL | 1,454,038 | 1,454,038 | 1,454,038 | 0 | 0 | 1,454,038 | 0 |
| NS | 2,388,245 | 2,388,245 | 2,388,245 | 0 | 0 | 2,388,245 | 0 |
| NT | 36,376 | 36,376 | 0 | 36,376 | 0 | 36,376 | 0 |
| NU | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ON | 13,493,596 | 13,493,596 | 13,493,596 | 0 | 0 | 13,493,596 | 0 |
| PE | 302,210 | 302,210 | 302,210 | 0 | 0 | 302,210 | 0 |
| QC | 26,674,334 | 26,674,334 | 26,674,334 | 0 | 0 | 26,674,334 | 0 |
| SK | 4,344,698 | 4,344,698 | 4,344,698 | 0 | 0 | 4,344,698 | 0 |
| YT | 43,926 | 43,926 | 43,926 | 0 | 0 | 43,926 | 0 |

## Largest assignments in `province_capacity_floor`

| Facility | Province | Class | Capacity status | Capacity m3 | Assigned m3 | Utilization | Scale |
|---|---|---|---|---|---|---|---|
| OSM-AB-N11413751583 | AB | PULP | proxy_harvest_scaled | 8,461,661 | 8,461,661 | 100.0% | 4.710 |
| OSM-ON-W299165594 | ON | PULP | proxy_harvest_scaled | 3,116,527 | 3,116,527 | 100.0% | 1.735 |
| OSM-AB-W1189211303 | AB | BIO | proxy_harvest_scaled | 2,934,797 | 2,934,797 | 100.0% | 4.710 |
| OSM-AB-W1216113686 | AB | BIO | proxy_harvest_scaled | 2,934,797 | 2,934,797 | 100.0% | 4.710 |
| BC-BIO-4011 | BC | BIO | published | 2,162,923 | 2,162,923 | 100.0% | 1.000 |
| BC-SAW-1387 | BC | SAW | published | 1,822,248 | 1,822,248 | 100.0% | 1.000 |
| BC-SAW-1253 | BC | SAW | published | 1,811,424 | 1,811,424 | 100.0% | 1.000 |
| OSM-NB-W687974759 | NB | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% | 1.000 |
| OSM-QC-N12499086803 | QC | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% | 1.000 |
| OSM-QC-N7791815148 | QC | PULP | proxy | 1,796,476 | 1,796,476 | 100.0% | 1.000 |

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- The 119 Mm3 case is a planning allocation, not a legal AAC, a sustainable-supply determination, or an observed harvest outcome. No legal/AAC claim is made.
- Published capacity is the 2015 Mills DB/FFCM processing-line infeed proxy carried by national_facility_inventory_v0, not licensed, current, or verified operating capacity.
- Class-median proxies cover 292 relevant records (120.24 Mm3/yr). Each proxy is a BC class median with a p25-p75 range, not a facility measurement.
- 81 published-capacity records (27.30 Mm3/yr) have no coordinate and are excluded from the spatial screen. `published_only` is therefore a lower bound on placement in published capacity, not a full use of it.
- 15 OTHER-class records are excluded before capacity screening. No unbounded facility exists in v3: every assignment row carries a finite capacity, and no relevant record is left without one.
- The allocation remains local-first with a 500 km cross-border ranking penalty. Cross-border volume is a screening result, not an interprovincial trade forecast.
- The 119 Mm3 provincial volume is one ungraded offer per province. No sawlog/pulp/panel/pellet/biomass split is inferred; class totals are recipient facility classes, not feedstock grades.
- Harvest volume is treated one-to-one as facility infeed volume. Moisture, bark, oversize, grade, and recovery conversions are not modelled.
- Distances are haversine from an unweighted ADM1 polygon centroid to the facility coordinate, multiplied by a 1.3 road factor for ranking. No routing, road network, travel time, or cost model is used.
- OSM presence does not establish operating status. Non-operating records are excluded; all other inventory statuses are unknown.
- The class-median proxy assumes BC class structure is transferable to other provinces. That assumption is untested and is a first-order uncertainty, not an observed capacity.
- The unscaled published-plus-proxy scenario is not a published-capacity-maximizing run. Local proxies displace some cross-border published volume because the rule fills local capacity first and ranks cross-border candidates by distance.
- No UI or public OSeCAN surface is changed by this artifact.
- The provincial capacity floor is a documented screening assumption of 1.2x harvest, not an observed capacity requirement, a legal AAC, or evidence that a province can physically or economically process that volume.
- Floor scaling changes proxy capacities only. In v3, 49 proxy records across 4 provinces (AB, SK, MB, ON) are multiplied by one province-wide factor. Every published capacity is unchanged.
- Scaled proxies carry `capacity_status=proxy_harvest_scaled` and `capacity_evidence=class_median_proxy_scaled_to_harvest_floor`. They are still class-median placeholders, not facility measurements; the scale factor is a planning adjustment, not evidence.
- The floor is tested on relevant-class finite capacity, including any unlocated record. No scaled province has unlocated proxy capacity, so its assignable capacity also meets the floor. BC meets the floor on either basis.
- Every province with eligible facility capacity meets the 1.2x floor after scaling. NT has no eligible facility capacity and remains 43,651 m3/yr below its floor, so its offer crosses to the nearest remaining facility. Cross-border volume therefore collapses from the v2 level to this small residual. That is an artefact of the floor assumption and local-first ordering, not evidence of provincial self-sufficiency or of zero interprovincial trade.
- The floor scenario assigns less published capacity than v2 because expanded local proxy capacity displaces cross-border published capacity under the local-first rule. It is not a published-capacity-maximizing run.
- Capacity remains a caveated screening input: published values are 2015 Mills DB/FFCM processing-line infeed proxies and proxies are BC class medians. Scaling does not make either current, verified, licensed, or facility-specific.

## Verification

```bash
.venv/bin/python -m workflows.national.facilities.national_facility_assignment_v3
.venv/bin/pytest tests/test_national_facility_assignment_v3.py
.venv/bin/ruff check workflows/national/facilities/national_facility_assignment_v3.py tests/test_national_facility_assignment_v3.py
```
