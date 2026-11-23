# Node-Level Transport-Aware Facility Assignment V10

Status: **model estimate screening** — `evidence_label=model_estimate`, `observed=false`, `policy_grade=false`. No national claim, no policy claim, and no official OSeCAN change.

## 1. What changed

V10 replaces the v9 province-centroid assignment origin with the 525 committed RSYC supply nodes from `supply_node_distance_v1`. 486 nodes carry positive 119 Mm3 harvest volume; 39 NU nodes carry zero volume and therefore have no flow. Facility capacity v3, the 1.2x provincial floor, the 118.977 Mm3 harvest total, products and residue are unchanged. No greenfield or new facility is introduced.

## 2. Node-facility LP

The v10 assignment is a bipartite transportation linear program (HiGHS) from positive-volume nodes to 591 eligible operating facilities:

- Objective: transport cost from the committed transport cost v1 curve (52.5 m3 payload, empty return, 2026 CAD) plus the v9 500 km cross-border preference penalty expressed in cost.
- Local preference penalty: **51.45 CAD/m3** (500 km equivalent); it is a soft cost penalty, not a hard flow prohibition.
- Every positive node harvest is an equality; every facility capacity v3 is a finite upper bound.
- Distance is haversine from node coordinate to facility coordinate multiplied by the facility-province road factor from the committed `facility_road_distance_audit_v2`. No full OSRM routing is run.

The supply-node v1 paired 81-route public OSRM sample is the external distance check: node median road/haversine is 1.4562 versus 1.4672 at centroids, and the province-factor transfer error at nodes has median -5.15%, p25 -11.79%, p75 +5.34%. The factor method is a screening approximation, not a routed distance for every pair.

## 3. V10 result

- Assigned **118,977,339 m3/yr** across **296 facilities**.
- Transport cost **3.392 billion CAD/yr** (28.51 CAD/m3; 7.005 CAD/GJ).
- Mean road distance **270.3 km**; median 147.2 km; p90 635.7 km; maximum 2,354.4 km.
- Share at or above 150 km **48.62%**; at or above 300 km **30.16%**.
- Local volume **116,651,989 m3/yr**; cross-border **2,325,350 m3/yr** (1.954%).
- Proxy share of assigned volume **54.08%**.

The maximum row distance is a small-volume remote-node row, not a national typical haul. It rises above the v9 centroid maximum because v10 starts at the actual northern and interior node coordinates and finite capacity pushes some remote volume to distant facilities; the volume-weighted distribution still falls sharply. The proxy share is slightly above v9 because the LP uses more facilities, including proxy-capacity facilities, to reach nearby nodes.

## 4. V9 versus V10

| Metric | Unit | V9 centroid | V9 fixed at nodes | V10 node LP | V10 vs V9 centroid | V10 vs V9 node fixed |
|---|---|---:|---:|---:|---:|---:|
| mean_road_distance_km | km | 521.972 | 677.533 | 270.289 | -48.217617149% | -60.106820047% |
| max_road_distance_km | km | 1,462.458 | 3,516.047 | 2,354.373 | 60.987400394% | -33.039195007% |
| share_ge_150_km | share | 0.835 | 0.927 | 0.486 | -41.768486525% | -47.552285393% |
| share_ge_300_km | share | 0.493 | 0.791 | 0.302 | -38.826700181% | -61.865758903% |
| transport_cost_cad | CAD/yr | 6,382,487,942.404 | 8,230,799,897.884 | 3,392,104,138.709 | -46.852948735% | -58.787673364% |
| transport_cost_cad_m3 | CAD/m3 | 53.645 | 69.180 | 28.511 | -46.852948735% | -58.787673310% |
| facilities_used | count | 203.000 | 203.000 | 296.000 | 45.812807882% | 45.812807882% |
| proxy_share_of_assigned | share | 0.529 | 0.529 | 0.541 | 2.278024389% | 2.278024484% |
| cross_border_m3 | m3/yr | 36,376.000 | 36,376.000 | 2,325,349.765 | 6292.538391844% | 6292.538379059% |
| local_m3 | m3/yr | 118,940,963.100 | 118,940,963.254 | 116,651,989.335 | -1.924462108% | -1.924462234% |

