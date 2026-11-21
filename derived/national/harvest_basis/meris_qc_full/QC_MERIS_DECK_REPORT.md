# QC MERIS model-input revenue/cost deck report

| Field | Value |
|---|---|
| Date | 2026-11-21 |
| Status | `screening_only`; `policy_grade=false`; `observed_transactions=false`; `model_input=true` |
| Source | Quebec BMMB/MFFP MERIS 3.3.0, `MERIS_BdTbl.accdb`, database release 2025-09-23 |
| Artifact | `data/derived/national/harvest_basis/meris_qc_full/` |
| Parent design | `planning/forest-cost-revenue-ledger.md` |
| Extraction note | `planning/meris-qc-extraction.md` §7–§8 |
| Access | Read-only `mdb-tables` / `mdb-count` / `mdb-export`, mdbtools 1.0.0; no password or Access UI |

**Bottom line.** MERIS exposes a complete **model-input** revenue and cost
deck, not an observed price or harvest register. The deck is published in full
(45 species / 7 products / 2 series; 12 SEPM species × 76 DBH × 2 series × 3
shipped profiles; 191 zones × 14 groups for both the economic decomposition
and the administered rates; 191 zones of supply costs; 94 treatments). The
`Tot = Rdv + Bnf + Rsl + Aut1 + Aut2` identity holds exactly on all 18,718
zone × group × product cells. A **2,688-row** ledger block is provided so the
deck can be joined to the forest-sector ledger without pretending that any value
is an observed transaction; it carries the optional `quality` and `dbh_cm`
dimensions, both price series, and the 12-species species/DBH curves. **No
provincial net value is estimated**: MERIS has no
actual volume, no permit/UA crosswalk, no destination mix for haul, no full
harvest cost per zone, and no join from its royalty group taxonomy to its
economic-value group taxonomy.

## 1. Provenance and extraction

| Item | Value |
|---|---|
| Archive | `/tmp/meris/meris.zip`, 41,762,907 bytes, SHA-256 `145431a93b466525751e08f3fe73437de3aee49f3f6d78dc9d77378769f9faa3` |
| Database | `/tmp/meris/extracted/MERIS_BdTbl.accdb`, 70,893,568 bytes, SHA-256 `033f8cc1f428430cd66d247e022ef78ab76b3d78cedae00df498177b5c087857` |
| Database release | 2025-09-23 (`MERIS 3.3.0`) |
| Extraction | `scripts/extract_meris_qc_full.py`; read-only `mdb-export` |
| Reproduce | `.venv/bin/python scripts/extract_meris_qc_full.py --db /tmp/meris/extracted/MERIS_BdTbl.accdb --out data/derived/national/harvest_basis/meris_qc_full` |
| Machine manifest | `manifest.json` (source counts, file hashes, columns, checks) |

No value was imputed, zero-filled, scaled to a provincial harvest, or copied
from another province. Zeros and placeholders are retained in the price deck
and explicitly labelled `not_applicable_zero` or `placeholder_0.0100`; they are
excluded from the ledger block rather than converted into revenue.

## 2. Deliverables and row counts

| File | Rows | Grain / content |
|---|---:|---|
| `meris_price_deck.csv` | 630 | species × 7 products × 2 series (45 species) |
| `meris_price_deck_wide.csv` | 45 | source species layout, 14 price fields plus inclusion flags |
| `meris_revenue_curves.csv` | 5,472 | profile (2/3/4) × 1,824 species × type × DBH rows; 12 SEPM species, DBH 10–160 |
| `meris_zone_values.csv` | 18,718 | zone × group × product; `Rdv/Bnf/Rsl/Aut1/Aut2/Tot` (2,674 × 7) |
| `meris_zone_values_wide.csv` | 2,674 | source zone × group layout, 42 value fields |
| `meris_royalties.csv` | 2,674 | zone × group administered rates, 7 products, 2025-09-19 |
| `meris_royalties_long.csv` | 18,718 | zone × group × product long form |
| `meris_costs.csv` | 191 | zone supply-cost parameters plus ledger-ready aggregates |
| `meris_silviculture.csv` | 94 | treatment catalogue; 40 `DolHa` usable in the ledger |
| `forest_cost_revenue_qc_model.csv` | 2,688 | canonical 18-field ledger block (16 core fields plus `quality` and `dbh_cm`; model input only) |
| `manifest.json` | — | source counts, output hashes, check results |

