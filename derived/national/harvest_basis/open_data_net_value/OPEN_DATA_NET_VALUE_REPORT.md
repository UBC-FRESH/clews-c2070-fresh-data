# Open-data BC modeled margin

**Status:** `model_estimate` only. This is a **modeled margin**, not observed
profit, not a mill settlement, not an official net value, and not a legal, AAC,
tenure, or policy result. Generated from public data only.

## Headline

- Rows: **945** (7 forest zones x 5 slope-system scenarios [2 ground, 2 cable, 1 heli] x 3 piece sizes x 3 sale volumes x 3 haul distances).
- Zone-system groups: **21**.
- Median base `net_model`: **48.84 CAD/m3**.
- Base `net_model` range: **-23.38 to 86.85 CAD/m3**.
- Rows with a negative base `net_model`: **168 / 945**. Negative values are reported modeled losses, not errors or NaN.
- `road_silviculture_included=true` only on Interior-priced rows using the published Interior basic silviculture CAD/m3 allowance. Coast rows are `false` because CAM publishes Coast basic silviculture in CAD/ha only.
- No BC+QC combined national total exists in this artifact.

## Price/cost mapping

The primary price panel uses **one vintage only**: `3_month` reports ending
**2025-12-31**. The `1_month` vintage is kept separate as a
sensitivity and is never pooled with the primary panel.

| Region | Low | Base | High | Method | Vintage |
|---|---|---|---|---|---|
| Coast | 118.49 | 122.59 | 134.06 | published_report_average_volume_weighted_across_coast_log_classes | 3_month to 2025-12-31 |
| Interior | 59.19 | 113.38 | 130.08 | volume_weighted_product_cell_mean_and_p10_p90_excluding_aggregates | 3_month to 2025-12-31 |

Coast base is the volume-weighted average of the published old-growth and
second-growth report averages. Coast low/high are those two published class
averages. The two report classes come from the PDF report footers; `cells_used`
counts the 79 plausible underlying cells used for the outlier audit, not 79
independent panel observations. Interior base is the volume-weighted mean of
plausible product cells; low/high are the volume-weighted P10/P90 product
prices. Interior `is_aggregate=true` weighted-average rows are excluded from all
product sums. Flagged price cells are not used and are written separately to
`bc_open_price_outliers.csv`.

The cost layer is `open_proxy_model`: published 2026 BC machine rates divided by
public case-study productivity for logging, plus a published-appraisal/engineering
truck-cycle haul model. It is not an observed contractor cost. Haul and ground
extraction follow the cost model's `appraisal_region`: North West Zone is
appraisal-Interior and uses the IAM-derived Interior haul method and a grapple
skidder, even though its hourly rates come from the coastal/northwest rate group.

| Forest zone | CAD/m3 | Applied in model | Source |
|---|---|---|---|
| North Central Zone | 10.02 | Interior-priced rows | Interior Basic Silviculture 2026-10 |
| North East Zone | 10.61 | Interior-priced rows | Interior Basic Silviculture 2026-10 |
| North Fort Nelson Zone | 10.61 | Interior-priced rows | Interior Basic Silviculture 2026-10 |
| North West Zone | 5.84 | Interior-priced rows | Interior Basic Silviculture 2026-10 |
| South Central Zone | 8.40 | Interior-priced rows | Interior Basic Silviculture 2026-10 |
| South East Zone | 10.65 | Interior-priced rows | Interior Basic Silviculture 2026-10 |
| South West Zone | 11.23 | not applied (Coast-priced; CAM publishes CAD/ha only) | Interior Basic Silviculture 2026-10 |

Road construction, bridges, and culverts are **not** included: the public
allowances are CAD/km or CAD/each, and converting them to CAD/m3 without site
quantities would invent data. Road maintenance is also excluded because no
zone-to-road-group mapping exists. The included allowance is the published
Interior basic silviculture all-species average, CAD/m3, by forest zone,
effective 2026-10-01. It is applied **only** to
Interior-priced rows. The Interior table's `South West Zone` value is therefore
not applied to the Coast-priced South West Zone: CAM Table 5-6 publishes Coast
basic silviculture only in CAD/ha, and that value is not converted here.

## BC margin results by zone and system

Base `net_model` = price base - logging base - haul base - silviculture
allowance where an Interior CAD/m3 allowance exists; on Coast rows net_model
equals gross margin. The range columns are the min/max of the scenario rows in
each zone-system group (27 helicopter rows, 54 ground or cable rows). The
low/high envelope is conservative/optimistic:
low uses price low and cost high; high uses price high and cost low.

