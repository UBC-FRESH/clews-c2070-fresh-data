# National Facility Residue Supply v3

This artifact recomputes facility-level class feedstock, products, and process residue on the assignment v6 `province_capacity_floor` case, and reports provincial harvest residue alongside it. Process residue is facility-assigned; harvest residue is not.

All values are screening model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Facility residue

| Province | Facility | Class | Residue odt | Residue PJ | Residue type | Capacity status | Evidence tier |
|---|---|---|---:|---:|---|---|---|
| AB | Alberta Newsprint Company | PULP | 1,462,275 | 27.052 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| BC | Domtar-Kamloops | PULP | 1,035,682 | 19.160 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| BC | Paper Excellence-Mackenzie | PULP | 1,004,036 | 18.575 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| ON | Thunder Bay Pulp and Paper | PULP | 861,954.5 | 15.946 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Ranger Board | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Blue Ridge Lumber | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | High Prairie Forest Products | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | Nuway lumber | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| AB | OSM-AB-W1282337611 | SAW | 617,678.3 | 11.427 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| QC | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | 592,842.9 | 10.968 | process_residue | published | donor_coefficient+published_authorized_consumption |
| BC | Canfor Pulp-Taylor | PULP | 514,064.5 | 9.510 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| QC | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | 491,435.6 | 9.092 | process_residue | published | donor_coefficient+published_authorized_consumption |
| BC | Canfor Corporation-Plateau Forest Products Division | SAW | 473,590.5 | 8.761 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| BC | Dunkley Lumber-Dunkley Lum | SAW | 470,777.4 | 8.709 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| AB | West Fraser | SAW | 430,455.8 | 7.963 | process_residue | proxy_harvest_scaled | donor_coefficient+class_median_proxy_scaled_to_harvest_floor |
| BC | Canfor Corporation-Houston Division | SAW | 405,716.5 | 7.506 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| NB | Irving Paper | PULP | 398,265.1 | 7.368 | process_residue | proxy | donor_coefficient+class_median_proxy |
| QC | Les Chantiers de Chibougamau ltée | SAW | 366,558.8 | 6.781 | process_residue | published | donor_coefficient+published_authorized_consumption |
| BC | Canfor Corporation-Prince George | SAW | 351,727.8 | 6.507 | process_residue | published | bc_anchor_species_group+published_mills_db_2015_infeed_proxy |
| QC | Arbec, Bois d'oeuvre inc. (L'Ascension-de-Notre-Seigneur) | SAW | 318,624.2 | 5.895 | process_residue | published | donor_coefficient+published_authorized_consumption |

Facility process residue is 28,432,733 odt / 526.006 PJ at 18.5 GJ/odt. 208 facilities receive class-matched feedstock; 186 have positive process residue.

## Province/national totals

| Province | Process odt | Process PJ | Harvest gross odt | Harvest recoverable odt | Harvest recoverable PJ | RSYC ratio |
|---|---:|---:|---:|---:|---:|---:|
| BC | 9,876,753 | 182.720 | 3,047,388 | 2,168,630 | 40.120 | 0.7628 |
| AB | 5,776,863 | 106.872 | 1,744,909 | 1,241,739 | 22.972 | 0.7742 |
| SK | 683,522.2 | 12.645 | 331,176.8 | 235,677.2 | 4.360 | 0.4355 |
| MB | 185,285.5 | 3.428 | 86,533.9 | 61,580.6 | 1.139 | 0.4005 |
| ON | 3,088,533 | 57.138 | 1,028,556 | 731,957.3 | 13.541 | 0.8254 |
| QC | 6,659,522 | 123.201 | 2,033,265 | 1,446,944 | 26.768 | 0.9196 |
| NB | 1,436,308 | 26.572 | 475,243.2 | 338,200.0 | 6.257 | 1.1918 |
| NS | 547,183.7 | 10.123 | 182,045.2 | 129,549.9 | 2.397 | 1.1161 |
| PE | 47,544.7 | 0.879578 | 23,036.1 | 16,393.3 | 0.303277 | 0.5558 |
| NL | 124,308.9 | 2.300 | 110,834.8 | 78,874.0 | 1.459 | 0.2223 |
| YT | 6,910.6 | 0.127845 | 3,348.3 | 2,382.7 | 0.044081 | 0.5365 |
| NT | 0.000000 | 0.000000 | 2,772.8 | 1,973.2 | 0.036504 | 0.3015 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.0000 |

