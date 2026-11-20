# MERIS QC cost/revenue sample

| Field | Value |
|---|---|
| Status | `screening_only`; `policy_grade=false`; **sample, not a full provincial extraction** |
| Date | 2026-11-20 |
| Source | Quebec BMMB/MFFP MERIS 3.3.0 (public download) |
| Archive | `https://encheres.forets.gouv.qc.ca/media/29260/meris.zip` (41,762,907 bytes; SHA-256 `145431a9…f9faa3`) |
| Database | `MERIS_BdTbl.accdb` (70,893,568 bytes; SHA-256 `033f8cc1…087857`) |
| Access | Read-only `mdb-tables` / `mdb-count` / `mdb-export` with mdbtools 1.0.0. No password, encryption, or Access UI was required to read the tables. |
| Parent report | `planning/meris-qc-extraction.md` |

This directory is a **sample** extracted from the MERIS back-end to test the
forest cost/revenue ledger mapping. It is not a provincial inventory, not a
volume-weighted estimate, and not a policy-grade dataset. No value was
imputed, zero-filled, or fabricated. The two demo ledger rows blocks are
explicitly flagged `demo_simulation=1` and `not_for_policy=1`.

## 1. Archive and database

The public page links `meris.zip`. The archive contains:

| Member | Bytes | Role |
|---|---:|---|
| `MERIS_BdTbl.accdb` | 70,893,568 | Back-end tables (the extraction target) |
| `MERIS.accdr` | 85,258,240 | Compiled Access 2016 runtime UI (not executed) |
| `Import-MERIS.xlsm` | 63,631,610 | Bulk-import workbook |
| `importation_donnees_meris.xlsx` | 111,204 | Small import template (downloaded separately) |
| `Conversion-Redevances.xlsm` | 433,411 | Q3 2025 VMBSP → PETRO quality conversion |
| `MERIS_Aide.doc` | 9,665,024 | 177-page user manual (field semantics) |
| `Notes_Versions.txt` | 12,837 | Version history |
| `Shell.bat` | 216 | Reports `MERIS 3.3.0`, Access 2016 |

The database is **ACCDB**, not the `.mdb` named in the task brief. `mdbtools`
1.0.0 reads it. `mdb-tables -1` lists **264 tables**. `mdb-count` and
`mdb-export` work. `mdb-schema` fails with `Invalid backend type` for ACCDB, so
field types below are inferred from export headers and the MERIS manual, not
from a declared schema dump. This is an access-layer limitation, not a data
lock.

## 2. Key tables and semantics

| Table | Rows | Content |
|---|---:|---|
| `tbl_Liste_ZonesRedev` | 191 | Tarification zone list (`Zone_Redev`, `Secteur`) |
| `tbl_redevances_F1234` | 2,674 | Current administered stumpage rates, 191 zones × 14 species groups, `DateMaj=2025-09-19` |
| `tbl_Zones_RedevBenefRentSal_F1234` | 2,674 | Economic value decomposition in **$2023**: `Rdv` (trend redevance), `Bnf` (harvest/processing profit), `Rsl` (labour rent), `Aut1` (CPRS 25 $/m3 adjustment), `Tot` |
| `tbl_couts_zones` | 191 | Supply-cost parameters by zone: road, transport, loading/unloading, scaling, administration ($/m3 and $/ha) |
| `tbl_Liste_Traitements` | 94 | Treatment catalogue: 40 `DolHa`, 19 `Dol1000Plants`, 1 `Dol1000Micro`, 34 harvest treatments without a rate |
| `tbl_Equations_Recolte` | 45 | Harvest-skidding cost equation coefficients by species/cutting mode |
| `tbl_Profil_Rentabilite_EqGraph` | 30 | Computed harvest cost ($/m3) by m3/tige for CT/CP+/CP− |
| `tbl_essences_revenus_EssDhp` | 1,824 | Product revenue by species/DBH; **every `SCIAGE` and `PATE` value is 0.0100** (placeholder) |
| `tbl_770rq_Resultats_Rentabilite` | 54 | Shipped demo profitability simulations ($/ha) |
| `tbl_775rq_Resultats_Rentabilite_Frais` | 54 | Cost breakdown of those simulations |
| `tbl_Rentabilite` | 18 | Financial/economic simulation detail (64 fields) |
| `tbl_Volume_Prescription` | 0 | Empty; MERIS is not an actual-volume register |
| `tbl_unifiee_assigne_zones` | 1 | One row; not a provincial assignment table |
| `tbl_unifiee_assigne_traitements` | 1 | One row |