| Zone | System | Price region | Price base | Logging+haul base (median) | Silviculture | Net base median | Net base range | Negative rows |
|---|---|---|---|---|---|---|---|---|
| North Central Zone | cable | Interior | 113.38 | 57.78 | 10.02 | 45.58 | 26.88 to 63.82 | 0/54 |
| North Central Zone | ground | Interior | 113.38 | 46.43 | 10.02 | 56.93 | 37.51 to 75.89 | 0/54 |
| North Central Zone | heli | Interior | 113.38 | 113.96 | 10.02 | -10.60 | -22.75 to 1.17 | 26/27 |
| North East Zone | cable | Interior | 113.38 | 57.78 | 10.61 | 44.99 | 26.29 to 63.23 | 0/54 |
| North East Zone | ground | Interior | 113.38 | 46.43 | 10.61 | 56.34 | 36.92 to 75.30 | 0/54 |
| North East Zone | heli | Interior | 113.38 | 113.96 | 10.61 | -11.19 | -23.34 to 0.58 | 26/27 |
| North Fort Nelson Zone | cable | Interior | 113.38 | 57.78 | 10.61 | 44.99 | 26.29 to 63.23 | 0/54 |
| North Fort Nelson Zone | ground | Interior | 113.38 | 46.43 | 10.61 | 56.34 | 36.92 to 75.30 | 0/54 |
| North Fort Nelson Zone | heli | Interior | 113.38 | 113.96 | 10.61 | -11.19 | -23.34 to 0.58 | 26/27 |
| North West Zone | cable | Interior | 113.38 | 61.77 | 5.84 | 45.77 | 27.04 to 64.04 | 0/54 |
| North West Zone | ground | Interior | 113.38 | 49.78 | 5.84 | 57.76 | 38.32 to 76.74 | 0/54 |
| North West Zone | heli | Interior | 113.38 | 114.03 | 5.84 | -6.49 | -18.66 to 5.31 | 24/27 |
| South Central Zone | cable | Interior | 113.38 | 57.78 | 8.40 | 47.20 | 28.50 to 65.44 | 0/54 |
| South Central Zone | ground | Interior | 113.38 | 46.43 | 8.40 | 58.55 | 39.13 to 77.51 | 0/54 |
| South Central Zone | heli | Interior | 113.38 | 113.96 | 8.40 | -8.98 | -21.13 to 2.79 | 25/27 |
| South East Zone | cable | Interior | 113.38 | 57.78 | 10.65 | 44.95 | 26.25 to 63.19 | 0/54 |
| South East Zone | ground | Interior | 113.38 | 46.43 | 10.65 | 56.30 | 36.88 to 75.26 | 0/54 |
| South East Zone | heli | Interior | 113.38 | 113.96 | 10.65 | -11.23 | -23.38 to 0.54 | 26/27 |
| South West Zone | cable | Coast | 122.59 | 72.11 | excluded | 50.48 | 28.47 to 72.03 | 0/54 |
| South West Zone | ground | Coast | 122.59 | 58.19 | excluded | 64.40 | 41.86 to 86.85 | 0/54 |
| South West Zone | heli | Coast | 122.59 | 124.37 | excluded | -1.78 | -17.23 to 13.30 | 15/27 |

**Highest median base net_model (model estimates):**

| Zone | System | Net base median |
|---|---|---|
| South West Zone | ground | 64.40 |
| South Central Zone | ground | 58.55 |
| North West Zone | ground | 57.76 |
| North Central Zone | ground | 56.93 |
| North East Zone | ground | 56.34 |

**Lowest median base net_model (model estimates):**

| Zone | System | Net base median |
|---|---|---|
| South East Zone | heli | -11.23 |
| North East Zone | heli | -11.19 |
| North Fort Nelson Zone | heli | -11.19 |
| North Central Zone | heli | -10.60 |
| South Central Zone | heli | -8.98 |

## QC reference

The QC purchased-wood channel reference is **separate** and is not a net value,
not a mill margin, and not combined with BC.

| Item | Value |
|---|---:|
| Geography | QC |
| Year | 2022 |
| Purchase cost (CAD/m3) | 107.2200 |
| BGAD before transfers (CAD/m3) | 81.4000 |
| Transfers (CAD/m3) | 25.0100 |
| BGAD after transfers (CAD/m3) | 106.4100 |
| Cost spread before transfers (CAD/m3) | 25.8200 |
| Cost spread after transfers (CAD/m3) | **0.8100** |

