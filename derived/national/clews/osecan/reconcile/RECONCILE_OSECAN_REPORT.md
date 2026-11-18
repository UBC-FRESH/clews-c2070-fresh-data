# Reconciled zonal OSeCAN run

Status: **fresh_side_provisional_not_c2070_official**.  The BC residue caps were reconciled to the refined
all-BC chain (B1 3.605475 PJ, B2 32.204471 PJ from 2028; total 35.809946 PJ)
and the `Current Measures` zonal experiment was rerun in a disposable OSeCAN
copy at commit `40d5b43`.  The public `deltae/C2070` repository was
not modified.

## Caps loaded

| Technology | 2028 (PJ) | 2070 (PJ) |
|---|---:|---:|
| SUPBCW | 35.809946 | 35.809946 |
| SUPBCWB1 | 3.605475 | 3.605475 |
| SUPBCWB2 | 32.204471 | 32.204471 |

## Solver and objective

| Run | Status | Objective (M$) | LP rows | LP cols |
|---|---|---:|---:|---:|
| control | optimal | 1,371,586.14 | 274,851 | 235,800 |
| zonal | optimal | 1,371,621.94 | 274,851 | 235,800 |

Previous run: control 1,371,553.35 M$,
zonal 1,371,600.56 M$ with B2 cap
39.286509 PJ.  New-minus-old objective:
control 32.79 M$,
zonal 21.38 M$.

## SUP activity by year (PJ)

National `SUPBCW` (control only):

| Year | Control | Zonal |
|---:|---:|---:|
| 2021 | 0.000 | 0.000 |
| 2022 | 35.810 | 0.000 |
| 2025 | 35.810 | 0.000 |
| 2028 | 35.810 | 0.000 |
| 2030 | 35.810 | 0.000 |
| 2035 | 35.810 | 0.000 |
| 2040 | 35.810 | 0.000 |
| 2050 | 35.810 | 0.000 |
| 2060 | 35.810 | 0.000 |
| 2070 | 35.810 | 0.000 |

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
| 2030 | 0.000 | 32.205 |
| 2035 | 0.000 | 32.205 |
| 2040 | 0.000 | 32.205 |
| 2050 | 0.000 | 32.205 |
| 2060 | 0.000 | 32.205 |
| 2070 | 0.000 | 32.205 |

## PWRBCWB1/B2 dispatch (PJ)

| Year | PWRBCWB1 control | PWRBCWB1 zonal | PWRBCWB2 control | PWRBCWB2 zonal |
|---:|---:|---:|---:|---:|
| 2021 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2022 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2025 | 0.000 | 0.969 | 0.000 | 0.992 |
| 2028 | 0.000 | 0.969 | 0.000 | 5.204 |
| 2030 | 0.000 | 0.969 | 0.000 | 8.657 |
| 2035 | 0.000 | 0.969 | 0.000 | 8.657 |
| 2040 | 0.000 | 0.969 | 0.000 | 8.657 |
| 2050 | 0.000 | 0.969 | 0.000 | 8.657 |
| 2060 | 0.000 | 0.969 | 0.000 | 8.657 |
| 2070 | 0.000 | 0.969 | 0.000 | 8.657 |

## Cap binding (zonal run)

| Technology | Max utilisation | Binding | Binding years |
|---|---:|---|---|
| SUPBCW | 0.000 | no | none |
| SUPBCWB1 | 1.000 | yes | 2026-2070 |
| SUPBCWB2 | 1.000 | yes | 2030-2070 |

## Other-zone PWRBCW dispatch (PJ)

| Year | Control | Zonal |
|---:|---:|---:|
| 2021 | 0.000 | 0.000 |
| 2022 | 9.626 | 0.000 |
| 2025 | 9.626 | 0.000 |
| 2028 | 9.626 | 0.000 |
| 2030 | 9.626 | 0.000 |
| 2035 | 9.626 | 0.000 |
| 2040 | 9.626 | 0.000 |
| 2050 | 9.626 | 0.000 |
| 2060 | 9.626 | 0.000 |
| 2070 | 9.626 | 0.000 |

Totals: control 471.690 PJ;
zonal 0.000 PJ.

## Emissions

| Year | Control (Mt CO2) | Zonal (Mt CO2) |
|---:|---:|---:|
| 2021 | 0.023274 | 0.023274 |
| 2022 | 1.767534 | 2.258476 |
| 2025 | 0.520740 | 1.011682 |
| 2028 | 0.791052 | 1.281994 |
| 2030 | 1.745088 | 2.236030 |
| 2035 | 1.767534 | 2.258476 |
| 2040 | 1.767534 | 2.258476 |
| 2050 | 1.767534 | 2.258476 |
| 2060 | 0.000000 | 0.000000 |
| 2070 | 0.000000 | 0.000000 |

Cumulative: control 46.930848 Mt;
zonal 61.659110 Mt;
delta 14.728262 Mt.

## Old vs new

| Metric | Previous | Reconciled |
|---|---:|---:|
| Zonal B1 cap 2028+ (PJ) | 3.672286 | 3.605475 |
| Zonal B2 cap 2028+ (PJ) | 39.286509 | 32.204471 |
| Zonal B1 binding years | 2026-2070 | 2026-2070 |
| Zonal B2 binding years | 2032-2070 | 2030-2070 |
| PWRBCWB1 2050 (PJ) | 0.987175 | 0.969212 |
| PWRBCWB2 2050 (PJ) | 10.560887 | 8.657124 |
| Zonal objective (M$) | 1,371,600.56 | 1,371,621.94 |
| Control objective (M$) | 1,371,553.35 | 1,371,586.14 |
| Zonal emissions (Mt) | 61.659110 | 61.659110 |
| Control emissions (Mt) | 43.990577 | 46.930848 |

The zonal run is the cap-constrained case; the control uses the same total
energy cap as one national technology.  All runs solved to the status shown
above.  The reduced B2 cap removes 7.082 PJ/yr of Interior residue relative
to the previous run; the dispatch response is reported in the tables, not
asserted as a forecast.
