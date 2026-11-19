# Full-backstop constraint test with a 20% per-zone wind cap (OSeCAN)

**Status:** FRESH-side provisional, not an official C2070 result.  
**Model:** disposable `/tmp/osecan_full_windcap`, a fresh copy of `/tmp/osecan_fullconstraint`; the source copy and the public OSeCAN repository are unchanged.  
**Basis:** tiered rest-of-Canada BCW supply curve, BC zonal caps, CO2 $200/t from 2026, 2021 hydro upper cap, corrected output-basis emission factors, single annual timeslice.

## 1. Caps (per-zone wind + existing)

| Lever | Technology | Value | Years | Source |
|---|---|---:|---|---|
| Power bioenergy | `PWRBIO<z>` (13 zones) | 5% of each zone's `efix_tier_200` 2050 generation; total **162.608451 PJ/yr** | 2021–2070 | `pwrbio_cap/pwrbio_caps.json` |
| Wind hard cap | `PWRWND<z>` (13 zones) | 20% of each zone's `efix_tier_200` 2050 activity; total **193.596136 PJ/yr** | 2021–2070 | `wind_integration_audit/wind_caps_20pct.json` |
| Wind integration cost | `PWRWND<z>` (13 zones) | variable cost **+$3/GJ** (retained from the existing case) | 2021–2070 | scenario adder |
| Nuclear | `PWRURN<z>` (13 zones) | **0 GW** in `TotalAnnualMaxCapacity` and `TotalAnnualMaxCapacityInvestment` | 2021–2070 | no new nuclear |
| High-cost biomass T4 | `SUPBCWT4` | **0 PJ/yr** | 2021–2070 | removes high-cost tier |
| Mid-cost biomass T3 (primary) | `SUPBCWT3` | **39.873714 PJ/yr** | 2021–2070 | kept |
| Mid-cost biomass T3 (optional case) | `SUPBCWT3` | **0 PJ/yr** | 2021–2070 | removes mid-cost tier |
| Rest-of-Canada T1 | `SUPBCWT1` | **85.007113 PJ/yr** | 2021–2070 | kept |
| Rest-of-Canada T2 | `SUPBCWT2` | **24.391750 PJ/yr** | 2021–2070 | kept |
| Rest-of-Canada T1+T2 | — | **109.398863 PJ/yr** | 2021–2070 | kept |
| BC zonal | `SUPBCWB1` / `SUPBCWB2` | adopted caps, **43.523816 PJ** from 2028 | 2021–2070 | kept |
| Non-power BIO | `RNWBIO` | **uncapped** | 2021–2070 | fixed non-power BIO demand |
| Carbon price | CO2 | **$200/t** from 2026 | 2026–2070 | scenario |
| Hydro | `PWRHYD<z>` | 2021 activity upper bound, held constant | 2021–2070 | scenario |

The hard wind cap is the new lever.  The existing +$3/GJ wind adder is retained, but the quantity cap binds before the adder can expand wind; the adder only prices the wind that remains inside the cap.

### Per-zone 20% wind caps

| Technology | Reference 2050 activity (PJ) | Cap (PJ/yr) |
|---|---:|---:|
| `PWRWNDA1` | 134.410738 | 26.882148 |
| `PWRWNDA2` | 70.416817 | 14.083363 |
| `PWRWNDB1` | 134.615443 | 26.923089 |
| `PWRWNDB2` | 34.463848 | 6.892770 |
| `PWRWNDL1` | 9.309792 | 1.861958 |
| `PWRWNDM1` | 18.195891 | 3.639178 |
| `PWRWNDN1` | 1.852812 | 0.370562 |
| `PWRWNDO1` | 270.431604 | 54.086321 |
| `PWRWNDO2` | 47.714049 | 9.542810 |
| `PWRWNDQ1` | 142.157026 | 28.431405 |
| `PWRWNDQ2` | 35.629091 | 7.125818 |
| `PWRWNDS1` | 39.947043 | 7.989409 |
| `PWRWNDT1` | 28.836524 | 5.767305 |
| **Total** | **967.980678** | **193.596136** |

