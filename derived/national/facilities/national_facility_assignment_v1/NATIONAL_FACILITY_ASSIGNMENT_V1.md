# National Facility Assignment v1

Generated 2026-11-22T20:21:33+00:00.

**Labels:** `model_estimate`; `observed=false`; `policy_grade=false`.

This artifact screens the 119 Mm3 provincial harvest case against the national facility inventory v0. It is not a legal AAC, not an observed allocation, and not policy-grade. No UI or public OSeCAN surface is changed.

## Assignment rule

1. Build one ungraded supply offer per province from `119m.csv` (118,977,339 m3 nationally).
2. Eligible facilities are located inventory records in SAW, PULP, PANEL, PELLET, or BIO. OTHER records and non-operating records are excluded.
3. Local province first. Local known-capacity facilities are filled before local unknown-capacity proxies, nearest road-adjusted distance first.
4. Known capacity is a hard maximum. Unknown capacity is an explicit `capacity_unbounded_proxy`; no capacity number is invented for it.
5. Cross-border facilities are considered only after local capacity is exhausted. They are ranked by road distance plus a 500 km screening penalty.
6. Province residuals compete for shared cross-border capacity in descending residual volume, then province code. This follows the existing `assign_feedstock` ordering convention.
7. Distances are haversine from an unweighted ADM1 polygon centroid to the facility coordinate; the ranking road distance applies a 1.3 factor. No routing or cost model is used.

## Capacity basis

| Measure | Records | Capacity m3/yr |
|---|---:|---:|
| Relevant facility records | 471 | |
| Known capacity, all | 179 | 95,838,409 |
| Known capacity, located and screenable | 98 | 68,536,598 |
| Known capacity, unlocated and excluded | 81 | 27,301,812 |
| Unknown capacity | 292 | not published |
| Excluded OTHER class | 15 | |

The 81 unlocated known-capacity records have no coordinate. They are not assigned by distance. Consequently `known_only` is a lower bound on placement in published capacity, not a full use of published capacity.

## Province totals

### `known_only`

| Province | Offer m3 | Assigned m3 | Local m3 | Cross-border m3 | Known m3 | Unknown m3 | Unassigned m3 |
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

### `unbounded_unknown`

| Province | Offer m3 | Assigned m3 | Local m3 | Cross-border m3 | Known m3 | Unknown m3 | Unassigned m3 |
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

## Class totals

Recipient facility classes, not feedstock grades. The 119 Mm3 offer is ungraded; no sawlog/pulp/panel/pellet/biomass split is inferred.

| Facility class | `known_only` m3 | `unbounded_unknown` m3 |
|---|---|---|
| SAW | 35,420,846 | 64,769,465 |
| PULP | 16,939,282 | 5,105,974 |
| PANEL | 3,343,592 | 2,291,299 |
| PELLET | 5,395,600 | 4,841,690 |
| BIO | 7,437,278 | 41,968,911 |

## Known versus unknown capacity

| Scenario | Assigned m3 | Known-capacity m3 | Unknown-capacity m3 | Unknown share | Cross-border m3 | Facilities used |
|---|---|---|---|---|---|---|
| known_only | 68,536,598 | 68,536,598 | 0 | 0.0% | 28,558,021 | 98 |
| unbounded_unknown | 118,977,339 | 39,978,577 | 78,998,762 | 66.4% | 36,376 | 63 |

Known-capacity records exist only in BC. In `known_only`, a province without local known capacity must either cross a provincial border or overflow. This is an inventory coverage result, not an interprovincial trade forecast.

`unbounded_unknown` is deliberately permissive: every eligible unknown-capacity facility can absorb unlimited volume. The volume shown on those facilities is a scenario artefact, not evidence of available or permitted capacity.

## Unassigned and overflow

| Scenario | Province | Unassigned m3 | Share of offer |
|---|---|---|---|
| known_only | AB | 21,007,717 | 91.8% |
| known_only | MB | 1,135,236 | 100.0% |
| known_only | NB | 6,234,700 | 100.0% |
| known_only | NL | 1,454,038 | 100.0% |
| known_only | NS | 2,388,245 | 100.0% |
| known_only | NT | 36,376 | 100.0% |
| known_only | ON | 13,493,596 | 100.0% |
| known_only | PE | 302,210 | 100.0% |
| known_only | SK | 4,344,698 | 100.0% |
| known_only | YT | 43,926 | 100.0% |

Overflow is demand that no eligible located facility could take under the scenario's capacity rule. It is not a statement that the province lacks physical wood or legal harvest rights.

## Largest assignments in `unbounded_unknown`

| Facility | Province | Class | Capacity status | Assigned m3 |
|---|---|---|---|---|
| OSM-QC-W1423131952 | QC | SAW | unknown | 26,674,334 |
| OSM-AB-W1189211303 | AB | BIO | unknown | 22,891,404 |
| OSM-ON-W253815017 | ON | BIO | unknown | 13,493,596 |
| OSM-NB-W1516388704 | NB | SAW | unknown | 6,234,700 |
| OSM-SK-W432827092 | SK | SAW | unknown | 4,344,698 |
| OSM-NS-W108285234 | NS | SAW | unknown | 2,388,245 |
| BC-BIO-4011 | BC | BIO | known | 2,162,923 |
| BC-SAW-1387 | BC | SAW | known | 1,822,248 |
| BC-SAW-1253 | BC | SAW | known | 1,811,424 |
| BC-PAP-511 | BC | PULP | known | 1,609,072 |

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- The 119 Mm3 case is a planning allocation, not a legal AAC, a sustainable-supply determination, or an observed harvest outcome. No legal/AAC claim is made.
- Known capacity is the 2015 Mills DB/FFCM processing-line infeed proxy carried by national_facility_inventory_v0, not licensed, current, or verified operating capacity.
- All known-capacity records are in BC. In `known_only`, every non-BC province must either cross a provincial border or overflow. That is a property of the inventory, not an interprovincial trade forecast.
- 81 known-capacity records (27.30 Mm3/yr) have no coordinate and are excluded from the spatial screen. `known_only` is therefore a lower bound on placement in published capacity, not a full use of it.
- 292 relevant facilities have no published capacity. `unbounded_unknown` treats them as non-binding absorbers (`capacity_unbounded_proxy`) and does not assign them an invented capacity. Volume placed on them is not evidence of available, permitted, or operating capacity.
- The 119 Mm3 provincial volume is one ungraded offer per province. No sawlog/pulp/panel/pellet/biomass split is inferred, and class totals are recipient facility classes, not feedstock grades.
- Harvest volume is treated one-to-one as facility infeed volume. Moisture, bark, oversize, grade, and recovery conversions are not modelled.
- Distances are haversine from an unweighted ADM1 polygon centroid to the facility coordinate, multiplied by a 1.3 road factor for ranking. No routing, road network, travel time, or cost model is used.
- Cross-border assignments carry a 500 km screening penalty and are considered only after local capacity is exhausted. The penalty is an assumption, not a transport-cost estimate.
- OSM presence does not establish operating status. 1 non-operating record(s) are excluded; all other inventory statuses are unknown.
- No facility data are introduced. Coordinates, classes, statuses, and published capacities come from national_facility_inventory_v0.
- No UI or public OSeCAN surface is changed by this artifact.

## Verification

```bash
.venv/bin/python -m workflows.national.facilities.national_facility_assignment
.venv/bin/pytest tests/test_national_facility_assignment.py
.venv/bin/ruff check workflows/national/facilities/national_facility_assignment.py tests/test_national_facility_assignment.py
```
