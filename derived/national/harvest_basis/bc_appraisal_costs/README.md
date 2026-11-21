# BC public appraisal cost allowances

Standalone extraction of **published appraisal cost allowances** from the BC
Interior Appraisal Manual (IAM), Coast Appraisal Manual (CAM), and the quarterly
Interior Basic Silviculture Costs sheet. These are appraisal inputs, **not
observed contractor costs, winning bids, or transaction records**. This dataset
is not merged into `forest_cost_revenue.csv`, the national ledger, or any UI.

- **Observation type:** `appraisal_allowance`
- **Jurisdiction:** British Columbia
- **Regions:** `Interior` and `Coast`
- **Effective dates:** IAM 2026-07-01; CAM 2026-01-01; Interior basic
  silviculture 2026-10-01 and 2026-07-01
- **Units:** CAD/m³, CAD/km, CAD/ha, CAD/m, CAD/each, CAD/tree, and published
  add-on rates (CAD/km/%, CAD/ha/%, CAD/ha/stem, CAD/m³/km)
- **Rows:** 879 (599 Interior, 280 Coast)
- **Status:** 19 tables parsed, 3 partial, 2 not published, and 4 policy/rule
  entries recorded in coverage

## Files

| File | Rows | Purpose |
|---|---:|---|
| `bc_appraisal_costs.csv` | 879 | Tidy allowance cells/components |
| `bc_appraisal_coverage.csv` | 28 | Tables/sections parsed, partial, or not published |
| `manifest.json` | — | Source URLs, hashes, timestamps, row counts, policy rules, spot checks |
| `PROVENANCE.md` | — | Discovery, download, extraction, and audit trail |
| `README.md` | — | This file |

Source PDFs are not committed. `manifest.json` and `PROVENANCE.md` retain the
URL, retrieval timestamp, byte size, and SHA-256 of every PDF and discovery
page so the corpus can be re-fetched and verified.

## Schema: `bc_appraisal_costs.csv`

| Column | Meaning |
|---|---|
| `record_id` | Stable sequential key |
| `jurisdiction` | Always `BC` |
| `region` | `Interior` or `Coast` |
| `source_series` | `IAM 2026`, `CAM 2026`, or `Interior Basic Silviculture 2026-{10,07}` |
| `component_group` | `tree_to_truck`, `hauling`, `road_development`, `road_management`, `bridge`, `culvert`, `silviculture`, `tenure_obligation`, or `specified_operations` |
| `component` | Published cost component (for example `subgrade_construction_base`, `log_bridge`, `forest_management_administration_constant`) |
| `subcomponent` | Component variant (for example `superstructure`, `bec_unit`, `reservoir_marine`) |
| `species` | Species only where published; blank otherwise |
| `operability` | Operability/stand class only where published (`old_growth`, `second_growth`) |
| `zone_basis` | `appraisal_region`, `forest_zone`, `point_of_origin_area`, `forest_district`, `bec_unit`, `road_maintenance_group`, or blank |
| `zone` | Zone/region/unit code or name |
| `road_group` | IAM road group (1–12) where applicable |
| `effective_date` | Published effective date (ISO) |
| `year` | Effective year |
| `cost_basis` | `CAD/m3`, `CAD/km`, `CAD/ha`, `CAD/m`, `CAD/each`, `CAD/tree`, `CAD/m3/km`, `CAD/km/%`, `CAD/ha/%`, or `CAD/ha/stem` |
| `value` | Published value; never negative |
| `min_value`, `max_value` | Published floor/cap where one applies (for example FMA min/max, root disease control) |
| `matrix_row`, `matrix_column` | Row/column selectors for matrix tables (span, diameter, crib height, rock class, etc.) |
| `unit_note` | Short description of the unit or formula |
| `table_reference` | Manual table/section reference |
| `source_page` | PDF page number in the downloaded source |
| `source_document`, `source_url`, `source_sha256` | Source audit fields |
| `observation_type` | Always `appraisal_allowance` |
| `notes` | Eligibility, formula, or interpretation notes |

## Parsed components