The row-count checks in the task map to the **source** tables as follows:
price table 45 species (630 long rows), curves 1,824 × 3 (5,472 long rows),
zone values 2,674 zone × group rows (18,718 long rows), royalties 2,674,
costs 191. The wide companions preserve the source row counts (`45`, `2,674`,
`2,674`, `191`) for audit.

## 3. Units and price-point assumptions

### 3.1 Species/product price deck (`tbl_Essences_frm_inv_tiges`)

- **Series.** `Prix_*_1` is the **tendance** series and `Prix_*_2` is the
  **courant** series. This is the manual’s ordering in §4.5.2 (“Les valeurs
  tendance (1) et courantes (2)”). The mapping is an assumption from the
  manual; it is not a field label in the table.
- **Unit.** `CAD_per_m3_log`, inferred. MERIS prices its products per m3 of
  log/product volume; the table has no unit column. This is not an observed
  mill settlement.
- **Price point.** `mill_gate`, inferred. The manual defines the product value
  as the market value of products and by-products **minus the costs of
  transformation**; for species the profiled mill does not transform, the
  default value is the supply cost, treated as the sale price to the user.
  That is a delivered-log value at the mill gate, not a standing bid.
- **Stumpage inclusion.** `Redev_*_Inclus=1` means the redevance is included in
  the price. Such a value is gross of the Crown charge; the royalty deck must
  be subtracted before a sector net value, not added to revenue.
- **Placeholders.** Every `PATE` value is `0.0100` or `0.0000`. The manual
  states that `0.01` is the default “value not set” and raises a warning. These
  values are labelled `placeholder_0.0100` and are **not** used as revenue.
  Only `THO` has a positive `AUTRE` value (75.00).
- **Coverage.** 251 of 630 cells are positive model inputs; 293 are zero
  (not applicable), 86 are the `PATE` placeholder. Positive values cover 28
  hardwood species; the 12 SEPM species are zero in this table and are covered
  by the DBH curves instead.
- **Ledger ingest.** Both series are carried into the ledger as alternative
  model scenarios, with licence suffixes `C` (courant) and `T` (tendance). The
  rows are not independent observations and are never summed. `PATE` maps to
  `pulpwood` but has no usable value, so no pulpwood row is emitted.

Current-series positive ranges (CAD/m3): DER 113.00–263.00 (19 species),
F1 73.2633–319.1016 (27), F2 73.00–258.00 (27), F3 48.00–230.00 (28),
F4 37.00–120.00 (25), AUTRE 75.00 (1; THO), PATE none usable.

### 3.2 Species × DBH revenue curves (`tbl_essences_revenus_EssDhp_Profil_2/3/4`)

- **Series.** Each table has 912 `courant` and 912 `tendance` rows.
- **Coverage.** 12 SEPM species: EPB, EPN, EPO, EPR, MEH, MEJ, MEL, MEU, PID,
  PIG, PIS, SAB; DBH 10–160 cm; 152 rows per species per profile (76 DBH × 2
  series).
- **Unit.** `CAD_per_m3_log`, inferred from the MERIS revenue form.
- **Price point.** `mill_gate`, the same product-value definition as §3.1.
- **`SCIAGE = PATE` in every row.** The manual explains that SEPM revenue is a
  composite of sawing, chips, and by-products; the two columns are identical
  and the split is used for the SEPM royalty calculation, not for two
  independent prices. The CSV therefore has one `revenue` column plus
  `sciage` and `pate` columns; the equality is asserted at extraction.
