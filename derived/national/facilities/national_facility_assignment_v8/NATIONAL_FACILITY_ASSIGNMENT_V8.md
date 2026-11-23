# National Facility Assignment V8 (Province Road Factors)

Assignment v8 is the distance-only rerun of assignment v6. Capacity v3, the 1.2x provincial floor, products, and residue are unchanged. Each candidate's haversine distance is multiplied by the facility-province factor from the expanded OSRM audit. All values are model estimates: `observed=false`, `policy_grade=false`.

## V6 versus V8

| Metric | V6 | V8 | Delta | Delta % |
|---|---:|---:|---:|---:|
| assigned_m3 | 118977339.1 | 118977339.1 | 0 | 0 |
| local_m3 | 118940963.1 | 118940963.1 | 0 | 0 |
| local_share | 0.999694 | 0.999694 | 0 | 0 |
| cross_border_m3 | 36376 | 36376 | 0 | 0 |
| cross_border_share | 0.000306 | 0.000306 | 0 | 0 |
| proxy_m3 | 47463455.792305 | 47463455.792305 | 0 | 0 |
| proxy_share_of_assigned | 0.398929 | 0.398929 | 0 | 0 |
| facilities_used | 208 | 208 | 0 | 0 |
| max_facility_share | 0.068022 | 0.068022 | 0 | 0 |
| top5_share | 0.157464 | 0.157464 | 0 | 0 |
| hhi | 0.01287 | 0.01287 | 0 | 0 |
| unassigned_m3 | 0 | 0 | 0 |  |
| volume_weighted_mean_road_distance_km | 402.122851 | 558.536156 | 156.413305 | 38.896895 |
| total_volume_distance_m3_km | 47843506815.642181 | 66453145604.571678 | 18609638788.929497 | 38.896895 |
| median_row_road_distance_km | 525.318549 | 542.272459 | 16.95391 | 3.227358 |
| max_row_road_distance_km | 1201.811125 | 1527.025157 | 325.214032 | 27.060328 |

## Distance comparison

- Rows v6 / v8: 208 / 208.
- Common rows: 208; added: 0; removed: 0.
- Rows with changed road distance: 208.
- Assigned volume moved between facilities: 0 m3.
- Provinces with a changed assignment: none.

Local candidates in one province all receive the same province factor, so the local-first order is invariant. Any assignment change is confined to the cross-border residual. In this run the cross-border recipient did not switch, so all assignment-composition metrics are unchanged.

## Province factors

| Province | Factor v6 | Factor v8 | Delta % | n | IQR | 90% CI | Flags |
|---|---:|---:|---:|---:|---:|---|---|
| BC | 1.3 | 1.474247 | 13.403584 | 10 | 0.19984889964846375 | 1.3765563724396437–1.5919181531079478 | ['no_flags'] |
| AB | 1.3 | 1.304567 | 0.351283 | 9 | 0.09939047929245493 | 1.280845110017304–1.5715422738745886 | ['outliers_excluded'] |
| SK | 1.3 | 1.396504 | 7.42338 | 3 | 0.33271901163592355 | 1.3961464588212247–2.061584482093072 | ['low_n', 'tukey_fence_not_applied_small_n'] |
| MB | 1.3 | 1.456361 | 12.027741 | 5 | 0.0003107881911943444 | 1.3417006903071553–1.5385535760349085 | ['tukey_fence_not_applied_small_n'] |
| ON | 1.3 | 1.358977 | 4.536686 | 8 | 0.06302093287181298 | 1.3089308119350398–1.3809802932130486 | ['outliers_excluded'] |
| QC | 1.3 | 2.417833 | 85.987149 | 10 | 0.6306852620382806 | 1.9565025127298732–2.899029043698541 | ['no_flags'] |
| NB | 1.3 | 1.488075 | 14.467287 | 9 | 0.36628792713314806 | 1.3004856563601612–1.715625960200113 | ['outliers_excluded'] |
| NS | 1.3 | 1.204041 | -7.381424 | 9 | 0.09056817905760584 | 1.1597823379033791–1.2929799862655653 | ['outliers_excluded'] |
| PE | 1.3 | 1.110171 | -14.602197 | 2 | 0.0001898624411966754 | 1.10998157707204–1.1103613019544336 | ['very_low_n', 'high_dispersion', 'tukey_fence_not_applied_small_n'] |
| NL | 1.3 | 2.004151 | 54.165477 | 8 | 0.040384979171484314 | 1.988079599844687–2.036524863811142 | ['outliers_excluded'] |
| YT | 1.3 | 1.725186 | 32.706651 | 1 | 0.0 | 1.7251864577854052–1.7251864577854052 | ['very_low_n', 'high_dispersion', 'tukey_fence_not_applied_small_n'] |
| NT | 1.3 | n/a | n/a | 0 | n/a | n/a–n/a | ['no_eligible_facilities'] |
| NU | 1.3 | n/a | n/a | 0 | n/a | n/a–n/a | ['no_eligible_facilities'] |

