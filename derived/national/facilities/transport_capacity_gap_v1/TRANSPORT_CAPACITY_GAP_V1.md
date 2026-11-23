# Transport-Radius Capacity Gap V1

Status: **model estimate screening** — `evidence_label=model_estimate`, `observed=false`, `policy_grade=false`. No national claim, no policy recommendation, no official OSeCAN change, no UI change, and no siting optimization.

## 1. Scope and method

- Harvest volume: the committed 119 Mm3 provincial offers assigned to facilities in v8 (published-first local-first) and v9 (transport-cost minimization with a 500 km local preference).
- Capacity: eligible operating, located facilities in capacity v3 after the 1.2x provincial harvest floor scaling used by v9.
- Distance: haversine from the **unweighted ADM1 polygon centroid** of the origin province to the facility coordinate, multiplied by the facility-province road factor from `facility_road_distance_audit_v2`.
- Bands: `[0, 50)`, `[50, 100)`, `[100, 150)`, `[150, 300)`, `[300, ∞)` km.
- Long-haul exposure: assigned volume at or above 150 km. Stranded volume: assigned volume at or above 300 km.
- Local access gap at a threshold: `max(0, assigned - eligible same-province capacity of the same facility class within the threshold)`. This is a capacity-existence measure, not the actual volume that traveled beyond the threshold.

> **Centroid-origin caveat.** These are province-centroid to facility screening distances, not actual harvest-node origins, routed distances, or observed truck trips. A facility near a province's population or geometric centre can still be hundreds of kilometres from the centroid. The results are therefore an accessibility screen, not a local supply audit or a siting recommendation.

## 2. Scenario totals

| Scenario | Assigned Mm3 | >150 km Mm3 | >150 share | >300 km Mm3 | >300 share | Mean km | Transport CAD | CAD/m3 | Avoidable CAD (>150, 50 km ref) |
|---|---|---|---|---|---|---|---|---|---|
| v8 | 118.98 | 99.81 | 83.9% | 67.42 | 56.7% | 558.5 | 6,816,930,869 | 57.30 | 5,930,691,551 |
| v9 | 118.98 | 99.34 | 83.5% | 58.66 | 49.3% | 522.0 | 6,382,487,942 | 53.64 | 5,495,257,480 |

- Assigned volume is conserved at **118.98 Mm3** in both v8 and v9.
- V9 lowers the assigned-volume-weighted mean centroid-origin road distance from **558.5 km** to **522.0 km**.
- V9 transport cost is **53.64 CAD/m3** versus **57.30 CAD/m3** in v8 on the same truck curve.

## 3. Distance bands

Aggregated across province/class cells. Eligible local capacity is same-province capacity of the assigned class; each facility appears once in this local-capacity column.

### V8

| Band | Assigned Mm3 | Share | Eligible local capacity Mm3 | Local headroom Mm3 | Utilization |
|---|---|---|---|---|---|
| 0-50 | 1.03 | 0.9% | 1.03 | 0.00 | 100.0% |
| 50-100 | 5.94 | 5.0% | 9.82 | 3.88 | 60.5% |
| 100-150 | 12.20 | 10.3% | 12.67 | 0.47 | 96.3% |
| 150-300 | 32.39 | 27.2% | 48.10 | 15.71 | 67.3% |
| >300 | 67.42 | 56.7% | 201.84 | 134.43 | 33.4% |

### V9

| Band | Assigned Mm3 | Share | Eligible local capacity Mm3 | Local headroom Mm3 | Utilization |
|---|---|---|---|---|---|
| 0-50 | 1.03 | 0.9% | 1.03 | 0.00 | 100.0% |
| 50-100 | 6.41 | 5.4% | 9.82 | 3.41 | 65.3% |
| 100-150 | 12.20 | 10.3% | 12.67 | 0.47 | 96.3% |
| 150-300 | 40.67 | 34.2% | 48.10 | 7.43 | 84.6% |
| >300 | 58.66 | 49.3% | 201.84 | 143.18 | 29.1% |

The >300 km band carries the largest assigned share. The large >300 km eligible local capacity is partly a centroid artifact: facilities in large provinces such as BC and QC are far from the single ADM1 centroid even when they are locally important.

## 4. Capacity gaps by province and class

Top v9 cells by local access gap within 150 km. `Gap 0-150` is assigned volume minus eligible same-province, same-class capacity within 150 km.

