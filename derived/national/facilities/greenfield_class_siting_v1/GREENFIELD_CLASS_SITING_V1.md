# Class-Specific Transport-Only Greenfield Siting V1

Status: **transport_only_siting_screen** — `not_investment_advice`.
Evidence label: `model_estimate`; `observed=false`; `policy_grade=false`.

This is a transport-cost screening exercise. It is not investment advice,
not a capital, permitting, technology or landbase estimate, and not a
facility-design or class-capacity claim. No national, policy, UI or
official OSeCAN surface is changed.

## 1. Setup

- **Demand:** 525 committed RSYC supply nodes; 486 positive-volume nodes;
  118.977 Mm3/yr split into SAW, PULP, PANEL,
  PELLET and BIO feedstock.
- **Class split:** v5.1 E1/E2c province/class feedstock shares, normalised
  within each province and applied to node harvest. The split conserves
  node harvest and each province/class total.
- **Existing facilities:** capacity v3 with the documented 1.2x provincial
  floor, partitioned by class and held fixed; 591
  eligible facilities and 273.468 Mm3/yr
  of capacity.
- **Greenfield candidates:** positive class feedstock nodes in provinces
  with a published road factor. The class module is unlimited-throughput
  in the screen; no class capacity, technology, cost, product or residue
  is asserted.
- **Candidate modules:** 2047 across the five classes.
  NT positive nodes are demand nodes but not module hosts because no NT
  road factor is published.
- **Objective:** minimise 2026 CAD truck transport cost from transport
  cost v1 (52.5 m3 payload, empty return). No local-preference penalty.
- **Distances:** haversine x destination province road factor from
  `facility_road_distance_audit_v2`; no full OSRM routing.
- **Method:** greedy forward k-median/facility-location screening with
  exact capacitated transport-LP re-evaluation (HiGHS). At each k the
  shortlist is the top 10 candidates by
  capacity-relaxed distance savings. This is not a proven global optimum.

## 2. Class feedstock split

| class | demand (Mm3) | share of harvest | candidates | existing facilities | existing capacity (Mm3) |
|---|---:|---:|---:|---:|---:|
| SAW | 45.617 | 38.34% | 392 | 405 | 133.815 |
| PULP | 52.680 | 44.28% | 421 | 55 | 88.205 |
| PANEL | 7.467 | 6.28% | 392 | 32 | 12.865 |
| PELLET | 10.925 | 9.18% | 421 | 54 | 12.390 |
| BIO | 2.287 | 1.92% | 421 | 45 | 26.193 |

The class split is a proportional screening allocation of node
harvest. It is not a mass-balance routing of harvest residue, and it
does not assert that the v5.1 absolute class feedstock totals are
physically available at every node.

### Province/class shares

| province | SAW | PULP | PANEL | PELLET | BIO |
|---|---:|---:|---:|---:|---:|
| BC | 55.56% | 27.41% | 9.09% | 6.57% | 1.37% |
| AB | 34.11% | 56.92% | 5.58% | 2.79% | 0.58% |
| SK | 0.00% | 38.60% | 0.00% | 50.77% | 10.63% |
| MB | 29.12% | 50.00% | 4.77% | 13.32% | 2.79% |
| ON | 33.54% | 43.74% | 5.49% | 14.25% | 2.98% |
| QC | 26.49% | 57.83% | 4.34% | 9.39% | 1.96% |
| NB | 42.53% | 44.15% | 6.96% | 5.26% | 1.10% |
| NS | 15.21% | 62.94% | 2.49% | 16.00% | 3.35% |
| PE | 19.57% | 65.23% | 3.20% | 9.92% | 2.08% |
| NL | 39.31% | 43.68% | 6.44% | 8.74% | 1.83% |
| YT | 29.80% | 45.94% | 4.88% | 16.03% | 3.36% |
| NT | 47.34% | 31.68% | 7.75% | 10.95% | 2.29% |
| NU | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% |

## 3. Class-specific k tradeoff

