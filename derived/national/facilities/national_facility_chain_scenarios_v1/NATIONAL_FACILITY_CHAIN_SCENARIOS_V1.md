# National Facility Chain Scenarios V1

Multi-scenario 100/119/150 Mm3 facility assignment and product/residue chain on inventory v1 / capacity v2. All values are model estimates: `observed=false`, `policy_grade=false`. No legal/AAC claim is made.

## Scenarios

| Scenario | Harvest Mm3 | Source | Capacity case |
|---|---|---|---|
| 100m | 100.000 | provincial_allocation/100m.csv | published_plus_proxy |
| 119m | 118.977 | provincial_allocation/119m.csv | published_plus_proxy |
| 150m | 150.000 | provincial_allocation/150m.csv | published_plus_proxy |

## Assignment by scenario

| Scenario | Assigned Mm3 | Unassigned m3 | Cross-border Mm3 | Proxy share | Facilities | Max facility share | HHI | Capacity utilization |
|---|---|---|---|---|---|---|---|---|
| 100m | 100.000 | 0 | 16.637 | 57.9% | 249 | 2.16% | 0.00859 | 52.0% |
| 119m | 118.977 | 0 | 23.689 | 58.5% | 289 | 1.82% | 0.00737 | 61.8% |
| 150m | 150.000 | 0 | 40.136 | 59.3% | 330 | 2.33% | 0.00700 | 78.0% |

## Products/residue by scenario

| Scenario | Sawlog product Mm3 | Pulp product Million odt | Panel product Mm3 | Pellet product Million odt | Bio product GWh | Process residue PJ | Harvest gross PJ | Harvest recoverable PJ | Total gross PJ | Total recoverable PJ |
|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 40.736 | 6.380 | 4.459 | 3.991 | 710.4 | 442.11 | 141.02 | 100.35 | 583.12 | 542.46 |
| 119m | 48.467 | 7.590 | 5.305 | 4.748 | 845.2 | 526.01 | 167.78 | 119.40 | 693.78 | 645.40 |
| 150m | 61.104 | 9.569 | 6.688 | 5.986 | 1,065.6 | 663.16 | 211.53 | 150.53 | 874.68 | 813.69 |

## Capacity/proxy/overflow

| Scenario | Eligible capacity Mm3/yr | Published assigned Mm3 | Proxy assigned Mm3 | Capacity utilization | Global capacity binding | Local binding provinces | Unassigned m3 | Overflow m3 |
|---|---|---|---|---|---|---|---|---|
| 100m | 192.414 | 42.095 | 57.905 | 52.0% | false | AB;SK;MB;ON;NT | 0 | 0 |
| 119m | 192.414 | 49.428 | 69.549 | 61.8% | false | AB;SK;MB;ON;NT | 0 | 0 |
| 150m | 192.414 | 61.013 | 88.987 | 78.0% | false | AB;SK;MB;ON;NT | 0 | 0 |

### Capacity v2 basis

| Measure | Value |
|---|---|
| Published records | 212 |
| Proxy records | 292 |
| Not-published records | 15 |
| Published capacity Mm3/yr | 100.285 |
| Proxy capacity Mm3/yr | 120.241 |
| Total capacity Mm3/yr | 220.526 |
| Eligible assignment capacity Mm3/yr | 192.414 |
| Unlocated capacity excluded Mm3/yr | 27.302 |
| Non-operating records excluded | 2 |

## Scenario comparison

| Scenario | Harvest Mm3 | Assigned Mm3 | Utilization | Total gross PJ | Total recoverable PJ | Delta assigned vs 119m | Delta gross PJ vs 119m |
|---|---|---|---|---|---|---|---|
| 100m | 100.000 | 100.000 | 52.0% | 583.12 | 542.46 | -18,977,339 | -110.66 |
| 119m | 118.977 | 118.977 | 61.8% | 693.78 | 645.40 | +0 | +0.00 |
| 150m | 150.000 | 150.000 | 78.0% | 874.68 | 813.69 | +31,022,661 | +180.90 |

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
- Product and residue quantities apply product-chain-v1 province/class coefficients to assigned class feedstock. They are not measured mill output.
- Process residue is facility-assigned and separate from provincial harvest residue; harvest residue is never assigned to a facility.
- The 150m documented ceiling is not the 1.0 or 1.2 m3/ha/yr operable-proxy intensity screen. Both intensity screens are infeasible at 150 Mm3 and are reported separately.
- No UI or public OSeCAN surface is changed by this artifact.

Labels: `model_estimate`, `observed=false`, `policy_grade=false`.
