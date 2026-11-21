# Net-Value Evidence v2d

| Field | Value |
|---|---|
| Document | `data/derived/national/harvest_basis/net_value_v2d/NET_VALUE_V2D_REPORT.md` |
| Date | 2026-11-21 |
| Status | Evidence layer. No merged-ledger, model, UI, or public OSeCAN change. |
| QC source | `data/derived/national/harvest_basis/net_value_benchmark/` |
| BC sources | `bc_log_market/`, `bcts_bc/`, `bc_appraisal_costs/` |
| Net value | QC `benchmark_only`; BC `not_estimated` |

**Decision summary.** The QC 2022 survey benchmark is referenced, not recomputed.
BC has observed mill-delivered log-price averages, observed BCTS standing-timber
stumpage, and published appraisal cost allowances. BC has **no** published
general logging (tree-to-truck) or truck-haul $/m3: both are embedded in the
estimated winning bid (EWB). Therefore BC `net_value_status=not_estimated` with
reason `missing_logging_and_haul_cost`. No BC partial net value is computed, and
no combined national net value exists.

## 1. Evidence labels

| Label | Meaning | Used for |
|---|---|---|
| survey_benchmark | QC 2022 MRNF survey aggregate residual | QC reference only |
| benchmark_historical | BMMB 2011-2015 delivered-sale revenue | QC historical revenue reference only |
| observed_price | BC published mill-delivered log-market average | BC revenue/price range only |
| observed_stumpage | BC BCTS winning bid for standing timber | BC stumpage reference only; not delivered revenue |
| appraisal_allowance | BC IAM/CAM tabular cost allowance | BC partial cost coverage only; not observed cost |

## 2. QC reference (not re-derived)

The QC benchmark is validated against its own manifest and source CSVs. Values
below are exact source copies; no QC number is recomputed into a new definition.

| QC measure | Purchase | Before | Transfers | After | Residual before | Residual after |
|---|---|---|---|---|---|---|
| SEPM total | 107.2200 | 81.4000 | 25.0100 | 106.4100 | 25.8200 | 0.8100 |
| Hardwood sciage | 85.4200 | 79.7300 | 20.2200 | 99.9500 | 5.6900 | -14.5300 |
| Poplar trituration | 65.0100 | 72.2800 | 2.1800 | 74.4600 | -7.2700 | -9.4500 |

Regional SEPM conditional residual range: **10.1500 to 48.4900**
before transfers and **-10.8800 to 28.4400** after
transfers, holding the provincial SEPM purchase price constant. BMMB is a
separate nominal 2011-2015 delivered-sale revenue benchmark: weighted
**38.2940** CAD/m3, median **36.6668**
CAD/m3, 18 sales. It has no cost stack.

## 3. BC revenue/price benchmark

- 14815 period product cells from 505 source reports; the detailed CSV
  carries annual and period rows and is not a total.
- Blank source cells are missing, not zero.
- 16 exact-zero, 7 below CAD 1/m3, and 17 above CAD 1,000/m3 cells are retained
  with flags and excluded from the primary ranges; they are not clipped or filled.
- Interior `weighted_average` rows (`is_aggregate=true`) are reported separately
  and never added to product cells.
- One-month and three-month vintages are separate series. Neither is annualized,
  and overlapping three-month windows are not summed with monthly reports.
- Coast old growth is a published blend of old and mixed growth.

### 3.1 Period price ranges by published vintage

| Region | Vintage | Log class | Cells | Reports | Plausible | Flagged | Min | P25 | Median | P75 | Max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| coast | 1_month | old_growth | 4164 | 85 | 4149 | 15 | 2.4400 | 53.6000 | 92.8300 | 241.7700 | 999.5600 |
| coast | 1_month | second_growth | 1889 | 84 | 1884 | 5 | 1.4900 | 62.7375 | 100.9750 | 192.3000 | 805.0200 |
| coast | 3_month | old_growth | 4700 | 84 | 4682 | 18 | 2.7600 | 52.7400 | 94.3050 | 261.7400 | 987.2100 |
| coast | 3_month | second_growth | 2375 | 83 | 2373 | 2 | 1.0700 | 59.2900 | 101.0000 | 212.7400 | 900.8100 |
| interior | 1_month | not_reported | 791 | 85 | 791 | 0 | 37.9500 | 62.6500 | 109.3400 | 144.8100 | 624.3800 |
| interior | 3_month | not_reported | 896 | 84 | 896 | 0 | 35.4800 | 60.5975 | 103.0850 | 143.4975 | 350.9500 |

