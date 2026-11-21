# Forest Economics Evidence v2d

| Field | Value |
|---|---|
| Document | `data/derived/national/harvest_basis/forest_economics_v2d/FOREST_ECONOMICS_V2D_REPORT.md` |
| Date | 2026-11-21 |
| Status | Evidence layer. No merged-ledger, model, UI, or public OSeCAN change. |
| QC source | `data/derived/national/harvest_basis/procurement_benchmark/` |
| BC sources | `bc_log_market/`, `bcts_bc/`, `bc_appraisal_costs/` |
| Net value | QC and BC both `not_estimated` |

**Decision summary.** Neither jurisdiction has a defensible net value. QC
`107.22` is a buyer-side procurement cost, not revenue; `25.82` and `0.81`
CAD/m3 are procurement-channel cost spreads. BC has observed mill-delivered
price averages, observed BCTS standing-timber stumpage, and partial appraisal
allowances, but no public general logging (tree-to-truck) or truck-haul $/m3.
BC `net_value_status=not_estimated` with reason `missing_logging_and_haul_cost`.
No BC partial net value is computed and no combined national net value exists.

## 1. Evidence classes

| Evidence tier | What it is | What it is not |
|---|---|---|
| `survey_procurement_cost` | QC 2022 T2 purchase cost vs T20 BGAD cost | Not revenue, not a transaction, not net value |
| `survey_regional_procurement_cost` | QC 2022 regional conditional cost spread | Not an observed regional price or net value |
| `benchmark_historical` | BMMB 2011-2015 delivered-sale rate, nominal | Not a current price, not a cost stack, not net value |
| `observed_price` | BC published mill-delivered average | Not a transaction, not a complete population |
| `observed_stumpage` | BC BCTS winning bid for standing timber | Not delivered-log revenue |
| `appraisal_allowance` | BC IAM/CAM tabular allowance | Not an observed contractor cost or payment |
| `not_available` | Missing logging, truck haul, or full net value | Not zero |

## 2. QC procurement reference

The QC rows are exact validated copies of the procurement benchmark. The
T2/T20 difference is a **cost spread**, not revenue and not net value.

| Scope | Purchase | BGAD before | Transfers | BGAD after | Spread before | Spread after | Status |
|---|---|---|---|---|---|---|---|
| SEPM total | 107.2200 | 81.4000 | 25.0100 | 106.4100 | 25.8200 | 0.8100 | computed |
| Hardwood sciage | 85.4200 | 79.7300 | 20.2200 | 99.9500 | 5.6900 | -14.5300 | computed |
| Poplar trituration | 65.0100 | 72.2800 | 2.1800 | 74.4600 | -7.2700 | -9.4500 | computed |

Regional conditional range: 10.15 to
48.49 CAD/m3 before
transfers and -10.88 to
28.44 CAD/m3 after
transfers, holding the provincial SEPM purchase cost constant. Bound rows are
independent column-wise extrema and are not additive ranges.

## 3. BMMB historical delivered-sale reference

| Scope | Role | Full rates | Rate volume (m3) | Weighted | Median | Min | Max | Basis |
|---|---|---|---|---|---|---|---|---|
| crown_public_forest | primary | 9 | 74550.0000 | 35.7547 | 34.2849 | 30.1042 | 43.6385 | CAD_nominal |
| teaching_research_forest | separate | 2 | 15350.0000 | 50.6266 | 50.8627 | 50.3258 | 51.3995 | CAD_nominal |
| all_delivered | secondary | 11 | 89900.0000 | 38.2940 | 36.6668 | 30.1042 | 51.3995 | CAD_nominal |

The Crown-only row is primary. Teaching/research is separate. The all-in row is
secondary and mixes Crown and teaching lots. All values are nominal 2011-2015
delivered-sale rates with no deflation, grade split, species allocation, or cost
stack. They are not stumpage and not net value.

## 4. BC revenue evidence

