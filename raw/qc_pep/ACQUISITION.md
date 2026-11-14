# Québec PEP (Placettes-échantillons permanentes) — Acquisition Record — 2026-11-14

## Identity

| Field | Value |
|-------|-------|
| Publisher | Ministère des Ressources naturelles et des Forêts du Québec (MRNF), Direction des inventaires forestiers (DIF) |
| Dataset | Placettes-échantillons permanentes, 1970 à aujourd'hui |
| Données Québec record | `placettes-echantillons-permanentes-1970-a-aujourd-hui` (package `adb12ba6-4e55-4e4a-8a63-235c48be7865`) |
| Resource | `Placette-échantillon permanente` (resource `72828f8a-d008-4119-b246-89e6103120cb`, format GPKG) |
| Catalogue URL | https://www.donneesquebec.ca/recherche/dataset/placettes-echantillons-permanentes-1970-a-aujourd-hui |
| Direct URL | https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Placettes_permanentes/02-Donnees/PROV/PEP_GPKG.zip |
| Licence | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| Coverage | Québec méridional; all PEP networks (`BAS1`, `BAS2`, `SPIM`, `FEDE`, `UNLA`, `SCOF`, `PACA`) |
| Temporal coverage | 1970–2025 |
| Format | Esri GeoPackage (`PEP.gpkg`) inside a ZIP; 46 SQLite tables, of which 24 are feature classes or attribute layers |
| Access tier | Tier 1 open download; no credentials, request form, or DSA |
| Acquisition date | 2026-11-14 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |

CKAN metadata observed 2026-11-14: `metadata_modified`
2026-11-11T19:53:33Z; resource `last_modified` 2026-06-19T12:00:00. The
package-show snapshot is archived as `donnees_quebec_package_show.json`.

## Retrieval

The server returns HTTP 404 to `HEAD`/`curl -I` but HTTP 200 to `GET`. The
download used `GET`:

```bash
curl -sS -L --retry 3 \
  -o PEP_GPKG.zip \
  'https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Placettes_permanentes/02-Donnees/PROV/PEP_GPKG.zip'
```

Response: HTTP 200, 128,568,617 bytes. ZIP integrity passes
(`ZipFile.testzip()` returns `None`); the archive contains one member,
`PEP.gpkg`, 739,045,376 bytes uncompressed.

| File | Bytes | SHA-256 |
|------|------:|---------|
| `PEP_GPKG.zip` | 128,568,617 | `a5deb82b8e05c3226f83eb8daa4842900b6564e31b30915d9215f8a031faa5e5` |
| `PEP.gpkg` (member) | 739,045,376 | `6d53e90a23799d681d050e13a433bc6e7ede6549b0733c8cc9c01fc8f94348c9` |

Documentation archived beside the payload:

| File | Bytes | SHA-256 |
|------|------:|---------|
| `LISEZ-MOI_pep.pdf` (27 pp., June 2026) | 1,316,492 | `9f849f0fadf879940d8fd5b4b4e032807e36745b94361b4f7888a9df6a7177c6` |
| `DICTIONNAIRE_PLACETTE.xlsx` (92 code sheets) | 2,183,559 | `ef526a8159a5752d1130a36c7aa3d1cc1692a444c8d241e3c6bd96a1b6a28a7d` |
| `donnees_quebec_package_show.json` | 25,236 | `790e054834e280a17fb2a10d7418a44a2c1b871b6422fc47b9de248c5f4c0113` |

## What the package contains

`PEP.gpkg` is the complete provincial PEP relational database. The core
measurement chain is:

- `placette` — one row per plot (12,834), point geometry, `id_pe`, network,
  map sheet, latitude/longitude, establishment and last-measurement fields.
- `placette_mes` — one row per plot visit (53,632), keyed by `id_pe_mes`,
  with `no_mes`, plot dimension code, and `date_sond`.
- `dendro_arbres` — one row per tree measurement (2,210,417), keyed by
  `id_arb_mes`; persistent tree identity is `id_arbre`. Live/dead `etat`,
  species `essence`, DBH in millimetres `dhp`, total height `hauteurdef`,
  diameter at commercial height `dic`/`hauteurdic`, and per-tree expansion
  and basal area `tige_ha`/`st_ha`.