Cross-grade/cross-species ranges are wide by construction. The detailed CSV
carries annual and period rows by region, grade or end use, and species.

### 3.2 BCTS observed stumpage

| Measure | Value |
|---|---|
| Awarded sales | 51 |
| Full winning-bid sales | 49 |
| Premium-only lower bounds | 2 |
| Sale volume (m3) | 1313211.0000 |
| Full-bid volume (m3) | 1253065.0000 |
| Volume-weighted stumpage (CAD/m3) | 42.7913 |
| Median full bid (CAD/m3) | 45.2800 |
| Full-bid range (CAD/m3) | 0.2513 to 257.3077 |

Stumpage is a bid for standing timber, not delivered-log revenue. It is kept
separate from the mill-delivered log-price averages.

## 4. BC cost coverage and gap

| Component | Coverage | Rows | Bases | Direct CAD/m3 rows | Usable | Missing reason |
|---|---|---|---|---|---|---|
| road | published_appraisal_allowance | 124 | CAD/km;CAD/km/%;CAD/m3 | 22 | requires_site_conversion |  |
| bridge | published_appraisal_allowance | 260 | CAD/each | 0 | requires_site_conversion |  |
| culvert | published_appraisal_allowance | 207 | CAD/each;CAD/m | 0 | requires_site_conversion |  |
| silviculture | published_appraisal_allowance | 247 | CAD/ha;CAD/m3 | 14 | partially_direct |  |
| specified_operations | published_appraisal_allowance | 19 | CAD/m3;CAD/m3/km;CAD/tree | 15 | conditional_route_specific |  |
| tenure_obligation | published_appraisal_allowance | 17 | CAD/ha;CAD/ha/%;CAD/ha/stem;CAD/m3 | 11 | partially_direct |  |
| logging | not_published | 0 |  | 0 | no | logging_not_published_embedded_in_ewb |
| truck_haul | partial_appraisal_allowance | 5 | CAD/m3 | 5 | no | general_truck_haul_not_published_embedded_in_ewb |
| estimated_winning_bid | not_published_as_cost | 0 |  | 0 | no | ewb_is_stumpage_formula_embedding_logging_and_haul |
| full_bc_net_value | not_estimated | 0 |  | 0 | no | missing_logging_and_haul_cost |

All 879 cost rows are `appraisal_allowance`, not observed contractor costs. The
covered components use different units (CAD/km, CAD/each, CAD/ha, CAD/m3) and
cannot be summed into a single $/m3 without road length, structure counts,
treated area, and harvest volume.

**Stop rule.** A BC number computed as `log price - road allowance - silviculture allowance` (or any subset of the published allowances) is **not** net value. It omits logging and general truck haul, mixes CAD/m3 with CAD/km and CAD/each without site quantities, and treats appraisal allowances as observed costs.

## 5. QC + BC comparison (explicitly non-comparable)

| Dimension | QC 2022 survey benchmark | BC 2026 evidence | Comparability |
|---|---|---|---|
| Evidence tier | survey_benchmark | observed_price + observed_stumpage + appraisal_allowance | Not comparable: different evidence classes |
| Revenue basis | delivered-to-mill survey purchase price, nominal 2022 | mill-delivered published averages (2019-2026) and standing-timber BCTS bids (2026) | Not comparable: different price point and year |
| Cost coverage | full survey procurement stack: harvest, road, haul, hosting, other, transfers | partial appraisal allowances: road, bridge, culvert, silviculture, specified operations, TOA; missing logging, general truck haul, EWB | Not comparable: BC has no logging or general truck-haul cost |
| Net value | benchmark_only: SEPM 25.82 before / 0.81 after transfers CAD/m3; regional conditional 10.15-48.49 / -10.88-28.44 | not_estimated; reason missing_logging_and_haul_cost | Not comparable: QC benchmark vs BC partial coverage |
| Policy grade | false | false | Neither is policy-grade |

## 6. Validation

All 29 checks passed:

| Check | Status | Detail |
|---|---|---|
| bc_price_cell_count | pass | 15705 cells (expected 15705) |
| bc_price_report_count | pass | 505 reports (expected 505) |
| bc_price_observation_labels | pass | regions and vintages are in the allowed set |
| bc_price_hard_range_and_nonnegative | pass | all prices are within 0-2000 CAD/m3 |
| bc_price_flag_counts | pass | zero=16, below_1=7, above_1000=17 |
| bc_price_flagged_cells_excluded_from_ranges | pass | no zero or negative value enters an ok range |
| bc_price_aggregation_role_separation | pass | weighted-average rows are separate from product cells |
| bc_price_product_cells_exclude_aggregate | pass | no is_aggregate=true row appears as a product cell |
| bc_price_no_vintage_mixing | pass | each range has one published vintage and is marked non-additive |
| bc_price_annual_report_limit | pass | at most 12 published reports per series-year; three-month windows still overlap |
| bc_price_cell_key_unique | pass | 15705 unique report/species/grade/end-use keys |
| bc_interior_aggregate_rows | pass | 890 Interior weighted-average cells kept outside product sums |
| bc_interior_aggregate_within_product_range | pass | 890 aggregate cells checked against product siblings |
| bc_interior_volume_sum_excludes_aggregate | pass | 169 Interior reports reconciled; 0 violations |
| bc_stumpage_sale_count | pass | 51 awarded sales (expected 51) |
| bc_stumpage_full_and_lower_bound_split | pass | full=49, lower_bound=2 |
| bc_stumpage_nonnegative_and_labeled | pass | all observed stumpage totals are nonnegative and carry a basis label |
| bc_cost_row_count | pass | 879 appraisal rows assigned (expected 879) |
| bc_cost_appraisal_vs_observed | pass | all cost rows are appraisal allowances or explicitly unavailable; none is observed cost |
| bc_cost_missing_components | pass | logging, general truck haul, and EWB are explicitly missing |
| bc_cost_no_full_net_value | pass | full BC net value row is explicitly not estimated |
| qc_reference_row_count | pass | 14 QC references (3 provincial + 7 regional + 3 sensitivity + 1 historical) |
| qc_reference_labels | pass | all QC references are validated copies with policy_grade=false |
| qc_sepm_values_match_source | pass | SEPM 107.22 purchase and 25.82/0.81 residuals match the QC source |
| bc_net_value_reason_present | pass | 8 BC summary rows all not_estimated/missing_logging_and_haul_cost |
| no_combined_national_net_value | pass | no national combined net-value row exists |
| evidence_tiers_separated | pass | BC observed price, observed stumpage, and appraisal allowance rows are distinct |
| policy_grade_false | pass | policy_grade=false on every summary and QC reference row |
| no_undocumented_negative_values | pass | QC negative residuals are documented; no negative BC price, stumpage, or cost |

## 7. Non-claims

- Not an observed transaction net value.
- Not policy-grade; `policy_grade=false` on every row.
- Not a BC full net value and not a BC partial net value.
- Not a combined national net value.
- Not a mill margin; transformation and by-product revenue are excluded.
- Not a stumpage rate for QC and not a delivered-log price for BCTS.
- Not an observed contractor cost; appraisal allowances are policy inputs.
- Not merged into `forest_cost_revenue.csv`, the Forest LP, the UI, or OSeCAN.
- Not deflated; years and currency bases remain separate.
- Not a legal AAC, sustainable-supply estimate, or forecast.

## 8. What would unlock BC net value

1. A public or authorized general logging/tree-to-truck $/m3 and a general
   truck-haul $/m3, or a documented decomposition of the EWB into its cost
   components. The restricted ILCR/CCTMCS microdata were not used.
2. Site quantities to convert allowances: road km, bridge and culvert counts,
   treated hectares, and harvest volume by appraisal zone.
3. A region/grade/volume weighting for the log-price series and a matching
   cost vintage. Until then, only revenue, stumpage, and partial allowance
   coverage are reported.

## 9. Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.net_value_v2d
.venv/bin/python -m pytest tests/test_net_value_v2d.py -q
.venv/bin/ruff check workflows/national/harvest/net_value_v2d.py tests/test_net_value_v2d.py
```

Outputs: `v2d_net_value_summary.csv`, `bc_revenue_benchmark.csv`, `bc_observed_stumpage.csv`,
`bc_cost_coverage.csv`, `qc_reference.csv`, `summary.json`, `manifest.json`.