Full table list: `tables_all.txt`. Key counts: `tables_key.csv`.

### Field semantics confirmed by `MERIS_Aide.doc`

- §4.5.2–4.5.5: `tbl_couts_zones` is the **supply-cost parameter** set, from
  industrial surveys, by tarification zone. It is not an audited actual.
- §4.5.4: `Redevances` are the VMBSP (valeur marchande des bois sur pied).
- §4.8.1: `Rdv` = redevance tendance; `Bnf` = profit of harvesting and
  processing firms; `Rsl` = labour rent; `Aut1` = CPRS adjustment of 25 $/m3 net
  (MERIS 3.3.0); `Tot` = sum. The matrix is in **$2023** and is an economic
  value decomposition, **not** a market price.
- §9.3.1–9.3.2: the four economic reports are `Revenus détaillés`, `Flux
  monétaires`, `Rapport synthèse`, `Rapport détaillé`; the CSV exports are the
  intended analysis layer.
- `Conversion-Redevances.xlsm` sheet `Données brutes 3eme trim 2025` contains
  the raw Q3 2025 VMBSP by species/quality/zone. Sheet `Correspondance` holds
  the ABCD → PETRO F1/F2/F3/F4/Pâte weights; sheet `Matrice F1-2-3-4` matches
  `tbl_redevances_F1234`; sheet `Export` is the 2,674-row export.

## 3. Files in this sample

| File | Rows | Content |
|---|---:|---|
| `redevances_2025_sample.csv` | 42 | Raw `tbl_redevances_F1234` for zones 151/192/888 |
| `couts_zones_sample.csv` | 3 | Raw `tbl_couts_zones` for zones 151/192/888 |
| `economic_values_2023_sample.csv` | 42 | Raw `tbl_Zones_RedevBenefRentSal_F1234` for zones 151/192/888 |
| `traitements_sample.csv` | 94 | Full `tbl_Liste_Traitements` |
| `simulation_770_sample.csv` | 3 | Demo `2-Courant / 1-Base` for CPRS, CPPT M and EC |
| `simulation_775_sample.csv` | 3 | Matching cost breakdown |
| `forest_cost_revenue_sample.csv` | 17 | **Actual parameter rows** mapped to the ledger (zone 151) |
| `forest_cost_revenue_demo.csv` | 7 | **Demo simulation block**, flagged `demo_simulation=1` |
| `field_mapping.csv` | 49 | MERIS field → ledger component/unit/basis/confidence |
| `gaps.csv` | 14 | Explicit coverage and schema gaps |
| `provenance.json` | — | URLs, hashes, versions, access mode |
| `manifest.json` | — | Per-file size and SHA-256 |
| `tables_all.txt` | 264 | Table names |
| `tables_key.csv` | 20 | Key tables and row counts |
| `extraction_commands.sh` | — | Exact read-only commands |

### Actual parameter sample (`forest_cost_revenue_sample.csv`)

Zone 151, species `BOJ`, `SAB`, `EPB`; year 2025 for current rates and 2023 for
the economic-mode `Rdv` row. It contains:

- `stumpage_base` from `tbl_redevances_F1234`, with Crown `+1` and
  forest-sector `−1` mirrors: BOJ DER 18.6386, BOJ F1 8.2792, BOJ PATE 0.2500,
  SAB F3 7.4400, EPB PATE 0.2500, plus a 2023 BOJ F1 `Rdv=20.0000` in
  `CAD_real_2023`.
- `haul=17.10` = mill transport 15.20 + fardier 0.90 + unloading 1.00.
- `road=0.90` = maintenance 0.10 + primary/secondary construction 0.80;
  tertiary road (1,214 $/ha) is excluded because the ledger only allows
  `CAD_per_ha` for silviculture.
- `overhead=6.10` = operator administration 5.40 + scaling 0.70.
- `harvest=2.80` = loading only, confidence `low`; the full falling/bucking/
  skidding cost is equation-based and is **not** in this sample.
- `silviculture=1,026.00 CAD/ha` for treatment `BPR`.

