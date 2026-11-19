# Generic-biomass sensitivity for the tiered national BCW supply curve

**Status:** FRESH-side provisional sensitivity; not an official C2070 result.  
**Base:** committed tiered national supply curve (`SUPBCWT1`–`SUPBCWT4` + BC zonal `SUPBCWB1`/`SUPBCWB2`).  
**Stress:** CO2 $200/t from 2026; hydro annual upper cap at 2021 activity.  
**Source copy:** `/tmp/osecan_supply_curve` copied to `/tmp/osecan_bio_sens`; source left unchanged.

## 1. Case definitions

| Case | RNWBIO cost | RNWBIO cap | Purpose |
|---|---|---|---|
| Reference | 3.00 $/GJ | uncapped | Committed tiered stress result |
| A | 4.00 $/GJ | uncapped | Raise generic biomass above T3 ($3.194) and T4 ($3.50) |
| High diagnostic | 10.00 $/GJ | uncapped | Confirm whether any finite RNWBIO cost activates T3/T4 |
| B | 3.00 $/GJ | 50 PJ/yr | Requested cap scenario to isolate the bypass |
| B diagnostic | 3.00 $/GJ | 531.055925 PJ/yr | Cap at 2021 BIO supply |

All other assumptions are inherited from the committed stress run (`SUPBCW` disabled, tier caps and BC zonal caps unchanged).

## 2. Case A ($4/GJ, uncapped)

| Metric | Reference ($3/GJ) | Case A ($4/GJ) | Delta |
|---|---:|---:|---:|
| Objective (M$) | 1,371,124.50 | 1,384,777.42 | +13,652.92 (+0.9957%) |
| Emissions, cumulative 2021–2070 (Mt) | 38.457287 | 38.457287 | +0.000000 |
| Emissions, 2050 (Mt) | 1.484692 | 1.484692 | +0.000000 |
| National BCW, 2050 (PJ) | 152.922570 | 152.922570 | +0.000000 |
| National BCW, cumulative (PJ) | 7087.666476 | 7087.666476 | +0.000000 |
| PWRBCW, 2050 (PJ) | 41.108217 | 41.108217 | +0.000000 |
| PWRBCW, cumulative (PJ) | 1905.286669 | 1905.286667 | -0.000002 |

### Tier dispatch

| Tier | 2050 reference | 2050 Case A | Cumulative reference | Cumulative Case A |
|---|---:|---:|---:|---:|
| SUPBCWT1 | 85.007100 | 85.007100 | 4095.001069 | 4059.345622 |
| SUPBCWT2 | 24.391700 | 24.391700 | 1120.076321 | 1155.731768 |
| SUPBCWT3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| SUPBCWT4 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| **T1+T2 combined** | **109.398800** | **109.398800** | **5215.077390** | **5215.077390** |

**Binding tiers:** `SUPBCWT1`, `SUPBCWT2`.  
T3 and T4 remain zero in every year (`T3 zero all years=True`, `T4 zero all years=True`).  
T1 and T2 have identical variable cost (2.456978 $/GJ), so their individual split is degenerate; the combined T1+T2 dispatch is unchanged from the reference.

The objective rises by 13,652.92 M$ because RNWBIO is the sole BIO supplier to fixed end-use demand and its cost rises by 1 $/GJ.  National BCW and emissions are identical to the reference at six-decimal reporting precision; PWRBCW differs by at most 1e-6 PJ in any year (2e-6 PJ cumulative from result rounding).

## 3. Case B (50 PJ cap, 3 $/GJ)

The 50 PJ/yr cap is **infeasible**.  GLPK simplex returns 10 (`GLP_ENOPFS`, no primal feasible solution); the wrapper records `unknown` only because `GLP_UNDEF` is not mapped to a label.

This is structural, not a solver tolerance:

- `RNWBIO` is the only producer of the `BIO` fuel in the assembled model.
- Reference BIO demand is 531.055925 PJ in 2021 rising to 801.961215 PJ in 2050; 50 PJ is 6.2% of the 2050 level.
- Capping `RNWBIO` below annual BIO demand leaves fixed end-use demand unserved.

A diagnostic cap at the 2021 BIO level (531.055925 PJ/yr) is also infeasible.  Any feasible cap must be at least the exogenous annual BIO demand, which makes it non-binding; there is therefore no binding cap that can isolate a generic-biomass bypass without adding an alternative BIO supplier.

## 4. High-cost diagnostic ($10/GJ)

| Metric | Reference | $10/GJ | Delta |
|---|---:|---:|---:|
| Objective (M$) | 1,371,124.50 | 1,466,694.98 | +95,570.48 |
| Emissions, cumulative (Mt) | 38.457287 | 38.457287 | +0.000000 |
| National BCW, 2050 (PJ) | 152.922570 | 152.922570 | +0.000000 |
| PWRBCW, 2050 (PJ) | 41.108217 | 41.108217 | +0.000000 |
| SUPBCWT1 cumulative (PJ) | 4095.001069 | 4019.884090 | -75.116979 |
| SUPBCWT2 cumulative (PJ) | 1120.076321 | 1195.193300 | +75.116979 |
| SUPBCWT3 cumulative (PJ) | 0.000000 | 0.000000 | +0.000000 |
| SUPBCWT4 cumulative (PJ) | 0.000000 | 0.000000 | +0.000000 |

T3/T4 remain zero even at 10 $/GJ.  The extra objective cost is the higher RNWBIO price on the same physical BIO demand.

## 5. Is the supply curve economically active beyond T2?

**No.**  In this model structure the curve is active only through T2:

- BCW is consumed only by `PWRBCW` technologies, at 3.72 PJ of BCW per PJ of electricity.
- Reference 2050 `PWRBCW` output is 41.108217 PJ, so BCW fuel demand is 3.72 × 41.108217 = 152.922567 PJ (reported national BCW supply 152.922570 PJ; the 3e-6 PJ difference is result rounding).
- BC zonal supply contributes 43.523770 PJ; the remaining rest-of-Canada requirement is exactly T1+T2 (109.398863 PJ).
- T3 would require rest-of-Canada BCW demand above 109.398863 PJ/yr (about 152.922633 PJ/yr national at the observed BC zonal supply).
- T4 would require rest-of-Canada BCW demand above 149.272577 PJ/yr (about 192.796347 PJ/yr national).

Cost is not the barrier: T3 (3.194071 $/GJ) and T4 (3.500000 $/GJ) are already cheaper than the 4 $/GJ generic biomass in Case A, yet neither dispatches.  Raising `RNWBIO` cost cannot create BCW demand because `RNWBIO` supplies `BIO` to fixed demand technologies and never dispatches to `PWRBIO` (zero in all runs).  A cost or cap on `RNWBIO` therefore cannot make T3/T4 economic.

**What would be needed (documented, not fabricated):** a structural change that raises BCW demand above 109.398863 PJ/yr rest-of-Canada (for T3) or 149.272577 PJ/yr (for T4) — for example, a larger `PWRBCW` electricity role or an exogenous BCW demand — or a reduction in BC zonal supply below the observed 43.524 PJ/yr, which would force the rest-of-Canada stack upward.  No `RNWBIO` cost achieves this.

## 6. Caveats

- Tier costs are adopted scenario values, not a fitted marginal-cost curve; T4 is a documented high-cost tier.
- The curve is RSYC-only: no AAC, THLB, operability, or local correction applies.
- The hydro stress is an annual upper bound at 2021 activity, not a forecast.
- T1/T2 cost degeneracy means their individual split should not be interpreted; use T1+T2 combined.
- Case B caps are diagnostic scenarios, not policy recommendations.
- Results come from the disposable model copy and do not modify the public OSeCAN repository.
