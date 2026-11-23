# TSA24 default vs tipsy45 bucking-profile comparison
| Field | Value |
|---|---|
| Validation | `industrial_sort_validation` |
| Grade status | `not_assigned` |
| Official grade validation | no |
| Profiles | `default` vs `tipsy45` |
| Verdict | `gap_does_not_close_on_both_pooled_and_mean_plot_tvd` |

> The profiles were declared before the comparison. No profile value was tuned to improve TVD. This is an industrial sort recovery check, not an official BC log-grade validation.

## 1. Before/after metrics

| metric | default | tipsy45 | delta |
| --- | --- | --- | --- |
| pooled_tvd | 0.4329 | 0.4404 | 0.0075 |
| pooled_overlap | 0.5671 | 0.5596 | -0.0075 |
| mean_plot_tvd | 0.5052 | 0.5354 | 0.0302 |
| median_plot_tvd | 0.4801 | 0.5176 | 0.0375 |
| volume_weighted_tvd | 0.4909 | 0.5266 | 0.0358 |
| diameter_marginal_tvd | 0.1906 | 0.1858 | -0.0049 |
| length_marginal_tvd | 0.3176 | 0.4009 | 0.0833 |
| bias_sum_m3ha | 2,532.9846 | 2,632.9855 | 100.0009 |
| relative_bias | 0.0279 | 0.0290 | 0.0011 |
| ratio_predicted_observed | 1.0279 | 1.0290 | 0.0011 |
| mae_m3ha | 105.3425 | 105.2027 | -0.1397 |
| rmse_m3ha | 137.5964 | 137.4483 | -0.1481 |

Pilot logs: default **24,424**, tipsy45 **22,365** on the same **341** comparable AU-matched plots and **12,950** trees.

## 2. Sort shares

`abs_difference_change` is the tipsy45 absolute pilot-vs-TIPSY share difference minus the default difference; negative values are improvements.

| code | default_pilot_share | default_tipsy_share | tipsy45_pilot_share | tipsy45_tipsy_share | abs_difference_change |
| --- | --- | --- | --- | --- | --- |
| D125L51 | 0.1923 | 0.3786 | 0.1747 | 0.3785 | 0.0175 |
| D20L8 | 0.1053 | 0.2275 | 0.0879 | 0.2276 | 0.0174 |
| D125L13 | 0.0814 | 0.0035 | 0.1233 | 0.0035 | 0.0419 |
| D125L11 | 0.0765 | 0.0196 | 0.0802 | 0.0196 | 0.0037 |
| D125L5 | 0.0012 | 0.0550 | 0.0012 | 0.0550 | -0.0001 |
| D30L13 | 0.0030 | 0.0039 | 0.0526 | 0.0039 | 0.0477 |
| D125L63 | 0.2555 | 0.0891 | 0.1310 | 0.0891 | -0.1245 |
| D152 | 0.0220 | 0.0000 | 0.0377 | 0.0000 | 0.0157 |
| D38L13 | 0.0023 | 0.0007 | 0.0270 | 0.0007 | 0.0247 |
| D30L11 | 0.0071 | 0.0050 | 0.0298 | 0.0050 | 0.0227 |
| D38L11 | 0.0059 | 0.0015 | 0.0245 | 0.0015 | 0.0186 |
| D20L13 | 0.0033 | 0.0393 | 0.0166 | 0.0393 | -0.0133 |

## 3. Non-TIPSY nominal lengths

Counts of bucked logs whose exact length is outside the nominal TIPSY length list. This diagnostic is descriptive; TIPSY sort codes are minimum-length classes, so it is not a grade claim.

| length_m | default_logs | tipsy45_logs |
| --- | --- | --- |
| 10.000 | 761 | 0 |
| 12.500 | 0 | 0 |
| 15.000 | 0 | 0 |
| 2.400 | 0 | 0 |
| 7.500 | 3410 | 0 |

## 4. Per-AU TVD

| au_id | n_plots | pooled_tvd_default | pooled_tvd_tipsy45 | pooled_tvd_delta | mean_plot_tvd_delta |
| --- | --- | --- | --- | --- | --- |
| 23000 | 128 | 0.4289 | 0.4306 | 0.0017 | 0.0281 |
| 23003 | 78 | 0.4399 | 0.4665 | 0.0265 | 0.0349 |
| 22003 | 36 | 0.4562 | 0.4654 | 0.0092 | 0.0264 |
| 23001 | 21 | 0.3737 | 0.3894 | 0.0157 | 0.0254 |
| 23007 | 16 | 0.7718 | 0.7792 | 0.0074 | 0.0117 |
| 22000 | 16 | 0.4124 | 0.4358 | 0.0234 | 0.0484 |
| 23008 | 14 | 0.4344 | 0.4509 | 0.0165 | 0.0477 |
| 22008 | 8 | 0.4108 | 0.4218 | 0.0111 | 0.0493 |
| 23002 | 8 | 0.3417 | 0.4113 | 0.0696 | 0.0268 |
| 21008 | 5 | 0.4235 | 0.4469 | 0.0234 | 0.0342 |
| 21002 | 3 | 0.5010 | 0.5378 | 0.0368 | 0.0281 |
| 21007 | 3 | 0.8165 | 0.8176 | 0.0011 | 0.0009 |
| 22007 | 3 | 0.9570 | 0.9577 | 0.0007 | 0.0001 |
| 22002 | 2 | 0.4329 | 0.4314 | -0.0016 | -0.0011 |

## 5. What remains

- The tipsy45 geometry removes every non-nominal 7.5 m and 10.0 m log, but the pooled and mean-per-plot TVD do not improve.
- The value-maximising dynamic program without a published FAN$IER length/grade price surface over-selects 13 m and 11 m logs and under-selects the 8 m and 5.1 m classes that dominate the TIPSY curves.
- FAN$IER 4.5 Help does not publish numeric default log prices or a sort-specific relativity. No such values were invented; the tipsy45 price scenario keeps the published BC Interior product-class prices.
- The remaining gap is a model-definition gap (bucking objective and price/grade surface), not a threshold that should be tuned here.
