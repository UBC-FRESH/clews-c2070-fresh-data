# Transport-Only Greenfield Siting Sensitivity V1: 100/119/150 Mm3

Status: **transport_only_siting_screen** — `not_investment_advice`.
Evidence label: `model_estimate`; `observed=false`; `policy_grade=false`.

This is a transport-cost screening exercise. It is not investment advice,
not a capital or permitting estimate, and not a landbase or facility-design
claim. No national, policy, UI or official OSeCAN surface is changed.

## 1. Setup

- **Demand cases:** 100.000, 118.977 and 150.000 Mm3/yr. The 100 and
  150 Mm3 node vectors use the documented provincial allocations and
  the same within-province scaling as the committed v10 case extension.
- **Existing facilities:** capacity v3 with the documented 1.2x provincial
  floor, held fixed; 591 eligible
  facilities, 273.468
  Mm3/yr of capacity.
- **Greenfield candidates:** positive-volume supply nodes in provinces with
  a published road factor. The generic module is class-agnostic and has
  unlimited throughput in the screen; no class capacity, technology, cost,
  product or residue is asserted.
- **Candidate count:** 421 nodes.
  NT positive nodes are not module hosts because no NT road factor is
  published; they remain demand nodes.
- **Objective:** minimise 2026 CAD truck transport cost from the committed
  transport cost v1 base curve (52.5 m3 payload, empty return). No
  local-preference penalty is applied in the k-series.
- **Distances:** haversine x province road factor from
  `facility_road_distance_audit_v2`; no full OSRM routing.
- **Method:** greedy forward k-median/facility-location screening. At each
  k the shortlist is the top 10 candidates by capacity-relaxed distance
  savings, and every trial and every k is re-evaluated with the exact
  capacitated transport LP (HiGHS). This is not a proven global optimum.
- **119 Mm3 source:** the committed v1 siting artifact is loaded unchanged.

## 2. k tradeoff by case

