# Supply-node distance v1

Generated: 2026-11-23T15:23:21+00:00

Status: **model estimate**. Open RSYC harvest supply nodes replace province-centroid origins; the v9 assignment is unchanged. `model_estimate`, `observed=false`, `policy_grade=false`. No national claim, no policy claim, no siting or greenfield optimization, and no UI or official OSeCAN change.

## 1. Node construction

- **525 nodes** in 13 provinces from RSYC 150-km tile x province cells with a geographic province intersection.
- Node location: centroid of the tile-province intersection (representative point when the centroid falls outside the intersection).
- Node weight: RSYC age-100 standing volume on the geographically located part of the tile-province cell, normalised within province.
- 119 Mm3 provincial harvest is assigned as province harvest x node weight. Province totals and the 118.977 Mm3 control total are preserved.
- RSYC district-fallback area with no province intersection is excluded: 16.26 Mm3 of raw RSYC production (0.03%). AB and SK contribute 12.51 Mm3 of the excluded total; Nunavut loses 2.77% of its own RSYC production but has zero harvest. Remaining weights are renormalised within province. No fallback cell is given a fabricated location.
- A SCANFI forest-area weight is carried for transparency and sensitivity. The production-area weight correlation is 0.983.

| Province | Nodes | Harvest Mm3 | Top node share | HHI | Top node |
|---|---|---|---|---|---|
| BC | 65 | 39.98 | 3.8% | 0.023 | I5|BC |
| AB | 38 | 22.89 | 7.8% | 0.043 | H7|AB |
| SK | 29 | 4.34 | 9.4% | 0.056 | H11|SK |
| MB | 39 | 1.14 | 6.4% | 0.040 | H14|MB |
| ON | 59 | 13.49 | 4.9% | 0.027 | B25|ON |
| QC | 90 | 26.67 | 4.3% | 0.022 | C26|QC |
| NB | 11 | 6.23 | 32.4% | 0.213 | E30|NB |
| NS | 10 | 2.39 | 31.6% | 0.203 | D32|NS |
| PE | 6 | 0.30 | 78.5% | 0.646 | E32|PE |
| NL | 38 | 1.45 | 8.7% | 0.048 | J31|NL |
| YT | 36 | 0.04 | 9.6% | 0.050 | R3|YT |
| NT | 65 | 0.04 | 7.0% | 0.031 | N7|NT |
| NU | 39 | 0.00 | 15.9% | 0.088 | O14|NU |

## 2. Distance comparison

Distances are haversine to eligible facility coordinates multiplied by the facility-province road factor. The node figure is harvest-weighted across nodes; the centroid figure is the unweighted ADM1 polygon centroid.

| Scope | Centroid mean km | Node weighted mean km | Delta km | Centroid median km | Node weighted median km | Centroid p90 km | Node p90 km | Centroid percentile in node distribution |
|---|---|---|---|---|---|---|---|---|
| national | 1,201.6 | 994.0 | -207.6 | 1,214.3 | 866.4 | 2,089.4 | 1,851.3 | 70.3 |

The national centroid mean sits at the 70.3 percentile of the node-facility distance distribution. The all-facility distribution is an accessibility surface; it is not the assigned-facility distance in Section 3.

| Province | Nodes | Facilities | Centroid mean km | Node mean km | Delta km | Centroid median km | Node median km | Delta km | Centroid percentile |
|---|---|---|---|---|---|---|---|---|---|
| BC | 65 | 185 | 735.3 | 791.5 | 56.2 | 889.4 | 729.9 | -159.5 | 63.7 |
| AB | 38 | 20 | 355.5 | 508.0 | 152.5 | 257.0 | 464.6 | 207.6 | 34.8 |
| SK | 29 | 3 | 319.8 | 499.2 | 179.3 | 408.4 | 454.1 | 45.7 | 37.9 |
| MB | 39 | 5 | 761.0 | 726.5 | -34.5 | 788.1 | 727.1 | -61.0 | 57.6 |
| ON | 59 | 37 | 894.7 | 905.5 | 10.8 | 1,003.2 | 838.6 | -164.5 | 59.7 |
| QC | 90 | 283 | 1,759.6 | 1,249.4 | -510.2 | 1,796.4 | 1,134.9 | -661.5 | 78.7 |
| NB | 11 | 24 | 147.9 | 198.5 | 50.5 | 139.1 | 182.7 | 43.6 | 30.0 |
| NS | 10 | 20 | 124.7 | 194.3 | 69.6 | 88.3 | 179.2 | 90.9 | 37.1 |
| PE | 6 | 2 | 66.2 | 71.9 | 5.8 | 66.0 | 73.3 | 7.3 | 17.0 |
| NL | 38 | 11 | 1,260.5 | 1,109.6 | -150.9 | 1,281.9 | 1,216.0 | -66.0 | 52.9 |
| YT | 36 | 1 | 549.7 | 634.0 | 84.3 | 549.7 | 565.7 | 16.0 | 40.0 |

