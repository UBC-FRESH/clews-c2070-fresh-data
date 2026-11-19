# Nuclear-cap backstop audit (OSeCAN)

**Status:** FRESH-side provisional, not an official C2070 result.  
**Model:** disposable `/tmp/osecan_nuclear_audit`, copied from `/tmp/osecan_emfix` with the corrected output-basis emission factors.  
**Stress:** tiered national BCW curve, CO2 $200/t from 2026, 2021 hydro upper cap, 5%-of-zone-generation `PWRBIO<z>` cap, +$3/GJ on every `PWRWND<z>`, BC zonal caps unchanged.

## 1. What was capped

`PWRURN<z>` has no activity cap, no residual capacity, and no build-rate limit in the model.  The audit adds both `TotalAnnualMaxCapacity` and `TotalAnnualMaxCapacityInvestment` for all 13 `PWRURN<z>` technologies in every year 2021-2070.  Values are in GW.  `PWRURN` residual capacity is zero in 2021, so the annual total-capacity bound is the binding representation; the investment bound is set to the same value and is non-additional.

| Case | Nuclear cap | Basis |
|---|---:|---|
| `nuclear_cap0_pwrbio5_wind3` | 0 GW | all 13 zones zero in every year |
| `nuclear_cap10gw_pwrbio5_wind3` | 10 GW | national cap allocated by each zone's share of the uncapped stacked-case 2050 nuclear dispatch |
| `nuclear_cap0_tier200_reference` | 0 GW | no wind adder, no PWRBIO cap; isolates the nuclear cap |

The 10 GW allocation is a labelled scenario, not a forecast or a current-fleet estimate.  The model's `PWRURN` residual capacity is zero, so the 10 GW bound is new-build capacity.

### Per-zone 10 GW allocation

| Technology | Reference 2050 nuclear (PJ) | Share | 10 GW cap (GW) |
|---|---:|---:|---:|
| `PWRURNA1` | 107.009035 | 0.132570 | 1.325703 |
| `PWRURNA2` | 54.898813 | 0.068012 | 0.680125 |
| `PWRURNB1` | 118.464343 | 0.146762 | 1.467619 |
| `PWRURNB2` | 29.080158 | 0.036027 | 0.360265 |
| `PWRURNL1` | 6.746843 | 0.008358 | 0.083585 |
| `PWRURNM1` | 13.099151 | 0.016228 | 0.162281 |
| `PWRURNN1` | 1.581084 | 0.001959 | 0.019588 |
| `PWRURNO1` | 233.398904 | 0.289151 | 2.891508 |
| `PWRURNO2` | 41.178859 | 0.051015 | 0.510153 |
| `PWRURNQ1` | 116.151189 | 0.143896 | 1.438962 |
| `PWRURNQ2` | 28.491191 | 0.035297 | 0.352969 |
| `PWRURNS1` | 32.461659 | 0.040216 | 0.402158 |
| `PWRURNT1` | 24.625999 | 0.030508 | 0.305084 |
| **Total** | **807.187228** | **1.000000** | **10.000000** |

## 2. Headline results

| Case | Objective (M$) | Emissions total (Mt) | Emissions 2050 (Mt) | Gas 2050 (PJ) | Wind 2050 (PJ) | Hydro 2050 (PJ) | Nuclear 2050 (PJ) | BIO 2050 (PJ) | PWRBCW 2050 (PJ) | T3 total (PJ) | T4 active |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `nuclear_cap0_pwrbio5_wind3` | 1387922.37 | 0.465597 | 0.000000 | 0.00 | 789.91 | 2230.55 | 0.00 | 162.61 | 69.10 | 1610.71 | yes |
| `nuclear_cap10gw_pwrbio5_wind3` | 1385098.46 | 0.496039 | 0.000000 | 0.00 | 506.09 | 2230.55 | 283.82 | 162.61 | 69.10 | 1610.82 | yes |
| `nuclear_cap0_tier200_reference` | 1371773.03 | 0.460752 | 0.000000 | 0.00 | 967.98 | 2230.55 | 0.00 | 12.53 | 41.11 | 0.00 | no |

## 3. Dispatch by key year

### `nuclear_cap0_pwrbio5_wind3`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Generation | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 0.00 | 0.00 | 2230.55 | 0.13 | 0.21 | 0.00 | 2230.88 | 0.000000 |
| 2025 | 0.00 | 0.00 | 2230.32 | 6.04 | 28.76 | 0.00 | 2265.12 | 0.000000 |
| 2028 | 0.00 | 0.00 | 2230.55 | 44.17 | 35.91 | 0.00 | 2310.63 | 0.000000 |
| 2030 | 12.35 | 0.00 | 2230.55 | 126.32 | 44.53 | 0.00 | 2413.75 | 0.000000 |
| 2040 | 427.57 | 0.00 | 2230.55 | 162.61 | 69.10 | 0.00 | 2889.83 | 0.000000 |
| 2050 | 789.91 | 0.00 | 2230.55 | 162.61 | 69.10 | 0.00 | 3252.17 | 0.000000 |
| 2060 | 789.91 | 0.00 | 2230.55 | 162.61 | 69.10 | 0.00 | 3252.17 | 0.000000 |
| 2070 | 789.91 | 0.00 | 2230.55 | 162.61 | 69.10 | 0.00 | 3252.17 | 0.000000 |

