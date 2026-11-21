# Provenance — Quebec MRNF 2022 forest cost/revenue survey

## Scope

This dataset republishes observed, aggregated results from the Quebec
Ministère des Ressources naturelles et des Forêts (MRNF) / Bureau de mise en
marché des bois (BMMB) 2022 survey of forest procurement, transformation, and
revenue. The observations are survey aggregates. They are **not** mill-level
records and they are **not** model output.

The extraction is stand-alone. It does not modify
`data/derived/national/harvest_basis/forest_cost_revenue/` or any ledger code.

## Public source page

Landing page (accessed 2026-11-21):

https://www.quebec.ca/agriculture-environnement-et-ressources-naturelles/forets/entreprises-industrie/publications-statistiques-industrie-forestiere/etudes-statistiques-produits-forestiers

The PDFs are public downloads from `cdn-contenu.quebec.ca`. No authentication,
paywall, cookie, or access-control bypass was used.

## Files retrieved

| ID | File | URL | Retrieved (UTC) | Bytes | SHA-256 | Pages |
|---|---|---|---|---:|---|---:|
| `main_2022` | `RA_couts_approvisionnement_transformation_revenus_2022.pdf` | https://cdn-contenu.quebec.ca/cdn-contenu/forets/documents/entreprises/statistiques/RA_couts_approvisionnement_transformation_revenus_2022.pdf | 2026-11-21T20:33:38Z | 1,248,519 | `d9971b8228bf10159f2536d1f7690f7e84b833106c63e5fd9bad1014fb6b6871` | 61 |
| `regional_2022` | `Compilation_donnees_regionalisees_2022.pdf` | https://cdn-contenu.quebec.ca/cdn-contenu/forets/documents/entreprises/statistiques/Compilation_donnees_regionalisees_2022.pdf | 2026-11-21T20:33:38Z | 695,116 | `5263e2c3af94b6cdd656826323ea21baced6d226429d2a9c297ebbe047021139` | 1 |
| `survey_2019` | `RA_enquete_couts_operation_2019.pdf` | https://cdn-contenu.quebec.ca/cdn-contenu/forets/documents/entreprises/statistiques/RA_enquete_couts_operation_2019.pdf | 2026-11-21T20:33:39Z | 2,853,156 | `870090018a51d12b0c78adb67741eb10c524fc5d5aafc4dce96d101612dc6a1f` | 64 |
| `regional_2019` | `Compilation_donnees_regionalisees_2019.pdf` | https://cdn-contenu.quebec.ca/cdn-contenu/forets/documents/entreprises/statistiques/Compilation_donnees_regionalisees_2019.pdf | 2026-11-21T20:33:39Z | 187,301 | `dc13bfd249046d6accdc80aace0e90e6850a682394c96bd55e38c423acb44118` | 3 |
| `sylviculture_public_2021_2022` | `RA_couts_sylviculture_foret-publique_2021-2022.pdf` | https://cdn-contenu.quebec.ca/cdn-contenu/forets/documents/entreprises/statistiques/RA_couts_sylviculture_foret-publique_2021-2022.pdf | 2026-11-21T20:33:40Z | 4,177,901 | `743b71b52725762040139391d987f99b3c21cc70159a61af5faf560216101a3a` | 138 |
| `sylviculture_private_2021_2022` | `RA_couts_sylviculture_foret-privee_2021-2022.pdf` | https://cdn-contenu.quebec.ca/cdn-contenu/forets/documents/entreprises/statistiques/RA_couts_sylviculture_foret-privee_2021-2022.pdf | 2026-11-21T20:33:41Z | 2,115,377 | `50c378e3538aeb2408adea1c9504ee7fb83c66b18a54fbaa6ca795ca5ff9d90b` | 59 |

PDFs are retained locally under `tmp/qc_cost_survey/pdf/` for reproducibility
but are not committed. The hash is the identity check; the extractor refuses to
run if a local PDF does not match the recorded SHA-256.

## Source metadata notes

- `main_2022` title page: *Enquête quinquennale sur les coûts
  d'approvisionnement, de transformation et les revenus de l'industrie
  forestière 2022*, dated September 2025. Reference period: enterprise fiscal
  years ending no later than 2023-03-31, mostly calendar 2022.
- `regional_2022` title: *Compilation des données régionalisées du regroupement
  des essences résineuses sapin, épinettes, pin gris et mélèzes*, November 2025.
  It regionalises SEPM only; hardwoods and poplars are withheld because of the
  small number of respondents.
