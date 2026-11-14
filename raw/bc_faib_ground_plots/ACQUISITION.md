# BC FAIB Ground Plot Compilations (PSP + non-PSP) — Acquisition Record — 2026-11-14

## Identity

| Field | Value |
|-------|-------|
| Publisher | BC Ministry of Forests — Forest Analysis and Inventory Branch (FAIB) |
| Dataset | Forest Inventory Ground Plot Data and Interactive Map |
| BC Data Catalogue record | `824e684b-4114-4a05-a490-aa56332b57f4` |
| Catalogue URL | https://catalogue.data.gov.bc.ca/dataset/824e684b-4114-4a05-a490-aa56332b57f4 |
| Sub-corpus acquired | `psp/` (PSP compilations) and `non_psp/` (non-PSP compilations) |
| Compilation date | 2026-04-16/21 (dictionaries `PSP_data_dictionary_2026Apr20.xlsx` and `non_PSP_data_dictionary_2026Apr20.xlsx`) |
| Licence | Open Government Licence — British Columbia |
| Coverage | British Columbia; PSP 7,341 sites / 23,956 visits; non-PSP 9,512 sites / 11,951 visits; combined 16,853 sites / 35,907 visits |
| Format | PSP: 10 CSV tables + XLSX dictionary; non-PSP: 456 CSV tables + XLSX dictionary |
| Access tier | Open. Anonymous FTP; no credentials, request form, or DSA. |
| Acquisition date | 2026-11-14 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |

This record covers both sub-corpora. The PSP tables are in `psp/` and are
described below. The non-PSP companion is in `non_psp/` and has its own
`ACQUISITION.md`, `CONTENTS.md`, and `PROVENANCE.csv`. The two site identifier
sets are disjoint.

The PSP tables contain exactly **7,341 sites and 23,956 visits**, matching
the `fresh-fvsbc` reference counts.

## Access route

The BC Data Catalogue record exposes two resources:

1. **Ground Plot Data FTP Download** —
   `https://www.for.gov.bc.ca/ftp/HTS/external/!publish/ground_plot_compilations/`
2. **Interactive Mapping App** —
   `https://bcgov-env.shinyapps.io/FAIB_GROUND_SAMPLE/`

The HTTPS FTP path returns **HTTP 401** with
`WWW-Authenticate: Negotiate, NTLM` (observed 2026-11-14). It is not
anonymously readable over HTTPS, so it is not a usable bulk-download route
without credentials.

The same publication tree is anonymously readable over the FTP protocol:

```text
ftp://ftp.for.gov.bc.ca/HTS/external/!publish/ground_plot_compilations/
├── psp/           <- acquired 2026-11-14
└── non_psp/       <- acquired 2026-11-14
    ├── publish_province/
    └── publish_by_tsa/  (37 TSA directories)
```

Login is `anonymous` with no password. The FTP service welcomed the anonymous
session and served the directory listings and files. No access controls were
circumvented, and no credentials were used.

The `bcgov/FAIBCompiler` repository (Apache-2.0; inspected at commit
`1dd44cdc8da014e220e6bd9b175edcbdddfe7fc8`) contains the VRI/PSP compiler
code and publication preparation functions. Its README and R sources describe
loading from FAIB Oracle and writing compilation outputs; they do not expose a
separate HTTP bulk-download endpoint. The anonymous FTP tree above is the
publication target. The sibling `nemora` repository independently documents
the same anonymous FTP path in `nemora.ingest.faib`.

The Shiny app is interactive and was not scraped. Its catalogue description
states that the export button produces a **plot summary file with limited
attributes**, not the full tree-level compilation tables. Reproducing the full
corpus therefore uses the FTP route documented here.

The separate catalogue layer "Forest Inventory Ground Plots - Public Access"
(`6d6d115f-4cc2-4141-909e-3344b3a72bcf`) is a spatial plot-location layer
(WMS, KML, and BCGW custom download). It does not contain the compiled
mensuration tables and was not used as a substitute.

## Retrieved PSP files

All CSVs were gzipped with `gzip -9 -n` for git-annex. Original sizes and
SHA-256 values were verified against the decompressed streams.