| Province | Class | Assigned Mm3 | GT150 Mm3 | GT300 Mm3 | Local cap 0-150 Mm3 | Gap 0-150 Mm3 | Mean km | Avoidable CAD |
|---|---|---|---|---|---|---|---|---|
| QC | SAW | 16.80 | 16.80 | 16.80 | 0.00 | 16.80 | 1,255.1 | 2,022,057,306 |
| BC | SAW | 20.21 | 14.24 | 5.02 | 5.97 | 14.24 | 211.8 | 291,283,681 |
| BC | PULP | 10.33 | 10.33 | 1.80 | 0.00 | 10.33 | 241.9 | 197,979,671 |
| AB | PULP | 8.09 | 8.09 | 0.00 | 0.00 | 8.09 | 180.0 | 105,059,274 |
| AB | SAW | 7.45 | 7.45 | 2.13 | 0.00 | 7.45 | 266.4 | 160,911,172 |
| ON | SAW | 7.20 | 7.20 | 6.94 | 0.00 | 7.20 | 919.5 | 625,364,449 |
| QC | PULP | 5.11 | 5.11 | 5.11 | 0.00 | 5.11 | 1,334.1 | 655,742,248 |
| BC | BIO | 4.67 | 3.14 | 1.69 | 1.53 | 3.14 | 216.8 | 72,996,098 |
| ON | BIO | 2.98 | 2.98 | 1.99 | 0.00 | 2.98 | 418.9 | 109,810,482 |
| ON | PULP | 2.86 | 2.86 | 2.86 | 0.00 | 2.86 | 451.3 | 114,798,450 |
| AB | BIO | 5.61 | 2.81 | 2.81 | 2.81 | 2.81 | 244.2 | 83,222,809 |
| SK | SAW | 4.34 | 2.61 | 2.61 | 1.74 | 2.61 | 302.1 | 93,306,434 |

The same cells under v8, for comparison:

| Province | Class | v8 assigned Mm3 | v8 GT300 Mm3 | v9 assigned Mm3 | v9 GT300 Mm3 | v9 mean km |
|---|---|---|---|---|---|---|
| QC | SAW | 14.54 | 14.54 | 16.80 | 16.80 | 1,255.1 |
| BC | SAW | 23.65 | 9.40 | 20.21 | 5.02 | 211.8 |
| BC | PULP | 3.44 | 2.09 | 10.33 | 1.80 | 241.9 |
| AB | PULP | 8.09 | 0.00 | 8.09 | 0.00 | 180.0 |
| AB | SAW | 6.06 | 0.74 | 7.45 | 2.13 | 266.4 |
| ON | SAW | 7.20 | 6.94 | 7.20 | 6.94 | 919.5 |
| QC | PULP | 5.46 | 5.46 | 5.11 | 5.11 | 1,334.1 |
| BC | BIO | 5.58 | 3.23 | 4.67 | 1.69 | 216.8 |
| ON | BIO | 2.98 | 1.99 | 2.98 | 1.99 | 418.9 |
| ON | PULP | 2.86 | 2.86 | 2.86 | 2.86 | 451.3 |
| AB | BIO | 5.61 | 2.81 | 5.61 | 2.81 | 244.2 |
| SK | SAW | 4.34 | 2.61 | 4.34 | 2.61 | 302.1 |

## 5. Stranded provinces

The high-exposure flag is a screening flag: at least 50% of assigned volume at or above the threshold and at least 1 Mm3/yr assigned. Small provinces can have high shares on small absolute volumes.

| Province | Assigned Mm3 | >150 share | >300 share | Top stranded class | Top class Mm3 | Gap 0-150 Mm3 | Mean km | Avoidable CAD | High >300 flag |
|---|---|---|---|---|---|---|---|---|---|
| QC | 26.67 | 100.0% | 100.0% | SAW | 16.80 | 26.67 | 1,267.7 | 3,243,763,657 | true |
| NL | 1.45 | 100.0% | 100.0% | PULP | 1.45 | 1.45 | 947.7 | 130,356,973 | true |
| MB | 1.14 | 100.0% | 100.0% | SAW | 1.13 | 1.14 | 787.6 | 83,619,868 | true |
| YT | 0.04 | 100.0% | 100.0% | SAW | 0.04 | 0.04 | 549.7 | 2,191,933 | false |
| NT | 0.04 | 100.0% | 100.0% | PANEL | 0.04 | 0.04 | 1,147.0 | 3,985,117 | false |
| ON | 13.49 | 100.0% | 90.5% | SAW | 6.94 | 13.49 | 700.8 | 876,913,430 | true |
| SK | 4.34 | 60.0% | 60.0% | SAW | 2.61 | 2.61 | 302.1 | 93,306,434 | true |
| BC | 39.98 | 76.4% | 23.8% | SAW | 5.02 | 30.56 | 220.2 | 623,681,346 | false |
| AB | 22.89 | 87.3% | 21.8% | BIO | 2.81 | 19.99 | 228.5 | 382,740,366 | false |
| NB | 6.23 | 53.6% | 0.0% | — | 0.00 | 3.34 | 159.0 | 54,698,355 | false |
| NS | 2.39 | 0.0% | 0.0% | — | 0.00 | 0.00 | 56.6 | 0 | false |
| PE | 0.30 | 0.0% | 0.0% | — | 0.00 | 0.00 | 66.1 | 0 | false |

