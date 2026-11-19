# Full-backstop constraint test (OSeCAN)

**Status:** FRESH-side provisional, not an official C2070 result.  
**Model:** disposable `/tmp/osecan_fullconstraint`, copied from `/tmp/osecan_emfix` with the corrected output-basis emission factors.  
**Basis:** tiered rest-of-Canada BCW supply curve, BC zonal caps, CO2 $200/t from 2026, 2021 hydro upper cap, single annual timeslice.

## 1. Constraint set (exact caps)

| Lever | Technology | Value | Years | Source |
|---|---|---:|---|---|
| Power bioenergy | `PWRBIO<z>` (13 zones) | 5% of each zone's `efix_tier_200` 2050 generation; total **162.608451 PJ/yr** | 2021–2070 | `pwrbio_cap/pwrbio_caps.json` |
| Wind integration | `PWRWND<z>` (13 zones) | variable cost **+$3/GJ** | 2021–2070 | scenario adder |
| Nuclear | `PWRURN<z>` (13 zones) | **0 GW** in `TotalAnnualMaxCapacity` and `TotalAnnualMaxCapacityInvestment` | 2021–2070 | no new nuclear |
| High-cost biomass T4 | `SUPBCWT4` | **0 PJ/yr** | 2021–2070 | removes high-cost tier |
| High-cost biomass T3 (optional case) | `SUPBCWT3` | **0 PJ/yr** | 2021–2070 | removes mid-cost tier |
| Rest-of-Canada T1 | `SUPBCWT1` | **85.007113 PJ/yr** | 2021–2070 | kept |
| Rest-of-Canada T2 | `SUPBCWT2` | **24.391750 PJ/yr** | 2021–2070 | kept |
| Rest-of-Canada T1+T2 | — | **109.398863 PJ/yr** | 2021–2070 | kept |
| BC zonal | `SUPBCWB1` / `SUPBCWB2` | adopted caps, **43.523816 PJ** from 2028 | 2021–2070 | kept |
| Non-power BIO | `RNWBIO` | **uncapped** | 2021–2070 | fixed non-power BIO demand |

The primary case keeps T3 (39.873714 PJ/yr) and removes T4.  The optional case removes both T3 and T4, so T1/T2 plus the BC zonal stack are the only biomass power supply.  The wind lever is the **+$3/GJ cost adder**, not the alternative 20% wind cap.

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

## 2. Result

| Case | Status | Objective (M$) | Emissions total (Mt) | Emissions 2050 (Mt) | Gas total (PJ) | Gas 2050 (PJ) | Wind 2050 (PJ) | Hydro 2050 (PJ) | Nuclear 2050 (PJ) | BIO 2050 (PJ) | PWRBCW 2050 (PJ) | T3 total (PJ) | T4 total (PJ) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `fullconstraint_t4zero` | optimal | 1387944.73 | 0.465597 | 0.000000 | 3.381 | 0.00 | 807.19 | 2230.55 | 0.00 | 162.61 | 51.83 | 1610.71 | 0.00 |
| `fullconstraint_t3t4zero` | optimal | 1388092.40 | 0.465597 | 0.000000 | 3.381 | 0.00 | 817.91 | 2230.55 | 0.00 | 162.61 | 41.11 | 0.00 | 0.00 |

Dispatch by key year:

### `fullconstraint_t4zero`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Generation | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 0.00 | 0.00 | 2230.55 | 0.13 | 0.21 | 0.00 | 2230.88 | 0.000000 |
| 2025 | 0.00 | 0.00 | 2230.32 | 6.04 | 28.76 | 0.00 | 2265.12 | 0.000000 |
| 2028 | 0.00 | 0.00 | 2230.55 | 44.17 | 35.91 | 0.00 | 2310.63 | 0.000000 |
| 2030 | 12.35 | 0.00 | 2230.55 | 126.32 | 44.53 | 0.00 | 2413.75 | 0.000000 |
| 2040 | 444.85 | 0.00 | 2230.55 | 162.61 | 51.83 | 0.00 | 2889.83 | 0.000000 |
| 2050 | 807.19 | 0.00 | 2230.55 | 162.61 | 51.83 | 0.00 | 3252.17 | 0.000000 |
| 2060 | 807.19 | 0.00 | 2230.55 | 162.61 | 51.83 | 0.00 | 3252.17 | 0.000000 |
| 2070 | 807.19 | 0.00 | 2230.55 | 162.61 | 51.83 | 0.00 | 3252.17 | 0.000000 |