| case | k | cost (B CAD) | CAD/m3 | mean km | median km | p90 km | >=150 km | >=300 km | module share | existing util |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100m | 0 | 2.572 B | 25.72 | 242.3 | 137.2 | 603.0 | 44.8% | 25.3% | 0.0% | 36.6% |
| 100m | 1 | 2.391 B | 23.91 | 224.2 | 137.1 | 555.2 | 44.2% | 24.7% | 2.9% | 35.5% |
| 100m | 2 | 2.233 B | 22.33 | 208.4 | 130.0 | 494.8 | 43.2% | 22.1% | 7.4% | 33.9% |
| 100m | 3 | 2.094 B | 20.94 | 194.5 | 123.3 | 451.0 | 39.4% | 19.0% | 11.9% | 32.2% |
| 100m | 4 | 1.978 B | 19.78 | 182.9 | 123.2 | 431.4 | 39.1% | 16.6% | 15.0% | 31.1% |
| 100m | 5 | 1.900 B | 19.00 | 175.0 | 123.2 | 401.1 | 39.0% | 16.2% | 16.2% | 30.7% |
| 100m | 6 | 1.835 B | 18.35 | 168.5 | 123.2 | 373.9 | 38.9% | 15.4% | 17.7% | 30.1% |
| 100m | 7 | 1.779 B | 17.79 | 163.0 | 121.6 | 367.0 | 38.1% | 13.3% | 18.8% | 29.7% |
| 100m | 8 | 1.737 B | 17.37 | 158.7 | 121.6 | 335.0 | 37.9% | 12.5% | 19.8% | 29.3% |
| 100m | 9 | 1.695 B | 16.95 | 154.6 | 118.5 | 319.0 | 37.4% | 11.9% | 21.0% | 28.9% |
| 100m | 10 | 1.662 B | 16.62 | 151.2 | 117.6 | 305.1 | 36.6% | 10.9% | 21.3% | 28.8% |
| 100m | 11 | 1.634 B | 16.34 | 148.4 | 115.5 | 305.1 | 35.5% | 10.9% | 23.7% | 27.9% |
| 100m | 12 | 1.608 B | 16.08 | 145.8 | 115.5 | 291.9 | 35.3% | 9.8% | 24.3% | 27.7% |
| 100m | 13 | 1.583 B | 15.83 | 143.3 | 105.7 | 291.9 | 35.0% | 9.8% | 26.3% | 26.9% |
| 100m | 14 | 1.557 B | 15.57 | 140.7 | 102.0 | 290.9 | 34.3% | 9.5% | 26.3% | 26.9% |
| 100m | 15 | 1.533 B | 15.33 | 138.3 | 99.5 | 283.7 | 33.9% | 8.7% | 26.5% | 26.9% |
| 100m | 16 | 1.510 B | 15.10 | 136.0 | 99.5 | 283.7 | 32.9% | 8.7% | 27.5% | 26.5% |
| 100m | 17 | 1.489 B | 14.89 | 133.9 | 98.6 | 281.3 | 32.6% | 8.3% | 27.5% | 26.5% |
| 100m | 18 | 1.468 B | 14.68 | 131.8 | 98.1 | 281.3 | 31.6% | 8.3% | 28.3% | 26.2% |
| 100m | 19 | 1.448 B | 14.48 | 129.8 | 96.0 | 281.3 | 31.4% | 8.3% | 30.3% | 25.5% |
| 100m | 20 | 1.428 B | 14.28 | 127.7 | 95.9 | 281.3 | 31.3% | 8.1% | 30.3% | 25.5% |
| 119m | 0 | 3.220 B | 27.07 | 255.8 | 144.7 | 628.7 | 48.4% | 27.7% | 0.0% | 43.5% |
| 119m | 1 | 2.994 B | 25.16 | 236.8 | 144.4 | 603.0 | 47.9% | 27.0% | 3.2% | 42.1% |
| 119m | 2 | 2.790 B | 23.45 | 219.7 | 130.9 | 577.5 | 42.9% | 22.6% | 8.3% | 39.9% |
| 119m | 3 | 2.589 B | 21.76 | 202.7 | 125.6 | 491.2 | 41.9% | 19.7% | 12.9% | 37.9% |
| 119m | 4 | 2.436 B | 20.47 | 189.8 | 124.6 | 437.4 | 41.3% | 17.2% | 16.3% | 36.4% |
| 119m | 5 | 2.339 B | 19.66 | 181.6 | 124.6 | 410.5 | 41.1% | 17.0% | 17.3% | 36.0% |
| 119m | 6 | 2.258 B | 18.98 | 174.9 | 124.3 | 386.4 | 41.0% | 16.2% | 18.9% | 35.3% |
| 119m | 7 | 2.183 B | 18.35 | 168.6 | 123.5 | 367.4 | 39.5% | 14.1% | 19.8% | 34.9% |
| 119m | 8 | 2.130 B | 17.90 | 164.0 | 123.3 | 351.2 | 39.3% | 13.2% | 21.2% | 34.3% |
| 119m | 9 | 2.077 B | 17.46 | 159.6 | 123.2 | 322.3 | 38.8% | 12.8% | 22.1% | 33.9% |
| 119m | 10 | 2.035 B | 17.10 | 156.1 | 121.6 | 319.0 | 38.1% | 12.1% | 22.7% | 33.6% |
| 119m | 11 | 2.000 B | 16.81 | 153.1 | 120.6 | 310.8 | 37.9% | 11.3% | 23.5% | 33.3% |
| 119m | 12 | 1.964 B | 16.51 | 150.1 | 117.6 | 310.8 | 36.7% | 11.3% | 26.0% | 32.2% |
| 119m | 13 | 1.935 B | 16.26 | 147.7 | 115.9 | 301.9 | 36.3% | 10.4% | 26.1% | 32.2% |
| 119m | 14 | 1.907 B | 16.03 | 145.3 | 115.5 | 301.7 | 35.7% | 10.1% | 26.1% | 32.2% |
| 119m | 15 | 1.879 B | 15.79 | 142.9 | 113.3 | 301.7 | 34.7% | 10.1% | 27.2% | 31.7% |
| 119m | 16 | 1.852 B | 15.57 | 140.7 | 112.3 | 288.0 | 34.5% | 9.2% | 27.7% | 31.5% |
| 119m | 17 | 1.826 B | 15.35 | 138.5 | 102.3 | 284.3 | 33.6% | 9.2% | 28.6% | 31.1% |
| 119m | 18 | 1.800 B | 15.13 | 136.3 | 102.0 | 284.3 | 32.8% | 9.1% | 28.6% | 31.1% |
| 119m | 19 | 1.774 B | 14.91 | 134.1 | 99.5 | 283.9 | 32.4% | 8.7% | 28.6% | 31.1% |
| 119m | 20 | 1.749 B | 14.70 | 132.0 | 98.1 | 283.9 | 32.1% | 8.7% | 30.3% | 30.3% |
| 150m | 0 | 4.728 B | 31.52 | 300.4 | 172.0 | 691.3 | 55.6% | 34.7% | 0.0% | 54.9% |
| 150m | 1 | 4.197 B | 27.98 | 265.0 | 156.9 | 633.6 | 53.4% | 28.7% | 4.8% | 52.2% |
| 150m | 2 | 3.828 B | 25.52 | 240.4 | 144.7 | 568.1 | 48.3% | 23.3% | 11.0% | 48.8% |
| 150m | 3 | 3.543 B | 23.62 | 221.3 | 144.7 | 555.2 | 48.0% | 22.9% | 13.8% | 47.3% |
| 150m | 4 | 3.303 B | 22.02 | 205.3 | 138.7 | 459.5 | 47.1% | 20.2% | 18.0% | 45.0% |
| 150m | 5 | 3.184 B | 21.23 | 197.4 | 138.7 | 450.3 | 46.9% | 20.0% | 18.8% | 44.5% |
| 150m | 6 | 3.073 B | 20.49 | 190.0 | 137.2 | 427.6 | 46.6% | 19.2% | 20.5% | 43.6% |
| 150m | 7 | 2.975 B | 19.84 | 183.4 | 137.1 | 401.1 | 46.0% | 17.8% | 21.8% | 42.9% |
| 150m | 8 | 2.881 B | 19.21 | 177.1 | 130.3 | 373.9 | 44.2% | 15.8% | 22.8% | 42.4% |
| 150m | 9 | 2.798 B | 18.65 | 171.6 | 129.5 | 365.3 | 43.6% | 14.3% | 25.2% | 41.0% |
| 150m | 10 | 2.723 B | 18.15 | 166.6 | 128.8 | 352.1 | 42.9% | 13.5% | 26.3% | 40.4% |
| 150m | 11 | 2.650 B | 17.67 | 161.7 | 128.8 | 319.0 | 42.3% | 12.1% | 27.2% | 39.9% |
| 150m | 12 | 2.601 B | 17.34 | 158.4 | 124.6 | 311.9 | 41.7% | 11.5% | 27.8% | 39.6% |
| 150m | 13 | 2.559 B | 17.06 | 155.6 | 124.3 | 311.9 | 40.7% | 11.5% | 30.2% | 38.3% |
| 150m | 14 | 2.519 B | 16.79 | 152.9 | 123.3 | 305.1 | 39.9% | 11.1% | 30.4% | 38.2% |
| 150m | 15 | 2.481 B | 16.54 | 150.4 | 121.6 | 305.1 | 39.3% | 10.7% | 30.4% | 38.2% |
| 150m | 16 | 2.444 B | 16.29 | 148.0 | 117.8 | 305.1 | 39.1% | 10.7% | 32.9% | 36.8% |
| 150m | 17 | 2.408 B | 16.05 | 145.5 | 115.9 | 305.1 | 38.1% | 10.6% | 33.7% | 36.4% |
| 150m | 18 | 2.373 B | 15.82 | 143.2 | 114.4 | 305.1 | 37.1% | 10.6% | 34.6% | 35.8% |
| 150m | 19 | 2.340 B | 15.60 | 141.0 | 112.3 | 292.0 | 36.7% | 9.8% | 34.7% | 35.8% |
| 150m | 20 | 2.307 B | 15.38 | 138.8 | 111.1 | 290.8 | 36.3% | 9.4% | 34.7% | 35.8% |