- `dendro_arbres_etudes` — the intensively measured subsample (442,560 rows,
  193,463 unique trees): total height `haut_arbre`, age `age`,
  `age_sansop`, `source_age`, and age-core reading height `nivlectage`.
- `dendro_gaules` — sapling tally by DBH class (235,455 rows; classes 2, 4,
  6, 8 cm), with `nb_tige`, `tige_ha`, and `st_ha`.
- `station_pe` — one station description per visit (53,632), including
  origin, disturbance, cover, age class, dominant height, potential
  vegetation, and ecological type.
- `classi_eco_pe` — one ecological classification per plot (12,834).
- Supporting tables: `pee_ori_sond`, `pee_essence_ori_sond`,
  `pee_etage_ori_sond`, `meta_notes_pe`, `station_sol`, `station_essence`,
  `station_etage`, `station_semis`, `station_semis_nco`,
  `station_debris_4`, `station_debris_5`, `plan_descr_type_pe`,
  `plan_reseau`, `plan_composante_factexp_region`, and three polygon
  region layers.

Detailed counts and profiling are in `CONTENTS.md`.

## Method notes and limitations

- The database is a **multi-network** sample. Only `BAS1` is representative
  of the covered forest area, and `BAS2` is incomplete; `SPIM`, `FEDE`,
  `UNLA`, `SCOF`, and `PACA` are targeted networks with unequal sampling
  weights (`LISEZ-MOI_pep.pdf`; `plan_reseau`). Do not pool networks without
  design weights.
- PEP plots are **fixed-area circular** designs (4, 40, 400, and 625 m²;
  expansion factors 2,500, 250, 25, and 16 stems/ha). There is no BAF.
  `dendro_arbres.tige_ha` already carries the per-tree expansion; plot area
  is recoverable from `plan_descr_type_pe` and `placette_mes.dimension`.
- Tree identity persists through `id_arbre` across visits; `id_arb_mes` is
  unique per measurement. 683,328 of 843,175 trees (81.0%) appear in more
  than one visit.
- Height is measured on the study-tree subsample, not every tally tree:
  372,225 of 442,560 study rows (84.1%) carry `haut_arbre`, covering
  193,420 of 193,463 study trees. Only 43,559 tally rows (2.0%) carry
  `hauteurdef`.
- DBH is in millimetres. Live tally DBH ranges 77–1,089 mm with a median of
  136 mm. Dead, removed, and regeneration rows can carry 0 or missing DBH;
  filter on `etat` before diameter analysis.
- There is **no explicit site-index column**. Age (157,394 trees), dominant
  height (`station_pe.haut_domi`, 11,247 visits), age class
  (`station_pe.cl_age`, 35,613 visits), and ecological type
  (`station_pe.type_eco`, 29,627 visits; `classi_eco_pe`, all 12,834 plots)
  are the available productivity inputs. Site index must be derived.
- `classi_eco_pe.eta_veg` is populated for 5,257 plots (41.0%);
  `zone_veg`, `dom_bio`, and `reg_eco` are populated for all 12,834.
- The live WFS/portal resource can change without a version number. Re-run
  the CKAN query and re-hash before reuse.

## Cleaner access path (optional, not vendored)

The CFS Canadian Wood Fibre Centre publishes two R packages that clean and
intervalize this same source:

- `CWFC-CCFB/QcPSP` (LGPL-3.0): restores six tables — `QcMeasurementIndex`,
  `QcPlotIndex`, `QcTreeIndex`, `QcTreeMeasurements`,
  `QcSaplingMeasurements`, and `QcSBWDefoliation` (spruce budworm
  defoliation).
- `CWFC-CCFB/QcPSPIntervals` (LGPL-3.0): adds non-overlapping growth
  intervals, harvested-tree counts, species grouping, and climate variables.

These packages are a convenient harmonized view, not the archival source.
The source archive here remains the authoritative CC BY 4.0 MRNF product.
Neither package is vendored in this repository.

## Citation

Ministère des Ressources naturelles et des Forêts du Québec, Direction des
inventaires forestiers. 2026. *Placettes-échantillons permanentes, 1970 à
aujourd'hui* [database]. Données Québec.
https://www.donneesquebec.ca/recherche/dataset/placettes-echantillons-permanentes-1970-a-aujourd-hui
(accessed 2026-11-14). Licence CC BY 4.0.
