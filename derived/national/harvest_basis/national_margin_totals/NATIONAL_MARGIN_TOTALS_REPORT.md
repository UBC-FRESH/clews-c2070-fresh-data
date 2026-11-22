# National margin totals at the 119 Mm3 allocation

Generated: 2026-11-22T16:24:47+00:00

## Purpose and labels

This artifact multiplies the committed v2.3 model margins by the committed 119 Mm3 provincial allocation. It is a `model_estimate_not_policy` diagnostic: `observed=false`, `policy_grade=false`, and `combined_national_net_value=false`. It is not a policy result.

## National totals

| Scenario | Role | Low (M CAD) | Base (M CAD) | High (M CAD) | Base CAD/m3 | Positive / negative / zero provinces (base) |
|---|---|---:|---:|---:|---:|---:|
| donor_flat | base | -3854.908563 | 5205.328748 | 9137.988762 | 43.7506 | 12 / 0 / 1 |
| stumpage_scaled | sensitivity | -8058.885700 | -655.319124 | 4032.879740 | -5.5079 | 7 / 5 / 1 |

Allocation total: **118,977,339.1 m3**. Nunavut is held at zero volume and therefore zero total in both scenarios; its unit margin is not clipped or reclassified.

## Province totals and shares

### donor_flat (base)

| Province | Allocation (m3) | Margin base (CAD/m3) | Total low | Total base | Total high | Base share | Negative base |
|---|---:|---:|---:|---:|---:|---:|---|
| BC | 39,978,577.0 | 41.5880 | -3601.150280 | 1662.629060 | 3786.343043 | 0.319409 | false |
| AB | 22,891,404.0 | 60.8415 | 457.519046 | 1392.747356 | 1743.244511 | 0.267562 | false |
| SK | 4,344,697.6 | 79.4071 | 167.497216 | 344.999837 | 411.522805 | 0.066278 | false |
| MB | 1,135,235.8 | 62.9575 | 25.091549 | 71.471608 | 88.853544 | 0.013730 | false |
| ON | 13,493,596.0 | 32.0987 | -118.153975 | 433.126890 | 639.731386 | 0.083208 | false |
| QC | 26,674,334.0 | 32.4580 | -792.947927 | 865.795533 | 1873.586548 | 0.166329 | false |
| NB | 6,234,700.0 | 17.1615 | -147.721864 | 106.996804 | 202.458166 | 0.020555 | false |
| NS | 2,388,245.0 | 76.3049 | 84.663046 | 182.234796 | 218.801932 | 0.035009 | false |
| NL | 1,454,037.5 | 79.7102 | 56.496918 | 115.901620 | 138.164824 | 0.022266 | false |
| PE | 302,210.4 | 70.6565 | 9.006323 | 21.353129 | 25.980363 | 0.004102 | false |
| YT | 43,925.8 | 91.6445 | 2.230969 | 4.025558 | 4.698119 | 0.000773 | false |
| NT | 36,376.0 | 111.2425 | 2.560416 | 4.046557 | 4.603521 | 0.000777 | false |
| NU | 0.0 | 28.8899 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | false |

Negative provinces by case: low BC, ON, QC, NB; base none; high none.

### stumpage_scaled (sensitivity)

| Province | Allocation (m3) | Margin base (CAD/m3) | Total low | Total base | Total high | Base share | Negative base |
|---|---:|---:|---:|---:|---:|---:|---|
| BC | 39,978,577.0 | 41.5880 | -3601.150280 | 1662.629060 | 3786.343043 | -2.537129 | false |
| AB | 22,891,404.0 | -36.3258 | -1125.719129 | -831.548563 | -149.762432 | 1.268922 | true |
| SK | 4,344,697.6 | 16.3892 | -133.564694 | 71.206118 | 101.536452 | -0.108659 | false |
| MB | 1,135,235.8 | -30.6666 | -48.663926 | -34.813822 | -31.481792 | 0.053125 | true |
| ON | 13,493,596.0 | -60.9518 | -951.204063 | -822.458965 | -781.829747 | 1.255051 | true |
| QC | 26,674,334.0 | -35.8577 | -2042.384401 | -956.480266 | 667.485197 | 1.459564 | true |
| NB | 6,234,700.0 | -14.1365 | -287.917823 | -88.136837 | 29.407209 | 0.134495 | true |
| NS | 2,388,245.0 | 83.3069 | 61.423990 | 198.957287 | 237.734983 | -0.303604 | false |
| NL | 1,454,037.5 | 79.7102 | 56.496918 | 115.901620 | 138.164824 | -0.176863 | false |
| PE | 302,210.4 | 70.6565 | 9.006323 | 21.353129 | 25.980363 | -0.032584 | false |
| YT | 43,925.8 | 91.6445 | 2.230969 | 4.025558 | 4.698119 | -0.006143 | false |
| NT | 36,376.0 | 111.2425 | 2.560416 | 4.046557 | 4.603521 | -0.006175 | false |
| NU | 0.0 | 28.8899 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | false |

Negative provinces by case: low BC, AB, SK, MB, ON, QC, NB; base AB, MB, ON, QC, NB; high AB, MB, ON.

## Negative and zero-volume handling

Negative margins and negative totals are retained unclipped. `negative_flag` marks a negative base unit margin; the case flags remain available in the CSV. Nunavut's zero allocation makes its total zero, which is a multiplication result, not an observed zero-profit finding.

## Cross-check against v2.3

The computed 119 Mm3 national unit margins match the v2.3 `119m_allocation_sensitivity` diagnostic. Maximum absolute difference: **0.000000 CAD/m3**.

## Caveats

- Totals multiply committed v2.3 CAD/m3 margins by the 119 Mm3 provincial allocation; observed 2024 harvest is not the multiplier here.
- The national total is a volume-weighted model diagnostic labelled model_estimate_not_policy. It is not a policy result and not a combined national net value.
- Negative margins and negative totals are retained unclipped; they are not set to zero or omitted.
- Nunavut has zero allocation volume, so its total is zero by multiplication. Its unit margin is still shown and is not treated as observed.
- No jurisdiction is ranked. Donor-price and donor-cost provinces remain model estimates and are not reclassified as observed.
- Stumpage_scaled is a method sensitivity, not the base scenario, and is not observed or policy grade.

## Non-claims

- Not a combined national net value.
- Not observed; observed=false.
- Not policy grade; policy_grade=false.
- Not a policy result or policy frontier.
- Not a Forest LP objective or constraint input.
- Not a public OSeCAN input.
- No margin ranking and no observed reclassification of donor-only provinces.

## Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.national_margin_totals
```
