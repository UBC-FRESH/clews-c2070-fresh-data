# National Economics v2.3 - StatCan industry aggregate cost proxy

Generated: 2026-11-22T15:36:32+00:00

## What changed

Version 2.3 keeps the v2.1/v2.2 price scenarios unchanged. The base price scenario remains `donor_flat`; `stumpage_scaled` remains a sensitivity. Costs change only for the eleven jurisdictions outside BC and QC, which now use the Statistics Canada NAICS 11331 industry aggregate expense per m3 as a total-cost proxy.

## Cost mapping

| Province group | Cost basis | Low | Base | High | Tier |
|---|---|---:|---:|---:|---|
| BC | v2.2 component stack | 36.4300 | 74.2400 | 165.0500 | `component_mix_partial_direct` |
| QC | v2.2 component stack | 60.9000 | 83.3700 | 104.7000 | `component_survey_aggregate` |
| AB, SK, MB, ON, NB, NS, NL, PE, YT, NT | StatCan NAICS 11331 aggregate total cost | point | point | point | `industry_aggregate_proxy` |
| NU | explicit v2.2 donor-total fallback | 52.0003 | 86.9381 | 180.2789 | `donor_fallback_total` |

StatCan values are total expenses divided by `observed_2024_m3`. The 119 Mm3 ratio is retained only as a sensitivity column and is not used in the margins. The aggregate includes overheads and does not provide a logging/haul breakdown; no road, silviculture or haul component is added to it.

## Margins and coverage delta

| Province | Base donor_flat low | Base donor_flat central | Base donor_flat high | Sensitivity scaled central |
|---|---:|---:|---:|---:|
| BC | -90.0770 | 41.5880 | 94.7093 | 41.5880 |
| AB | 19.9865 | 60.8415 | 76.1528 | -36.3258 |
| SK | 38.5521 | 79.4071 | 94.7184 | 16.3892 |
| MB | 22.1025 | 62.9575 | 78.2688 | -30.6666 |
| ON | -8.7563 | 32.0987 | 47.4100 | -60.9518 |
| QC | -29.7270 | 32.4580 | 70.2393 | -35.8577 |
| NB | -23.6935 | 17.1615 | 32.4728 | -14.1365 |
| NS | 35.4499 | 76.3049 | 91.6162 | 83.3069 |
| NL | 38.8552 | 79.7102 | 95.0215 | 79.7102 |
| PE | 29.8015 | 70.6565 | 85.9678 | 70.6565 |
| YT | 50.7895 | 91.6445 | 106.9558 | 91.6445 |
| NT | 70.3875 | 111.2425 | 126.5538 | 111.2425 |
| NU | -105.3059 | 28.8899 | 79.1390 | 28.8899 |

| Scenario | Volume basis | Low | Base | High | Label | Combined net value |
|---|---|---:|---:|---:|---|---|
| donor_flat | observed_2024_m3 | -32.1594 | 43.0187 | 75.5834 | `model_estimate_not_policy` | false |
| donor_flat | 119m_allocation_sensitivity | -32.4004 | 43.7506 | 76.8044 | `model_estimate_not_policy` | false |
| stumpage_scaled | observed_2024_m3 | -67.1392 | -5.7444 | 33.0932 | `model_estimate_not_policy` | false |
| stumpage_scaled | 119m_allocation_sensitivity | -67.7346 | -5.5079 | 33.8962 | `model_estimate_not_policy` | false |

Observed 2024 harvest is the primary volume denominator. The 119 Mm3 allocation is a sensitivity, not the primary ratio.

### Cost-proxy coverage before and after

| Volume basis | Version | Aggregate-proxy cells | Donor-proxy cells | Donor fallback cells | Component cells | Aggregate-proxy volume share | Donor-proxy volume share |
|---|---|---:|---:|---:|---:|---:|---:|
| observed 2024 | v2.2 | 0 | 11 | 0 | 2 | 0.00000000 | 0.45522715 |
| observed 2024 | v2.3 | 10 | 0 | 1 | 2 | 0.45522715 | 0.00000000 |
| 119 Mm3 sensitivity | v2.2 | 0 | 11 | 0 | 2 | 0.00000000 | 0.43978482 |
| 119 Mm3 sensitivity | v2.3 | 10 | 0 | 1 | 2 | 0.43978482 | 0.00000000 |

Cost-proxy upgrades: **10** province cells changed from donor costs to the StatCan aggregate proxy. This is not direct-cost coverage: the aggregate is a NAICS 11331 industry total, not an observed logging or haul cost.

## ON and AB results

Alberta and Ontario are the two largest aggregate-proxy replacements after BC/QC. Their donor stacks were identical to the v2.2 AB/ON donor values; the central cost changes are shown in `v2_2_v2_3_comparison.csv`.

- **AB**: aggregate proxy 54.9865 CAD/m3; central donor_flat margin 60.8415 CAD/m3; v2.2-to-v2.3 margin delta 25.8055 CAD/m3.
- **ON**: aggregate proxy 83.7293 CAD/m3; central donor_flat margin 32.0987 CAD/m3; v2.2-to-v2.3 margin delta -3.1028 CAD/m3.

## Caveats

- **Employer-establishment coverage**: the Annual Survey of Manufacturing and Logging Industries covers employer establishments. Non-employer contractors, owner-operators and informal or community harvest are not fully represented while the harvest denominator includes all provincial harvest; this can bias CAD/m3 downward, especially in the territories.
- **2024 preliminary**: reference year 2024 is the latest available and is preliminary and subject to revision. Values are nominal 2024 CAD; no deflator or escalation is applied.
- **Materials double-count risk**: the aggregate includes materials and supplies, which may include payments to contract loggers (NAICS 113312). Contract logging is a child industry and must not be added to the parent aggregate; doing so would double count.
- **Not a logging/haul breakdown**: total expenses include administration, depreciation, overhead, non-logging activity and any in-forest hauling performed by logging establishments. They are not a logging-only or haul-only cost curve.
- **No separate haul add-on**: the aggregate already includes any hauling performed by logging establishments. Do not add a separate truck-haul, road or silviculture cost to it without checking overlap; v2.3 adds none.
- **NU blank**: Nunavut has zero reported harvest and blank StatCan CAD/m3. The explicit v2.2 donor-total fallback is retained; no StatCan value is fabricated.

## Negative margins and labels

21 of 78 margin rows are negative and are **unclipped**.
- `donor_flat`: 5 negative rows.
- `stumpage_scaled`: 16 negative rows.

No value is observed: every row carries `evidence=model_estimate`, `observed=false`, `policy_grade=false` and `combined_national_net_value=false`.

## Non-claims

- Not observed profit, not a mill margin and not official net value.
- The StatCan aggregate is not observed and is not an observed logging cost or a policy-grade value.
- No combined national net value is computed.
- No strict-open licence claim is made; source documents are not redistributed.
- No restricted, confidential or microdata input is used.

## Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.national_economics_v2_3
```
