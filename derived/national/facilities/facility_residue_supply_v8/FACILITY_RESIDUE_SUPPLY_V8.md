# National Facility Residue Supply v8 (Node Transport-Aware v10)

This artifact recomputes facility-level class feedstock, products, and process residue on the assignment v10 `node_transport_aware` case, and reports provincial harvest residue alongside it. Process residue is facility-assigned; harvest residue is not.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Facility residue

| Province | Facility | Class | Residue odt | Residue PJ | Residue type | Capacity status | Evidence tier |
|---|---|---|---:|---:|---|---|---|
| AB | Alberta Newsprint Company | PULP | 2,773,312 | 51.306 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| ON | Thunder Bay Pulp and Paper | PULP | 1,419,430 | 26.259 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| QC | Compagnie WestRock du Canada Corp. | PULP | 669,682.5 | 12.389 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Neucel Specialty Cellulose | PULP | 655,919.4 | 12.135 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| QC | Nordic Paper Québec | PULP | 625,691.6 | 11.575 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| NL | Corner Brook Pulp And Paper | PULP | 571,353.7 | 10.570 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| QC | Cascades Multi-Pro | PULP | 519,685.1 | 9.614 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| BC | Paper Excellence-Mackenzie | PULP | 493,307.2 | 9.126 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Houston Division | SAW | 401,066.5 | 7.420 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| QC | Entreprises Sappi Canada inc. (Matane) | PULP | 395,925.6 | 7.325 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| NB | Irving Paper | PULP | 392,207.7 | 7.256 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| BC | Dunkley Lumber-Dunkley Lum | SAW | 388,063.4 | 7.179 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| NS | OSM-NS-R11703982 | PULP | 378,277.9 | 6.998 | process_residue | proxy | E2c_open_inventory_density_calibrated+class_median_proxy |
| BC | Howe Sound Pulp & Paper | PULP | 305,803.5 | 5.657 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| BC | West Fraser Timber Co. Ltd.-Fraser Lake Mills | SAW | 280,279.7 | 5.185 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Mackenzie Division | SAW | 277,533.2 | 5.134 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Catalyst-Powell River | PULP | 274,973.7 | 5.087 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | West Fraser Timber Co. Ltd.-Pacific Inland Resources | SAW | 273,235.5 | 5.055 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | OSM-BC-W620787274 | PULP | 273,055.0 | 5.052 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| BC | Canfor Corporation-Fort St. John Division | SAW | 263,998.5 | 4.884 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |

Facility process residue is 26,959,509 odt / 498.751 PJ at 18.5 GJ/odt. 294 facilities receive class-matched feedstock; 271 have positive process residue.

## Province/national totals

| Province | Process odt | Process PJ | Harvest gross odt | Harvest recoverable odt | Harvest recoverable PJ | RSYC ratio |
|---|---:|---:|---:|---:|---:|---:|
| BC | 9,838,408 | 182.011 | 6,461,417 | 3,876,850 | 71.722 | 1.6174 |
| AB | 5,398,777 | 99.877 | 3,657,251 | 2,194,351 | 40.595 | 1.6226 |
| SK | 51,627.8 | 0.955114 | 2,758,446 | 1,655,067 | 30.619 | 3.6271 |
| MB | 164,244.9 | 3.039 | 220,191.1 | 132,114.7 | 2.444 | 1.0191 |
| ON | 2,919,952 | 54.019 | 2,836,137 | 1,701,682 | 31.481 | 2.2758 |
| QC | 5,319,178 | 98.405 | 5,801,855 | 3,481,113 | 64.401 | 2.6241 |
| NB | 1,651,898 | 30.560 | 1,168,546 | 701,127.6 | 12.971 | 2.9305 |
| NS | 598,227.1 | 11.067 | 708,021.3 | 424,812.8 | 7.859 | 4.3406 |
| PE | 36,351.5 | 0.672503 | 71,917.4 | 43,150.5 | 0.798283 | 1.7351 |
| NL | 927,373.2 | 17.156 | 320,137.3 | 192,082.4 | 3.554 | 0.6421 |
| YT | 53,470.9 | 0.989211 | 11,846.3 | 7,107.8 | 0.131494 | 1.8980 |
| NT | 0.000000 | 0.000000 | 6,439.3 | 3,863.6 | 0.071477 | 0.7001 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.0000 |