### Per-zone 5% PWRBIO caps

| Technology | Reference 2050 generation (PJ) | 5% cap (PJ/yr) |
|---|---:|---:|
| `PWRBIOA1` | 333.153069 | 16.657653 |
| `PWRBIOA2` | 179.389875 | 8.969494 |
| `PWRBIOB1` | 323.021655 | 16.151083 |
| `PWRBIOB2` | 107.673774 | 5.383689 |
| `PWRBIOL1` | 49.238823 | 2.461941 |
| `PWRBIOM1` | 106.485741 | 5.324287 |
| `PWRBION1` | 8.728152 | 0.436408 |
| `PWRBIOO1` | 740.654604 | 37.032730 |
| `PWRBIOO2` | 130.703721 | 6.535186 |
| `PWRBIOQ1` | 812.373147 | 40.618657 |
| `PWRBIOQ2` | 203.093149 | 10.154657 |
| `PWRBIOS1` | 126.146838 | 6.307342 |
| `PWRBIOT1` | 131.506473 | 6.575324 |
| **Total** | **3252.169021** | **162.608451** |

## 2. Result (objective, emissions, dispatch, tiers)

| Case | Status | Objective (M$) | Emissions total (Mt) | Emissions 2050 (Mt) | Gas total (PJ) | Gas 2050 (PJ) | Wind 2050 (PJ) | Hydro 2050 (PJ) | Nuclear 2050 (PJ) | BIO 2050 (PJ) | PWRBCW 2050 (PJ) | T1 total (PJ) | T2 total (PJ) | T3 total (PJ) | T4 total (PJ) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `full_windcap20_t4zero` | optimal | 1,410,717.32 | 0.523856 | 0.000000 | 3.804 | 0.000 | 193.60 | 2230.55 | 0.00 | 162.61 | 51.83 | 4096.94 | 1082.67 | 1598.59 | 0.00 |
| `full_windcap20_t3t4zero` | optimal | 1,411,456.31 | 0.538720 | 0.000000 | 3.912 | 0.000 | 193.60 | 2230.55 | 0.00 | 162.61 | 41.11 | 4046.29 | 1099.03 | 0.00 | 0.00 |

Dispatch by key year:

### `full_windcap20_t4zero`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Solar | Geo | Coal | BSW | Nuclear | Generation | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 0.00 | 0.00 | 2230.55 | 0.13 | 0.21 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2230.88 | 0.000000 |
| 2025 | 0.00 | 0.00 | 2230.32 | 9.13 | 25.65 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2265.11 | 0.000000 |
| 2028 | 0.00 | 0.00 | 2230.55 | 44.16 | 35.91 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2310.61 | 0.000000 |
| 2030 | 12.46 | 0.00 | 2230.55 | 129.42 | 41.33 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2413.76 | 0.000000 |
| 2040 | 193.60 | 0.00 | 2230.55 | 162.61 | 51.83 | 237.81 | 0.00 | 0.00 | 13.44 | 0.00 | 2889.83 | 0.000000 |
| 2050 | 193.60 | 0.00 | 2230.55 | 162.61 | 51.83 | 600.15 | 0.00 | 0.00 | 13.44 | 0.00 | 3252.17 | 0.000000 |
| 2060 | 193.60 | 0.00 | 2230.55 | 162.61 | 51.83 | 600.15 | 0.00 | 0.00 | 13.44 | 0.00 | 3252.17 | 0.000000 |
| 2070 | 193.60 | 0.00 | 2230.55 | 162.61 | 51.83 | 600.15 | 0.00 | 0.00 | 13.44 | 0.00 | 3252.17 | 0.000000 |

