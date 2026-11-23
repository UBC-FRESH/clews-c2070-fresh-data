# Greenfield break-even annualized capital thresholds v1: 100/119/150 Mm3

Status: **threshold diagnostic** — `not_investment_advice`.
Evidence label: `model_estimate`; sensitivity label: `transport_only`; `observed=false`; `policy_grade=false`.

This artifact states a break-even **threshold**, not a capital cost
estimate, for each transport-only siting case. It does not estimate
module capex, operating cost, technology, class capacity, revenue,
permitting, landbase or facility design. No national or policy
claim is made.

## 1. Definition

For case `c` and module count `k`, with transport cost `TC` and
module-served annual volume `V`:

```text
cumulative threshold_k = (TC_0 - TC_k) / V_k
marginal threshold_k = (TC_{k-1} - TC_k) / (V_k - V_{k-1})
```

Units are 2026 CAD per (m3/yr) of module-served volume. The
threshold is the maximum annualized capital charge that the
transport saving versus the case `k=0` baseline could support at
break-even, before any other cost or revenue. No discount rate,
lifetime or capex assumption is used.

Source: `data/derived/national/facilities/greenfield_siting_sensitivity_v1_cases/k_tradeoff.csv`  
SHA-256: `27cdb095bf2ee72bcbcfb435bc6f766741ee891119a20d9a064c4204d1cded01`  
The 119 Mm3 rows are checked for parity against `greenfield_breakeven_capital_threshold_v1`.

## 2. Case headline

| case | assigned (Mm3/yr) | k=1 cumulative | minimum cumulative | k=20 cumulative | k=20 saving (B CAD/yr) | k=20 volume (Mm3/yr) | median defined marginal |
|---|---:|---:|---:|---:|---:|---:|---:|
| 100m | 100.000 | 63.00 | 37.14 (k=19) | 37.80 | 1.144 | 30.266 | 37.07 |
| 119m | 118.977 | 59.47 | 40.55 (k=4) | 40.87 | 1.471 | 36.006 | 41.89 |
| 150m | 150.000 | 74.09 | 45.31 (k=18) | 46.47 | 2.421 | 52.092 | 51.23 |

All threshold values are CAD per (m3/yr).

## 3. Combined threshold table (k = 0..20)

