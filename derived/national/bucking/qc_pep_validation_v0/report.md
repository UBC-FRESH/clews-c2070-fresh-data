# Quebec PEP measured-tree bucking validation v0

**Status:** model validation only.  Tree geometry is measured open data; every
log, residue, volume and value row is a model estimate.  `observed=false`,
`policy_grade=false`, `national_claim=false`.  This is not a provincial
inventory, an official Quebec grade, or a national supply estimate.

## Download/schema

| Field | Value |
|---|---|
| Dataset | placettes-echantillons-permanentes-1970-a-aujourd-hui |
| Publisher | Ministere des Ressources naturelles et des Forets du Quebec (MRNF), Direction des inventaires forestiers |
| Catalogue | https://www.donneesquebec.ca/recherche/dataset/placettes-echantillons-permanentes-1970-a-aujourd-hui |
| Direct URL | https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Placettes_permanentes/02-Donnees/PROV/PEP_GPKG.zip |
| Retrieval UTC | 2026-11-23T00:24:03Z |
| Licence | CC BY 4.0 |
| ZIP bytes / SHA-256 | 128,568,617 / `a5deb82b8e05c3226f83eb8daa4842900b6564e31b30915d9215f8a031faa5e5` |
| GPKG member / bytes / SHA-256 | `PEP.gpkg` / 739,045,376 / `6d53e90a23799d681d050e13a433bc6e7ede6549b0733c8cc9c01fc8f94348c9` |
| ZIP hash matches acquisition record | True |
| GPKG hash matches acquisition record | True |

PEP tables inspected: 46.  Core measurement chain:
12,834 plots, 53,632 visits,
2,210,417 tree measurements, and
442,560 intensive-study rows.

| PEP field | Use |
|---|---|
| `dendro_arbres.dhp` | DBH in millimetres; converted to centimetres. |
| `dendro_arbres_etudes.haut_arbre` | Total tree height in decimetres; converted to metres. |
| `dendro_arbres.hauteurdef` | **Defect height, not total height**; not used. |
| `dendro_arbres.tige_ha` | Stems-per-hectare expansion; inclusion area = `1/tige_ha`. |
| `dendro_arbres.etat` | Live codes 10, 12, 30, 40, 42, 50, 52, 58. |
| `dendro_arbres.essence` | Species code; only the published Schneider taper species are used. |
| `dendro_arbres.vmb_tige`, `vmb_ha` | Compiled gross merchantable volume fields; present but null for all 2,210,417 tree rows. |

The full PEP tree table has 0 non-null
`vmb_tige` values and 0 non-null
`vmb_ha` values.  There is no PEP biomass field in the tree table.

## Sample

Selection is deterministic and recent, not random: Latest eligible visit per PEP plot (exclude visit status AB, DE, NT), ordered by measurement date descending and id_pe ascending; first 1000 plots; every eligible tree in those plots; deterministic hash cap at 12000 trees if needed.
The sample contains **1,000 plots / visits and
7,767 trees**, measured 2024-06-28 to
2025-10-02.  8 species with a
published Schneider taper are included.  Trees outside the taper domain
(DBH 5-100 cm,
height 5-40 m)
are excluded rather than extrapolated.  Plot design counts:
`20`=7,767;
network tree counts:
`BAS1`=3,552, `BAS2`=3,626, `SCOF`=165, `SPIM`=424.

| stage | count |
| --- | --- |
| Latest-visit trees in PEP | 616792 |
| Live trees | 432853 |
| Live, positive DBH and expansion | 432852 |
| Live, species identified | 432852 |
| Live, measured height | 95274 |
| Live, height in taper domain | 95221 |
| Live, species with Schneider taper | 66359 |
| Candidate trees in taper DBH domain | 66359 |
| Candidate plots | 9545 |
| Selected plots | 1000 |
| Selected trees | 7767 |

The sample is **not** a provincial inventory estimate.  It over-represents
recently remeasured networks and the eight species with a published Quebec
taper; the many PEP species without a taper row are excluded.  `defect_pct`
is set to zero because PEP records defect type codes but not per-tree defect
severity; dimension-only sorting does not use defect severity, but net volume
would be overstated for defective stems if interpreted as a merchantable
recovery estimate.

## Logs/residue

