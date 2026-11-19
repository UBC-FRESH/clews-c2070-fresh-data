# PWRBIO cap: constraining the generic power-biomass backstop

**Status:** FRESH-side provisional, not an official C2070 result.  
**Model:** disposable `/tmp/osecan_pwrbio_cap`, copied from `/tmp/osecan_emfix` with the corrected output-basis emission factors.  
**Basis:** tiered national BCW supply curve, CO2 $200/t from 2026, hydro capped at the reference run's 2021 activity, single annual timeslice.

## 1. What was capped

The primary cap is **5% of each zone's total 2050 generation in the post-fix $200 reference run** (`efix_tier_200`).  Generation is every `PWR*` technology except `PWRTRN` transmission.  The cap is applied to each `PWRBIO<z>` annual activity in every year 2021–2070.  `RNWBIO` is **not** capped, so non-power BIO demand is unchanged.  The BCW tier caps and the BC zonal caps are unchanged.

This is a share cap, not a 5% haircut of observed bio output: the national cap total is 162.61 PJ, about 12.97× the reference 2050 bio dispatch.  In the plain $200 case it only binds in zone N1.  The wind-penalty diagnostic is therefore the informative test.

### Per-zone caps

| Zone | Ref 2050 generation | Ref 2050 PWRBIO | 5% cap | 10% cap | Cap5 2050 | Cap5+wind 2050 | Cap5+wind binding |
|---|---:|---:|---:|---:|---:|---:|---|
| `PWRBIOA1` | 333.15 | 0.00 | 16.658 | 33.315 | 0.000 | 16.658 | 2030–2070 |
| `PWRBIOA2` | 179.39 | 0.00 | 8.969 | 17.939 | 0.000 | 8.969 | 2030–2070 |
| `PWRBIOB1` | 323.02 | 0.00 | 16.151 | 32.302 | 0.000 | 16.151 | 2029–2070 |
| `PWRBIOB2` | 107.67 | 0.00 | 5.384 | 10.767 | 0.000 | 5.384 | 2034–2070 |
| `PWRBIOL1` | 49.24 | 0.00 | 2.462 | 4.924 | 0.000 | 2.462 | 2032–2070 |
| `PWRBIOM1` | 106.49 | 0.23 | 5.324 | 10.649 | 0.228 | 5.324 | 2033–2070 |
| `PWRBION1` | 8.73 | 0.60 | 0.436 | 0.873 | 0.436 | 0.436 | 2028–2070 |
| `PWRBIOO1` | 740.65 | 0.00 | 37.033 | 74.065 | 0.000 | 37.033 | 2031–2070 |
| `PWRBIOO2` | 130.70 | 0.00 | 6.535 | 13.070 | 0.000 | 6.535 | 2031–2070 |
| `PWRBIOQ1` | 812.37 | 8.29 | 40.619 | 81.237 | 8.289 | 40.619 | 2032–2070 |
| `PWRBIOQ2` | 203.09 | 2.48 | 10.155 | 20.309 | 2.481 | 10.155 | 2033–2070 |
| `PWRBIOS1` | 126.15 | 0.00 | 6.307 | 12.615 | 0.000 | 6.307 | 2030–2070 |
| `PWRBIOT1` | 131.51 | 0.94 | 6.575 | 13.151 | 0.937 | 6.575 | 2034–2070 |
| **Total** | **3,252.17** | **12.53** | **162.608** | **325.217** | **12.371** | **162.609** | |

The tight sensitivity replaces the share cap with 5% of each zone's reference 2050 `PWRBIO` output (national total 0.627 PJ).  It is not a policy cap; it exists to see what substitutes when bio is almost entirely removed.

## 2. Headline results

