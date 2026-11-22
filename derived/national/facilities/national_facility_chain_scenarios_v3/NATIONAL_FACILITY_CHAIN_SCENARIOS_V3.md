# National Facility Chain Scenarios V3

Multi-scenario 100/119/150 Mm3 facility assignment and product/residue chain on inventory v1 / capacity v3 with 1.2x provincial floor. All values are model estimates: `observed=false`, `policy_grade=false`. No legal/AAC claim is made.

## Scenarios

| Scenario | Harvest Mm3 | Source | Capacity case |
|---|---|---|---|
| 100m | 100.000 | provincial_allocation/100m.csv | province_capacity_floor |
| 119m | 118.977 | provincial_allocation/119m.csv | province_capacity_floor |
| 150m | 150.000 | provincial_allocation/150m.csv | province_capacity_floor |

## Assignment by scenario

| Scenario | Assigned Mm3 | Unassigned m3 | Cross-border Mm3 | Proxy share | Facilities | Max facility share | HHI | Capacity utilization |
|---|---|---|---|---|---|---|---|---|
| 100m | 100.000 | 0 | 0.031 | 39.7% | 185 | 6.61% | 0.01354 | 37.7% |
| 119m | 118.977 | 0 | 0.036 | 39.9% | 208 | 6.80% | 0.01287 | 43.5% |
| 150m | 150.000 | 0 | 0.036 | 43.9% | 242 | 7.24% | 0.01350 | 51.1% |

## Products/residue by scenario

| Scenario | Sawlog product Mm3 | Pulp product Million odt | Panel product Mm3 | Pellet product Million odt | Bio product GWh | Process residue PJ | Harvest gross PJ | Harvest recoverable PJ | Total gross PJ | Total recoverable PJ |
|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 40.736 | 6.380 | 4.459 | 3.991 | 710.4 | 442.11 | 141.02 | 100.35 | 583.12 | 542.46 |
| 119m | 48.467 | 7.590 | 5.305 | 4.748 | 845.2 | 526.01 | 167.78 | 119.40 | 693.78 | 645.40 |
| 150m | 61.104 | 9.569 | 6.688 | 5.986 | 1,065.6 | 663.16 | 211.53 | 150.53 | 874.68 | 813.69 |

## Capacity/proxy/overflow

| Scenario | Eligible capacity Mm3/yr | Published assigned Mm3 | Proxy assigned Mm3 | Capacity utilization | Global capacity binding | Local binding provinces | Unassigned m3 | Overflow m3 |
|---|---|---|---|---|---|---|---|---|
| 100m | 265.012 | 60.294 | 39.706 | 37.7% | false | NT | 0 | 0 |
| 119m | 273.468 | 71.514 | 47.463 | 43.5% | false | NT | 0 | 0 |
| 150m | 293.272 | 84.200 | 65.800 | 51.1% | false | NT | 0 | 0 |

### Capacity v3 basis and provincial floor

| Measure | Value |
|---|---|
| Published records | 433 |
| Proxy records | 241 |
| Not-published records | 15 |
| Published capacity Mm3/yr | 166.609 |
| Proxy capacity Mm3/yr | 104.733 |
| Total capacity Mm3/yr | 271.342 |
| Eligible assignment capacity Mm3/yr | 243.230 |
| Unlocated capacity excluded Mm3/yr | 27.302 |
| Non-operating records excluded | 2 |

## Scenario comparison

| Scenario | Harvest Mm3 | Assigned Mm3 | Utilization | Total gross PJ | Total recoverable PJ | Delta assigned vs 119m | Delta gross PJ vs 119m |
|---|---|---|---|---|---|---|---|
| 100m | 100.000 | 100.000 | 37.7% | 583.12 | 542.46 | -18,977,339 | -110.66 |
| 119m | 118.977 | 118.977 | 43.5% | 693.78 | 645.40 | +0 | +0.00 |
| 150m | 150.000 | 150.000 | 51.1% | 874.68 | 813.69 | +31,022,661 | +180.90 |

## 150 Mm3 intensity note

The 150m scenario uses the documented provincial ceiling table. It is not an operable-proxy intensity screen.

The 1.0 and 1.2 m3/ha/yr operable-proxy screens are infeasible at 150 Mm3. They are separate sensitivity results and must not be used to relabel or reject the documented 150m ceiling case.

| Intensity m3/ha/yr | Status | Deficit m3 | Capacity Mm3 |
|---|---|---|---|
| 1.0 | infeasible | 16,296,352 | 133.704 |
| 1.2 | infeasible | 4,491,873 | 145.508 |

## Validation

| Check | Status | Detail |
|---|---|---|
| scenario_coverage | PASS | assignment scenarios=['100m', '119m', '150m'] |
| assignment_conservation | PASS | assigned + unassigned equals harvest in every scenario |
| capacity_bounds | PASS | every assignment row has finite capacity and assigned <= capacity |
| product_residue_conservation | PASS | class feedstock and process residue conserve in every scenario |
| scenario_ordering | PASS | 100m < 119m < 150m for assigned volume, residue, products, and utilization |
| proxy_share | PASS | proxy share equals proxy volume / assigned volume and is in [0,1] |
| no_overflow_unless_true | PASS | no assignment above capacity or offer; unassigned only with binding capacity |
| labels | PASS | all assignment and product/residue rows carry screening labels |
| intensity_150m_separate | PASS | 150m documented ceiling retained; 1.0/1.2 intensity screens infeasible and separate |

## Caveats

- All values are model estimates; `observed=false` and `policy_grade=false`.
- The 100/119/150 Mm3 cases are planning allocations, not legal AACs, sustainable-supply determinations, or observed harvest outcomes.
- The 1.2x provincial floor is recomputed from each case's harvest. Proxy capacities only are scaled; published capacity is never altered, and scaled proxies are not observed capacity.
- Capacity v3 mixes published mill records and class-median proxy capacity. The bases are not interchangeable.
- The allocation is local first; cross-border volume is only the residual that local finite capacity cannot serve.
- Product and residue quantities apply product-chain-v1 province/class coefficients to assigned class feedstock. They are not measured mill output.
- Process residue is facility-assigned and separate from provincial harvest residue; harvest residue is never assigned to a facility.
- The 150m documented ceiling is not the 1.0 or 1.2 m3/ha/yr operable-proxy intensity screen. Both intensity screens are infeasible at 150 Mm3 and are reported separately.
- No UI or public OSeCAN surface is changed by this artifact.

Labels: `model_estimate`, `observed=false`, `policy_grade=false`.
