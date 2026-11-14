# MAGPlot v1.2 — Acquisition Record — 2026-11-14

## Identity

| Field | Value |
|-------|-------|
| Publisher | National Forest Inventory Canada / Natural Resources Canada |
| Title | Multi-Agency Ground Plot (MAGPlot) Database — Tree Measurements & Sites Summary |
| Version | MAGPlot v1.2 (data package member timestamps 2026-02-26; data dictionary v1.2 dated 2026) |
| Open Canada record | https://open.canada.ca/data/en/dataset/8824392d-464e-413d-8bde-eaed61c79743 |
| Related Open Canada record | https://open.canada.ca/data/en/dataset/1a73441d-cbe9-485b-bc91-84e07f97193f (same ZIP resources; older WMS view) |
| Licence | Open Government Licence — Canada (`ca-ogl-lgo`), https://open.canada.ca/en/open-government-licence-canada |
| Access tier | Tier 1 open-sharing package. Published coordinates are approximate (within ±10 km); exact locations require the NFI Data Request Form and jurisdictional approvals. |
| Acquisition date | 2026-11-14 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | Pan-Canadian compilation; this package contains 8 provinces/territories (BC, QC, NB, NL, YT, NT, SK, MB) |
| Format | ZIP archive containing 8 CSV tables + 1 PDF |
| CRS / coordinates | Decimal degrees (latitude/longitude); no CRS statement in the package. Published coordinates are approximate. |

## Source URLs and HTTP responses

HEAD probes run 2026-11-14 17:34 UTC. All three payload URLs returned HTTP 200 with the expected content types; no HTML/XML error response was accepted.

| Requested file | URL | HTTP | Content-Type | Content-Length (bytes) |
|----------------|-----|-----:|--------------|----------------------:|
| `MAGPlot_latest_data_package.zip` | `https://ca.nfis.org/fss/fss?command=retrieveByName&fileName=MAGPlot_latest_data_package.zip&fileNameSpace=magplot&format=xml&promptToSave=true` | 200 | `application/x-zip-compressed` | 127,123,248 |
| `MAGPlot_DB_Data_Dictionary_En.pdf` | `https://ca.nfis.org/fss/fss?command=retrieveByName&fileName=MAGPlot_DB_Data_Dictionary_En.pdf&fileNameSpace=magplot&format=xml&promptToSave=true` | 200 | `application/pdf` | 933,385 |
| `MAGPlot_Supplementary_Material.zip` | `https://ca.nfis.org/fss/fss?command=retrieveByName&fileName=MAGPlot_Supplementary_Material.zip&fileNameSpace=magplot&format=xml&promptToSave=true` | 200 | `application/x-zip-compressed` | 288,487 |

Raw HEAD transcripts are retained as `*.head.txt` in this directory. `Set-Cookie` response headers were removed before archiving; they carried only an anonymous session identifier.

## Retrieved files

| Local filename | Bytes | SHA-256 | Status |
|----------------|------:|---------|--------|
| `MAGPlot_latest_data_package.zip` | 127,123,248 | `270055bb9eeed6ccd6cbd75f6a2026b54e340c5a4938af18ad06e479792888db` | downloaded, ZIP integrity verified |
| `MAGPlot_DB_Data_Dictionary_En.pdf` | 933,385 | `36915d70fbac64a2d2b07272e0eabbb3c4dddbe36ea81a839e240e8df8666525` | downloaded, PDF version 1.6, 44 pages |
| `MAGPlot_Supplementary_Material.zip` | 288,487 | `11d4f3ab4151d41f352e6fe071fe2196d61d0a61bd6a9db55f5bf8714ea8147a` | downloaded, ZIP integrity verified |
| `open_canada_record_8824392d.json` | 32,839 | `a5b07a533f604f217593e9e6742291c5c400a083cdf03a5cb40bc16bcfa5a4fc` | CKAN metadata snapshot, HTTP 200 |

Retrieval timestamp recorded at `acquired_at_utc.txt`: `2026-11-14T17:34:19Z`.

## Prior scratch copy comparison

A scratch copy existed at `tmp/magplot_triage/MAGPlot_latest_data_package.zip` (2,957,065 bytes, SHA-256 `df55c5c961123363736044572a30ec73ecf350abac31a6c9fe7011d12973cafe`). It is **not** the current package and was not used: the fresh download is 127,123,248 bytes with SHA-256 `270055bb…`. The scratch data dictionary PDF is byte-identical to the fresh copy (SHA-256 `36915d70…`).

## Validation

```text
unzip -t MAGPlot_latest_data_package.zip  -> exit 0, "No errors detected"
archive members                          -> 9 files (8 CSV + 1 PDF)
compressed size                          -> 127,123,248 bytes
uncompressed size                        -> 1,720,730,897 bytes
```

