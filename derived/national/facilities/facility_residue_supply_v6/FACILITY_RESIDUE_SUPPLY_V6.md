# National Facility Residue Supply v6 (E1+E2 Coefficients)

This artifact recomputes facility-level class feedstock, products, and process residue on the assignment v6 `province_capacity_floor` case, and reports provincial harvest residue alongside it. Process residue is facility-assigned; harvest residue is not.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Facility residue

| Province | Facility | Class | Residue odt | Residue PJ | Residue type | Capacity status | Evidence tier |
|---|---|---|---:|---:|---|---|---|
| AB | Alberta Newsprint Company | PULP | 1,790,160 | 33.118 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| ON | Thunder Bay Pulp and Paper | PULP | 1,419,430 | 26.259 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| QC | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | 1,234,131 | 22.831 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | 1,023,030 | 18.926 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Domtar-Kamloops | PULP | 990,424.6 | 18.323 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Paper Excellence-Mackenzie | PULP | 960,161.6 | 17.763 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| NB | Irving Paper | PULP | 603,644.1 | 11.167 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| AB | Ranger Board | SAW | 536,394.0 | 9.923 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| AB | Blue Ridge Lumber | SAW | 536,394.0 | 9.923 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| AB | High Prairie Forest Products | SAW | 536,394.0 | 9.923 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| AB | Nuway lumber | SAW | 536,394.0 | 9.923 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| AB | OSM-AB-W1282337611 | SAW | 536,394.0 | 9.923 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| BC | Canfor Pulp-Taylor | PULP | 491,600.7 | 9.095 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Plateau Forest Products Division | SAW | 477,774.0 | 8.839 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Dunkley Lumber-Dunkley Lum | SAW | 474,936.1 | 8.786 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| QC | PF Résolu Canada inc. (Alma) | PULP | 470,918.4 | 8.712 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Entreprises Sappi Canada inc. (Matane) | PULP | 438,441.3 | 8.111 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Canfor Corporation-Houston Division | SAW | 409,300.5 | 7.572 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| AB | West Fraser | SAW | 373,809.4 | 6.915 | process_residue | proxy_harvest_scaled | e2_open_data_imputation+class_median_proxy_scaled_to_harvest_floor |
| BC | Canfor Corporation-Prince George | SAW | 354,834.8 | 6.564 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |

Facility process residue is 27,315,295 odt / 505.333 PJ at 18.5 GJ/odt. 208 facilities receive class-matched feedstock; 186 have positive process residue.

## Province/national totals

| Province | Process odt | Process PJ | Harvest gross odt | Harvest recoverable odt | Harvest recoverable PJ | RSYC ratio |
|---|---:|---:|---:|---:|---:|---:|
| BC | 9,712,741 | 179.686 | 6,461,417 | 3,876,850 | 71.722 | 1.6174 |
| AB | 5,596,867 | 103.542 | 3,033,510 | 1,820,106 | 33.672 | 1.3459 |
| SK | 467,394.2 | 8.647 | 733,418.0 | 440,050.8 | 8.141 | 0.9644 |
| MB | 143,253.2 | 2.650 | 247,561.7 | 148,537.0 | 2.748 | 1.1458 |
| ON | 3,004,210 | 55.578 | 2,802,004 | 1,681,203 | 31.102 | 2.2485 |
| QC | 6,229,428 | 115.244 | 5,801,855 | 3,481,113 | 64.401 | 2.6241 |
| NB | 1,408,439 | 26.056 | 1,168,546 | 701,127.6 | 12.971 | 2.9305 |
| NS | 530,144.3 | 9.808 | 462,101.7 | 277,261.0 | 5.129 | 2.8330 |
| PE | 26,688.6 | 0.493739 | 55,640.2 | 33,384.1 | 0.617606 | 1.3424 |
| NL | 191,851.4 | 3.549 | 319,438.5 | 191,663.1 | 3.546 | 0.6407 |
| YT | 4,277.3 | 0.079131 | 11,846.3 | 7,107.8 | 0.131494 | 1.8980 |
| NT | 0.000000 | 0.000000 | 6,325.1 | 3,795.0 | 0.070208 | 0.6877 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.0000 |

