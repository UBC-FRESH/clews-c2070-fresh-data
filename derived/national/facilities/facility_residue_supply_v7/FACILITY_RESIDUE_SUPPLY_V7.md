# National Facility Residue Supply v7 (E1+E2c Coefficients)

This artifact recomputes facility-level class feedstock, products, and process residue on the assignment v6 `province_capacity_floor` case, and reports provincial harvest residue alongside it. Process residue is facility-assigned; harvest residue is not.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Facility residue

| Province | Facility | Class | Residue odt | Residue PJ | Residue type | Capacity status | Evidence tier |
|---|---|---|---:|---:|---|---|---|
| AB | Alberta Newsprint Company | PULP | 2,773,312 | 51.306 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| ON | Thunder Bay Pulp and Paper | PULP | 1,419,430 | 26.259 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| QC | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | 1,234,131 | 22.831 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | 1,023,030 | 18.926 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Domtar-Kamloops | PULP | 990,424.6 | 18.323 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Paper Excellence-Mackenzie | PULP | 960,161.6 | 17.763 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| NB | Irving Paper | PULP | 603,644.1 | 11.167 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| BC | Canfor Pulp-Taylor | PULP | 491,600.7 | 9.095 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Plateau Forest Products Division | SAW | 477,774.0 | 8.839 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Dunkley Lumber-Dunkley Lum | SAW | 474,936.1 | 8.786 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| QC | PF Résolu Canada inc. (Alma) | PULP | 470,918.4 | 8.712 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Entreprises Sappi Canada inc. (Matane) | PULP | 438,441.3 | 8.111 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Canfor Corporation-Houston Division | SAW | 409,300.5 | 7.572 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| NS | OSM-NS-R11703982 | PULP | 380,875.1 | 7.046 | process_residue | proxy | E2c_open_inventory_density_calibrated+class_median_proxy |
| AB | Ranger Board | SAW | 365,393.6 | 6.760 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| AB | Blue Ridge Lumber | SAW | 365,393.6 | 6.760 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| AB | High Prairie Forest Products | SAW | 365,393.6 | 6.760 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| AB | Nuway lumber | SAW | 365,393.6 | 6.760 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| AB | OSM-AB-W1282337611 | SAW | 365,393.6 | 6.760 | process_residue | proxy_harvest_scaled | E2c_open_inventory_density_calibrated+class_median_proxy_scaled_to_harvest_floor |
| BC | Canfor Corporation-Prince George | SAW | 354,834.8 | 6.564 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |

Facility process residue is 26,959,509 odt / 498.751 PJ at 18.5 GJ/odt. 208 facilities receive class-matched feedstock; 186 have positive process residue.

## Province/national totals

| Province | Process odt | Process PJ | Harvest gross odt | Harvest recoverable odt | Harvest recoverable PJ | RSYC ratio |
|---|---:|---:|---:|---:|---:|---:|
| BC | 9,805,916 | 181.409 | 6,461,417 | 3,876,850 | 71.722 | 1.6174 |
| AB | 5,493,518 | 101.630 | 3,657,251 | 2,194,351 | 40.595 | 1.6226 |
| SK | 11,594.5 | 0.214498 | 2,758,446 | 1,655,067 | 30.619 | 3.6271 |
| MB | 112,825.5 | 2.087 | 220,191.1 | 132,114.7 | 2.444 | 1.0191 |
| ON | 3,033,842 | 56.126 | 2,836,137 | 1,701,682 | 31.481 | 2.2758 |
| QC | 6,293,606 | 116.432 | 5,801,855 | 3,481,113 | 64.401 | 2.6241 |
| NB | 1,433,849 | 26.526 | 1,168,546 | 701,127.6 | 12.971 | 2.9305 |
| NS | 549,941.3 | 10.174 | 708,021.3 | 424,812.8 | 7.859 | 4.3406 |
| PE | 17,919.2 | 0.331505 | 71,917.4 | 43,150.5 | 0.798283 | 1.7351 |
| NL | 202,220.2 | 3.741 | 320,137.3 | 192,082.4 | 3.554 | 0.6421 |
| YT | 4,277.3 | 0.079131 | 11,846.3 | 7,107.8 | 0.131494 | 1.8980 |
| NT | 0.000000 | 0.000000 | 6,439.3 | 3,863.6 | 0.071477 | 0.7001 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.0000 |

National process residue: 26,959,509 odt / 498.751 PJ. National harvest residue: gross 24,022,204 odt / 444.411 PJ; recoverable 14,413,322 odt / 266.646 PJ.

## RSYC comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ at 18.5 GJ/odt. The model recoverable harvest residue is 14,413,322 odt / 266.646 PJ, ratio 2.0358 (`model_above_rsyc`).