The 0.81 CAD/m3 figure is the published SEPM purchased-versus-BGAD procurement
cost spread after transfers. It is a channel cost spread, not forest net value.
The upstream `survey_procurement_cost` evidence label is preserved.

## Sensitivity

| Case | Group | Median | Min | Max |
|---|---|---|---|---|
| base | base | 48.84 | -23.38 | 86.85 |
| price_low | price | -3.61 | -77.57 | 82.75 |
| price_high | price | 64.57 | -6.68 | 98.32 |
| cost_low | cost | 62.03 | -3.67 | 96.68 |
| cost_high | cost | 19.41 | -57.61 | 70.59 |
| gross_margin_road_silviculture_excluded | road_silviculture | 56.56 | -17.23 | 86.85 |
| net_model_road_silviculture_included | road_silviculture | 48.84 | -23.38 | 86.85 |
| envelope_low | combined | -32.31 | -111.80 | 66.49 |
| envelope_high | combined | 77.94 | 13.03 | 108.15 |
| price_1month_base | price_vintage | 45.55 | -26.35 | 82.28 |
| price_1month_low | price_vintage | -3.71 | -77.51 | 80.15 |
| price_1month_high | price_vintage | 61.93 | -16.03 | 93.00 |

Price low/high is the published price distribution within the single primary
vintage. Cost low/high is the open cost model's published-rate/productivity
range. The combined envelope combines the conservative price and cost ends
(low price minus high cost, high price minus low cost); it does not multiply
them. The 1-month price cases are a separate vintage and are not pooled with the
3-month primary panel. Road/silviculture excluded versus included is the
gross-margin versus net-model comparison; Coast rows have no CAD/m3
silviculture deduction in either case.

## Licensing

All inputs are **public-reference copyrighted sources**, not strict
OGL/CC-BY/Statistics Canada open-licence data. The BC appraisal manuals,
silviculture table, log-market reports, and CVSE material are BC Crown
copyright; the rate guide is TLA/ILA/NWLA/MNP copyright; FPInnovations/FERIC
case studies are publisher copyright; the QC survey is a Government of Québec
public-reference report. Source PDFs are not redistributed in this repository.
Commercial reuse or redistribution requires permission from the rights holder.

## Caveats and non-claims

- Published averages, not observed transactions. The price is a reported
  mill-delivered market average, not a transaction record or a mill settlement.
- Proxy productivity and proxy system assignment. The public cost model uses
  case-study productivity and maps seven forest zones to two rate groups, with
  an explicit appraisal region that selects haul and ground-extraction method.
- North West Zone is appraisal-Interior: it is priced Interior and uses the
  Interior haul method and a grapple skidder, while its hourly machine rates
  come from the coastal/northwest rate group. South West Zone is the only
  Coast-priced zone.
- Coast basic silviculture is not deducted: CAM Table 5-6 publishes CAD/ha by
  BEC unit, not a CAD/m3 allowance, and that value is not converted.
- Slope, piece-size and sale-volume adjustments are published IAM estimated-
  winning-bid coefficients used as **cost proxies**, not measured cost elasticities.
- Helicopter logging uses a published IAM specified-operation allowance as a
  total cost proxy.
- Logging and haul are model estimates, not observed contractor costs.
- The silviculture allowance is an appraisal/policy allowance, not an observed
  reforestation invoice. It is applied only to Interior-priced rows.
- Public-reference copyrighted sources, not strict open-licence data; source
  PDFs are not redistributed and commercial reuse needs rights-holder permission.
- Nominal CAD. Prices are nominal dollars of their report period; no deflator is applied.
- No grade, species, end-use, or mill-specific matching is possible. Prices are
  regional averages applied uniformly within a price region.
- No legal, AAC, tenure, stumpage, policy, or investment claim is made.
- No restricted ILCR/CCTMCS, FPInterface, mill-settlement, bidder-level, or
  confidential input was used.
- No combined BC+QC national total is produced.

## Validation

- Cost rows: 945 / 945.
- Net-value rows: 945.
- Ordered low <= base <= high on all cost, gross-margin, and net-model rows: True.
- No NaN or infinite values in numeric outputs: True.
- Primary price panels use one report basis and one period: True.
- Coast report totals are consistent and price basis/status are mill_delivered/reported: True.
- Interior aggregate rows excluded from product sums: True.
- `road_silviculture_included=true` on Interior rows only, `false` and blank allowance on Coast rows: True.
- All rows carry `evidence=model_estimate`, `observed=false`, `policy_grade=false`, `net_value_status=model_estimate`: True.
- Unexpected `D` (deleted paths) check is performed before commit; see the task report.