| class | k | cost (B CAD) | CAD/m3 | mean km | >=150 km | >=300 km | module share | existing util |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SAW | 0 | 1.201 B | 26.34 | 248.5 | 45.7% | 25.7% | 0.0% | 34.1% |
| SAW | 1 | 1.084 B | 23.77 | 222.8 | 44.5% | 22.7% | 4.8% | 32.5% |
| SAW | 2 | 0.977 B | 21.43 | 199.4 | 43.0% | 19.0% | 12.5% | 29.8% |
| SAW | 3 | 0.926 B | 20.29 | 188.0 | 42.9% | 18.5% | 14.6% | 29.1% |
| SAW | 4 | 0.878 B | 19.24 | 177.5 | 39.9% | 15.6% | 18.5% | 27.8% |
| SAW | 5 | 0.849 B | 18.60 | 171.1 | 39.2% | 13.4% | 19.0% | 27.6% |
| PULP | 0 | 2.573 B | 48.85 | 473.9 | 83.1% | 62.0% | 0.0% | 59.7% |
| PULP | 1 | 2.236 B | 42.44 | 409.8 | 82.5% | 58.6% | 9.9% | 53.8% |
| PULP | 2 | 1.941 B | 36.84 | 353.7 | 80.1% | 43.8% | 21.6% | 46.8% |
| PULP | 3 | 1.832 B | 34.78 | 333.0 | 80.0% | 43.0% | 24.8% | 44.9% |
| PULP | 4 | 1.729 B | 32.81 | 313.4 | 79.7% | 41.5% | 26.4% | 43.9% |
| PULP | 5 | 1.659 B | 31.50 | 300.2 | 79.3% | 40.0% | 30.0% | 41.8% |
| PANEL | 0 | 0.394 B | 52.82 | 513.7 | 79.6% | 56.5% | 0.0% | 58.0% |
| PANEL | 1 | 0.333 B | 44.62 | 431.6 | 79.4% | 54.6% | 9.0% | 52.8% |
| PANEL | 2 | 0.290 B | 38.78 | 373.1 | 77.9% | 48.8% | 20.7% | 46.0% |
| PANEL | 3 | 0.251 B | 33.64 | 321.7 | 77.1% | 43.1% | 32.4% | 39.3% |
| PANEL | 4 | 0.240 B | 32.12 | 306.5 | 76.3% | 37.7% | 37.0% | 36.6% |
| PANEL | 5 | 0.232 B | 31.00 | 295.2 | 75.1% | 34.4% | 40.3% | 34.7% |
| PELLET | 0 | 0.915 B | 83.76 | 823.5 | 89.9% | 75.4% | 0.0% | 88.2% |
| PELLET | 1 | 0.576 B | 52.70 | 512.5 | 84.1% | 62.4% | 25.6% | 65.6% |
| PELLET | 2 | 0.457 B | 41.82 | 403.6 | 82.6% | 55.0% | 36.0% | 56.4% |
| PELLET | 3 | 0.426 B | 39.02 | 375.5 | 82.1% | 51.3% | 36.0% | 56.4% |
| PELLET | 4 | 0.398 B | 36.42 | 349.5 | 78.9% | 48.1% | 43.6% | 49.7% |
| PELLET | 5 | 0.372 B | 34.07 | 326.0 | 77.0% | 40.9% | 46.4% | 47.2% |
| BIO | 0 | 0.097 B | 42.40 | 409.4 | 77.6% | 57.2% | 0.0% | 8.7% |
| BIO | 1 | 0.081 B | 35.30 | 338.3 | 76.0% | 47.7% | 18.1% | 7.2% |
| BIO | 2 | 0.076 B | 33.38 | 319.1 | 75.8% | 47.5% | 21.0% | 6.9% |
| BIO | 3 | 0.073 B | 31.93 | 304.5 | 75.4% | 44.2% | 25.3% | 6.5% |
| BIO | 4 | 0.070 B | 30.52 | 290.4 | 74.7% | 41.9% | 26.3% | 6.4% |
| BIO | 5 | 0.067 B | 29.44 | 279.6 | 73.2% | 39.7% | 26.3% | 6.4% |

## 4. Aggregate k tradeoff and generic comparison

