# Zonal BC woody-residue supply in OSeCAN

Status: **FRESH-side provisional** — not an official C2070 result.  The experiment uses a disposable copy of public `deltae/C2070` commit `40d5b43bb3f8`; the public clone was not modified.

## Zonal structure (fuels/techs/input ratios; harmonize result)

| Item | Change |
|---|---|
| Fuels | Added `BCWB1` (B1 South Coast) and `BCWB2` (B2 Interior & North), same matter state/units as `BCW` (PJ). |
| Supply technologies | Added `SUPBCWB1` and `SUPBCWB2`, REGION=CAN, 2021-2070, producing `BCWB1`/`BCWB2` at OAR 1. |
| Conversion plants | `PWRBCWB1` consumes `BCWB1`; `PWRBCWB2` consumes `BCWB2`; input ratio 3.72, capex 3,200 $/kW, fixed 95 $/kW-yr, variable 0, life 30, CF 0.70, CO2 0. |
| National chain | The other eleven `PWRBCW<z>` plants keep national `BCW`; `SUPBCW` is retained for the national control. |

`build-sets` produced 524 technologies and 381 fuels (22,650 IAR rows, 26,200 OAR rows).  `osecan info` loaded the modified model.  `harmonize` returned exit 0 for the base parameters and for all three scenario parameter sets: **HARMONIZED — all params reference valid SET codes.**

### Zonal caps and costs

| Technology | 2021 cap (PJ) | 2028 cap (PJ) | 2050 cap (PJ) | Cost ($/GJ) |
|---|---:|---:|---:|---:|
| `SUPBCWB1` | 3.678381 | 3.672286 | 3.672286 | 2.456978 |
| `SUPBCWB2` | 46.794140 | 39.286509 | 39.286509 | 2.456978 |

The national rollup (`SUPBCW`, used by the control) is 50.472521 PJ in 2021 and 42.958795 PJ from 2028, at 2.456978 $/GJ.

## Runs (objective, SUPBCWB1/B2 activity, PWRBCWB1/B2 dispatch, cap binding, emissions)

All runs are `Current Measures`, 2021-2070, with hydro fixed at 2021 activity and CO2 at 95 $/t to 2025 and 200 $/t from 2026.

| Run | Forcing | Solver | Objective (M$) | Δ vs control (M$) | Emissions total (Mt) |
|---|---|---|---:|---:|---:|
| control | national control | optimal | 1,371,553.35 | — | 43.991 |
| zonal | zonal BC supply | optimal | 1,371,600.56 | 47.21 | 61.659 |
| zonal_bio | zonal BC supply + generic-BIO cost | optimal | 1,385,253.48 | 13,700.13 | 61.659 |

### SUP activity by year (PJ)

| Run / technology | 2021 | 2025 | 2028 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| control / `SUPBCW` | 0.000 | 42.959 | 42.959 | 42.959 | 42.959 | 42.959 | 2,104.981 |
| zonal / `SUPBCWB1` | 0.000 | 3.672 | 3.672 | 3.672 | 3.672 | 3.672 | 168.925 |
| zonal / `SUPBCWB2` | 0.000 | 3.691 | 19.357 | 35.394 | 39.286 | 39.286 | 1,682.097 |
| zonal_bio / `SUPBCWB1` | 0.000 | 3.672 | 3.672 | 3.672 | 3.672 | 3.672 | 168.925 |
| zonal_bio / `SUPBCWB2` | 0.000 | 3.691 | 19.357 | 35.394 | 39.286 | 39.286 | 1,682.097 |

### PWR dispatch by year (PJ electricity)