National process residue: 26,959,509 odt / 498.751 PJ. National harvest residue: gross 24,022,204 odt / 444.411 PJ; recoverable 14,413,322 odt / 266.646 PJ.

## RSYC comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ at 18.5 GJ/odt. The model recoverable harvest residue is 14,413,322 odt / 266.646 PJ, ratio 2.0358 (`model_above_rsyc`).

The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ. The familiar 129.6709 PJ figure is that 100 Mm3 reference, not a 119 Mm3 value; the 119 Mm3 base is derived with the same province factors and the documented LHV.

Process residue is not added to the RSYC comparison. A combined process plus recoverable harvest stream is 41,372,831 odt / 765.397 PJ, labelled `combined` and not RSYC-comparable.

## Proxy/concentration

- Facilities used: 294.
- HHI of facility process residue: 0.023211; effective facility count: 43.1.
- Top 1 share: 10.93%; top 5 share: 24.67%.
- Published-capacity share of process residue: 43.40%.
- Proxy-capacity share of process residue: 56.60% (scaled proxy: 29.36%).
- National class fallback share of process residue: 4.67% (1,259,643 odt).
- Cross-border process residue (facility province differs from origin): 8.50% (2,291,443 odt). Assignment v10 cross-border volume differs from the class-fallback cross-border residue because the fallback routes origin class streams to facilities in other provinces.

### Top facilities by process residue

| Rank | Facility | Class | Province | Residue odt | Share | Capacity status |
|---:|---|---|---|---:|---:|---|
| 1 | Alberta Newsprint Company | PULP | AB | 2,773,312 | 10.29% | proxy_harvest_scaled |
| 2 | Thunder Bay Pulp and Paper | PULP | ON | 1,419,430 | 5.27% | proxy_harvest_scaled |
| 3 | Compagnie WestRock du Canada Corp. | PULP | QC | 669,682.5 | 2.48% | published |
| 4 | Neucel Specialty Cellulose | PULP | BC | 655,919.4 | 2.43% | proxy |
| 5 | Nordic Paper Québec | PULP | QC | 625,691.6 | 2.32% | published |
| 6 | Corner Brook Pulp And Paper | PULP | NL | 571,353.7 | 2.12% | proxy |
| 7 | Cascades Multi-Pro | PULP | QC | 519,685.1 | 1.93% | proxy |
| 8 | Paper Excellence-Mackenzie | PULP | BC | 493,307.2 | 1.83% | published |
| 9 | Canfor Corporation-Houston Division | SAW | BC | 401,066.5 | 1.49% | published |
| 10 | Entreprises Sappi Canada inc. (Matane) | PULP | QC | 395,925.6 | 1.47% | published |
| 11 | Irving Paper | PULP | NB | 392,207.7 | 1.45% | proxy |
| 12 | Dunkley Lumber-Dunkley Lum | SAW | BC | 388,063.4 | 1.44% | published |
| 13 | OSM-NS-R11703982 | PULP | NS | 378,277.9 | 1.40% | proxy |
| 14 | Howe Sound Pulp & Paper | PULP | BC | 305,803.5 | 1.13% | proxy |
| 15 | West Fraser Timber Co. Ltd.-Fraser Lake Mills | SAW | BC | 280,279.7 | 1.04% | published |
| 16 | Canfor Corporation-Mackenzie Division | SAW | BC | 277,533.2 | 1.03% | published |
| 17 | Catalyst-Powell River | PULP | BC | 274,973.7 | 1.02% | published |
| 18 | West Fraser Timber Co. Ltd.-Pacific Inland Resources | SAW | BC | 273,235.5 | 1.01% | published |
| 19 | OSM-BC-W620787274 | PULP | BC | 273,055.0 | 1.01% | proxy |
| 20 | Canfor Corporation-Fort St. John Division | SAW | BC | 263,998.5 | 0.98% | published |

