# Tight PWRBIO backstop cap on the corrected-emission OSeCAN model

**Status:** `fresh_side_provisional_not_c2070_official`. The public [deltae/C2070](https://github.com/deltae/C2070) repository was not modified.

## 1. What was implemented

The cap is an annual ceiling on BIO fuel input to the `PWRBIO<zone>` power plants. `PWRBIO` has one mode, one output fuel, an output ratio of 1, and a constant BIO input ratio of 2.85 PJ fuel per PJ output in every year. The ceiling is written as `TotalTechnologyAnnualActivityUpperLimit` on each `PWRBIO<zone>` at the reference 2050 output level, held in every year 2021-2070. That is exactly equivalent to a BIO-input cap because the input ratio is fixed.

The total cap is **35.72 PJ/yr of BIO input**, equal to **12.533855 PJ/yr of electricity output**. Per-zone caps are the reference 2050 `PWRBIO` distribution:

| Zone | Reference 2050 output (PJ) | BIO input cap (PJ) |
|---|---:|---:|
| `PWRBIOA1` | 0.000000 | 0.000000 |
| `PWRBIOA2` | 0.000000 | 0.000000 |
| `PWRBIOB1` | 0.000000 | 0.000000 |
| `PWRBIOB2` | 0.000000 | 0.000000 |
| `PWRBIOL1` | 0.000000 | 0.000000 |
| `PWRBIOM1` | 0.227550 | 0.648518 |
| `PWRBION1` | 0.599067 | 1.707341 |
| `PWRBIOO1` | 0.000000 | 0.000000 |
| `PWRBIOO2` | 0.000000 | 0.000000 |
| `PWRBIOQ1` | 8.288763 | 23.622975 |
| `PWRBIOQ2` | 2.481080 | 7.071078 |
| `PWRBIOS1` | 0.000000 | 0.000000 |
| `PWRBIOT1` | 0.937395 | 2.671576 |

`RNWBIO` is uncapped. It remains the sole BIO producer and continues to serve the fixed non-power BIO demand. The tier stack, BC zonal caps, demand, and corrected emission factors are unchanged.  The BC zonal caps `SUPBCWB1` / `SUPBCWB2` remain at their reference values and bind in every solved case (3.6055 and 39.9183 PJ in 2050).

## 2. Headline results

| Case | Objective (M$) | Emissions (Mt) | Gas 2050 (PJ) | Wind 2050 (PJ) | Hydro 2050 (PJ) | Uranium 2050 (PJ) | PWRBIO out 2050 (PJ) | PWRBIO in 2050 (PJ) | PWRBCW 2050 (PJ) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `pwrbio_cap3572_tier200` | 1,371,773.03 | 0.460752 | 0.000 | 967.981 | 2,230.546 | 0.000 | 12.534 | 35.721 | 41.108 |
| `pwrbio_cap0_tier200` | 1,371,789.49 | 0.542358 | 0.000 | 980.515 | 2,230.546 | 0.000 | 0.000 | 0.000 | 41.108 |
| `pwrbio_cap3572_windint3_tier200` | 1,385,135.04 | 0.530558 | 0.000 | 0.000 | 2,230.546 | 957.262 | 12.534 | 35.721 | 51.827 |

### 2050 dispatch by fuel

| Case | Gas | Coal | Wind | Hydro | Solar | Uranium | Geo | BSW | BIO power (output) | PWRBIO fuel input | PWRBCW |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `pwrbio_cap3572_tier200` | 0.000 | 0.000 | 967.981 | 2,230.546 | 0.000 | 0.000 | 0.000 | 0.000 | 12.534 | 35.721 | 41.108 |
| `pwrbio_cap0_tier200` | 0.000 | 0.000 | 980.515 | 2,230.546 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 41.108 |
| `pwrbio_cap3572_windint3_tier200` | 0.000 | 0.000 | 0.000 | 2,230.546 | 0.000 | 957.262 | 0.000 | 0.000 | 12.534 | 35.721 | 51.827 |

### Biomass supply tiers

| Case | T1 2050 | T2 2050 | T3 2050 | T4 2050 | T1/T2 bind | T3/T4 active | National BCW 2050 |
|---|---:|---:|---:|---:|---|---|---:|
| `pwrbio_cap3572_tier200` | 85.007 | 24.392 | 0.000 | 0.000 | yes | no | 152.923 |
| `pwrbio_cap0_tier200` | 85.007 | 24.392 | 0.000 | 0.000 | yes | no | 152.923 |
| `pwrbio_cap3572_windint3_tier200` | 85.007 | 24.392 | 39.874 | 0.000 | yes | yes | 192.796 |

### PWRBIO cap utilisation

| Case | Total cap (PJ input) | 2050 input (PJ) | Utilisation | Binding zones in 2050 | First binding year |
|---|---:|---:|---:|---|---:|
| `pwrbio_cap3572_tier200` | 35.721 | 35.721 | 1.0000 | PWRBIOM1, PWRBION1, PWRBIOQ1, PWRBIOQ2, PWRBIOT1 | 2022 |
| `pwrbio_cap0_tier200` | 0.000 | 0.000 | n/a | none | none |
| `pwrbio_cap3572_windint3_tier200` | 35.721 | 35.721 | 1.0000 | PWRBIOM1, PWRBION1, PWRBIOQ1, PWRBIOQ2, PWRBIOT1 | 2022 |

## 3. Comparison with the uncapped post-fix cases

| Case | PWRBIO input 2050 (PJ) | Gas 2050 (PJ) | Wind 2050 (PJ) | Emissions (Mt) | Objective (M$) |
|---|---:|---:|---:|---:|---:|
| Post-fix $200, no cap (`efix_tier_200`) | 35.721 | 0.00 | 967.98 | 0.460752 | 1,371,773.03 |
| Wind +$3/GJ, no cap (`wind_int3_tier200`) | 2,792.99 | 0.00 | 0.00 | 0.449816 | 1,372,459.69 |
| `pwrbio_cap3572_tier200` | 35.721 | 0.000 | 967.981 | 0.460752 | 1,371,773.03 |
| `pwrbio_cap0_tier200` | 0.000 | 0.000 | 980.515 | 0.542358 | 1,371,789.49 |
| `pwrbio_cap3572_windint3_tier200` | 35.721 | 0.000 | 0.000 | 0.530558 | 1,385,135.04 |

The uncapped comparison rows are the committed post-fix and wind-audit runs; they are not rerun here.  The wind-audit's `BIO 2050 = 980 PJ` is PWRBIO **electricity output**; the corresponding BIO **fuel input** is 2,792.99 PJ at the fixed 2.85 input ratio.  The cap in this test is on the fuel input, so it is 35.72 PJ, not 980 PJ.

The cap-0 case has slightly higher emissions than the reference (0.542358 vs 0.460752 Mt) because removing the 12.5 PJ of bio power raises pre-2026 gas use.  Post-2026 gas is unchanged at the reference sliver: 0.037 PJ in `PWRNGSN1` in 2037 (0.00509 Mt) and 0.0018 PJ in 2042 (0.000245 Mt).  The wind +$3 capped case also keeps the 2037 sliver and adds a 0.037 PJ `PWRNGSN1` sliver in 2042 (0.00509 Mt).

## 4. Verdict

- **Cap 35.72 PJ:** the cap reproduces the reference: gas 2050 0.000 PJ, emissions 0.460752 Mt, T1/T2 bind, T3/T4 idle. The cap is set at the reference zonal maxima, so it reproduces the reference instead of cutting it.
- **Cap 0 PJ:** PWRBIO output is zero. Gas 2050 is 0.000 PJ and emissions are 0.542358 Mt. The 12.5 PJ gap is small enough for existing zero-carbon capacity to absorb.
- **Wind +$3 with the 35.72 PJ cap:** gas 2050 is 0.000 PJ, wind 2050 is 0.000 PJ, uranium 2050 is 957.262 PJ, PWRBCW 2050 is 51.827 PJ, and emissions are 0.530558 Mt. Gas does not return at scale in 2050; uranium and additional PWRBCW fill the gap.  Post-2026 gas is a 0.037 PJ `PWRNGSN1` sliver in 2037 and 2042 (0.00509 Mt each), so near-zero emissions survive numerically but not with exactly the reference timing.
- **T3/T4:** T3 activates in the wind +$3 capped case at its 39.8737 PJ cap; T4 remains idle. The tight PWRBIO cap alone does not pull the high-cost tiers in; the T3 activation is driven by the larger PWRBCW requirement.

## 5. Tests

- `cap_loading` (pwrbio_cap3572_tier200): PASS
- `dispatch_reconciliation` (pwrbio_cap3572_tier200): PASS
- `tier_caps` (pwrbio_cap3572_tier200): PASS
- `osecan_harmonize` (pwrbio_cap3572_tier200): PASS
- `cap_loading` (pwrbio_cap0_tier200): PASS
- `dispatch_reconciliation` (pwrbio_cap0_tier200): PASS
- `tier_caps` (pwrbio_cap0_tier200): PASS
- `osecan_harmonize` (pwrbio_cap0_tier200): PASS
- `cap_loading` (pwrbio_cap3572_windint3_tier200): PASS
- `dispatch_reconciliation` (pwrbio_cap3572_windint3_tier200): PASS
- `tier_caps` (pwrbio_cap3572_windint3_tier200): PASS
- `osecan_harmonize` (pwrbio_cap3572_windint3_tier200): PASS

## 6. Caveats

- The cap is a scenario constraint, not a policy recommendation.
- Single annual timeslice: no diurnal, seasonal, ramping, reserve-margin, or curtailment constraints.
- `RNWBIO` remains uncapped for non-power BIO demand. The test caps `PWRBIO` only; it does not test a national BIO inventory ceiling.
- Per-zone caps are the reference 2050 distribution, held constant in every year. They are not an engineering limit.
- Uranium expansion is not constrained by a fuel-cycle, lead-time, or site limit in this single-ANN model; the 957 PJ of 2050 uranium in the wind +$3 capped case is a model outcome, not a project schedule.
- The uncapped comparison rows come from the committed post-fix and wind-audit artefacts; only the three capped cases are solved here.
