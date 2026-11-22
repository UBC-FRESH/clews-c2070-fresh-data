# National Economics Scaffold v1

Status: **model estimate scaffold — not policy grade, not observed, not a
strict-open dataset.** Generated 2026-11-22T06:02:42+00:00.

## 1. Scope and coverage

All **13 provinces and territories** are covered: BC, AB, SK, MB, ON, QC, NB, NS, NL, PE, YT, NT, NU.
There are **39 margin rows** (13 jurisdictions x low/base/high)
and **no `not_estimated`** coverage gaps. NU has zero allocation volume; its
margin is a proxy only and no commercial harvest is asserted.

## 2. Method

### 2.1 Price

- **BC:** published 2025-12 3-month Coast and Interior mill-delivered report
  averages, volume-weighted by the published report totals. This is a
  `reported_average`, not a transaction record.
- **All other jurisdictions:** BC donor price with an explicit price index of
  **1.00**. No provincial wage, diesel or price index is materialised in the
  repository, so the index is a labelled national-median donor assumption.
- **QC:** no current delivered-log price. The QC 2022 purchase cost
  **107.22** and BMMB Crown-only
  historical rate **35.7547** are
  references only and are **not** used as price inputs.

### 2.2 Cost

- Start from the **945-row BC logging+haul distribution**:
  low = p10(total_low), base = median(total_base), high = p90(total_high).
- Apply explicit factors: wage **1.00**, diesel **1.00**, terrain
  `1 + 0.25 * (province share_gt15 - BC share_gt15)`, road
  `1 + 0.15 * (province road_gt20_share - BC road_gt20_share)`, clamped to
  [0.75, 1.25].
- Add a **road allowance** from the published QC 2022 T5 CAD/m3 values
  (15.52 /
  16.58 /
  19.90).
- Add a **silviculture allowance** from the published BC Interior basic
  silviculture CAD/m3 zone range
  (5.84 /
  10.61 /
  11.23).
- **No CAD/km or CAD/each road, bridge or culvert value is converted to CAD/m3.**

### 2.3 Margin

```
margin = price - logging_haul - road - silviculture
```

- **low:** low price minus high logging+haul, road and silviculture.
- **base:** base price minus base costs.
- **high:** high price minus low costs.
- Unclipped; negative values are documented, not suppressed.

Every row is `evidence=model_estimate`, `observed=false`,
`policy_grade=false`, `net_value_status=model_estimate` and
`combined_national_net_value=false`.

## 3. Price proxies (CAD/m3 nominal 2025)

| Province | Low | Base | High | Tier | Donor | Index |
|---|---|---|---|---|---|---|
| BC | 74.9730 | 115.8280 | 131.1393 | reported_average | self | 1.0000 |
| AB | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| SK | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| MB | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| ON | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| QC | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| NB | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| NS | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| NL | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| PE | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| YT | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| NT | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |
| NU | 74.9730 | 115.8280 | 131.1393 | donor_proxy | BC | 1.0000 |

## 4. Cost proxies (CAD/m3, mixed nominal 2022-2026, no deflator)

| Province | Logging+haul low | Base | High | Road base | Silv. base | Total base | Index | Cost tier |
|---|---|---|---|---|---|---|---|---|
| BC | 29.5900 | 57.7000 | 144.0400 | 16.5800 | 10.6100 | 84.8900 | 1.000000 | proxy_model |
| AB | 27.4884 | 53.6020 | 133.8099 | 16.5800 | 10.6100 | 80.7920 | 0.928978 | donor_proxy |
| SK | 27.8836 | 54.3725 | 135.7335 | 16.5800 | 10.6100 | 81.5625 | 0.942332 | donor_proxy |
| MB | 28.3301 | 55.2432 | 137.9068 | 16.5800 | 10.6100 | 82.4332 | 0.957420 | donor_proxy |
| ON | 27.4036 | 53.4365 | 133.3969 | 16.5800 | 10.6100 | 80.6265 | 0.926110 | donor_proxy |
| QC | 28.8686 | 56.2933 | 140.5284 | 16.5800 | 10.6100 | 83.4833 | 0.975621 | donor_proxy_with_reported_road |
| NB | 26.5197 | 51.7130 | 129.0943 | 16.5800 | 10.6100 | 78.9030 | 0.896239 | donor_proxy |
| NS | 26.5216 | 51.7166 | 129.1033 | 16.5800 | 10.6100 | 78.9066 | 0.896302 | donor_proxy |
| NL | 28.8610 | 56.2785 | 140.4914 | 16.5800 | 10.6100 | 83.4685 | 0.975363 | donor_proxy |
| PE | 26.5196 | 51.7128 | 129.0939 | 16.5800 | 10.6100 | 78.9028 | 0.896236 | donor_proxy |
| YT | 29.6772 | 57.8701 | 144.4646 | 16.5800 | 10.6100 | 85.0601 | 1.002948 | donor_proxy |
| NT | 29.8238 | 58.1559 | 145.1780 | 16.5800 | 10.6100 | 85.3459 | 1.007901 | donor_proxy |
| NU | 30.6403 | 59.7481 | 149.1529 | 16.5800 | 10.6100 | 86.9381 | 1.035497 | donor_proxy |

