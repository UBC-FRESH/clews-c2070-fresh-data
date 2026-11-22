# Quebec pilot grade-rule rerun

**Pilot / assumption. Not an official Quebec grade, MERIS classification
or operational supply estimate.**

The rerun uses the ten committed v1 Quebec representative trees, the
published Schneider (2013) taper and two sort sets on identical geometry.
The dimension-only comparator is `qc_pilot_sorts.csv`; the earlier v1
13-jurisdiction run used `national_pilot_sorts.csv` and is not the
comparator here.

## Grade rule set

`qc_pilot_grade_sorts.csv` contains 44 rules.  The quality
class is a pilot mapping from top DIB, target length and tree defect
percentage.  Dimensions are `published_table`; mapping and prices are
`assumption`.

| Quality | Product | Grade label | Top min (cm) | Defect max (%) |
|---|---|---|---:|---:|
| DER | peeler | pilot_DER | 24.0 | 5.0 |
| F1 | sawlog | pilot_F1 | 20.0 | 7.5 |
| F2 | sawlog | pilot_F2 | 16.0 | 10.0 |
| F3 | sawlog | pilot_F3 | 12.5 | 100.0 |
| F4 | sawlog | pilot_F4 | 10.0 | 100.0 |
| PATE | pulpwood | pilot_PATE | 8.0 | 100.0 |
| AUTRE | other | pilot_AUTRE | 8.0 | 100.0 |

## QC grade results

| Metric | Dimension-only | Grade rules | Delta |
|---|---:|---:|---:|
| n_logs | 11 | 18 | +7 |
| n_trees_with_logs | 5 | 7 | +2 |
| taper_total_m3 | 1.14936 | 1.14936 | +0 |
| recovered_gross_m3 | 0.872793 | 1.00182 | +0.12903 |
| recovered_net_m3 | 0.823762 | 0.94491 | +0.121148 |
| defect_m3 | 0.049031 | 0.0569126 | +0.00788162 |
| residue_m3 | 0.276564 | 0.147534 | -0.12903 |
| residue_odt | 0.110199 | 0.0597244 | -0.0504742 |
| value_cad | 55.9043 | 134.242 | +78.3376 |
| sawlog_m3 | 0.593838 | 0.896659 | +0.302821 |
| peeler_m3 | 0 | 0 | +0 |
| pulpwood_m3 | 0.278955 | 0.0913483 | -0.187606 |
| other_m3 | 0 | 0.013815 | +0.013815 |
| sawlog_plus_peeler_m3 | 0.593838 | 0.896659 | +0.302821 |
| sawlog_plus_peeler_share | 0.680388 | 0.895028 | +0.21464 |
| sawlog_share | 0.680388 | 0.895028 | +0.21464 |
| pulpwood_share | 0.319612 | 0.0911822 | -0.228429 |
| other_share | 0 | 0.0137898 | +0.0137898 |
| residue_m3_per_recovered_m3 | 0.316873 | 0.147266 | -0.169607 |
| residue_odt_per_recovered_m3 | 0.12626 | 0.0596158 | -0.0666441 |
| balance_error_m3 | 0 | 0 | +0 |
| net_defect_error_m3 | 0 | 0 | +0 |

Log-level results are in `bucked_logs.csv`; grade distribution in
`grade_distribution.csv`; residue in `residue_ledger.csv` and
`volume_reconciliation.csv`.

## Dimension-only vs grade

- Sawlog + peeler share: 0.680 vs 0.895.
- Pulpwood share: 0.320 vs 0.091.
- Residue: 0.276564 m3 vs 0.147534 m3.
- Value: 55.904 CAD vs 134.242 CAD.

Both scenarios satisfy taper total = recovered gross + residue and
recovered gross = recovered net + defect, per tree and in total.

## Evidence and caveats

- Taper geometry: `published_table` (Schneider 2013).
- Rule dimensions: `published_table` from MERIS/Petro product references.
- Quality mapping, tree geometry, prices, density, moisture and chip/hog
  yields: `assumption`.
- In this bucking contract AUTRE is carried as product `other`; it is not
  the MERIS mixed-log product class.
- Ten representative trees, not inventory; no official grade claim.
- No UI or public OSeCAN surface was changed.

## Checks

- `ten_qc_trees`: PASS — 10 QC trees loaded from the v1 tree list
- `same_geometry`: PASS — both scenarios use the same taper total for every tree
- `volume_balance`: PASS — dimension_only=0; grade_rules=0
- `grade_mapping`: PASS — 44 grade rules map quality to product
- `dimension_not_assigned`: PASS — dimension-only logs have no grade or quality class
- `grade_rows_labelled`: PASS — all grade-rule logs carry a pilot grade and quality class
- `pilot_labels`: PASS — model_estimate/synthetic/observed=false/policy_grade=false/national_claim=false
- `no_nan`: PASS — numeric columns contain no NaN
- `no_negative`: PASS — volumes, residues and values are non-negative
- `evidence_tiers`: PASS — taper published_table; dimensions published_table; mapping/prices assumption
- `repository_hygiene`: PASS — no unexpected D in parent or data git status before run