National process residue: 28,432,733 odt / 526.006 PJ. National harvest residue: gross 9,069,109 odt / 167.779 PJ; recoverable 6,453,901 odt / 119.397 PJ.

## RSYC comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ at 18.5 GJ/odt. The model recoverable harvest residue is 5,441,465 odt / 100.667 PJ, ratio 0.7686 (`model_below_rsyc`).

The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ. The familiar 129.6709 PJ figure is that 100 Mm3 reference, not a 119 Mm3 value; the 119 Mm3 base is derived with the same province factors and the documented LHV.

Process residue is not added to the RSYC comparison. A combined process plus recoverable harvest stream is 34,886,634 odt / 645.403 PJ, labelled `combined` and not RSYC-comparable.

## Proxy/concentration

- Facilities used: 208.
- HHI of facility process residue: 0.015471; effective facility count: 64.6.
- Top 1 share: 5.59%; top 5 share: 18.30%.
- Published-capacity share of process residue: 61.34%.
- Proxy-capacity share of process residue: 38.66% (scaled proxy: 31.27%).
- National class fallback share of process residue: 3.80% (1,081,307 odt).
- Cross-border process residue (facility province differs from origin): 3.82% (1,086,899 odt). Assignment v6 cross-border volume differs from the class-fallback cross-border residue because the fallback routes origin class streams to facilities in other provinces.

### Top facilities by process residue

| Rank | Facility | Class | Province | Residue odt | Share | Capacity status |
|---:|---|---|---|---:|---:|---|
| 1 | Alberta Newsprint Company | PULP | AB | 1,462,275 | 5.14% | proxy_harvest_scaled |
| 2 | Domtar-Kamloops | PULP | BC | 1,035,682 | 3.64% | published |
| 3 | Paper Excellence-Mackenzie | PULP | BC | 1,004,036 | 3.53% | published |
| 4 | Thunder Bay Pulp and Paper | PULP | ON | 861,954.5 | 3.03% | proxy_harvest_scaled |
| 5 | Ranger Board | SAW | AB | 617,678.3 | 2.17% | proxy_harvest_scaled |
| 6 | Blue Ridge Lumber | SAW | AB | 617,678.3 | 2.17% | proxy_harvest_scaled |
| 7 | High Prairie Forest Products | SAW | AB | 617,678.3 | 2.17% | proxy_harvest_scaled |
| 8 | Nuway lumber | SAW | AB | 617,678.3 | 2.17% | proxy_harvest_scaled |
| 9 | OSM-AB-W1282337611 | SAW | AB | 617,678.3 | 2.17% | proxy_harvest_scaled |
| 10 | Fibrek S.E.N.C. (Pâtes et papiers) | PULP | QC | 592,842.9 | 2.09% | published |
| 11 | Canfor Pulp-Taylor | PULP | BC | 514,064.5 | 1.81% | published |
| 12 | Kraft Nordic S.E.C. (pâtes et papiers) | PULP | QC | 491,435.6 | 1.73% | published |
| 13 | Canfor Corporation-Plateau Forest Products Division | SAW | BC | 473,590.5 | 1.67% | published |
| 14 | Dunkley Lumber-Dunkley Lum | SAW | BC | 470,777.4 | 1.66% | published |
| 15 | West Fraser | SAW | AB | 430,455.8 | 1.51% | proxy_harvest_scaled |
| 16 | Canfor Corporation-Houston Division | SAW | BC | 405,716.5 | 1.43% | published |
| 17 | Irving Paper | PULP | NB | 398,265.1 | 1.40% | proxy |
| 18 | Les Chantiers de Chibougamau ltée | SAW | QC | 366,558.8 | 1.29% | published |
| 19 | Canfor Corporation-Prince George | SAW | BC | 351,727.8 | 1.24% | published |
| 20 | Arbec, Bois d'oeuvre inc. (L'Ascension-de-Notre-Seigneur) | SAW | QC | 318,624.2 | 1.12% | published |

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

Run `.venv/bin/python -m workflows.national.facilities.facility_residue_supply_v3` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_facility_residue_supply_v3.py -q` to run the regression tests.

No policy/AAC claim is made.
