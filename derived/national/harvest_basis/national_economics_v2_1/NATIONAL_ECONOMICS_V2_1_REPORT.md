# National Economics v2.1 - donor-flat base with stumpage-scaled sensitivity

Generated: 2026-11-22T06:53:23+00:00

## Decision

**Base scenario: `donor_flat`.** All 13 jurisdictions use the v1 BC 2025-12 blended mill-delivered donor price. The national base diagnostic is **33.1365 CAD/m3** (low -94.7046, high 81.3168).
**Sensitivity: `stumpage_scaled`.** The v2 provincial stumpage/dues rate proxies are retained only as a sensitivity and fallback exercise. The national sensitivity diagnostic is **-16.1220 CAD/m3** (low -130.0389, high 38.4085).
The stumpage-scaled scenario is the **sensitivity, not the base**. It is not observed and not policy grade. It is a synthetic method sensitivity, not a delivered price series and not a mill margin.

## Coverage and evidence tiers

- 13 jurisdictions: BC, AB, SK, MB, ON, QC, NB, NS, NL, PE, YT, NT, NU.
- Two price scenarios: `donor_flat` (base) and `stumpage_scaled` (sensitivity).
- No `not_estimated` rows; every jurisdiction has low/base/high margins.
- `donor_flat` tiers: `donor_proxy`=12, `reported_average`=1.
- `stumpage_scaled` tiers: `donor_proxy`=5, `reported_average`=1, `stumpage_scaled_proxy`=7.
- Cost tiers are unchanged from v1: `proxy_model` (BC), `donor_proxy_with_reported_road` (QC), `donor_proxy` (11).

## Province results

| Province | Base donor_flat low | Base donor_flat central | Base donor_flat high | Sensitivity scaled central |
|---|---:|---:|---:|---:|
| BC | -100.1930 | 30.9380 | 80.1893 | 30.9380 |
| AB | -89.9629 | 35.0360 | 82.2909 | -62.1313 |
| SK | -91.8865 | 34.2655 | 81.8957 | -28.7524 |
| MB | -94.0598 | 33.3948 | 81.4492 | -60.2293 |
| ON | -89.5499 | 35.2015 | 82.3757 | -57.8490 |
| QC | -96.6814 | 32.3447 | 80.9107 | -35.9710 |
| NB | -85.2473 | 36.9250 | 83.2596 | 5.6270 |
| NS | -85.2563 | 36.9214 | 83.2577 | 43.9234 |
| NL | -96.6444 | 32.3595 | 80.9183 | 32.3595 |
| PE | -85.2469 | 36.9252 | 83.2597 | 36.9252 |
| YT | -100.6176 | 30.7679 | 80.1021 | 30.7679 |
| NT | -101.3310 | 30.4821 | 79.9555 | 30.4821 |
| NU | -105.3059 | 28.8899 | 79.1390 | 28.8899 |

## National diagnostic

| Scenario | Role | Low | Base | High | Label | Combined net value |
|---|---|---:|---:|---:|---|---|
| donor_flat | base | -94.7046 | 33.1365 | 81.3168 | `model_estimate_not_policy` | false |
| stumpage_scaled | sensitivity | -130.0389 | -16.1220 | 38.4085 | `model_estimate_not_policy` | false |

The national numbers are volume-weighted diagnostics across all 13 jurisdictions on the 119 Mt screening allocation. They are not a combined national net value, not a policy result, and not a total of observed profits.

## Scenario comparison

`scenario_comparison.csv` reports the v1 flat donor, the v2.1 donor-flat base and the v2.1 stumpage-scaled sensitivity. Because the cost stack is unchanged, the donor-flat base reproduces v1.

### Why dues are not comparable

Stumpage, dues, royalty and standing-value rates are charges on standing timber. They are not delivered log prices: a delivered price embeds harvest, haul, road and silviculture cost plus a margin. Subtracting the same cost stack from a scaled dues rate double counts those costs if the result is read as a mill margin. Rates also differ in unit, species/grade, tenure, scaling and vintage. Deltas are therefore method changes, not observed market changes.

The `scaled_minus_donor_flat_cad_m3` column is therefore a method delta. It must not be read as an observed market change, a provincial stumpage effect, or a base-scenario estimate.

## Negative margins and labels

34 of 78 margin rows are negative and are **unclipped**. Negatives are a result, not an error.
- `donor_flat`: 13 negative rows, 0 in the central case.
- `stumpage_scaled`: 21 negative rows, 5 in the central case.

Every row carries `evidence=model_estimate`, `observed=false`, `policy_grade=false` and `combined_national_net_value=false`.

## Non-claims

- Not observed profit, not a mill margin and not official net value.
- Not a stumpage rate and not policy grade.
- The stumpage-scaled sensitivity is not the base scenario and is not observed.
- No combined national net value is computed.
- No strict-open licence claim is made; source documents are not redistributed.
- No restricted, confidential or microdata input is used.
