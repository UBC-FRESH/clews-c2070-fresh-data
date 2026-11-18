# FFCM-implied zonal OSeCAN reconciliation

Status: **fresh_side_provisional_not_c2070_official**.  The BC residue base was resolved to the recomputed
FFCM-implied B2 recovery 0.723799161 (not the stale published 0.583931303) and
the caps were rebuilt with the chain (B1 3.605475
PJ, B2 39.918341 PJ, total
43.523816 PJ from 2028).  The `Current Measures`
experiment was rerun in a disposable OSeCAN copy at commit
`40d5b43`.  The public `deltae/C2070` repository was not modified.

## Caps loaded

| Technology | 2028 (PJ) | 2070 (PJ) |
|---|---:|---:|
| SUPBCW | 43.523816 | 43.523816 |
| SUPBCWB1 | 3.605475 | 3.605475 |
| SUPBCWB2 | 39.918341 | 39.918341 |

## Solver and objective

| Run | Status | Objective (M$) | LP rows | LP cols |
|---|---|---:|---:|---:|
| control | optimal | 1,371,550.76 | 274,851 | 235,800 |
| zonal | optimal | 1,371,599.09 | 274,851 | 235,800 |

Objective deltas against the two earlier bases:

| Basis | Control (M$) | Zonal (M$) | Control delta (M$) | Zonal delta (M$) |
|---|---:|---:|---:|---:|
| Original published (42.9588 PJ) | 1,371,553.35 | 1,371,600.56 | -2.59 | -1.47 |
| Interim held (35.8099 PJ) | 1,371,586.14 | 1,371,621.94 | -35.38 | -22.85 |

## SUP activity by year (PJ)

National `SUPBCW` (control only):

| Year | Control | Zonal |
|---:|---:|---:|
| 2021 | 0.000 | 0.000 |
| 2022 | 43.524 | 0.000 |
| 2025 | 43.524 | 0.000 |
| 2028 | 43.524 | 0.000 |
| 2030 | 43.524 | 0.000 |
| 2035 | 43.524 | 0.000 |
| 2040 | 43.524 | 0.000 |
| 2050 | 43.524 | 0.000 |
| 2060 | 43.524 | 0.000 |
| 2070 | 43.524 | 0.000 |

Zonal `SUPBCWB1`:

| Year | Control | Zonal |
|---:|---:|---:|
| 2021 | 0.000 | 0.000 |
| 2022 | 0.000 | 0.000 |
| 2025 | 0.000 | 3.605 |
| 2028 | 0.000 | 3.605 |
| 2030 | 0.000 | 3.605 |
| 2035 | 0.000 | 3.605 |
| 2040 | 0.000 | 3.605 |
| 2050 | 0.000 | 3.605 |
| 2060 | 0.000 | 3.605 |
| 2070 | 0.000 | 3.605 |

Zonal `SUPBCWB2`:

| Year | Control | Zonal |
|---:|---:|---:|
| 2021 | 0.000 | 0.000 |
| 2022 | 0.000 | 0.000 |
| 2025 | 0.000 | 3.691 |
| 2028 | 0.000 | 19.357 |
| 2030 | 0.000 | 35.394 |
| 2035 | 0.000 | 39.918 |
| 2040 | 0.000 | 39.918 |
| 2050 | 0.000 | 39.918 |
| 2060 | 0.000 | 39.918 |
| 2070 | 0.000 | 39.918 |

## PWRBCWB1/B2 dispatch (PJ)

| Year | PWRBCWB1 control | PWRBCWB1 zonal | PWRBCWB2 control | PWRBCWB2 zonal |
|---:|---:|---:|---:|---:|
| 2021 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2022 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2025 | 0.000 | 0.969 | 0.000 | 0.992 |
| 2028 | 0.000 | 0.969 | 0.000 | 5.204 |
| 2030 | 0.000 | 0.969 | 0.000 | 9.515 |
| 2035 | 0.000 | 0.969 | 0.000 | 10.731 |
| 2040 | 0.000 | 0.969 | 0.000 | 10.731 |
| 2050 | 0.000 | 0.969 | 0.000 | 10.731 |
| 2060 | 0.000 | 0.969 | 0.000 | 10.731 |
| 2070 | 0.000 | 0.969 | 0.000 | 10.731 |

## Cap binding (zonal run)

| Technology | Max utilisation | Binding | Binding years |
|---|---:|---|---|
| SUPBCW | 0.000 | no | none |
| SUPBCWB1 | 1.000 | yes | 2026-2070 |
| SUPBCWB2 | 1.000 | yes | 2032-2070 |

## Other-zone PWRBCW dispatch (PJ)

| Year | Control | Zonal |
|---:|---:|---:|
| 2021 | 0.000 | 0.000 |
| 2022 | 11.700 | 0.000 |
| 2025 | 11.700 | 0.000 |
| 2028 | 11.700 | 0.000 |
| 2030 | 11.700 | 0.000 |
| 2035 | 11.700 | 0.000 |
| 2040 | 11.700 | 0.000 |
| 2050 | 11.700 | 0.000 |
| 2060 | 11.700 | 0.000 |
| 2070 | 11.700 | 0.000 |

Totals: control 573.297 PJ;
zonal 0.000 PJ.

## Emissions

| Year | Control (Mt CO2) | Zonal (Mt CO2) |
|---:|---:|---:|
| 2021 | 0.023274 | 0.023274 |
| 2022 | 1.661779 | 2.258476 |
| 2025 | 0.414984 | 1.011682 |
| 2028 | 0.685297 | 1.281994 |
| 2030 | 1.639333 | 2.236030 |
| 2035 | 1.661779 | 2.258476 |
| 2040 | 1.661779 | 2.258476 |
| 2050 | 1.661779 | 2.258476 |
| 2060 | 0.000000 | 0.000000 |
| 2070 | 0.000000 | 0.000000 |

Cumulative: control 43.758197 Mt;
zonal 61.659110 Mt;
delta 17.900913 Mt.

## Three-basis comparison

| Metric | Original 42.9588 PJ | Interim 35.8099 PJ | FFCM-implied |
|---|---:|---:|---:|
| Zonal B1 cap 2028+ (PJ) | 3.672286 | 3.605475 | 3.605475 |
| Zonal B2 cap 2028+ (PJ) | 39.286509 | 32.204471 | 39.918341 |
| Zonal B1 binding years | 2026-2070 | 2026-2070 | 2026-2070 |
| Zonal B2 binding years | 2032-2070 | 2030-2070 | 2032-2070 |
| PWRBCWB1 2050 (PJ) | 0.987175 | 0.969212 | 0.969212 |
| PWRBCWB2 2050 (PJ) | 10.560887 | 8.657124 | 10.730726 |
| Zonal objective (M$) | 1,371,600.56 | 1,371,621.94 | 1,371,599.09 |
| Control objective (M$) | 1,371,553.35 | 1,371,586.14 | 1,371,550.76 |
| Zonal emissions (Mt) | 61.659110 | 61.659110 | 61.659110 |
| Control emissions (Mt) | 43.990577 | 46.930848 | 43.758197 |

The zonal run is the cap-constrained case; the control uses the same total
energy cap as one national technology.  All runs solved to the status shown
above.  The FFCM-implied B2 cap is 7.714 PJ/yr above the interim held cap and
0.632 PJ/yr above the original published cap; the dispatch response is
reported in the tables, not asserted as a forecast.
