# Quebec MRNF 2022 forest cost and revenue survey — observed aggregates

Stand-alone extraction of the public Quebec MRNF/BMMB 2022 survey of forest
procurement, transformation, and revenue. The dataset is a tidy, long-format
table of observed survey aggregates. It is **not** merged into the forest
cost/revenue ledger.

## Files

| File | Contents |
|---|---|
| `qc_cost_revenue_survey.csv` | 660 numeric observations, one per source table × column × row |
| `qc_cost_revenue_coverage.csv` | Every source table parsed or deliberately not parsed, with missing/suppressed counts |
| `manifest.json` | Source URLs, timestamps, SHA-256 hashes, coverage, validation, reconciliation, spot checks, limitations |
| `PROVENANCE.md` | Acquisition and transformation audit trail |
| `README.md` | This file |

## Schema

| Column | Meaning |
|---|---|
| `source_id` | `main_2022` or `regional_2022` |
| `source_table` | `T2`…`T22`, `A2`, or `REG` (mapped in `PROVENANCE.md`) |
| `source_page` | Printed page in the main report; PDF page 37 for A2; page 1 for REG |
| `survey_year` | `2022`; `2014`/`2019` only for Table A2 comparison rows |
| `reference_period` | Fiscal year definition |
| `region_code` | `QC` or one of seven published regional groups (`R01-R03-R11-R12`, `R09`, `R02`, `R04`, `R14-R15-R07-R08`, `R08`, `R10`) |
| `region_label` | Published regional coverage |
| `aggregation_level` | `provincial`, `regional`, or `provincial` total row in the regional table |
| `species_group` | `sepm`, `feuillus_durs`, `peupliers`, `pins`, `thuyas` |
| `species_label` | Human-readable species group |
| `product_or_grade` | `total`, `sciage`, `trituration`, `lumber`, `byproduct` |
| `component_group` | `purchase`, `harvest`, `road`, `haul`, `hosting`, `other_costs`, `transfers`, `market_reference`, `transformation`, `finished_goods_transport`, `overhead`, `revenue`, `byproduct`, `synthesis_procurement`, `synthesis_revenue`, `historical_comparison` |
| `component` | Canonical snake_case component |
| `subcomponent` | Transport mode, quarter, or drying species where applicable |
| `source_label_fr` | Original French row label |
| `value` | Reported numeric value; never imputed |
| `unit` | `CAD/m3`, `CAD/ha`, `CAD/MPMP`, `CAD/tma`, `CAD/tmv`, `m3/ha`, `m3/MPMP`, `percent`, `km` |
| `price_basis` | Cost or revenue basis (see below) |
| `sample_n` | Respondent count where the source reports one: regional table and Table A2 |
| `observation_type` | Always `survey_aggregate` |
| `observation_kind` | `component`, `synthesis`, `regional_survey_aggregate`, `historical_comparison`, `species_breakdown_non_additive` |
| `confidentiality_flag` | `none`, `three_respondents`, `suppressed_lt3`, `not_available`, `not_applicable` |
| `sign_convention` | `positive_cost`, `negative_credit_or_loss`, `signed_gain_loss`, `signed_net` |
| `notes` | Cell-level caveats, including red-flag and asterisk notes |

### Units and price bases

- `CAD/m3` — nominal 2022 Canadian dollars per cubic metre of merchantable wood,
  as defined by the survey.
- `CAD/MPMP` — dollars per thousand board feet (mille pieds mesure de planche).
- `CAD/tma` / `CAD/tmv` — dollars per oven-dry or green metric tonne, as
  published for by-products.
- `percent` — percentage points, not a fraction.
- `m3/ha` — mean merchantable volume harvested per hectare.
- `m3/MPMP` — board-foot-to-cubic-metre sawing recovery.
- `roadside` — harvest cost at roadside.
- `access_cost` / `access_cost_net` — forest road construction, maintenance, and
  amortization, before/after PRCCM compensation.
- `hauled_to_mill` — loading, transport, and unloading to mill.
- `delivered_to_mill` — total procurement before or after transfers to the State,
  depending on component.
