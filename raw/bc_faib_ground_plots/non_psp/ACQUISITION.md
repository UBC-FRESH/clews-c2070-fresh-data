# BC FAIB Non-PSP Ground Plot Compilations — Acquisition Record — 2026-11-14

## Identity

| Field | Value |
|-------|-------|
| Publisher | BC Ministry of Forests — Forest Analysis and Inventory Branch (FAIB) |
| Dataset | Forest Inventory Ground Plot Data and Interactive Map |
| BC Data Catalogue record | `824e684b-4114-4a05-a490-aa56332b57f4` |
| Catalogue URL | https://catalogue.data.gov.bc.ca/dataset/824e684b-4114-4a05-a490-aa56332b57f4 |
| Sub-corpus acquired | `non_psp/` — province-wide and per-TSA non-PSP ground-sample compilations |
| Compilation date | 2026-04-20/21 (dictionary `non_PSP_data_dictionary_2026Apr20.xlsx`) |
| Licence | Open Government Licence — British Columbia |
| Coverage | British Columbia; 9,512 sites, 11,951 visits, 37 TSAs |
| Format | 456 CSV tables (12 province-wide + 37 TSA directories × 12) + XLSX data dictionary |
| Access tier | Open. Anonymous FTP; no credentials, request form, or DSA. |
| Acquisition date | 2026-11-14 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |

This is the companion corpus to the Permanent Sample Plot (PSP) archive in
`../psp/`. It contains the non-PSP ground samples: VRI, CMI, YSM, NFI, SUP,
and VLT establishment types. The site identifier sets of the PSP and non-PSP
corpora are disjoint: PSP 7,341 sites plus non-PSP 9,512 sites gives 16,853
distinct BC FAIB sites (35,907 visits). See `CONTENTS.md` for the profile.

## Access route

The BC Data Catalogue record exposes the same FTP publication tree used for
the PSP archive:

```text
ftp://ftp.for.gov.bc.ca/HTS/external/!publish/ground_plot_compilations/non_psp/
├── non_PSP_data_dictionary_2026Apr20.xlsx
├── publish_province/    12 CSV tables, province-wide
└── publish_by_tsa/      37 TSA directories × 12 CSV tables
```

The HTTPS form of this path returns HTTP 401 with
`WWW-Authenticate: Negotiate, NTLM`, so the FTP scheme is used. Login is
`anonymous` with no password. No access controls were circumvented and no
credentials were used.

The upstream tree was listed on 2026-11-14 with an anonymous FTP walk. The
saved listing is at `../metadata/ftp_listing_non_psp_tree.txt`; the original
top-level listing is at `../metadata/ftp_listing_non_psp.txt`. The walk found
457 files, 39 directories (`publish_province`, `publish_by_tsa`, and 37 TSA
directories), and 269,779,544 bytes.

## Retrieved files

All 456 CSVs were downloaded over anonymous FTP with `curl --fail` and
retried by the mirror script. Sizes were checked against the FTP `SIZE`
returned for every file. The data dictionary was already archived during the
PSP pass and was copied into place rather than re-downloaded; its SHA-256
matches the recorded metadata copy.

All CSVs were gzipped with `gzip -9 -n`. The gzip round-trip was verified by
decompressing each file and comparing its SHA-256 with the pre-compression
hash.

| Scope | Files | Uncompressed bytes | Gzip bytes |
|-------|------:|-------------------:|-----------:|
| `publish_province/` | 12 | 134,811,426 | 26,325,729 |
| `publish_by_tsa/` (37 directories) | 444 | 134,929,002 | 26,400,186 |
| Dictionary | 1 | 39,116 | 39,116 (not gzipped) |
| **Total** | **457** | **269,779,544** | **52,765,031** |

The province-wide and per-TSA tables are not independent. The 37 TSA
directories contain exact subsets of the province-wide tables: their site,
visit, and tree-row counts sum exactly to the province-wide counts, and the
union of their site identifiers equals the province-wide 9,512 sites. Use
`publish_province/` for analysis and treat `publish_by_tsa/` as the upstream
publication partition, not as additional data.

Per-file gzip hashes, uncompressed sizes, row counts, source URLs, and
retrieval timestamps are in `PROVENANCE.csv`. The parent dataset provenance
file `../PROVENANCE.csv` includes the same rows. The acquisition manifest is
`data/manifests/bc-faib-ground-plots-nonpsp-acquisition.csv`.

## Corpus statistics (summary)

