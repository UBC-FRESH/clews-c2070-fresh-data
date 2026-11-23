# OSeCAN Candidate Cases V1 (D1 x D2, 119 Mm3)

Status: **pass**. Artifact version `1.0.0`; generated 2026-11-23T07:36:12+00:00.

Read-only candidate package. Every row is `model_estimate=true`, `observed=false`, `policy_grade=false`, and `official_osecan_changed=false`. No official OSeCAN input is written or modified. Process and harvest residue are separate streams and are never summed.

## Scope and method

- Scenario: `119m` (119 Mm3 planning allocation).
- D1 harvest recovery: 0.35 / 0.60 / 0.75.
- D2 process-residue availability: 0 / 25 / 50 / 75%.
- Cases: 12 D1 x D2 combinations. Each case carries both streams separately.
- Candidate zone limits are the v7 119m zone candidate limits (handoff v8 weights) regrouped under each case id.
- Case candidate zone PJ sums are reconciled to `forestry_osecan_handoff_v8` at 119m.
- Official references are the adopted national supply-curve tiers (T1-T4), the 2050 OSeCAN national context, and the B1/B2 official 2050 activity limits.

## Case index

| Case | D1 recovery | D2 availability | Harvest PJ | Harvest tier | Process PJ | Process tier |
|---|---:|---:|---:|---|---:|---|
| `r035_a000` | 0.35 | 0.00 | 155.544 | T4 | 0.000 | T1 |
| `r035_a025` | 0.35 | 0.25 | 155.544 | T4 | 124.688 | T3 |
| `r035_a050` | 0.35 | 0.50 | 155.544 | T4 | 249.375 | above_T4 |
| `r035_a075` | 0.35 | 0.75 | 155.544 | T4 | 374.063 | above_T4 |
| `r060_a000` | 0.60 | 0.00 | 266.646 | above_T4 | 0.000 | T1 |
| `r060_a025` | 0.60 | 0.25 | 266.646 | above_T4 | 124.688 | T3 |
| `r060_a050` | 0.60 | 0.50 | 266.646 | above_T4 | 249.375 | above_T4 |
| `r060_a075` | 0.60 | 0.75 | 266.646 | above_T4 | 374.063 | above_T4 |
| `r075_a000` | 0.75 | 0.00 | 333.308 | above_T4 | 0.000 | T1 |
| `r075_a025` | 0.75 | 0.25 | 333.308 | above_T4 | 124.688 | T3 |
| `r075_a050` | 0.75 | 0.50 | 333.308 | above_T4 | 249.375 | above_T4 |
| `r075_a075` | 0.75 | 0.75 | 333.308 | above_T4 | 374.063 | above_T4 |

Harvest and process columns are separate; no total column is defined.

## Candidate activity-limit table

`candidate_activity_limits.csv` is the documented read-only format. Grain: `scenario`, `case_id`, `stream`, `zone_id`. It has 312 rows (12 cases x 2 streams x 13 zones). Required fields: `scenario`, `case_id`, `stream`, `zone_id`, `candidate_activity_limit_pj`, and `technology_suggestion`. `candidate_status` is always `read_only_candidate_not_applied`. `official_limit_pj`, `candidate_ratio_to_official_limit`, and `candidate_headroom_pj` are populated only for B1/B2; blank means no official zone-specific limit exists in the adopted curve.

Column dictionary:

| Column | Meaning |
|---|---|
| `scenario` | `119m` planning allocation; not an AAC. |
| `case_id` | D1 x D2 case, e.g. `r060_a025`. |
| `stream` | `process` or `harvest`; never combined. |
| `stream_case` | Seven-case key for that stream. |
| `stream_fraction` | D1 recovery or D2 availability fraction. |
| `zone_id` / `zone_name` | One of the 13 OSeCAN zones. |
| `candidate_activity_limit_odt` | Candidate zone residue, ODT. |
| `candidate_activity_limit_pj` | Candidate zone residue, PJ. |
| `technology_suggestion` | SUPBCW candidate string; not an assignment. |
| `official_limit_reference` | B1/B2 2050 limit reference or `none`. |
| `official_limit_pj` | Adopted B1/B2 2050 limit, PJ. |
| `candidate_ratio_to_official_limit` | Candidate PJ / official B1/B2 limit. |
| `candidate_headroom_pj` | Official B1/B2 limit - candidate PJ. |
| `candidate_status` | Always `read_only_candidate_not_applied`. |
| `model_estimate` / `observed` / `policy_grade` / `official_osecan_changed` | Fixed labels. |

## Comparison to official B1/B2 limits and national supply curve

Ratios above 1.0 mean the case exceeds the reference; negative headroom is the excess. References are context, not policy targets. The national supply curve is rest-of-Canada RSYC-only; comparisons that include BC are a context screen, not a capacity-adequacy or sustainability test.