- `per_m3_input_mill` — transformation or overhead per cubic metre entering the
  mill.
- `delivered_to_market` — finished-product transport.
- `gross_revenue` / `net_revenue` — before/after export taxes, commissions,
  discounts, and transport to market.
- `gross_byproduct_revenue` — by-product revenue per tonne or per cubic metre,
  as published.

## Coverage

- 23 source tables parsed: Tables 2–22 of the main report, Annex Table A2, and
  the 2022 regional compilation table.
- 660 numeric observations.
- 56 additive reconciliations pass. One known source inconsistency is recorded:
  Table 14's peupliers-sciage overhead components do not sum to its printed
  total; Annex A1 differs. The values are kept as printed and flagged in
  `manifest.json`.
- 8 direct spot checks against PDF values pass.
- 109 values are flagged `three_respondents` (red in the PDF).
- The 2019 regional compilation is not parsed because its tables are raster
  images. The 2019 report and the two 2021-22 silviculture reports were
  downloaded for provenance but are outside this dataset's scope.
- Annex Table A1 repeats Tables 2–22 and is not emitted separately; it is used
  only as a cross-check. The sampling profile, questionnaire, and Figure 3 are
  recorded in the coverage file with explicit not-parsed reasons.
- Compensation sub-lines in Table 10 are not a complete decomposition of the
  compensation total. Do not replace the total with the sum of the displayed
  sub-lines.

## How to regenerate

```bash
.venv/bin/python -m pip install pdfplumber
.venv/bin/python scripts/national/extract_qc_cost_survey_2022.py \
  --raw-dir tmp/qc_cost_survey/pdf
```

The extractor checks the SHA-256 of both parsed PDFs and refuses to write if a
file does not match. `--download` fetches missing PDFs from the public URLs.

## Merge recommendation

This dataset is evidence, not a drop-in ledger input. Recommended use by
component:

1. **Full harvest / road / haul cost stack:** use as a Quebec benchmark or
   calibration target for 2022. Do not merge row-for-row into
   `forest_cost_revenue.csv` without a deliberate crosswalk, because the survey
   values are provincial or regional means on a merchantable-volume basis and
   the ledger has different aggregation and provenance semantics. If a merge is
   later approved, merge the `T20`/`REG` synthesis rows, not the overlapping
   component tables.
2. **Delivered revenue:** use the SEPM and hardwood gross/net revenue series as
   an observed market benchmark. The net series is already net of export taxes,
   commissions, discounts, and transport to market; do not apply those
   deductions again.
3. **Silviculture:** do not merge the `Travaux sylvicoles` compensation line as a
   silviculture cost. It is a negative transfer to the State, not a treatment
   cost. The 2021-22 public/private silviculture surveys are a separate
   per-hectare / per-1000-plant dataset and should be extracted separately, then
   linked only through an explicit treatment-cost crosswalk.
4. **Transformation and by-products:** use as benchmarks only. Transformation
   costs are per cubic metre entering the sawmill and are not comparable to
   stump-to-mill procurement costs without a volume-basis conversion.

## Important limitations

- Survey aggregates only; no mill-level or respondent-level values.
- No value is allocated across species, grades, or regions beyond what the
  source published.
- Regional data cover SEPM only.
- Three-respondent means are statistically fragile and flagged.
- Dashes are confidentiality suppressions, not zeros.
- Table A2's 2014 and 2019 values are earlier surveys reproduced for comparison.
- Nominal CAD; no inflation adjustment.
- The source itself contains one internal inconsistency in Table 14; it is
  documented rather than silently corrected.
- This directory is intentionally not wired into the ledger, model, or UI.

## Citation

Groupe DDM, 2025. *Enquête quinquennale sur les coûts d'approvisionnement, de
transformation et les revenus de l'industrie forestière en 2022.* Report to the
Ministère des Ressources naturelles et des Forêts, 23 p. and appendices.
Internal reference 23-1734.

Bureau de mise en marché des bois, 2025. *Compilation des données régionalisées
du regroupement des essences résineuses sapin, épinettes, pin gris et mélèzes.*
November 2025.
