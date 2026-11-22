# National bucking pilot v1 schema

Every record is a pilot record.  `model_estimate=true`, `synthetic=true`,
`observed=false`, `policy_grade=false`, `national_claim=false`.

## Evidence tiers

`measured_taper`, `published_table`, `assumption`.  A row's `evidence` is the
weakest component tier.  `taper_status` separately says whether the published
taper is local (`local_published`) or a cross-jurisdiction donor
(`donor_published`).  `taper_proxy=true` means the species was mapped to a
published aggregate/proxy species in the donor table.

## Tables

| Table | Grain | Key fields |
|---|---|---|
| `tree_list.csv` | one representative tree | `tree_id`, `jurisdiction`, `species`, `dbh_cm`, `height_m`, `taper_id`, `taper_status`, `species_nfi`, `tree_list_basis` |
| `bucked_logs.csv` | one recovered log | `tree_id`, `log_index`, `length_m`, `large_end_dib_cm`, `small_end_dib_cm`, `volume_m3`, `net_volume_m3`, `product`, `grade`, `sort_basis`, `taper_evidence`, `taper_status` |
| `residue_ledger.csv` | one stem | `residue_volume_m3`, `residue_odt`, `green_tonnes`, `chip_green_tonnes`, `hog_green_tonnes`, `recovered_log_m3`, `taper_total_m3`, `balance_error_m3` |
| `reconciliation.csv` | one stem | total/recovered/residue/defect/net/log count/product volumes |
| `province_summary.csv` | one province | volume, residue, product shares, taper local/donor counts |
| `coefficient_comparison.csv` | one province | model ratios versus facility-chain coefficients |

`grade=not_assigned` and `grade_status=not_assigned` in every log row.  The sort
set is `dimension_only`; it is not an official federal or provincial grade.