Tier totals (PJ): T1 4090.78, T2 1146.41, T3 1610.71, T4 0.00.  Binding: T1 yes, T2 yes, T3 yes, T4 no.  PWRBCW split 2050: BC 11.70 PJ, rest of Canada 40.13 PJ.
PWRBIO caps bind in 13 of 13 zones, first from 2028 to 2034; 2050 output is 162.608568 PJ against the 162.608451 PJ total cap (solver rounding only).  BC zonal caps: `SUPBCWB1` binds (first 2026), `SUPBCWB2` binds (first 2031); 2050 activity is 43.523770 PJ against the 43.523816 PJ zonal cap total.  National BCW supply is 192.796270 PJ and PWRBCW fuel input is 192.796269 PJ (balance residual 0.000005 PJ).

### `fullconstraint_t3t4zero`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Generation | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 0.00 | 0.00 | 2230.55 | 0.13 | 0.21 | 0.00 | 2230.88 | 0.000000 |
| 2025 | 0.00 | 0.00 | 2230.32 | 9.08 | 25.70 | 0.00 | 2265.10 | 0.000000 |
| 2028 | 0.00 | 0.00 | 2230.55 | 44.17 | 35.91 | 0.00 | 2310.63 | 0.000000 |
| 2030 | 13.41 | 0.00 | 2230.55 | 129.51 | 40.29 | 0.00 | 2413.75 | 0.000000 |
| 2040 | 455.56 | 0.00 | 2230.55 | 162.61 | 41.11 | 0.00 | 2889.83 | 0.000000 |
| 2050 | 817.91 | 0.00 | 2230.55 | 162.61 | 41.11 | 0.00 | 3252.17 | 0.000000 |
| 2060 | 817.91 | 0.00 | 2230.55 | 162.61 | 41.11 | 0.00 | 3252.17 | 0.000000 |
| 2070 | 817.91 | 0.00 | 2230.55 | 162.61 | 41.11 | 0.00 | 3252.17 | 0.000000 |

Tier totals (PJ): T1 4025.47, T2 1154.88, T3 0.00, T4 0.00.  Binding: T1 yes, T2 yes, T3 no, T4 no.  PWRBCW split 2050: BC 11.70 PJ, rest of Canada 29.41 PJ.
PWRBIO caps bind in 13 of 13 zones, first from 2028 to 2034; 2050 output is 162.608568 PJ against the 162.608451 PJ total cap (solver rounding only).  BC zonal caps: `SUPBCWB1` binds (first 2026), `SUPBCWB2` binds (first 2031); 2050 activity is 43.523770 PJ against the 43.523816 PJ zonal cap total.  National BCW supply is 152.922570 PJ and PWRBCW fuel input is 152.922567 PJ (balance residual 0.000005 PJ).

## 3. Comparison to uncapped stress and nuclear-cap cases