## 3. Comparison with 119 Mm3

| case | k | cost (B CAD) | mean km | >=150 km | >=300 km | module share | delta cost vs 119 | delta mean vs 119 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 100m | 0 | 2.572 B | 242.3 | 44.8% | 25.3% | 0.0% | -0.648 B | -13.5 km |
| 100m | 5 | 1.900 B | 175.0 | 39.0% | 16.2% | 16.2% | -0.439 B | -6.6 km |
| 100m | 10 | 1.662 B | 151.2 | 36.6% | 10.9% | 21.3% | -0.373 B | -4.9 km |
| 100m | 15 | 1.533 B | 138.3 | 33.9% | 8.7% | 26.5% | -0.346 B | -4.6 km |
| 100m | 20 | 1.428 B | 127.7 | 31.3% | 8.1% | 30.3% | -0.321 B | -4.2 km |
| 119m | 0 | 3.220 B | 255.8 | 48.4% | 27.7% | 0.0% | +0.000 B | +0.0 km |
| 119m | 5 | 2.339 B | 181.6 | 41.1% | 17.0% | 17.3% | +0.000 B | +0.0 km |
| 119m | 10 | 2.035 B | 156.1 | 38.1% | 12.1% | 22.7% | +0.000 B | +0.0 km |
| 119m | 15 | 1.879 B | 142.9 | 34.7% | 10.1% | 27.2% | +0.000 B | +0.0 km |
| 119m | 20 | 1.749 B | 132.0 | 32.1% | 8.7% | 30.3% | +0.000 B | +0.0 km |
| 150m | 0 | 4.728 B | 300.4 | 55.6% | 34.7% | 0.0% | +1.508 B | +44.6 km |
| 150m | 5 | 3.184 B | 197.4 | 46.9% | 20.0% | 18.8% | +0.845 B | +15.7 km |
| 150m | 10 | 2.723 B | 166.6 | 42.9% | 13.5% | 26.3% | +0.688 B | +10.5 km |
| 150m | 15 | 2.481 B | 150.4 | 39.3% | 10.7% | 30.4% | +0.602 B | +7.5 km |
| 150m | 20 | 2.307 B | 138.8 | 36.3% | 9.4% | 34.7% | +0.559 B | +6.8 km |

