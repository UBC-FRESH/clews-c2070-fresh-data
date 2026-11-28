# National RSYC natural 5-parameter transform v1

Generated: 2026-11-28T17:07:39+00:00

## Status

This artifact recomputes all 3,948 RSYC cells with BC natural 5-parameter donors only. It reuses the fitted donor classes from `national_rsyc_transform_v1` and does not refit or delete the managed curves. Every curve preserves raw RSYC V100 (or raw peak when V100 is not meaningful). Labels: `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`, `natural_5param_only=true`, `managed_basis_quarantined=true`.

## Counts

- Curves: 3,948
- Rows: 789,600
- Provinces / species: 13 / 12
- Source managed cells rebuilt with natural donors: 1,926
- Source natural cells recomputed with the same natural policy: 2,022
- QC pass / flag / fail: 467 / 3,481 / 0
- V100 max absolute error: 0.000000 m3/ha

## CMAI

| Group | n | Raw CMAI median | Raw CMAI age median | Natural CMAI median | Natural CMAI age median |
|---|---:|---:|---:|---:|---:|
| conifer | 3,393 | 2.266 | 2 | 0.950 | 111 |
| deciduous | 555 | 2.119 | 24 | 1.114 | 119 |

Overall natural CMAI median: 0.966 m3/ha/yr at age 111. The low overall median is driven by northern low-productivity curves; area-weighted, BC, and productive-subset medians are reported by the corrected WS4 artifact.

## Reproduction

Build: `python -m scripts.national.build_rsyc_transform_natural_v1`.
Consume `usable_total_volume=true` rows; all rows in this artifact are natural and usable.
