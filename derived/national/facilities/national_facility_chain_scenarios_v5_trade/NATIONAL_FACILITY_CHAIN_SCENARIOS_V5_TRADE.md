# National Facility Chain Scenarios V5 Trade (Measured Total Residue)

Multi-scenario 100/119/150 Mm3 facility assignment and product/residue chain on inventory v1 / capacity v3. All values are model estimates: `observed=false`, `policy_grade=false`. No legal/AAC claim is made.

## Scenarios

| Scenario | Harvest Mm3 | Source | Capacity case |
|---|---|---|---|
| 100m | 100.000 | provincial_allocation/100m.csv | published_plus_proxy |
| 119m | 118.977 | provincial_allocation/119m.csv | published_plus_proxy |
| 150m | 150.000 | provincial_allocation/150m.csv | published_plus_proxy |

## Assignment by scenario

| Scenario | Assigned Mm3 | Unassigned m3 | Cross-border Mm3 | Proxy share | Facilities | Max facility share | HHI | Capacity utilization |
|---|---|---|---|---|---|---|---|---|
| 100m | 100.000 | 0 | 14.850 | 34.4% | 219 | 2.16% | 0.00915 | 41.1% |
| 119m | 118.977 | 0 | 21.902 | 33.9% | 263 | 1.82% | 0.00755 | 48.9% |
| 150m | 150.000 | 0 | 38.349 | 30.8% | 328 | 2.33% | 0.00664 | 61.7% |

## Products/residue by scenario

| Scenario | Sawlog product Mm3 | Pulp product Million odt | Panel product Mm3 | Pellet product Million odt | Bio product GWh | Process residue PJ | Harvest gross PJ | Harvest recoverable PJ | Total gross PJ | Total recoverable PJ |
|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 35.688 | 8.025 | 3.906 | 3.493 | 621.8 | 432.43 | 264.48 | 164.72 | 696.92 | 597.15 |
| 119m | 42.520 | 9.527 | 4.654 | 4.172 | 742.7 | 514.61 | 313.64 | 195.43 | 828.25 | 710.05 |
| 150m | 53.646 | 12.006 | 5.872 | 5.354 | 953.0 | 649.26 | 385.20 | 241.25 | 1,034.46 | 890.51 |

## Capacity/proxy/overflow

| Scenario | Eligible capacity Mm3/yr | Published assigned Mm3 | Proxy assigned Mm3 | Capacity utilization | Global capacity binding | Local binding provinces | Unassigned m3 | Overflow m3 |
|---|---|---|---|---|---|---|---|---|
| 100m | 243.230 | 65.562 | 34.438 | 41.1% | false | AB;SK;MB;ON;NT | 0 | 0 |
| 119m | 243.230 | 78.658 | 40.319 | 48.9% | false | AB;SK;MB;ON;NT | 0 | 0 |
| 150m | 243.230 | 103.799 | 46.201 | 61.7% | false | AB;SK;MB;ON;NT | 0 | 0 |

### Capacity v2 basis

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
| 100m | 100.000 | 100.000 | 41.1% | 696.92 | 597.15 | -18,977,339 | -131.34 |
| 119m | 118.977 | 118.977 | 48.9% | 828.25 | 710.05 | +0 | +0.00 |
| 150m | 150.000 | 150.000 | 61.7% | 1,034.46 | 890.51 | +31,022,661 | +206.21 |

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
- The 100/119/150 Mm3 cases are planning allocations, not legal AACs, sustainable-supply determinations, or observed harvest outcomes. No legal/AAC claim is made.
- Capacity v2 mixes 2015 Mills DB/FFCM infeed proxies, converted 2025 pellet-map finished-product volume, and BC class-median proxy capacity. Proxy capacity is not observed capacity, and the bases are not interchangeable.
- Converted pellet capacity is finished-product volume, not infeed-equivalent; no pellet yield, moisture, bark, grade, or recovery conversion is modelled.
- The allocation is local-first with a 500 km cross-border penalty. Cross-border volume is a screening result, not an interprovincial trade forecast.
- Product and residue quantities apply measured four-province product-chain-v3 coefficients to assigned class feedstock. They are not measured mill output.
- Process residue is facility-assigned and separate from provincial harvest residue; harvest residue is never assigned to a facility.
- The 150m documented ceiling is not the 1.0 or 1.2 m3/ha/yr operable-proxy intensity screen. Both intensity screens are infeasible at 150 Mm3 and are reported separately.
- No UI or public OSeCAN surface is changed by this artifact.

Labels: `model_estimate`, `observed=false`, `policy_grade=false`.

## Trade sensitivity

This chain uses the assignment-v5 `published_plus_proxy` case (unscaled capacity, trade-permissive cross-border allocation). It is the trade counterpart of the assignment-v6 `province_capacity_floor` chain v5; national products, process residue, harvest residue and residue scenarios are shared, while the provincial facility distribution differs. It is a screening counterfactual, not an interprovincial trade forecast.
