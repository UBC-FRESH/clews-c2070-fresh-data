# QC net-value benchmark — 2022 survey and BMMB historical check

**Status:** benchmark only. Generated 2026-11-21T21:13:14Z. `evidence=survey_benchmark` or `benchmark_historical`; `policy_grade=false`; `net_value_status=benchmark_only`.

This note reports a **forest-sector residual** at the mill gate, using the 2022 Quebec MRNF survey synthesis rows. It is not an observed transaction net value and not a policy result. It does not touch the merged ledger, the Forest LP objective, or the UI.

## Definitions

| Term | Definition |
|---|---|
| Delivered purchase | Survey `purchase.wood_purchase_delivered`, T2, CAD/m3 delivered to mill. |
| Procurement before transfers | Survey `synthesis_procurement.procurement_total_before_transfers`, T20 = harvest + road + haul + hosting + other. |
| Transfers | Survey `synthesis_procurement.transfers_total`, T20 = payments to the State. |
| Procurement after transfers | Survey `synthesis_procurement.procurement_total_after_transfers`, T20. |
| Residual before transfers | `delivered purchase - procurement before transfers` (pre-Crown surplus). |
| Residual after transfers | `delivered purchase - procurement after transfers` (forest-sector residual). |

The two residuals are linked by `residual_before = residual_after + transfers`. This is the ledger identity `pre-Crown surplus = forest-sector net value + Crown revenue` on the survey's 2022 basis.

Transformation, lumber, and by-product revenue are **not** netted against log costs. That would produce a mill margin, not forest net value.

## Provincial benchmark (2022, CAD/m3 nominal)

| Species | Product | Purchase | Procurement before | Transfers | Procurement after | Residual before | Residual after | Status |
|---|---|---:|---:|---:|---:|---:|---:|---|
| SEPM | total | 107.22 | 81.40 | 25.01 | 106.41 | 25.82 | 0.81 | computed |
| Hardwood | sciage | 85.42 | 79.73 | 20.22 | 99.95 | 5.69 | -14.53 | computed |
| Hardwood | trituration | 79.45 | — | — | — | — | — | not_computable_missing_synthesis_procurement |
| Hardwood | total | 80.95 | — | — | — | — | — | not_computable_missing_synthesis_procurement |
| Poplar | sciage | 75.44 | — | — | — | — | — | not_computable_missing_synthesis_procurement |
| Poplar | trituration | 65.01 | 72.28 | 2.18 | 74.46 | -7.27 | -9.45 | computed |
| Poplar | total | 66.16 | — | — | — | — | — | not_computable_missing_synthesis_procurement |
| Pine | total | 101.09 | — | — | — | — | — | not_computable_missing_synthesis_procurement |
| Cedar | total | 80.58 | — | — | — | — | — | not_computable_missing_synthesis_procurement |

Pine and cedar have a purchase price but no matching T20 synthesis row, so their residual is not computable. Hardwood and poplar totals are purchase-only for the same reason. Product rows are not additive to a species total without published volumes.

**Headline SEPM.** Delivered purchase **107.22**, procurement before transfers **81.40**, transfers **25.01**, procurement after transfers **106.41**. Residual before transfers **25.82**; residual after transfers **0.81** CAD/m3. The after-transfer residual is small because nearly all of the pre-Crown surplus is transferred to the State.

**Product-level exceptions.** Hardwood sciage residual before transfers **5.69**, after transfers **-14.53** CAD/m3 (negative after transfers). Poplar trituration residual before transfers **-7.27**, after transfers **-9.45** CAD/m3 (negative on both definitions). Negative values are reported as published arithmetic, not clipped.

## Regional range (SEPM only, 2022)

Seven published regional groups have T20 synthesis procurement rows. They do not publish a regional purchase price, so the residual range below holds the provincial SEPM purchase price of **107.22** constant. It is a conditional procurement-cost range, not an observed regional net value.

| Region | n | Procurement before | Transfers | Procurement after | Residual before | Residual after |
|---|---:|---:|---:|---:|---:|---:|
| R01-R03-R11-R12 | 11 | 58.73 | 20.05 | 78.78 | 48.49 | 28.44 |
| R09 ⚠ | 3 | 96.58 | 21.51 | 118.10 | 10.64 | -10.88 |
| R02 | 6 | 82.09 | 29.77 | 111.86 | 25.13 | -4.64 |
| R04 | 4 | 73.43 | 29.99 | 103.42 | 33.79 | 3.80 |
| R14-R15-R07-R08 | 5 | 97.07 | 17.50 | 114.57 | 10.15 | -7.35 |
| R08 | 4 | 82.04 | 28.36 | 110.40 | 25.18 | -3.18 |
| R10 | 4 | 89.30 | 22.45 | 111.75 | 17.92 | -4.53 |

