# National Facility Assignment V6

Assignment v6 runs the 119 Mm3 harvest case on capacity v3 with the 1.2x provincial capacity floor applied as the primary case. Proxy capacity only is scaled where a province is short; published capacity is unchanged. Allocation is local first and cross-border only serves the remaining local residual. All values are model estimates: `observed=false`, `policy_grade=false`.

## V5 primary versus V6 floor

| Metric | V5 | V6 | Delta v6-v5 |
|---|---|---|---|
| assigned_m3 | 118977339.1 | 118977339.1 | 0 |
| local_m3 | 97075401.469233 | 118940963.1 | 21865561.630767 |
| local_share | 0.815915 | 0.999694 | 0.183779 |
| cross_border_m3 | 21901937.630767 | 36376 | -21865561.630767 |
| cross_border_share | 0.184085 | 0.000306 | -0.183779 |
| proxy_m3 | 40318991.203272 | 47463455.792305 | 7144464.589033 |
| proxy_share_of_assigned | 0.33888 | 0.398929 | 0.060049 |
| scaled_proxy_m3 | 0 | 38034798.630767 | 38034798.630767 |
| published_m3 | 78658347.896728 | 71513883.307695 | -7144464.589033 |
| published_share | 0.66112 | 0.601071 | -0.060049 |
| facilities_used | 263 | 208 | -55 |
| max_facility_m3 | 2162922.563248 | 8093104.685436 | 5930182.122188 |
| max_facility_share | 0.018179 | 0.068022 | 0.049843 |
| top5_share | 0.079789 | 0.157464 | 0.077675 |
| hhi | 0.007546 | 0.01287 | 0.005324 |
| capacity_shortfall_m3_y | 30282199.510767 | 43651.2 | -30238548.310767 |
| provinces_below_floor | 5 | 1 | -4 |

## Provincial capacity floor

| Province | Harvest | Published | Proxy before | Proxy after | Scale | V5 shortfall | V6 shortfall |
|---|---|---|---|---|---|---|---|
| BC | 39,978,577 | 96,053,794 | 35,515,531 | 35,515,531 | 1.00 | 0 | 0 |
| AB | 22,891,404 | 2,159,818 | 5,618,186 | 25,309,866 | 4.50 | 19,691,680 | 0 |
| SK | 4,344,698 | 0 | 708,513 | 5,213,637 | 7.36 | 4,505,124 | 0 |
| MB | 1,135,236 | 21,538 | 708,513 | 1,340,744 | 1.89 | 632,231 | 0 |
| ON | 13,493,596 | 1,685,154 | 9,097,649 | 14,507,161 | 1.59 | 5,409,512 | 0 |
| QC | 26,674,334 | 65,694,025 | 29,193,204 | 29,193,204 | 1.00 | 0 | 0 |
| NB | 6,234,700 | 745,231 | 9,168,164 | 9,168,164 | 1.00 | 0 | 0 |
| NS | 2,388,245 | 230,769 | 10,092,720 | 10,092,720 | 1.00 | 0 | 0 |
| PE | 302,210 | 0 | 472,342 | 472,342 | 1.00 | 0 | 0 |
| NL | 1,454,038 | 18,462 | 3,922,015 | 3,922,015 | 1.00 | 0 | 0 |
| YT | 43,926 | 0 | 236,171 | 236,171 | 1.00 | 0 | 0 |
| NT | 36,376 | 0 | 0 | 0 | 1.00 | 43,651 | 43,651 |
| NU | 0 | 0 | 0 | 0 | 1.00 | 0 | 0 |

## Validation

- `conservation_gap_m3`: {'province_capacity_floor': 0.0, 'published_plus_proxy': 0.0, 'published_only': 0.0}
- `known_capacity_violations`: 0
- `unbounded_assignments`: 0
- `non_operating_assignments`: 0
- `max_utilization`: {'province_capacity_floor': 1.0, 'published_plus_proxy': 1.0, 'published_only': 1.0}
- `max_single_facility_share`: {'province_capacity_floor': 0.0680222363910337, 'published_plus_proxy': 0.018179281698593643, 'published_only': 0.02940290585133787}
- `capacity_v3_record_count`: 689
- `published_capacity_unchanged`: True
- `scaled_records_are_proxy_only`: True
- `scaled_proxy_records`: 47
- `scaled_provinces`: ['AB', 'SK', 'MB', 'ON']
- `local_first`: True
- `cross_border_rule`: post_local_residual_only
- `v5_floor_reproduction`: {'assigned_m3': {'v5': 118977339.10000001, 'v6': 118977339.10000001, 'abs_delta': 0.0}, 'published_m3': {'v5': 71513883.307695, 'v6': 71513883.307695, 'abs_delta': 0.0}, 'proxy_m3': {'v5': 47463455.79230501, 'v6': 47463455.79230501, 'abs_delta': 0.0}, 'cross_border_m3': {'v5': 36376.0, 'v6': 36376.0, 'abs_delta': 0.0}, 'facilities_used': {'v5': 208.0, 'v6': 208.0, 'abs_delta': 0.0}, 'max_facility_share': {'v5': 0.0680222363910337, 'v6': 0.0680222363910337, 'abs_delta': 0.0}, 'hhi': {'v5': 0.01287037617184876, 'v6': 0.01287037617184876, 'abs_delta': 0.0}}
- `v5_floor_reproduced`: True
- `capacity_shortfall_before_m3_y`: 30282199.510767
- `capacity_shortfall_after_m3_y`: 43651.20000000372
- `provinces_below_floor_before`: 5
- `provinces_below_floor_after`: 1
- `comparison_rows`: 17
- `no_unbounded_facility`: True
- `all_facilities_finite_capacity`: True
- `no_restricted_sources`: True
- `no_ui_or_public_osecan_change`: True

## Caveats

- All volumes are model estimates (`model_estimate`); `observed=false` and `policy_grade=false`.
- The 119 Mm3 case is a planning allocation, not a legal AAC, a sustainable-supply determination, or an observed harvest outcome.
- The 1.2x provincial floor is a documented sensitivity assumption. Scaled proxy capacity is not observed capacity and is not evidence of provincial self-sufficiency.
- Published capacity is never altered by the floor. Only class-median proxy records can be scaled, and every scaled row carries `capacity_status=proxy_harvest_scaled`.
- Allocation is local first; cross-border volume is only the residual that local finite capacity cannot serve. It is a screening result, not an interprovincial trade forecast.
- No unbounded facility exists: every assignment row carries a finite capacity.
- No restricted or proprietary data are used. No UI or public OSeCAN surface is changed by this artifact.