### IAM 2026 (effective 2026-07-01)

- FMA regional constants and min/max for six appraisal regions (Table 4-1).
- Specified operations: surface tow dump/boom and tow rate, dewater/reload, log
  barge, truck-to-rail transfer, five railway origins (Table 3-5), barge used and
  not used for truck haul, skyline, helicopter, and horse logging (section 3.3).
- Road development: subgrade construction base, slope, long-term, wet, and BEC
  add-ons by road group (section 4.3.2.3); snow/ice roads; stabilizing material
  base and RRQR add-on (section 4.3.4.1).
- Culverts: 168 installed cells (12 lengths × 14 diameters) and 14 supply-only
  cells (Table 4-3).
- Bridges: 36 superstructure cells and 19 substructure/bearing/survey cells
  (Table 4-4).
- Road maintenance: 22 road maintenance groups A–V (Table 4-6).
- Silviculture: 167 basic, 45 enhanced, and 6 wildfire-enhanced BEC entries
  (Table 4-8, CAD/ha).
- Root disease control base and adders with published $1,200–$1,469/ha clamp.
- High development cost threshold/rule (BCTS only).

### CAM 2026 (effective 2026-01-01)

- Road construction: 8 bank-height categories × 2 rock classes and 2 published
  add-ons (Table 5-1, CAD/km).
- Log bridges: 17 spans × 5 published cost columns (single log sill + four multi-log crib columns), normalized from thousands of
  dollars to CAD per bridge (Table 5-2).
- Permanent/portable bridges: 24 spans × 5 abutment heights, normalized from
  thousands of dollars to CAD per bridge (Table 5-3).
- Culverts: 12 diameters × installed/materials (Table 5-4, CAD/m) plus the
  wood-culvert flat rate.
- Basic silviculture: 15 BEC classes (Table 5-6, CAD/ha).
- TOA allowances: forest planning and administration $21.56/m³ (scale), low
  volume $10.89/m³, road management $4.73/m³ (scale), root disease control
  base/add-ons and $1,224–$1,560/ha clamp.
- Specified operations: inland water $12.10/m³, Clayoquot Sound $13.02/m³,
  tree crown modification $28.42/$15.46 per tree, ecosystem-based management
  $9.39/m³, long haul $0.171/m³/km beyond 100 km, barging $11.74 (GRIS)/$9.68
  (non-GRIS), and the BCTS high development cost rule.

### Interior Basic Silviculture (quarterly)

- 2026-10-01: seven forest zones, all-species average, CAD/m³.
- 2026-07-01: seven forest zones, all-species average, CAD/m³.

## Units and coverage

| Basis | Rows |
|---|---:|
| CAD/each | 429 |
| CAD/ha | 235 |
| CAD/km | 91 |
| CAD/m³ | 67 |
| CAD/m | 38 |
| CAD/km/% | 11 |
| CAD/m³/km | 2 |
| CAD/tree | 2 |
| CAD/ha/% | 2 |
| CAD/ha/stem | 2 |

Coverage is intentionally split between cost components and policy parameters.
Table 4-7/4-9 (IAM cruise and low-grade factors) and Table 5-5/5-7 (CAM ECE trend
and low-grade fractions) are parsed as policy parameters and are not emitted as
cost rows. See `bc_appraisal_coverage.csv`.

## What is *not* published as a unit allowance

- **IAM tree-to-truck / logging.** The IAM has no public $/m³ logging allowance
  table. Logging is embedded in the estimated winning bid. The restricted ILCR
  microdata were not used.
- **General truck hauling.** The IAM represents hauling through cycle time in the
  EWB equation and through rail/water/barge specified operations; it does not
  publish a general truck-haul $/m³ table.
- **CAM logging.** The CAM has no public $/m³ logging allowance table; logging is
  embedded in the EWB equation.
- **ECE project costs.** Engineering cost estimates are site-specific. This
  dataset captures tabular ECE components, trend-factor policy, and cost caps,
  but not a province-wide ECE $/m³ or $/km rate. Appendix I equipment/labour
  rates are input rates, not allowance tables.
