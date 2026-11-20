# Forest cost/revenue ledger coverage

**Status:** `screening_only` · `policy_grade=false` · **sample, not a population**

**Generated:** 2026-11-20T16:12:34+00:00

**Ledger:** `data/derived/national/harvest_basis/forest_cost_revenue/forest_cost_revenue.csv` (217 rows; SHA-256 `5b06836bfa6a…`)

## 1. Merge

The two blocks are concatenated, never re-keyed and never summed:

| Province | Source | Rows | SHA-256 |
|---|---|---:|---|
| BC | `data/derived/national/harvest_basis/bcts_bc/bcts_bid_ledger.csv` | 200 | `52e210ab9d7b…` |
| QC | `data/derived/national/harvest_basis/meris_qc_sample/forest_cost_revenue_sample.csv` | 17 | `9ba0a165c0b8…` |

Merged rows: **217**. By province: BC 200, QC 17. By perspective: crown 106, forest_sector 111.

### Rows by province / source / perspective / component

| Province | Source | Perspective | Component | Rows | Licences | Unit | Quantity weight | Confidence |
|---|---|---|---|---:|---:|---|---:|---|
| BC | `prov_bcts_auction_results` | crown | `stumpage_base` | 49 | 49 | CAD_per_m3_log | 1,253,065.00 | medium |
| BC | `prov_bcts_auction_results` | crown | `stumpage_bid_premium` | 51 | 51 | CAD_per_m3_log | 1,313,211.00 | medium |
| BC | `prov_bcts_auction_results` | forest_sector | `stumpage_base` | 49 | 49 | CAD_per_m3_log | 1,253,065.00 | medium |
| BC | `prov_bcts_auction_results` | forest_sector | `stumpage_bid_premium` | 51 | 51 | CAD_per_m3_log | 1,313,211.00 | medium |
| QC | `prov_qc_meris` | crown | `stumpage_base` | 6 | 1 | CAD_per_m3_log | 6.00 | low, medium |
| QC | `prov_qc_meris` | forest_sector | `stumpage_base` | 6 | 1 | CAD_per_m3_log | 6.00 | low, medium |
| QC | `prov_qc_meris` | forest_sector | `harvest` | 1 | 1 | CAD_per_m3_log | 1.00 | low |
| QC | `prov_qc_meris` | forest_sector | `road` | 1 | 1 | CAD_per_m3_log | 1.00 | medium |
| QC | `prov_qc_meris` | forest_sector | `haul` | 1 | 1 | CAD_per_m3_log | 1.00 | medium |
| QC | `prov_qc_meris` | forest_sector | `silviculture` | 1 | 1 | CAD_per_ha | 1.00 | medium |
| QC | `prov_qc_meris` | forest_sector | `overhead` | 1 | 1 | CAD_per_m3_log | 1.00 | medium |

Quantity weight is the sale volume for BCTS and a 1 m³ rate denominator for MERIS; it is not summed across components or sources.

## 2. Coverage against population denominators

**Not a population.** The ledger covers selected BCTS auctions and one MERIS tarification zone. The shares below describe how much of each source frame is represented; they do **not** estimate provincial values or allow scaling to the provincial harvest.

| Measure | Numerator | Denominator | Share |
|---|---:|---:|---:|
| BCTS scheduled sample volume | 1,940,031 m³ | BC 2024 harvest 38,876,568 m³ | 4.99% |
| BCTS awarded ledger volume | 1,313,211 m³ | BC 2024 harvest 38,876,568 m³ | 3.38% |
| BCTS awarded volume | 1,313,211 m³ | BCTS scheduled sample 1,940,031 m³ | 67.69% |
| BCTS awarded TSLs | 51 | 99 scheduled TSLs | 51.52% |
| BCTS awarded blocks | 84 | 162 scheduled blocks | 51.85% |
| MERIS current stumpage rate rows | 5 | 2,674 zone-species rows | 0.19% |
| MERIS tarification zones | 1 (zone 151) | 191 zones | 0.52% |
| MERIS silviculture treatments | 1 (BPR) | 94 treatments | 1.06% |
| MERIS observed harvest volume | 0 | QC 2024 harvest 25,939,056 m³ | **not estimable** |

For context only: BC + QC are 54.48% of the 2024 national harvest denominator (118,977,339 m³). This is a denominator share, not ledger coverage, and BC + QC values are not combined.

### BCTS sample detail

- Schedule frame: 99 TSLs, 162 blocks, 1,940,031 m³.
- Awarded ledger: 51 TSLs, 84 blocks, 1,313,211 m³ unique sale weight.
- Upset base is present for 49 sales; the bonus premium is present for 51. Two lump-sum sales publish a bonus but no upset; no base was fabricated.

### QC MERIS sample detail

- One tarification zone (151), 5 current zone-species stumpage rows, cost components harvest, haul, overhead, road, silviculture.
- `harvest` is loading-only (`not_for_net_value=1`), `road` excludes tertiary road, and `silviculture` is a CAD/ha treatment sample.
- MERIS has no observed permit-volume register: every row uses `volume_m3=1.0` as a rate denominator, so QC harvest-volume coverage is not estimable.

## 3. Net-value readiness

Net value is reported only in the `forest_sector` perspective and is `not_estimated` while any in-boundary component is missing or partial. `stumpage_total` is an alternative to `stumpage_base` plus `stumpage_bid_premium`, not an additional requirement.

| Component | BC BCTS | QC MERIS |
|---|---|---|
| `delivered_log_revenue` | **missing** | **missing** |
| `residue_revenue` | **missing** | **missing** |
| `stumpage_base` | partial | partial |
| `stumpage_bid_premium` | present | **missing** |
| `stumpage_total` | **missing** | **missing** |
| `harvest` | **missing** | partial |
| `road` | **missing** | partial |
| `haul` | **missing** | present |
| `silviculture` | **missing** | partial |
| `residue_recovery` | **missing** | **missing** |
| `overhead` | **missing** | present |
| `admin_fee` | **missing** | **missing** |
| `crown_other` | **missing** | **missing** |
| `crown_credit` | **missing** | **missing** |

**BC net value:** `not_estimated` — delivered log revenue and every production cost are absent; a standing bid is not a log price.

**QC net value:** `not_estimated` — delivered log revenue is absent, harvest is loading-only, and silviculture is CAD/ha without a yield conversion.

Present/partial components:

- BC: `stumpage_base`, `stumpage_bid_premium`.
- QC: `stumpage_base`, `harvest`, `road`, `haul`, `silviculture`, `overhead`.

## 4. Validation

- `load_ledger` accepted all 217 rows after the merge.
- 106 mirror rows are paired exactly; all are Crown/forest-sector transfers.
- Duplicate keys, source-exclusivity conflicts, sign violations, currency/volume-basis mixing, and unpaired mirrors fail the merge.
- No `delivered_log_revenue` row exists in either source; none was invented.

## 5. Caveats

- The merged file is a sample ledger, not a provincial or national population estimate.
- BCTS and MERIS rows are never summed; each remains a separate source under its own province.
- Crown and forest-sector rows are never summed into a combined total; only the reconciliation identity may relate them.
- BCTS sells standing timber: its upset and bonus are stumpage, not delivered log revenue.
- MERIS is a tarification/cost parameter set, not an observed harvest or delivered-price register.
- Missing components are missing, not zero; no value, volume, or component was imputed.

## 6. Reproduce

```bash
.venv/bin/python -m workflows.national.harvest.merge_cost_revenue
```
