# Facility road-distance audit v1

Generated: 2026-11-23T13:34:13+00:00

Status: **model estimate**. This audit does not change the facility assignment and makes no national claim from its 24-pair sample.

## Routing source

- Provider: OSRM public demo server
- Endpoint: `https://router.project-osrm.org` (driving profile)
- Road data: OpenStreetMap road network (ODbL-1.0, © OpenStreetMap contributors)
- Requests: 24 ok / 24 attempted; 0 failed.
- Rate limit: one request every 1.2 s.

## Sample

- Facilities sampled: 24 (4 per province across BC, AB, ON, QC, NS, NL).
- Facility universe: 689 records, 608 mapped; 81 unmapped records excluded.
- Selection: deterministic distance quantiles 0.125, 0.375, 0.625, 0.875 of eligible facilities per province. This is a stratified sample, not a random national sample.

## Comparison

| Metric | Value |
|---|---|
| Successful routes | 24 / 24 |
| Median road / haversine | 1.533792 |
| Median proxy / road | 0.848154 |
| Mean absolute proxy error | 22.284919 % |
| Sample-fitted road factor (sum road / sum haversine) | 1.860229 |
| Proxy underestimates road | 0.833333 |
| Within 10% of road distance | 0.416667 |

Positive proxy error means `haversine x 1.3` exceeds the OSRM road distance (conservative for ranking); negative means it underestimates.

## Province summary

| Province | Pairs | OK | Median road/hav | Median proxy/road | Mean abs error % | Fitted factor |
|---|---|---|---|---|---|---|
| BC | 4 | 4 | 1.470516792 | 0.888436971 | 14.688545 | 1.61387 |
| AB | 4 | 4 | 1.522141717 | 0.861547865 | 17.061328 | 1.44985 |
| ON | 4 | 4 | 1.388660127 | 0.936364494 | 6.630746 | 1.387872 |
| QC | 4 | 4 | 2.642536628 | 0.502433176 | 49.180748 | 2.557578 |
| NS | 4 | 4 | 1.319755057 | 0.993128869 | 10.120319 | 1.257214 |
| NL | 4 | 4 | 2.013333802 | 0.645780897 | 36.027828 | 2.029075 |

## Sample detail

