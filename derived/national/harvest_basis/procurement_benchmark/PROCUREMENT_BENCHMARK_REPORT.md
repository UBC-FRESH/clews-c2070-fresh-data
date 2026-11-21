# QC procurement cost benchmark — 2022 survey and BMMB delivered sales

**Status:** procurement-cost benchmark only. Generated 2026-11-21T23:25:01Z. `net_value_status=not_estimated`; `interpretation=purchased_vs_bgad_procurement_cost_spread`; `policy_grade=false` on every row.

This note replaces the earlier framing of the 2022 survey difference as a forest-sector residual or net value. It is a **procurement-channel cost spread across different respondent samples**, not forest net value, not a mill margin, and not a policy result. The old `net_value_benchmark` artifact is retained only for audit and is marked deprecated. No QC or M CAD volume-scaled diagnostic is produced, and the builder does not read `provincial_allocation/`.

## Definitions

| Term | Definition |
|---|---|
| Purchase cost | Survey T2 `purchase.wood_purchase_delivered`: buyer-side procurement cost including purchase, State transfers, transport/unloading, and road costs where applicable. It is not observed log-sale revenue. |
| BGAD before transfers | Survey T20 `synthesis_procurement.procurement_total_before_transfers`: harvest + road + haul + hosting + other costs. |
| Transfers | Survey T20 `synthesis_procurement.transfers_total`: payments to the State. |
| BGAD after transfers | Survey T20 `synthesis_procurement.procurement_total_after_transfers`. |
| Cost spread before | `purchase cost - BGAD before transfers` (procurement-channel difference). |
| Cost spread after | `purchase cost - BGAD after transfers` (procurement-channel difference). |

The arithmetic identity is `BGAD before + transfers = BGAD after`, so `cost spread before - cost spread after = transfers`. That identity does not turn the spread into net value.

## Accounting caveats

- T2 purchase is a **buyer-side procurement cost**, not observed log-sale revenue or stumpage.
- T20 BGAD excludes species gain/loss (reported separately in T22); for SEPM the exclusion is larger than the after-transfer spread.
- PRCCM road rebates sit inside T10/T20 `transfers_total`, not in the T20 `road` component. Do not combine `T5.road_total_after_prccm` with `T10.transfers_total`; that would double-count the rebate.
- Purchase and BGAD cover different respondent samples. Their difference is a channel cost spread, not an arm's-length forest-sector net value.

## Provincial procurement cost benchmark (2022, CAD/m3 nominal)

| Species | Product | Purchase cost | BGAD before | Transfers | BGAD after | Spread before | Spread after | Status |
|---|---|---:|---:|---:|---:|---:|---:|---|
| SEPM | total | 107.22 | 81.40 | 25.01 | 106.41 | 25.82 | 0.81 | computed |
| Hardwood | sciage | 85.42 | 79.73 | 20.22 | 99.95 | 5.69 | -14.53 | computed |
| Hardwood | trituration | 79.45 | — | — | — | — | — | not_computable_missing_bgad_synthesis |
| Hardwood | total | 80.95 | — | — | — | — | — | not_computable_missing_bgad_synthesis |
| Poplar | sciage | 75.44 | — | — | — | — | — | not_computable_missing_bgad_synthesis |
| Poplar | trituration | 65.01 | 72.28 | 2.18 | 74.46 | -7.27 | -9.45 | computed |
| Poplar | total | 66.16 | — | — | — | — | — | not_computable_missing_bgad_synthesis |
| Pine | total | 101.09 | — | — | — | — | — | not_computable_missing_bgad_synthesis |
| Cedar | total | 80.58 | — | — | — | — | — | not_computable_missing_bgad_synthesis |

Pine and cedar have a purchase cost but no matching T20 BGAD synthesis row, so their spread is not computable. Hardwood and poplar totals are purchase-only for the same reason. Product rows are not additive to a species total without published volumes.

**SEPM headline.** Purchase cost **107.22**, BGAD before transfers **81.40**, transfers **25.01**, BGAD after transfers **106.41**. The before-transfer channel spread is **25.82** and the after-transfer channel spread is **0.81** CAD/m3. The after-transfer spread is small because nearly all of the pre-transfer difference is accounted for by transfers; it is still a cost spread, not net value.

**Product-level exceptions.** Hardwood sciage spread before transfers **5.69**, after transfers **-14.53** CAD/m3. Poplar trituration spread before transfers **-7.27**, after transfers **-9.45** CAD/m3. Negative spreads are reported as published arithmetic, not clipped, and are not evidence of an error by themselves.

## Regional conditional range (SEPM only, 2022)

The seven regional groups come from **REG `regional_2022`**, `Compilation_donnees_regionalisees_2022.pdf`, not from T20. They publish regional BGAD procurement costs but no regional purchase cost. The conditional spread below holds the provincial SEPM purchase cost of **107.22** constant. It is not an observed regional net value.