The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ. The familiar 129.6709 PJ figure is that 100 Mm3 reference, not a 119 Mm3 value; the 119 Mm3 base is derived with the same province factors and the documented LHV.

Process residue is not added to the RSYC comparison. A combined process plus recoverable harvest stream is 41,372,831 odt / 765.397 PJ, labelled `combined` and not RSYC-comparable.

## Proxy/concentration

- Facilities used: 208.
- HHI of facility process residue: 0.028873; effective facility count: 34.6.
- Top 1 share: 11.27%; top 5 share: 29.51%.
- Published-capacity share of process residue: 62.22%.
- Proxy-capacity share of process residue: 37.78% (scaled proxy: 29.87%).
- National class fallback share of process residue: 5.20% (1,401,512 odt).
- Cross-border process residue (facility province differs from origin): 5.22% (1,406,576 odt). Assignment v6 cross-border volume differs from the class-fallback cross-border residue because the fallback routes origin class streams to facilities in other provinces.

### Top facilities by process residue

| Rank | Facility | Class | Province | Residue odt | Share | Capacity status |
|---:|---|---|---|---:|---:|---|
| 1 | Alberta Newsprint Company | PULP | AB | 2,773,312 | 10.29% | proxy_harvest_scaled |
| 2 | Thunder Bay Pulp and Paper | PULP | ON | 1,419,430 | 5.27% | proxy_harvest_scaled |
| 3 | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | QC | 1,234,131 | 4.58% | published |
| 4 | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | QC | 1,023,030 | 3.79% | published |
| 5 | Domtar-Kamloops | PULP | BC | 990,424.6 | 3.67% | published |
| 6 | Paper Excellence-Mackenzie | PULP | BC | 960,161.6 | 3.56% | published |
| 7 | Irving Paper | PULP | NB | 603,644.1 | 2.24% | proxy |
| 8 | Canfor Pulp-Taylor | PULP | BC | 491,600.7 | 1.82% | published |
| 9 | Canfor Corporation-Plateau Forest Products Division | SAW | BC | 477,774.0 | 1.77% | published |
| 10 | Dunkley Lumber-Dunkley Lum | SAW | BC | 474,936.1 | 1.76% | published |
| 11 | PF Résolu Canada inc. (Alma) | PULP | QC | 470,918.4 | 1.75% | published |
| 12 | Entreprises Sappi Canada inc. (Matane) | PULP | QC | 438,441.3 | 1.63% | published |
| 13 | Canfor Corporation-Houston Division | SAW | BC | 409,300.5 | 1.52% | published |
| 14 | OSM-NS-R11703982 | PULP | NS | 380,875.1 | 1.41% | proxy |
| 15 | Ranger Board | SAW | AB | 365,393.6 | 1.36% | proxy_harvest_scaled |
| 16 | Blue Ridge Lumber | SAW | AB | 365,393.6 | 1.36% | proxy_harvest_scaled |
| 17 | High Prairie Forest Products | SAW | AB | 365,393.6 | 1.36% | proxy_harvest_scaled |
| 18 | Nuway lumber | SAW | AB | 365,393.6 | 1.36% | proxy_harvest_scaled |
| 19 | OSM-AB-W1282337611 | SAW | AB | 365,393.6 | 1.36% | proxy_harvest_scaled |
| 20 | Canfor Corporation-Prince George | SAW | BC | 354,834.8 | 1.32% | published |

## Labels and caveats

- `model_estimate=true`, `observed=false`, `policy_grade=false`; facility rows also carry `facility_assignment=true`.
- Proxy capacity is a BC class-median screening fill, not an observed facility capacity. `proxy_harvest_scaled` records are proxy capacities scaled to the provincial 1.2x harvest floor.
- Class matching forces each origin/class stream to assigned facilities of the same class. Provinces without a local assigned facility of a class use the documented national class fallback.
- Facility feedstock is the product-chain class feedstock allocated by assignment v6 assigned volume. It is not a re-measurement of facility infeed and may differ from the assigned_m3 weight.
- Process residue is generated at facilities and is kept separate from provincial harvest residue. Harvest residue is never assigned to a facility.
- Conversion uses the RSYC dry LHV from `data/derived/national/clews_supply/rsyc_backbone/national_residue_factor_summary.json`; no moisture, bark, or heat-rate adjustment is applied.
- The RSYC comparison is a screening check, not a calibration. The 129.6709 PJ value is the documented 100 Mm3 RSYC base.
- No transport, cost, revenue, capacity-expansion, tenure, AAC, or policy claim is made. No UI or public OSeCAN surface is changed.

## Tests and status

Build status: `pass`. Validation checks: 14, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.facility_residue_supply_v7` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_facility_residue_supply_v7.py -q` to run the regression tests.

No policy/AAC claim is made.