| k/class | modules | cost (B CAD) | CAD/m3 | mean km | >=150 km | >=300 km | module share | generic same-k (B) | generic matched k | generic matched (B) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 5.181 B | 43.55 | 420.9 | 69.0% | 48.9% | 0.0% | 3.220 B | 0 | 3.220 B |
| 1 | 5 | 4.310 B | 36.22 | 347.5 | 67.7% | 44.7% | 9.5% | 2.994 B | 5 | 2.339 B |
| 2 | 10 | 3.741 B | 31.44 | 299.7 | 65.9% | 35.7% | 19.4% | 2.790 B | 10 | 2.035 B |
| 3 | 15 | 3.508 B | 29.49 | 280.1 | 65.7% | 34.4% | 22.4% | 2.589 B | 15 | 1.879 B |
| 4 | 20 | 3.314 B | 27.85 | 263.7 | 64.0% | 32.0% | 25.6% | 2.436 B | 20 | 1.749 B |
| 5 | 25 | 3.179 B | 26.72 | 252.4 | 63.3% | 29.5% | 27.9% | 2.339 B | 20 | 1.749 B |

The aggregate has five classes, so k per class means 5k total modules.
The same-k generic column has only k shared class-agnostic modules and
is not module-count matched. The matched column uses the generic k
nearest to 5k; the k=4 row is the exact 20-module match. The k=5
aggregate has 25 class modules, above the generic k=20 maximum.

## 5. Module locations at k=5

| class | module | province | first k | served (Mm3) | share of class demand | nodes | mean km |
|---|---|---|---:|---:|---:|---:|---:|
| SAW | GFC\|SAW\|E18\|ON | ON | 1 | 2.163 | 4.74% | 43 | 340.3 |
| SAW | GFC\|SAW\|M5\|BC | BC | 2 | 2.709 | 5.94% | 31 | 248.9 |
| SAW | GFC\|SAW\|J27\|NL | NL | 3 | 0.957 | 2.10% | 44 | 624.7 |
| SAW | GFC\|SAW\|K9\|AB | AB | 4 | 1.807 | 3.96% | 44 | 191.5 |
| SAW | GFC\|SAW\|N3\|BC | BC | 5 | 1.013 | 2.22% | 11 | 158.8 |
| PULP | GFC\|PULP\|F23\|ON | ON | 1 | 3.694 | 7.01% | 50 | 516.6 |
| PULP | GFC\|PULP\|K9\|AB | AB | 2 | 5.448 | 10.34% | 64 | 241.5 |
| PULP | GFC\|PULP\|I28\|NL | NL | 3 | 2.768 | 5.25% | 48 | 625.7 |
| PULP | GFC\|PULP\|H12\|SK | SK | 4 | 1.996 | 3.79% | 55 | 405.3 |
| PULP | GFC\|PULP\|M4\|BC | BC | 5 | 1.923 | 3.65% | 81 | 333.8 |
| PANEL | GFC\|PANEL\|E20\|ON | ON | 1 | 0.586 | 7.84% | 81 | 536.4 |
| PANEL | GFC\|PANEL\|F31\|PE | PE | 2 | 0.959 | 12.85% | 111 | 486.5 |
| PANEL | GFC\|PANEL\|L3\|BC | BC | 3 | 0.645 | 8.63% | 26 | 324.2 |
| PANEL | GFC\|PANEL\|I2\|BC | BC | 4 | 0.491 | 6.57% | 9 | 204.9 |
| PANEL | GFC\|PANEL\|M6\|BC | BC | 5 | 0.329 | 4.40% | 67 | 196.2 |
| PELLET | GFC\|PELLET\|H13\|SK | SK | 1 | 1.393 | 12.75% | 46 | 324.1 |
| PELLET | GFC\|PELLET\|D22\|ON | ON | 2 | 1.229 | 11.25% | 43 | 449.4 |
| PELLET | GFC\|PELLET\|E18\|ON | ON | 3 | 0.624 | 5.72% | 32 | 303.2 |
| PELLET | GFC\|PELLET\|F31\|PE | PE | 4 | 0.903 | 8.26% | 91 | 598.4 |
| PELLET | GFC\|PELLET\|H11\|SK | SK | 5 | 0.924 | 8.45% | 16 | 220.2 |
| BIO | GFC\|BIO\|H12\|SK | SK | 1 | 0.249 | 10.89% | 14 | 215.7 |
| BIO | GFC\|BIO\|J27\|NL | NL | 2 | 0.067 | 2.93% | 46 | 628.6 |
| BIO | GFC\|BIO\|F18\|ON | ON | 3 | 0.102 | 4.47% | 33 | 280.9 |
| BIO | GFC\|BIO\|K12\|SK | SK | 4 | 0.093 | 4.05% | 55 | 234.8 |
| BIO | GFC\|BIO\|F13\|SK | SK | 5 | 0.091 | 4.00% | 17 | 159.5 |

