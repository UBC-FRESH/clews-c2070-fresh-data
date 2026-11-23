# National bucking pilot v2 schema

Every record is a pilot record.  BC tree geometry is measured FAIB PSP data;
the other 12 jurisdictions keep the v1 representative synthetic geometry.

## Labels

| Column | BC | Other 12 |
|---|---|---|
| `tree_list_label` | `measured_tree_list` | `representative_synthetic` |
| `measured_tree_list` | `true` | `false` |
| `synthetic` | `false` | `true` |
| `model_estimate` (tree rows) | `false` | `true` |
| `model_estimate` (log/residue/summary rows) | `true` | `true` |
| `observed` | `false` | `false` |
| `policy_grade` | `false` | `false` |
| `national_claim` | `false` | `false` |

BC bucked logs and residue are model estimates because taper and sort rules are
published models applied to measured stems.  They are not observed mill
receipts.  `grade=not_assigned`, `sort_basis=dimension_only`.

## Residue components

`residue_odt` is the stem taper residue only.  For BC measured stems,
`stem_residue_odt`, `branch_odt`, `foliage_odt`,
`branch_foliage_odt`, `total_residue_odt`, `recovery_factor` and
`recoverable_residue_odt` are populated from the CFS branch/foliage allometry.
The identities are:

```
branch_foliage_odt = branch_odt + foliage_odt
total_residue_odt = stem_residue_odt + branch_foliage_odt
recoverable_residue_odt = total_residue_odt * recovery_factor
```

`recovery_factor` is the existing pilot default 0.60.  Gross and recoverable
values are both reported; the factor is not calibrated to the facility
coefficient.  Non-BC synthetic rows set `branch_foliage_estimated=false` and
leave the optional branch/foliage/total values empty: an unestimated component
is never presented as zero biomass.

Branch and foliage coefficients come from the CFS Biomass and Nutrients
Calculator tree-level DBH + height table (Open Government Licence - Canada),
which implements Lambert et al. (2005) and Ung et al. (2008).  The exact source
CSV and its checksum are in `workflows/national/bucking/rules/cfs_biomass/`.
The equations are applied only to live measured stems within the documented
DBH/height application guardrails.

## Tables

| Table | Grain | Content |
|---|---|---|
| `tree_list.csv` | one selected stem | Combined 13-jurisdiction list |
| `tree_lists/BC.csv` | one measured aggregate stem | BC empirical list |
| `bc_tree_list_selection.csv` | one retained stem | Stratum, source PHF, pooled PHF |
| `bucked_logs.csv` | one recovered log | National-sort v2 pilot |
| `residue_ledger.csv` | one stem | National-sort v2 pilot |
| `reconciliation.csv` | one stem | National-sort v2 volume audit |
| `bc_tipsy_logs.csv` | one recovered log | BC interior TIPSY sort rerun |
| `bc_tipsy_residue.csv` | one stem | BC TIPSY residue |
| `bc_tipsy_reconciliation.csv` | one stem | BC TIPSY volume audit |
| `bc_tipsy_sort_rules.yaml`, `.csv` | one sort rule | Exact BC TIPSY rule file used |
| `province_summary.csv` | one province | Unweighted and expansion-weighted metrics |
| `coefficient_comparison.csv` | one province | Model versus facility coefficients |
| `bc_facility_comparison.csv` | one BC variant | v1, v2 TIPSY, v2 national, facility reference |
| `bc_residue_allometry.csv` | one BC stem and sort rule set | Stem, branch, foliage, gross and recoverable residue |
| `bc_residue_allometry_summary.csv` | one residue variant | Gross/recoverable comparison against facility and prior stem-only |
| `v1_v2_comparison.csv` | one province plus national rows | v1 to v2 deltas |
| `bc_population_reconciliation.csv` | one metric | v2 list versus full v0 population |
| `summary.json` | artifact | Machine-readable totals, labels, checks |
| `report.md` | artifact | Human-readable report |
| `manifest.json` | artifact | Inputs, outputs, hashes, checks |

## Expansion factors

- BC: `expansion_factor` is the pooled `PHF_TREE` total of the
  species x BEC zone x 2.5 cm DBH stratum.  `source_expansion_factor` is the
  retained stem's original FAIB value.  The BC list preserves the source PHF
  total exactly.
- Other provinces: `expansion_factor=1.0`; the v1 tree is a unit-weight
  representative draw, not an inventory expansion.

Absolute volumes are therefore not comparable between BC and the other
provinces.  Shares and per-tree metrics are the comparison basis; national rows
are explicitly macro or mixed-basis, never a national supply estimate.