National process residue: 27,315,295 odt / 505.333 PJ. National harvest residue: gross 21,103,663 odt / 390.418 PJ; recoverable 12,662,198 odt / 234.251 PJ.

## RSYC comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ at 18.5 GJ/odt. The model recoverable harvest residue is 12,662,198 odt / 234.251 PJ, ratio 1.7884 (`model_above_rsyc`).

The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ. The familiar 129.6709 PJ figure is that 100 Mm3 reference, not a 119 Mm3 value; the 119 Mm3 base is derived with the same province factors and the documented LHV.

Process residue is not added to the RSYC comparison. A combined process plus recoverable harvest stream is 39,977,493 odt / 739.584 PJ, labelled `combined` and not RSYC-comparable.

## Proxy/concentration

- Facilities used: 208.
- HHI of facility process residue: 0.022084; effective facility count: 45.3.
- Top 1 share: 7.31%; top 5 share: 25.12%.
- Published-capacity share of process residue: 61.08%.
- Proxy-capacity share of process residue: 38.92% (scaled proxy: 31.16%).
- National class fallback share of process residue: 4.08% (1,113,671 odt).
- Cross-border process residue (facility province differs from origin): 4.10% (1,118,735 odt). Assignment v6 cross-border volume differs from the class-fallback cross-border residue because the fallback routes origin class streams to facilities in other provinces.

### Top facilities by process residue

| Rank | Facility | Class | Province | Residue odt | Share | Capacity status |
|---:|---|---|---|---:|---:|---|
| 1 | Alberta Newsprint Company | PULP | AB | 1,790,160 | 6.55% | proxy_harvest_scaled |
| 2 | Thunder Bay Pulp and Paper | PULP | ON | 1,419,430 | 5.20% | proxy_harvest_scaled |
| 3 | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | QC | 1,234,131 | 4.52% | published |
| 4 | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | QC | 1,023,030 | 3.75% | published |
| 5 | Domtar-Kamloops | PULP | BC | 990,424.6 | 3.63% | published |
| 6 | Paper Excellence-Mackenzie | PULP | BC | 960,161.6 | 3.52% | published |
| 7 | Irving Paper | PULP | NB | 603,644.1 | 2.21% | proxy |
| 8 | Ranger Board | SAW | AB | 536,394.0 | 1.96% | proxy_harvest_scaled |
| 9 | Blue Ridge Lumber | SAW | AB | 536,394.0 | 1.96% | proxy_harvest_scaled |
| 10 | High Prairie Forest Products | SAW | AB | 536,394.0 | 1.96% | proxy_harvest_scaled |
| 11 | Nuway lumber | SAW | AB | 536,394.0 | 1.96% | proxy_harvest_scaled |
| 12 | OSM-AB-W1282337611 | SAW | AB | 536,394.0 | 1.96% | proxy_harvest_scaled |
| 13 | Canfor Pulp-Taylor | PULP | BC | 491,600.7 | 1.80% | published |
| 14 | Canfor Corporation-Plateau Forest Products Division | SAW | BC | 477,774.0 | 1.75% | published |
| 15 | Dunkley Lumber-Dunkley Lum | SAW | BC | 474,936.1 | 1.74% | published |
| 16 | PF Résolu Canada inc. (Alma) | PULP | QC | 470,918.4 | 1.72% | published |
| 17 | Entreprises Sappi Canada inc. (Matane) | PULP | QC | 438,441.3 | 1.61% | published |
| 18 | Canfor Corporation-Houston Division | SAW | BC | 409,300.5 | 1.50% | published |
| 19 | West Fraser | SAW | AB | 373,809.4 | 1.37% | proxy_harvest_scaled |
| 20 | Canfor Corporation-Prince George | SAW | BC | 354,834.8 | 1.30% | published |

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

Run `.venv/bin/python -m workflows.national.facilities.facility_residue_supply_v6` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_facility_residue_supply_v6.py -q` to run the regression tests.

No policy/AAC claim is made.