## 5. Provincial margins (CAD/m3)

| Province | Volume m3 | Margin low | Margin base | Margin high | Base status |
|---|---|---|---|---|---|
| BC | 39978577.0000 | -100.1930 | 30.9380 | 80.1893 | low_negative_documented |
| AB | 22891404.0000 | -89.9629 | 35.0360 | 82.2909 | low_negative_documented |
| SK | 4344697.6000 | -91.8864 | 34.2655 | 81.8957 | low_negative_documented |
| MB | 1135235.8000 | -94.0598 | 33.3948 | 81.4492 | low_negative_documented |
| ON | 13493596.0000 | -89.5498 | 35.2015 | 82.3757 | low_negative_documented |
| QC | 26674334.0000 | -96.6814 | 32.3447 | 80.9107 | low_negative_documented |
| NB | 6234700.0000 | -85.2473 | 36.9250 | 83.2596 | low_negative_documented |
| NS | 2388245.0000 | -85.2563 | 36.9214 | 83.2577 | low_negative_documented |
| NL | 1454037.5000 | -96.6443 | 32.3595 | 80.9183 | low_negative_documented |
| PE | 302210.4000 | -85.2468 | 36.9252 | 83.2597 | low_negative_documented |
| YT | 43925.8000 | -100.6176 | 30.7679 | 80.1021 | low_negative_documented |
| NT | 36376.0000 | -101.3310 | 30.4821 | 79.9555 | low_negative_documented |
| NU | 0.0000 | -105.3059 | 28.8899 | 79.1390 | low_negative_documented |
| NATIONAL | 118977339.1000 | -94.7046 | 33.1365 | 81.3168 | model_estimate_not_policy |

**Negative margin note:** 13 negative margin rows are documented. The low case is a conservative envelope (low price minus high cost); negative values are not clipped.

## 6. National diagnostic

The national row is a volume-weighted average across **all 13 jurisdictions**
using the 119 Mt provincial allocation:

| Item | Value |
|---|---:|
| Allocation volume (m3/yr) | 118977339.10 |
| Weighted margin low | -94.7046 |
| Weighted margin base | 33.1365 |
| Weighted margin high | 81.3168 |
| Label | `model_estimate_not_policy` |
| Combined national net value | `false` |

This is **not** a BC+QC-only total and not a policy result.

## 7. Observed vs proxy

| Layer | BC | QC | Other jurisdictions |
|---|---|---|---|
| Price | reported average | donor proxy (no delivered price) | donor proxy |
| Logging+haul | proxy model | donor proxy + QC cross-check | donor proxy |
| Road | QC donor | reported average (2022 CAD/m3) | QC donor |
| Silviculture | reported BC allowance | BC donor | BC donor |
| Margin | model estimate | model estimate | model estimate |

The QC direct 2022 harvest+haul+road total is
**72.76 CAD/m3**; the model's
QC logging+haul+road base is compared at a ratio of
**1.0016** (within_2pct).
This is a cross-check, not a second input.

## 8. Validation

| Check | Status | Detail |
|---|---|---|
| All 13 jurisdictions | PASS | 13 provinces/territories |
| No not_estimated | PASS | 0 rows |
| Ranges ordered | PASS | low<=base<=high |
| Finite outputs | PASS | no NaN/Inf |
| QC cross-check | PASS | 1.001557477261451 |
| No restricted inputs | PASS | aggregate/public-reference only |
| No CAD/km conversion | PASS | CAD/m3 only |
| Strict-open claim | PASS | false; public-reference copyrighted inputs |

Negative margins: 13 rows, documented in
`summary.json` and `national_margin_estimates.csv`.

## 9. Licensing and non-claims

**No strict-open claim.** Inputs are public-reference copyrighted sources or
this model's own explicit assumptions. Source PDFs are not redistributed.
Commercial reuse requires permission from the rights holder.

Non-claims: not observed profit; not a mill margin; not an official net value;
not a stumpage rate; not policy grade; not a combined BC+QC-only national
total; not a strict-open dataset.

## 10. Files

| File | Content |
|---|---|
| `national_price_proxies.csv` | Province price low/base/high and tiers |
| `national_cost_proxies.csv` | Province logging+haul, road, silviculture and total cost |
| `national_margin_estimates.csv` | 39 province x scenario margin rows |
| `national_margin_summary.csv` | Province summary plus national weighted diagnostic |
| `assumptions_donor_register.csv` | Every donor, factor and coverage assumption |
| `sources.csv` | Source register with hashes and licences |
| `summary.json` | Machine-readable summary, validation and labels |
| `manifest.json` | Input/output hashes and coverage |
