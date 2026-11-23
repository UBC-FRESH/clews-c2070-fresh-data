# National Facility Residue Supply v5 Trade (Measured Total Residue)

This artifact recomputes facility-level class feedstock, products, and process residue on the assignment v5 `published_plus_proxy` case, and reports provincial harvest residue alongside it. Process residue is facility-assigned; harvest residue is not.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Facility residue

| Province | Facility | Class | Residue odt | Residue PJ | Residue type | Capacity status | Evidence tier |
|---|---|---|---:|---:|---|---|---|
| QC | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | 1,234,131 | 22.831 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | 1,023,030 | 18.926 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Domtar-Kamloops | PULP | 990,424.6 | 18.323 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Paper Excellence-Mackenzie | PULP | 960,161.6 | 17.763 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| ON | Thunder Bay Pulp and Paper | PULP | 861,954.5 | 15.946 | process_residue | proxy | donor_coefficient+class_median_proxy |
| NB | Irving Paper | PULP | 603,644.1 | 11.167 | process_residue | proxy | measured_bucking_pilot+class_median_proxy |
| BC | Canfor Corporation-Radium Division | SAW | 504,800.4 | 9.339 | process_residue | published | donor_coefficient+published_mills_db_2015_infeed_proxy |
| BC | Canfor Pulp-Taylor | PULP | 491,600.7 | 9.095 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Plateau Forest Products Division | SAW | 477,774.0 | 8.839 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Dunkley Lumber-Dunkley Lum | SAW | 474,936.1 | 8.786 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| QC | PF Résolu Canada inc. (Alma) | PULP | 470,918.4 | 8.712 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| QC | Entreprises Sappi Canada inc. (Matane) | PULP | 438,441.3 | 8.111 | process_residue | published | measured_bucking_pilot+published_authorized_consumption |
| BC | Canfor Corporation-Houston Division | SAW | 409,300.5 | 7.572 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Prince George | SAW | 354,834.8 | 6.564 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | West Fraser Timber Co. Ltd.-Fraser Lake Mills | SAW | 314,825.1 | 5.824 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | West Fraser Timber Co. Ltd.-Chetwynd Forest Industries | SAW | 305,830.0 | 5.658 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Mackenzie Division | SAW | 283,231.0 | 5.240 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | West Fraser Timber Co. Ltd.-Pacific Inland Resources | SAW | 278,845.0 | 5.159 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Fort St. John Division | SAW | 271,347.7 | 5.020 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |
| BC | West Fraser Timber Co. Ltd.-100 Mile Lumber | SAW | 260,855.0 | 4.826 | process_residue | published | measured_bucking_pilot+published_mills_db_2015_infeed_proxy |

Facility process residue is 27,816,974 odt / 514.614 PJ at 18.5 GJ/odt. 263 facilities receive class-matched feedstock; 237 have positive process residue.

## Province/national totals

| Province | Process odt | Process PJ | Harvest gross odt | Harvest recoverable odt | Harvest recoverable PJ | RSYC ratio |
|---|---:|---:|---:|---:|---:|---:|
| BC | 13,781,489 | 254.958 | 6,461,417 | 3,876,850 | 71.722 | 1.6174 |
| AB | 2,227,432 | 41.207 | 1,744,909 | 1,241,739 | 22.972 | 0.7742 |
| SK | 111,436.7 | 2.062 | 331,176.8 | 235,677.2 | 4.360 | 0.4355 |
| MB | 120,306.4 | 2.226 | 86,533.9 | 61,580.6 | 1.139 | 0.4005 |
| ON | 2,624,823 | 48.559 | 1,028,556 | 731,957.3 | 13.541 | 0.8254 |
| QC | 6,834,108 | 126.431 | 5,801,855 | 3,481,113 | 64.401 | 2.6241 |
| NB | 1,391,852 | 25.749 | 1,168,546 | 701,127.6 | 12.971 | 2.9305 |
| NS | 546,121.8 | 10.103 | 182,045.2 | 129,549.9 | 2.397 | 1.1161 |
| PE | 47,532.4 | 0.879349 | 23,036.1 | 16,393.3 | 0.303277 | 0.5558 |
| NL | 121,835.3 | 2.254 | 110,834.8 | 78,874.0 | 1.459 | 0.2223 |
| YT | 10,037.9 | 0.185702 | 11,846.3 | 7,107.8 | 0.131494 | 1.8980 |
| NT | 0.000000 | 0.000000 | 2,772.8 | 1,973.2 | 0.036504 | 0.3015 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.0000 |

National process residue: 27,816,974 odt / 514.614 PJ. National harvest residue: gross 16,953,529 odt / 313.640 PJ; recoverable 10,563,943 odt / 195.433 PJ.

## RSYC comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ at 18.5 GJ/odt. The model recoverable harvest residue is 10,172,117 odt / 188.184 PJ, ratio 1.4367 (`model_above_rsyc`).

The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ. The familiar 129.6709 PJ figure is that 100 Mm3 reference, not a 119 Mm3 value; the 119 Mm3 base is derived with the same province factors and the documented LHV.