V9 provinces meeting the high >300 km exposure screen: **QC** (100.0% of 26.67 Mm3), **NL** (100.0% of 1.45 Mm3), **MB** (100.0% of 1.14 Mm3), **ON** (90.5% of 13.49 Mm3), **SK** (60.0% of 4.34 Mm3).

Provinces with the largest absolute >300 km volumes dominate the stranded total even when their share is lower: **QC** (26.67 Mm3), **ON** (12.21 Mm3), **BC** (9.50 Mm3), **AB** (5.00 Mm3), **SK** (2.61 Mm3).

## 6. Greenfield/local capacity screening

The table ranks v9 province/class cells by the modelled transport cost reduction if their >150 km volume were served at a 50 km reference distance. This is a screening counterfactual, not a siting optimization. It ignores greenfield capital, feedstock availability, landbase, facility scale, permitting, and product or residue constraints; rows are not additive across classes without capacity reconciliation.

| Rank | Province | Class | GT150 Mm3 | GT300 Mm3 | Avoidable m3*km | Avoidable CAD | Share of v9 avoidable CAD |
|---|---|---|---|---|---|---|---|
| 1 | QC | SAW | 16.80 | 16.80 | 20.25 billion | 2,022,057,306 | 36.8% |
| 2 | QC | PULP | 5.11 | 5.11 | 6.57 billion | 655,742,248 | 11.9% |
| 3 | ON | SAW | 7.20 | 6.94 | 6.26 billion | 625,364,449 | 11.4% |
| 4 | BC | SAW | 14.24 | 5.02 | 2.92 billion | 291,283,681 | 5.3% |
| 5 | QC | BIO | 2.34 | 2.34 | 2.75 billion | 274,347,467 | 5.0% |
| 6 | BC | PULP | 10.33 | 1.80 | 1.98 billion | 197,979,671 | 3.6% |
| 7 | QC | PELLET | 1.52 | 1.52 | 1.75 billion | 174,341,175 | 3.2% |
| 8 | AB | SAW | 7.45 | 2.13 | 1.61 billion | 160,911,172 | 2.9% |
| 9 | NL | PULP | 1.45 | 1.45 | 1.31 billion | 130,356,973 | 2.4% |
| 10 | QC | PANEL | 0.91 | 0.91 | 1.17 billion | 117,275,462 | 2.1% |

The v8 ranking is retained in `greenfield_local_capacity_priority.csv`; the v9 ranking is the primary transport-aware screen.

## 7. Validation

- `band_volume_conservation`: True
- `source_assignment_totals`: True
- `band_cell_sums_match_capacity_gap`: True
- `band_shares_sum_to_one`: True
- `threshold_partitions`: True
- `capacity_partitions`: True
- `band_capacity_comparison`: True
- `capacity_headroom_identity`: True
- `province_partitions`: True
- `priority_rank_order`: True
- `no_nan_or_infinite`: True
- `no_negative_volumes_or_costs`: True
- `capacity_total_matches_layer`: True
- `labels`: True
- `all_passed`: True

## 8. Caveats

- Road distances are province-centroid to facility screening distances, not actual harvest-node origins, routed distances, or observed truck trips. The centroid is an unweighted ADM1 polygon centroid.
- The analysis inherits the v8/v9 assignment and capacity v3 model assumptions, including the 1.2x provincial capacity floor and proxy capacity scaling. It does not re-optimize assignment or capacity.
- Eligible local capacity is same-province operating located capacity of the assigned facility class. All-province capacity is shown only as context and can overlap across origin provinces.
- The local access gap is a capacity-existence measure. It is not the same as the volume that actually traveled beyond a threshold; v8 in particular fills published capacity before nearer proxy capacity, so actual long-haul volume can exceed the gap.
- Avoidable distance and cost assume the long-haul volume could be served at 50 km. They ignore greenfield capital, feedstock availability, landbase, facility scale, permitting, and product or residue constraints, and are not additive across classes without capacity reconciliation.
- This is a model-estimate screening artifact. It is not a national statistic, national average, policy recommendation, official OSeCAN result, or UI product.

## 9. Reproduce

`.venv/bin/python -m workflows.national.facilities.transport_capacity_gap_v1`