Tier totals (PJ): T1 4096.94, T2 1082.67, T3 1598.59, T4 0.00.  Binding: T1 yes, T2 yes, T3 yes, T4 no.  PWRBCW split 2050: BC 11.70 PJ, rest of Canada 40.13 PJ.
Wind caps bind in 13 of 13 zones, from 2033 to 2070; 2050 wind is 193.596122 PJ against the 193.596136 PJ total cap (100.00% utilisation).
PWRBIO caps bind in 13 of 13 zones, from 2028 to 2070; 2050 output is 162.608568 PJ against the 162.608451 PJ total cap.
Hydro 2021 upper caps bind in 13 of 13 zones, from 2021 to 2070; 2050 hydro is 2230.55 PJ.
BC zonal caps: `SUPBCWB1` binds (first 2026), `SUPBCWB2` binds (first 2031); 2050 activity is 43.523770 PJ against the 43.523816 PJ zonal cap total.  National BCW supply is 192.796270 PJ and PWRBCW fuel input is 192.796273 PJ (balance residual 0.000007 PJ).

| Wind zone | 2050 activity (PJ) | Cap (PJ/yr) | Utilisation | First binding year |
|---|---:|---:|---:|---:|
| `PWRWNDA1` | 26.882100 | 26.882148 | 100.00% | 2036 |
| `PWRWNDA2` | 14.083400 | 14.083363 | 100.00% | 2036 |
| `PWRWNDB1` | 26.923100 | 26.923089 | 100.00% | 2033 |
| `PWRWNDB2` | 6.892770 | 6.892770 | 100.00% | 2035 |
| `PWRWNDL1` | 1.861960 | 1.861958 | 100.00% | 2036 |
| `PWRWNDM1` | 3.639180 | 3.639178 | 100.00% | 2037 |
| `PWRWNDN1` | 0.370562 | 0.370562 | 100.00% | 2036 |
| `PWRWNDO1` | 54.086300 | 54.086321 | 100.00% | 2035 |
| `PWRWNDO2` | 9.542810 | 9.542810 | 100.00% | 2036 |
| `PWRWNDQ1` | 28.431400 | 28.431405 | 100.00% | 2036 |
| `PWRWNDQ2` | 7.125820 | 7.125818 | 100.00% | 2036 |
| `PWRWNDS1` | 7.989410 | 7.989409 | 100.00% | 2035 |
| `PWRWNDT1` | 5.767310 | 5.767305 | 100.00% | 2036 |

### `full_windcap20_t3t4zero`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Solar | Geo | Coal | BSW | Nuclear | Generation | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 0.00 | 0.00 | 2230.55 | 0.07 | 0.27 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2230.88 | 0.000000 |
| 2025 | 0.00 | 0.00 | 2230.32 | 10.83 | 23.96 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2265.11 | 0.000000 |
| 2028 | 0.00 | 0.00 | 2230.55 | 44.17 | 35.91 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2310.63 | 0.000000 |
| 2030 | 12.82 | 0.00 | 2230.55 | 130.07 | 40.35 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2413.78 | 0.000000 |
| 2040 | 193.60 | 0.00 | 2230.55 | 162.61 | 41.11 | 248.53 | 0.00 | 0.00 | 13.44 | 0.00 | 2889.83 | 0.000000 |
| 2050 | 193.60 | 0.00 | 2230.55 | 162.61 | 41.11 | 610.87 | 0.00 | 0.00 | 13.44 | 0.00 | 3252.17 | 0.000000 |
| 2060 | 193.60 | 0.00 | 2230.55 | 162.61 | 41.11 | 610.87 | 0.00 | 0.00 | 13.44 | 0.00 | 3252.17 | 0.000000 |
| 2070 | 193.60 | 0.00 | 2230.55 | 162.61 | 41.11 | 610.87 | 0.00 | 0.00 | 13.44 | 0.00 | 3252.17 | 0.000000 |