- **Profile duplication.** `Profil_2`, `Profil_3`, and `Profil_4` are
  byte-identical in this release (same SHA-256 for all three exports). The
  profile descriptions are retained (`Scieur Res`, `Scieur FD et Res`,
  `Scieur Res autre 1`) but the values do not differ. Do not treat the three
  profiles as independent observations. The ledger ingests the canonical
  `Profil_2` only.
- **Ledger ingest.** Both `courant` and `tendance` curve rows are carried as
  `model_input:mill_gate` `delivered_log_revenue` rows with `dbh_cm` and
  `quality=NA`. The curve is a composite of sawing, chips, and by-products, so
  it is booked as `mixed_log`, not as a single grade. `SCIAGE=PATE` is asserted
  at extraction; no `0.01` placeholder exists in the curve tables.
- **Base table is a placeholder.** `tbl_essences_revenus_EssDhp` (the
  unsuffixed base table) is all `0.0100`; the actual model values are in the
  three `_Profil_*` tables. This is a correction to the earlier sample note.

### 3.3 Zone economic values (`tbl_Zones_RedevBenefRentSal_F1234`)

- **Unit/currency.** `CAD_per_m3_log`, **$2023** (`CAD_real_2023`), per manual
  §4.8.1.
- **Components.** `Rdv` = trend redevance; `Bnf` = profit of harvesting and
  processing firms; `Rsl` = labour rent; `Aut1` = CPRS adjustment of 25 $/m3
  net in 3.3.0 (0 or 25 in this release); `Aut2` = second adjustment (zero in
  this release); `Tot` = their sum.
- **Identity.** `Tot = Rdv + Bnf + Rsl + Aut1 + Aut2` holds on all 18,718
  zone × group × product cells; maximum absolute residual is `0.0000` after
  4-decimal source rounding.
- **Not a market price.** This is an economic value decomposition. `Bnf`,
  `Rsl`, and `Aut1` are factor incomes/adjustments, not ledger revenue
  components. Do not add `Bnf + Rsl + Aut1` to `delivered_log_revenue`.

### 3.4 Administered royalties (`tbl_redevances_F1234`)

- **Unit/currency.** `CAD_per_m3_log`, nominal; all rows `DateMaj=2025-09-19`;
  all `RdvVariable=0`.
- **Products.** DER, F1, F2, F3, F4, PATE, AUTRE.
- **Taxonomy.** The 14 groups are `Auf, Boj, Bop, ChCet, Epx, Ero, Ers, Heg,
  Mel-Pru-Tho, Peu, Pib, Pig, Pir, Sab`. They are **not the same 14 groups** as
  the zone-value table (`AUF, BOJ, BOP, CHE-CET-NOY-CAR, ERO, ERS, FRX, HEG,
  PEU, PIB, PIR, PRU, SEPM, THO`). A direct group-name join is invalid; a
  crosswalk is required. This is a new gap (G18).
- **Coverage.** All 2,674 zone × group rows; F3 and PATE are always at least
  0.25, F1/F2 are zero in 955 rows, DER zero in 1,528, AUTRE zero in 2,483.

### 3.5 Zone supply costs (`tbl_couts_zones`)

- **Units.** `CAD_per_m3_log` for all `*_dol_m3` fields;
  `chemin_constr_tertiaire_dol_ha` and `autre*_fixe_dol_ha` are `CAD_per_ha`.
- **No date field.** The cost year is taken as the database release (2025) for
  ledger bookkeeping and is labelled `cost_year_basis=db_release_2025-09-23`.
  This is an assumption, not a source field.
- **Semantics.** Industrial-survey/model parameters by tarification zone, not
  audited actuals. `admin_dol_m3` is operator administration, not Crown
  `admin_fee`. `transport_marche_*` is market transport, not mill supply.
- **Ledger-ready aggregates.** `road = chemin_entretien + chemin_constr_prim_sec`;
  `overhead = admin + mesurage`; `harvest` uses `chargement` only (loading);
  `roadside_haul_partial = transport_fardier + dechargement` is retained as a
  deck field but is **not** a complete haul row. The tertiary road and
  `autre*_fixe` area costs are not converted to CAD/m3 (no yield/area basis).
