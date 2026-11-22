# National Economics v2 - provincial stumpage-scaled price proxies

Generated: 2026-11-22T06:53:21+00:00

## What this is

A 13-jurisdiction **model estimate** of log-price proxies and margins. Provincial stumpage, dues, royalty or standing-value rates are multiplied by the BC delivered-price/BCTS-stumpage ratio. The result is labelled `stumpage_scaled_proxy`; it is not a delivered price and not observed revenue. A flat BC donor scenario is retained as sensitivity and as the fallback where no current rate was extracted.

## Stumpage references

- Extracted current rates: **8 of 13** (BC, AB, SK, MB, ON, QC, NB, NS).
- Fallback donor jurisdictions: **NL, PE, YT, NT, NU**.
- NU is a fallback: the open.canada record in the research map is an Ontario data mirror, not a Nunavut rate. No numeric NU rate is asserted.
- No rate is described as a delivered price; `is_delivered_price=false` on every row.

| Province | Rate type | Low | Base | High | Source date |
|---|---|---:|---:|---:|---|
| BC | bcts_average_stumpage_rate | 34.3250 | 34.3250 | 34.3250 | 2025 |
| AB | timber_dues_rate | 2.6600 | 5.5300 | 12.6800 | 2026-11 |
| SK | timber_dues_rate | 2.6000 | 15.6500 | 15.6500 | 2026-Q3 |
| MB | timber_dues_rate | 4.5800 | 6.5800 | 6.5800 | 2026-11 |
| ON | crown_timber_charges_rate | 6.0600 | 6.7500 | 6.7500 | 2026-11 |
| QC | standing_value_rate | 12.8800 | 14.0800 | 22.4900 | 2026-11 |
| NB | timber_royalty_rate | 24.0300 | 25.0500 | 27.0600 | 2026-11 |
| NS | standing_timber_value_survey | 29.8700 | 36.4000 | 36.4000 | 2024-07 |

## Price proxy construction

BC BCTS stumpage = 137.3M CAD / 4.0M m3 = 34.33 CAD/m3.
BC blended delivered price = 115.83 CAD/m3, so the base ratio is 3.3745. Low/high ratios are 2.1842/3.8205.
The base scenario produces **7 stumpage-scaled price proxies**; BC itself keeps its reported average and five jurisdictions use the flat donor.
The ratio transfers BC's cost-plus-margin structure. It is not a provincial cost survey and can overshoot where a province's stumpage is high relative to BC.
Scope: BC blended Coast+Interior. BCTS does not publish a regional stumpage revenue/volume split in the materialised source, so separate Coast and Interior ratios are not computed.

## Margins

Base-scenario national volume-weighted margin: **-16.1220 CAD/m3** (low -130.0389, high 38.4085).
Flat-donor sensitivity national base margin: **33.1365 CAD/m3**.
34 of 78 margin rows are negative and are **unclipped**. Negatives are a result, not an error.
Costs are v1 donors: BC logging+haul distribution, QC 2022 road allowance and BC Interior silviculture allowance.

## Comparison with v1

| Province | v1 base margin | v2 scaled base | v2 donor flat | Delta |
|---|---:|---:|---:|---:|
| BC | 30.9380 | 30.9380 | 30.9380 | 0.0000 |
| AB | 35.0360 | -62.1313 | 35.0360 | -97.1673 |
| SK | 34.2655 | -28.7524 | 34.2655 | -63.0179 |
| MB | 33.3948 | -60.2293 | 33.3948 | -93.6241 |
| ON | 35.2015 | -57.8490 | 35.2015 | -93.0505 |
| QC | 32.3447 | -35.9710 | 32.3447 | -68.3157 |
| NB | 36.9250 | 5.6270 | 36.9250 | -31.2980 |
| NS | 36.9214 | 43.9234 | 36.9214 | 7.0020 |
| NL | 32.3595 | 32.3595 | 32.3595 | 0.0000 |
| PE | 36.9252 | 36.9252 | 36.9252 | 0.0000 |
| YT | 30.7679 | 30.7679 | 30.7679 | 0.0000 |
| NT | 30.4821 | 30.4821 | 30.4821 | 0.0000 |
| NU | 28.8899 | 28.8899 | 28.8899 | 0.0000 |

## Tiers and coverage

- 13 jurisdictions, no `not_estimated` rows.
- Two price scenarios: `stumpage_scaled` (base) and `donor_flat` (sensitivity).
- Price tiers: `reported_average` (BC), `stumpage_scaled_proxy` (8), `donor_proxy` (fallbacks).
- Volume references: 119 Mt allocation, 2024 observed harvest, NFD supply and documented AAC are carried in the summary table.
- National diagnostic uses the 119 Mt allocation and is labelled `model_estimate_not_policy`.

## Non-claims

- Every row: `evidence=model_estimate`, `observed=false`, `policy_grade=false`, `combined_national_net_value=false`.
- No strict-open licence claim is made; source documents are not redistributed.
- No restricted, confidential or microdata input is used.
- Not a policy result, not a provincial cost survey and not a combined BC+QC-only total.
