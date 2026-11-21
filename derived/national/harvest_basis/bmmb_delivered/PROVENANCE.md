# Provenance and extraction log

Dataset: `bmmb_delivered` (Quebec BMMB delivered-to-destination auction
results). Generated 2026-11-21. Machine-readable copy: `manifest.json`.

## Source

| Item | Value |
|---|---|
| Publisher | Bureau de mise en marché des bois (BMMB), Ministère des Ressources naturelles et des Forêts du Québec |
| Archive page | <https://bmmb.gouv.qc.ca/Auction/Auctions/Archive> |
| Public bulk export | <https://bmmb.gouv.qc.ca/Auction/Auctions/Export?IsArchive=True> |
| Access | Public HTTP GET. No login, API key, cookie, or access approval was used. The host redirects to `encheres.forets.gouv.qc.ca`. |
| Export filename | `VentesArchivees.xls` (legacy OLE2 Excel, one sheet `Sheet0`, 3,796 data rows, 142 columns) |
| Dataset scope | Archived public auction results; delivered-to-destination subset only in the sales file; all four sale types in the summary file |

The site is a public government service. Reuse should retain attribution to
BMMB / MRNF. No separate open-data licence statement was captured from the
archive page during this extraction.

## Retrieval log

### Archive export

| Field | Value |
|---|---|
| Requested URL | `https://bmmb.gouv.qc.ca/Auction/Auctions/Export?IsArchive=True` |
| Redirect | HTTP 302 to `https://encheres.forets.gouv.qc.ca/Auction/Auctions/Export?IsArchive=True` |
| Final HTTP status | 200 |
| Content-Type | `application/vnd.ms-excel` |
| Content-Disposition | `attachment; filename=VentesArchivees.xls` |
| Bytes | 9,795,584 |
| SHA-256 | `48c11fff0cb0f556be4d81cb454ff1468a51df4493b3a2c13ef3a58b72b2b3ce` |
| Retrieved (UTC) | 2026-11-21T20:29:05Z |
| Server response date | `Sat, 21 Nov 2026 20:29:22 GMT` |
| Sheet / rows | `Sheet0` / 3,796 data rows |

The parser verifies this exact byte count and SHA-256 before reading. A new
export must be reviewed and the provenance constants updated deliberately.

### Archive page

| Field | Value |
|---|---|
| URL | `https://bmmb.gouv.qc.ca/Auction/Auctions/Archive` |
| HTTP status | 200 |
| Content-Type | `text/html; charset=utf-8` |
| Bytes | 52,875 |
| SHA-256 | `75ab4d0d49c1266b8b6f185a4f78360d26e7bbd93727b6029cc3abdbf2914413` |
| Retrieved (UTC) | 2026-11-21T20:29:23Z |

The HTML page exposes the same archive grid and the detail-page links. Detail
URLs are opaque identifiers and are recorded individually below.

### Detail pages

All 18 delivered sales were opened on the public detail page. Each request
returned HTTP 200 and `text/html; charset=utf-8`.