- **Ranges.** Road 0.50–12.10 (median 2.50); overhead 5.40–8.00 (6.60);
  loading 1.60–3.10 (2.90); tertiary road 920–1,833 CAD/ha (median 1,191).

### 3.6 Silviculture treatments (`tbl_Liste_Traitements`)

- **Units.** 40 `DolHa` (CAD/ha), 19 `Dol1000Plants`, 1 `Dol1000Micro`, and 34
  equation treatments (`LnCP+`, `LnCT`, `LnCP-`).
- **Usable in ledger.** Only the 40 `DolHa` rates (412–2,318 CAD/ha). The
  per-1,000-plant and per-1,000-microsite rates need plants/ha and
  microsites/ha, which MERIS does not supply; the equations need m3/tige and
  cutting mode. These are not converted or zero-filled.
- **Semantics.** Provincial treatment catalogue rates, not actual spend or a
  specific licence obligation. `Valeur_Tot = Taux_EXE + Autre_cout` in the
  source.

## 4. QC ledger block

`forest_cost_revenue_qc_model.csv` is a canonical 18-field ledger block. It
contains **model input only** and has no Crown perspective, no mirrors, and no
observed transaction.

| Component | Rows | Unit | Price point | Confidence | Derivation |
|---|---:|---|---|---|---|
| `delivered_log_revenue` | 2,075 | `CAD_per_m3_log` | `mill_gate` | medium (2,073) / low (2 AUTRE) | 251 species × product × series price rows plus 1,824 species × DBH × series curve rows; positive values only; DER→peeler, F1–F4→sawlog, PATE→pulpwood, AUTRE→mixed_log |
| `road` | 191 | `CAD_per_m3_log` | `roadside` | medium | `chemin_entretien + chemin_constr_prim_sec` per zone |
| `overhead` | 191 | `CAD_per_m3_log` | `roadside` | medium | `admin + mesurage` per zone |
| `harvest` | 191 | `CAD_per_m3_log` | `roadside` | low | `chargement` only; **partial**, full harvest equation missing |
| `silviculture` | 40 | `CAD_per_ha` | `roadside` | medium | `DolHa` treatments only; 54 rows not usable |

Common row properties:

- `jurisdiction=QC`, `source=prov_qc_meris`, `year=2025`,
  `perspective=forest_sector`.
- `value_basis=model_input:mill_gate` for revenue and
  `model_input:roadside` for costs.
- `confidence=medium` or `low`; no `high`.
- `volume_m3=1.0` and `rate_denominator=1_m3` (or `1_ha` for silviculture).
  It is a **rate denominator**, not an actual harvest volume or a weight from
  a permit record.
- `notes` carry `currency_basis`, source table/field, `not_observed=1`,
  `model_input=1`, `not_a_transaction=1`, price point, volume basis, coverage,
  and the release date used for the price/cost year.
- The quality class (DER/F1/F2/F3/F4/AUTRE) is in the dedicated `quality`
  field and repeated in `qc_quality` and the licence suffix
  (`QC-MERIS-<species>-<quality>-<C|T>`). F1–F4 therefore do not collide.
- The DBH curve coordinate is in `dbh_cm` on `mixed_log` rows with `quality=NA`
  and a `QC-MERIS-CURVE-<species>-<dbh>-<C|T>` licence.
- All 2,688 rows pass `workflows.national.harvest.cost_revenue.load_ledger`;
  the normalized key is unique; no duplicate or unpaired mirror rows exist.

The validator’s `Evidence` enum now includes `model_input`. A model-input row
must carry `not_observed=1` and `model_input=1`, and cannot use `high`
confidence. This prevents a model parameter from being mistaken for an
observed payment or sale.

## 5. Coverage and gaps

### 5.1 What the deck covers