| Archived file | Table | Rows | Original bytes | Gzip bytes | SHA-256 (gzip) |
|---------------|-------|-----:|---------------:|-----------:|----------------|
| `psp/faib_header.csv.gz` | `faib_header` | 7,341 | 1,406,012 | 314,277 | `c385452cc76b1f6bb4d55102cb0226d811e2eab840c83e762702e6395e5bf19d` |
| `psp/faib_plot_header.csv.gz` | `faib_plot_header` | 24,974 | 2,815,639 | 230,273 | `cacc06c524bd783c13bcbba94c0d2fad9d98a0f3710eb6431edc49918bf56e9f` |
| `psp/faib_sample_byvisit.csv.gz` | `faib_sample_byvisit` | 23,956 | 3,186,768 | 311,679 | `9e8488ed089833ec23281edde2e6689c9994c542ff069408e860a0b7e0599461` |
| `psp/faib_compiled_smries.csv.gz` | `faib_compiled_smries` | 119,780 | 23,756,202 | 5,516,961 | `bcc8d1e5e7e96dec7625282464a8fb9d66831575423e427da2902800348e701b` |
| `psp/faib_compiled_smeries_ht.csv.gz` | `faib_compiled_smeries_ht` | 23,956 | 1,072,453 | 287,056 | `156f9013b21039d8d6c813ab7527ab95a3af699461183966e969bd32a7707334` |
| `psp/faib_compiled_spcsmries.csv.gz` | `faib_compiled_spcsmries` | 416,570 | 60,369,135 | 10,771,934 | `63dfa52f1d208bfcaa34628d1b22b8772b47b67ed12932e7c3051f8cc219fb74` |
| `psp/faib_compiled_spcsmries_siteage.csv.gz` | `faib_compiled_spcsmries_siteage` | 86,468 | 6,585,676 | 1,695,648 | `218ee66b428ce51734a49f93cd4b9cae306279865ed9f172c3d646c922ba7521` |
| `psp/faib_smltree_smries_cl.csv.gz` | `faib_smltree_smries_cl` | 14,911 | 1,116,373 | 280,982 | `50613da7b3841b191cae08841cc9eefd8f8011107536c246a55aa24fbd8be5ab` |
| `psp/faib_smltree_smries_clsp.csv.gz` | `faib_smltree_smries_clsp` | 21,111 | 1,113,152 | 242,806 | `e626252f6e354209484e6b3327391c12b10b73ce262566b7d320940b0b5d8ddb` |
| `psp/faib_tree_detail.csv.gz` | `faib_tree_detail` | 3,217,648 | 740,181,676 | 111,371,932 | `9ed7b0a23dd74686173ee45fddfcb71a7bbddd7995230c7de2696b7c76d614e8` |

The PSP data dictionary is archived at
`metadata/PSP_data_dictionary_2026Apr20.xlsx` (33,118 bytes, SHA-256
`beda1c2a523a6495de92aad97b1b1a8f548548599c15d87fe0df07d4696ee6a1`).
The non-PSP dictionary is retained at
`metadata/non_PSP_data_dictionary_2026Apr20.xlsx` (39,116 bytes) to document
the companion corpus. Catalogue JSON snapshots, FTP listings, the FAIBCompiler
README, and the compiler commit hash are also under `metadata/`.

Full per-file provenance, including original and gzip hashes, is in
`PROVENANCE.csv`.

## Corpus statistics (feasibility check)

### Sites, visits, and trees

| Measure | Value |
|---------|------:|
| Sites (`faib_header.SITE_IDENTIFIER`) | 7,341 |
| Visits (`faib_sample_byvisit.CLSTR_ID`) | 23,956 |
| Remeasured sites (>1 visit) | 5,735 (78.1%) |
| Maximum visits per site | 13 |
| Tree measurement rows (`faib_tree_detail`) | 3,217,648 |
| Unique trees (site + plot + tree number) | 1,138,768 |
| Remeasured trees (>1 visit) | 803,868 (70.6% of unique trees) |
| Mean measurements per tree | 2.83 |
| Live tree rows | 2,646,320 |
| Dead tree rows | 571,323 |
| Missing live/dead status | 5 |
| Measurement year range | 1921–2025 |
| Measurement date range | 1921-10-24 to 2025-09-10 |
| Site status: inactive / active | 4,298 IA / 3,043 A |
| Establishment type: ground / remeasured | 5,289 PSP_G / 2,052 PSP_R |