| case | k | added module | cost (B CAD/yr) | cumulative saving (B CAD/yr) | module volume (Mm3/yr) | cumulative threshold (CAD per m3/yr) | marginal saving (B CAD/yr) | marginal volume (Mm3/yr) | marginal threshold (CAD per m3/yr) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 100m | 0 | `` | 2.572 | 0.000 | 0.000 |  | 0.000 | 0.000 |  |
| 100m | 1 | `GFM\|J27\|NL` | 2.391 | 0.181 | 2.870 | 63.00 | 0.181 | 2.870 | 63.00 |
| 100m | 2 | `GFM\|M4\|BC` | 2.233 | 0.338 | 7.358 | 46.00 | 0.158 | 4.488 | 35.13 |
| 100m | 3 | `GFM\|K9\|AB` | 2.094 | 0.477 | 11.906 | 40.08 | 0.139 | 4.548 | 30.50 |
| 100m | 4 | `GFM\|F18\|ON` | 1.978 | 0.594 | 15.048 | 39.45 | 0.116 | 3.141 | 37.07 |
| 100m | 5 | `GFM\|H25\|QC` | 1.900 | 0.672 | 16.177 | 41.54 | 0.078 | 1.129 | 69.32 |
| 100m | 6 | `GFM\|I31\|NL` | 1.835 | 0.737 | 17.723 | 41.57 | 0.065 | 1.546 | 41.89 |
| 100m | 7 | `GFM\|M6\|BC` | 1.779 | 0.792 | 18.845 | 42.05 | 0.056 | 1.123 | 49.68 |
| 100m | 8 | `GFM\|I13\|SK` | 1.737 | 0.835 | 19.791 | 42.19 | 0.043 | 0.946 | 45.02 |
| 100m | 9 | `GFM\|G28\|QC` | 1.695 | 0.876 | 20.972 | 41.78 | 0.041 | 1.181 | 34.90 |
| 100m | 10 | `GFM\|K1\|BC` | 1.662 | 0.910 | 21.267 | 42.78 | 0.033 | 0.294 | 113.83 |
| 100m | 11 | `GFM\|H2\|BC` | 1.634 | 0.938 | 23.660 | 39.63 | 0.028 | 2.393 | 11.67 |
| 100m | 12 | `GFM\|E20\|ON` | 1.608 | 0.963 | 24.289 | 39.67 | 0.026 | 0.629 | 40.92 |
| 100m | 13 | `GFM\|E30\|NB` | 1.583 | 0.989 | 26.310 | 37.59 | 0.026 | 2.021 | 12.64 |
| 100m | 14 | `GFM\|K10\|AB` | 1.557 | 1.014 | 26.310 | 38.56 | 0.025 | 0.001 | 44,517.81 † |
| 100m | 15 | `GFM\|N3\|BC` | 1.533 | 1.039 | 26.470 | 39.24 | 0.024 | 0.160 | 151.28 |
| 100m | 16 | `GFM\|K7\|AB` | 1.510 | 1.062 | 27.474 | 38.65 | 0.023 | 1.004 | 23.16 |
| 100m | 17 | `GFM\|G27\|QC` | 1.489 | 1.083 | 27.474 | 39.42 | 0.021 | 0.000 | — |
| 100m | 18 | `GFM\|C25\|QC` | 1.468 | 1.104 | 28.350 | 38.93 | 0.021 | 0.876 | 23.42 |
| 100m | 19 | `GFM\|H7\|AB` | 1.448 | 1.124 | 30.266 | 37.14 | 0.020 | 1.917 | 10.63 |
| 100m | 20 | `GFM\|K26\|QC` | 1.428 | 1.144 | 30.266 | 37.80 | 0.020 | 0.000 | — |
| 119m | 0 | `` | 3.220 | 0.000 | 0.000 |  | 0.000 | 0.000 |  |
| 119m | 1 | `GFM\|J27\|NL` | 2.994 | 0.226 | 3.805 | 59.47 | 0.226 | 3.805 | 59.47 |
| 119m | 2 | `GFM\|K9\|AB` | 2.790 | 0.430 | 9.848 | 43.63 | 0.203 | 6.044 | 33.65 |
| 119m | 3 | `GFM\|M4\|BC` | 2.589 | 0.631 | 15.352 | 41.12 | 0.202 | 5.504 | 36.63 |
| 119m | 4 | `GFM\|F18\|ON` | 2.436 | 0.784 | 19.341 | 40.55 | 0.153 | 3.989 | 38.34 |
| 119m | 5 | `GFM\|H25\|QC` | 2.339 | 0.881 | 20.572 | 42.84 | 0.097 | 1.231 | 78.95 |
| 119m | 6 | `GFM\|I31\|NL` | 2.258 | 0.962 | 22.479 | 42.79 | 0.080 | 1.907 | 42.17 |
| 119m | 7 | `GFM\|L6\|BC` | 2.183 | 1.037 | 23.595 | 43.94 | 0.075 | 1.116 | 67.26 |
| 119m | 8 | `GFM\|I12\|SK` | 2.130 | 1.090 | 25.189 | 43.29 | 0.054 | 1.594 | 33.62 |
| 119m | 9 | `GFM\|G28\|QC` | 2.077 | 1.143 | 26.272 | 43.51 | 0.053 | 1.082 | 48.72 |
| 119m | 10 | `GFM\|K1\|BC` | 2.035 | 1.185 | 27.067 | 43.79 | 0.042 | 0.795 | 52.77 |
| 119m | 11 | `GFM\|F23\|ON` | 2.000 | 1.221 | 27.911 | 43.73 | 0.035 | 0.844 | 41.89 |
| 119m | 12 | `GFM\|H2\|BC` | 1.964 | 1.256 | 30.906 | 40.63 | 0.035 | 2.995 | 11.75 |
| 119m | 13 | `GFM\|N3\|BC` | 1.935 | 1.285 | 31.048 | 41.39 | 0.029 | 0.142 | 206.46 |
| 119m | 14 | `GFM\|K10\|AB` | 1.907 | 1.313 | 31.048 | 42.29 | 0.028 | 0.000 | — |
| 119m | 15 | `GFM\|K7\|AB` | 1.879 | 1.341 | 32.328 | 41.49 | 0.028 | 1.280 | 21.90 |
| 119m | 16 | `GFM\|E20\|ON` | 1.852 | 1.368 | 32.930 | 41.54 | 0.027 | 0.602 | 44.48 |
| 119m | 17 | `GFM\|C25\|QC` | 1.826 | 1.394 | 33.983 | 41.03 | 0.027 | 1.053 | 25.18 |
| 119m | 18 | `GFM\|M6\|BC` | 1.800 | 1.420 | 33.985 | 41.79 | 0.026 | 0.002 | 16,131.99 † |
| 119m | 19 | `GFM\|G27\|QC` | 1.774 | 1.446 | 33.985 | 42.55 | 0.026 | 0.000 | — |
| 119m | 20 | `GFM\|E30\|NB` | 1.749 | 1.471 | 36.006 | 40.87 | 0.026 | 2.021 | 12.64 |
| 150m | 0 | `` | 4.728 | 0.000 | 0.000 |  | 0.000 | 0.000 |  |
| 150m | 1 | `GFM\|F19\|ON` | 4.197 | 0.532 | 7.174 | 74.09 | 0.532 | 7.174 | 74.09 |
| 150m | 2 | `GFM\|K9\|AB` | 3.828 | 0.900 | 16.522 | 54.45 | 0.368 | 9.348 | 39.39 |
| 150m | 3 | `GFM\|J27\|NL` | 3.543 | 1.185 | 20.772 | 57.05 | 0.285 | 4.250 | 67.12 |
| 150m | 4 | `GFM\|M4\|BC` | 3.303 | 1.425 | 27.043 | 52.70 | 0.240 | 6.272 | 38.31 |
| 150m | 5 | `GFM\|H25\|QC` | 3.184 | 1.544 | 28.238 | 54.68 | 0.119 | 1.195 | 99.40 |
| 150m | 6 | `GFM\|I31\|NL` | 3.073 | 1.655 | 30.771 | 53.77 | 0.111 | 2.533 | 43.70 |
| 150m | 7 | `GFM\|I12\|SK` | 2.975 | 1.753 | 32.678 | 53.64 | 0.098 | 1.906 | 51.43 |
| 150m | 8 | `GFM\|L7\|BC` | 2.881 | 1.847 | 34.147 | 54.08 | 0.094 | 1.469 | 64.07 |
| 150m | 9 | `GFM\|C22\|ON` | 2.798 | 1.930 | 37.743 | 51.14 | 0.083 | 3.596 | 23.19 |
| 150m | 10 | `GFM\|G28\|QC` | 2.723 | 2.005 | 39.403 | 50.88 | 0.075 | 1.660 | 45.04 |
| 150m | 11 | `GFM\|E17\|ON` | 2.650 | 2.078 | 40.827 | 50.89 | 0.073 | 1.424 | 51.23 |
| 150m | 12 | `GFM\|K1\|BC` | 2.601 | 2.127 | 41.762 | 50.93 | 0.049 | 0.934 | 52.59 |
| 150m | 13 | `GFM\|H2\|BC` | 2.559 | 2.169 | 45.225 | 47.97 | 0.042 | 3.464 | 12.25 |
| 150m | 14 | `GFM\|F23\|ON` | 2.519 | 2.209 | 45.614 | 48.44 | 0.040 | 0.388 | 102.96 |
| 150m | 15 | `GFM\|K10\|AB` | 2.481 | 2.247 | 45.614 | 49.26 | 0.037 | 0.000 | — |
| 150m | 16 | `GFM\|H7\|AB` | 2.444 | 2.284 | 49.404 | 46.23 | 0.037 | 3.790 | 9.75 |
| 150m | 17 | `GFM\|C25\|QC` | 2.408 | 2.320 | 50.562 | 45.89 | 0.036 | 1.159 | 31.36 |
| 150m | 18 | `GFM\|K7\|AB` | 2.373 | 2.355 | 51.972 | 45.31 | 0.034 | 1.410 | 24.43 |
| 150m | 19 | `GFM\|N3\|BC` | 2.340 | 2.388 | 52.092 | 45.84 | 0.033 | 0.120 | 279.56 |
| 150m | 20 | `GFM\|G27\|QC` | 2.307 | 2.421 | 52.092 | 46.47 | 0.033 | 0.000 | — |