- **BGC-level quarterly silviculture.** The quarterly Interior table is published
  by **forest zone**, not BGC zone. BGC detail is available only in IAM Table 4-8
  (CAD/ha, basic/enhanced). No BGC allocation of the quarterly $/m³ values was
  invented.

## Validation

- 879 rows; no negative, NaN, infinite, or zero values.
- `observation_type` is `appraisal_allowance` on every row.
- All `cost_basis` values are in the published unit set.
- Unique key `(source, component, subcomponent, operability, zone, road group,
  matrix row, matrix column)`: 0 duplicates.
- Regional tables reconcile: IAM FMA 6/6; IAM road maintenance 22/22; CAM road
  construction 20/20; IAM culverts 182/182; CAM log bridges 85/85; CAM permanent
  bridges 120/120; CAM culverts 24 + 1 wood; CAM silviculture 15/15; quarterly
  silviculture 7 + 7.
- Eleven spot checks against the PDFs pass (five IAM, four CAM, two quarterly).
  Exact checks are recorded in `manifest.json.spot_checks` and
  `PROVENANCE.md`.

## Policy rules and caps

- IAM FMA equations are clamped to the regional min/max in Table 4-1.
- IAM FEWB floor is $0.25/m³; CAM EWB/FEWB floor is $0.25/m³.
- IAM high development cost: `HDC = DC - 3.27`, zero when `DC <= 5.93`
  (BCTS only).
- CAM high development cost: `HDC = DC - 8.23`, zero when `DC <= 13.76`
  (BCTS only).
- CAM long haul: `LHC = (HD - 100) * 0.171`, zero when `HD <= 100 km`.
- IAM surface tow: `rate = 0.0389 * D - 0.8744`, floor $1.69/m³.
- IAM root disease control is clamped to $1,200–$1,469/ha; CAM to
  $1,224–$1,560/ha.
- IAM uses RFM 1.076, MLDC $2.66/m³, MLSO $0.12/m³; CAM uses CTC 0.975,
  RFM 1.052, ACPI 182.89, and competitive timber sale infrastructure/operation
  costs $0.12/$0.33 per m³.
- Tabular road, bridge, and culvert values must not be interpolated. Use the
  nearest published unit; out-of-table structures require an ECE.

## Limitations

- **Allowance ≠ actual cost.** These are appraisal policy values. They can differ
  materially from a contractor's incurred cost and from a winning bid.
- **Not transaction microdata.** No ILCR, CCTMCS, bidder-level, or licence-level
  records were used. Publishing a public table does not make it an observed cost.
- **Scale/cruise differences.** CAM FPA and road management values are for
  scale-based cutting authorities; cruise-based appraisals multiply by CTC.
  IAM FMA is a regional equation, not a flat allowance.
- **No general logging/truck-haul rate.** Users must not treat the EWB equation
  coefficients as a cost allowance.
- **Bridge/culvert bases.** Values are per structure or per metre, not per m³ of
  timber. Do not sum them into a $/m³ cost without volume and structure counts.
- **Vintage.** Values apply only on/after their effective date. The manuals are
  revised; use the matching manual version for a given cutting authority.
- **Quarterly forest zones.** The quarterly table is forest-zone-level, not BGC.
  A BGC-level quarterly series cannot be derived from the public table alone.

## Merge recommendation

**Do not merge into `forest_cost_revenue.csv` or the model as observed costs.**
If a later task needs appraisal allowances, keep them in a separate
`appraisal_allowance` layer, carry the `cost_basis` and effective date, and do not
add them to contractor-cost or market-price observations. Any comparison must
label them as policy allowances and avoid double counting with stumpage, EWB, or
TOA components already embedded in appraisal rates.

## Rebuild

```bash
python scripts/national/build_bc_appraisal_costs.py \
  --pdf-dir tmp/bc_appraisal_costs_raw/pdfs \
  --out-dir data/derived/national/harvest_basis/bc_appraisal_costs
```

The builder fails closed on unexpected table layouts, missing regions, duplicate
keys, negative values, or failed spot checks.