### Visits per site

| Visits | Sites |
|-------:|-----:|
| 1 | 1,606 |
| 2 | 1,341 |
| 3 | 1,254 |
| 4 | 1,322 |
| 5 | 991 |
| 6 | 453 |
| 7 | 197 |
| 8 | 106 |
| 9 | 33 |
| 10 | 13 |
| 11 | 15 |
| 12 | 4 |
| 13 | 6 |

### BEC zones

12 BEC zones are represented:

| BEC zone | Sites |
|----------|-----:|
| CWH | 2,335 |
| ICH | 1,269 |
| SBS | 1,206 |
| IDF | 973 |
| BWBS | 534 |
| ESSF | 420 |
| MS | 376 |
| SBPS | 170 |
| CDF | 26 |
| PP | 16 |
| MH | 13 |
| CMA | 3 |

`TSA` has 40 distinct values; `TFL` has 26. Latitude/longitude are present for
6,315 of 7,341 sites (86.0%); 1,026 sites lack coordinates.

### Species and sizes

45 species codes occur (plus 5 rows with missing species). The ten most
frequent tree-measurement species are:

| Species | Tree rows |
|---------|----------:|
| HW | 688,291 |
| FD | 619,648 |
| PL | 583,856 |
| CW | 260,930 |
| SW | 222,068 |
| BL | 200,782 |
| AT | 136,074 |
| LW | 75,959 |
| SS | 73,456 |
| EP | 71,726 |

DBH (`DBH`, cm; 3,217,462 non-null rows):

| Statistic | Value |
|-----------|------:|
| Minimum | 0.5 |
| 1st percentile | 2.9 |
| Median | 12.4 |
| 99th percentile | 59.9 |
| Maximum | 401.7 |

Height (`HEIGHT`, m; 3,217,457 non-null rows, 99.99%):

| Statistic | Value |
|-----------|------:|
| Minimum | 0.37 |
| Median | 13.4 |
| Maximum | 73.3 |
| Field measured | 788,305 rows (24.5%) |
| Estimated from DBH | 2,429,152 rows (75.5%) |
| Missing | 191 rows (0.006%) |

The `HEIGHT_SOURCE` field distinguishes field-measured from DBH-estimated
heights, which is essential for height-growth calibration.

### Age and site index

Site index and age are present:

- `faib_compiled_spcsmries_siteage.csv` has 86,468 species-by-visit rows with
  three site-index methods (`SI1`, `SI2`, `SI3`), BH age, total age, and top
  height.
- 21,639 of 23,956 visits (90.3%) have at least one site-index value.
- 21,976 visits (91.7%) have at least one BH-age or total-age value.
- Tree-level `SI_TREE` is populated for 296,482 of 3,217,648 tree rows (9.2%);
  `AGE_BH` and `AGE_TOT` are populated for 304,185 rows (9.5%).

### Plot design and compiled tables

- All 23,956 visits are `SAMP_TYP = F` (fixed area), `VISIT_TYPE = REP`, and
  `SAMPLE_SITE_PURPOSE_TYPE_CODE = PSP`.
- `faib_plot_header` has 24,974 plot rows: 23,446 visits have one plot, 508
  have three plots, and 2 have two plots. Main-plot area has a median of
  0.0809 ha (range 0.0050–0.81 ha).
- `faib_compiled_smries` has 119,780 rows: one stand summary per visit for each
  of five utilization limits (2, 4, 7.5, 12.5, and 17.5 cm).
- `faib_compiled_spcsmries` has 416,570 species-by-utilization rows.
- `faib_compiled_smeries_ht` has 23,956 visit-level height summaries; mean
  live height is present for 23,948 visits and Lorey height for 20,861.

## Non-PSP companion corpus

The non-PSP compilations were archived on 2026-11-14 under `non_psp/`. The
upstream tree is `ftp://ftp.for.gov.bc.ca/HTS/external/!publish/ground_plot_compilations/non_psp/`
and contains a province-wide 12-table set plus 37 per-TSA directories, each
with the same 12 table names, plus the non-PSP dictionary. The archive has 457
files (456 gzipped CSVs and one XLSX), 269,779,544 bytes uncompressed and
52,765,031 bytes gzipped.