| Case | Objective (M$) | Emissions total (Mt) | Gas total (PJ) | Gas 2050 (PJ) | Wind 2050 (PJ) | Nuclear 2050 (PJ) | BIO 2050 (PJ) | PWRBCW 2050 (PJ) | T3 total (PJ) | T4 total (PJ) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `efix_tier_200` | 1371773.03 | 0.460752 | 3.346 | 0.00 | 967.98 | 0.00 | 12.53 | 41.11 | 0.00 | 0.00 |
| `pwrbio_cap5_windint3_tier200` | 1382042.24 | 0.489886 | 3.558 | 0.00 | 0.00 | 807.19 | 162.61 | 51.83 | 1613.44 | 0.00 |
| `nuclear_cap0_pwrbio5_wind3` | 1387922.37 | 0.465597 | 3.381 | 0.00 | 789.91 | 0.00 | 162.61 | 69.10 | 1610.71 | 2531.55 |
| `nuclear_cap10gw_pwrbio5_wind3` | 1385098.46 | 0.496039 | 3.602 | 0.00 | 506.09 | 283.82 | 162.61 | 69.10 | 1610.82 | 2142.21 |
| `fullconstraint_t4zero` | 1387944.73 | 0.465597 | 3.381 | 0.00 | 807.19 | 0.00 | 162.61 | 51.83 | 1610.71 | 0.00 |
| `fullconstraint_t3t4zero` | 1388092.40 | 0.465597 | 3.381 | 0.00 | 817.91 | 0.00 | 162.61 | 41.11 | 0.00 | 0.00 |

## 4. Verdict

- **Does gas return?** No.  2050 gas is 0.00 PJ in both full-constraint cases.  All-years gas is 3.381 PJ in each case: 3.307 PJ in 2022–2024, 0.074 PJ in 2037/2042, and zero in 2050.  This is the reference pre-2026 residual plus a negligible mid-century trace, not gas-fired baseload.  Emissions total 0.465597 Mt, of which 97.8% is in 2022–2024; 2050 emissions are zero.

- **Which remaining option fills the gap?** In the primary case, wind rises to 807.19 PJ at 2050 and T3 binds at 1610.71 PJ over the horizon. In the optional case, wind rises to 817.91 PJ and PWRBCW falls to 41.11 PJ because T3/T4 are unavailable. All 13 PWRBIO caps, T1, T2 and the BC zonal caps bind; the biomass supply stack is fully used (192.80 PJ in the primary, 152.92 PJ in the optional case).  The +$3/GJ adder does not suppress wind, which remains cheaper than $200/t gas and the high-cost biomass tiers.  Uncapped wind is the remaining zero-carbon backstop.

- **Comparison to the nuclear-only cap.** The nuclear-cap case (`nuclear_cap0_pwrbio5_wind3`) had 2050 wind 789.91 PJ and T4 2531.55 PJ. Removing T4 raises wind to 807.19 PJ; removing T3 as well raises it to 817.91 PJ.  Emissions stay near zero because wind and the remaining biomass supply are zero-carbon.

- **Comparison to the uncapped stress.** `efix_tier_200` had objective 1371773.03 M$, emissions 0.460752 Mt, 2050 wind 967.98 PJ, and no nuclear.  The full constraint set costs 16171.70 M$ more (T4=0) and 16319.37 M$ more (T3=T4=0), about 1.18% and 1.19% respectively.

The combined constraints do not expose a gas margin in this model.  They replace nuclear and high-cost biomass with uncapped wind.  A 20% wind cap, a wind build limit, or a firm-capacity/reserve constraint would be required to test whether gas returns; the +$3/GJ case used here is not sufficient.

## 5. Tests/commits/publish/status

Tests are recorded in `tests.json`: cap loading, dispatch reconciliation, tier caps, and `osecan harmonize`.  Artifacts are committed in the `data` submodule and the parent pointer is committed in `clews-c2070-fresh`; neither the public OSeCAN model nor the disposable source copy is modified.

## 6. Caveats

- The 5% PWRBIO cap is a scenario assumption based on each zone's 2050 generation in `efix_tier_200`, not policy.
- The +$3/GJ wind adder is a scenario stress, not a measured integration cost; the model has no wind build limit, curtailment, or grid constraint.
- Nuclear is capped at 0 GW in every year.  Existing Canadian nuclear capacity is not represented as residual capacity; all `PWRURN` build is new capacity.
- T4 (and T3 in the optional case) are documented scenario supply tiers, not empirical marginal costs.
- `RNWBIO` is uncapped and continues to supply fixed non-power BIO demand; only power bioenergy is capped.
- Single annual timeslice (`ANN`): no diurnal/seasonal balancing, ramping, reserve margin, or firm-capacity constraint.
- Solver: GLPK via swiglpk 5.0.13.  Results are for the disposable model copy only.