Range: procurement before **58.73–97.07**, after **78.78–118.10**; residual before **10.15–48.49**, after **-10.88–28.44** CAD/m3. R09 has `sample_n=3` and retains a three-respondent flag. Five regions have a negative after-transfer residual under the constant provincial purchase price: R02, R08, R09, R10, R14-R15-R07-R08. This does not mean their costs are wrong; it means the reported procurement total exceeds the provincial reference price for those groups.

## BMMB historical benchmark (nominal 2011–2015)

BMMB delivered auction results are a separate historical benchmark. They are **not** a 2022 price, **not** stumpage, and **not** a confirmed mill-gate price.

| Scope | Sales | Awarded | Full rates | Partial awards | Volume (m3) | Value (CAD) | Weighted (CAD/m3) | Median (CAD/m3) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| All years | 18 | 13 | 11 | 2 | 159,850 | 3,878,958.50 | 38.2940 | 36.6668 |
| 2011 | 6 | 3 | 3 | 0 | 29,550 | 340,387.00 | 37.8208 | 33.7000 |
| 2012 | 4 | 2 | 0 | 2 | 49,400 | 436,325.00 | — | — |
| 2014 | 1 | 1 | 1 | 0 | 4,300 | 221,018.00 | 51.3995 | 51.3995 |
| 2015 | 7 | 7 | 7 | 0 | 76,600 | 2,881,228.50 | 37.6139 | 36.6668 |

**Caveat:** nominal, 18 sales, no grade split. Eleven full rates cover 89,900 m3 and CAD 3,442,633.50; two 2012 partial awards (CAD 436,325) are excluded from the rate and retained only as lower bounds. No deflation is applied, so this table must not be compared with the 2022 survey as if it were the same price year. The archive does not publish species, grade, destination, or service-bundle allocation.

## QC total sensitivity (screening, M CAD)

QC allocation volumes are clearly mapped from the provincial allocation screening files. The survey SEPM residual is applied to each candidate total. This is a **sensitivity**, not an observed provincial total: it assumes all QC volume is SEPM, uses no species mix, and is not volume-weighted to the survey population.

| Case | QC volume (Mm3) | Volume source | Before transfers (M CAD) | After transfers (M CAD) |
|---|---:|---|---:|---:|
| 100m | 22.184 | `data/derived/national/harvest_basis/provincial_allocation/100m.csv` | 572.8 | 18.0 |
| 119m | 26.674 | `data/derived/national/harvest_basis/provincial_allocation/119m.csv` | 688.7 | 21.6 |
| 150m | 34.115 | `data/derived/national/harvest_basis/provincial_allocation/150m.csv` | 880.9 | 27.6 |

Sensitivity range: **572.8–880.9 M CAD** before transfers and **18.0–27.6 M CAD** after transfers. The after-transfer range is narrow because the SEPM after-transfer residual is only 0.81 CAD/m3.

## Validation

All **22** checks pass. The builder recomputes the T20 component identity, the transfer identity, every residual, the regional range, the BMMB weighted/median rate, and the sensitivity arithmetic. It fails closed on a missing row, duplicate key, unexpected unit, non-finite value, or arithmetic mismatch. T2 purchase rows are used once; the overlapping T21 purchase rows are used only as a cross-check.

## Non-claims and limitations

- Not an observed transaction net value.
- Not a policy result and not `policy_grade`.
- Not a mill margin; transformation and lumber revenue are excluded.
- Not a stumpage rate.
- Not a current or representative BMMB price.
- Not a provincial harvest-population estimate.
- Not merged into the ledger, Forest LP, or UI.
- Not deflated; BMMB remains nominal 2011–2015.
- Not species- or grade-allocated.
- Regional residuals are conditional on a constant provincial purchase price.
- The QC sensitivity uses screening allocation volumes, not observed harvest.

## Sources

- `data/derived/national/harvest_basis/qc_cost_survey_2022/qc_cost_revenue_survey.csv` (T2 and T20 synthesis rows).
- `data/derived/national/harvest_basis/bmmb_delivered/bmmb_delivered_sales.csv` (delivered-to-destination sales).
- `data/derived/national/harvest_basis/provincial_allocation/{100m,119m,150m}.csv` (QC screening volumes).
- `planning/forest-cost-revenue-ledger.md` (definitions and identity).

Reproduce with:

```bash
.venv/bin/python -m workflows.national.harvest.net_value_benchmark_v1
.venv/bin/python -m pytest tests/test_net_value_benchmark.py -q
```
