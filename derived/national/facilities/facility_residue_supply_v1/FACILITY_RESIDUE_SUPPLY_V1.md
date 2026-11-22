# National Facility Residue Supply v1

This artifact recomputes facility-level class feedstock, products, and process residue on the assignment v3 `province_capacity_floor` case, and reports provincial harvest residue alongside it. Process residue is facility-assigned; harvest residue is not.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Facility residue

| Province | Facility | Class | Residue odt | Residue PJ | Residue type | Capacity status | Evidence tier |
|---|---|---|---:|---:|---|---|---|
| AB | Alberta Newsprint Company | PULP | 1,462,275 | 27.052 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| BC | Domtar-Kamloops | PULP | 1,125,217 | 20.817 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| BC | Paper Excellence-Mackenzie | PULP | 944,820.1 | 17.479 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| ON | Thunder Bay Pulp and Paper | PULP | 861,954.5 | 15.946 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Ranger Board | SAW | 518,257.6 | 9.588 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Blue Ridge Lumber | SAW | 518,257.6 | 9.588 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | High Prairie Forest Products | SAW | 518,257.6 | 9.588 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Nuway lumber | SAW | 518,257.6 | 9.588 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | OSM-AB-W1282337611 | SAW | 518,257.6 | 9.588 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | West Fraser | SAW | 518,257.6 | 9.588 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| BC | Canfor Pulp-Taylor | PULP | 483,745.9 | 8.949 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| BC | Canfor Corporation-Plateau Forest Products Division | SAW | 473,590.5 | 8.761 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| BC | Dunkley Lumber-Dunkley Lum | SAW | 470,777.4 | 8.709 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| AB | La Crete Sawmills | SAW | 409,301.9 | 7.572 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| BC | Canfor Corporation-Houston Division | SAW | 405,716.5 | 7.506 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| QC | Nordic Paper Québec | PULP | 380,479.7 | 7.039 | process_residue | proxy | donor_coefficient+class_median_proxy |
| QC | Cascades | PULP | 380,479.7 | 7.039 | process_residue | proxy | donor_coefficient+class_median_proxy |
| QC | Cascades Multi-Pro | PULP | 380,479.7 | 7.039 | process_residue | proxy | donor_coefficient+class_median_proxy |
| QC | Technocell | PULP | 380,479.7 | 7.039 | process_residue | proxy | donor_coefficient+class_median_proxy |
| AB | Alberta Plywood | PANEL | 354,176.4 | 6.552 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |

Facility process residue is 28,432,733 odt / 526.006 PJ at 18.5 GJ/odt. 201 facilities receive class-matched feedstock; 188 have positive process residue.

## Province/national totals

| Province | Process odt | Process PJ | Harvest gross odt | Harvest recoverable odt | Harvest recoverable PJ | RSYC ratio |
|---|---:|---:|---:|---:|---:|---:|
| BC | 10,236,495 | 189.375 | 3,047,388 | 2,168,630 | 40.120 | 0.7628 |
| AB | 5,602,654 | 103.649 | 1,744,909 | 1,241,739 | 22.972 | 0.7742 |
| SK | 682,970.8 | 12.635 | 331,176.8 | 235,677.2 | 4.360 | 0.4355 |
| MB | 178,455.0 | 3.301 | 86,533.9 | 61,580.6 | 1.139 | 0.4005 |
| ON | 3,002,660 | 55.549 | 1,028,556 | 731,957.3 | 13.541 | 0.8254 |
| QC | 6,626,191 | 122.585 | 2,033,265 | 1,446,944 | 26.768 | 0.9196 |
| NB | 1,402,638 | 25.949 | 475,243.2 | 338,200.0 | 6.257 | 1.1918 |
| NS | 533,933.3 | 9.878 | 182,045.2 | 129,549.9 | 2.397 | 1.1161 |
| PE | 47,506.4 | 0.878868 | 23,036.1 | 16,393.3 | 0.303277 | 0.5558 |
| NL | 112,325.1 | 2.078 | 110,834.8 | 78,874.0 | 1.459 | 0.2223 |
| YT | 6,905.0 | 0.127742 | 3,348.3 | 2,382.7 | 0.044081 | 0.5365 |
| NT | 0.000000 | 0.000000 | 2,772.8 | 1,973.2 | 0.036504 | 0.3015 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.0000 |

National process residue: 28,432,733 odt / 526.006 PJ. National harvest residue: gross 9,069,109 odt / 167.779 PJ; recoverable 6,453,901 odt / 119.397 PJ.

## RSYC comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ at 18.5 GJ/odt. The model recoverable harvest residue is 5,441,465 odt / 100.667 PJ, ratio 0.7686 (`model_below_rsyc`).