| sale_id | HTTP | Content-Type | Bytes | SHA-256 (first 12) | Retrieved (UTC) |
|---|---:|---|---:|---|---|
| CS201206004 | 200 | text/html; charset=utf-8 | 28,036 | `42e750aa7300` | 2026-11-21T20:30:09Z |
| CS201207001 | 200 | text/html; charset=utf-8 | 27,064 | `e0d1512a8e4c` | 2026-11-21T20:30:09Z |
| CS201408201 | 200 | text/html; charset=utf-8 | 25,334 | `d4edb2356442` | 2026-11-21T20:30:09Z |
| CS201506201 | 200 | text/html; charset=utf-8 | 25,812 | `ae53322ac844` | 2026-11-21T20:30:10Z |
| SE201111001 | 200 | text/html; charset=utf-8 | 26,041 | `1975f179e72c` | 2026-11-21T20:30:09Z |
| SE201111002 | 200 | text/html; charset=utf-8 | 26,053 | `6e4611f2c287` | 2026-11-21T20:30:12Z |
| SE201111003 | 200 | text/html; charset=utf-8 | 24,978 | `2731a7fcd83c` | 2026-11-21T20:30:09Z |
| SE201111004 | 200 | text/html; charset=utf-8 | 24,341 | `328b637d4f38` | 2026-11-21T20:30:09Z |
| SE201111009 | 200 | text/html; charset=utf-8 | 26,042 | `60dd50788a01` | 2026-11-21T20:30:09Z |
| SE201503010 | 200 | text/html; charset=utf-8 | 28,341 | `14d9084ddec6` | 2026-11-21T20:30:09Z |
| SE201503011 | 200 | text/html; charset=utf-8 | 26,776 | `9ebc36ddf9c9` | 2026-11-21T20:30:10Z |
| SE201503020 | 200 | text/html; charset=utf-8 | 28,091 | `749022e35993` | 2026-11-21T20:30:09Z |
| SE201503021 | 200 | text/html; charset=utf-8 | 26,149 | `cb4c89a17ca6` | 2026-11-21T20:30:10Z |
| SE201503022 | 200 | text/html; charset=utf-8 | 26,093 | `b19aeff19074` | 2026-11-21T20:30:09Z |
| SE201503023 | 200 | text/html; charset=utf-8 | 28,093 | `2da2dd0c4db3` | 2026-11-21T20:30:09Z |
| SO201111011 | 200 | text/html; charset=utf-8 | 26,627 | `5a6803fe762d` | 2026-11-21T20:30:09Z |
| SO201206009 | 200 | text/html; charset=utf-8 | 29,189 | `548b65e2c6fe` | 2026-11-21T20:30:11Z |
| SO201207001 | 200 | text/html; charset=utf-8 | 29,004 | `3e7e85c262dc` | 2026-11-21T20:30:09Z |

The full URLs and full hashes are in `manifest.json` under
`source.detail_pages`. The detail page was used to cross-check the published
result text for 11 of the 13 priced sales; all 11 matched the export exactly.

### Result PDFs

Two awarded 2012 sales had a blank `Prix de vente` in the export. The public
detail pages link a one-page sale-result PDF. Both PDFs were fetched, hashed,
and parsed with `pdftotext -layout`.

| sale_id | URL | HTTP | Content-Type | Bytes | SHA-256 | Retrieved (UTC) |
|---|---|---:|---|---:|---|---|
| CS201206004 | `https://bmmb.gouv.qc.ca/Auction/File/GetHashable/mBd9BQq1g9MoQnSHIOsUAQ` | 200 | application/pdf | 173,296 | `0f5c16ca3c79fef06acc5b31a7411a43fb4b50322d96ee6440b0c2b36f800101` | 2026-11-21T20:30:23Z |
| CS201207001 | `https://bmmb.gouv.qc.ca/Auction/File/GetHashable/oexkf1webqUU3HnRc1DggA` | 200 | application/pdf | 175,176 | `2038759b3262627704e1ca3f957706b9ff21bd9933f8d6cc4a86e716b4d096b1` | 2026-11-21T20:30:28Z |

PDF text used:

- `CS201206004`: `Prix de vente : 112 450 $`; winner named in the PDF.
- `CS201207001`: `Prix de vente : 323 875 $`; winner named in the PDF.

Both PDFs also state: `*Certains volumes de bois offerts sont non-adjugés.`
(Awarded volume is therefore less than offered volume and is not published.)
The dataset records a lower bound only for these two sales.

## Field mapping

Source column names are French. The mapping below is exact; no source column
is silently reinterpreted.