The non-PSP corpus has 9,512 sites and 11,951 visits in 37 TSAs, with 367,096
tree measurement rows, 275,264 unique trees, and 76,667 remeasured trees. It
is predominantly single-visit (7,484 sites, 78.7%), but 2,028 sites are
remeasured. Establishment types are VRI 6,684 sites, YSM 1,129, CMI 995, SUP
387, NFI 254, and VLT 63. The site identifiers are disjoint from PSP, so the
combined BC FAIB archive holds 16,853 sites and 35,907 visits.

The province-wide and per-TSA tables are not independent: the per-TSA site,
visit, and tree-row counts sum exactly to the province-wide counts, and the
union of per-TSA site identifiers equals the province-wide 9,512. Use
`publish_province/` for analysis and treat `publish_by_tsa/` as the upstream
publication partition.

Full detail is in `non_psp/ACQUISITION.md`, `non_psp/CONTENTS.md`, and
`non_psp/PROVENANCE.csv`. The acquisition manifest is
`data/manifests/bc-faib-ground-plots-nonpsp-acquisition.csv`.

## Feasibility for fresh-fvsca

**Verdict: strong primary BC calibration corpus.** The PSP compilation is a
near-exact match to the `fresh-fvsbc` corpus (7,341 sites / 23,956 visits) and
provides the attributes that the open MAGPlot package lacks:

- repeated individual-tree measurements with 803,868 remeasured trees;
- fixed-area plots with explicit plot area and per-tree expansion factors;
- species-level site index, BH age, total age, and top height for about 90% of
  visits;
- 12 BEC zones and 45 species codes;
- DBH for 99.99% of tree rows and height for 99.99% of tree rows.

Caveats for calibration:

- **Height is mostly modelled.** Only 24.5% of tree heights are field
  measured; 75.5% are estimated from DBH. Filter on `HEIGHT_SOURCE` when
  fitting height–diameter or height-growth relationships.
- **Species crosswalk required.** The 45 codes are BC provincial species codes;
  map them to FVS species before calibration.
- **Utilization duplication.** The stand and species summaries repeat each
  visit at five utilization limits. Filter `UTIL` explicitly; do not sum rows
  across utilization levels.
- **Coordinates are incomplete.** 1,026 sites (14.0%) lack latitude/longitude.
  Spatial joins or climate overlays must handle missing coordinates.
- **PSP is the primary calibration subset.** The PSP tables are the
  remeasurement-rich corpus. The non-PSP companion is archived under
  `non_psp/` and adds 9,512 mostly single-visit sites (2,028 remeasured) plus
  367,096 tree rows; see `non_psp/ACQUISITION.md` and `non_psp/CONTENTS.md`.
- **Snapshot, not a versioned release.** The files are dated 2026-04-16/21.
  Re-list and re-hash the FTP directory before reuse.

## Reproduction

```bash
mkdir -p data/raw/bc_faib_ground_plots/psp
cd data/raw/bc_faib_ground_plots/psp
BASE='ftp://ftp.for.gov.bc.ca/HTS/external/!publish/ground_plot_compilations/psp'
for f in faib_header.csv faib_plot_header.csv faib_sample_byvisit.csv \
         faib_compiled_smries.csv faib_compiled_smeries_ht.csv \
         faib_compiled_spcsmries.csv faib_compiled_spcsmries_siteage.csv \
         faib_smltree_smries_cl.csv faib_smltree_smries_clsp.csv \
         faib_tree_detail.csv PSP_data_dictionary_2026Apr20.xlsx; do
  wget -c --tries=20 --timeout=120 "$BASE/$f"
done
gzip -9 -n *.csv
sha256sum *.gz
```

The HTTPS form of the same path returns 401; use the `ftp://` scheme. No
credentials are required.

## Citation and contacts

Province of British Columbia, Ministry of Forests, Forest Analysis and
Inventory Branch. 2026. Forest Inventory Ground Plot Data and Interactive Map
— Ground Plot Data FTP Download. BC Data Catalogue record
`824e684b-4114-4a05-a490-aa56332b57f4` (accessed 2026-11-14).

Contact route: the BC Data Catalogue dataset page and the FAIB organization
record. The catalogue record does not publish a direct contact email; use the
dataset page's contact/organization links. Do not send credentials or
authenticated FTP details in correspondence.