The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ. The familiar 129.6709 PJ figure is that 100 Mm3 reference, not a 119 Mm3 value; the 119 Mm3 base is derived with the same province factors and the documented LHV.

Process residue is not added to the RSYC comparison. A combined process plus recoverable harvest stream is 34,886,634 odt / 645.403 PJ, labelled `combined` and not RSYC-comparable.

## Proxy/concentration

- Facilities used: 201.
- HHI of facility process residue: 0.014324; effective facility count: 69.8.
- Top 1 share: 5.54%; top 5 share: 17.98%.
- Published-capacity share of process residue: 36.00%.
- Proxy-capacity share of process residue: 64.00% (scaled proxy: 33.30%).

### Top facilities by process residue

| Rank | Facility | Class | Province | Residue odt | Share | Capacity status |
|---:|---|---|---|---:|---:|---|
| 1 | Alberta Newsprint Company | PULP | AB | 1,462,275 | 5.14% | proxy_harvest_scaled |
| 2 | Domtar-Kamloops | PULP | BC | 1,125,217 | 3.96% | published |
| 3 | Paper Excellence-Mackenzie | PULP | BC | 944,820.1 | 3.32% | published |
| 4 | Thunder Bay Pulp and Paper | PULP | ON | 861,954.5 | 3.03% | proxy_harvest_scaled |
| 5 | Ranger Board | SAW | AB | 518,257.6 | 1.82% | proxy_harvest_scaled |
| 6 | Blue Ridge Lumber | SAW | AB | 518,257.6 | 1.82% | proxy_harvest_scaled |
| 7 | High Prairie Forest Products | SAW | AB | 518,257.6 | 1.82% | proxy_harvest_scaled |
| 8 | Nuway lumber | SAW | AB | 518,257.6 | 1.82% | proxy_harvest_scaled |
| 9 | OSM-AB-W1282337611 | SAW | AB | 518,257.6 | 1.82% | proxy_harvest_scaled |
| 10 | West Fraser | SAW | AB | 518,257.6 | 1.82% | proxy_harvest_scaled |
| 11 | Canfor Pulp-Taylor | PULP | BC | 483,745.9 | 1.70% | published |
| 12 | Canfor Corporation-Plateau Forest Products Division | SAW | BC | 473,590.5 | 1.67% | published |
| 13 | Dunkley Lumber-Dunkley Lum | SAW | BC | 470,777.4 | 1.66% | published |
| 14 | La Crete Sawmills | SAW | AB | 409,301.9 | 1.44% | proxy_harvest_scaled |
| 15 | Canfor Corporation-Houston Division | SAW | BC | 405,716.5 | 1.43% | published |
| 16 | Nordic Paper Québec | PULP | QC | 380,479.7 | 1.34% | proxy |
| 17 | Cascades | PULP | QC | 380,479.7 | 1.34% | proxy |
| 18 | Cascades Multi-Pro | PULP | QC | 380,479.7 | 1.34% | proxy |
| 19 | Technocell | PULP | QC | 380,479.7 | 1.34% | proxy |
| 20 | Alberta Plywood | PANEL | AB | 354,176.4 | 1.25% | proxy_harvest_scaled |

## Labels and caveats

- `model_estimate=true`, `observed=false`, `policy_grade=false`; facility rows also carry `facility_assignment=true`.
- Proxy capacity is a BC class-median screening fill, not an observed facility capacity. `proxy_harvest_scaled` records are proxy capacities scaled to the provincial 1.2x harvest floor.
- Class matching forces each origin/class stream to assigned facilities of the same class. Provinces without a local assigned facility of a class use the documented national class fallback.
- Facility feedstock is the product-chain class feedstock allocated by assignment v3 assigned volume. It is not a re-measurement of facility infeed and may differ from the assigned_m3 weight.
- Process residue is generated at facilities and is kept separate from provincial harvest residue. Harvest residue is never assigned to a facility.
- Conversion uses the RSYC dry LHV from `data/derived/national/clews_supply/rsyc_backbone/national_residue_factor_summary.json`; no moisture, bark, or heat-rate adjustment is applied.
- The RSYC comparison is a screening check, not a calibration. The 129.6709 PJ value is the documented 100 Mm3 RSYC base.
- No transport, cost, revenue, capacity-expansion, tenure, AAC, or policy claim is made. No UI or public OSeCAN surface is changed.

## Tests and status

Build status: `pass`. Validation checks: 14, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.facility_residue_supply` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_facility_residue_supply.py -q` to run the regression tests.

No policy/AAC claim is made.
