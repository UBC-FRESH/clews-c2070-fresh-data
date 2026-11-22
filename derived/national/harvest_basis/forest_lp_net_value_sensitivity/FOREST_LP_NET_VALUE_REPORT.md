# Forest LP net-value sensitivity

**Generated:** 2026-11-22T16:42:39+00:00

**Model:** `forest_lp_net_value_sensitivity_v1` `1.0.0`

**Status:** `model_estimate_not_policy` · **Observed:** `false` · **Policy grade:** `false` · **LP objective:** `not_used`

This artifact joins the committed Forest LP v1 allocation rows to the committed national province margin totals and reports a volume-weighted net-value sensitivity. It does not solve an LP, change the Forest LP objective, or write back to any Forest LP v1 output.

## 1. Join and coverage

- Forest LP v1 allocation rows: **117** (13 provinces x 3 allocation levels x 3 cap cases).
- Province margin totals: **26** rows (13 provinces x 2 scenarios), from the artifact bundled in the `national-economics-v2.4` publication (underlying model `national_economics_v2_3`).
- Scenarios: `donor_flat` (base) and `stumpage_scaled` (sensitivity).
- Feasible allocation rows: **91**; infeasible and blank: **26**.
- Join key: `province` + `scenario`; the allocation level supplies the volume and the margin artifact supplies CAD/m3.

## 2. National totals by allocation case

Each row is the national sum for one cap case, allocation level, and scenario. Levels are alternative screening ladders and must not be summed across rows. Infeasible rows are blank.

| Scenario | Cap case | Level | Status | Allocation (Mm3) | Low (M CAD) | Base (M CAD) | High (M CAD) | Base (CAD/m3) | Negative base provinces |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| donor_flat | documented_ceiling | 100m | optimal | 100.000 | -3230.786923 | 4347.226340 | 7633.971898 | 43.4723 | none |
| stumpage_scaled | documented_ceiling | 100m | optimal | 100.000 | -6750.691500 | -559.722836 | 3359.095964 | -5.5972 | AB, MB, ON, QC, NB |
| donor_flat | documented_ceiling | 119m | optimal | 118.977 | -3854.908562 | 5205.328748 | 9137.988762 | 43.7506 | none |
| stumpage_scaled | documented_ceiling | 119m | optimal | 118.977 | -8058.885699 | -655.319123 | 4032.879740 | -5.5079 | AB, MB, ON, QC, NB |
| donor_flat | documented_ceiling | 150m | optimal | 150.000 | -4299.883636 | 6662.823950 | 11436.002324 | 44.4188 | none |
| stumpage_scaled | documented_ceiling | 150m | optimal | 150.000 | -9950.394662 | -1194.863823 | 4505.859579 | -7.9658 | AB, MB, ON, QC, NB |
| donor_flat | intensity_1.0 | 100m | optimal | 100.000 | -3494.678442 | 4377.398167 | 7811.963398 | 43.7740 | none |
| stumpage_scaled | intensity_1.0 | 100m | optimal | 100.000 | -7041.105130 | -588.308659 | 3481.717363 | -5.8831 | AB, MB, ON, QC, NB |
| donor_flat | intensity_1.0 | 119m | optimal | 118.977 | -4380.974391 | 5144.587973 | 9263.984141 | 43.2401 | none |
| stumpage_scaled | intensity_1.0 | 119m | optimal | 118.977 | -8500.784098 | -636.279694 | 4078.507445 | -5.3479 | AB, MB, ON, QC, NB |
| donor_flat | intensity_1.0 | 150m | infeasible | — | — | — | — | — | none |
| stumpage_scaled | intensity_1.0 | 150m | infeasible | — | — | — | — | — | none |
| donor_flat | intensity_1.2 | 100m | optimal | 100.000 | -3338.197498 | 4416.332373 | 7791.809234 | 44.1633 | none |
| stumpage_scaled | intensity_1.2 | 100m | optimal | 100.000 | -6938.015687 | -619.867990 | 3404.714702 | -6.1987 | AB, MB, ON, QC, NB |
| donor_flat | intensity_1.2 | 119m | optimal | 118.977 | -4142.893627 | 5212.079155 | 9292.896700 | 43.8073 | none |
| stumpage_scaled | intensity_1.2 | 119m | optimal | 118.977 | -8369.501089 | -705.812831 | 4132.820518 | -5.9323 | AB, MB, ON, QC, NB |
| donor_flat | intensity_1.2 | 150m | infeasible | — | — | — | — | — | none |
| stumpage_scaled | intensity_1.2 | 150m | infeasible | — | — | — | — | — | none |

## 3. Canonical 119 Mm3 documented-ceiling totals