| Region | n | BGAD before | Transfers | BGAD after | Conditional spread before | Conditional spread after |
|---|---:|---:|---:|---:|---:|---:|
| R01-R03-R11-R12 | 11 | 58.73 | 20.05 | 78.78 | 48.49 | 28.44 |
| R02 | 6 | 82.09 | 29.77 | 111.86 | 25.13 | -4.64 |
| R04 | 4 | 73.43 | 29.99 | 103.42 | 33.79 | 3.80 |
| R08 | 4 | 82.04 | 28.36 | 110.40 | 25.18 | -3.18 |
| R09 (n=3) | 3 | 96.58 | 21.51 | 118.10 | 10.64 | -10.88 |
| R10 | 4 | 89.30 | 22.45 | 111.75 | 17.92 | -4.53 |
| R14-R15-R07-R08 | 5 | 97.07 | 17.50 | 114.57 | 10.15 | -7.35 |

Range: BGAD before **58.73–97.07**, after **78.78–118.10**; conditional spread before **10.15–48.49**, after **-10.88–28.44** CAD/m3. R09 has `sample_n=3` and carries the three-respondent flag. Regions with a negative after-transfer conditional spread: R02, R08, R09, R10, R14-R15-R07-R08. The min/max bound rows in the CSV are independent column-wise extrema across the seven groups, so horizontal identities such as `before + transfers = after` do not hold across a bound row. The bound rows also retain the three-respondent flag.

## BMMB delivered-sale benchmark (nominal CAD)

BMMB delivered auction results are a separate historical benchmark. They are **not** a 2022 price, **not** stumpage, and **not** a confirmed mill-gate price. **Crown public-forest sales are the primary series.** Teaching and research forest sales are shown separately; the all-in pooled rate is secondary.

| Scope | Sales | Full rates | Partial awards | Offered vol. (m3) | Awarded val. (CAD) | Rate vol. (m3) | Rate val. (CAD) | Weighted (CAD/m3) | Median (CAD/m3) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Crown public forest, 2011–2015 (primary) | 16 | 9 | 2 | 144,500 | 3,101,840.50 | 74,550 | 2,665,515.50 | 35.7547 | 34.2849 |
| Teaching/research forest, 2014–2015 | 2 | 2 | 0 | 15,350 | 777,118.00 | 15,350 | 777,118.00 | 50.6266 | 50.8627 |
| All delivered, 2011–2015 | 18 | 11 | 2 | 159,850 | 3,878,958.50 | 89,900 | 3,442,633.50 | 38.2940 | 36.6668 |
| All delivered, 2011 | 6 | 3 | 0 | 29,550 | 340,387.00 | 9,000 | 340,387.00 | 37.8208 | 33.7000 |
| All delivered, 2012 | 4 | 0 | 2 | 49,400 | 436,325.00 | 0 | 0.00 | — | — |
| All delivered, 2014 | 1 | 1 | 0 | 4,300 | 221,018.00 | 4,300 | 221,018.00 | 51.3995 | 51.3995 |
| All delivered, 2015 | 7 | 7 | 0 | 76,600 | 2,881,228.50 | 76,600 | 2,881,228.50 | 37.6139 | 36.6668 |

**Crown-only primary rate:** 2,665,515.50 / 74,550 = **35.7547 CAD/m3** over 9 full-rate sales. Teaching/research: 777,118.00 / 15,350 = **50.6266 CAD/m3** over 2 sales. All-in: 3,442,633.50 / 89,900 = **38.2940 CAD/m3**.

**Re-offer caveat.** The 2012 archive re-offers 2 lots (22,200 m3), double-counting offered and awarded volume totals. The full-rate numerator and denominator are unaffected because those two sales are excluded: one is a partial award and one is unsold. Offered volume is not the rate denominator.

The per-year rows in the CSV carry per-year counts and per-year price-year bases. No deflation is applied. The archive does not publish species, grade, destination, or service-bundle allocation.

## Validation

All **20** checks pass. The builder recomputes the T20 component identity, the transfer identity, every provincial and regional cost spread, the BMMB Crown/teaching/all-in rates, per-year counts, and the re-offer overlap. It fails closed on missing rows, duplicate keys, unexpected units, unexpected survey years, non-finite values, non-binary booleans, malformed rates, and arithmetic mismatches. T2 purchase rows are used once; the overlapping T21 purchase rows are used only as a cross-check.

## Non-claims and limitations

- Not a forest net value; `net_value_status=not_estimated`.
- Not an observed transaction and not a policy result.
- Not `policy_grade`.
- Not a mill margin; transformation and lumber revenue are excluded.
- Not a stumpage rate.
- Not a current or representative BMMB price.
- Not a provincial harvest-population estimate.
- Not merged into the ledger, Forest LP, UI, or OSeCAN.
- Not deflated; BMMB remains nominal 2011–2015.
- Not species- or grade-allocated.
- No volume-scaled M CAD diagnostic is produced.

## Sources

- `data/derived/national/harvest_basis/qc_cost_survey_2022/qc_cost_revenue_survey.csv` (T2 purchase cost and T20 BGAD synthesis rows).
- `data/derived/national/harvest_basis/qc_cost_survey_2022/README.md` and `manifest.json` (accounting caveats and provenance).
- `data/derived/national/harvest_basis/qc_cost_survey_2022/qc_cost_revenue_survey.csv` REG `regional_2022` rows from `Compilation_donnees_regionalisees_2022.pdf` (regional costs).
- `data/derived/national/harvest_basis/bmmb_delivered/bmmb_delivered_sales.csv` (delivered-to-destination sales).

Reproduce with:

```bash
.venv/bin/python -m workflows.national.harvest.procurement_benchmark_v1
.venv/bin/python -m pytest tests/test_procurement_benchmark.py -q
```