## 6. Generic comparison detail

| basis | k/class | class modules | generic k | class (B CAD) | generic (B CAD) | delta | class mean km | generic mean km | delta mean km |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| same_k_per_class | 0 | 0 | 0 | 5.181 B | 3.220 B | 60.90% | 420.9 | 255.8 | 165.0 |
| same_k_per_class | 1 | 5 | 1 | 4.310 B | 2.994 B | 43.95% | 347.5 | 236.8 | 110.8 |
| module_count_matched | 1 | 5 | 5 | 4.310 B | 2.339 B | 84.28% | 347.5 | 181.6 | 165.9 |
| same_k_per_class | 2 | 10 | 2 | 3.741 B | 2.790 B | 34.06% | 299.7 | 219.7 | 80.0 |
| module_count_matched | 2 | 10 | 10 | 3.741 B | 2.035 B | 83.83% | 299.7 | 156.1 | 143.6 |
| same_k_per_class | 3 | 15 | 3 | 3.508 B | 2.589 B | 35.51% | 280.1 | 202.7 | 77.4 |
| module_count_matched | 3 | 15 | 15 | 3.508 B | 1.879 B | 86.71% | 280.1 | 142.9 | 137.1 |
| same_k_per_class | 4 | 20 | 4 | 3.314 B | 2.436 B | 36.04% | 263.7 | 189.8 | 73.9 |
| module_count_matched | 4 | 20 | 20 | 3.314 B | 1.749 B | 89.51% | 263.7 | 132.0 | 131.7 |
| same_k_per_class | 5 | 25 | 5 | 3.179 B | 2.339 B | 35.92% | 252.4 | 181.6 | 70.7 |
| module_count_matched | 5 | 25 | 20 | 3.179 B | 1.749 B | 81.79% | 252.4 | 132.0 | 120.4 |

## 7. Findings

- The class-specific existing-only cost is
**5.181 B CAD/yr** at
420.9 km mean distance.
  This is
60.90% above
  the class-agnostic generic k=0 cost of
3.220 B CAD/yr.
- At k=5 per class (25 modules), the aggregate transport cost is
**3.179 B CAD/yr**
(252.4 km mean;
27.87% module share).
- The aggregate k=5 screen reduces transport cost by
**2.002 B CAD/yr**
(38.64%)
versus class-specific k=0.
- No class or aggregate marginal reduction from k=1 to k=5 falls
  below 1% of its k=0 cost; the diminishing-returns cutoff is not
  reached inside the tested range.
- At the exact 20-module count match (class k=4 versus generic k=20),
the class-specific cost is 3.314 B
CAD/yr at 263.7 km
versus 1.749 B CAD/yr
at 132.0 km generic
(+89.51%;
mean distance +131.7 km).
- Class costs at k=5 differ widely because the existing class facility
  geography and capacity differ; the class split is not a single
  national facility pool.
- The k-series is a greedy prefix, not a globally optimal siting set;
  no optimality-gap claim is made.

## 8. Labels and caveats

- `transport_only_siting_screen`; `not_investment_advice`;
  `model_estimate`; `observed=false`; `policy_grade=false`.
- No capital, operating, permitting, technology, landbase, procurement,
  class-capacity or facility-design claim is made.
- The v5.1 class split is a proportional screening allocation of node
  harvest, not a facility-level mass balance.
- Existing facilities are capacity v3 records partitioned by class; the
  published/proxy capacity mix is unchanged.
- The class module is a class-specific transport sink with unlimited
  throughput in the screen. No class capacity is invented.
- Distances are haversine x province-factor screening distances, not
  observed routes for every pair; no full OSRM routing.
- Transport cost excludes feedstock, processing, conversion, handling,
  storage and product revenue.
- No local-preference penalty is applied; cross-border flows are
  reported, not restricted.
- No national claim, policy claim, UI change or official OSeCAN change
  is made.

## 9. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.greenfield_class_siting_v1
```