V10 transport cost is **2.990 billion CAD/yr lower** than the v9 centroid assignment and **4.839 billion CAD/yr lower** than the same v9 facility allocation evaluated at node origins.

V9 centroid shares are the v9 assignment distances. The V9 fixed at nodes column is not a new assignment: it holds the v9 facility allocation fixed and splits each v9 row by supply-node weight, so it isolates the origin effect and reproduces the committed supply-node v1 677.5 km node mean. The V10 maximum row distance is higher than the v9 centroid maximum because the node LP sees the remote node origins that the centroid hides; the mean, median, p90 and threshold shares all fall.

## 5. Can assignment reduce the 677 km node mean?

**Yes.** The v9 allocation at node origins has a 677.5 km assigned-volume-weighted mean. The v10 node-level LP has **270.3 km**, a reduction of **407.2 km (60.11%)**.

The residual is not arbitrary. A diagnostic distance-only LP with zero local-preference penalty, the same capacities and the same node supplies reaches **255.8 km**; the unconstrained nearest-facility weighted mean is **191.5 km**. The 500 km local preference therefore costs about 14.5 km of mean distance to cut cross-border volume. Facility geography and finite capacity still set a hard floor well above zero: assignment can remove the centroid-origin and local-first penalty, but cannot move facilities to the northern and interior nodes. No facility siting or greenfield optimization is performed.

## 6. Province comparison

| Province | Nodes | V9 node fixed km | V10 km | Delta km | V9 node fixed cost CAD | V10 cost CAD | V10 facilities |
|---|---:|---:|---:|---:|---:|---:|---:|
| AB | 38 | 431.7 | 220.0 | -211.6 | 1,021.6 M | 537.8 M | 20 |
| BC | 65 | 636.4 | 203.1 | -433.4 | 2,601.7 M | 871.4 M | 95 |
| MB | 39 | 741.3 | 694.0 | -47.3 | 85.8 M | 80.4 M | 6 |
| NB | 11 | 207.0 | 89.7 | -117.3 | 138.3 M | 65.3 M | 24 |
| NL | 38 | 919.8 | 805.2 | -114.5 | 135.8 M | 119.1 M | 8 |
| NS | 10 | 154.5 | 47.9 | -106.7 | 40.5 M | 15.0 M | 11 |
| NT | 65 | 876.4 | 973.9 | 97.4 | 3.2 M | 3.6 M | 10 |
| ON | 59 | 800.3 | 337.9 | -462.4 | 1,098.8 M | 475.8 M | 32 |
| PE | 6 | 71.9 | 71.8 | -0.0 | 2.6 M | 2.6 M | 2 |
| QC | 90 | 1,066.3 | 375.2 | -691.0 | 2,880.8 M | 1,040.1 M | 107 |
| SK | 29 | 489.1 | 395.1 | -94.0 | 218.8 M | 178.0 M | 3 |
| YT | 36 | 634.0 | 634.0 | -0.0 | 2.8 M | 2.8 M | 1 |

## 7. Validation and labels

- Validation all passed: `true`.
- Conservation, capacity, cost arithmetic, comparison arithmetic, distance-factor arithmetic, roll-up identities, no NaN/negative, and label checks are recorded in `summary.json`.
- V9 fixed-at-node metrics reproduce the committed supply-node v1 band table within tolerance.
- Every output row is `model_estimate`, `observed=false`, `policy_grade=false`. `assignment_change_vs_v9=true`; capacity, floor, products, residue, UI and official OSeCAN are unchanged. No national or policy claim is made.

## 8. Reproduce

`.venv/bin/python -m workflows.national.facilities.national_facility_assignment_v10`