| Layer | Coverage |
|---|---|
| Species/product price deck | 45 species; 28 with positive current values; 251 positive cells |
| Species/DBH curves | 12 SEPM species; 76 DBH classes × 2 series × 3 profiles |
| Economic zone values | 191 zones × 14 groups × 7 products; identity exact |
| Administered royalties | 191 zones × 14 groups × 7 products; 2025-09-19 |
| Supply costs | 191 zones; road, overhead, loading aggregates; full route columns retained |
| Silviculture | 40 `DolHa` rates; 54 treatment rows retained but not ledger-usable |
| Ledger block | 2,688 model-input rows; 251 quality-class price rows; 1,824 species/DBH curve rows; 28 + 12 revenue species |

### 5.2 Gaps (existing G01–G14 plus new)

| ID | Gap | Consequence |
|---|---|---|
| G01 | No observed delivered log price | `delivered_log_revenue` here is a model input, not a transaction |
| G02 | **Resolved 2026-11-21.** Ledger now has a `quality` field | quality classes are keyed in `quality`; product compatibility is validator-enforced |
| G03 | Harvest is equation-based | ledger `harvest` is loading only and low confidence |
| G04 | Treatment density missing | 19 per-1,000-plant and 1 per-1,000-microsite rates not converted |
| G05 | Tertiary road is CAD/ha | excluded from `road`; no yield factor to convert |
| G06 | No tarification-zone → UA crosswalk | `spatial_unit` is a zone, not a management unit |
| G07 | No actual volume | `volume_m3=1` is a rate denominator; no volume weighting or provincial total |
| G08 | Year/currency mismatch | royalties 2025 nominal; zone values $2023 real; never mix |
| G09 | Factor incomes | `Bnf`, `Rsl`, `Aut1` are not ledger components |
| G10 | Cost year absent | 2025 is a release-year assumption |
| G11 | ACCDB schema not dumpable | types inferred from export headers and manual |
| G12 | Base revenue table is placeholder | use `_Profil_*`, not `tbl_essences_revenus_EssDhp` |
| G13 | `admin_dol_m3` is operator admin | not Crown `admin_fee` |
| G14 | Sample was one zone | now full 191-zone deck, but still no volume coverage |
| **G15** | Price `PATE` column is `0.0100` placeholder | no hardwood pulp revenue; excluded from ledger |
| **G16** | Profiles 2/3/4 are byte-identical | do not treat as independent estimates |
| **G17** | Price deck has no unit/price-point field | unit/price point inferred from manual, not declared |
| **G18** | Royalty and zone-value group taxonomies differ | no direct zone × group royalty join; crosswalk required |
| **G19** | Haul destination mix missing | zone table has 10 mill-route columns; no zone × species × destination weights; haul omitted from ledger |
| **G20** | Price deck has no date | 2025 is a release-year assumption; may be model vintage, not a market year |
| **G21** | **Resolved 2026-11-21.** Ledger now has a `dbh_cm` field | 12 SEPM species × 76 DBH × 2 series are in the ledger block as `mixed_log` curve rows |
| **G22** | Price point inferred as mill gate | manual supports a net-of-processing value; confirm with a BMMB/mill settlement |
| **G23** | `PATE`/`AUTRE` product semantics | ledger product enum cannot represent all QC classes; AUTRE mapped to `mixed_log` with low confidence |

### 5.3 What can and cannot feed net value

| Use | Status |
|---|---|
| Model-input delivered log revenue for 28 hardwood species, mill gate | **Can feed** a sensitivity/labelled model-input revenue term; not a transaction or policy price |
| Zone road, overhead, loading, silviculture costs | **Can feed** a cost deck as model parameters; loading is partial and harvest is incomplete |
| Administered royalties | **Can feed** a Crown-rate deck; not joined to the ledger because the group taxonomies differ |
| Zone economic values | **Can feed** context only; not additive to cash revenue/cost |
| Species/DBH curves | **Can feed** the ledger as `dbh_cm` model-input revenue rows; still not an observed price |
| Full harvest cost per zone | **Cannot**; needs m3/tige, cutting mode, stand type, and the equation |
| Haul to mill per zone/species | **Cannot** from this table alone; destination mix and assignment are missing |
| Volume-weighted provincial revenue/cost | **Cannot**; no actual volume or UA crosswalk |
| Forest-sector net value | **Not estimated**; incomplete component coverage and no compatible volume |
| Policy-grade price or net value | **No**; `policy_grade=false` |

