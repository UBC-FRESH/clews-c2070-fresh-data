# MAGPlot Tier 1 measured tree lists - QC, NB, YT - v0

**Status:** measured open-data tree lists only. No bucking, no volume or
biomass model, no growth model, no official grade, and no provincial or
national supply claim. `measured_tree_list=true`, `open_data=true`,
`model_estimate=false`, `national_claim=false` on every row.

## Download and schema

| Field | Value |
|---|---|
| Dataset | MAGPlot v1.2 (package members dated 2026-02-26) |
| Publisher | Natural Resources Canada / Canadian Forest Service |
| Direct URL | https://ca.nfis.org/fss/fss?command=retrieveByName&fileName=MAGPlot_latest_data_package.zip&fileNameSpace=magplot&format=xml&promptToSave=true |
| Retrieved UTC | 2026-11-23T00:26:18Z |
| Bytes | 127,123,248 |
| SHA-256 | `270055bb9eeed6ccd6cbd75f6a2026b54e340c5a4938af18ad06e479792888db` |
| Licence | Open Government Licence - Canada |
| Access tier | Tier 1 open package |
| Archive | `data/raw/magplot/MAGPlot_latest_data_package.zip` |

The ZIP contains eight CSV tables plus one coordinate-type PDF. The
tables used here are `magp_sites`, `magp_site_sources`,
`magp_tree_header` and `magp_trees`. The full schema, source field and
nullability for every output column are in `schema.csv`.

Tier-1 selection is the source allowlist in the MAGPlot data dictionary:
`QC_PSP`, `NB_CLI` on public land and `YT_PSP`. `NFM_GP` records also
occur in the open ZIP but are excluded because the dictionary's Tier-1
list does not name that source. No Tier-2, Tier-3 or restricted source
was read. NB_CLI is the public-land subset published in the Tier-1
package; the package has no ownership field to re-test that condition.

## QC / NB / YT coverage

| Jurisdiction | Source | Sites | Plots | Latest tree rows | Included trees | Live standing | Species |
|---|---|---|---|---|---|---|---|
| NB | NB_CLI | 7609 | 14471 | 548511 | 548350 | 481480 | 52 |
| QC | QC_PSP | 12827 | 56143 | 748085 | 506367 | 436895 | 63 |
| YT | YT_PSP | 261 | 515 | 22003 | 17691 | 17482 | 10 |

Tree-list scope: latest measured visit per MAGPlot plot, large-tree
(`L`) and measured small-tree (`S1`) plots, positive DBH, positive
expansion and positive fixed-plot area. Regeneration (`R`) and `S2`
count-tree plots are excluded because they are tally/count layers
rather than individual measured stems; their counts remain in
`coverage.csv`. Trees with
non-positive DBH are excluded rather than patched.

| Jurisdiction | Included sites | Included plots | Excluded DBH | Excluded group | Height present | Unknown status |
|---|---:|---:|---:|---:|---:|---:|
| NB | 7,527 | 14,469 | 161 | 0 | 97,789 | 0 |
| QC | 12,495 | 22,997 | 52 | 241,666 | 96,809 | 12,530 |
| YT | 261 | 514 | 4,312 | 0 | 13,665 | 86 |

## Expansion and plot area

`plot_area_ha` is `meas_plot_size`; `expansion_factor_stems_ha` is the
source `stem_ha`. For fixed-area plots the source normally sets
`stem_ha = 1 / meas_plot_size`. The extract preserves the source
expansion and flags, rather than silently replacing, the small number of
rows where the two disagree by more than 1%:

| Jurisdiction | Mismatch rows | Min expansion | Max expansion | Min area | Max area |
|---|---:|---:|---:|---:|---:|
| NB | 128 | 25.00 | 200.00 | 0.005000 | 0.0400 |
| QC | 0 | 16.00 | 250.00 | 0.004000 | 0.0625 |
| YT | 0 | 25.00 | 25.00 | 0.040000 | 0.0400 |

## Compiled volume and biomass

MAGPlot v1.2 has **no compiled tree volume or biomass field**. All eight
table headers and the v1.2 data dictionary were scanned. The only
`volume` token is the disturbance `mortality_basis` code `VL` (volume),
which is not a tree-level volume. There is no `vmb_tige`, `vmb_ha`,
merchantable-volume, gross-volume, net-volume or biomass column in
`magp_trees.csv`. No volume or biomass is computed or imputed in this
product. The QC PEP comparison source likewise has `vmb_tige` and
`vmb_ha` columns, but both are null for all 2,210,417 PEP tree rows.