Nuclear capacity: 2050 0.000 GW, max 0.000 GW; cap binding: False (None–None).

### `nuclear_cap10gw_pwrbio5_wind3`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Generation | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 0.00 | 0.00 | 2230.55 | 0.13 | 0.21 | 0.00 | 2230.88 | 0.000000 |
| 2025 | 0.00 | 0.00 | 2230.32 | 5.78 | 29.00 | 0.00 | 2265.11 | 0.000000 |
| 2028 | 0.00 | 0.00 | 2230.55 | 44.14 | 35.91 | 0.00 | 2310.60 | 0.000000 |
| 2030 | 0.00 | 0.00 | 2230.55 | 126.05 | 44.49 | 12.64 | 2413.73 | 0.000000 |
| 2040 | 144.62 | 0.00 | 2230.55 | 162.61 | 69.10 | 282.95 | 2889.83 | 0.000000 |
| 2050 | 506.09 | 0.00 | 2230.55 | 162.61 | 69.10 | 283.82 | 3252.17 | 0.000000 |
| 2060 | 506.09 | 0.00 | 2230.55 | 162.61 | 69.10 | 283.82 | 3252.17 | 0.000000 |
| 2070 | 506.09 | 0.00 | 2230.55 | 162.61 | 69.10 | 283.82 | 3252.17 | 0.000000 |

Nuclear capacity: 2050 10.000 GW, max 10.000 GW; cap binding: True (2041–2070).

### `nuclear_cap0_tier200_reference`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Generation | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 0.00 | 0.00 | 2230.55 | 0.34 | 0.00 | 0.00 | 2230.88 | 0.000000 |
| 2025 | 8.82 | 0.00 | 2230.32 | 0.43 | 25.59 | 0.00 | 2265.16 | 0.000000 |
| 2028 | 38.08 | 0.00 | 2230.55 | 6.10 | 35.91 | 0.00 | 2310.64 | 0.000000 |
| 2030 | 130.33 | 0.00 | 2230.55 | 12.53 | 40.22 | 0.00 | 2413.63 | 0.000000 |
| 2040 | 605.64 | 0.00 | 2230.55 | 12.53 | 41.11 | 0.00 | 2889.83 | 0.000000 |
| 2050 | 967.98 | 0.00 | 2230.55 | 12.53 | 41.11 | 0.00 | 3252.17 | 0.000000 |
| 2060 | 980.51 | 0.00 | 2230.55 | 0.00 | 41.11 | 0.00 | 3252.17 | 0.000000 |
| 2070 | 980.51 | 0.00 | 2230.55 | 0.00 | 41.11 | 0.00 | 3252.17 | 0.000000 |

Nuclear capacity: 2050 0.000 GW, max 0.000 GW; cap binding: False (None–None).

## 4. Verdict

- **Does gas return?** No.  2050 gas is 0.00 PJ in both nuclear-capped stress cases.  All-years gas is 3.381 PJ with no nuclear and 3.602 PJ at the 10 GW cap, versus 3.558 PJ in the uncapped control.  Nothing resembling a gas backstop appears; the gas that does run is the same small pre-2026 residual as in the reference.
- **Do T3/T4 activate?** Yes.  T3 is binding in all stress cases.  T4 is binding too once nuclear is capped: T4 activity totals 2531.55 PJ (no nuclear) and 2142.21 PJ (10 GW), versus 0 PJ in the uncapped control.  2050 PWRBCW rises from 51.83 PJ to 69.10 PJ because the T3+T4 stack feeds more biomass power; the national BCW supply is fully used.
- **Is the near-zero result dependent on uncapped nuclear?** No, not in this model.  With nuclear at zero, 2050 wind rises to 789.91 PJ and T4 supplies the rest; emissions total 0.465597 Mt and 2050 emissions are zero.  At 10 GW, 2050 nuclear is 283.82 PJ, wind 506.09 PJ, and emissions total 0.496039 Mt.  The near-zero outcome is therefore robust to capping nuclear, but it is still dependent on other uncapped or high-tier zero-carbon options: wind has no MW build limit, and T3/T4 biomass is a scenario supply curve.  The audit replaces one zero-carbon backstop (nuclear) with wind plus the high-cost biomass tier, rather than exposing a gas margin.
- **Reference-with-cap control.** The $200/t reference has zero nuclear dispatch, so the zero-nuclear cap leaves it unchanged: objective 1371773.03 M$, emissions 0.460752 Mt (identical to `efix_tier_200`).  This confirms that the stress result, not the cap alone, is what creates the nuclear/wind/T4 substitution.

## 5. Caveats

- The 0 GW and 10 GW caps are scenario assumptions, not policy.  The 10 GW national cap is allocated across zonal `PWRURN` technologies by their uncapped stacked-case 2050 shares; the model has no national nuclear technology.
- The model has a single annual timeslice (`ANN`): no diurnal/seasonal balancing, ramping, curtailment, reserve margin, or firm-capacity constraint.
- There is no nuclear build-rate limit, fuel-chain constraint, or endogenous construction lead time beyond the annual capacity bound.
- Existing Canadian nuclear capacity is not represented as residual capacity in this model; all `PWRURN` build is new capacity.
- The BCW tiers, BC zonal caps, corrected EAR, PWRBIO 5% cap and +$3/GJ wind adder are unchanged from the audited stress case.
- Solver: GLPK via swiglpk 5.0.13.  Results are for the disposable model copy only.