## Labels and caveats

- `model_estimate=true`, `observed=false`, `policy_grade=false`; facility rows also carry `facility_assignment=true`.
- Proxy capacity is a BC class-median screening fill, not an observed facility capacity. `proxy_harvest_scaled` records are proxy capacities scaled to the provincial 1.2x harvest floor.
- Class matching forces each origin/class stream to assigned facilities of the same class. Provinces without a local assigned facility of a class use the documented national class fallback.
- Facility feedstock is the product-chain class feedstock allocated by assignment v10 assigned volume. It is not a re-measurement of facility infeed and may differ from the assigned_m3 weight.
- Process residue is generated at facilities and is kept separate from provincial harvest residue. Harvest residue is never assigned to a facility.
- Conversion uses the RSYC dry LHV from `data/derived/national/clews_supply/rsyc_backbone/national_residue_factor_summary.json`; no moisture, bark, or heat-rate adjustment is applied.
- The RSYC comparison is a screening check, not a calibration. The 129.6709 PJ value is the documented 100 Mm3 RSYC base.
- No transport, cost, revenue, capacity-expansion, tenure, AAC, or policy claim is made. No UI or public OSeCAN surface is changed.

## Tests and status

Build status: `pass`. Validation checks: 14, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.facility_residue_supply_v8` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_national_facility_chain_v5.py -q` to run the regression tests.

No policy/AAC claim is made.

## v4 centroid/local-first versus v5 node transport-aware

| Metric | Unit | v4 | v5 | Delta | Delta % |
|---|---|---:|---:|---:|---:|
| assigned_m3 | m3/yr | 118977339.099999979 | 118977339.100000083 | 0.000000104 | 0.000000000 |
| transport_cost_cad | CAD/yr | 4958493704.090264320 | 3392104138.709090233 | -1566389565.381174088 | -31.590028320 |
| transport_cost_cad_m3 | CAD/m3 | 41.675950577 | 28.510505987 | -13.165444590 | -31.590028320 |
| transport_cost_cad_gj | CAD/GJ | 10.239791297 | 7.005038326 | -3.234752971 | -31.590028320 |
| mean_road_distance_km | km | 402.122851104 | 270.289409051 | -131.833442052 | -32.784369675 |
| weighted_median_road_distance_km | km | 345.675232075 | 147.217048390 | -198.458183685 | -57.411745266 |
| p90_road_distance_km | km | 762.517038002 | 635.737453852 | -126.779584150 | -16.626459191 |
| share_ge_150_km | share | 0.838292177 | 0.486188642 | -0.352103535 | -42.002483697 |
| share_ge_300_km | share | 0.526509996 | 0.301630753 | -0.224879243 | -42.711296025 |
| facilities_used | count | 208.000000000 | 296.000000000 | 88.000000000 | 42.307692308 |
| cross_border_m3 | m3/yr | 36376.000000000 | 2325349.765417041 | 2288973.765417041 | 6292.538391844 |
| cross_border_share | share | 0.000305739 | 0.019544476 | 0.019238737 | 6292.538391844 |
| published_m3 | m3/yr | 71513883.307695001 | 54637593.770862781 | -16876289.536832221 | -23.598619955 |
| proxy_m3 | m3/yr | 47463455.792304978 | 64339745.329137303 | 16876289.536832325 | 35.556385971 |
| hhi | index_0_1 | 0.012870376 | 0.008868046 | -0.004002330 | -31.097227635 |
| top5_share | share | 0.157463893 | 0.129431842 | -0.028032050 | -17.802208312 |

Transport cost is separate from the OSeCAN official tiers. National product and residue totals are invariant.
