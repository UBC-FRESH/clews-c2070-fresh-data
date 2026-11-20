# Forest cost/revenue ledger coverage

**Status:** `screening_only` · `policy_grade=false` · **observed sample plus model-input deck; not a population**

**Generated:** 2026-11-20T16:42:00+00:00

**Ledger:** `data/derived/national/harvest_basis/forest_cost_revenue/forest_cost_revenue.csv` (940 rows; SHA-256 `11fc4b091f92…`)

## 1. Merge

The two blocks are concatenated, never re-keyed and never summed:

| Province | Source | Rows | SHA-256 |
|---|---|---:|---|
| BC | `data/derived/national/harvest_basis/bcts_bc/bcts_bid_ledger.csv` | 200 | `52e210ab9d7b…` |
| QC | `data/derived/national/harvest_basis/meris_qc_full/forest_cost_revenue_qc_model.csv` | 740 | `888a18128f04…` |

Merged rows: **940**. By province: BC 200, QC 740. By perspective: crown 100, forest_sector 840.

Evidence classes: **200 observed** rows and **740 model-input** rows. BC: observed 200, model input 0; QC: observed 0, model input 740. The classes are counted separately and never summed.

### Rows by province / source / perspective / component

| Province | Source | Perspective | Component | Evidence | Rows | Licences | Unit | Quantity weight | Confidence |
|---|---|---|---|---|---:|---:|---|---:|---|
| BC | `prov_bcts_auction_results` | crown | `stumpage_base` | observed | 49 | 49 | CAD_per_m3_log | 1,253,065.00 | medium |
| BC | `prov_bcts_auction_results` | crown | `stumpage_bid_premium` | observed | 51 | 51 | CAD_per_m3_log | 1,313,211.00 | medium |
| BC | `prov_bcts_auction_results` | forest_sector | `stumpage_base` | observed | 49 | 49 | CAD_per_m3_log | 1,253,065.00 | medium |
| BC | `prov_bcts_auction_results` | forest_sector | `stumpage_bid_premium` | observed | 51 | 51 | CAD_per_m3_log | 1,313,211.00 | medium |
| QC | `prov_qc_meris` | forest_sector | `delivered_log_revenue` | model_input | 127 | 127 | CAD_per_m3_log | 127.00 | low, medium |
| QC | `prov_qc_meris` | forest_sector | `harvest` | model_input | 191 | 191 | CAD_per_m3_log | 191.00 | low |
| QC | `prov_qc_meris` | forest_sector | `road` | model_input | 191 | 191 | CAD_per_m3_log | 191.00 | medium |
| QC | `prov_qc_meris` | forest_sector | `silviculture` | model_input | 40 | 40 | CAD_per_ha | 40.00 | medium |
| QC | `prov_qc_meris` | forest_sector | `overhead` | model_input | 191 | 191 | CAD_per_m3_log | 191.00 | medium |

Quantity weight is the sale volume for BCTS and a 1 m³ rate denominator for MERIS; it is not summed across components or sources.

## 2. Coverage against population denominators

**Not a population.** The ledger covers selected BCTS auctions and the full MERIS model-input deck. The shares below describe how much of each source frame is represented; they do **not** estimate provincial values or allow scaling to the provincial harvest. MERIS coverage is model-input coverage, not observed transactions.

| Measure | Numerator | Denominator | Share |
|---|---:|---:|---:|
| BCTS scheduled sample volume | 1,940,031 m³ | BC 2024 harvest 38,876,568 m³ | 4.99% |
| BCTS awarded ledger volume | 1,313,211 m³ | BC 2024 harvest 38,876,568 m³ | 3.38% |
| BCTS awarded volume | 1,313,211 m³ | BCTS scheduled sample 1,940,031 m³ | 67.69% |
| BCTS awarded TSLs | 51 | 99 scheduled TSLs | 51.52% |
| BCTS awarded blocks | 84 | 162 scheduled blocks | 51.85% |
| MERIS delivered-log model inputs | 127 model-input rows | 0 observed rows | **model input, not observed** |
| MERIS cost-deck tarification zones | 191 | 191 zones | 100.00% |
| MERIS usable silviculture treatments | 40 | 94 treatments | 42.55% |
| MERIS current Crown stumpage rate rows | 0 | 2,674 zone-species rows | **not in full model deck** |
| MERIS observed harvest volume | 0 | QC 2024 harvest 25,939,056 m³ | **not estimable** |

