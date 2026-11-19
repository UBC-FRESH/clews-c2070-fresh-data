# National rest-of-Canada biomass supply curve (OSeCAN)

**Status:** FRESH-side provisional, not an official C2070 result.  
**Basis:** RSYC-only v0 at 200M m3/yr log volume, no AAC/THLB/local corrections.

## 1. Tier structure

| Tier | Technology | Interval (PJ) | Incremental cap (PJ) | Cost ($/GJ) | Flag |
|---|---|---|---|---|---|
| T1 | `SUPBCWT1` | 0.000000–85.007113 | 85.007113 | 2.456978 | base_cost |
| T2 | `SUPBCWT2` | 85.007113–109.398863 | 24.391750 | 2.456978 | base_cost |
| T3 | `SUPBCWT3` | 109.398863–149.272577 | 39.873714 | 3.194071 | mid_cost |
| T4 | `SUPBCWT4` | 149.272577–213.538041 | 64.265464 | 3.500000 | scenario_high_cost_marginal_tier |

The tier caps sum to the rest-of-Canada cap (213.538041 PJ).  The BC zonal `SUPBCWB1` / `SUPBCWB2` caps are unchanged and sum to 43.523816 PJ from 2028.  Tiers plus BC zones equal the national total 257.061857 PJ.  The single `SUPBCW` cap is set to zero so the four tiers cannot double count the rest-of-Canada supply.

T1-T3 keep their adopted incremental caps in every year.  T4 absorbs the existing 2021-2027 BC zonal phase-down, so the tier sum equals the rest-of-Canada cap in every year.

## 2. Results

| Run | Status | Objective | Tier activity 2050 (PJ) | BCW supply 2050 (PJ) | PWRBCW 2050 (PJ) | Emissions 2050 (Mt) |
|---|---|---|---|---|---|---|
| baseline | optimal | 1331289.52 | 0.000000 | 0.000000 | 0.000000 | 1.030757 |
| stress | optimal | 1371124.5 | 109.398800 | 152.922570 | 41.108217 | 1.484692 |
| stress_fixed_hydro | optimal | 1371135.69 | 109.398800 | 152.922570 | 41.108217 | 1.520512 |

### Tier dispatch

#### baseline

| Year | T1 | T2 | T3 | T4 | Total tiers | PWRBCW total | Emissions |
|---|---|---|---|---|---|---|---|
| 2021 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.017136 |
| 2022 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.030757 |
| 2025 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 2028 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.108501 |
| 2030 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.030757 |
| 2035 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.030757 |
| 2040 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.030757 |
| 2050 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.030757 |
| 2060 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 2070 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

**Cap binding:**
- `SUPBCWT1`: binding=False, years=none, max utilisation=0.000000
- `SUPBCWT2`: binding=False, years=none, max utilisation=0.000000
- `SUPBCWT3`: binding=False, years=none, max utilisation=0.000000
- `SUPBCWT4`: binding=False, years=none, max utilisation=0.000000

#### stress

| Year | T1 | T2 | T3 | T4 | Total tiers | PWRBCW total | Emissions |
|---|---|---|---|---|---|---|---|
| 2021 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.028659 |
| 2022 | 56.397661 | 0.000000 | 0.000000 | 0.000000 | 56.397661 | 15.160661 | 1.484692 |
| 2025 | 71.879147 | 24.391700 | 0.000000 | 0.000000 | 96.270847 | 27.840626 | 0.235088 |
| 2028 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 35.581063 | 0.510857 |
| 2030 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 39.892114 | 1.462246 |
| 2035 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108217 | 1.484692 |
| 2040 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108217 | 1.484692 |
| 2050 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108217 | 1.484692 |
| 2060 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108218 | 0.000000 |
| 2070 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108218 | 0.000000 |

**Cap binding:**
- `SUPBCWT1`: binding=True, years=2024–2070, max utilisation=1.000000
- `SUPBCWT2`: binding=True, years=2025–2070, max utilisation=0.999998
- `SUPBCWT3`: binding=False, years=none, max utilisation=0.000000
- `SUPBCWT4`: binding=False, years=none, max utilisation=0.000000

#### stress_fixed_hydro

| Year | T1 | T2 | T3 | T4 | Total tiers | PWRBCW total | Emissions |
|---|---|---|---|---|---|---|---|
| 2021 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.017161 |
| 2022 | 29.108897 | 24.391700 | 0.000000 | 0.000000 | 53.500597 | 14.381880 | 1.520512 |
| 2025 | 85.007100 | 8.316574 | 0.000000 | 0.000000 | 93.323674 | 27.117519 | 0.271969 |
| 2028 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 35.650207 | 0.546628 |
| 2030 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 39.961259 | 1.498066 |
| 2035 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108217 | 1.520512 |
| 2040 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108217 | 1.520512 |
| 2050 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108217 | 1.520512 |
| 2060 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108218 | 0.000000 |
| 2070 | 85.007100 | 24.391700 | 0.000000 | 0.000000 | 109.398800 | 41.108218 | 0.000000 |

**Cap binding:**
- `SUPBCWT1`: binding=True, years=2025–2070, max utilisation=1.000000
- `SUPBCWT2`: binding=True, years=2022–2070, max utilisation=0.999998
- `SUPBCWT3`: binding=False, years=none, max utilisation=0.000000
- `SUPBCWT4`: binding=False, years=none, max utilisation=0.000000

## 3. Comparison with single-cap cases

| Case | CO2 from 2026 | Rest cap 2028 (PJ) | Objective | SUPBCW 2050 (PJ) | PWRBCW 2050 (PJ) |
|---|---|---|---|---|---|
| 119M baseline | 95/115 | 109.398863 | 1331289.52 | 0.0 | 0 |
| 150M baseline | 95/115 | 149.272577 | 1331289.52 | 0.0 | 0 |
| 119M stress | 95/200 | 109.398863 | 1371124.38 | 109.399 | 41.108271 |
| 150M stress | 95/200 | 149.272577 | 1370983.13 | 149.273 | 51.827088 |
| 200M stress | 95/200 | 213.538041 | 1370767.51 | 213.538 | 69.102625 |

The single-cap 200M baseline is not present in the retained run set; the 200M comparison is the stress case only.  The tiered curve uses the same caps but a higher marginal cost above 109.4 PJ, so it is expected to differ from the flat-cost single-cap case.

In the $200/t hydro-capped stress the binding tiers are `SUPBCWT1`, `SUPBCWT2`.  The non-binding tiers are `SUPBCWT3`, `SUPBCWT4`.  The model stops at the 109.4 PJ boundary because the next tier costs 3.194 $/GJ, above the 3.0 $/GJ generic RNWBIO substitute; this is an economic result of the adopted scenario costs, not a cap or structural exclusion.

## 4. Caveats

- Tier costs are scenario values, not a fitted marginal-cost curve.  T4 at 3.50 $/GJ is a documented high-cost marginal tier.
- The curve is RSYC-only: no AAC, THLB, operability, or local correction factor is applied.
- The hydro stress is an annual upper bound at 2021 activity.  The fixed-hydro variant additionally sets the annual lower bound equal to that activity; neither is a forecast.
- Results are for the disposable model copy and do not modify the public OSeCAN repository.
