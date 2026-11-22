# National bucking pilot schema v0

This file documents the Phase 0/2 records emitted by
`workflows/national/bucking/national_bucking_pilot.py`.  The records are a
pilot contract; field names follow the national architecture note
(`planning/national-bucking-supply-architecture.md`) and are not a claim that
the schema is final.

## Evidence tiers

Every row carries an `evidence` value.  The allowed values, strongest first,
are `measured_taper`, `published_table` and `assumption`.  A row's `evidence`
is the weakest tier among its components; component tiers are retained in
separate columns so a consumer can see what is measured and what is assumed.

| Tier | Meaning in this pilot |
|---|---|
| `measured_taper` | Coefficients or measurements tied to the individual stem. Not used in this pilot. |
| `published_table` | A published equation or coefficient table applied to the tree list. Used for the Schneider (2013) taper. |
| `assumption` | A clearly labelled planning value: synthetic tree geometry, dimension sorts, prices, density, moisture, chip and hog yield. |

## `tree_list.csv`

| Field | Type | Notes |
|---|---|---|
| `tree_id` | text | Stable tree identifier. |
| `site_id` | text | Pilot site identifier. |
| `jurisdiction` | text | `QC` for this pilot. |
| `species` | text | Quebec species code used by the taper registry. |
| `species_group` | text | `conifer` or `deciduous`. |
| `dbh_cm` | float | DBH outside bark, cm. Synthetic in v0. |
| `height_m` | float | Total height, m. Synthetic in v0. |
| `defect_pct` | float | Defect deduction applied to log net volume, percent of gross. |
| `expansion_factor` | float | Trees per hectare; 1.0 for the unweighted pilot grid. |
| `status` | text | `live` or `dead`; only live trees are bucked. |
| `provenance` | text | Source statement. Synthetic in v0. |
| `evidence` | text | Evidence tier for the tree geometry. |
| `taper_id` | text | Registry key resolved for the tree. |

## `bucked_logs.csv`

| Field | Type | Notes |
|---|---|---|
| `tree_id` | text | Tree identifier. |
| `jurisdiction` | text | `QC`. |
| `log_index` | integer | 1-based, from stump upward. |
| `length_m` | float | Log length. |
| `large_end_dib_cm` | float | Inside-bark diameter at the lower end. |
| `small_end_dib_cm` | float | Inside-bark diameter at the upper end. |
| `volume_m3` | float | Gross inside-bark log volume. |
| `net_volume_m3` | float | Gross volume after the tree defect deduction. |
| `defect_deduction_m3` | float | `volume_m3 - net_volume_m3`. |
| `sort_code` | text | Pilot dimension sort code. |
| `product` | text | `sawlog`, `peeler`, `pulpwood` or `other`. |
| `grade` | text | `not_assigned` in v0: no official grade evidence. |
| `grade_status` | text | `not_assigned`. |
| `sort_basis` | text | `dimension_only`. |
| `price_cad_m3` | float | Pilot price, CAD per net m3. |
| `value_cad` | float | `net_volume_m3 * price_cad_m3`. |
| `evidence` | text | Weakest component tier. |
| `taper_evidence` | text | Tier of the taper geometry. |
| `sort_evidence` | text | Tier of the sort rule. |
| `value_evidence` | text | Tier of the price deck. |
| `tree_evidence` | text | Tier of the tree geometry. |
| `taper_id` | text | Registry key. |
| `taper_source` | text | Published taper citation. |
| `grade_rule_id` | text | Rule-set row that selected the sort. |
| `price_deck_id` | text | Versioned pilot deck identifier. |
| `provenance` | text | Tree provenance carried forward. |

## `residue_ledger.csv`

| Field | Type | Notes |
|---|---|---|
| `tree_id` | text | Tree identifier. |
| `jurisdiction` | text | `QC`. |
| `species` | text | Species code. |
| `residue_volume_m3` | float | Taper total minus recovered gross logs. |
| `basic_density_odt_m3` | float | Oven-dry tonnes per m3, pilot assumption. |
| `residue_odt` | float | `residue_volume_m3 * basic_density_odt_m3`. |
| `moisture_wet_basis` | float | Wet-basis moisture, pilot assumption. |
| `green_tonnes` | float | `residue_odt / (1 - moisture)`. |
| `chip_yield_fraction` | float | Green chip fraction, pilot assumption. |
| `chip_green_tonnes` | float | `green_tonnes * chip_yield_fraction`. |
| `hog_yield_fraction` | float | Green hog fraction, pilot assumption. |
| `hog_green_tonnes` | float | `green_tonnes * hog_yield_fraction`. |
| `recovered_log_m3` | float | Recovered gross log volume. |
| `taper_total_m3` | float | Taper total from stump height 0.3 m to tip. |
| `balance_error_m3` | float | `abs(recovered + residue - taper total)`. |
| `evidence` | text | Weakest component tier. |
| `taper_evidence` | text | Tier of the taper geometry. |
| `density_evidence` | text | Tier of the density assumption. |
| `moisture_evidence` | text | Tier of the moisture assumption. |
| `chip_evidence` | text | Tier of the chip/hog assumptions. |
| `provenance` | text | Tree provenance carried forward. |
| `notes` | text | Balance and assumption statement. |

## `reconciliation.csv`

One row per tree: taper total, recovered gross, residue, defect, net recovered,
log count, product volumes, value, the balance error, and the row evidence tier.
Pilot totals are in
`reconciliation_summary.json` and `manifest.json`; the CSV has no aggregate
row, so every numeric field is a real tree value.

## Taper registry and grade rules

`taper_registry.csv` is the registry actually used.  `grade_rules.csv` is the
pilot dimension rule set actually used.  Both are versioned data products, not
code branches.