| Run / technology | 2021 | 2025 | 2028 | 2030 | 2050 | 2070 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| control / `PWRBCW (other zones)` | 0.000 | 11.548 | 11.548 | 11.548 | 11.548 | 11.548 | 565.855 |
| zonal / `PWRBCWB1` | 0.000 | 0.987 | 0.987 | 0.987 | 0.987 | 0.987 | 45.410 |
| zonal / `PWRBCWB2` | 0.000 | 0.992 | 5.204 | 9.515 | 10.561 | 10.561 | 452.177 |
| zonal_bio / `PWRBCWB1` | 0.000 | 0.987 | 0.987 | 0.987 | 0.987 | 0.987 | 45.410 |
| zonal_bio / `PWRBCWB2` | 0.000 | 0.992 | 5.204 | 9.515 | 10.561 | 10.561 | 452.177 |

The control delivers all BCW electricity outside B1/B2; the zonal runs deliver it only in B1/B2.  `PWRBIO` and `SUPBSW` are zero in every run.

### Cap binding

| Run | Technology | Cap binds | Binding years | Binding years count | Max utilisation |
|---|---|---|---|---:|---:|
| control | `SUPBCW` | yes | 2028-2070 | 43 | 1.000 |
| control | `SUPBCWB1` | no | — | 0 | 0.000 |
| control | `SUPBCWB2` | no | — | 0 | 0.000 |
| zonal | `SUPBCW` | no | — | 0 | 0.000 |
| zonal | `SUPBCWB1` | yes | 2026-2070 | 45 | 1.000 |
| zonal | `SUPBCWB2` | yes | 2032-2070 | 39 | 1.000 |
| zonal_bio | `SUPBCW` | no | — | 0 | 0.000 |
| zonal_bio | `SUPBCWB1` | yes | 2026-2070 | 45 | 1.000 |
| zonal_bio | `SUPBCWB2` | yes | 2032-2070 | 39 | 1.000 |

`SUPBCWB1` binds in 2026-2070 (45 years); `SUPBCWB2` binds in 2032-2070 (39 years).  The zonal caps therefore bind even though the national control had no zonal cap.

### PWRBCW dispatch outside B1/B2 (PJ, total 2021-2070)

| Zone | Control | Zonal | Zonal + BIO |
|---|---:|---:|---:|
| A1 | 78.136 | 0.000 | 0.000 |
| A2 | 15.977 | 0.000 | 0.000 |
| L1 | 5.308 | 0.000 | 0.000 |
| M1 | 82.620 | 0.000 | 0.000 |
| O2 | 3.854 | 0.000 | 0.000 |
| Q1 | 115.838 | 0.000 | 0.000 |
| Q2 | 61.002 | 0.000 | 0.000 |
| S1 | 165.432 | 0.000 | 0.000 |
| T1 | 37.689 | 0.000 | 0.000 |

### Emissions

| Run | 2021 | 2025 | 2030 | 2050 | 2070 | Total (Mt) |
|---|---:|---:|---:|---:|---:|---:|
| control | 0.023 | 0.423 | 1.647 | 1.670 | 0.000 | 43.991 |
| zonal | 0.023 | 1.012 | 2.236 | 2.258 | 0.000 | 61.659 |
| zonal_bio | 0.023 | 1.012 | 2.236 | 2.258 | 0.000 | 61.659 |

The zonal constraint raises discounted cost by 47.21 M$ and cumulative CO2 by 17.669 Mt relative to the national control.  The mechanism is spatial: the control sites BCW where it displaces gas; the zonal runs must site it in B1/B2, where it displaces local wind, while gas remains in the other zones.

## Generic-BIO sensitivity

The `zonal_bio` run raises `RNWBIO` VariableCost from 3.00 to 4.00 $/GJ.  This is a documented biomass-wide bypass sensitivity, not a dedicated power-biomass supply curve.

| Metric | Zonal | Zonal + BIO | Δ |
|---|---:|---:|---:|
| Objective (M$) | 1,371,600.56 | 1,385,253.48 | 13,652.92 |
| Emissions total (Mt) | 61.659 | 61.659 | 0.000 |
| SUPBCWB1 total (PJ) | 168.925 | 168.925 | 0.000 |
| SUPBCWB2 total (PJ) | 1,682.097 | 1,682.097 | 0.000 |
| PWRBIO total (PJ) | 0.000 | 0.000 | 0.000 |

