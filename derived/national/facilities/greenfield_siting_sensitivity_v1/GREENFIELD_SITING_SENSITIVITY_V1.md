# Transport-Only Greenfield Siting Sensitivity V1

Status: **transport_only_siting_screen** — `not_investment_advice`.
Evidence label: `model_estimate`; `observed=false`; `policy_grade=false`.

This is a transport-cost screening exercise. It is not investment advice,
not a capital or permitting estimate, and not a landbase or facility-design
claim. No national, policy, UI or official OSeCAN surface is changed.

## 1. Setup

- **Demand:** 525 committed RSYC supply nodes; 486 positive-volume nodes;
  118.977 Mm3/yr.
- **Existing facilities:** capacity v3 with the documented 1.2x provincial
  floor, held fixed; 591 eligible
  facilities, 273.468 Mm3/yr of capacity.
- **Greenfield candidates:** positive-volume supply nodes in provinces with
  a published road factor. The generic module is class-agnostic and has
  unlimited throughput in the screen; no class capacity, technology, cost,
  product or residue is asserted.
- **Candidate count:** 421 nodes.
  NT positive nodes are not module hosts because no NT road factor is
  published; they remain demand nodes and are 0.031% of volume.
- **Objective:** minimise 2026 CAD truck transport cost from the committed
  transport cost v1 base curve (52.5 m3 payload, empty return). No
  local-preference penalty is applied in the k-series.
- **Distances:** haversine x province road factor from
  `facility_road_distance_audit_v2`; no full OSRM routing.
- **Method:** greedy forward k-median/facility-location screening. At each
  k the shortlist is the top 10 candidates by capacity-relaxed distance
  savings, and every trial and every k is re-evaluated with the exact
  capacitated transport LP (HiGHS). This is not a proven global optimum.

The committed v10 existing-only baseline keeps its 500 km cross-border
preference penalty. The k=0 row is a transport-only re-solve with the same
capacity and the same transport curve but no preference penalty, so its
cost is not directly identical to v10. The independent v10 reproduction
check passes (cost delta -0.000010 CAD).

## 2. k tradeoff

| k | modules | cost (B CAD) | CAD/m3 | mean km | median km | p90 km | >=150 km | >=300 km | module share | existing util |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 3.220 B | 27.07 | 255.8 | 144.7 | 628.7 | 48.4% | 27.7% | 0.0% | 43.5% |
| 1 | 1 | 2.994 B | 25.16 | 236.8 | 144.4 | 603.0 | 47.9% | 27.0% | 3.2% | 42.1% |
| 2 | 2 | 2.790 B | 23.45 | 219.7 | 130.9 | 577.5 | 42.9% | 22.6% | 8.3% | 39.9% |
| 3 | 3 | 2.589 B | 21.76 | 202.7 | 125.6 | 491.2 | 41.9% | 19.7% | 12.9% | 37.9% |
| 4 | 4 | 2.436 B | 20.47 | 189.8 | 124.6 | 437.4 | 41.3% | 17.2% | 16.3% | 36.4% |
| 5 | 5 | 2.339 B | 19.66 | 181.6 | 124.6 | 410.5 | 41.1% | 17.0% | 17.3% | 36.0% |
| 6 | 6 | 2.258 B | 18.98 | 174.9 | 124.3 | 386.4 | 41.0% | 16.2% | 18.9% | 35.3% |
| 7 | 7 | 2.183 B | 18.35 | 168.6 | 123.5 | 367.4 | 39.5% | 14.1% | 19.8% | 34.9% |
| 8 | 8 | 2.130 B | 17.90 | 164.0 | 123.3 | 351.2 | 39.3% | 13.2% | 21.2% | 34.3% |
| 9 | 9 | 2.077 B | 17.46 | 159.6 | 123.2 | 322.3 | 38.8% | 12.8% | 22.1% | 33.9% |
| 10 | 10 | 2.035 B | 17.10 | 156.1 | 121.6 | 319.0 | 38.1% | 12.1% | 22.7% | 33.6% |
| 11 | 11 | 2.000 B | 16.81 | 153.1 | 120.6 | 310.8 | 37.9% | 11.3% | 23.5% | 33.3% |
| 12 | 12 | 1.964 B | 16.51 | 150.1 | 117.6 | 310.8 | 36.7% | 11.3% | 26.0% | 32.2% |
| 13 | 13 | 1.935 B | 16.26 | 147.7 | 115.9 | 301.9 | 36.3% | 10.4% | 26.1% | 32.2% |
| 14 | 14 | 1.907 B | 16.03 | 145.3 | 115.5 | 301.7 | 35.7% | 10.1% | 26.1% | 32.2% |
| 15 | 15 | 1.879 B | 15.79 | 142.9 | 113.3 | 301.7 | 34.7% | 10.1% | 27.2% | 31.7% |
| 16 | 16 | 1.852 B | 15.57 | 140.7 | 112.3 | 288.0 | 34.5% | 9.2% | 27.7% | 31.5% |
| 17 | 17 | 1.826 B | 15.35 | 138.5 | 102.3 | 284.3 | 33.6% | 9.2% | 28.6% | 31.1% |
| 18 | 18 | 1.800 B | 15.13 | 136.3 | 102.0 | 284.3 | 32.8% | 9.1% | 28.6% | 31.1% |
| 19 | 19 | 1.774 B | 14.91 | 134.1 | 99.5 | 283.9 | 32.4% | 8.7% | 28.6% | 31.1% |
| 20 | 20 | 1.749 B | 14.70 | 132.0 | 98.1 | 283.9 | 32.1% | 8.7% | 30.3% | 30.3% |