| Case | Objective (M$) | Δ vs ref (M$) | Emissions (Mt) | Wind 2050 | Gas 2050 | BIO 2050 | Hydro 2050 | PWRBCW 2050 | Nuclear 2050 | T3 total | T4 active |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `efix_tier_200` | 1,371,773.03 | 0.00 | 0.460752 | 967.98 | 0.00 | 12.53 | 2,230.55 | 41.11 | 0.00 | 0.00 | no |
| `wind_int3_tier200` | 1,372,459.69 | 686.66 | 0.449816 | 0.00 | 0.00 | 980.00 | 2,231.06 | 41.11 | 0.00 | 0.00 | no |
| `wind_int3_refhydro_tier200` | 1,372,498.99 | 725.96 | 0.446139 | 0.00 | 0.00 | 980.51 | 2,230.55 | 41.11 | 0.00 | 0.00 | no |
| `pwrbio_cap5_tier200` | 1,371,773.07 | 0.04 | 0.461645 | 968.14 | 0.00 | 12.37 | 2,230.55 | 41.11 | 0.00 | 0.00 | no |
| `pwrbio_cap5_windint3_tier200` | 1,382,042.24 | 10,269.21 | 0.489886 | 0.00 | 0.00 | 162.61 | 2,230.55 | 51.83 | 807.19 | 1,613.44 | no |
| `pwrbio_cap10_windint3_tier200` | 1,379,320.13 | 7,547.10 | 0.491194 | 0.00 | 0.00 | 325.22 | 2,230.55 | 51.83 | 644.58 | 1,473.22 | no |
| `pwrbio_cap5ofbio_tier200` | 1,371,788.34 | 15.31 | 0.542358 | 979.89 | 0.00 | 0.63 | 2,230.55 | 41.11 | 0.00 | 0.00 | no |

`Wind 2050`, `Gas 2050`, `BIO 2050`, `Hydro 2050`, `PWRBCW 2050` and `Nuclear 2050` are PJ of output in 2050.  `T3 total` is the sum of T3 activity over 2021–2070.

## 3. Dispatch by key year

#### `pwrbio_cap5_tier200`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 8.98 | 0.00 | 2,230.32 | 0.43 | 25.43 | 0.00 | 0.000000 |
| 2030 | 130.49 | 0.00 | 2,230.55 | 12.37 | 40.22 | 0.00 | 0.000000 |
| 2040 | 605.80 | 0.00 | 2,230.55 | 12.37 | 41.11 | 0.00 | 0.000000 |
| 2050 | 968.14 | 0.00 | 2,230.55 | 12.37 | 41.11 | 0.00 | 0.000000 |
| 2060 | 980.51 | 0.00 | 2,230.55 | 0.00 | 41.11 | 0.00 | 0.000000 |
| 2070 | 980.51 | 0.00 | 2,230.55 | 0.00 | 41.11 | 0.00 | 0.000000 |

#### `pwrbio_cap5_windint3_tier200`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 0.00 | 0.00 | 2,230.32 | 4.85 | 29.94 | 0.00 | 0.000000 |
| 2030 | 0.00 | 0.00 | 2,230.55 | 125.12 | 45.65 | 12.41 | 0.000000 |
| 2040 | 0.00 | 0.00 | 2,230.55 | 162.61 | 51.83 | 444.85 | 0.000000 |
| 2050 | 0.00 | 0.00 | 2,230.55 | 162.61 | 51.83 | 807.19 | 0.000000 |
| 2060 | 0.00 | 0.00 | 2,230.55 | 162.61 | 51.83 | 807.19 | 0.000000 |
| 2070 | 0.00 | 0.00 | 2,230.55 | 162.61 | 51.83 | 807.19 | 0.000000 |

#### `pwrbio_cap10_windint3_tier200`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 0.00 | 0.00 | 2,230.32 | 6.35 | 28.39 | 0.00 | 0.000000 |
| 2030 | 0.00 | 0.00 | 2,230.55 | 142.86 | 40.22 | 0.00 | 0.000000 |
| 2040 | 0.00 | 0.00 | 2,230.55 | 325.22 | 51.83 | 282.32 | 0.000000 |
| 2050 | 0.00 | 0.00 | 2,230.55 | 325.22 | 51.83 | 644.58 | 0.000000 |
| 2060 | 0.00 | 0.00 | 2,230.55 | 325.22 | 51.83 | 644.58 | 0.000000 |
| 2070 | 0.00 | 0.00 | 2,230.55 | 325.22 | 51.83 | 644.58 | 0.000000 |

#### `pwrbio_cap5ofbio_tier200`