The Schneider (2013) fixed-effect tree taper is integrated inside bark from
the 0.3 m stump to total height.  The existing Quebec pilot
dimension-only sort set is used: sawlog top diameters 24/20/16 cm and
pulpwood 10 cm, with the pilot lengths and prices.  `grade=not_assigned` and
`policy_grade=false`; the sort set is a dimension contract, not an official
Quebec grade.

| Metric | Value |
|---|---:|
| Trees bucked | 7,767 |
| Trees with at least one log | 5,873 |
| Trees with no merchantable log | 1,894 |
| Logs | 12,599 |
| Taper total (inside bark) | 1,070.51 m3 |
| Recovered gross logs | 852.01 m3 |
| Recovered net logs | 852.01 m3 |
| Stem residue | 218.49 m3 |
| Residue | 88.71 ODT |
| Sawlog share of recovered | 49.8% |
| Pulpwood share of recovered | 50.2% |
| Mean taper total per tree | 0.1378 m3 |
| Mean taper total per ha | 25.80 m3/ha |
| Mean residue per ha | 5.44 m3/ha |
| Mean residue | 2.21 ODT/ha |
| Balance error | 2.274e-13 m3 |

Per-tree residue is `taper total - recovered gross logs`; it includes the
stump section above 0.3 m, top, and unmerchantable sections.
Density, moisture, chip and hog fractions are planning assumptions:
basic density from the national pilot species table, 45%
wet-basis moisture, 85% chip yield and 10% hog yield.  Volume below the
0.3 m taper base is outside the taper total.  Bark is not
modelled: the taper is inside bark.

Species summary:

| species | common | trees | plots | mean DBH cm | mean H m | taper m3 | logs m3 | residue m3 | mean taper m3/ha |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BOP | paper birch | 508 | 176 | 14.32 | 12.01 | 51.85 | 37.91 | 13.94 | 1.28 |
| EPB | white spruce | 220 | 114 | 21.78 | 13.25 | 62.91 | 58.35 | 4.56 | 1.33 |
| EPN | black spruce | 5157 | 820 | 15.60 | 12.64 | 647.50 | 497.16 | 150.34 | 16.05 |
| EPR | red spruce | 7 | 4 | 12.90 | 11.14 | 0.60 | 0.44 | 0.16 | 0.02 |
| PEG | large-tooth aspen | 1 | 1 | 20.00 | 18.60 | 0.21 | 0.19 | 0.02 | 0.01 |
| PET | trembling aspen | 228 | 80 | 20.28 | 15.95 | 75.38 | 70.02 | 5.36 | 1.58 |
| SAB | balsam fir | 1617 | 370 | 16.45 | 12.09 | 226.16 | 182.63 | 43.53 | 5.41 |
| THO | eastern white cedar | 29 | 14 | 21.13 | 10.17 | 5.89 | 5.31 | 0.58 | 0.12 |

Product summary:

| product | sort | logs | trees | gross m3 | net m3 | value CAD |
| --- | --- | --- | --- | --- | --- | --- |
| pulpwood | P10L25 | 3725 | 2294 | 125.34 | 125.34 | 4,387.02 |
| pulpwood | P10L30 | 6424 | 4601 | 302.53 | 302.53 | 11,496.27 |
| sawlog | S16L365 | 812 | 808 | 82.77 | 82.77 | 5,793.95 |
| sawlog | S16L49 | 260 | 260 | 37.22 | 37.22 | 2,791.64 |
| sawlog | S16L55 | 652 | 651 | 115.47 | 115.47 | 9,237.33 |
| sawlog | S20L365 | 211 | 211 | 32.13 | 32.13 | 2,731.44 |
| sawlog | S20L49 | 86 | 86 | 18.63 | 18.63 | 1,676.64 |
| sawlog | S20L55 | 172 | 172 | 43.82 | 43.82 | 4,163.24 |
| sawlog | S24L365 | 65 | 65 | 13.95 | 13.95 | 1,395.45 |
| sawlog | S24L49 | 31 | 30 | 9.27 | 9.27 | 973.11 |
| sawlog | S24L55 | 161 | 138 | 70.87 | 70.87 | 7,795.51 |

The value column uses the Quebec pilot price deck (`QC-PILOT-2026`) carried by
the dimension-only sort rules.  Prices are planning assumptions, not observed
transactions; the deliverable's primary quantities are volume and residue.