```text
unzip -t MAGPlot_Supplementary_Material.zip -> exit 0, "No errors detected"
archive members                             -> 7 members (1 directory + 4 XLSX + 2 TXT)
uncompressed size                           -> 315,537 bytes
```

## Contents summary

The data package contains exactly the eight MAGPlot tables named in the source review, with `.csv` extensions, plus a coordinate-type note PDF:

| File | Uncompressed bytes | Rows (excl. header) | Columns |
|------|-------------------:|--------------------:|--------:|
| `magp_sites.csv` | 2,652,652 | 39,130 | 10 |
| `magp_site_sources.csv` | 1,289,533 | 39,130 | 3 |
| `magp_tree_header.csv` | 15,306,234 | 257,031 | 10 |
| `magp_trees.csv` | 1,588,811,499 | 7,771,041 | 29 |
| `magp_tree_condition.csv` | 86,992,072 | 1,383,908 | 11 |
| `magp_tree_removed.csv` | 24,051,724 | 382,012 | 9 |
| `magp_treatment.csv` | 967,512 | 14,362 | 6 |
| `magp_disturbance.csv` | 512,954 | 5,378 | 8 |
| `v1.2_FGP_magp_sites_coordinate_type_by_source.pdf` | 146,717 | — | — |

Detailed profiling is in `MAGPlot_CONTENTS.md`.

## Known limitations

- **Tier-1 only.** The open package is dominated by BC and QC and contains no Alberta, Ontario, Prince Edward Island, or Nova Scotia records. National calibration requires the NFI Data Request Form / DUA and provincial agreements.
- **Approximate coordinates.** All published coordinates are approximate within ±10 km; 1,027 BC sites have `latitude = -1` / `longitude = -1` (`flag_sites = 1`) because BC declined to publish even approximate coordinates. Exact locations require a request.
- **No age, site-index, soil, or ecological tables in v1.2.** The data dictionary states these are intended for a future version. This constrains height-growth and site-productivity calibration.
- **Variable-radius plots lack plot area/BAF.** `MEAS_PLOT_SIZE = -9` for all V1 and B1 plot types (29,169 tree-header rows; BC VRI/SUP/VLT only). No PHF, BAF, or explicit expansion-factor field is present; `STEM_HA` is the supplied per-hectare expansion for fixed-area plots.
- **Height is incomplete.** Height is present for 4,716,644 of 7,771,041 tree measurements (60.7%); live-standing trees are better covered (72.6%) than dead or unknown-status trees.
- **Tree identity is conditional.** `TREE_NUM < 8,000,000` denotes tracked trees that persist across measurements; 8M-series regeneration and 9M-series small/duplicate records are untracked and cannot be paired individually.
- **Data-quality flags.** DBH has 272 records >200 cm (max 450 cm) and `STEM_HA` has 11,991 records >1,000 stems/ha (max 18,444), mostly small-subplot scaling. These require QA before calibration.
- **In-place package name.** The download filename is `MAGPlot_latest_data_package.zip` and carries no version token; the version is established from the data dictionary and member timestamps. Re-download and re-hash before reuse.

## Reproduction

```bash
mkdir -p data/raw/magplot
cd data/raw/magplot
curl -fL --retry 3 -o MAGPlot_latest_data_package.zip \
  'https://ca.nfis.org/fss/fss?command=retrieveByName&fileName=MAGPlot_latest_data_package.zip&fileNameSpace=magplot&format=xml&promptToSave=true'
curl -fL --retry 3 -o MAGPlot_DB_Data_Dictionary_En.pdf \
  'https://ca.nfis.org/fss/fss?command=retrieveByName&fileName=MAGPlot_DB_Data_Dictionary_En.pdf&fileNameSpace=magplot&format=xml&promptToSave=true'
curl -fL --retry 3 -o MAGPlot_Supplementary_Material.zip \
  'https://ca.nfis.org/fss/fss?command=retrieveByName&fileName=MAGPlot_Supplementary_Material.zip&fileNameSpace=magplot&format=xml&promptToSave=true'
sha256sum MAGPlot_latest_data_package.zip MAGPlot_DB_Data_Dictionary_En.pdf MAGPlot_Supplementary_Material.zip
unzip -t MAGPlot_latest_data_package.zip
```

## Citation

National Forest Inventory. 2026. Multi-agency Ground Plot (MAGPlot) database — standards for forest ground plot data harmonization, version 1.2. Available from the MAGPlot FGP page (accessed 2026-11-14).

Araya, Y. H., Shay, P. E., Gamal El-Dien, O., Ratcliffe, B., Green, F., Thompson, M., Stinson, G., and Smiley, B. 2026. The Multi-Agency Ground Plot database: a repository for pan-Canadian forest ground plot data. Canadian Journal of Forest Research. https://doi.org/10.1139/cjfr-2025-0256