| Year | Wind | Gas | Hydro | BIO | PWRBCW | Nuclear | Emissions (Mt) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 9.98 | 0.00 | 2,230.32 | 0.00 | 24.84 | 0.00 | 0.000000 |
| 2030 | 142.23 | 0.00 | 2,230.55 | 0.63 | 40.22 | 0.00 | 0.000000 |
| 2040 | 617.55 | 0.00 | 2,230.55 | 0.63 | 41.11 | 0.00 | 0.000000 |
| 2050 | 979.89 | 0.00 | 2,230.55 | 0.63 | 41.11 | 0.00 | 0.000000 |
| 2060 | 980.51 | 0.00 | 2,230.55 | 0.00 | 41.11 | 0.00 | 0.000000 |
| 2070 | 980.51 | 0.00 | 2,230.55 | 0.00 | 41.11 | 0.00 | 0.000000 |

The 2050 emissions column is zero in every case.  The cumulative 0.45–0.54 Mt is almost entirely 2022–2024 gas, before the carbon price reaches $200/t.

## 4. BCW tiers

| Case | T1 total | T2 total | T3 total | T4 total | T1 bind | T2 bind | T3 bind | T4 bind |
|---|---:|---:|---:|---:|---|---|---|---|
| `efix_tier_200` | 4,107.37 | 1,178.46 | 0.00 | 0.00 | yes | yes | no | no |
| `wind_int3_tier200` | 4,086.27 | 1,187.80 | 0.00 | 0.00 | yes | yes | no | no |
| `wind_int3_refhydro_tier200` | 4,089.18 | 1,188.88 | 0.00 | 0.00 | yes | yes | no | no |
| `pwrbio_cap5_tier200` | 4,113.95 | 1,171.88 | 0.00 | 0.00 | yes | yes | no | no |
| `pwrbio_cap5_windint3_tier200` | 4,108.00 | 1,149.71 | 1,613.44 | 0.00 | yes | yes | yes | no |
| `pwrbio_cap10_windint3_tier200` | 4,032.99 | 1,195.78 | 1,473.22 | 0.00 | yes | yes | yes | no |
| `pwrbio_cap5ofbio_tier200` | 4,152.73 | 1,130.90 | 0.00 | 0.00 | yes | yes | no | no |

T1 and T2 bind every year in every case.  T3 binds in the wind+cap cases: from 2031 at the 5% cap and from 2036 at the 10% cap.  T4 stays idle, because T3 plus nuclear is cheaper than the T4 marginal tier.  The whole T3+T4 stack is only 104.14 PJ/yr of fuel, about 28 PJ/yr of power, so it cannot absorb the ~800 PJ gap left by an uncapped BIO fleet.

## 5. Emissions by year

| Case | 2022 | 2023 | 2024 | 2037 | 2042 | 2050 | total |
|---|---:|---:|---:|---:|---:|---:|---:|
| `efix_tier_200` | 0.436548 | 0.000000 | 0.018869 | 0.005090 | 0.000245 | 0.000000 | 0.460752 |
| `wind_int3_tier200` | 0.421728 | 0.022753 | 0.000000 | 0.005090 | 0.000245 | 0.000000 | 0.449816 |
| `wind_int3_refhydro_tier200` | 0.437360 | 0.000000 | 0.003444 | 0.005090 | 0.000245 | 0.000000 | 0.446139 |
| `pwrbio_cap5_tier200` | 0.437441 | 0.000000 | 0.018869 | 0.005090 | 0.000245 | 0.000000 | 0.461645 |
| `pwrbio_cap5_windint3_tier200` | 0.461798 | 0.022753 | 0.000000 | 0.005090 | 0.000245 | 0.000000 | 0.489886 |
| `pwrbio_cap10_windint3_tier200` | 0.463106 | 0.022753 | 0.000000 | 0.005090 | 0.000245 | 0.000000 | 0.491194 |
| `pwrbio_cap5ofbio_tier200` | 0.474866 | 0.022753 | 0.039404 | 0.005090 | 0.000245 | 0.000000 | 0.542358 |

## 6. Comparison with the post-fix $200 and wind cases

