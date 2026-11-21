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
| `sign_convention` | `positive_cost`, `positive_revenue`, `physical_quantity`, `negative_credit_or_loss`, `signed_gain_loss`, `signed_net` |
| `notes` | Cell-level caveats, including red-flag and asterisk notes |

### Units and price bases

- `CAD/m3` — nominal Canadian dollars of the survey year (2022 for the main
  and regional tables; 2014, 2019, or 2022 for Table A2 rows), per cubic metre
  of merchantable wood as defined by the survey.
- `CAD/MPMP` — dollars per thousand board feet (mille pieds mesure de planche).
- `CAD/tma` / `CAD/tmv` — dollars per oven-dry or green metric tonne, as
  published for by-products.
- `percent` — percentage points, not a fraction.
- `m3/ha` — mean merchantable volume harvested per hectare.
- `m3/MPMP` — board-foot-to-cubic-metre sawing recovery.
- `roadside` — harvest cost at roadside.
- `access_cost` / `access_cost_net` / `access_cost_gross` — forest road
  construction, maintenance, and amortization, before or after PRCCM
  compensation. `access_cost_gross` is the before-PRCCM total used by T20 and
  REG; `access_cost_net` is the after-PRCCM total used by T5.
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

`sign_convention` describes how to read the number, not its sign: revenue rows
use `positive_revenue`, non-monetary physical rows (`m3/ha`, `m3/MPMP`,
`percent`, `km`) use `physical_quantity`, costs use `positive_cost`, and
credits, gain/loss, and net-transfer rows use their signed conventions. The
extractor fails if a physical or revenue row is labelled with any other
convention.

## Coverage

- 23 source tables parsed: Tables 2–22 of the main report, Annex Table A2, and
  the 2022 regional compilation table.
- 660 numeric observations.
- 56 additive reconciliations pass. Table 19 by-product totals are not
  reconciled over a partial component set because at least one component is
  suppressed; those two checks are recorded explicitly as
  `skipped_suppressed_component`. One known source inconsistency is recorded:
  Table 14's peupliers-sciage overhead components do not sum to its printed
  total; Annex A1 differs. The values are kept as printed and flagged in
  `manifest.json`.
- 8 direct spot checks against PDF values pass.
- 128 values are flagged `three_respondents`: red PDF cells, every regional
  R09 row (`sample_n=3`), and the T20 peupliers-trituration rows whose source
  basis is red-flagged in T3/T5/T10/T21 even though T20 prints them in black.
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

## Accounting caveats for net-value use

These caveats are mandatory for any comparison with delivered log value or a
forest-sector net-value calculation.

1. **`T2` / `T21` `Achats de bois (livré)` is a procurement cost, not log-sale
   revenue.** The SEPM value `107.22 CAD/m3` is what buying mills paid for
   public-forest wood. It includes the wood purchase, transfers to the State,
   transport and unloading, and road costs where applicable. It is not an
   observed stumpage price, log-sale revenue, or forest-sector gross value.
   `T21` repeats the `T2` purchase values as a synthesis row; do not add them
   together.
2. **`T20` `106.41` is the parallel BGAD supply channel.** `T20` builds up
   harvest, road, haul, hosting, other costs, and transfers for mills supplied
   through BGAD. `107.22 - 106.41 = 0.81 CAD/m3` is a procurement-channel cost
   spread between different respondent samples (for poplar trituration, BGAD is
   a 3-respondent subset), not forest-sector net value. The same caution applies
   to hardwood sawlog (`85.42 - 99.95 = -14.53`) and poplar trituration
   (`65.01 - 74.46 = -9.45`).
3. **PRCCM rebates sit inside `T10`/`T20` `transfers_total`.** The SEPM
   `T10.compensations` (`-1.94`) contains the T5 PRCCM rebates
   (`-0.69 - 0.33 - 0.04 = -1.06`). `T20.procurement_total_before_transfers`
   (`81.40`) uses gross road cost (`16.58`), while `T20.transfers_total`
   (`25.01`) is net of PRCCM. Do **not** combine `T5.road_total_after_prccm`
   (`15.52`, already net) with `T10.transfers_total` (`25.01`); that double
   counts the `-1.06` rebate. `T20`/`REG` road is `access_cost_gross`.
4. **`T20` excludes species gain/loss.** The excluded SEPM item is `-2.75
   CAD/m3`; hardwood sawlog is `-1.85` and poplar trituration is `-6.80`.
   Those items are carried in `T3` and in the `T22` revenue synthesis. Any
   delivered-value versus `T20`-cost comparison must state the exclusion; the
   SEPM item is larger than the entire `0.81 CAD/m3` purchased-versus-BGAD
   spread.

## Merge recommendation

This dataset is evidence, not a drop-in ledger input. Recommended use by
component:

1. **Full harvest / road / haul cost stack:** use as a Quebec benchmark or
   calibration target for 2022. Do not merge row-for-row into
   `forest_cost_revenue.csv` without a deliberate crosswalk, because the survey
   values are provincial or regional means on a merchantable-volume basis and
   the ledger has different aggregation and provenance semantics. If a merge is
   later approved, merge the `T20`/`REG` synthesis rows, not the overlapping
   component tables, and carry the accounting caveats above with them.
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
- `T2`/`T21` purchase values are procurement costs, not log-sale revenue;
  `T2 - T20` is a procurement-channel cost spread, not forest-sector net value.
- PRCCM rebates are inside `T10`/`T20` transfers; do not combine the after-PRCCM
  road total with transfers.
- `T20` excludes species gain/loss; flag this in every comparison.
- Three-respondent means are statistically fragile and flagged, including all
  R09 rows and the inherited T20 peupliers-trituration basis.
- Dashes are confidentiality suppressions, not zeros.
- Table A2's 2014 and 2019 values are earlier surveys reproduced for comparison.
- Nominal CAD of the survey year; no inflation adjustment.
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