| Case | Stream | PJ | Tier | T4 ratio | 2050 national ratio | B1 PJ | B1 ratio | B2 PJ | B2 ratio | BC zonal ratio |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| `r035_a000` | process | 0.000 | T1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `r035_a000` | harvest | 155.544 | T4 | 0.728 | 1.017 | 3.466 | 0.961 | 38.372 | 0.961 | 0.961 |
| `r035_a025` | process | 124.688 | T3 | 0.584 | 0.815 | 3.613 | 1.002 | 40.000 | 1.002 | 1.002 |
| `r035_a025` | harvest | 155.544 | T4 | 0.728 | 1.017 | 3.466 | 0.961 | 38.372 | 0.961 | 0.961 |
| `r035_a050` | process | 249.375 | above_T4 | 1.168 | 1.631 | 7.226 | 2.004 | 79.999 | 2.004 | 2.004 |
| `r035_a050` | harvest | 155.544 | T4 | 0.728 | 1.017 | 3.466 | 0.961 | 38.372 | 0.961 | 0.961 |
| `r035_a075` | process | 374.063 | above_T4 | 1.752 | 2.446 | 10.838 | 3.006 | 119.999 | 3.006 | 3.006 |
| `r035_a075` | harvest | 155.544 | T4 | 0.728 | 1.017 | 3.466 | 0.961 | 38.372 | 0.961 | 0.961 |
| `r060_a000` | process | 0.000 | T1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `r060_a000` | harvest | 266.646 | above_T4 | 1.249 | 1.744 | 5.941 | 1.648 | 65.780 | 1.648 | 1.648 |
| `r060_a025` | process | 124.688 | T3 | 0.584 | 0.815 | 3.613 | 1.002 | 40.000 | 1.002 | 1.002 |
| `r060_a025` | harvest | 266.646 | above_T4 | 1.249 | 1.744 | 5.941 | 1.648 | 65.780 | 1.648 | 1.648 |
| `r060_a050` | process | 249.375 | above_T4 | 1.168 | 1.631 | 7.226 | 2.004 | 79.999 | 2.004 | 2.004 |
| `r060_a050` | harvest | 266.646 | above_T4 | 1.249 | 1.744 | 5.941 | 1.648 | 65.780 | 1.648 | 1.648 |
| `r060_a075` | process | 374.063 | above_T4 | 1.752 | 2.446 | 10.838 | 3.006 | 119.999 | 3.006 | 3.006 |
| `r060_a075` | harvest | 266.646 | above_T4 | 1.249 | 1.744 | 5.941 | 1.648 | 65.780 | 1.648 | 1.648 |
| `r075_a000` | process | 0.000 | T1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `r075_a000` | harvest | 333.308 | above_T4 | 1.561 | 2.180 | 7.427 | 2.060 | 82.225 | 2.060 | 2.060 |
| `r075_a025` | process | 124.688 | T3 | 0.584 | 0.815 | 3.613 | 1.002 | 40.000 | 1.002 | 1.002 |
| `r075_a025` | harvest | 333.308 | above_T4 | 1.561 | 2.180 | 7.427 | 2.060 | 82.225 | 2.060 | 2.060 |
| `r075_a050` | process | 249.375 | above_T4 | 1.168 | 1.631 | 7.226 | 2.004 | 79.999 | 2.004 | 2.004 |
| `r075_a050` | harvest | 333.308 | above_T4 | 1.561 | 2.180 | 7.427 | 2.060 | 82.225 | 2.060 | 2.060 |
| `r075_a075` | process | 374.063 | above_T4 | 1.752 | 2.446 | 10.838 | 3.006 | 119.999 | 3.006 | 3.006 |
| `r075_a075` | harvest | 333.308 | above_T4 | 1.561 | 2.180 | 7.427 | 2.060 | 82.225 | 2.060 | 2.060 |

## Zone and technology mapping

| Zone | Zone name | Technology suggestion | Mapping kind |
|---|---|---|---|
| B1 | South Coast / Lower Mainland | `SUPBCWB1` | zone_specific_candidate |
| B2 | Interior & North | `SUPBCWB2` | zone_specific_candidate |
| A1 | Calgary–Edmonton corridor | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| A2 | North (oil sands) | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| S1 | Saskatchewan | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| M1 | Manitoba | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| O1 | Southern Ontario | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| O2 | Northern Ontario | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| Q1 | Southern Quebec | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| Q2 | Northern Quebec (hydro) | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| T1 | Atlantic | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| L1 | Newfoundland & Labrador | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |
| N1 | North (territories) | `SUPBCWT1|SUPBCWT2|SUPBCWT3|SUPBCWT4` | rest_of_canada_tier_pool_candidate |

## Conservation, coverage, and labels

- 12 cases, each with 2 streams x 13 zones = 312 candidate rows.
- Every case/stream zone PJ sum reconciles to the handoff v8 119m total within 1e-6 PJ.
- Every case/stream covers all 13 OSeCAN zones.
- The zero availability case is exactly zero for process; it is the zero anchor, not a physical process-residue estimate.
- `candidate_status` is `read_only_candidate_not_applied` on every candidate row.
- Official derived OSeCAN tree hash before/after: unchanged = True.
- Official SUPBCW schema files before/after: unchanged = True.

## Caveats

- All values are model estimates; observed=false and policy_grade=false.
- The 119 Mm3 case is a planning allocation, not a legal AAC, sustainable-supply determination, or observed harvest outcome.
- Zone splits are explicit forestry_osecan_handoff_v8 proxy weights; no observed sub-provincial residue split exists.
- Process residue is facility-assigned by receiving facility province; harvest residue is province-only gross residue multiplied by the recovery fraction.
- Process and harvest residue are separate streams and are never summed. No combined or total residue value is produced.
- Candidate activity limits are read-only screening values; they are not applied to any OSeCAN technology, region, or input file.
- Official zone-specific limits exist only for SUPBCWB1 and SUPBCWB2; other zones have no official zone-specific activity limit in the adopted curve.
- The national supply-curve tier caps are rest-of-Canada RSYC-only; national comparisons that include BC are a context screen, not a like-for-like capacity test.
- Supply-curve and 2050 OSeCAN values are context, not policy targets, and the comparison is not a capacity-adequacy or sustainability test.
- No UI or public OSeCAN surface is changed by this artifact.

## Validation and status

Validation: True; failed checks: 0. Build status: `pass`.

Reproduce:

```bash
.venv/bin/python -m workflows.national.facilities.osecan_candidate_cases_v1
.venv/bin/python -m pytest tests/test_osecan_candidate_cases_v1.py -q
```

No policy, AAC, tenure, or official OSeCAN claim is made.