- Plain $200 reference: objective 1,371,773.03 M$, emissions 0.460752 Mt, 2050 wind 967.98 PJ, 2050 bio 12.53 PJ, gas 0.
- The 5% cap alone changes almost nothing: objective 1,371,773.07 M$ (+0.04 M$), emissions 0.461645 Mt (+0.000893 Mt). Only `PWRBION1` binds (0.436 PJ cap versus 0.599 PJ in the reference); the other 12 zones are below their caps.
- The old +$3/GJ wind case removes wind and lets bio rise to 980.00 PJ, with emissions 0.449816 Mt and gas 0.  Rebuilding the same wind adder with the reference hydro caps gives emissions 0.446139 Mt and bio 980.51 PJ.
- Adding the 5% cap to that wind case forces bio to exactly the cap (162.61 PJ) but **does not bring gas back**: 2050 gas is 0, all-years gas rises by only 0.32 PJ, and emissions rise by 0.043747 Mt versus the reference-hydro wind control. Nuclear rises to 807.19 PJ at 2050 (28.4 GW), and T3 binds at 39.87 PJ/yr.
- The 10% cap behaves the same way: bio 325.22 PJ, nuclear 644.58 PJ, gas 0, emissions 0.491194 Mt.
- The tight 5%-of-BIO cap removes 95% of bio without a wind adder; wind rises to 979.89 PJ, gas stays 0, and emissions rise to 0.542358 Mt (still near-zero and still with zero 2050 emissions).

## 7. Verdict

**Does gas return? No.**  In every capped case 2050 gas is 0.00 PJ.  All-years gas moves from 3.35 PJ in the reference to 3.56 PJ in the 5% cap + wind case; the emissions effect is +0.04 Mt, almost all in 2022–2023, not a return to gas-fired 2050 generation.  A full gas backstop would have added roughly 800 PJ of gas and ~110 Mt CO2; nothing like that happens.

**Do T3/T4 activate?**  T3 activates and binds at its 39.87 PJ/yr cap from 2031 (5% cap) or 2036 (10% cap); T3 totals 1,613.44 and 1,473.22 PJ over the horizon.  T4 remains idle in every case.  The high-cost tier is available but not needed because nuclear is cheaper than T4.

**Is the near-zero result solely the BIO backstop?**  No.  The BIO cap is real and binding under the wind stress, but the gap is filled by an uncapped zero-carbon **nuclear** fleet (807 PJ at 2050 in the 5% + wind case), with a small assist from T3.  When wind is not penalized, wind itself fills the gap left by a 95% bio cut.  The correct statement is that the near-zero result depends on *some* uncapped zero-carbon backstop; it is not specifically dependent on `RNWBIO`/`PWRBIO`.  Gas is not the marginal substitute in this model even when bio is constrained.

This also means the test does not prove the result is robust to a full set of realistic constraints.  It replaces one uncapped backstop (generic BIO) with another (nuclear) and, in the no-wind-penalty cases, with wind.  If nuclear were capped, costed at a higher capital cost, or subject to a build-rate limit, gas would become the marginal option.

## 8. Caveats

- The 5% and 10% caps are scenario assumptions, not policy.  They are shares of each zone's reference 2050 generation, held constant in every year.
- Single annual timeslice: no diurnal or seasonal balancing, ramping, curtailment, or reserve margin.  The wind and nuclear substitutions are annual-energy substitutions, not firm-capacity demonstrations.
- `RNWBIO` remains uncapped for non-power BIO demand; only `PWRBIO<z>` is capped.  `PWRURN` (nuclear) is also uncapped in the model; that is the main reason gas does not return.
- BCW tiers and BC zonal caps are unchanged.  T4 is a documented high-cost scenario tier, not an empirical marginal cost.
- Hydro caps are taken from the reference `efix_tier_200` parameter set so that the cap/wind lever is the only change; the older `wind_int3` run used slightly higher baseline-2021 hydro caps and is shown separately.
- Solver: GLPK via swiglpk 5.0.13.  All cases are `optimal`.

## 9. Artifacts

- `run_summaries.json` — objectives, emissions, dispatch, per-zone bio activity, cap binding, and tiers for every case.
- `dispatch_by_zone.csv` — long-format annual activity for every supply and dispatch technology.
- `pwrbio_caps.json` — reference generation, reference bio, and the exact per-zone caps for the 5%, 10%, and tight cases.
- `tests.json` — cap loading, dispatch reconciliation, tier caps, `osecan harmonize`, and unchanged-input checks.
- `manifest.json` — input/output hashes and source revisions.