## 4. k=20 headline

| case | cost (B CAD) | CAD/m3 | mean km | median km | p90 km | >=150 km | >=300 km | module share | modules | existing util |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100m | 1.428 B | 14.28 | 127.7 | 95.9 | 281.3 | 31.3% | 8.1% | 30.3% | 20 | 25.5% |
| 119m | 1.749 B | 14.70 | 132.0 | 98.1 | 283.9 | 32.1% | 8.7% | 30.3% | 20 | 30.3% |
| 150m | 2.307 B | 15.38 | 138.8 | 111.1 | 290.8 | 36.3% | 9.4% | 34.7% | 20 | 35.8% |

## 5. Module locations at k=20

The selected sets are nested prefixes: the module selected at k is
retained at every larger k.

| case | module | province | first k | served (Mm3) | share of assigned | nodes served | mean km |
|---|---|---|---:|---:|---:|---:|---:|
| 100m | GFM\|J27\|NL | NL | 1 | 0.924 | 0.92% | 20 | 346.1 |
| 100m | GFM\|M4\|BC | BC | 2 | 1.229 | 1.23% | 4 | 119.6 |
| 100m | GFM\|K9\|AB | AB | 3 | 2.454 | 2.45% | 4 | 113.9 |
| 100m | GFM\|F18\|ON | ON | 4 | 2.250 | 2.25% | 26 | 253.2 |
| 100m | GFM\|H25\|QC | QC | 5 | 1.572 | 1.57% | 11 | 399.8 |
| 100m | GFM\|I31\|NL | NL | 6 | 1.840 | 1.84% | 22 | 340.8 |
| 100m | GFM\|M6\|BC | BC | 7 | 2.297 | 2.30% | 30 | 146.9 |
| 100m | GFM\|I13\|SK | SK | 8 | 1.196 | 1.20% | 26 | 256.2 |
| 100m | GFM\|G28\|QC | QC | 9 | 0.794 | 0.79% | 2 | 129.4 |
| 100m | GFM\|K1\|BC | BC | 10 | 0.679 | 0.68% | 3 | 33.3 |
| 100m | GFM\|H2\|BC | BC | 11 | 2.393 | 2.39% | 4 | 97.1 |
| 100m | GFM\|E20\|ON | ON | 12 | 1.460 | 1.46% | 12 | 215.6 |
| 100m | GFM\|E30\|NB | NB | 13 | 2.021 | 2.02% | 1 | 0.0 |
| 100m | GFM\|K10\|AB | AB | 14 | 1.873 | 1.87% | 33 | 147.1 |
| 100m | GFM\|N3\|BC | BC | 15 | 1.521 | 1.52% | 12 | 159.5 |
| 100m | GFM\|K7\|AB | AB | 16 | 1.355 | 1.36% | 4 | 68.9 |
| 100m | GFM\|G27\|QC | QC | 17 | 0.857 | 0.86% | 3 | 200.3 |
| 100m | GFM\|C25\|QC | QC | 18 | 0.876 | 0.88% | 1 | 0.0 |
| 100m | GFM\|H7\|AB | AB | 19 | 1.917 | 1.92% | 2 | 34.6 |
| 100m | GFM\|K26\|QC | QC | 20 | 0.760 | 0.76% | 14 | 412.2 |
| 119m | GFM\|J27\|NL | NL | 1 | 1.810 | 1.52% | 30 | 459.6 |
| 119m | GFM\|K9\|AB | AB | 2 | 2.951 | 2.48% | 4 | 113.9 |
| 119m | GFM\|M4\|BC | BC | 3 | 2.122 | 1.78% | 4 | 174.0 |
| 119m | GFM\|F18\|ON | ON | 4 | 2.740 | 2.30% | 28 | 259.4 |
| 119m | GFM\|H25\|QC | QC | 5 | 1.627 | 1.37% | 9 | 395.2 |
| 119m | GFM\|I31\|NL | NL | 6 | 2.260 | 1.90% | 22 | 343.4 |
| 119m | GFM\|L6\|BC | BC | 7 | 1.370 | 1.15% | 2 | 54.4 |
| 119m | GFM\|I12\|SK | SK | 8 | 1.861 | 1.56% | 24 | 264.5 |
| 119m | GFM\|G28\|QC | QC | 9 | 0.955 | 0.80% | 2 | 129.4 |
| 119m | GFM\|K1\|BC | BC | 10 | 0.822 | 0.69% | 3 | 33.9 |
| 119m | GFM\|F23\|ON | ON | 11 | 1.367 | 1.15% | 17 | 286.1 |
| 119m | GFM\|H2\|BC | BC | 12 | 2.995 | 2.52% | 4 | 101.7 |
| 119m | GFM\|N3\|BC | BC | 13 | 1.828 | 1.54% | 12 | 159.5 |
| 119m | GFM\|K10\|AB | AB | 14 | 2.252 | 1.89% | 33 | 147.0 |
| 119m | GFM\|K7\|AB | AB | 15 | 1.473 | 1.24% | 3 | 46.6 |
| 119m | GFM\|E20\|ON | ON | 16 | 1.658 | 1.39% | 8 | 198.0 |
| 119m | GFM\|C25\|QC | QC | 17 | 1.053 | 0.89% | 1 | 0.0 |
| 119m | GFM\|M6\|BC | BC | 18 | 1.812 | 1.52% | 29 | 106.0 |
| 119m | GFM\|G27\|QC | QC | 19 | 1.030 | 0.87% | 3 | 200.3 |
| 119m | GFM\|E30\|NB | NB | 20 | 2.021 | 1.70% | 1 | 0.0 |
| 150m | GFM\|F19\|ON | ON | 1 | 3.219 | 2.15% | 22 | 248.1 |
| 150m | GFM\|K9\|AB | AB | 2 | 3.882 | 2.59% | 5 | 114.0 |
| 150m | GFM\|J27\|NL | NL | 3 | 2.338 | 1.56% | 30 | 460.1 |
| 150m | GFM\|M4\|BC | BC | 4 | 3.075 | 2.05% | 12 | 193.3 |
| 150m | GFM\|H25\|QC | QC | 5 | 2.081 | 1.39% | 9 | 395.2 |
| 150m | GFM\|I31\|NL | NL | 6 | 3.033 | 2.02% | 22 | 348.0 |
| 150m | GFM\|I12\|SK | SK | 7 | 2.940 | 1.96% | 25 | 269.9 |
| 150m | GFM\|L7\|BC | BC | 8 | 3.875 | 2.58% | 19 | 176.5 |
| 150m | GFM\|C22\|ON | ON | 9 | 2.956 | 1.97% | 7 | 148.8 |
| 150m | GFM\|G28\|QC | QC | 10 | 1.497 | 1.00% | 3 | 172.6 |
| 150m | GFM\|E17\|ON | ON | 11 | 3.552 | 2.37% | 18 | 222.9 |
| 150m | GFM\|K1\|BC | BC | 12 | 0.934 | 0.62% | 3 | 34.2 |
| 150m | GFM\|H2\|BC | BC | 13 | 3.464 | 2.31% | 4 | 104.1 |
| 150m | GFM\|F23\|ON | ON | 14 | 1.958 | 1.31% | 17 | 281.0 |
| 150m | GFM\|K10\|AB | AB | 15 | 3.034 | 2.02% | 35 | 150.9 |
| 150m | GFM\|H7\|AB | AB | 16 | 3.790 | 2.53% | 3 | 66.8 |
| 150m | GFM\|C25\|QC | QC | 17 | 1.347 | 0.90% | 1 | 0.0 |
| 150m | GFM\|K7\|AB | AB | 18 | 1.730 | 1.15% | 3 | 28.8 |
| 150m | GFM\|N3\|BC | BC | 19 | 2.071 | 1.38% | 14 | 159.9 |
| 150m | GFM\|G27\|QC | QC | 20 | 1.317 | 0.88% | 3 | 200.3 |

## 6. Diminishing returns and screening diagnostics

| case | first k with marginal < 1% of k=0 cost | k=20 capacity-relaxed gap | k=20 existing utilization |
|---|---:|---:|---:|
| 100m | 13 | 7.81% | 25.50% |
| 119m | 13 | 9.69% | 30.34% |
| 150m | 13 | 10.46% | 35.80% |

The capacity-relaxed gap is against a bound that ignores existing
capacity; it is not an optimality gap. The selected sets are greedy
prefixes, not a global optimum.

## 7. Labels and caveats

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
- The 100 and 150 Mm3 cases scale each province's node harvest vector
  from the 119 Mm3 allocation; within-province node shares are
  unchanged.
- NT positive nodes are not candidate module hosts because no NT road
  factor is published; their volume remains in the demand set.
- No national claim, policy claim, UI change or official OSeCAN change
  is made.

## 8. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.greenfield_siting_sensitivity_v1_cases
```