Section 2 uses every eligible facility in the origin province. Section 3 uses only the facilities that the unchanged v9 assignment actually selects. The two can move in opposite directions: the all-facility centroid can sit above most node pairs while the assigned-volume-weighted mean rises, because v9 targets a selected facility subset.

### Paired OSRM sample

- 81 requests to the public OSRM demo server: 81 ok, 0 failed; 81 pairs have both node and centroid routes.
- Median node road/haversine ratio: 1.4562; centroid ratio: 1.4672; node minus centroid: 0.0546.
- Median node factor error: -5.15%; centroid factor error: 0.00%.
- Node origin snap: median 1.84 km, max 54.46 km. Large snaps mean the node is not on the road network; routed distance is a lower bound because the off-road connector is not included.

| Province | Pairs ok | Node median ratio | Audit factor | Node factor delta |
|---|---|---|---|---|
| BC | 10 | 1.7452 | 1.4742 | 18.38 |
| AB | 10 | 1.3945 | 1.3046 | 6.89 |
| SK | 3 | 1.3068 | 1.3965 | -6.43 |
| MB | 5 | 1.2169 | 1.4564 | -16.44 |
| ON | 10 | 1.5326 | 1.3590 | 12.78 |
| QC | 10 | 1.4562 | 2.4178 | -39.77 |
| NB | 10 | 1.9602 | 1.4881 | 31.73 |
| NS | 10 | 1.3445 | 1.2040 | 11.66 |
| PE | 2 | 1.0745 | 1.1102 | -3.22 |
| NL | 10 | 2.0864 | 2.0042 | 4.10 |
| YT | 1 | 1.8304 | 1.7252 | 6.10 |

The node-origin factor delta is the top-node median road/haversine ratio relative to the audit-v2 province factor. It is a transfer diagnostic only; no factor is changed and no assignment is re-run. Positive values mean the centroid-fitted factor understates node-origin road distance; negative values mean it overstates it.

The OSRM sample is a paired factor-transfer check, not a new routing product. If the sample is unavailable, the documented province factors still drive the full distance and band tables.

## 3. Band and transport-gap comparison

Bands: `[0,50)`, `[50,100)`, `[100,150)`, `[150,300)`, `[300,∞)` km. The assignment is unchanged; each v9 row is split across origin-province nodes by node weight.

| Band | Centroid share | Node share | Delta pp | Centroid mean km | Node mean km |
|---|---|---|---|---|---|
| 0-50 | 0.9% | 0.8% | 0.0 | 28.4 | 35.6 |
| 50-100 | 5.4% | 2.7% | -2.7 | 71.6 | 76.0 |
| 100-150 | 10.3% | 3.7% | -6.5 | 132.8 | 127.7 |
| 150-300 | 34.2% | 13.6% | -20.6 | 205.7 | 223.5 |
| >300 | 49.3% | 79.1% | 29.8 | 880.0 | 809.1 |

At the unchanged v9 assignment, the centroid-origin screen gives 99.34 Mm3 (83.5%) at or above 150 km and 58.66 Mm3 (49.3%) at or above 300 km. Node origins give 110.29 Mm3 (92.7%) and 94.11 Mm3 (79.1%).