| Pair | Facility | Class | Haversine km | OSRM km | Road/hav | Proxy/road | Proxy error % | Status |
|---|---|---|---|---|---|---|---|---|
| BC-01 | Canfor Corporation-Isle Pierre Saw | SAW | 134.670029 | 184.1075 | 1.367100772 | 0.950917465 | -4.908254 | ok |
| BC-02 | Gilbert Smith Forest Products Ltd. | SAW | 504.137012 | 682.6603 | 1.354116607 | 0.96003549 | -3.996451 | ok |
| BC-03 | Franklin Forest Products | SAW | 628.240807 | 1208.9624 | 1.924361466 | 0.675548759 | -32.445124 | ok |
| BC-04 | Kalesnikoff Lumber Co. Ltd. | SAW | 773.181733 | 1216.9361 | 1.573932812 | 0.825956477 | -17.404352 | ok |
| AB-01 | Ranger Board | SAW | 126.551417 | 258.2657 | 2.040796593 | 0.637006159 | -36.299384 | ok |
| AB-02 | Drax Entwistle - Entwistle | PELLET | 177.984666 | 296.175 | 1.664047843 | 0.781227538 | -21.877246 | ok |
| AB-03 | West Fraser | SAW | 329.465204 | 454.7396 | 1.38023559 | 0.941868192 | -5.813181 | ok |
| AB-04 | Spray Lakes Sawmills | SAW | 443.410117 | 552.9043 | 1.246936593 | 1.042555016 | 4.255502 | ok |
| ON-01 | Thunder Bay Abibow power station | BIO | 327.581586 | 412.8073 | 1.260166375 | 1.031609814 | 3.160981 | ok |
| ON-02 | OSM-ON-W952015190 | SAW | 649.619702 | 945.0061 | 1.454706649 | 0.893650965 | -10.634904 | ok |
| ON-03 | OSM-ON-W189465122 | SAW | 800.861707 | 1128.7915 | 1.409471186 | 0.922331732 | -7.766827 | ok |
| ON-04 | Chisholm Lumber | SAW | 942.94 | 1289.7996 | 1.367849068 | 0.950397256 | -4.960274 | ok |
| QC-01 | Produits forestiers Résolu | SAW | 536.919094 | 1623.7581 | 3.024213735 | 0.429863797 | -57.01362 | ok |
| QC-02 | 9551069 Canada inc. (MultiFib) | SAW | 686.294863 | 2104.1388 | 3.065939894 | 0.424013531 | -57.598647 | ok |
| QC-03 | Scierie Cojovi Toupin & fils inc. | SAW | 802.052088 | 1813.3271 | 2.260859521 | 0.575002555 | -42.499745 | ok |
| QC-04 | Fontaine inc. | SAW | 892.754005 | 1921.8397 | 2.152709132 | 0.603890224 | -39.610978 | ok |
| NS-01 | Great Northern Timber Resources In | PELLET | 27.231069 | 40.6737 | 1.4936505 | 0.870350862 | -12.964914 | ok |
| NS-02 | OSM-NS-R11703982 | PULP | 66.648689 | 95.9025 | 1.43892553 | 0.903451897 | -9.65481 | ok |
| NS-03 | Resolute Forest Facility | SAW | 124.705416 | 149.7194 | 1.200584584 | 1.082805841 | 8.280584 | ok |
| NS-04 | Brooklyn Power | BIO | 162.072106 | 192.2722 | 1.186337398 | 1.095809676 | 9.580968 | ok |
| NL-01 | OSM-NL-W961439731 | SAW | 506.796464 | 1074.0229 | 2.119239135 | 0.613427706 | -38.657229 | ok |
| NL-02 | OSM-NL-W749252371 | SAW | 639.541865 | 1272.7796 | 1.99014274 | 0.653219477 | -34.678052 | ok |
| NL-03 | Ironwood Industries/Sawmill | SAW | 639.806374 | 1271.986 | 1.988079599 | 0.65389736 | -34.610264 | ok |
| NL-04 | OSM-NL-W1098532892 | SAW | 729.29608 | 1485.2296 | 2.036524864 | 0.638342317 | -36.165768 | ok |

## Failures and limits

- Failures are reported with their exact OSRM error; no distance is imputed.
- Endpoint snap distances are recorded. 16 pair(s) snap more than 5 km from the requested coordinate.
- OSRM routes start and end at the nearest road point; the off-road connector from the province centroid or facility coordinate is not included in the routed distance. Because a connector would only add distance, the finding that the 1.3 factor underestimates road distance is conservative for these sampled centroid-to-facility pairs.
- OSRM demo is a public best-effort service; it is suitable for this 24-request audit, not for production or bulk routing.
- The OSRM car profile may route through the United States where that is the shortest road path; no border delay or customs cost is modelled.
- Only car-road distance/duration is measured. Resource-road, winter, ferry, weight, and log-truck restrictions are not validated.
- The sample is distance-stratified and province-stratified; it does not support a national mean or a replacement road factor.

## Labels

- `model_estimate`; `observed=false`; `policy_grade=false`.
- No assignment change; no legal, AAC, or operating-status claim.
- No UI or public OSeCAN surface is changed.

## Provenance

- National facility capacity v3: `data/derived/national/facilities/national_facility_capacity_v3/national_facility_capacity_v3.csv` (project-derived; see source metadata); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`
- GeoBoundaries Canada ADM1 simplified: `data/raw/boundaries/canada_adm1_geoboundaries_simplified.geojson` (CC BY 4.0); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`
- National facility assignment v6: `data/derived/national/facilities/national_facility_assignment_v6/facility_assignment.csv` (project-derived; see source metadata); `https://github.com/UBC-FRESH/clews-c2070-fresh`
- OSRM public demo server: `osrm_routes.json` (ODbL-1.0); `https://router.project-osrm.org/route/v1/driving`
- OpenStreetMap contributors: (ODbL-1.0); `https://www.openstreetmap.org/copyright`

Reproduce: `.venv/bin/python -m workflows.national.facilities.facility_road_distance_audit`
