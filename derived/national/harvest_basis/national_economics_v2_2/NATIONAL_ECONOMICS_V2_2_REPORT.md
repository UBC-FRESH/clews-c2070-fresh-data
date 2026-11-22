# National Economics v2.2 - direct P1 cost inputs where available

Generated: 2026-11-22T15:21:03+00:00

## What changed

Version 2.2 keeps the v2.1 price scenarios unchanged and upgrades only the cost cells with published direct evidence. The base price scenario remains `donor_flat`; `stumpage_scaled` remains a sensitivity.

## QC cost upgrade

Quebec harvest, haul and road now use the MRNF 2022 T20 survey synthesis: **harvest 31.42**, **haul 24.76**, **road 16.58 CAD/m3**. Road is `access_cost_gross` before PRCCM; the T5 after-PRCCM value is deliberately not used with T10 transfers.

| Component | Low | Base | High | Tier | Source year |
|---|---:|---:|---:|---|---:|
| QC harvest | 28.2700 | 31.4200 | 34.4800 | `reported_survey_aggregate` | 2022 |
| QC haul | 19.3200 | 24.7600 | 36.8600 | `reported_survey_aggregate` | 2022 |
| QC road | 7.4700 | 16.5800 | 22.1300 | `reported_survey_aggregate` | 2022 |

Low/high are the published regional SEPM minimum/maximum across the seven regional means. R09 is a three-respondent mean and remains flagged in the source. These are survey aggregates, not observed transactions.

## BC road result

A published BC road-management CAD/m3 allowance exists: the IAM 2026 Table 4-6 road-maintenance groups. It is used with low/base/high equal to the minimum/median/maximum of the 22 published groups.

| Low | Base | High | Tier | Source year |
|---:|---:|---:|---|---:|
| 1.0000 | 5.9300 | 9.7800 | `appraisal_allowance` | 2026 |

This is a **maintenance-only** appraisal allowance. BC road construction is published as CAD/km and was **not** converted to CAD/m3. The result is partial direct road coverage, not a full road construction/amortization cost.

## AB and ON

Alberta and Ontario keep the donor cost values. The source map indicates no direct public logging, haul, road or silviculture cost series for either jurisdiction. The rows are labelled `not_available_direct_cost_series`; no value is invented and their central margins are unchanged from v2.1.

## Margins and coverage delta

| Province | Base donor_flat low | Base donor_flat central | Base donor_flat high | Sensitivity scaled central |
|---|---:|---:|---:|---:|
| BC | -90.0770 | 41.5880 | 94.7093 | 41.5880 |
| AB | -89.9629 | 35.0360 | 82.2909 | -62.1313 |
| SK | -91.8865 | 34.2655 | 81.8957 | -28.7524 |
| MB | -94.0598 | 33.3948 | 81.4492 | -60.2293 |
| ON | -89.5499 | 35.2015 | 82.3757 | -57.8490 |
| QC | -29.7270 | 32.4580 | 70.2393 | -35.8577 |
| NB | -85.2473 | 36.9250 | 83.2596 | 5.6270 |
| NS | -85.2563 | 36.9214 | 83.2577 | 43.9234 |
| NL | -96.6444 | 32.3595 | 80.9183 | 32.3595 |
| PE | -85.2469 | 36.9252 | 83.2597 | 36.9252 |
| YT | -100.6176 | 30.7679 | 80.1021 | 30.7679 |
| NT | -101.3310 | 30.4821 | 79.9555 | 30.4821 |
| NU | -105.3059 | 28.8899 | 79.1390 | 28.8899 |

| Scenario | Role | Low | Base | High | Label | Combined net value |
|---|---|---:|---:|---:|---|---|
| donor_flat | base | -76.2945 | 36.7405 | 83.8033 | `model_estimate_not_policy` | false |
| stumpage_scaled | sensitivity | -111.6288 | -12.5180 | 40.8950 | `model_estimate_not_policy` | false |

The national numbers are volume-weighted diagnostics across all 13 jurisdictions on the 119 Mt screening allocation. They are not a combined national net value, not a policy result and not a total of observed profits.

### Direct-cost coverage before and after

| Scope | Version | Direct cells | Total cells | Volume-weighted direct share |
|---|---|---:|---:|---:|
| All 5 components | v2_1 | 3 | 65 | 0.17924672 |
| All 5 components | v2_2 | 6 | 65 | 0.33612911 |
| Cost components only | v2_1 | 2 | 52 | 0.14005379 |
| Cost components only | v2_2 | 5 | 52 | 0.33615678 |

P1 direct-coverage upgrades: **3** cells (BC road, QC logging, QC haul). The QC road cell was already direct in v2.1 and is relabelled to the more precise `reported_survey_aggregate` tier; it is not counted as a new direct cell. Coverage is still partial: no full direct coverage is claimed.

### Scenario comparison

`v2_1_v2_2_comparison.csv` reports low/base/high margins and central total cost for v2.1 and v2.2 in both price scenarios. The deltas are model method changes, not observed market changes.

## Negative margins and labels

34 of 78 margin rows are negative and are **unclipped**. Negatives are a result, not an error.
- `donor_flat`: 13 negative rows, 0 in the central case.
- `stumpage_scaled`: 21 negative rows, 5 in the central case.

Every row carries `evidence=model_estimate`, `observed=false`, `policy_grade=false` and `combined_national_net_value=false`.

## Non-claims

- Not observed profit, not a mill margin and not official net value.
- Survey aggregates and appraisal allowances are model inputs, not transactions.
- BC road is maintenance-only and does not establish full road cost coverage.
- AB and ON have no direct cost series; donor values remain.
- No combined national net value is computed.
- No strict-open licence claim is made; source documents are not redistributed.
- No restricted, confidential or microdata input is used.

## Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.national_economics_v2_2
```