## QC MAGPlot / QC PEP overlap

QC_PSP `source_plot` is the PEP `id_pe`; MAGPlot `tree_num` is PEP
`no_arbre`; MAGPlot `meas_num + 1` is PEP `no_mes`. This supports a
direct record-level check, not just a name comparison.

| Metric | Value |
|---|---:|
| QC_PSP sites | 12,827 |
| PEP plots | 12,834 |
| Matched plots | 12,826 |
| MAGPlot-only plots | 1 |
| PEP-only plots | 8 |
| Matched plot share | 99.9922% |
| Matched visits | 50,962 |
| Matched visit-year mismatches | 10 |
| Matched tree measurements | 1,810,494 |
| DBH agreement within 0.1 cm | 99.9964% |
| Expansion exact match | 99.9908% |
| PEP `vmb_tige` non-null | 0 |
| PEP `vmb_ha` non-null | 0 |

The unmatched MAGPlot QC rows are overwhelmingly regeneration/small
count trees (`R1_I`, `S2_I`) that have no one-to-one PEP
`dendro_arbres` record. The matched tracked-tree population agrees on
DBH and expansion to within source rounding. Per-plot overlap is in
`qc_pep_overlap.csv`; all metrics are in `qc_pep_comparison.csv`.

## Sources and provenance

| Source | Licence | Tier | Retrieved UTC | SHA-256 |
|---|---|---|---|---|
| QC_PSP | Open Government Licence - Canada | 1 | 2026-11-23T00:26:18Z | 270055bb9eeed6ccd6cbd75f6a2026b54e340c5a4938af18ad06e479792888db |
| NB_CLI | Open Government Licence - Canada | 1 | 2026-11-23T00:26:18Z | 270055bb9eeed6ccd6cbd75f6a2026b54e340c5a4938af18ad06e479792888db |
| YT_PSP | Open Government Licence - Canada | 1 | 2026-11-23T00:26:18Z | 270055bb9eeed6ccd6cbd75f6a2026b54e340c5a4938af18ad06e479792888db |
| QC_PEP | CC BY 4.0 | 1 | 2026-11-14T17:34:19Z | a5deb82b8e05c3226f83eb8daa4842900b6564e31b30915d9215f8a031faa5e5 |

`sources.csv` records the full URL, retrieval time, bytes, SHA-256,
licence, Tier-1 basis, coordinate caveat and restrictions for MAGPlot
and the PEP comparison source. `manifest.json` hashes every artifact
and records the input package hash.

## Files

| File | Contents |
|---|---|
| `qc_tree_list.csv.gz` | Quebec MAGPlot Tier-1 measured tree list (gzip CSV) |
| `nb_tree_list.csv.gz` | New Brunswick MAGPlot Tier-1 measured tree list (gzip CSV) |
| `yt_tree_list.csv.gz` | Yukon MAGPlot Tier-1 measured tree list (gzip CSV) |
| `schema.csv` | Output column dictionary, units and constraints |
| `coverage.csv` | Source and included counts, exclusions and ranges |
| `sources.csv` | Licence, URL, timestamp, hash and Tier-1 basis |
| `qc_pep_overlap.csv` | Per-plot QC_PSP/PEP overlap |
| `qc_pep_comparison.csv` | QC/PEP overlap and schema-reconciliation metrics |
| `summary.json` | Machine-readable totals and checks |
| `report.md` | This report |
| `manifest.json` | Artifact hashes, input hashes and run metadata |

## Limitations

- Latest-visit selection keeps one measurement per plot, not a growth
  panel. Earlier visits remain in MAGPlot but are not in these lists.
- Heights are missing for many source trees; the extract leaves them
  empty. It does not impute height.
- NB_CLI coverage is the Tier-1 public-land subset in the open package.
  The package has no land-ownership field to verify public-land status
  independently.
- The MAGPlot dictionary is internally inconsistent about whether Tier-1
  coordinates are exact or approximate within +/-10 km. Coordinates are
  therefore carried only in the source tables, not in these tree lists.
- No compiled volume or biomass exists in MAGPlot v1.2. Any later
  bucking or biomass layer must be labelled as a model estimate and
  must not be presented as observed mill or inventory volume.
