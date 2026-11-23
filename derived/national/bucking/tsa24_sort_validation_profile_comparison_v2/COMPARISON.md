# TSA24 default vs tipsy45 vs market-surface bucking comparison
| Field | Value |
|---|---|
| Validation | `industrial_sort_validation` |
| Grade status | `not_assigned` |
| Official grade validation | no |
| Profiles | `default` vs `tipsy45` vs `market_surface` |
| Verdict | `market_surface_does_not_close_gap` |

> The profiles were declared before the comparison. No profile value was tuned to improve TVD. This is an industrial sort recovery check, not an official BC log-grade validation.

## 1. Before/after metrics

| metric | default | tipsy45 | market_surface | tipsy45_delta | market_vs_default | market_vs_tipsy45 |
| --- | --- | --- | --- | --- | --- | --- |
| pooled_tvd | 0.4329 | 0.4404 | 0.5972 | 0.0075 | 0.1644 | 0.1568 |
| pooled_overlap | 0.5671 | 0.5596 | 0.4028 | -0.0075 | -0.1644 | -0.1568 |
| mean_plot_tvd | 0.5052 | 0.5354 | 0.6606 | 0.0302 | 0.1554 | 0.1252 |
| median_plot_tvd | 0.4801 | 0.5176 | 0.6561 | 0.0375 | 0.1760 | 0.1384 |
| volume_weighted_tvd | 0.4909 | 0.5266 | 0.6660 | 0.0358 | 0.1751 | 0.1393 |
| diameter_marginal_tvd | 0.1906 | 0.1858 | 0.2069 | -0.0049 | 0.0163 | 0.0211 |
| length_marginal_tvd | 0.3176 | 0.4009 | 0.5257 | 0.0833 | 0.2081 | 0.1247 |
| bias_sum_m3ha | 2,532.9846 | 2,632.9855 | 3,285.4163 | 100.0009 | 752.4317 | 652.4307 |
| relative_bias | 0.0279 | 0.0290 | 0.0365 | 0.0011 | 0.0086 | 0.0074 |
| ratio_predicted_observed | 1.0279 | 1.0290 | 1.0365 | 0.0011 | 0.0086 | 0.0074 |
| mae_m3ha | 105.3425 | 105.2027 | 104.9621 | -0.1397 | -0.3804 | -0.2406 |
| rmse_m3ha | 137.5964 | 137.4483 | 136.9097 | -0.1481 | -0.6867 | -0.5386 |

Pilot logs: default **24,424**, tipsy45 **22,365**, market_surface **20,317** on the same **341** comparable AU-matched plots and **12,950** trees.

Market-surface gap check: vs default `False`, vs tipsy45 `False`. A gap closes only when both pooled and mean per-plot TVD decline.

## 2. Sort shares

`abs_difference_change` is the tipsy45 absolute pilot-vs-TIPSY share difference minus the default difference; negative values are improvements. For the market surface, `abs_market_vs_default_change` and `abs_market_vs_tipsy45_change` use the same sign convention.

| code | default_pilot_share | default_tipsy_share | tipsy45_pilot_share | tipsy45_tipsy_share | market_surface_pilot_share | market_surface_tipsy_share | abs_market_vs_default_change | abs_market_vs_tipsy45_change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D125L51 | 0.1923 | 0.3786 | 0.1747 | 0.3785 | 0.0141 | 0.3784 | 0.1780 | 0.1604 |
| D125L13 | 0.0814 | 0.0035 | 0.1233 | 0.0035 | 0.1524 | 0.0035 | 0.0710 | 0.0291 |
| D20L8 | 0.1053 | 0.2275 | 0.0879 | 0.2276 | 0.0898 | 0.2277 | 0.0157 | -0.0018 |
| D125L63 | 0.2555 | 0.0891 | 0.1310 | 0.0891 | 0.2126 | 0.0890 | -0.0428 | 0.0816 |
| D125L11 | 0.0765 | 0.0196 | 0.0802 | 0.0196 | 0.0814 | 0.0196 | 0.0049 | 0.0012 |
| D125L5 | 0.0012 | 0.0550 | 0.0012 | 0.0550 | 0.0012 | 0.0549 | -0.0001 | -0.0001 |
| D30L13 | 0.0030 | 0.0039 | 0.0526 | 0.0039 | 0.0511 | 0.0039 | 0.0462 | -0.0015 |
| D152 | 0.0220 | 0.0000 | 0.0377 | 0.0000 | 0.0357 | 0.0000 | 0.0137 | -0.0020 |
| D125L8 | 0.1166 | 0.0968 | 0.1049 | 0.0968 | 0.1275 | 0.0968 | 0.0110 | 0.0227 |
| D38L11 | 0.0059 | 0.0015 | 0.0245 | 0.0015 | 0.0322 | 0.0015 | 0.0263 | 0.0077 |
| D30L11 | 0.0071 | 0.0050 | 0.0298 | 0.0050 | 0.0335 | 0.0050 | 0.0264 | 0.0037 |
| D38L13 | 0.0023 | 0.0007 | 0.0270 | 0.0007 | 0.0269 | 0.0007 | 0.0246 | -0.0001 |

