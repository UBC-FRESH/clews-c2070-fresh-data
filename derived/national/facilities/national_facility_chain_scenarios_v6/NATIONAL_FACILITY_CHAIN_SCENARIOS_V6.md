# National Facility Chain Scenarios V6 (E1+E2 Coefficients)

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
| 100m | 32.028 | 9.104 | 3.505 | 3.646 | 649.0 | 424.71 | 328.34 | 197.00 | 753.05 | 621.72 |
| 119m | 38.119 | 10.824 | 4.172 | 4.356 | 775.4 | 505.33 | 390.42 | 234.25 | 895.75 | 739.58 |
| 150m | 47.330 | 13.873 | 5.180 | 5.656 | 1,006.8 | 636.14 | 494.83 | 296.90 | 1,130.97 | 933.04 |

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
| 100m | 100.000 | 100.000 | 37.7% | 753.05 | 621.72 | -18,977,339 | -142.70 |
| 119m | 118.977 | 118.977 | 43.5% | 895.75 | 739.58 | +0 | +0.00 |
| 150m | 150.000 | 150.000 | 51.1% | 1,130.97 | 933.04 | +31,022,661 | +235.22 |

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

## Prior donor-product chain versus E2 coefficients

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
| solid_product_m3 (m3) | 47,174,038.475 | 42,291,403.688 | -4,882,634.787 | -10.35% |
| sawlog_product_m3 (m3) | 42,520,151.761 | 38,119,206.266 | -4,400,945.496 | -10.35% |
| panel_product_m3 (m3) | 4,653,886.714 | 4,172,197.422 | -481,689.291 | -10.35% |
| pulp_product_odt (odt) | 9,526,992.918 | 10,824,299.935 | 1,297,307.017 | +13.62% |
| pellet_product_odt (odt) | 4,172,333.553 | 4,356,049.838 | 183,716.285 | +4.40% |
| bio_product_mwh (MWh) | 742,724.744 | 775,428.416 | 32,703.673 | +4.40% |
| process_residue_pj (PJ) | 514.614 | 505.333 | -9.281 | -1.80% |
| harvest_residue_gross_pj (PJ) | 313.640 | 390.418 | 76.777 | +24.48% |
| harvest_residue_recoverable_pj (PJ) | 195.433 | 234.251 | 38.818 | +19.86% |
| total_residue_gross_pj (PJ) | 828.254 | 895.751 | 67.496 | +8.15% |
| total_residue_recoverable_pj (PJ) | 710.047 | 739.584 | 29.537 | +4.16% |

### Provincial 119m process and harvest residue

| Province | Donor process PJ | Measured process PJ | Delta | Donor harvest gross PJ | Measured harvest gross PJ | Delta |
|---|---:|---:|---:|---:|---:|---:|
| BC | 174.450 | 174.450 | 0.000 | 119.536 | 119.536 | 0.000 |
| AB | 101.204 | 97.382 | -3.822 | 32.281 | 56.120 | 23.839 |
| SK | 19.208 | 18.188 | -1.020 | 6.127 | 13.568 | 7.441 |
| MB | 5.019 | 4.841 | -0.178 | 1.601 | 4.580 | 2.979 |
| ON | 59.656 | 56.376 | -3.280 | 19.028 | 51.837 | 32.809 |
| QC | 110.033 | 110.033 | 0.000 | 107.334 | 107.334 | 0.000 |
| NB | 26.371 | 26.371 | 0.000 | 21.618 | 21.618 | 0.000 |
| NS | 10.559 | 9.873 | -0.686 | 3.368 | 8.549 | 5.181 |
| PE | 1.336 | 1.234 | -0.102 | 0.426 | 1.029 | 0.603 |
| NL | 6.428 | 6.238 | -0.191 | 2.050 | 5.910 | 3.859 |
| YT | 0.189 | 0.189 | 0.000 | 0.219 | 0.219 | 0.000 |
| NT | 0.161 | 0.158 | -0.003 | 0.051 | 0.117 | 0.066 |
| NU | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Process residue is facility-assigned; harvest residue is province-only. They are never combined into a single OSeCAN row.

## E1/E2 coefficient source

BC/QC/NB/YT use E1 measured coefficients; the other nine use E2 open-data imputation coefficients. No donor provincial product share is used. See `donor_vs_e2_comparison.csv` for the prior chain-v5 versus E2-chain-v6 change and `national_product_chain_v4/donor_vs_e2_coefficients.csv` for the coefficient table.
