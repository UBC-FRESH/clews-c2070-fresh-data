# National Facility Chain Scenarios V4 (Measured Coefficients)

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
| 100m | 35.688 | 8.025 | 3.906 | 3.493 | 621.8 | 432.43 | 106.93 | 76.09 | 539.36 | 508.52 |
| 119m | 42.520 | 9.527 | 4.654 | 4.172 | 742.7 | 514.61 | 127.86 | 90.99 | 642.47 | 605.60 |
| 150m | 53.646 | 12.006 | 5.872 | 5.354 | 953.0 | 649.26 | 165.85 | 118.03 | 815.11 | 767.29 |

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
| 100m | 100.000 | 100.000 | 37.7% | 539.36 | 508.52 | -18,977,339 | -103.12 |
| 119m | 118.977 | 118.977 | 43.5% | 642.47 | 605.60 | +0 | +0.00 |
| 150m | 150.000 | 150.000 | 51.1% | 815.11 | 767.29 | +31,022,661 | +172.64 |

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

## Measured versus donor coefficients

BC, QC, NB and YT use measured bucking-pilot solid/pulp/other and harvest-residue coefficients. The other nine jurisdictions keep the donor coefficients. Differences below are coefficient effects only; the assignment and harvest are identical.

### Coefficient replacement

| Province | Coefficient | Donor | Measured | Delta | Ratio |
|---|---|---:|---:|---:|---:|
| BC | solid_share | 0.689193 | 0.695281 | +0.006088 | 1.009 |
| BC | pulp_share | 0.308234 | 0.294764 | -0.013469 | 0.956 |
| BC | other_share | 0.080095 | 0.009955 | -0.070141 | 0.124 |
| BC | harvest_residue_odt_per_m3 | 0.076226 | 0.040577 | -0.035649 | 0.532 |
| QC | solid_share | 0.689193 | 0.341993 | -0.347200 | 0.496 |
| QC | pulp_share | 0.308234 | 0.641655 | +0.333422 | 2.082 |
| QC | other_share | 0.080095 | 0.016352 | -0.063744 | 0.204 |
| QC | harvest_residue_odt_per_m3 | 0.076226 | 0.059410 | -0.016816 | 0.779 |
| NB | solid_share | 0.689193 | 0.523792 | -0.165401 | 0.760 |
| NB | pulp_share | 0.308234 | 0.467185 | +0.158951 | 1.516 |
| NB | other_share | 0.080095 | 0.009023 | -0.071072 | 0.113 |
| NB | harvest_residue_odt_per_m3 | 0.076226 | 0.030341 | -0.045884 | 0.398 |
| YT | solid_share | 0.689193 | 0.424617 | -0.264576 | 0.616 |
| YT | pulp_share | 0.308234 | 0.562531 | +0.254298 | 1.825 |
| YT | other_share | 0.080095 | 0.012851 | -0.067244 | 0.160 |
| YT | harvest_residue_odt_per_m3 | 0.076226 | 0.123046 | +0.046821 | 1.614 |

### National 119m products and residue

| Metric | Donor | Measured | Delta | Delta % |
|---|---:|---:|---:|---:|
| solid_product_m3 (m3) | 53,771,528.207 | 47,174,038.475 | -6,597,489.732 | -12.27% |
| sawlog_product_m3 (m3) | 48,466,775.661 | 42,520,151.761 | -5,946,623.900 | -12.27% |
| panel_product_m3 (m3) | 5,304,752.546 | 4,653,886.714 | -650,865.832 | -12.27% |
| pulp_product_odt (odt) | 7,590,251.824 | 9,526,992.918 | 1,936,741.095 | +25.52% |
| pellet_product_odt (odt) | 4,747,898.211 | 4,172,333.553 | -575,564.658 | -12.12% |
| bio_product_mwh (MWh) | 845,182.063 | 742,724.744 | -102,457.320 | -12.12% |
| process_residue_pj (PJ) | 526.006 | 514.614 | -11.392 | -2.17% |
| harvest_residue_gross_pj (PJ) | 167.779 | 127.860 | -39.918 | -23.79% |
| harvest_residue_recoverable_pj (PJ) | 119.397 | 90.990 | -28.407 | -23.79% |
| total_residue_gross_pj (PJ) | 693.784 | 642.474 | -51.310 | -7.40% |
| total_residue_recoverable_pj (PJ) | 645.403 | 605.604 | -39.799 | -6.17% |

### Provincial 119m process and harvest residue

| Province | Donor process PJ | Measured process PJ | Delta | Donor harvest gross PJ | Measured harvest gross PJ | Delta |
|---|---:|---:|---:|---:|---:|---:|
| BC | 176.748 | 174.450 | -2.297 | 56.377 | 30.011 | -26.366 |
| AB | 101.204 | 101.204 | 0.000 | 32.281 | 32.281 | 0.000 |
| SK | 19.208 | 19.208 | 0.000 | 6.127 | 6.127 | 0.000 |
| MB | 5.019 | 5.019 | 0.000 | 1.601 | 1.601 | 0.000 |
| ON | 59.656 | 59.656 | 0.000 | 19.028 | 19.028 | 0.000 |
| QC | 117.929 | 110.033 | -7.896 | 37.615 | 29.317 | -8.298 |
| NB | 27.564 | 26.371 | -1.193 | 8.792 | 3.500 | -5.292 |
| NS | 10.559 | 10.559 | 0.000 | 3.368 | 3.368 | 0.000 |
| PE | 1.336 | 1.336 | 0.000 | 0.426 | 0.426 | 0.000 |
| NL | 6.428 | 6.428 | 0.000 | 2.050 | 2.050 | 0.000 |
| YT | 0.194 | 0.189 | -0.006 | 0.062 | 0.100 | 0.038 |
| NT | 0.161 | 0.161 | 0.000 | 0.051 | 0.051 | 0.000 |
| NU | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Process residue is facility-assigned; harvest residue is province-only. They are never combined into a single OSeCAN row.
