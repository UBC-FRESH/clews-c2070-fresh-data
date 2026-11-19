# Demand-side sensitivity for the tiered national BCW supply curve

**Status:** FRESH-side provisional sensitivity; not an official C2070 result.  
**Base:** committed tiered national supply curve (`SUPBCWT1`-`SUPBCWT4` + BC zonal `SUPBCWB1`/`SUPBCWB2`).  
**Stress:** hydro annual upper cap at 2021 activity in every case.  
**Source copy:** `/tmp/osecan_supply_curve` copied to `/tmp/osecan_demand_sens`; source left unchanged.

## 1. Case definitions

| Case | CO2 from 2026 ($/t) | Hydro | Demand-side change |
|---|---:|---|---|
| Reference | 200 | upper cap at 2021 | none |
| carbon_250 | 250 | upper cap at 2021 | none |
| carbon_300 | 300 | upper cap at 2021 | none |
| carbon_400 | 400 | upper cap at 2021 | none |
| mandate_saturation | 200 | upper cap at 2021 | 7 proportional lower limits on rest-of-Canada `PWRBCW` zones summing to 57.333609 PJ, plus 11.699938 PJ BC zonal reference, for a national target of 69.033547 PJ in 2050 (diagnostic, not policy) |

## 2. Headline results

| Case | Status | Objective (M$) | Emissions cumulative (Mt) | Emissions 2050 (Mt) | National BCW 2050 (PJ) | PWRBCW 2050 (PJ) | Binding tiers |
|---|---|---:|---:|---:|---:|---:|---|
| reference_200 | optimal | 1371124.50 | 38.457287 | 1.484692 | 152.922570 | 41.108217 | SUPBCWT1,SUPBCWT2 |
| carbon_250 | optimal | 1371648.82 | 2.446648 | 0.000000 | 152.922570 | 41.108219 | SUPBCWT1,SUPBCWT2 |
| carbon_300 | optimal | 1371649.82 | 2.445288 | 0.000000 | 152.922570 | 41.108219 | SUPBCWT1,SUPBCWT2 |
| carbon_400 | optimal | 1371650.78 | 2.417297 | 0.000000 | 152.922570 | 41.108220 | SUPBCWT1,SUPBCWT2 |
| mandate_saturation | optimal | 1371191.11 | 38.027154 | 1.471004 | 256.804505 | 69.033469 | SUPBCWT1,SUPBCWT2,SUPBCWT3 |

## 3. Tier dispatch

### 2050 (PJ)

| Case | T1 | T2 | T3 | T4 | T1+T2 | Total tiers |
|---|---:|---:|---:|---:|---:|---:|
| reference_200 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 109.398800 |
| carbon_250 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 109.398800 |
| carbon_300 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 109.398800 |
| carbon_400 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 109.398800 |
| mandate_saturation | 85.007100 | 24.391700 | 39.873700 | 64.008235 | 109.398800 | 213.280735 |

### Cumulative 2021-2070 (PJ)

| Case | T1 | T2 | T3 | T4 | T1+T2 | Total tiers |
|---|---:|---:|---:|---:|---:|---:|
| reference_200 | 4095.001069 | 1120.076321 | 0.000000 | 0.000000 | 5215.077390 | 5215.077390 |
| carbon_250 | 4137.020922 | 1134.615002 | 0.000000 | 0.000000 | 5271.635924 | 5271.635924 |
| carbon_300 | 4098.222988 | 1173.412936 | 0.000000 | 0.000000 | 5271.635924 | 5271.635924 |
| carbon_400 | 4159.530910 | 1112.105015 | 0.000000 | 0.000000 | 5271.635925 | 5271.635925 |
| mandate_saturation | 4112.875650 | 1114.454398 | 217.875708 | 138.490990 | 5227.330048 | 5583.696746 |

## 4. Comparison with the $200/t reference

| Case | Objective delta (M$) | Emissions delta (Mt) | National BCW 2050 delta (PJ) | PWRBCW 2050 delta (PJ) |
|---|---:|---:|---:|---:|
| carbon_250 | 524.32 | -36.010639 | 0.000000 | 0.000002 |
| carbon_300 | 525.32 | -36.011999 | 0.000000 | 0.000002 |
| carbon_400 | 526.28 | -36.039990 | 0.000000 | 0.000003 |
| mandate_saturation | 66.61 | -0.430133 | 103.881935 | 27.925252 |

The $250-$400/t cases cut cumulative emissions from 38.457 Mt to about 2.4 Mt without increasing BCW demand: 2050 `PWRBCW` stays at 41.108 PJ and national BCW at 152.923 PJ.  The abatement is delivered by non-BC options, so a higher carbon price is not a biomass-demand driver in this model structure.

## 5. Tier activation

T3 or T4 dispatch is non-zero in: `mandate_saturation`.
- `mandate_saturation`: T3 2050 39.873700 PJ, T4 2050 64.008235 PJ; T3 cumulative 217.875708 PJ, T4 cumulative 138.490990 PJ.
No carbon-price case activates T3 or T4 up to the highest tested price.  Activation is induced only by the demand-side mandate diagnostic, not by the carbon price.

## 6. Biomass-power mandate diagnostic

Reference 2050 electricity generation is 6182.051020 PJ.  A 5% mandate would require 309.102551 PJ of `PWRBCW` output, which needs 1149.861490 PJ of BCW fuel.  The national BCW cap is 257.061857 PJ, so the maximum possible `PWRBCW` output is 69.102650 PJ (1.12% of reference 2050 generation).  A 5% or 10% mandate is therefore structurally infeasible before any cost effect, because it exceeds the BCW cap by a factor of 4.47 (5%) or 8.95 (10%).  The exact limiting constraint is the national BCW cap: 1,149.861490 PJ (5%) or 2,299.722980 PJ (10%) of BCW fuel is required against 257.061857 PJ available.  These cases are therefore not solved; no dispatch is fabricated.

The diagnostic case imposes proportional lower limits on 7 rest-of-Canada `PWRBCW` zones in 2050.  The limits sum to 57.333609 PJ; the BC zonal B1/B2 reference is 11.699938 PJ, so the national `PWRBCW` target is 69.033547 PJ.  This is the BCW-cap saturation point, not a policy number.  Solver status: `optimal`.
- PWRBCW 2050: 69.033469 PJ; national BCW 2050: 256.804505 PJ; T3 2050: 39.873700 PJ; T4 2050: 64.008235 PJ (99.60% of the T4 cap).

## 7. Caveats

- Carbon prices are scenario sensitivities, not forecasts or policy recommendations.
- The hydro stress is an annual upper bound at 2021 activity, not a forecast.
- The curve is RSYC-only: no AAC, THLB, operability, or local correction applies.
- T1 and T2 have identical variable cost, so their individual split is degenerate; use T1+T2 combined.
- T4 is a documented high-cost marginal tier, not a fitted marginal-cost curve.
- Results come from the disposable model copy and do not modify the public OSeCAN repository.