Process residue is not added to the RSYC comparison. A combined process plus recoverable harvest stream is 38,380,917 odt / 710.047 PJ, labelled `combined` and not RSYC-comparable.

## Proxy/concentration

- Facilities used: 263.
- HHI of facility process residue: 0.013413; effective facility count: 74.6.
- Top 1 share: 4.53%; top 5 share: 18.63%.
- Published-capacity share of process residue: 66.55%.
- Proxy-capacity share of process residue: 33.45% (scaled proxy: 0.00%).
- National class fallback share of process residue: 3.06% (851,678.2 odt).
- Cross-border process residue (facility province differs from origin): 19.60% (5,452,859 odt). Assignment v5 cross-border volume differs from the class-fallback cross-border residue because the fallback routes origin class streams to facilities in other provinces.

### Top facilities by process residue

| Rank | Facility | Class | Province | Residue odt | Share | Capacity status |
|---:|---|---|---|---:|---:|---|
| 1 | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | QC | 1,234,131 | 4.44% | published |
| 2 | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | QC | 1,023,030 | 3.68% | published |
| 3 | Domtar-Kamloops | PULP | BC | 990,424.6 | 3.56% | published |
| 4 | Paper Excellence-Mackenzie | PULP | BC | 960,161.6 | 3.45% | published |
| 5 | Thunder Bay Pulp and Paper | PULP | ON | 861,954.5 | 3.10% | proxy |
| 6 | Irving Paper | PULP | NB | 603,644.1 | 2.17% | proxy |
| 7 | Canfor Corporation-Radium Division | SAW | BC | 504,800.4 | 1.81% | published |
| 8 | Canfor Pulp-Taylor | PULP | BC | 491,600.7 | 1.77% | published |
| 9 | Canfor Corporation-Plateau Forest Products Division | SAW | BC | 477,774.0 | 1.72% | published |
| 10 | Dunkley Lumber-Dunkley Lum | SAW | BC | 474,936.1 | 1.71% | published |
| 11 | PF Résolu Canada inc. (Alma) | PULP | QC | 470,918.4 | 1.69% | published |
| 12 | Entreprises Sappi Canada inc. (Matane) | PULP | QC | 438,441.3 | 1.58% | published |
| 13 | Canfor Corporation-Houston Division | SAW | BC | 409,300.5 | 1.47% | published |
| 14 | Canfor Corporation-Prince George | SAW | BC | 354,834.8 | 1.28% | published |
| 15 | West Fraser Timber Co. Ltd.-Fraser Lake Mills | SAW | BC | 314,825.1 | 1.13% | published |
| 16 | West Fraser Timber Co. Ltd.-Chetwynd Forest Industries | SAW | BC | 305,830.0 | 1.10% | published |
| 17 | Canfor Corporation-Mackenzie Division | SAW | BC | 283,231.0 | 1.02% | published |
| 18 | West Fraser Timber Co. Ltd.-Pacific Inland Resources | SAW | BC | 278,845.0 | 1.00% | published |
| 19 | Canfor Corporation-Fort St. John Division | SAW | BC | 271,347.7 | 0.98% | published |
| 20 | West Fraser Timber Co. Ltd.-100 Mile Lumber | SAW | BC | 260,855.0 | 0.94% | published |

## Labels and caveats

- `model_estimate=true`, `observed=false`, `policy_grade=false`; facility rows also carry `facility_assignment=true`.
- Proxy capacity is a BC class-median screening fill, not an observed facility capacity. `proxy_harvest_scaled` records are proxy capacities scaled to the provincial 1.2x harvest floor.
- Class matching forces each origin/class stream to assigned facilities of the same class. Provinces without a local assigned facility of a class use the documented national class fallback.
- Facility feedstock is the product-chain class feedstock allocated by assignment v5 assigned volume. It is not a re-measurement of facility infeed and may differ from the assigned_m3 weight.
- Process residue is generated at facilities and is kept separate from provincial harvest residue. Harvest residue is never assigned to a facility.
- Conversion uses the RSYC dry LHV from `data/derived/national/clews_supply/rsyc_backbone/national_residue_factor_summary.json`; no moisture, bark, or heat-rate adjustment is applied.
- The RSYC comparison is a screening check, not a calibration. The 129.6709 PJ value is the documented 100 Mm3 RSYC base.
- No transport, cost, revenue, capacity-expansion, tenure, AAC, or policy claim is made. No UI or public OSeCAN surface is changed.

## Tests and status

Build status: `pass`. Validation checks: 14, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.facility_residue_supply_v5_trade` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_facility_residue_supply_v5_trade.py -q` to run the regression tests.

No policy/AAC claim is made.

## Trade sensitivity

Facility process residue is computed from the assignment-v5 `published_plus_proxy` distribution. National process residue and provincial harvest residue match the local chain v5; the facility-province process distribution differs. This is a screening counterfactual, not an interprovincial trade forecast.