`†` marks a thin marginal volume (below 0.01% of that case's
annual demand); the ratio is shown but is not a stable per-unit
threshold. `—` marks a zero marginal module volume, so the
marginal threshold is undefined. An empty cumulative cell marks
the `k=0` baseline.

## 4. Key thresholds and caveats

- 100m: k=1 **63.00**; minimum **37.14** at k=19; k=20 **37.80** CAD per m3/yr; zero marginal volume at k=17, 20; thin marginal volume at k=14.
- 119m: k=1 **59.47**; minimum **40.55** at k=4; k=20 **40.87** CAD per m3/yr; zero marginal volume at k=14, 19; thin marginal volume at k=18.
- 150m: k=1 **74.09**; minimum **45.31** at k=18; k=20 **46.47** CAD per m3/yr; zero marginal volume at k=15, 20; thin marginal volume at k=none.

The cumulative threshold is not monotonic across k. Each k-series
is a greedy screening prefix, not a global optimum. The table is
not a module ranking or a recommendation.

- `model_estimate`; `transport_only`; `not_investment_advice`;
  `observed=false`; `policy_grade=false`.
- This is a break-even threshold, not a capital cost estimate.
- No capex, discount rate, asset life, fixed operating cost,
  feedstock cost, processing cost, product revenue or financing
  assumption is introduced.
- Transport savings include re-routing and existing-facility
  effects; they are not a module-only revenue stream.
- Distances and costs inherit the screening limitations of
  `greenfield_siting_sensitivity_v1_cases`.
- No national claim, policy claim, UI change or official OSeCAN
  change is made.

## 5. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.greenfield_breakeven_capital_threshold_v1_cases
```
