# Wind integration audit - corrected-emission OSeCAN

Generated: 2026-11-19T07:08:24+00:00

Status: `fresh_side_provisional_not_c2070_official`. The public [deltae/C2070](https://github.com/deltae/C2070) repository was not modified. All solves ran in the disposable copy `/tmp/osecan_wind_audit` copied from `/tmp/osecan_emfix`.

## Reference and case definitions

Reference: `efix_tier_200` - tiered national BC supply curve, CO2 $200/t from 2026, hydro capped at 2021 activity, corrected output-basis emission factors (gas 0.1377 Mt/PJ, coal 0.261 Mt/PJ of output).

| Case | Change vs reference |
|---|---|
| `wind_int3_tier200` | +$3/GJ wind integration cost |
| `wind_cap20_tier200` | 20% zonal wind activity caps |
| `wind_int5_tier200` | +$5/GJ wind integration cost |

The tier stack, BC zonal caps, demand, and corrected emission factors are unchanged in every case. Only the wind lever differs.

## Headline results

| Case | Objective (M$) | Delta vs ref (M$) | Emissions (Mt) | Wind 2050 (PJ) | Gas 2050 (PJ) | BIO 2050 (PJ) | Hydro 2050 (PJ) | National BCW total (PJ) | PWRBCW total (PJ) | T1/T2 bind | T3/T4 active |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| `efix_tier_200` | 1,371,773.03 | 0.00 | 0.460752 | 967.98 | 0.00 | 12.53 | 2,230.55 | 7,173.70 | 1,928.42 | yes | no |
| `wind_int3_tier200` | 1,372,459.69 | 686.66 | 0.449816 | 0.00 | 0.00 | 980.00 | 2,231.06 | 7,161.95 | 1,925.26 | yes | no |
| `wind_cap20_tier200` | 1,372,234.71 | 461.68 | 0.457246 | 193.60 | 0.00 | 786.40 | 2,231.06 | 7,169.14 | 1,927.19 | yes | no |
| `wind_int5_tier200` | 1,372,459.69 | 686.66 | 0.449816 | 0.00 | 0.00 | 980.00 | 2,231.06 | 7,161.95 | 1,925.26 | yes | no |

`T1/T2 bind` means at least one of the first two supply tiers reached its annual activity cap in at least one year. `T3/T4 active` means either high-cost tier produced any activity in any year.

## Wind cap (Case 2)

The cap is 20% of each zone's own 2050 activity in the reference run, held constant in every year. It is not a 20% share of total generation; it is a 20% haircut of the reference wind build-out.

| Zone | Reference 2050 (PJ) | 20% cap (PJ) | Case-2 2050 (PJ) | Utilisation | Binding years |
|---|---:|---:|---:|---:|---|
| PWRWNDA1 | 134.411 | 26.882 | 26.882 | 1.000 | 2031-2070 (40 yrs) |
| PWRWNDA2 | 70.417 | 14.083 | 14.083 | 1.000 | 2031-2070 (40 yrs) |
| PWRWNDB1 | 134.615 | 26.923 | 26.923 | 1.000 | 2030-2070 (41 yrs) |
| PWRWNDB2 | 34.464 | 6.893 | 6.893 | 1.000 | 2034-2070 (37 yrs) |
| PWRWNDL1 | 9.310 | 1.862 | 1.862 | 1.000 | 2031-2070 (40 yrs) |
| PWRWNDM1 | 18.196 | 3.639 | 3.639 | 1.000 | 2034-2070 (37 yrs) |
| PWRWNDN1 | 1.853 | 0.371 | 0.371 | 1.000 | 2034-2070 (37 yrs) |
| PWRWNDO1 | 270.432 | 54.086 | 54.086 | 1.000 | 2032-2070 (39 yrs) |
| PWRWNDO2 | 47.714 | 9.543 | 9.543 | 1.000 | 2032-2070 (39 yrs) |
| PWRWNDQ1 | 142.157 | 28.431 | 28.431 | 1.000 | 2034-2070 (37 yrs) |
| PWRWNDQ2 | 35.629 | 7.126 | 7.126 | 1.000 | 2033-2070 (38 yrs) |
| PWRWNDS1 | 39.947 | 7.989 | 7.989 | 1.000 | 2030-2070 (41 yrs) |
| PWRWNDT1 | 28.837 | 5.767 | 5.767 | 1.000 | 2035-2070 (36 yrs) |
| **Total** | **967.98** | **193.60** | **193.60** | | |

## BCW supply tiers

| Case | T1 total (PJ) | T2 total (PJ) | T3 total (PJ) | T4 total (PJ) | T1 bind | T2 bind | T3 bind | T4 bind |
|---|---:|---:|---:|---:|---|---|---|---|
| `efix_tier_200` | 4,107.37 | 1,178.46 | 0.00 | 0.00 | yes | yes | no | no |
| `wind_int3_tier200` | 4,086.27 | 1,187.80 | 0.00 | 0.00 | yes | yes | no | no |
| `wind_cap20_tier200` | 4,142.53 | 1,138.73 | 0.00 | 0.00 | yes | yes | no | no |
| `wind_int5_tier200` | 4,080.68 | 1,193.39 | 0.00 | 0.00 | yes | yes | no | no |

### wind_cap20_tier200: key-year dispatch

| Year | Wind (PJ) | Gas (PJ) | Hydro (PJ) | Emissions (Mt) |
|---:|---:|---:|---:|---:|
| 2025 | 4.99 | 0.00 | 2,230.50 | 0.000000 |
| 2030 | 124.29 | 0.00 | 2,231.06 | 0.000000 |
| 2040 | 193.60 | 0.00 | 2,231.06 | 0.000000 |
| 2050 | 193.60 | 0.00 | 2,231.06 | 0.000000 |
| 2060 | 193.60 | 0.00 | 2,231.06 | 0.000000 |
| 2070 | 193.60 | 0.00 | 2,231.06 | 0.000000 |

### wind_int3_tier200: key-year dispatch

| Year | Wind (PJ) | Gas (PJ) | Hydro (PJ) | Emissions (Mt) |
|---:|---:|---:|---:|---:|
| 2025 | 0.00 | 0.00 | 2,230.50 | 0.000000 |
| 2030 | 0.00 | 0.00 | 2,231.06 | 0.000000 |
| 2040 | 0.00 | 0.00 | 2,231.06 | 0.000000 |
| 2050 | 0.00 | 0.00 | 2,231.06 | 0.000000 |
| 2060 | 0.00 | 0.00 | 2,231.06 | 0.000000 |
| 2070 | 0.00 | 0.00 | 2,231.06 | 0.000000 |

## Verdict

- **+$3/GJ flips wind out of the merit order.** 2050 wind falls from 967.98 PJ to 0 PJ while generic BIO rises from 12.53 PJ to 980.00 PJ. Gas remains 0 and emissions stay near-zero (0.449816 Mt). The objective rises by 686.66 M$. This is a discrete switch to uncapped BIO, not a gradual integration-cost penalty on dispatched wind.
- **Wind cap:** Near-zero emissions persist numerically under the 20% wind cap. Case-2 emissions are 0.457246 Mt versus 0.460752 Mt in the reference. 2050 wind falls to 193.60 PJ, but 2050 gas stays at 0.00 PJ; generic BIO rises from 12.53 PJ to 786.40 PJ. The caps bind in 13 zones; the first binding year is 2030.
- **High-cost biomass tiers:** T3/T4 are still idle in Case 2 (T3 total 0.00 PJ, T4 total 0.00 PJ), versus idle in the reference. Generic BIO is cheaper than the T3/T4 tiers, so the wind gap does not pull the high-cost residue tiers into the merit order.
- **Interpretation:** the reference's near-zero emissions survive the wind cases only because `RNWBIO` is an uncapped, zero-carbon backstop at $3/GJ. The audit concern about wind is confirmed: wind has no integration cost, reserve margin, or firm-capacity requirement, and a $3/GJ adder is enough to remove it entirely. But the emissions conclusion is buffered by a second unmodelled resource. If generic BIO were capped or costed, the wind gap would have to be filled by gas and emissions would rise.
- **+$5/GJ variant:** the same wind exit occurs: 2050 wind is 0 PJ and generic BIO is 980.00 PJ. Objective 1,372,459.69 M$, emissions 0.449816 Mt. With no wind activity the $5 adder is not paid, so this case is nearly identical to the +$3/GJ case.

## Caveats

- Single ANN timeslice: no diurnal or seasonal wind integration constraint, no ramping, no curtailment, and no reserve margin.
- The reference has no wind integration cost. The $3/GJ and $5/GJ cases are sensitivity adders, not a transmission or balancing study.
- The 20% cap is applied to each `PWRWND<z>` annual activity in every year using the post-fix 2050 reference per zone. It is a scenario cap, not an engineering limit.
- Hydro is capped at 2021 activity, matching the post-fix $200 reference. The tiered supply curve and BC zonal caps are unchanged.
- Model code is the disposable copy with the corrected emission factors; the public OSeCAN repository is unchanged.
- Solver: GLPK via swiglpk 5.0.13. Statuses are in `run_summaries.json`.

## Artifacts

- `run_summaries.json` - objectives, emissions, dispatch, tier activity, and cap binding for every case.
- `dispatch_by_zone.csv` - long-format annual activity for every supply and dispatch technology.
- `wind_caps_20pct.json` - the exact per-zone caps.
- `manifest.json` - input/output hashes and source revisions.
