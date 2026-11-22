# Province break-even delivered price

Generated: 2026-11-22T18:26:59+00:00

## Purpose and labels

This artifact computes a central break-even delivered price for the 13 Canadian jurisdictions from the committed v2.3 national cost model. It is a `model_estimate_not_policy` diagnostic: `observed=false`, `policy_grade=false` and `combined_national_net_value=false`. It is not a policy result.

Break-even = central modeled total delivered cost in CAD/m3. Margin = price - break-even. Gap to break-even = break-even - price. Negative values are retained unclipped.

## Cost basis

| Province | Cost basis | Components | Low | Central | High | Double-count guard |
|---|---|---|---:|---:|---:|---|
| BC | `component_sum` | logging_haul;road;silviculture | 36.4300 | 74.2400 | 165.0500 | `component_stack_summed_once` |
| AB | `industry_aggregate_proxy` | industry_aggregate_proxy | 54.9865 | 54.9865 | 54.9865 | `single_industry_aggregate_no_addons` |
| SK | `industry_aggregate_proxy` | industry_aggregate_proxy | 36.4209 | 36.4209 | 36.4209 | `single_industry_aggregate_no_addons` |
| MB | `industry_aggregate_proxy` | industry_aggregate_proxy | 52.8705 | 52.8705 | 52.8705 | `single_industry_aggregate_no_addons` |
| ON | `industry_aggregate_proxy` | industry_aggregate_proxy | 83.7293 | 83.7293 | 83.7293 | `single_industry_aggregate_no_addons` |
| QC | `component_sum` | harvest;haul;road;silviculture | 60.9000 | 83.3700 | 104.7000 | `component_stack_summed_once` |
| NB | `industry_aggregate_proxy` | industry_aggregate_proxy | 98.6665 | 98.6665 | 98.6665 | `single_industry_aggregate_no_addons` |
| NS | `industry_aggregate_proxy` | industry_aggregate_proxy | 39.5231 | 39.5231 | 39.5231 | `single_industry_aggregate_no_addons` |
| NL | `industry_aggregate_proxy` | industry_aggregate_proxy | 36.1178 | 36.1178 | 36.1178 | `single_industry_aggregate_no_addons` |
| PE | `industry_aggregate_proxy` | industry_aggregate_proxy | 45.1715 | 45.1715 | 45.1715 | `single_industry_aggregate_no_addons` |
| YT | `industry_aggregate_proxy` | industry_aggregate_proxy | 24.1835 | 24.1835 | 24.1835 | `single_industry_aggregate_no_addons` |
| NT | `industry_aggregate_proxy` | industry_aggregate_proxy | 4.5855 | 4.5855 | 4.5855 | `single_industry_aggregate_no_addons` |
| NU | `donor_fallback_total` | total_cost_fallback | 52.0003 | 86.9381 | 180.2789 | `donor_total_fallback_no_addons` |

BC and QC sum their v2.3 component stacks once. The ten aggregate-proxy provinces use one StatCan NAICS 11331 total-cost proxy and receive no separate road, silviculture or haul add-on. Nunavut uses the explicit v2.2 donor-total fallback.

## Break-even and price comparison

| Province | Break-even | Donor price | Donor margin | Donor gap | Donor class | Scaled price | Scaled margin | Scaled gap | Scaled class | Classification |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|---|
| BC | 74.2400 | 115.8280 | 41.5880 | -41.5880 | `positive_margin` | 115.8280 | 41.5880 | -41.5880 | `positive_margin` | **`positive_margin`** |
| AB | 54.9865 | 115.8280 | 60.8415 | -60.8415 | `positive_margin` | 18.6607 | -36.3258 | 36.3258 | `negative_margin` | **`cost_limited`** |
| SK | 36.4209 | 115.8280 | 79.4071 | -79.4071 | `positive_margin` | 52.8101 | 16.3892 | -16.3892 | `positive_margin` | **`positive_margin`** |
| MB | 52.8705 | 115.8280 | 62.9575 | -62.9575 | `positive_margin` | 22.2039 | -30.6666 | 30.6666 | `negative_margin` | **`cost_limited`** |
| ON | 83.7293 | 115.8280 | 32.0987 | -32.0987 | `positive_margin` | 22.7775 | -60.9518 | 60.9518 | `negative_margin` | **`cost_limited`** |
| QC | 83.3700 | 115.8280 | 32.4580 | -32.4580 | `positive_margin` | 47.5123 | -35.8577 | 35.8577 | `negative_margin` | **`cost_limited`** |
| NB | 98.6665 | 115.8280 | 17.1615 | -17.1615 | `price_limited` | 84.5300 | -14.1365 | 14.1365 | `price_limited` | **`price_limited`** |
| NS | 39.5231 | 115.8280 | 76.3049 | -76.3049 | `positive_margin` | 122.8300 | 83.3069 | -83.3069 | `positive_margin` | **`positive_margin`** |
| NL | 36.1178 | 115.8280 | 79.7102 | -79.7102 | `positive_margin` | 115.8280 | 79.7102 | -79.7102 | `positive_margin` | **`positive_margin`** |
| PE | 45.1715 | 115.8280 | 70.6565 | -70.6565 | `positive_margin` | 115.8280 | 70.6565 | -70.6565 | `positive_margin` | **`positive_margin`** |
| YT | 24.1835 | 115.8280 | 91.6445 | -91.6445 | `positive_margin` | 115.8280 | 91.6445 | -91.6445 | `positive_margin` | **`positive_margin`** |
| NT | 4.5855 | 115.8280 | 111.2425 | -111.2425 | `positive_margin` | 115.8280 | 111.2425 | -111.2425 | `positive_margin` | **`positive_margin`** |
| NU | 86.9381 | 115.8280 | 28.8899 | -28.8899 | `positive_margin` | 115.8280 | 28.8899 | -28.8899 | `positive_margin` | **`positive_margin`** |

