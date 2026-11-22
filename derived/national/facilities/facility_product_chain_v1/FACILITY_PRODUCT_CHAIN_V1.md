# National Facility Product/Residue Chain v1

This artifact joins the national product/residue chain to the `published_plus_proxy` facility assignment. It allocates only class-matched feedstock, calculates products and process residue at the facility, and retains harvest residue as a separate provincial stream.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, or investment statement.

## Method and class joining

For each origin province and facility class, the product-chain class feedstock is allocated to assigned v2 facilities of the same class in proportion to their assigned volume. A local class pool is used first. If a province has no assigned facility of that class, the class stream is routed to the national set of assigned facilities of that class; the row records `allocation_scope=national_class_fallback`. No class feedstock is ever assigned to a different facility class.

- Scenario: `published_plus_proxy`.
- Allocation rows: 900; facilities used: 262.
- Province/class pools using local assignment: 29; national class fallback: 31.
- Fallback feedstock: 8,806,809 m3 (6.61% of facility feedstock).

Conversion is the effective product-chain class ratio (`class product / class feedstock`) for the origin province. This preserves the product-chain province/class totals exactly while making the facility allocation auditable.

## National facility products and process residue

| Class | Feedstock m3 | Product | Unit | Process residue odt |
|---|---:|---:|---|---:|
| SAW | 70,463,901 | 48,466,776 | m3 | 18,289,096 |
| PULP | 36,672,817 | 7,590,252 | odt | 7,600,128 |
| PANEL | 11,534,443 | 5,304,753 | m3 | 1,840,820 |
| PELLET | 12,112,416 | 4,747,898 | odt | 702,688.9 |
| BIO | 2,535,765 | 845,182.1 | MWh | 0.000000 |

Process residue is 28,432,733 odt (63,183,852 m3 at 0.45 odt/m3). Harvest residue is reported separately: 9,069,109 odt gross, 6,453,901 odt recoverable.

## Provincial products and residue

| Province | Harvest m3 | Facility feed m3 | SAW feed m3 | PULP feed m3 | PANEL feed m3 | PELLET feed m3 | BIO feed m3 | Process residue odt | Harvest residue recoverable odt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | 39,978,577 | 44,797,754 | 23,677,168 | 12,322,742 | 3,875,785 | 4,069,995 | 852,063.6 | 9,553,922 | 2,168,630 |
| AB | 22,891,404 | 25,650,825 | 13,557,352 | 7,055,901 | 2,219,243 | 2,330,446 | 487,884.6 | 5,470,497 | 1,241,739 |
| SK | 4,344,698 | 4,868,425 | 2,573,132 | 1,339,182 | 421,203.4 | 442,309.3 | 92,598.6 | 1,038,279 | 235,677.2 |
| MB | 1,135,236 | 1,272,082 | 672,339.3 | 349,917.9 | 110,057.2 | 115,572.0 | 24,195.3 | 271,294.2 | 61,580.6 |
| ON | 13,493,596 | 15,120,168 | 7,991,534 | 4,159,180 | 1,308,158 | 1,373,707 | 287,589.1 | 3,224,646 | 731,957.3 |
| QC | 26,674,334 | 29,889,764 | 15,797,778 | 8,221,927 | 2,585,985 | 2,715,564 | 568,510.2 | 6,374,527 | 1,446,944 |
| NB | 6,234,700 | 6,986,256 | 3,692,479 | 1,921,744 | 604,432.7 | 634,719.9 | 132,880.2 | 1,489,944 | 338,200.0 |
| NS | 2,388,245 | 2,676,134 | 1,414,430 | 736,137.4 | 231,532.1 | 243,133.8 | 50,900.7 | 570,733.3 | 129,549.9 |
| PE | 302,210.4 | 338,640.0 | 178,983.0 | 93,151.4 | 29,298.3 | 30,766.3 | 6,441.0 | 72,221.0 | 16,393.3 |
| NL | 1,454,038 | 1,629,313 | 861,148.5 | 448,183.3 | 140,963.9 | 148,027.4 | 30,989.9 | 347,480.1 | 78,874.0 |
| YT | 43,925.8 | 49,220.8 | 26,014.9 | 13,539.4 | 4,258.5 | 4,471.8 | 936.191 | 10,497.2 | 2,382.7 |
| NT | 36,376.0 | 40,760.9 | 21,543.6 | 11,212.3 | 3,526.5 | 3,703.2 | 775.282 | 8,693.0 | 1,973.2 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

Province/class detail is written to `province_class_product_chain.csv`. Every class row carries the reference and facility quantities plus the gap.

## Conservation and RSYC

| Check | Status | Detail |
|---|---|---|
| class_matching | PASS | 0 class-mismatched allocation rows |
| province_class_feedstock_conservation | PASS | 0 province/class feedstock gaps exceed tolerance |
| national_product_residue_conservation | PASS | all five class products and process residues match product-chain totals |
| product_chain_summary_crosscheck | PASS | facility totals reproduce product-chain summary national totals |
| finite_nonnegative | PASS | 0 non-finite or negative values |
| allocation_normalization | PASS | failed pools: [] |
| fallback_scope | PASS | failed: [] |
| harvest_residue_separate | PASS | failed: [] |
| rsyc_reproduction | PASS | failed: [] |
| used_facility_capacity | PASS | failed: [] |
| assignment_scenario | PASS | failed: [] |
| repository_hygiene | PASS | no unexpected D in parent or data git status |