The higher generic-BIO cost leaves the BCW dispatch and cap binding unchanged: `PWRBIO` was not on the margin, because wind is slightly cheaper than generic BIO and the zonal BCW caps are already binding.  The objective rises by 13,652.92 M$ because `RNWBIO` also serves end-use BIO demand; this is a real cost of the sensitivity, not a BCW effect.

## Economics/why dispatch or not

The model merit order after the hydro cap is: hydro 67.85 < BCW 82.34 < wind 86.04 < generic BIO 86.28 < gas at $200/t 89.65 $/MWh.  At the documented $95/t gas is 70.37 $/MWh, below BCW, which is why the earlier hydro-frozen diagnostic had zero BCW.  At $200/t the BCW-vs-gas parity price is about 160 $/t; the run is above it, so BCW dispatches.

| Plant | Fuel ($/GJ) | Carbon ($/t) | LCOE ($/MWh) |
|---|---:|---:|---:|
| PWRBCW (zonal BCW base) | 2.4570 | 0.0 | 82.34 |
| PWRBCW (zonal BCW base at $200/t (zero CO2)) | 2.4570 | 200.0 | 82.34 |
| PWRBIO (generic BIO base) | 3.0000 | 0.0 | 86.28 |
| PWRBIO (generic BIO sensitivity) | 4.0000 | 0.0 | 96.54 |
| PWRBSW (switchgrass placeholder) | 4.0000 | 0.0 | 103.01 |
| PWRNGS (gas at $95/t) | 3.0000 | 95.0 | 70.37 |
| PWRNGS (gas at $200/t) | 3.0000 | 200.0 | 89.65 |
| PWRHYD (hydro with $3/GJ RNW placeholder) | 3.0000 | 0.0 | 67.85 |
| PWRWND (wind with $3/GJ RNW placeholder) | 3.0000 | 0.0 | 86.04 |

The zonal caps bind because BCW is the cheapest non-hydro option.  B1 is a small cap (3.67 PJ) and binds from 2026; B2 (39.29 PJ from 2028) binds from 2032.  The early-year ramp is spatial: B1/B2 biomass is not needed until local demand and transmission make it economic, whereas the national control can site BCW in other zones from 2022.

## Tests/commits/publish/status

- Rebuilt `SETs` and `data/params` in `/tmp/osecan_zonal`; `harmonize` exit 0 for base and all three scenario parameter sets.
- `osecan info` loaded the modified model (exit 0).
- Three GLPK solves returned `optimal`; the control reproduced the previous 1,371,553.35 M$ objective exactly.
- Focused tests: `python -m pytest -q workflows/national/clews/tests/test_osecan_zonal.py`.
- Committed only CLEWS artifacts, workflow code and tests; no commit was made to the public OSeCAN repository.
- `git status --porcelain` and any unexpected `D` are reported by the orchestrator after the commit.

## Blockers/next

1. The zonal B1/B2 boundary is the FRESH-side provisional crosswalk; it is not a C2070 official boundary.
2. The hydro cap is a sensitivity probe, not a hydro availability forecast.  A provincial hydro resource constraint or reservoir representation is still needed.
3. The generic-BIO sensitivity is a flat $4/GJ fuel cost, not a WS3/FABLE supply curve.  A dedicated power-biomass cap or supply curve would isolate the bypass more cleanly.
4. The model's gas and biomass costs remain v0.3 placeholders; replace them with Canadian values before drawing policy conclusions.
5. The zonal constraint raises emissions because B1/B2 biomass displaces local wind while gas remains in other zones.  A transmission-expansion or BC-export sensitivity would test whether that is a boundary artifact.