| Source column | Output field | Notes |
|---|---|---|
| `Numéro d'appel d'offres` | `sale_id` | Also encodes `sale_year` as the four digits after the two-letter prefix. |
| `Date de fin enchère` | `auction_end_date`, `auction_end_year` | Date part only. |
| `Territoire` | `region_bmmb` | BMMB sales region, not a Quebec administrative region. |
| `UA` | `ua` | Unité d'aménagement, kept as text to preserve leading zeroes. |
| `Nom du secteur` | `sector_name` | Source sector name. |
| `Latitude`, `Longitude` | `latitude`, `longitude` | Source coordinates, six decimals. |
| `Provenance` | `tenure` | `Forêt publique`, `Forêt d'enseignement et recherche`, etc. |
| `Type d'enchère` | `auction_type` | Base or combinatorial auction. |
| `Type de vente` | `sale_type`, `sale_type_family` | Exact label plus controlled family. |
| `Etat` | `status`, `awarded` | `awarded=1` only for `Adjugé*`. |
| `Volume obligatoire total m³` | `volume_m3` | Mandatory offered volume; price denominator. |
| `Volume optionnel total m³` | `volume_optional_m3` | Kept separately; zero for all delivered rows. |
| `Prix de vente` | `total_cad` | **Total lot value**, not a per-m3 price. |
| `Prix estimé` | `estimated_total_cad` | Pre-auction estimate; `estimated_cad_m3` is derived and flagged as not observed. |
| `Prix de départ` | not exported | Retained internally; not needed for delivered results. |
| `Montant de la garantie` | not exported | Retained internally; not needed for delivered results. |
| Species/product columns, `... - Volume de bois d'oeuvre` or `... - Volume de trituration obligatoire` | `bmmb_delivered_species_volume.csv` | `sawlog` / `pulpwood`; optional volumes are zero for delivered rows. |
| No grade column | `quality=NA` | The source has no grade/quality field for these sales. |

`price_cad_m3` is derived as `total_cad / volume_m3`. It is blank when the
awarded volume is unknown (partial award) and `price_cad_m3_lower_bound` is
provided instead.

## Sale-type taxonomy

| Source label | Family | Delivered? | Value semantics |
|---|---|---:|---|
| `Livré à destination` | `delivered_to_destination` | yes | `delivered_sale_total_cad` |
| `Récolté` | `harvested_recolte_unspecified` | no | `recolte_sale_total_cad_basis_unspecified` |
| `Sur pied selon mesurage` | `standing_measured` | no | `standing_sale_total_cad` |
| `Sur pied selon inventaire` | `standing_inventory` | no | `standing_sale_total_cad` |

The parser fails if an unknown `Type de vente` appears. This is deliberate:
new sale types require a reviewed classification, not a silent fallback.

## Processing and validation

1. Read `Sheet0` from the hash-verified export with `xlrd`.
2. Parse every row into a sale record. Reject unknown sale types, missing
   sale IDs, negative/non-finite numbers, and delivered rows with invalid
   volume.
3. Parse the species/product columns for every sale and check that mandatory
   and optional species volumes reconcile to the corresponding total columns.
4. Filter to `sale_type == "Livré à destination"`.
5. Fill the two blank 2012 prices from the hash-verified result PDFs. Mark
   both as `partial_award=1`.
6. Cross-check the other 11 prices against the detail-page result text.
7. Build the all-sale-type summary from all 3,796 rows, keeping delivered,
   `Récolté`, and standing types separate.
8. Validate: 3,796 source rows; 18 delivered rows; 13 awarded; 13 observed
   prices; no duplicate IDs; no negative or non-finite values; awarded rows
   have prices; unsold rows do not; years match; species volumes reconcile;
   summary counts/volumes reconcile to the export.
9. Write CSV, recompute SHA-256 of every output, and write `manifest.json`.

Validation result at generation: **pass**. See `manifest.json` for the
recorded checks and output hashes.

## Artifacts and reproducibility

Generated by `scripts/national/extract_bmmb_delivered.py` in the parent
repository. The raw export, detail pages, and PDFs are local working files
under `tmp/bmmb/` and are not committed. Their hashes and URLs above are the
audit trail. Re-download from the public URLs and rerun the command in the
README; the parser fails if the export hash or byte count differs.

## Known source quirks

- The export has 142 columns and one row per sale/sector, not one row per
  species or grade.
- `Prix de vente` is a total sale value. It must not be read as CAD/m3.
- Two awarded delivered sales have a blank export price but a public result
  PDF with a price.
- The detail page `Destination` field is empty for all delivered sales.
- The delivered subset ends in 2015; the recent archive is overwhelmingly
  `Sur pied selon mesurage` (standing) sales.
- `Récolté` is a distinct sale type and is not documented as delivered. It is
  never included in the delivered table.
- The 2014 and 2015 delivered sales on `Forêt d'enseignement et recherche`
  are not Crown public forest; they are flagged in `tenure`.