RSYC base recoverable residue is 7,080,062 odt; the model recoverable harvest residue is 5,441,465 odt, a ratio of 0.7686 (`model_below_rsyc`). This is the same screening comparison as product-chain v1. Facility process residue is not included in that ratio; it is a separate stream.

## Concentration and proxy capacity

- Facilities with feedstock: 262.
- HHI: 0.009905; effective facility count: 101.0.
- Top 1 share: 4.14%; top 5 share: 13.50%.
- Proxy-capacity facilities: 197 of 262; proxy feedstock share: 55.06%.
- Proxy share of used facility capacity: 62.00%.
- Assignment v2 proxy share of assigned volume: 61.23%.
- Cross-border origin feedstock: 25.56%.

Proxy capacity is a BC class-median screening fill, not an observed facility capacity. Facilities are OSM/published records whose operating status is not established by this artifact.

### Top facilities by feedstock

| Rank | Facility | Class | Province | Feedstock m3 | Share | Cumulative | Capacity status |
|---:|---|---|---|---:|---:|---:|---|
| 1 | Domtar-Kamloops | PULP | BC | 5,522,077 | 4.14% | 4.14% | published |
| 2 | Paper Excellence-Mackenzie | PULP | BC | 4,634,597 | 3.48% | 7.62% | published |
| 3 | GDS Énergie | PELLET | QC | 3,021,321 | 2.27% | 9.88% | proxy |
| 4 | Pinnacle Renewable Energy Inc-Pinnacle Pellet - Armstrong | PELLET | BC | 2,442,047 | 1.83% | 11.72% | published |
| 5 | Canfor Pulp-Taylor | PULP | BC | 2,372,904 | 1.78% | 13.50% | published |
| 6 | Thunder Bay Pulp and Paper | PULP | ON | 2,130,889 | 1.60% | 15.09% | proxy |
| 7 | Global Paper | PULP | QC | 2,130,889 | 1.60% | 16.69% | proxy |
| 8 | Louisiana-Pacific Canada Ltd.-Peace Valley | PANEL | BC | 2,057,119 | 1.54% | 18.24% | published |
| 9 | Nordic Paper Québec | PULP | QC | 1,936,401 | 1.45% | 19.69% | proxy |
| 10 | Cascades | PULP | QC | 1,936,401 | 1.45% | 21.14% | proxy |
| 11 | Cascades Multi-Pro | PULP | QC | 1,936,401 | 1.45% | 22.59% | proxy |
| 12 | Technocell | PULP | QC | 1,936,401 | 1.45% | 24.05% | proxy |
| 13 | Canfor Corporation-Plateau Forest Products Division | SAW | BC | 1,848,664 | 1.39% | 25.43% | published |
| 14 | Dunkley Lumber-Dunkley Lum | SAW | BC | 1,837,683 | 1.38% | 26.81% | published |
| 15 | Pinnacle Renewable Energy Inc-Pinnacle Pellet - Burns Lake | PELLET | BC | 1,726,309 | 1.29% | 28.11% | published |
| 16 | Tolko Industries Ltd.-Lavington Planer Mill | SAW | BC | 1,601,128 | 1.20% | 29.31% | published |
| 17 | Canfor Corporation-Radium Division | SAW | BC | 1,591,301 | 1.19% | 30.50% | published |
| 18 | Canfor Corporation-Houston Division | SAW | BC | 1,583,717 | 1.19% | 31.69% | published |
| 19 | Irving Paper | PULP | NB | 1,506,184 | 1.13% | 32.82% | proxy |
| 20 | Uniboard Canada Inc | PANEL | QC | 1,450,793 | 1.09% | 33.91% | proxy |

## Labels and caveats

- `model_estimate=true`, `observed=false`, `policy_grade=false`, `facility_assignment=true`.
- Proxy facility capacity is a BC class-median fill; the proxy feedstock share is reported above and is not an observed capacity.
- Class matching forces province class streams to existing assigned facilities of the same class. Provinces without a local assigned facility of a class use the documented national class fallback; this is a screening allocation, not a transport or market model.
- Conversion ratios are product-chain effective class ratios derived from the BC-anchored FFCM/Stage A/B evidence; they are engineering proxies, not current measured facility yields.
- Harvest residue is a provincial estimate from the product chain and is kept separate from facility process residue. It is not assigned to a facility.
- No transport cost, revenue, capacity expansion, legal tenure, AAC, or policy claim is made. No UI or public OSeCAN surface is changed.

## Tests and status

Build status: `pass`. Validation checks: 12, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.facility_product_chain` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_facility_product_chain.py -q` to run the regression tests.

No policy/AAC claim is made.
