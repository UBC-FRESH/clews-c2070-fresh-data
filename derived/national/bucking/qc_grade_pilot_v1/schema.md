# Quebec pilot grade-rule schema

Every row is a pilot/model row: `model_estimate=true`, `synthetic=true`,
`observed=false`, `policy_grade=false`, `national_claim=false`.

## Grade rule set

| Field | Meaning |
|---|---|
| `quality` | MERIS/Petro quality class (`DER`, `F1`-`F4`, `PATE`, `AUTRE`). |
| `grade` | Pilot label (`pilot_<quality>`), never an official grade. |
| `grade_status` | `pilot_assumption` for the grade scenario. |
| `sort_basis` | `grade_pilot_assumption` or `dimension_only`. |
| `min_top_cm` | Minimum inside-bark top diameter for the rule. |
| `target_length_m` | Candidate log length used by the bucker. |
| `max_defect_pct` | Maximum tree defect percentage eligible for the class. |
| `price_cad_m3` | Pilot price, CAD per net m3. |
| `price_deck_id` | `QC-MERIS-2025-C-PILOT`. |
| `price_reference` | Source row/statistic in the MERIS deck. |
| `dimension_evidence` | `published_table` for the MERIS/Petro dimensions. |
| `mapping_evidence` | `assumption` for the quality mapping. |
| `evidence` | Weakest of dimension and mapping evidence. |

## Outputs

| File | Grain |
|---|---|
| `tree_list.csv` | One row per input QC tree. |
| `bucked_logs.csv` | Scenario x recovered log. |
| `residue_ledger.csv` | Scenario x stem. |
| `reconciliation.csv` | Scenario x stem. |
| `grade_distribution.csv` | Scenario x grade x quality x product x sort. |
| `product_summary.csv` | Scenario x product. |
| `scenario_comparison.csv` | Metric x scenario. |
| `volume_reconciliation.csv` | Scenario totals. |
| `grade_rules.csv` | Grade rule set used. |
| `dimension_rules.csv` | Dimension-only comparator. |
| `summary.json` | Machine-readable totals, checks and limitations. |
| `manifest.json` | Input/output hashes and configuration. |
