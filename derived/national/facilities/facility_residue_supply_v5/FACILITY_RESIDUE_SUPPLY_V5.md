# National Facility Residue Supply v5 (Total Residue)

This artifact recomputes facility-level class feedstock, products, and process residue on the assignment v6 `province_capacity_floor` case, and reports provincial harvest residue alongside it. Process residue is facility-assigned; harvest residue is not.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Facility residue

| Province | Facility | Class | Residue odt | Residue PJ | Residue type | Capacity status | Evidence tier |
|---|---|---|---:|---:|---|---|---|
| AB | Alberta Newsprint Company | PULP | 1,462,275 | 27.052 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| QC | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | 1,234,131 | 22.831 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | 1,023,030 | 18.926 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Domtar-Kamloops | PULP | 990,424.6 | 18.323 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Paper Excellence-Mackenzie | PULP | 960,161.6 | 17.763 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| ON | Thunder Bay Pulp and Paper | PULP | 861,954.5 | 15.946 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Ranger Board | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Blue Ridge Lumber | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | High Prairie Forest Products | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Nuway lumber | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | OSM-AB-W1282337611 | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| NB | Irving Paper | PULP | 603,644.1 | 11.167 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| BC | Canfor Pulp-Taylor | PULP | 491,600.7 | 9.095 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Plateau Forest Products Division | SAW | 477,774.0 | 8.839 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Dunkley Lumber-Dunkley Lum | SAW | 474,936.1 | 8.786 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| QC | PF Résolu Canada inc. (Alma) | PULP | 470,918.4 | 8.712 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Entreprises Sappi Canada inc. (Matane) | PULP | 438,441.3 | 8.111 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| AB | West Fraser | SAW | 430,455.8 | 7.963 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| BC | Canfor Corporation-Houston Division | SAW | 409,300.5 | 7.572 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Prince George | SAW | 354,834.8 | 6.564 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |

Facility process residue is 27,816,974 odt / 514.614 PJ at 18.5 GJ/odt. 208 facilities receive class-matched feedstock; 186 have positive process residue.

## Province/national totals

| Province | Process odt | Process PJ | Harvest gross odt | Harvest recoverable odt | Harvest recoverable PJ | RSYC ratio |
|---|---:|---:|---:|---:|---:|---:|
| BC | 9,744,336 | 180.270 | 6,461,417 | 3,876,850 | 71.722 | 1.6174 |
| AB | 5,770,121 | 106.747 | 1,744,909 | 1,241,739 | 22.972 | 0.7742 |
| SK | 683,522.2 | 12.645 | 331,176.8 | 235,677.2 | 4.360 | 0.4355 |
| MB | 185,286.0 | 3.428 | 86,533.9 | 61,580.6 | 1.139 | 0.4005 |
| ON | 3,088,824 | 57.143 | 1,028,556 | 731,957.3 | 13.541 | 0.8254 |
| QC | 6,226,162 | 115.184 | 5,801,855 | 3,481,113 | 64.401 | 2.6241 |
| NB | 1,395,163 | 25.811 | 1,168,546 | 701,127.6 | 12.971 | 2.9305 |
| NS | 547,247.1 | 10.124 | 182,045.2 | 129,549.9 | 2.397 | 1.1161 |
| PE | 47,544.7 | 0.879578 | 23,036.1 | 16,393.3 | 0.303277 | 0.5558 |
| NL | 124,450.2 | 2.302 | 110,834.8 | 78,874.0 | 1.459 | 0.2223 |
| YT | 4,318.4 | 0.079891 | 11,846.3 | 7,107.8 | 0.131494 | 1.8980 |
| NT | 0.000000 | 0.000000 | 2,772.8 | 1,973.2 | 0.036504 | 0.3015 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.0000 |

National process residue: 27,816,974 odt / 514.614 PJ. National harvest residue: gross 16,953,529 odt / 313.640 PJ; recoverable 10,563,943 odt / 195.433 PJ.

## RSYC comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ at 18.5 GJ/odt. The model recoverable harvest residue is 10,172,117 odt / 188.184 PJ, ratio 1.4367 (`model_above_rsyc`).

The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ. The familiar 129.6709 PJ figure is that 100 Mm3 reference, not a 119 Mm3 value; the 119 Mm3 base is derived with the same province factors and the documented LHV.

Process residue is not added to the RSYC comparison. A combined process plus recoverable harvest stream is 38,380,917 odt / 710.047 PJ, labelled `combined` and not RSYC-comparable.

## Proxy/concentration

- Facilities used: 208.
- HHI of facility process residue: 0.018359; effective facility count: 54.5.
- Top 1 share: 5.72%; top 5 share: 21.21%.
- Published-capacity share of process residue: 60.59%.
- Proxy-capacity share of process residue: 39.41% (scaled proxy: 31.96%).
- National class fallback share of process residue: 3.81% (1,060,451 odt).
- Cross-border process residue (facility province differs from origin): 3.83% (1,066,043 odt). Assignment v6 cross-border volume differs from the class-fallback cross-border residue because the fallback routes origin class streams to facilities in other provinces.

### Top facilities by process residue

| Rank | Facility | Class | Province | Residue odt | Share | Capacity status |
|---:|---|---|---|---:|---:|---|
| 1 | Alberta Newsprint Company | PULP | AB | 1,462,275 | 5.26% | proxy_harvest_scaled |
| 2 | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | QC | 1,234,131 | 4.44% | published |
| 3 | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | QC | 1,023,030 | 3.68% | published |
| 4 | Domtar-Kamloops | PULP | BC | 990,424.6 | 3.56% | published |
| 5 | Paper Excellence-Mackenzie | PULP | BC | 960,161.6 | 3.45% | published |
| 6 | Thunder Bay Pulp and Paper | PULP | ON | 861,954.5 | 3.10% | proxy_harvest_scaled |
| 7 | Ranger Board | SAW | AB | 617,678.3 | 2.22% | proxy_harvest_scaled |
| 8 | Blue Ridge Lumber | SAW | AB | 617,678.3 | 2.22% | proxy_harvest_scaled |
| 9 | High Prairie Forest Products | SAW | AB | 617,678.3 | 2.22% | proxy_harvest_scaled |
| 10 | Nuway lumber | SAW | AB | 617,678.3 | 2.22% | proxy_harvest_scaled |
| 11 | OSM-AB-W1282337611 | SAW | AB | 617,678.3 | 2.22% | proxy_harvest_scaled |
| 12 | Irving Paper | PULP | NB | 603,644.1 | 2.17% | proxy |
| 13 | Canfor Pulp-Taylor | PULP | BC | 491,600.7 | 1.77% | published |
| 14 | Canfor Corporation-Plateau Forest Products Division | SAW | BC | 477,774.0 | 1.72% | published |
| 15 | Dunkley Lumber-Dunkley Lum | SAW | BC | 474,936.1 | 1.71% | published |
| 16 | PF Résolu Canada inc. (Alma) | PULP | QC | 470,918.4 | 1.69% | published |
| 17 | Entreprises Sappi Canada inc. (Matane) | PULP | QC | 438,441.3 | 1.58% | published |
| 18 | West Fraser | SAW | AB | 430,455.8 | 1.55% | proxy_harvest_scaled |
| 19 | Canfor Corporation-Houston Division | SAW | BC | 409,300.5 | 1.47% | published |
| 20 | Canfor Corporation-Prince George | SAW | BC | 354,834.8 | 1.28% | published |

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

Run `.venv/bin/python -m workflows.national.facilities.facility_residue_supply_v5` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_facility_residue_supply_v5.py -q` to run the regression tests.

No policy/AAC claim is made.