- `sylviculture_public_2021_2022` is titled *Enquête sur les coûts de la
  sylviculture en forêt publique pour la saison 2020-2021* despite the
  `2021-2022` filename. Its own title page is authoritative.
- `regional_2019` page 1-3 tables are raster images with no text layer.
  `pdftotext -layout` and pdfplumber return captions only. They were not OCRed
  and contribute no rows.

## Table inventory

`source_page` in the CSV is the printed page number for the body of the 2022
report. The PDF page is six higher for body pages (printed p. 12 = PDF p. 18).
Table A2 is on PDF page 37 (Annex 2, printed p. 3). The regional compilation is
PDF page 1.

| Table | Printed page | PDF page | Content | Status |
|---|---:|---:|---|---|
| 2 | 12 | 18 | Delivered wood purchase cost by species/use | parsed |
| 3 | 13 | 19 | Harvest cost components | parsed |
| 4 | 13 | 19 | Harvest physical parameters | parsed |
| 5 | 14 | 20 | Forest road cost components | parsed |
| 6 | 15 | 21 | Wood haul cost components | parsed |
| 7 | 15 | 21 | Haul mode shares and distances | parsed |
| 8 | 16 | 22 | Hosting / remoteness cost | parsed |
| 9 | 16 | 22 | Other procurement costs | parsed |
| 10 | 17 | 23 | Transfers to the State | parsed |
| 11 | 18 | 24 | Sawmill transformation costs | parsed |
| 12 | 18 | 24 | Sawing recovery | parsed |
| 13 | 19 | 25 | Finished-product transport | parsed |
| 14 | 19 | 25 | Overhead | parsed |
| 15 | 20 | 26 | SEPM gross lumber revenue by quarter | parsed |
| 16 | 20 | 26 | SEPM gross and net revenue | parsed |
| 17 | 21 | 27 | Hardwood and pine revenue | parsed |
| 18 | 21 | 27 | By-product revenue, $/tonne | parsed |
| 19 | 21 | 27 | By-product revenue, $/m3 | parsed |
| 20 | 22 | 28 | Procurement synthesis | parsed |
| 21 | 22 | 28 | Purchase versus BGAD supply synthesis | parsed |
| 22 | 23 | 29 | Revenue synthesis | parsed |
| A2 | Annex 2 p. 3 | 37 | 2014 / 2019 / 2022 comparison | parsed |
| Regional 1 | 1 | 1 | SEPM regional procurement costs | parsed |
| Regional 2019 tables 1-4 | 1-3 | 1-3 | 2019 regional results | not parsed, raster |
| 2019 report | — | — | Full 2019 survey | downloaded, not parsed |
| Silviculture public 2021-22 | — | — | Public-forest silviculture costs | downloaded, not parsed |
| Silviculture private 2021-22 | — | — | Private-forest silviculture costs | downloaded, not parsed |

## Extraction method

1. Download each PDF with `curl` and verify the SHA-256 before parsing.
2. Extract tables with `pdfplumber` (`page.find_tables()`), not by eyeballing
   text. `pdftotext -layout` was used as a cross-check for table context and
   captions.
3. Normalize French numbers: spaces and non-breaking spaces are thousands
   separators; comma is the decimal separator. `N.D.`, `N.A.`, and `S.O.` are
   missing/not-applicable; a dash is a confidentiality suppression unless the
   table says otherwise.
4. Detect red value cells directly from PDF character colour
   `(0.933, 0.0, 0.0)` and mark them `three_respondents`. This is how the
   report flags means based on exactly three respondents. The same flag is
   applied to every regional R09 row because its published `sample_n` is 3, and
   to the T20 peupliers-trituration rows because their basis is red-flagged in
   T3/T5/T10/T21 even though T20 prints the synthesis cells in black.
5. Map each row label and column to a canonical component, species group, and
   product/use. An unknown numeric row is a hard extraction failure.
6. Emit only numeric observations in the survey CSV. Suppressed and missing
   cells are counted in `qc_cost_revenue_coverage.csv`; no value is imputed.
7. Run additive reconciliation checks that the source actually supports
   (component sums to totals, regional subtotals, revenue synthesis) and eight
   direct page-value spot checks.
8. Write `manifest.json` last, including file hashes and validation results.

Parser: `scripts/national/extract_qc_cost_survey_2022.py`.

## Transformations and non-transformations

