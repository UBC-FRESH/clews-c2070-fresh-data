# National Facility Chain Scenarios V7 (E1+E2c Coefficients)

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
| 100m | 28.566 | 10.137 | 3.127 | 4.372 | 778.3 | 419.24 | 373.24 | 223.95 | 792.48 | 643.18 |
| 119m | 33.957 | 12.066 | 3.717 | 5.230 | 930.9 | 498.75 | 444.41 | 266.65 | 943.16 | 765.40 |
| 150m | 41.585 | 15.551 | 4.552 | 7.039 | 1,253.0 | 626.87 | 573.13 | 343.88 | 1,199.99 | 970.74 |

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
| 100m | 100.000 | 100.000 | 37.7% | 792.48 | 643.18 | -18,977,339 | -150.68 |
| 119m | 118.977 | 118.977 | 43.5% | 943.16 | 765.40 | +0 | +0.00 |
| 150m | 150.000 | 150.000 | 51.1% | 1,199.99 | 970.74 | +31,022,661 | +256.83 |

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
- Product and residue quantities apply measured four-province product-chain-v2 coefficients to assigned class feedstock. They are not measured mill output.
- Process residue is facility-assigned and separate from provincial harvest residue; harvest residue is never assigned to a facility.
- The 150m documented ceiling is not the 1.0 or 1.2 m3/ha/yr operable-proxy intensity screen. Both intensity screens are infeasible at 150 Mm3 and are reported separately.
- No UI or public OSeCAN surface is changed by this artifact.

Labels: `model_estimate`, `observed=false`, `policy_grade=false`.

## Frozen v3.2 versus E2c v4 coefficients

BC, QC, NB and YT use measured bucking-pilot solid/pulp/other and harvest-residue coefficients. The other nine jurisdictions keep the donor coefficients. Differences below are coefficient effects only; the assignment and harvest are identical.

### Coefficient replacement

| Province | Coefficient | Donor | Measured | Delta | Ratio |
|---|---|---:|---:|---:|---:|
| BC | solid_share | 0.919580 | 0.695281 | -0.224299 | 0.756 |
| BC | pulp_share | 0.000324 | 0.294764 | +0.294440 | 908.623 |
| BC | other_share | 0.080095 | 0.009955 | -0.070141 | 0.124 |
| BC | total_residue_odt_per_m3 | 0.076226 | 0.161622 | +0.085396 | 2.120 |
| QC | solid_share | 0.919580 | 0.341993 | -0.577587 | 0.372 |
| QC | pulp_share | 0.000324 | 0.641655 | +0.641331 | 1977.928 |
| QC | other_share | 0.080095 | 0.016352 | -0.063744 | 0.204 |
| QC | total_residue_odt_per_m3 | 0.076226 | 0.217507 | +0.141282 | 2.853 |
| NB | solid_share | 0.919580 | 0.523792 | -0.395788 | 0.570 |
| NB | pulp_share | 0.000324 | 0.467185 | +0.466860 | 1440.116 |
| NB | other_share | 0.080095 | 0.009023 | -0.071072 | 0.113 |
| NB | total_residue_odt_per_m3 | 0.076226 | 0.187426 | +0.111201 | 2.459 |
| YT | solid_share | 0.919580 | 0.424617 | -0.494963 | 0.462 |
| YT | pulp_share | 0.000324 | 0.562531 | +0.562207 | 1734.025 |
| YT | other_share | 0.080095 | 0.012851 | -0.067244 | 0.160 |
| YT | total_residue_odt_per_m3 | 0.076226 | 0.269689 | +0.193463 | 3.538 |

### National 119m products and residue

| Metric | Donor | Measured | Delta | Delta % |
|---|---:|---:|---:|---:|
| solid_product_m3 (m3) | 42,291,403.688 | 37,673,626.761 | -4,617,776.927 | -10.92% |
| sawlog_product_m3 (m3) | 38,119,206.266 | 33,956,989.460 | -4,162,216.806 | -10.92% |
| panel_product_m3 (m3) | 4,172,197.422 | 3,716,637.301 | -455,560.121 | -10.92% |
| pulp_product_odt (odt) | 10,824,299.935 | 12,066,311.270 | 1,242,011.334 | +11.47% |
| pellet_product_odt (odt) | 4,356,049.838 | 5,229,686.167 | 873,636.328 | +20.06% |
| bio_product_mwh (MWh) | 775,428.416 | 930,946.020 | 155,517.604 | +20.06% |
| process_residue_pj (PJ) | 505.333 | 498.751 | -6.582 | -1.30% |
| harvest_residue_gross_pj (PJ) | 390.418 | 444.411 | 53.993 | +13.83% |
| harvest_residue_recoverable_pj (PJ) | 234.251 | 266.646 | 32.396 | +13.83% |
| total_residue_gross_pj (PJ) | 895.751 | 943.162 | 47.411 | +5.29% |
| total_residue_recoverable_pj (PJ) | 739.584 | 765.397 | 25.814 | +3.49% |

### Provincial 119m process and harvest residue

| Province | Donor process PJ | Measured process PJ | Delta | Donor harvest gross PJ | Measured harvest gross PJ | Delta |
|---|---:|---:|---:|---:|---:|---:|
| BC | 174.450 | 174.450 | 0.000 | 119.536 | 119.536 | 0.000 |
| AB | 97.382 | 94.397 | -2.985 | 56.120 | 67.659 | 11.539 |
| SK | 18.188 | 14.660 | -3.528 | 13.568 | 51.031 | 37.463 |
| MB | 4.841 | 4.726 | -0.115 | 4.580 | 4.074 | -0.506 |
| ON | 56.376 | 56.406 | 0.029 | 51.837 | 52.469 | 0.631 |
| QC | 110.033 | 110.033 | 0.000 | 107.334 | 107.334 | 0.000 |
| NB | 26.371 | 26.371 | 0.000 | 21.618 | 21.618 | 0.000 |
| NS | 9.873 | 9.896 | 0.023 | 8.549 | 13.098 | 4.550 |
| PE | 1.234 | 1.227 | -0.007 | 1.029 | 1.330 | 0.301 |
| NL | 6.238 | 6.238 | 0.001 | 5.910 | 5.923 | 0.013 |
| YT | 0.189 | 0.189 | 0.000 | 0.219 | 0.219 | 0.000 |
| NT | 0.158 | 0.158 | 0.000 | 0.117 | 0.119 | 0.002 |
| NU | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Process residue is facility-assigned; harvest residue is province-only. They are never combined into a single OSeCAN row.

## E1/E2c coefficient source

BC/QC/NB/YT use E1 measured coefficients; the other nine use E2c density-calibrated open-data coefficients. No donor provincial product share is used. The frozen v3.2 baseline uses E2 v1 coefficients, not E2 v2; see `v3_2_vs_v4_comparison.csv` for the change and `national_product_chain_v5/e2_v2_vs_e2c_coefficients.csv` for the E2 v2 to E2c per-m3 coefficient check.
