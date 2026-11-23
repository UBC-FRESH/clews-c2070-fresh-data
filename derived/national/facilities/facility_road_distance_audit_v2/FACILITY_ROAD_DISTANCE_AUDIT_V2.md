# Facility road-distance audit v2

Generated: 2026-11-23T13:48:32+00:00

Status: **model estimate**. This audit fits province road factors but does not change any assignment and makes no national claim.

## Routing source

- Provider: OSRM public demo server
- Endpoint: `https://router.project-osrm.org` (driving profile)
- Road data: OpenStreetMap road network (ODbL-1.0, © OpenStreetMap contributors)
- Requests: 81 ok / 81 attempted; 0 failed.
- Rate limit: one request every 1.2 s.

## Sample

- Target: up to 10 eligible facilities per province across 13 jurisdictions.
- Realized: 81 pairs in 11 jurisdictions. Jurisdictions with fewer eligible facilities are sampled in full; NT and NU have no eligible located facility and are not fabricated.
- Selection: deterministic equal-frequency haversine quantile strata, median facility per stratum.

## Province factors

The factor is the province median `road km / haversine km`; the global 1.3 screen is shown only for comparison. A national factor is never substituted where province data exist.

| Province | Eligible | Sampled | OK | Outliers | Fit n | Median ratio | IQR | 90% CI | Factor | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| BC | 185 | 10 | 10 | 0 | 10 | 1.474247 | 0.199849 | 1.376556–1.591918 | 1.474247 | ['no_flags'] |
| AB | 20 | 10 | 10 | 1 | 9 | 1.304567 | 0.09939 | 1.280845–1.571542 | 1.304567 | ['outliers_excluded'] |
| SK | 3 | 3 | 3 | 0 | 3 | 1.396504 | 0.332719 | 1.396146–2.061584 | 1.396504 | ['low_n', 'tukey_fence_not_applied_small_n'] |
| MB | 5 | 5 | 5 | 0 | 5 | 1.456361 | 0.000311 | 1.341701–1.538554 | 1.456361 | ['tukey_fence_not_applied_small_n'] |
| ON | 37 | 10 | 10 | 2 | 8 | 1.358977 | 0.063021 | 1.308931–1.38098 | 1.358977 | ['outliers_excluded'] |
| QC | 283 | 10 | 10 | 0 | 10 | 2.417833 | 0.630685 | 1.956503–2.899029 | 2.417833 | ['no_flags'] |
| NB | 24 | 10 | 10 | 1 | 9 | 1.488075 | 0.366288 | 1.300486–1.715626 | 1.488075 | ['outliers_excluded'] |
| NS | 20 | 10 | 10 | 1 | 9 | 1.204041 | 0.090568 | 1.159782–1.29298 | 1.204041 | ['outliers_excluded'] |
| PE | 2 | 2 | 2 | 0 | 2 | 1.110171 | 0.00019 | 1.109982–1.110361 | 1.110171 | ['very_low_n', 'high_dispersion', 'tukey_fence_not_applied_small_n'] |
| NL | 11 | 10 | 10 | 2 | 8 | 2.004151 | 0.040385 | 1.98808–2.036525 | 2.004151 | ['outliers_excluded'] |
| YT | 1 | 1 | 1 | 0 | 1 | 1.725186 | 0 | 1.725186–1.725186 | 1.725186 | ['very_low_n', 'high_dispersion', 'tukey_fence_not_applied_small_n'] |
| NT | 0 | 0 | 0 | 0 | 0 | n/a | n/a | n/a–n/a | n/a | ['no_eligible_facilities'] |
| NU | 0 | 0 | 0 | 0 | 0 | n/a | n/a | n/a–n/a | n/a | ['no_eligible_facilities'] |

## Proxy comparison

| Metric | Global 1.3 | Province factor |
|---|---|---|
| Mean absolute proxy error % | 18.860598 | 8.872279 |
| Median absolute proxy error % | 12.920035 | 5.342221 |
| Within 10% of routed distance | 0.37037 | 0.679012 |

## Method and limits

- A routed road distance cannot be materially shorter than the great-circle distance; pairs below 0.90 are failed, not fitted.
- Outliers use physical bounds [0.90, 5.0] and, at n >= 8, a 1.5x Tukey fence on log ratios. Excluded pairs remain in the sample table with `ratio_used_in_fit=false`.
- Factors are capped to [1.0, 3.0]. Cap, low-n, wide dispersion, route failure, and small-n fence flags are reported in `province_road_factors.csv`.
- OSRM routes start and end at the nearest road point; the off-road connector is not included. Large snap distances are reported and are a source of uncertainty, not a fabricated correction.
- The OSRM car profile may route through the United States where that is the shortest path; no border delay or customs cost is modelled.
- Distances are car-road distances. Resource roads, winter roads, ferries, weight limits, and log-truck restrictions are not validated.

## Labels

- `model_estimate`; `observed=false`; `policy_grade=false`.
- No assignment change; no national single factor; no legal, AAC, or operating-status claim.
- No UI or public OSeCAN surface is changed.

## Provenance

- National facility capacity v3: `data/derived/national/facilities/national_facility_capacity_v3/national_facility_capacity_v3.csv` (project-derived; see source metadata); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`
- GeoBoundaries Canada ADM1 simplified: `data/raw/boundaries/canada_adm1_geoboundaries_simplified.geojson` (CC BY 4.0); `https://github.com/UBC-FRESH/clews-c2070-fresh-data`
- National facility assignment v6: `data/derived/national/facilities/national_facility_assignment_v6/facility_assignment.csv` (project-derived; see source metadata); `https://github.com/UBC-FRESH/clews-c2070-fresh`
- OSRM public demo server: `osrm_routes.json` (ODbL-1.0); `https://router.project-osrm.org/route/v1/driving`
- OpenStreetMap contributors: (ODbL-1.0); `https://www.openstreetmap.org/copyright`

Reproduce: `.venv/bin/python -m workflows.national.facilities.facility_road_distance_audit_v2`