| Region | Vintage | Log class | Cells | Reports | Plausible | Flagged | Min | P25 | Median | P75 | Max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| coast | 1_month | old_growth | 4164 | 85 | 4149 | 15 | 2.4400 | 53.6000 | 92.8300 | 241.7700 | 999.5600 |
| coast | 1_month | second_growth | 1889 | 84 | 1884 | 5 | 1.4900 | 62.7375 | 100.9750 | 192.3000 | 805.0200 |
| coast | 3_month | old_growth | 4700 | 84 | 4682 | 18 | 2.7600 | 52.7400 | 94.3050 | 261.7400 | 987.2100 |
| coast | 3_month | second_growth | 2375 | 83 | 2373 | 2 | 1.0700 | 59.2900 | 101.0000 | 212.7400 | 900.8100 |
| interior | 1_month | not_reported | 791 | 85 | 791 | 0 | 37.9500 | 62.6500 | 109.3400 | 144.8100 | 624.3800 |
| interior | 3_month | not_reported | 896 | 84 | 896 | 0 | 35.4800 | 60.5975 | 103.0850 | 143.4975 | 350.9500 |

Blank source cells are missing, not zero. The 16 exact-zero, 7 below CAD 1/m3,
and 17 above CAD 1,000/m3 cells are retained with flags and excluded from the
plausible ranges; they are not clipped or filled. Interior `weighted_average`
rows (`is_aggregate=true`) are reported separately and never added to product
cells. One-month and three-month vintages are separate; neither is annualized,
and overlapping three-month windows are not summed. Coast old growth is a
published blend of old and mixed growth.

### 4.1 BCTS observed stumpage

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

Stumpage is a bid for standing timber, not delivered-log revenue, and is kept
separate from the mill-delivered price averages.

## 5. BC cost coverage

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

All 879 cost rows are appraisal allowances, not observed contractor costs. The
covered components use different units (CAD/km, CAD/each, CAD/ha, CAD/m3) and
cannot be summed into one $/m3 without road length, structure counts, treated
area, and harvest volume.

**Stop rule.** A number computed as `log price - road allowance - silviculture
allowance` (or any other subset of the published allowances) is **not** net
value. It omits general logging and truck haul, mixes units without site
quantities, and treats appraisal allowances as observed costs.

## 6. Summary statuses

| Jurisdiction | Evidence | Revenue measure | Cost coverage | Net value | Reason |
|---|---|---|---|---|---|
| QC | survey_procurement_cost | none | full_survey_procurement_stack | not_estimated | qc_procurement_cost_benchmark_not_net_value |
| QC | survey_regional_procurement_cost | none | regional_sepm_procurement_only | not_estimated | conditional_regional_cost_spread_not_net_value |
| QC | benchmark_historical | bmmb_delivered_sale_rate | revenue_only_no_cost_stack | not_estimated | revenue_benchmark_only_no_cost_stack |
| QC | benchmark_historical | bmmb_delivered_sale_rate | revenue_only_no_cost_stack | not_estimated | revenue_benchmark_only_no_cost_stack |
| QC | benchmark_historical | bmmb_delivered_sale_rate | revenue_only_no_cost_stack | not_estimated | revenue_benchmark_only_no_cost_stack |
| BC | observed_price | all_reported_grades_or_end_uses_and_species | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | observed_price | all_reported_grades_or_end_uses_and_species | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | observed_price | all_reported_grades_or_end_uses_and_species | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | observed_price | all_reported_grades_or_end_uses_and_species | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | observed_price | all_reported_grades_or_end_uses_and_species | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | observed_price | all_reported_grades_or_end_uses_and_species | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | observed_stumpage | bcts_winning_bid | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | appraisal_allowance | none | partial_appraisal_allowance_missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |
| BC | not_available | none | missing_logging_and_haul | not_estimated | missing_logging_and_haul_cost |

## 7. Validation

All 36 checks passed:

| Check | Status | Detail |
|---|---|---|
| procurement_manifest_labels | pass | every QC procurement reference is not_estimated, policy_grade=false, and a cost spread |
| qc_reference_row_count | pass | 18 references (9 provincial + 9 regional) |
| qc_sepm_values_match_procurement_benchmark | pass | SEPM 107.22 / 81.40 / 25.01 / 106.41 / 25.82 / 0.81 match the source |
| qc_no_withdrawn_wording | pass | QC references carry no withdrawn legacy framing terms |
| bmmb_reference_row_count | pass | 3 all-year BMMB references |
| bmmb_primary_teaching_secondary | pass | Crown-only 35.7547 primary, teaching 50.6266, all-in 38.2940 secondary |
| bmmb_nominal_no_net_value | pass | BMMB is nominal historical revenue with no cost stack and no net value |
| bc_price_cell_count | pass | 15705 cells (expected 15705) |
| bc_price_report_count | pass | 505 reports (expected 505) |
| bc_price_hard_range_and_nonnegative | pass | all prices are within 0-2000 CAD/m3 |
| bc_price_flag_counts | pass | zero=16, below_1=7, above_1000=17 |
| bc_price_is_aggregate_lowercase | pass | source is_aggregate tokens are lowercase true/false with 890 aggregates |
| bc_price_flagged_cells_excluded_from_ranges | pass | no zero or negative value enters an ok range |
| bc_price_product_cells_exclude_aggregate | pass | no is_aggregate=true row appears as a product cell |
| bc_price_no_double_count | pass | 1,748 product-cell rows and 104 aggregate-reference rows are separate |
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
| bc_cost_no_partial_net_value | pass | full BC net value is explicitly not estimated; no component is net-value usable |
| summary_all_not_estimated | pass | 14 summary rows all not_estimated with a reason |
| summary_policy_grade_false | pass | policy_grade=false on every summary row |
| summary_no_combined_national_net_value | pass | no national combined net-value row exists |
| summary_no_net_value_amounts | pass | summary rows have no monetary net-value field |
| summary_qc_revenue_not_reported | pass | QC procurement rows do not present buyer-side cost as revenue |
| summary_bc_revenue_nonnegative | pass | no negative BC revenue or stumpage range |
| summary_evidence_tiers_separated | pass | QC cost, historical, BC price, stumpage, allowance, and unavailable rows are distinct |
| no_nonfinite_output_text | pass | no NaN or infinity text in generated rows |

## 8. Non-claims

- Not an observed transaction net value.
- Not policy-grade; `policy_grade=false` on every summary row.
- Not a BC full net value and not a BC partial net value.
- Not a combined national net value; QC and BC monetary totals are never added.
- Not a mill margin; transformation and by-product revenue are excluded.
- Not a QC stumpage rate and not a BCTS delivered-log price.
- Not an observed contractor cost; appraisal allowances are policy inputs.
- Not merged into `forest_cost_revenue.csv`, the Forest LP, the UI, or OSeCAN.
- Not deflated; years and currency bases remain separate.
- Not a legal AAC, sustainable-supply estimate, or forecast.

## 9. What would unlock a real net value

1. A public or authorized general logging/tree-to-truck $/m3, general truck-haul
   $/m3, and a documented decomposition of the EWB into cost components.
2. Site quantities to convert allowances: road km, bridge and culvert counts,
   treated hectares, and harvest volume by appraisal zone.
3. A region/grade/volume weighting for the log-price series and a cost stack from
   a matching vintage.
4. For QC, an observed log-sale revenue series at the same basis and vintage as
   the cost stack; purchase cost alone cannot supply revenue.

## 10. Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.forest_economics_v2d
.venv/bin/python -m pytest tests/test_forest_economics_v2d.py -q
.venv/bin/ruff check workflows/national/harvest/forest_economics_v2d.py tests/test_forest_economics_v2d.py
```

Outputs: `forest_economics_v2d_summary.csv`, `qc_procurement_reference.csv`, `bc_revenue_benchmark.csv`,
`bc_cost_coverage.csv`, `bmmb_reference.csv`, `summary.json`, `manifest.json`.