## 3. Non-TIPSY nominal lengths

Counts of bucked logs whose exact length is outside the nominal TIPSY length list. This diagnostic is descriptive; TIPSY sort codes are minimum-length classes, so it is not a grade claim.

| length_m | default_logs | tipsy45_logs | market_surface_logs |
| --- | --- | --- | --- |
| 10.000 | 761 | 0 | 0 |
| 12.500 | 0 | 0 | 0 |
| 15.000 | 0 | 0 | 0 |
| 2.400 | 0 | 0 | 0 |
| 7.500 | 3410 | 0 | 0 |

## 4. Per-AU TVD

| au_id | n_plots | pooled_tvd_default | pooled_tvd_tipsy45 | pooled_tvd_market_surface | pooled_tvd_delta_vs_default | pooled_tvd_delta_vs_tipsy45 |
| --- | --- | --- | --- | --- | --- | --- |
| 23000 | 128 | 0.4289 | 0.4306 | 0.5900 | 0.1611 | 0.1594 |
| 23003 | 78 | 0.4399 | 0.4665 | 0.6192 | 0.1793 | 0.1527 |
| 22003 | 36 | 0.4562 | 0.4654 | 0.6073 | 0.1511 | 0.1419 |
| 23001 | 21 | 0.3737 | 0.3894 | 0.5652 | 0.1915 | 0.1758 |
| 23007 | 16 | 0.7718 | 0.7792 | 0.7942 | 0.0224 | 0.0150 |
| 22000 | 16 | 0.4124 | 0.4358 | 0.6111 | 0.1987 | 0.1753 |
| 23008 | 14 | 0.4344 | 0.4509 | 0.5933 | 0.1589 | 0.1424 |
| 22008 | 8 | 0.4108 | 0.4218 | 0.5888 | 0.1780 | 0.1669 |
| 23002 | 8 | 0.3417 | 0.4113 | 0.6356 | 0.2939 | 0.2243 |
| 21008 | 5 | 0.4235 | 0.4469 | 0.5909 | 0.1674 | 0.1439 |
| 21002 | 3 | 0.5010 | 0.5378 | 0.6711 | 0.1701 | 0.1334 |
| 21007 | 3 | 0.8165 | 0.8176 | 0.8176 | 0.0011 | 0.0000 |
| 22007 | 3 | 0.9570 | 0.9577 | 0.9577 | 0.0007 | -0.0000 |
| 22002 | 2 | 0.4329 | 0.4314 | 0.4314 | -0.0016 | 0.0000 |

## 5. What remains

- The tipsy45 geometry removes every non-nominal 7.5 m and 10.0 m log. The market surface changes the product prices and product assignment, not the geometry.
- The value-maximising dynamic program over-selects 13 m and 11 m logs and under-selects the 8 m and 5.1 m classes when the published price is a per-cubic-metre product average with no length premium.
- BC log-market reports publish species x product averages, not TIPSY-sort-specific or grade-specific prices. Coast grade letters have no documented crosswalk to TIPSY industrial dimension sorts; peeler prices cannot be assigned without quality. Those cells remain gaps, not invented values.
- FAN$IER 4.5 Help does not publish numeric default log prices or a sort-specific relativity. No such values were invented; the tipsy45 price scenario keeps the published BC Interior product-class prices.
- The remaining gap is a model-definition gap (bucking objective and price/grade surface), not a threshold that should be tuned here.