The ledger block is therefore a **pre-Crown component deck**, not a net-value
result. Even the pre-Crown surplus is not estimated because haul and full
harvest are missing. A user may combine the rows only after adding a documented
volume weight, a haul basis, a full harvest basis, and a royalty join; until
then the correct result is `not_estimated`, not a sum.

## 6. Tests, commits, status

### 6.1 Verification

- Extraction row counts: price table 45; curves 1,824 × 3; zone values 2,674;
  royalties 2,674; costs 191; treatments 94.
- Price deck: 45 species × 7 products × 2 series = 630; 0 NaN.
- Curves: 5,472 rows; 1,824 per profile; 912 `courant` + 912 `tendance` per
  profile; 0 NaN; `SCIAGE=PATE` everywhere.
- Zone values: 18,718 long rows; 191 zones; 14 groups; identity residual 0.
- Royalties: 2,674 rows; 191 zones; 14 groups; `RdvVariable=0`; one
  `DateMaj=2025-09-19`.
- Costs: 191 rows; all 191 zones; no zero road/overhead/loading.
- Ledger: 2,688 rows; unique normalized key; `load_ledger` passes; 2,075
  revenue (251 price + 1,824 DBH) + 191 road + 191 overhead + 191 harvest +
  40 silviculture; 0 `high` confidence; all rows `model_input=1` and
  `not_observed=1`.
- Quality rows: DER 38, F1 53, F2 53, F3 56, F4 49, AUTRE 2; `PATE` 0.
- DBH rows: 12 SEPM species, 76 DBH classes (10–160 cm), 2 series, canonical
  `Profil_2`; all `quality=NA` and `product=mixed_log`.
- `python -m pytest tests/test_forest_cost_revenue.py
  tests/test_cost_revenue_merge.py tests/test_forest_lp_v1.py -q` → **39
  passed**.
- `ruff check` on the changed Python files → clean.

### 6.2 Commits and status

- Data submodule branch: `feature/osecan-zonal-bc-supply`; data commit contains
  this directory (inspect with `git -C data log -1`).
- Parent commit contains the extractor, validator change, tests, and planning
  updates (inspect with `git log -1`).
- Public OSeCAN: **not touched**; no OSeCAN remote is configured in either
  repository.
- `git status --porcelain` at close: see the orchestrator report. The parent
  worktree may contain unrelated untracked work from other agents; it was not
  staged. No unexpected `D` was present at the start or end of this task.

## 7. Next

1. **QC net-value sensitivity (model-input, not policy).** Add a documented
   volume weight (UA/zone × species × product), a haul destination mix, and a
   full harvest equation; then compute a range, not a point estimate. Report
   the price point, year/currency, and the missing-component list.
2. **Forest LP reporting.** Use the deck as a post-solve report or a bounded
   within-QC sensitivity only after the missing components are filled. Do not
   place model-input revenue in the v1 least-deviation objective.
3. **Observed validation.** Obtain BMMB auction/delivered sale records or mill
   settlements to test the inferred mill-gate price point and the `PATE`
   placeholder.
4. **Schema follow-up (done 2026-11-21).** `quality` and `dbh_cm` are in the
   ledger key; the QC block now carries them. The remaining work is a
   volume-weighted join, not another schema change.
5. **Crosswalk.** Build a versioned MERIS royalty-group ↔ zone-value-group ↔
   species crosswalk, and a tarification-zone ↔ UA/region crosswalk.

## References

- `data/derived/national/harvest_basis/meris_qc_full/manifest.json`
- `data/derived/national/harvest_basis/meris_qc_sample/README.md`
- `planning/forest-cost-revenue-ledger.md` §2–§4
- `planning/meris-qc-extraction.md` §3–§4 and §7
- `workflows/national/harvest/cost_revenue.py`
- `scripts/extract_meris_qc_full.py`