This sample deliberately has **no `delivered_log_revenue`** row. The 17 rows
validate against `workflows.national.harvest.cost_revenue.load_ledger`; net
value is not estimated because revenue and full harvest are missing.

### Demo block (`forest_cost_revenue_demo.csv`)

From `Simulation - 1 / zone 192 / 2-Courant / 1-Base / CPRS`:

| Component | CAD/m3 | Derivation |
|---|---:|---|
| `delivered_log_revenue` | 178.534659 | `Valeurs_Produits 28,224.2871 / 158.08856` |
| `stumpage_total` | 1.755121 | `Redevances 277.4645 / 158.08856` |
| `harvest` | 31.968926 | `(Récolte_Débardage 4,790.5029 + Chargement 263.4186) / 158.08856` |
| `road` | 10.353922 | `(prim/sec 131.7093 + tertiaire 1,472.2 + entretien 32.9273) / 158.08856` |
| `haul` | 43.621321 | `(usine 4,501.1729 + marché 2,131.4404 + fardier 98.7820 + déchargement 164.6366) / 158.08856` |
| `overhead` | 4.373964 | `(administration 576.2281 + mesurage 115.2456) / 158.08856` |

The residual is **86.461404 CAD/m3**, matching the MERIS
`Benefice_Net_m3_net = 86.4614`. This is a useful proof that the component
mapping is internally consistent, but it is a **shipped demo**, not a Quebec
stand or sale. Do not use it for policy or calibration.

## 4. Explicit gaps

`gaps.csv` is authoritative. The main ones:

| ID | Gap |
|---|---|
| G01 | No observed delivered log price. `tbl_essences_revenus_EssDhp` is all 0.0100. |
| G02 | Ledger has no quality dimension; QC F1–F4/AUTRE collide in the 9-field key. |
| G03 | Harvest cost is an equation requiring m3/tige, cutting mode and stand type. |
| G04 | 19 treatment rates are per 1,000 plants; 1 is per 1,000 microsites. |
| G05 | Tertiary road is CAD/ha; the ledger only permits CAD/ha for silviculture. |
| G06 | 191 tarification zones are not UAs; no UA/region crosswalk in the DB. |
| G07 | No actual permit volumes: `tbl_Volume_Prescription` is empty. |
| G08 | Current rates are 2025 nominal; economic values are $2023. |
| G09 | `Bnf`, `Rsl`, `Aut1` are factor incomes/adjustments, not ledger components. |
| G10 | `tbl_couts_zones` has no date field; cost year is not stated. |
| G11 | `mdb-schema` cannot dump ACCDB types. |
| G12 | `tbl_essences_revenus_EssDhp` is a placeholder, not a price table. |
| G13 | `admin_dol_m3` is operator administration, not Crown `admin_fee`. |
| G14 | Sample covers one zone; no coverage share. |

## 5. Access-UI path (not needed)

Table extraction did **not** require the Access UI. `MERIS.accdr` is the
compiled front-end; on Linux it would need Windows/Access 2016 runtime under
Wine or a Windows VM. The smallest fallback would be a Windows VM with the
Access runtime, open `MERIS_BdTbl.accdb`, and export the four economic reports
to CSV. The XLSX template only contains input sheets (`Tbl_Peup_Gen_0`,
`Tbl_Peup_Gen_Scenarios`, `tbl_Liste_Traitements`,
`Tbl_Peup_Gen_Scenarios_Action`, `Tbl_Peup_Detail_Scenarios`); it does not
contain cost/revenue values beyond the treatment catalogue. The XLSM
`Conversion-Redevances.xlsm` is the useful non-Access artifact: it contains the
Q3 2025 raw VMBSP and the quality crosswalk.

## 6. Reproduce

```bash
mkdir -p /tmp/meris && cd /tmp/meris
curl -sSLO https://encheres.forets.gouv.qc.ca/media/29260/meris.zip
unzip -o meris.zip -d extracted
mdb-tables -1 extracted/MERIS_BdTbl.accdb > tables_all.txt
mdb-count  extracted/MERIS_BdTbl.accdb tbl_redevances_F1234
mdb-export extracted/MERIS_BdTbl.accdb tbl_redevances_F1234 > redevances.csv
```

`extraction_commands.sh` records the exact commands. The sample CSVs were
selected from those exports; no database write occurred.