Classification counts: positive_margin 8, negative_margin 0, price_limited 1, cost_limited 4. The price-limited band is 15.0 CAD/m3 or 20% of break-even. A province can be negative under one scenario and still be classified by its binding constraint; the negative-margin province lists below use the raw margin signs.

## Donor versus scaled

The donor_flat price is 115.8280 CAD/m3 for every province. The stumpage_scaled sensitivity is province-specific; it equals the donor price where no provincial stumpage rate is available and uses the BC delivered/BCTS ratio otherwise. The largest scaled price reductions are:

| Province | Scaled price | Price change vs donor | Margin change | Scaled margin | Classification |
|---|---:|---:|---:|---:|---|
| AB | 18.6607 | -97.1673 | -97.1673 | -36.3258 | `cost_limited` |
| MB | 22.2039 | -93.6241 | -93.6241 | -30.6666 | `cost_limited` |
| ON | 22.7775 | -93.0505 | -93.0505 | -60.9518 | `cost_limited` |
| QC | 47.5123 | -68.3157 | -68.3157 | -35.8577 | `cost_limited` |
| SK | 52.8101 | -63.0179 | -63.0179 | 16.3892 | `positive_margin` |

Negative-margin provinces under the scaled sensitivity: AB, MB, ON, QC, NB. Negative-margin provinces under the donor price: none.

## Price sensitivity

The diagnostic orders provinces by the smallest absolute margin as a share of break-even across the two scenarios. A province at the top has the least buffer, so a small price movement can flip its sign. This is not a merit or policy ranking.

| Diagnostic order | Province | Closest scenario | Absolute margin | % of break-even | Classification |
|---:|---|---|---:|---:|---|
| 1 | NB | `stumpage_scaled` | 14.1365 | 14.33% | `price_limited` |
| 2 | NU | `donor_flat` | 28.8899 | 33.23% | `positive_margin` |
| 3 | ON | `donor_flat` | 32.0987 | 38.34% | `cost_limited` |
| 4 | QC | `donor_flat` | 32.4580 | 38.93% | `cost_limited` |
| 5 | SK | `stumpage_scaled` | 16.3892 | 45.00% | `positive_margin` |
| 6 | BC | `donor_flat` | 41.5880 | 56.02% | `positive_margin` |
| 7 | MB | `stumpage_scaled` | 30.6666 | 58.00% | `cost_limited` |
| 8 | AB | `stumpage_scaled` | 36.3258 | 66.06% | `cost_limited` |

## Arithmetic and v2.3 cross-checks

Every province break-even is recomputed from `national_cost_inputs.csv`, not copied from the margin summary. The recomputed central cost matches the v2.3 margin-table total cost with a maximum absolute difference of **0.000000 CAD/m3**. The donor/scaled margins match with a maximum absolute difference of **0.000000 CAD/m3**.

The volume-weighted central margins also match the v2.3 national diagnostic: donor_flat on observed 2024 harvest **43.0187** CAD/m3; stumpage_scaled on observed 2024 harvest **-5.7444** CAD/m3. The 119 Mm3 sensitivity values are reported separately in the JSON.

## Caveats

- The break-even price is a central model estimate, not an observed delivered price, mill margin or official net value.
- BC and QC break-even values are component stacks. BC road is an appraisal maintenance allowance, not road construction or amortization. QC components are survey aggregates.
- The ten aggregate-proxy provinces use one StatCan NAICS 11331 total expense per m3. That total already includes overhead, depreciation, non-logging activity and any in-plant or in-forest hauling performed by logging establishments; adding a road, silviculture or haul cost would double count.
- Nunavut uses the explicit v2.2 donor-total fallback because the StatCan value is blank at zero harvest. No StatCan value is fabricated.
- The low/high break-even range is a cost envelope for BC, QC and NU. Aggregate-proxy provinces have a point estimate because StatCan publishes no comparable range.
- Stumpage_scaled is a method sensitivity, not the base price and not an observed price. It can fall below the modeled cost.
- Negative margins and negative gaps are retained without clipping. No value is set to zero to hide a negative result.

## Non-claims

- Not observed; observed=false.
- Not policy grade; policy_grade=false.
- Not a policy result, policy recommendation or policy frontier.
- Not a combined national net value.
- Not a Forest LP objective or constraint input.
- Not a public OSeCAN input.
- No jurisdictional merit ranking; the price-sensitivity list is a diagnostic ordering by distance to break-even.

## Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.province_breakeven
```