### Province distance impact

| Province | V6 weighted km | V8 weighted km | Delta km | Delta % | Changed rows |
|---|---:|---:|---:|---:|---:|
| BC | 273.912771 | 310.6269 | 36.714129 | 13.403584 | 53 |
| AB | 232.17794 | 232.993542 | 0.815602 | 0.351283 | 16 |
| SK | 281.239649 | 302.117137 | 20.877488 | 7.42338 | 3 |
| MB | 703.968363 | 788.639857 | 84.671494 | 12.027741 | 5 |
| ON | 670.345863 | 700.757347 | 30.411484 | 4.536686 | 30 |
| QC | 694.24941 | 1291.214685 | 596.965275 | 85.987149 | 65 |
| NB | 138.889292 | 158.982804 | 20.093512 | 14.467287 | 22 |
| NS | 61.117275 | 56.60595 | -4.511325 | -7.381424 | 8 |
| PE | 77.403592 | 66.100967 | -11.302625 | -14.602197 | 2 |
| NL | 616.006713 | 949.669685 | 333.662972 | 54.165477 | 2 |
| YT | 414.21172 | 549.6865 | 135.47478 | 32.706651 | 1 |
| NT | 1201.811125 | 1206.032883 | 4.221759 | 0.351283 | 1 |

## Method

- Allocation is local first; cross-border volume is only the residual that local finite capacity cannot serve.
- Road distance = haversine distance x province factor of the candidate facility. For a local candidate that province is also the route province sampled by the OSRM audit. For a cross-border candidate it is a documented screening extension, not an observed border-route factor.
- Factor basis: province median `road km / haversine km` from `facility_road_distance_audit_v2`, capped to [1.0, 3.0]. Outliers, low n, and wide dispersion are flagged in that artifact.
- NT and NU have no eligible located facility in the audit; they receive no local factor and no facility is fabricated.

## Validation

- `conservation_gap_m3`: True
- `local_plus_cross_equals_assigned`: True
- `capacity_bounds`: True
- `no_nan_or_negative`: True
- `factor_coverage`: True
- `local_first`: True
- `capacity_floor_unchanged`: True
- `distance_comparison_rows`: True
- `assignment_conservation`: True

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- The 119 Mm3 case is a planning allocation, not a legal AAC, a sustainable-supply determination, or an observed harvest outcome.
- Only the road-distance screen changed. Capacity v3, the 1.2x provincial floor, product coefficients, and residue coefficients are unchanged from v6.
- Province factors are median OSRM road/haversine ratios from a small deterministic sample; low-n provinces (SK, MB, PE, YT) and wide-dispersion provinces are flagged in the audit.
- A facility-province factor is applied to cross-border candidates as a screening extension. It is not an observed border-route factor and no customs or border delay is modelled.
- Local-first order within a province is invariant under a uniform province factor; observed assignment changes are confined to the cross-border residual.
- Allocation is a screening result, not an interprovincial trade forecast. No UI or official OSeCAN surface is changed.