## Comparison

PEP's compiled volume fields `vmb_tige` and `vmb_ha` are present in
`dendro_arbres` but have zero non-null values across the full
2,210,417-row tree table.  No PEP biomass field exists in
that table.  `dic` is a categorical code in this release, not a numeric
diameter, and `hauteurdic` is populated for only
127,194 rows; neither is a compiled
volume bank.  The comparison is therefore **taper total and residue only**;
there is no observed-versus-model volume comparison and no national claim.

| scope | species | trees | taper m3 | logs m3 | residue m3 |
| --- | --- | --- | --- | --- | --- |
| ALL | ALL | 7767 | 1,070.51 | 852.01 | 218.49 |
| species | BOP | 508 | 51.85 | 37.91 | 13.94 |
| species | EPB | 220 | 62.91 | 58.35 | 4.56 |
| species | EPN | 5157 | 647.50 | 497.16 | 150.34 |
| species | EPR | 7 | 0.60 | 0.44 | 0.16 |
| species | PEG | 1 | 0.21 | 0.19 | 0.02 |
| species | PET | 228 | 75.38 | 70.02 | 5.36 |
| species | SAB | 1617 | 226.16 | 182.63 | 43.53 |
| species | THO | 29 | 5.89 | 5.31 | 0.58 |

The per-ha columns are design-based means across the sampled plots, with
per-tree expansion by `tige_ha`; they are not a provincial total.

## Tests/commits/status

All internal checks passed before artifacts were written:

| name | passed | detail |
| --- | --- | --- |
| schema_columns | True | tree_missing=[], log_missing=[], residue_missing=[] |
| unique_tree_ids | True | trees=7767, unique=7767 |
| residue_covers_every_tree | True | residue=7767, trees=7767 |
| logs_are_subset_of_trees | True | log_trees=5873 |
| expansion_identity | True | max \|expansion * inclusion_area - 1\| = 0.000e+00 |
| tree_volume_residue_balance | True | max tree balance error = 2.220e-16 m3 |
| residue_ledger_balance | True | max ledger balance error = 6.939e-18 m3 |
| log_sum_matches_tree_recovered | True | max \|sum logs - recovered\| = 0.000e+00 m3 |
| plot_summary_reconciles | True | max errors={'n_trees': 0.0, 'taper_total_m3': 8.881784197001252e-16, 'recovered_gross_m3': 8.881784197001252e-16, 'residue_m3': 1.1102230246251565e-16, 'taper_total_m3_per_ha': 2.842170943040401e-14} |
| species_summary_reconciles | True | max errors={'n_trees': 0.0, 'taper_total_m3': 1.1368683772161603e-13, 'recovered_gross_m3': 5.684341886080802e-14, 'residue_m3': 0.0} |
| comparison_all_row | True | all_rows=1 |
| evidence_tiers | True | published_table taper; assumption logs/residue |
| no_policy_grade | True | grade=not_assigned and policy_grade=false |
| labels | True | {'measured_tree_list': True, 'open_data': True, 'model_estimate': True, 'observed': False, 'policy_grade': False, 'national_claim': False, 'synthetic': False} |
| tree_numeric_finite_non_negative | True | nan=0, negative=0, rows=7767 |
| log_numeric_finite_non_negative | True | nan=0, negative=0, rows=12599 |
| residue_numeric_finite_non_negative | True | nan=0, negative=0, rows=7767 |
| plot_numeric_finite_non_negative | True | nan=0, negative=0, rows=1000 |
| species_numeric_finite_non_negative | True | nan=0, negative=0, rows=8 |
| comparison_numeric_finite_non_negative | True | nan=0, negative=0, rows=9 |
| compiled_volume_fields_absent | True | no populated PEP vmb_tige/vmb_ha or biomass fields; taper-only comparison |
| no_national_claim | True | national_claim=false on every row |
| summary_counts | True | trees=7767, logs=12599, plots=1000 |

Unexpected git deletions: none.  The source ZIP and member hashes match the
recorded acquisition values.  The output directory is
`data/derived/national/bucking/qc_pep_validation_v0/`.  Commit hashes and push
status are recorded in the final handoff after the data and parent commits.