## 3. Module locations

The selected sets are nested prefixes: the module selected at k is
retained at every larger k. The table shows the k=20 locations.

| module | province | first k | k=20 served (Mm3) | share of assigned | nodes served | mean km |
|---|---|---:|---:|---:|---:|---:|
| GFM\|J27\|NL | NL | 1 | 1.810 | 1.52% | 30 | 459.6 |
| GFM\|K9\|AB | AB | 2 | 2.951 | 2.48% | 4 | 113.9 |
| GFM\|M4\|BC | BC | 3 | 2.122 | 1.78% | 4 | 174.0 |
| GFM\|F18\|ON | ON | 4 | 2.740 | 2.30% | 28 | 259.4 |
| GFM\|H25\|QC | QC | 5 | 1.627 | 1.37% | 9 | 395.2 |
| GFM\|I31\|NL | NL | 6 | 2.260 | 1.90% | 22 | 343.4 |
| GFM\|L6\|BC | BC | 7 | 1.370 | 1.15% | 2 | 54.4 |
| GFM\|I12\|SK | SK | 8 | 1.861 | 1.56% | 24 | 264.5 |
| GFM\|G28\|QC | QC | 9 | 0.955 | 0.80% | 2 | 129.4 |
| GFM\|K1\|BC | BC | 10 | 0.822 | 0.69% | 3 | 33.9 |
| GFM\|F23\|ON | ON | 11 | 1.367 | 1.15% | 17 | 286.1 |
| GFM\|H2\|BC | BC | 12 | 2.995 | 2.52% | 4 | 101.7 |
| GFM\|N3\|BC | BC | 13 | 1.828 | 1.54% | 12 | 159.5 |
| GFM\|K10\|AB | AB | 14 | 2.252 | 1.89% | 33 | 147.0 |
| GFM\|K7\|AB | AB | 15 | 1.473 | 1.24% | 3 | 46.6 |
| GFM\|E20\|ON | ON | 16 | 1.658 | 1.39% | 8 | 198.0 |
| GFM\|C25\|QC | QC | 17 | 1.053 | 0.89% | 1 | 0.0 |
| GFM\|M6\|BC | BC | 18 | 1.812 | 1.52% | 29 | 106.0 |
| GFM\|G27\|QC | QC | 19 | 1.030 | 0.87% | 3 | 200.3 |
| GFM\|E30\|NB | NB | 20 | 2.021 | 1.70% | 1 | 0.0 |

## 4. Capacity served and comparison with v10

| Metric | v10 existing-only | k=0 transport-only | k=20 |
|---|---:|---:|---:|
| transport cost (B CAD/yr) | 3.392 B | 3.220 B | 1.749 B |
| transport cost (CAD/m3) | 28.51 | 27.07 | 14.70 |
| mean road distance (km) | 270.3 | 255.8 | 132.0 |
| median road distance (km) | 147.2 | 144.7 | 98.1 |
| p90 road distance (km) | 635.7 | 628.7 | 283.9 |
| share >=150 km | 48.62% | 48.41% | 32.13% |
| share >=300 km | 30.16% | 27.69% | 8.69% |
| cross-border share | 1.95% | 9.86% | 5.89% |
| existing facilities used | 296 | 295 | 252 |
| modules serving | 0 | 0 | 20 |
| existing capacity served (Mm3) | 118.977 | 118.977 | 82.971 |
| module volume served (Mm3) | 0.000 | 0.000 | 36.006 |
| existing capacity utilization | 43.51% | 43.51% | 30.34% |

The k=20 screen reduces transport cost by
**1.471 B CAD/yr**
(45.70%) versus the
transport-only existing-only baseline, and by
**1.643 B CAD/yr**
(48.45%) versus
committed v10. The mean road distance falls from
255.8 km at k=0 to
132.0 km at k=20.

## 5. Diminishing returns and screening diagnostics

- First k with marginal cost reduction below 1% of the k=0 cost: **13**.
- k=20 module volume share: **30.26%**.
- k=20 existing capacity utilization: **30.34%**.
- k=20 capacity-relaxed lower-bound gap: **9.69%**.
  The bound ignores existing capacity and is not an optimality gap.
- The selected sets are greedy prefixes, not a global optimum; no
  optimality-gap claim is made.

## 6. Labels and caveats

- `transport_only_siting_screen`; `not_investment_advice`;
  `model_estimate`; `observed=false`; `policy_grade=false`.
- No capital, operating, permitting, landbase, procurement or
  facility-design claim is made.
- The generic module is a class-agnostic transport sink with unlimited
  throughput in the screen. No class-specific capacity is invented.
- Distances are haversine x province-factor screening distances, not
  observed routes for every node-module pair.
- Transport cost excludes feedstock, processing, conversion, handling,
  storage and product revenue.
- The k-series has no local-preference penalty. Cross-border flows are
  therefore unpenalised and are reported, not restricted.
- Existing capacity v3 and the 1.2x provincial floor are unchanged.
- NT positive nodes are not candidate module hosts because no NT road
  factor is published; their 0.031% of volume remains in the demand set.
- No national claim, policy claim, UI change or official OSeCAN change
  is made.

## 7. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.greenfield_siting_sensitivity_v1
```