| Province | Assigned Mm3 | Centroid >150 | Node >150 | Delta pp | Centroid >300 | Node >300 | Delta pp | Centroid mean km | Node mean km | Delta km |
|---|---|---|---|---|---|---|---|---|---|---|
| BC | 39.98 | 76.4% | 96.3% | 19.84 | 23.8% | 86.0% | 62.27 | 220.2 | 636.4 | 416.3 |
| AB | 22.89 | 87.3% | 89.6% | 2.31 | 21.8% | 68.7% | 46.88 | 228.5 | 431.7 | 203.1 |
| SK | 4.34 | 60.0% | 93.0% | 32.98 | 60.0% | 69.8% | 9.77 | 302.1 | 489.1 | 187.0 |
| MB | 1.14 | 100.0% | 99.1% | -0.86 | 100.0% | 88.0% | -12.02 | 787.6 | 741.3 | -46.3 |
| ON | 13.49 | 100.0% | 96.1% | -3.90 | 90.5% | 86.1% | -4.34 | 700.8 | 800.3 | 99.5 |
| QC | 26.67 | 100.0% | 98.3% | -1.74 | 100.0% | 95.6% | -4.43 | 1,267.7 | 1,066.3 | -201.4 |
| NB | 6.23 | 53.6% | 68.1% | 14.52 | 0.0% | 21.8% | 21.82 | 159.0 | 207.0 | 48.0 |
| NS | 2.39 | 0.0% | 49.9% | 49.89 | 0.0% | 8.6% | 8.58 | 56.6 | 154.5 | 97.9 |
| PE | 0.30 | 0.0% | 1.5% | 1.54 | 0.0% | 0.0% | 0.00 | 66.1 | 71.9 | 5.8 |
| NL | 1.45 | 100.0% | 97.4% | -2.56 | 100.0% | 81.7% | -18.27 | 947.7 | 919.8 | -28.0 |
| YT | 0.04 | 100.0% | 98.8% | -1.19 | 100.0% | 86.2% | -13.78 | 549.7 | 634.0 | 84.3 |
| NT | 0.04 | 100.0% | 100.0% | 0.00 | 100.0% | 99.2% | -0.76 | 1,147.0 | 876.4 | -270.6 |

### Local-capacity access

Node local capacity is the harvest-weighted expectation of same-province, same-class capacity within 150 or 300 km. It double-counts facilities across nodes and is an accessibility measure, not an additional capacity stock. The gap is `max(0, assigned - expected accessible capacity)`.

| Province | Assigned Mm3 | Centroid cap 150 Mm3 | Node cap 150 Mm3 | Centroid gap 150 Mm3 | Node gap 150 Mm3 | Centroid cap 300 Mm3 | Node cap 300 Mm3 |
|---|---|---|---|---|---|---|---|
| BC | 39.98 | 9.42 | 3.66 | 30.56 | 36.32 | 30.47 | 13.84 |
| AB | 22.89 | 0.72 | 0.72 | 22.18 | 22.17 | 4.52 | 2.21 |
| SK | 4.34 | 0.24 | 0.05 | 4.11 | 4.29 | 0.24 | 0.21 |
| MB | 1.14 | 0.00 | 0.01 | 1.14 | 1.13 | 0.00 | 0.09 |
| ON | 13.49 | 0.00 | 0.37 | 13.49 | 13.12 | 0.91 | 1.39 |
| QC | 26.67 | 0.00 | 1.58 | 26.67 | 25.09 | 0.00 | 5.04 |
| NB | 6.23 | 2.90 | 2.50 | 3.34 | 3.73 | 9.91 | 6.92 |
| NS | 2.39 | 6.10 | 4.18 | 0.00 | 0.00 | 9.85 | 8.25 |
| PE | 0.30 | 0.47 | 0.47 | 0.00 | 0.00 | 0.47 | 0.47 |
| NL | 1.45 | 0.00 | 0.05 | 1.45 | 1.41 | 0.00 | 0.33 |
| YT | 0.04 | 0.00 | 0.00 | 0.04 | 0.04 | 0.00 | 0.03 |
| NT | 0.04 | 0.00 | 0.00 | 0.04 | 0.04 | 0.00 | 0.00 |

## 4. Centroid bias