Tier totals (PJ): T1 4046.29, T2 1099.03, T3 0.00, T4 0.00.  Binding: T1 yes, T2 yes, T3 no, T4 no.  PWRBCW split 2050: BC 11.70 PJ, rest of Canada 29.41 PJ.
Wind caps bind in 13 of 13 zones, from 2033 to 2070; 2050 wind is 193.596122 PJ against the 193.596136 PJ total cap (100.00% utilisation).
PWRBIO caps bind in 13 of 13 zones, from 2029 to 2070; 2050 output is 162.608568 PJ against the 162.608451 PJ total cap.
Hydro 2021 upper caps bind in 13 of 13 zones, from 2021 to 2070; 2050 hydro is 2230.55 PJ.
BC zonal caps: `SUPBCWB1` binds (first 2026), `SUPBCWB2` binds (first 2031); 2050 activity is 43.523770 PJ against the 43.523816 PJ zonal cap total.  National BCW supply is 152.922570 PJ and PWRBCW fuel input is 152.922571 PJ (balance residual 0.000005 PJ).

| Wind zone | 2050 activity (PJ) | Cap (PJ/yr) | Utilisation | First binding year |
|---|---:|---:|---:|---:|
| `PWRWNDA1` | 26.882100 | 26.882148 | 100.00% | 2036 |
| `PWRWNDA2` | 14.083400 | 14.083363 | 100.00% | 2036 |
| `PWRWNDB1` | 26.923100 | 26.923089 | 100.00% | 2033 |
| `PWRWNDB2` | 6.892770 | 6.892770 | 100.00% | 2035 |
| `PWRWNDL1` | 1.861960 | 1.861958 | 100.00% | 2036 |
| `PWRWNDM1` | 3.639180 | 3.639178 | 100.00% | 2037 |
| `PWRWNDN1` | 0.370562 | 0.370562 | 100.00% | 2036 |
| `PWRWNDO1` | 54.086300 | 54.086321 | 100.00% | 2035 |
| `PWRWNDO2` | 9.542810 | 9.542810 | 100.00% | 2035 |
| `PWRWNDQ1` | 28.431400 | 28.431405 | 100.00% | 2036 |
| `PWRWNDQ2` | 7.125820 | 7.125818 | 100.00% | 2036 |
| `PWRWNDS1` | 7.989410 | 7.989409 | 100.00% | 2035 |
| `PWRWNDT1` | 5.767310 | 5.767305 | 100.00% | 2036 |

## 3. Comparison to uncapped-wind and nuclear-cap cases

| Case | Objective (M$) | Emissions total (Mt) | Gas total (PJ) | Gas 2050 (PJ) | Wind 2050 (PJ) | Nuclear 2050 (PJ) | BIO 2050 (PJ) | PWRBCW 2050 (PJ) | T3 total (PJ) | T4 total (PJ) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `efix_tier_200` | 1,371,773.03 | 0.460752 | 3.346 | 0.000 | 967.98 | 0.00 | 12.53 | 41.11 | 0.00 | 0.00 |
| `nuclear_cap0_pwrbio5_wind3` | 1,387,922.37 | 0.465597 | 3.381 | 0.000 | 789.91 | 0.00 | 162.61 | 69.10 | 1610.71 | 2531.55 |
| `nuclear_cap10gw_pwrbio5_wind3` | 1,385,098.46 | 0.496039 | 3.602 | 0.000 | 506.09 | 283.82 | 162.61 | 69.10 | 1610.82 | 2142.21 |
| `fullconstraint_t4zero` | 1,387,944.73 | 0.465597 | 3.381 | 0.000 | 807.19 | 0.00 | 162.61 | 51.83 | 1610.71 | 0.00 |
| `fullconstraint_t3t4zero` | 1,388,092.40 | 0.465597 | 3.381 | 0.000 | 817.91 | 0.00 | 162.61 | 41.11 | 0.00 | 0.00 |
| `full_windcap20_t4zero` | 1,410,717.32 | 0.523856 | 3.804 | 0.000 | 193.60 | 0.00 | 162.61 | 51.83 | 1598.59 | 0.00 |
| `full_windcap20_t3t4zero` | 1,411,456.31 | 0.538720 | 3.912 | 0.000 | 193.60 | 0.00 | 162.61 | 41.11 | 0.00 | 0.00 |