For context only: BC + QC are 54.48% of the 2024 national harvest denominator (118,977,339 m³). This is a denominator share, not ledger coverage, and BC + QC values are not combined.

### BCTS sample detail

- Schedule frame: 99 TSLs, 162 blocks, 1,940,031 m³.
- Awarded ledger: 51 TSLs, 84 blocks, 1,313,211 m³ unique sale weight.
- Upset base is present for 49 sales; the bonus premium is present for 51. Two lump-sum sales publish a bonus but no upset; no base was fabricated.

### QC MERIS full model-input deck detail

- 740 rows, all `model_input` and `forest_sector`; 191 cost-deck zones and 40 usable silviculture treatments. Cost components: harvest, overhead, road, silviculture.
- 127 `delivered_log_revenue` rows are mill-gate model inputs (0 observed). They are not mill settlements and are not monetised.
- `harvest` is loading-only (`partial=loading_only`), `road` excludes tertiary road, and `silviculture` is a CAD/ha treatment catalogue. The deck has no Crown perspective and no mirrors.
- MERIS has no observed permit-volume register: every row uses `volume_m3=1.0` as a rate denominator, so QC harvest-volume coverage is not estimable.

## 3. Net-value readiness

Net value is reported only in the `forest_sector` perspective and is `not_estimated` while any in-boundary component is missing or partial. `stumpage_total` is an alternative to `stumpage_base` plus `stumpage_bid_premium`, not an additional requirement.

| Component | BC BCTS | QC MERIS |
|---|---|---|
| `delivered_log_revenue` | **missing** | partial |
| `residue_revenue` | **missing** | **missing** |
| `stumpage_base` | partial | **missing** |
| `stumpage_bid_premium` | present | **missing** |
| `stumpage_total` | **missing** | **missing** |
| `harvest` | **missing** | partial |
| `road` | **missing** | partial |
| `haul` | **missing** | **missing** |
| `silviculture` | **missing** | partial |
| `residue_recovery` | **missing** | **missing** |
| `overhead` | **missing** | partial |
| `admin_fee` | **missing** | **missing** |
| `crown_other` | **missing** | **missing** |
| `crown_credit` | **missing** | **missing** |

**BC net value:** `not_estimated` — delivered log revenue and every production cost are absent; a standing bid is not a log price.

**QC net value:** `not_estimated` — the full MERIS deck is model input only: delivered log revenue is a mill-gate model price, harvest is loading-only, road excludes tertiary road, silviculture is CAD/ha without a yield conversion, and no observed volume or full cost exists.

Present/partial components:

- BC: `stumpage_base`, `stumpage_bid_premium`.
- QC: `delivered_log_revenue`, `harvest`, `road`, `silviculture`, `overhead`.

## 4. Validation

- `load_ledger` accepted all 940 rows after the merge.
- 100 mirror rows are paired exactly; all are Crown/forest-sector transfers.
- Duplicate keys, source-exclusivity conflicts, sign violations, currency/volume-basis mixing, and unpaired mirrors fail the merge.
- 127 `delivered_log_revenue` rows are model inputs; 0 are observed. No observed delivered-log revenue was invented.
- Model-input rows are counted and reported but excluded from every monetary total.

## 5. Caveats

- The ledger combines a BCTS auction sample with the full QC MERIS model-input deck; it is not a provincial or national population estimate.
- Observed rows and model-input rows are counted separately; model-input values are never monetised.
- BCTS and MERIS rows are never summed; each remains a separate source under its own province.
- Crown and forest-sector rows are never summed into a combined total; only the reconciliation identity may relate them.
- BCTS sells standing timber: its upset and bonus are stumpage, not delivered log revenue.
- MERIS is a tarification/cost parameter set, not an observed harvest or delivered-price register; its delivered-log values are mill-gate model inputs, not settlements.
- Missing components are missing, not zero; no value, volume, or component was imputed.

## 6. Reproduce

```bash
.venv/bin/python -m workflows.national.harvest.merge_cost_revenue
```