| Measure | Value |
|---------|------:|
| Distinct sites | 9,512 |
| Distinct visits (`CLSTR_ID`) | 11,951 |
| Remeasured sites (>1 visit) | 2,028 (21.3%) |
| Single-visit sites | 7,484 (78.7%) |
| Maximum visits per site | 5 |
| Tree measurement rows | 367,096 |
| Unique trees (site + plot + tree number) | 275,264 |
| Remeasured trees (>1 visit) | 76,667 (27.9% of unique trees) |
| Mean measurements per tree | 1.33 |
| TSAs covered | 37 |
| BEC zones | 16 |
| Measurement years | 1995–2025 |
| Species codes | 42 |
| DBH populated | 357,845 rows (97.5%) |
| Height populated | 285,584 rows (77.8%) |
| Visits with site index | 9,318 (78.0%) |
| Visits with age | 11,286 (94.4%) |

The corpus is predominantly single-visit: 78.7% of sites have one visit and
many are VRI/CMI/YSM temporary or single-measurement samples. It nevertheless
adds 2,028 remeasured sites and 76,667 remeasured trees that are disjoint
from the PSP corpus. Remeasurement is concentrated in YSM (832 remeasured
sites), VRI (497), CMI (446), and NFI (247).

## Feasibility for fresh-fvsca

**Verdict: useful companion, not a replacement for PSP.** The non-PSP corpus
broadens BC coverage to 37 TSAs and 16 BEC zones and supplies site index and
age for most visits, but it is mostly single-visit and includes variable-radius
and temporary samples that need explicit plot-design handling.

Strengths:

- 9,512 sites and 11,951 visits across 37 TSAs, disjoint from PSP;
- 2,028 remeasured sites and 76,667 remeasured trees, adding growth intervals
  beyond the PSP corpus;
- site index and age present for 78.0% and 94.4% of visits respectively in
  `faib_compiled_spcsmries_siteage.csv`;
- DBH for 97.5% and height for 77.8% of tree rows;
- 42 species codes and 16 BEC zones.

Caveats:

- **Mostly single-visit.** Do not treat the 9,512 sites as remeasurement
  plots; only 2,028 have more than one visit.
- **Mixed plot designs.** 6,930 visits are variable-radius (`SAMP_TYP = V`)
  and 5,021 are fixed-area (`F`). `PLOT_AREA_MAIN` is populated for only
  7,193 of 37,547 plot-header rows, so variable-radius expansion must use the
  BAF/prism fields or the compiled per-hectare summaries.
- **Utilization duplication.** `faib_compiled_smries` has 59,755 rows =
  11,951 visits × 5 utilization limits; filter `UTIL` before aggregating.
- **Species crosswalk required.** The 42 BC provincial codes need mapping to
  FVS species; 308 tree rows have missing species.
- **Coordinates incomplete.** Latitude/longitude are present for 7,134 of
  9,512 sites (75.0%); 2,378 sites lack usable coordinates.
- **Per-TSA duplication.** The `publish_by_tsa/` tree duplicates the
  province-wide tables; do not sum the two scopes.
- **Snapshot, not a versioned release.** Files are dated 2026-04-20/21.
  Re-list and re-hash the FTP directory before reuse.

## Reproduction

```bash
mkdir -p data/raw/bc_faib_ground_plots/non_psp
cd data/raw/bc_faib_ground_plots/non_psp
BASE='ftp://ftp.for.gov.bc.ca/HTS/external/!publish/ground_plot_compilations/non_psp'
# Province-wide tables
for f in faib_header.csv faib_plot_header.csv faib_sample_byvisit.csv \
         faib_compiled_smries.csv faib_compiled_smries_wk.csv \
         faib_compiled_smeries_ht.csv faib_compiled_spcsmries.csv \
         faib_compiled_spcsmries_wk.csv \
         faib_compiled_spcsmries_siteage.csv \
         faib_smltree_smries_cl.csv faib_smltree_smries_clsp.csv \
         faib_tree_detail.csv; do
  curl -sS --fail -O "$BASE/publish_province/$f"
done
# Per-TSA directories preserve upstream names, including spaces
curl -sS --fail -O "$BASE/non_PSP_data_dictionary_2026Apr20.xlsx"
# Use an FTP recursive client for publish_by_tsa/, or mirror the saved listing.
gzip -9 -n publish_province/*.csv publish_by_tsa/*/*.csv
sha256sum publish_province/*.gz publish_by_tsa/*/*.gz
```

The HTTPS form of the same path returns 401; use the `ftp://` scheme. No
credentials are required.

## Citation and contacts

Province of British Columbia, Ministry of Forests, Forest Analysis and
Inventory Branch. 2026. Forest Inventory Ground Plot Data and Interactive Map
— Ground Plot Data FTP Download, non-PSP compilations. BC Data Catalogue
record `824e684b-4114-4a05-a490-aa56332b57f4` (accessed 2026-11-14).

Contact route: the BC Data Catalogue dataset page and the FAIB organization
record. The catalogue record does not publish a direct contact email; use the
dataset page's contact/organization links. Do not send credentials or
authenticated FTP details in correspondence.