## 4. Verdict (gas return? remaining backstop?)

- **Does gas return?** No. 2050 gas is **0.000 PJ** and post-2026 gas is **0.464 PJ**, all a sub-petajoule 2036–2042 trace; the remaining 3.340 PJ is the 2022/2024 commissioning residual.  Gas capacity in 2050 is 0.124 GW, but it carries no 2050 activity.  Gas-attributable CO2 is about 0.524 Mt over 2021–2070 (0.000 Mt in 2050); total emissions are **0.523856 Mt**, slightly above the 0.465597 Mt of `fullconstraint_t4zero` because of the pre-2026 commissioning gas, not because of new gas generation.  The objective rises from 1,387,944.73 M$ to 1,410,717.32 M$ (+22,772.59 M$, 1.64%).

- **Remaining uncapped option.** **solar PV** is the backstop.  2050 solar is **600.150 PJ** (17056.79 PJ over the horizon) and 2050 BSW is 13.441 PJ (497.31 PJ over the horizon).  The 20% cap removes 613.591 PJ of 2050 wind relative to `fullconstraint_t4zero` (807.187 PJ down to 193.596 PJ); solar fills that gap.  Hydro is at its 2021 upper cap, PWRBIO at 5%, T1/T2/T3 at their caps, BC zonal at its caps, and nuclear at zero.  Gas does not return because solar is cheaper than $200/t gas in this single-timeslice model.  If solar and BSW were also capped, gas would be the next uncapped option; that case is not tested here.

- **Optional T3/T4-zero case.** 2050 gas is 0.000 PJ, post-2026 gas is 0.464 PJ, emissions total 0.538720 Mt, 2050 solar is 610.869 PJ, and 2050 wind is 193.596 PJ.  Removing T3 raises 2050 solar by 10.719 PJ relative to the primary case and changes total emissions by +0.014864 Mt; gas remains zero in 2050.

## 5. Tests/commits/publish/status

Tests are recorded in `tests.json`: cap loading (per-zone wind, PWRBIO, nuclear, tier and BC zonal caps), dispatch reconciliation (generation sum, BCW balance, non-power BIO, wind/PWRBIO/nuclear caps), tier caps, and `osecan harmonize`.  All tests passed.

Artifacts are written under `data/derived/national/clews/osecan/full_windcap/` in the `data` submodule and committed with the parent pointer in `clews-c2070-fresh`; both are pushed to their `feature/osecan-zonal-bc-supply` branches.  The public OSeCAN model repository is not modified.  `git status --porcelain` and any `D` entries are reported in the task response.

## 6. Caveats

- The 20% wind cap is a scenario assumption derived from each zone's 2050 activity in the post-fix `$200/t` reference, not a measured integration limit.  It is held constant 2021–2070 and does not vary with demand or grid conditions.
- The +$3/GJ wind adder is a scenario stress, retained from the existing full-constraint case.  With the hard cap binding, it prices but does not expand wind.
- The 5% PWRBIO cap is a scenario assumption, not policy.
- Nuclear is capped at 0 GW in every year; existing Canadian nuclear capacity is not represented as residual capacity.  All `PWRURN` build is new capacity.
- T3/T4 are documented scenario supply tiers, not empirical marginal costs.
- `RNWBIO` is uncapped and continues to supply fixed non-power BIO demand; only power bioenergy is capped.
- Gas is uncapped: no gas resource, import, build-rate, or capacity limit applies.
- Single annual timeslice (`ANN`): no diurnal/seasonal balancing, ramping, curtailment, reserve margin, firm-capacity, transmission, or build-rate constraint.
- Solver: GLPK via swiglpk 5.0.13.  Results are for the disposable model copy only.

