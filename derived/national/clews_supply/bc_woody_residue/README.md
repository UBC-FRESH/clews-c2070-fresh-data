# BC woody-residue supply curve for OSeCAN B1/B2

FRESH-side provisional supply curve. Read `BC_CLEWS_SUPPLY_REPORT.md` first.

## Primary files

- `bc_zone_crosswalk.csv`: ecoprovince → B1/B2, with rationale.
- `bc_tsa_zone_crosswalk.csv`: TSA → dominant zone, THLB/forest shares, split
  flags, and 2018 AAC/apportionment volumes.
- `bc_annual_residue.csv`: flat 2021–2070 annual log volume, residue ODT, and
  residue PJ by zone (`B1`, `B2`, `CAN`).
- `SUPBCWB1_activity_limits.csv`: `TotalTechnologyAnnualActivityUpperLimit`
  rows for `SUPBCWB1` (B1), PJ/yr.
- `SUPBCWB2_activity_limits.csv`: `TotalTechnologyAnnualActivityUpperLimit`
  rows for `SUPBCWB2` (B2), PJ/yr.
- `SUPBCWB1_variable_cost.csv`: `VariableCost` rows for `SUPBCWB1` (B1), $/GJ.
- `SUPBCWB2_variable_cost.csv`: `VariableCost` rows for `SUPBCWB2` (B2), $/GJ.

All OSeCAN parameter files have the otoole columns
`REGION,TECHNOLOGY,YEAR,VALUE`, `REGION=CAN`, and 50 rows for 2021–2070.

## Audit files

- `audit/bc_tsa_volume_allocation.csv`: TSA → ecoprovince volume allocation.
- `audit/bc_apportionment_adjustments.csv`: the five TSAs missing from the
  generic parser, with their 2018 AAC and apportionment.
- `audit/bc_pg_adjustment.csv`: the Prince George correction only.
- `audit/bc_residue_ratio_comparison.csv`: batch all-species, batch
  ecoprovince, and Stage B mill-residue ratios.
- `audit/bc_residue_ratio_by_ecoprovince.csv`: the batch ratios used.
- `audit/bc_cost_derivation.csv`: Stage B transport + processing cost
  derivation by zone.

## Comparison files

Do not load the national rollup together with the zone rows.

- `comparison/SUPBCW_activity_limits.csv`: national sum (93.170084 PJ/yr).
- `comparison/SUPBCW_variable_cost.csv`: national PJ-cap-weighted cost
  (1.791835 $/GJ).
- `comparison/SUPBCW_placeholder_comparison.csv`: comparison with the current
  50 PJ/$4 placeholder.
- `comparison/bc_annual_residue_parsed_only.csv`: parsed 36-TSA AAC.
- `comparison/bc_annual_residue_apportionment_full.csv`: all-BC apportionment.
- `comparison/bc_annual_residue_apportionment_parsed.csv`: parsed 36-TSA
  apportionment.
- `comparison/bc_annual_residue_all_species_ratio.csv`: all-BC AAC with the
  single BC all-species ratio.

## Metadata

- `manifest.json`: input/output SHA256, key totals, assumptions, cost basis.
- `BC_CLEWS_SUPPLY_REPORT.md`: methods, caveats, and comparison to the
  placeholder.
