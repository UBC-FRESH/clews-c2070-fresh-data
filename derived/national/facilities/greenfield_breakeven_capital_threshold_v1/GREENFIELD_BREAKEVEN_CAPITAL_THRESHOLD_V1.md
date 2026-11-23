# Greenfield break-even annualized capital thresholds v1

Status: **threshold diagnostic** — `not_investment_advice`.
Evidence label: `model_estimate`; sensitivity label: `transport_only`; `observed=false`; `policy_grade=false`.

This artifact states a break-even **threshold**, not a capital cost
estimate. It does not estimate module capex, operating cost,
technology, class capacity, revenue, permitting, landbase or
facility design. No national or policy claim is made.

## 1. Definition

For module count `k`, with transport cost `TC` from
`greenfield_siting_sensitivity_v1` and module-served annual volume
`V`:

```text
cumulative threshold_k = (TC_0 - TC_k) / V_k
marginal threshold_k = (TC_{k-1} - TC_k) / (V_k - V_{k-1})
```

Units are 2026 CAD per (m3/yr) of module-served volume. The
threshold is the maximum annualized capital charge that the
transport saving could support at break-even, before any other
cost or revenue. No discount rate, lifetime or capex assumption is
used.

The saving is the full transport re-optimization effect versus the
transport-only `k=0` baseline, including changes in existing
facility use. It is not attributed solely to module capital.

Source: `data/derived/national/facilities/greenfield_siting_sensitivity_v1/k_tradeoff.csv`  
SHA-256: `804dc54977c6a2f4b9abeea5885b8d3d3b6fe35333ddc77d2a8fda95948ee434`  
Baseline transport cost: 3.220 B CAD/yr  
Assigned demand: 118.977 Mm3/yr

## 2. Threshold table (k = 1..20)

| k | added module | cost (B CAD/yr) | cumulative saving (B CAD/yr) | module volume (Mm3/yr) | cumulative threshold (CAD per m3/yr) | marginal saving (B CAD/yr) | marginal volume (Mm3/yr) | marginal threshold (CAD per m3/yr) |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `GFM\|J27\|NL` | 2.994 | 0.226 | 3.805 | 59.47 | 0.226 | 3.805 | 59.47 |
| 2 | `GFM\|K9\|AB` | 2.790 | 0.430 | 9.848 | 43.63 | 0.203 | 6.044 | 33.65 |
| 3 | `GFM\|M4\|BC` | 2.589 | 0.631 | 15.352 | 41.12 | 0.202 | 5.504 | 36.63 |
| 4 | `GFM\|F18\|ON` | 2.436 | 0.784 | 19.341 | 40.55 | 0.153 | 3.989 | 38.34 |
| 5 | `GFM\|H25\|QC` | 2.339 | 0.881 | 20.572 | 42.84 | 0.097 | 1.231 | 78.95 |
| 6 | `GFM\|I31\|NL` | 2.258 | 0.962 | 22.479 | 42.79 | 0.080 | 1.907 | 42.17 |
| 7 | `GFM\|L6\|BC` | 2.183 | 1.037 | 23.595 | 43.94 | 0.075 | 1.116 | 67.26 |
| 8 | `GFM\|I12\|SK` | 2.130 | 1.090 | 25.189 | 43.29 | 0.054 | 1.594 | 33.62 |
| 9 | `GFM\|G28\|QC` | 2.077 | 1.143 | 26.272 | 43.51 | 0.053 | 1.082 | 48.72 |
| 10 | `GFM\|K1\|BC` | 2.035 | 1.185 | 27.067 | 43.79 | 0.042 | 0.795 | 52.77 |
| 11 | `GFM\|F23\|ON` | 2.000 | 1.221 | 27.911 | 43.73 | 0.035 | 0.844 | 41.89 |
| 12 | `GFM\|H2\|BC` | 1.964 | 1.256 | 30.906 | 40.63 | 0.035 | 2.995 | 11.75 |
| 13 | `GFM\|N3\|BC` | 1.935 | 1.285 | 31.048 | 41.39 | 0.029 | 0.142 | 206.46 |
| 14 | `GFM\|K10\|AB` | 1.907 | 1.313 | 31.048 | 42.29 | 0.028 | 0.000 | — |
| 15 | `GFM\|K7\|AB` | 1.879 | 1.341 | 32.328 | 41.49 | 0.028 | 1.280 | 21.90 |
| 16 | `GFM\|E20\|ON` | 1.852 | 1.368 | 32.930 | 41.54 | 0.027 | 0.602 | 44.48 |
| 17 | `GFM\|C25\|QC` | 1.826 | 1.394 | 33.983 | 41.03 | 0.027 | 1.053 | 25.18 |
| 18 | `GFM\|M6\|BC` | 1.800 | 1.420 | 33.985 | 41.79 | 0.026 | 0.002 | 16,131.99 † |
| 19 | `GFM\|G27\|QC` | 1.774 | 1.446 | 33.985 | 42.55 | 0.026 | 0.000 | — |
| 20 | `GFM\|E30\|NB` | 1.749 | 1.471 | 36.006 | 40.87 | 0.026 | 2.021 | 12.64 |

`†` marks a thin marginal volume (below 0.01% of annual demand);
the ratio is shown but is not a stable per-unit threshold.
`—` marks a zero marginal module volume, so the marginal
threshold is undefined.

## 3. Key thresholds

- k=1 cumulative threshold: **59.47** CAD per m3/yr.
- Minimum cumulative threshold: **40.55** CAD per m3/yr at k=4.
- k=20 cumulative threshold: **40.87** CAD per m3/yr.
- k=20 cumulative transport saving: **1.471 B CAD/yr**.
- k=20 module-served volume: **36.006 Mm3/yr**.
- Median defined marginal threshold: **41.89** CAD per m3/yr.
- Zero marginal module volume at k=14, 19; undefined marginal threshold.
- Thin marginal volume at k=18; flagged `†`.

The cumulative threshold is not monotonic across k. The
k-series is a greedy screening prefix, not a global optimum.
The table is not a module ranking or a recommendation.

## 4. Labels and caveats

- `model_estimate`; `transport_only`; `not_investment_advice`;
  `observed=false`; `policy_grade=false`.
- This is a break-even threshold, not a capital cost estimate.
- No capex, discount rate, asset life, fixed operating cost,
  feedstock cost, processing cost, product revenue or financing
  assumption is introduced.
- Module capacity is the screened module-served volume at that k;
  it is not a nameplate capacity, class capacity or design size.
- Transport savings include re-routing and existing-facility
  effects. They are not a module-only revenue stream.
- Distances and costs inherit the screening limitations of
  `greenfield_siting_sensitivity_v1`.
- No national claim, policy claim, UI change or official OSeCAN
  change is made.

## 5. Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.greenfield_breakeven_capital_threshold_v1
```
