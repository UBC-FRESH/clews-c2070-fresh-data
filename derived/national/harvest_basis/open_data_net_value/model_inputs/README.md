# Open-data BC net-value model inputs

This directory is the self-contained, derived model-input bundle for the
corrected BC open-data modeled-margin layer (`open_data_net_value`, model
version `1.1.0`). It publishes **code plus the exact derived input
rows** consumed by the model. Raw copyrighted reports are cited in
`sources.csv` by URL, hash and retrieval date; **no raw PDF is redistributed**.

## Headline reproduced from this bundle

- Median base `net_model`: **48.84 CAD/m3**
- Base `net_model` range: **-23.38 to 86.85 CAD/m3**
- Negative base rows: **168 / 945**
- South West Zone ground median: **64.40 CAD/m3**
- North West Zone ground median: **57.76 CAD/m3**
- QC SEPM after-transfer cost spread: **0.81 CAD/m3** (separate reference, not a net value)

## Files

| File | Rows | Purpose |
|---|---:|---|
| `bc_price_panel_used.csv` | 190 | Exact primary 3-month and sensitivity 1-month 2025-12 price rows; excluded Interior aggregates flagged. |
| `bc_cost_inputs_used.csv` | 945 | Full 945-row logging/haul cost grid with formula, parameter and source IDs. |
| `bc_cost_parameters_used.csv` | 36 | Parameter register subset referenced by the cost grid. |
| `silviculture_inputs_used.csv` | 22 | Seven Interior basic silviculture rows plus explicit Coast CAM CAD/ha exclusions. |
| `qc_reference_used.csv` | 1 | Exact QC 2022 SEPM procurement cost-spread row. |
| `zone_region_mapping.csv` | 7 | Zone to rate group, appraisal region, price region and silviculture rule. |
| `sources.csv` | 18 | Raw-source citations, URLs, SHA-256, retrieval dates and licence terms. |
| `input_manifest.json` | n/a | SHA-256 and row counts for every bundle file, headline outputs and provenance. |
| `README.md` | n/a | This file. |
| `RUN.md` | n/a | Exact reproduction commands. |

## Raw sources cited but not redistributed

No raw report is present in this bundle. `sources.csv` cites each one with URL,
retrieval date and SHA-256:

- BC Interior and Coast appraisal manuals, and the Interior basic silviculture
  costs table (BC Crown copyright);
- BC Coast and Interior log-market reports (BC Crown copyright);
- TLA/ILA/NWLA/MNP 2026 timber-harvest cost-model rate guide (publisher
  copyright);
- FPInnovations/FERIC case studies and the 9-axle B-train report (publisher
  copyright);
- BC CVSE approved logging-truck configurations (BC Crown copyright);
- Quebec MRNF 2022 forest-industry survey report (Quebec government copyright).

Commercial reuse or redistribution of those raw reports requires permission
from the rights holder. The published derived tables are sufficient to
reproduce the headline.

## Labels

- `input_publication=derived_model_inputs`
- `raw_source_redistribution=false`
- `evidence=model_estimate`
- `observed=false`
- `policy_grade=false`
- `net_value_status=model_estimate`

This bundle is not an observed transaction, a mill profit, an official net
value, or a legal/AAC/policy statement. No model result, UI, or public OSeCAN
artifact is changed by publishing it.
