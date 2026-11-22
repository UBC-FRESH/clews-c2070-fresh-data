# Forestry Residue Handoff to OSeCAN v1

This is a read-only forestry-side screening handoff from `national_residue_curve_v1` province/case totals to OSeCAN zones. It is not an official OSeCAN result, an operating plan, or a policy target.

All values are model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`, and `official_osecan_changed=false`. Process and harvest residue remain separate streams and are never summed into a combined row.

## Labels and boundary

- `official_osecan_changed=false` on every row.
- No official OSeCAN file and no public OSeCAN surface is modified.
- The OSeCAN tree is hashed before and after the build; hashes must match.
- The 2050 OSeCAN supply values are context, not policy targets.

## Zone mapping and coverage

9 of 13 jurisdictions map to exactly one OSeCAN zone. The remaining provinces span multiple zones and are kept in the explicit `UNMAPPED` bucket.

| Zone | Provinces mapped | Status |
|---|---|---|
| B1 | — | not_mapped_from_province_rows |
| B2 | — | not_mapped_from_province_rows |
| A1 | — | not_mapped_from_province_rows |
| A2 | — | not_mapped_from_province_rows |
| S1 | SK | mapped_single_zone |
| M1 | MB | mapped_single_zone |
| O1 | — | not_mapped_from_province_rows |
| O2 | — | not_mapped_from_province_rows |
| Q1 | — | not_mapped_from_province_rows |
| Q2 | — | not_mapped_from_province_rows |
| T1 | NB, NS, PE | mapped_aggregate_zone |
| L1 | NL | mapped_single_zone |
| N1 | YT, NT, NU | mapped_aggregate_zone |
| UNMAPPED | BC, AB, ON, QC | unmapped_multi_zone_province |

Volume coverage by case (PJ):

| Stream | Case | Mapped | UNMAPPED | Total |
|---|---|---:|---:|---:|
| process | `process_availability_000` | 0.000 | 0.000 | 0.000 |
| process | `process_availability_025` | 13.712 | 117.790 | 131.501 |
| process | `process_availability_050` | 27.424 | 235.579 | 263.003 |
| process | `process_availability_075` | 41.136 | 353.369 | 394.504 |
| harvest | `harvest_recovery_035` | 7.867 | 50.855 | 58.722 |
| harvest | `harvest_recovery_060` | 13.486 | 87.181 | 100.667 |
| harvest | `harvest_recovery_075` | 16.858 | 108.976 | 125.834 |

## Handoff PJ by zone/case

| Zone | Process 0% | Process 25% | Process 50% | Process 75% | Harvest 35% | Harvest 60% | Harvest 75% |
|---|---:|---:|---:|---:|---:|---:|---:|
| S1 | 0.000 | 3.159 | 6.317 | 9.476 | 2.144 | 3.676 | 4.595 |
| M1 | 0.000 | 0.825 | 1.651 | 2.476 | 0.560 | 0.961 | 1.201 |
| T1 | 0.000 | 9.176 | 18.353 | 27.529 | 4.405 | 7.552 | 9.440 |
| L1 | 0.000 | 0.520 | 1.039 | 1.559 | 0.718 | 1.230 | 1.538 |
| N1 | 0.000 | 0.032 | 0.064 | 0.096 | 0.040 | 0.068 | 0.085 |
| UNMAPPED | 0.000 | 117.790 | 235.579 | 353.369 | 50.855 | 87.181 | 108.976 |

National totals (PJ):

| Stream | Case | PJ |
|---|---|---:|
| process | `process_availability_000` | 0.000000 |
| process | `process_availability_025` | 131.501392 |
| process | `process_availability_050` | 263.002784 |
| process | `process_availability_075` | 394.504175 |
| harvest | `harvest_recovery_035` | 58.722480 |
| harvest | `harvest_recovery_060` | 100.667108 |
| harvest | `harvest_recovery_075` | 125.833885 |

## Supply-curve comparison

Ratios are case PJ divided by the reference. Headroom is reference minus case; a negative headroom means the case exceeds the reference. The 2050 values are context, not policy targets.

### National

| Case | PJ | Tier | T1 headroom | T2 headroom | T3 headroom | T4 headroom | 2050 context ratio | 2050 context headroom |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | T1 | 85.007 | 109.399 | 149.273 | 213.538 | 0.000 | 152.923 |
| `process_availability_025` | 131.501 | T3 | -46.494 | -22.103 | 17.771 | 82.037 | 0.860 | 21.421 |
| `process_availability_050` | 263.003 | above_T4 | -177.996 | -153.604 | -113.730 | -49.465 | 1.720 | -110.080 |
| `process_availability_075` | 394.504 | above_T4 | -309.497 | -285.105 | -245.232 | -180.966 | 2.580 | -241.581 |
| `harvest_recovery_035` | 58.722 | T1 | 26.285 | 50.676 | 90.550 | 154.816 | 0.384 | 94.200 |
| `harvest_recovery_060` | 100.667 | T2 | -15.660 | 8.732 | 48.605 | 112.871 | 0.658 | 52.256 |
| `harvest_recovery_075` | 125.834 | T3 | -40.827 | -16.435 | 23.439 | 87.704 | 0.823 | 27.089 |

### BC

| Case | PJ | BC zonal cap ratio | BC zonal headroom | 2050 BC context ratio | 2050 BC context headroom |
|---|---:|---:|---:|---:|---:|
| `process_availability_000` | 0.000 | 0.000 | 43.524 | 0.000 | 43.524 |
| `process_availability_025` | 47.344 | 1.088 | -3.820 | 1.088 | -3.820 |
| `process_availability_050` | 94.688 | 2.176 | -51.164 | 2.176 | -51.164 |
| `process_availability_075` | 142.031 | 3.263 | -98.508 | 3.263 | -98.508 |
| `harvest_recovery_035` | 19.732 | 0.453 | 23.792 | 0.453 | 23.792 |
| `harvest_recovery_060` | 33.826 | 0.777 | 9.698 | 0.777 | 9.698 |
| `harvest_recovery_075` | 42.283 | 0.971 | 1.241 | 0.971 | 1.241 |

## Caveats

- Zone mapping is screening-only and code-defined; no published sub-provincial zone polygon is used.
- BC, AB, ON, and QC span multiple OSeCAN zones; they are not split because the crosswalk has no residue-split basis.
- The T1 and N1 zones are exact aggregates of their member provinces; their totals are not duplicated province rows.
- Process residue is facility-province based; harvest residue is origin-province based. They are separate and not summed.
- Process rows use the `TOTAL` class row only; harvest rows use the `ALL` row only. Class detail is not double counted.
- SUPBCW technology strings are candidate mappings, not operating assignments or official OSeCAN technology choices.
- The 2050 OSeCAN national (152.923 PJ) and BC (43.524 PJ) values are model context, not policy targets.
- The 213.54 PJ national supply-curve top is an adopted model bound, not a policy target.
- No transport, cost, revenue, capacity-expansion, tenure, AAC, or policy claim is made.
- No UI or public OSeCAN surface is changed.

## Validation and status

Build status: `pass`. Validation checks: 15, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.forestry_osecan_handoff` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_forestry_osecan_handoff.py -q` to run the regression tests.

No policy/AAC claim is made.