The 119m documented-ceiling case is the committed allocation basis. The table is a model diagnostic, not an observed net value.

| Scenario | Role | Allocation (Mm3) | Low (M CAD) | Base (M CAD) | High (M CAD) | Base (CAD/m3) | Negative low/base/high provinces |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| donor_flat | base | 118.977 | -3854.908562 | 5205.328748 | 9137.988762 | 43.7506 | 4 / 0 / 0 |
| stumpage_scaled | sensitivity | 118.977 | -8058.885699 | -655.319123 | 4032.879740 | -5.5079 | 7 / 5 / 3 |

## 4. Negative rows

Negative margins and negative net values are retained unclipped. The table lists every negative base net-value province in the canonical 119m documented-ceiling case.

| Scenario | Province | Allocation (m3) | Base margin (CAD/m3) | Base net value (M CAD) |
| --- | --- | ---: | ---: | ---: |
| stumpage_scaled | AB | 22,891,404.0 | -36.3258 | -831.548563 |
| stumpage_scaled | MB | 1,135,235.8 | -30.6666 | -34.813822 |
| stumpage_scaled | ON | 13,493,596.0 | -60.9518 | -822.458965 |
| stumpage_scaled | QC | 26,674,334.0 | -35.8577 | -956.480266 |
| stumpage_scaled | NB | 6,234,700.0 | -14.1365 | -88.136837 |

## 5. Labels and caveats

- `net_value_label=model_estimate`
- `observed=false`
- `policy_grade=false`
- `net_value_status=model_estimate_not_policy`
- `lp_objective=not_used`
- `forest_lp_objective_changed=false`
- `v1_outputs_changed=false`
- `public_osecan_input=false`
- `restricted_data_used=false`

- Net value is a volume-weighted model estimate: allocation_m3 times province margin_cad_m3, divided by 1e6. It is not an observed transaction, a policy result, or a combined national net value.
- The Forest LP objective and every Forest LP v1 output are unchanged. Net value is used only for reporting and is not an LP objective or constraint.
- Negative margins and negative net values are retained without clipping. A negative value is a model result, not a data error.
- Infeasible allocation cases keep blank allocation and blank net-value fields. They are not clamped, back-filled, or allocated a zero value.
- The allocation levels are alternative screening ladders, not additive years or independent jurisdictions. National totals are reported per allocation case and must not be summed across levels.
- Donor-price and donor-cost provinces remain model estimates. Stumpage_scaled is a method sensitivity, not the base scenario.
- Nunavut has zero allocation volume in the 119m provenance, but a non-zero unit margin. Its net value is zero by multiplication where allocated volume is zero and is not an observed zero-profit finding.

## 6. Verification

| Check | Status | Detail |
| --- | --- | --- |
| allocation-rows: Forest LP v1 allocation rows preserved | pass | 117 rows (expected 117) |
| net-value-arithmetic: Net value equals allocation x margin / 1e6 | pass | 0 arithmetic mismatches |
| infeasible-blanks: Infeasible rows keep blank net values | pass | 0 non-blank values on infeasible rows |
| feasible-complete: Feasible rows carry all six net values | pass | 0 blank values on feasible rows |
| negative-unclipped: Negative values are retained without clipping | pass | 133 negative net-value cells; 0 sign/clipping mismatches |
| infeasible-count: Infeasible allocation rows are blank | pass | 26 infeasible rows |
| group-summaries: Allocation-level summaries cover cap x level x scenario | pass | 18 groups |
| national-rows: National totals cover every group and case | pass | 54 rows |
| national-equals-province-sum: National totals equal the province sum | pass | 0 total mismatches |
| tier-labels: Price and cost tiers match national_economics_v2_3 | pass | 0 tier mismatches |
| margin-total-crosscheck: Canonical 119m totals match the margin-total diagnostic | pass | max abs delta vs national_margin_totals.json: 0.000000959 M CAD |
| labels: Model-estimate labels are carried on every row | pass | observed=false, policy_grade=false, lp_objective=not_used |
| objective-unchanged: Forest LP objective and v1 outputs are unchanged | pass | 5 v1 output files hashed before and after; forest_lp_v1.py hash unchanged |
| no-restricted-data: No restricted or raw data is used | pass | all inputs are under data/derived or out/; restricted_data_used=false |
| no-public-ui: No UI or public OSeCAN publication is written | pass | output is a derived data artifact; public_osecan_input=false |

## 7. Reproduction

```bash
.venv/bin/python -m workflows.national.harvest.forest_lp_net_value
```

Inputs and outputs are hashed in `manifest.json`. The Forest LP v1 allocation is read from `out/forest_lp_v1/forest_lp_allocation.csv`; if it is absent, the generator runs the v1 synthesis first.