- Assigned-volume-weighted mean distance: centroid 522.0 km, node 677.5 km; delta 155.6 km (29.8%).
- >150 km share delta: 9.21 percentage points; >300 km share delta: 29.79 percentage points.
- Transport cost delta: 1.848 billion CAD (28.96%); CAD/m3 delta 15.53.
- National node-weighted distance distribution vs centroid: mean delta -207.6 km, median delta -347.8 km, p90 delta -238.1 km.

| Province | Centroid km | Node km | Delta km | >150 delta pp | >300 delta pp | CAD/m3 delta |
|---|---|---|---|---|---|---|
| BC | 220.2 | 636.4 | 416.3 | 19.84 | 62.27 | 41.57 |
| NT | 1,147.0 | 876.4 | -270.6 | 0.00 | -0.76 | -27.02 |
| AB | 228.5 | 431.7 | 203.1 | 2.31 | 46.88 | 20.28 |
| QC | 1,267.7 | 1,066.3 | -201.4 | -1.74 | -4.43 | -20.12 |
| SK | 302.1 | 489.1 | 187.0 | 32.98 | 9.77 | 18.67 |
| ON | 700.8 | 800.3 | 99.5 | -3.90 | -4.34 | 9.94 |
| NS | 56.6 | 154.5 | 97.9 | 49.89 | 8.58 | 9.78 |
| YT | 549.7 | 634.0 | 84.3 | -1.19 | -13.78 | 8.42 |
| NB | 159.0 | 207.0 | 48.0 | 14.52 | 21.82 | 4.79 |
| MB | 787.6 | 741.3 | -46.3 | -0.86 | -12.02 | -4.62 |
| NL | 947.7 | 919.8 | -28.0 | -2.56 | -18.27 | -2.79 |
| PE | 66.1 | 71.9 | 5.8 | 1.54 | 0.00 | 0.58 |

**How much centroid bias remains?** The measured province-centroid bias is the centroid-origin deviation above; the node-origin recomputation removes that measured bias by construction. Residual uncertainty is within-tile harvest heterogeneity, node-to-facility road-factor transfer, and off-road endpoint connectors. The OSRM paired sample quantifies the factor and snap component; the within-tile component cannot be removed with 150-km tiles and is not fabricated.

## 5. Weight-basis sensitivity

The assignment and distances are identical; only the within-province node weights change. This is a sensitivity check, not a second assignment.

| Weight basis | Assigned Mm3 | >150 share | >300 share | Mean km | CAD/m3 |
|---|---|---|---|---|---|
| rsyc_production | 118.98 | 92.7% | 79.1% | 677.5 | 69.18 |
| scanfi_area | 118.98 | 93.4% | 80.5% | 724.8 | 73.90 |

## 6. Method and limits

- The v9 `province_capacity_floor` assignment is read-only; no facility target, assigned volume, capacity, or cross-border flow is changed.
- Node volumes are proportional to RSYC age-100 standing volume on the located tile-province area, not observed harvest. The 119 Mm3 provincial control is a planning case, not a legal AAC.
- Distances are road-factor screening distances, not observed routes. The OSRM demo sample is best-effort and public; resource roads, winter roads, ferries, weight limits, log-truck restrictions, and border delays are not validated.
- Node local capacity is a harvest-weighted expectation and double-counts facilities across nodes. It is not a siting constraint or an additional capacity stock.
- This is not a national statistic, national average, policy recommendation, official OSeCAN result, UI product, or greenfield optimization.

## 7. Labels and provenance

- `evidence_label=model_estimate`; `observed=false`; `policy_grade=false`; `national_claim=false`; `assignment_change=false`; `official_osecan_changed=false`; `ui_changed=false`; `siting_optimization=false`; `greenfield_optimization=false`.
- Inputs: RSYC tile production library and tiles, tile ecodistrict province weights, SCANFI ecodistrict area weights, GeoBoundaries ADM1, 119 Mm3 harvest, facility capacity v3, road-distance audit v2 factors and paired sample, transport cost v1 parameters, v9 assignment, and OSRM/OpenStreetMap.
- OSRM: public demo server, ODbL-1.0, © OpenStreetMap contributors. No paid API key is used.

Reproduce: `.venv/bin/python -m workflows.national.facilities.supply_node_distance_v1`