- Currency: all monetary values are nominal CAD of the survey year (2022 for
  the main and regional tables; 2014, 2019, or 2022 for Table A2 rows). No
  deflation, indexing, or exchange-rate conversion.
- Volume basis: `$/m3` is per cubic metre of merchantable wood as defined by the
  survey. Transformation costs use merchantable solid volume entering the mill.
  By-product `$/m3` uses merchant and non-merchant volume transformed, as stated
  in Table 19.
- Regional aggregation: seven regional groups plus the provincial total, exactly
  as published. No regional value is allocated to a mill or to a finer region.
- Species aggregation: provincial values by SEPM, feuillus durs (sciage /
  trituration), peupliers (sciage / trituration), pins, and thuyas where
  published. No species value is allocated from a broader group.
- Grade aggregation: the survey publishes `sciage`, `trituration`, and totals,
  plus a hardwood quality caveat. No grade-level price is invented.
- Table A2 2014 and 2019 values are earlier survey results reproduced for
  comparison, not re-estimated 2022 values.
- Table 11 drying costs by species are non-additive breakdown values. They are
  labelled `observation_kind=species_breakdown_non_additive` and must not be
  summed with the drying total.

## Accounting caveats for net-value comparison

- **Purchased-wood cost, not revenue.** `T2`/`T21` `Achats de bois (livré)`
  (`107.22 CAD/m3` SEPM) is the buyer-side procurement cost of public-forest
  wood. It includes the purchase, transfers to the State, transport and
  unloading, and road costs where applicable. It is not observed log-sale
  revenue and must not be presented as stumpage or forest-sector gross value.
  `T21` repeats the `T2` purchase values as a synthesis row; do not add them.
- **BGAD is a parallel channel.** `T20`'s `106.41 CAD/m3` SEPM is the BGAD
  supply channel. The `107.22 - 106.41 = 0.81 CAD/m3` difference is a
  procurement-channel cost spread across different respondent samples, not
  forest-sector net value. The hardwood sawlog and poplar trituration spreads
  (`-14.53` and `-9.45`) have the same interpretation.
- **PRCCM placement.** PRCCM road rebates are inside `T10`/`T20`
  `transfers_total` (SEPM `-1.06 = -0.69 - 0.33 - 0.04`). `T5`
  `road_total_after_prccm` (`15.52`) is net of PRCCM; `T20` road (`16.58`) is
  gross (`access_cost_gross`). Combining the after-PRCCM road total with
  `T10.transfers_total` (`25.01`) double counts the rebate.
- **Species gain/loss exclusion.** `T20` excludes species gain/loss by design.
  SEPM is `-2.75 CAD/m3`, hardwood sawlog `-1.85`, and poplar trituration
  `-6.80`. The items are carried in `T3` and `T22`; any comparison must state
  the exclusion.

## Confidentiality and aggregation

The source withholds cells with fewer than three respondents. It also prints
some means based on exactly three respondents in red; those are preserved but
flagged `three_respondents`. The survey is confidential at the respondent
level: the report states that no respondent can be identified from the
published tables. This dataset therefore contains no mill identifiers, no
respondent identifiers, and no values below the published regional/species
aggregation.

## Known source inconsistency

Table 14 (overhead), peupliers-sciage column, prints components 3.25, 12.28,
0.00, 0.00, -4.87 and a total of 13.87. The components sum to 10.66. Annex A1
prints 2.06, 16.51, 0.05, 0.12, -4.87 and total 13.87 for the same cells. The
body row appears to repeat pins-column values. The dataset keeps the body values
as printed and records the discrepancy as
`known_source_inconsistency` in the manifest; it does not adjust either table.

## Suppressed Table 19 components

Table 19 suppresses at least one by-product component: `Résidus de bois` for
SEPM and `Rabotures` plus `Résidus de bois` for feuillus durs. The printed
totals are retained, but the additive check is recorded as
`skipped_suppressed_component` rather than reconciled over a partial component
set. The skipped checks are listed in
`validation.reconciliation_skipped_suppressed` in `manifest.json`.

## Citation

Groupe DDM, 2025. *Enquête quinquennale sur les coûts d'approvisionnement, de
transformation et les revenus de l'industrie forestière en 2022.* Report to the
Ministère des Ressources naturelles et des Forêts, 23 p. and appendices.
Internal reference 23-1734.

Bureau de mise en marché des bois, 2025. *Compilation des données régionalisées
du regroupement des essences résineuses sapin, épinettes, pin gris et mélèzes.*
November 2025.
