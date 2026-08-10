# NRN (National Road Network) — Multi-province GeoPackage Acquisition — 2026-08-10

## Identity

| Field | Value |
|-------|-------|
| Publisher | Statistics Canada / GeoBase (NRCan attribution for the GeoGratis mirror) |
| Title | National Road Network (NRN) — per-province GeoPackage releases |
| Catalog record | https://open.canada.ca/data/en/dataset/3d282116-e556-400c-9306-ca1a3cada77f |
| Source mirror (verified live per HEAD probe, 2026-08-10) | `https://geo.statcan.gc.ca/nrn_rrn/<prov>/nrn_rrn_<prov>_GPKG.zip` (drawn from CKAN resource list) |
| Licence | Open Government Licence — Canada (OGL Canada) |
| Acquisition date | 2026-08-10 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | All 13 provinces/territories (BC; AB; SK; MB; ON; QC; NB; NS; PE; NL; NT; YT; NU) |
| Vintage | 2026-06-26 (server Last-Modified across the family) — NRN is a continuously maintained national layer |
| CRS | Statistics Canada Lambert (EPSG:3347) — typical for NRN 2.0 releases |
| Format | GeoPackage (Vector) inside ZIP wrapper; one ZIP per province with EN+FR GPKG members |

## Source URLs (live-verified 2026-08-10)

| Province | URL | Bytes | Last-Modified | Status |
|----------|-----|------:|---------------|--------|
| BC | `https://geo.statcan.gc.ca/nrn_rrn/bc/nrn_rrn_bc_GPKG.zip` | 129,429,057 | 2026-06-26 | Archived (batch 1, 2026-08-10) |
| AB | `https://geo.statcan.gc.ca/nrn_rrn/ab/nrn_rrn_ab_GPKG.zip` | 254,938,403 | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| SK | `https://geo.statcan.gc.ca/nrn_rrn/sk/nrn_rrn_sk_GPKG.zip` | 153,989,918 | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| MB | `https://geo.statcan.gc.ca/nrn_rrn/mb/nrn_rrn_mb_GPKG.zip` | 44,372,783  | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| ON | `https://geo.statcan.gc.ca/nrn_rrn/on/nrn_rrn_on_GPKG.zip` | 507,430,394 | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| QC | `https://geo.statcan.gc.ca/nrn_rrn/qc/nrn_rrn_qc_GPKG.zip` | 402,694,935 | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| NB | `https://geo.statcan.gc.ca/nrn_rrn/nb/nrn_rrn_nb_GPKG.zip` | 66,437,628  | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| NS | `https://geo.statcan.gc.ca/nrn_rrn/ns/nrn_rrn_ns_GPKG.zip` | 129,980,403 | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| PE | `https://geo.statcan.gc.ca/nrn_rrn/pe/nrn_rrn_pe_GPKG.zip` | 14,227,278  | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| NL | `https://geo.statcan.gc.ca/nrn_rrn/nl/nrn_rrn_nl_GPKG.zip` | 23,858,147  | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| YT | `https://geo.statcan.gc.ca/nrn_rrn/yt/nrn_rrn_yt_GPKG.zip` | 6,367,064   | 2026-06-26 | Archived (batch 2, 2026-08-10) — Note: NRN-YT is distinct from `data/raw/yukon_roads/` (Forest Resource Roads GeoJSON) which was acquired in batch 1 |
| NT | `https://geo.statcan.gc.ca/nrn_rrn/nt/nrn_rrn_nt_GPKG.zip` | 10,413,272  | 2026-06-26 | Archived (batch 2, 2026-08-10) |
| NU | `https://geo.statcan.gc.ca/nrn_rrn/nu/nrn_rrn_nu_GPKG.zip` | 4,063,764   | 2026-06-26 | Archived (batch 2, 2026-08-10) |

All 13 per-province GeoPackages responded HTTP 200 OK with `Accept-Ranges: bytes` and stable server ETag values (`"0f4595da25dd1:0"`, `"0973b6fa25dd1:0"`, etc). None of the URLs returned 4xx/5xx; none required the fallback NRCan open-catalogue mirror URL.

The 12 batch-2 acquisitions contribute to the `nrn_vectors` source-inventory row 48 and supply the national transport cost-surface quantity sought by the P7.1 transport pipeline (rows 7, 11, 49 of source-inventory).

## Local files

Per province, the annex-managed archive file and its corresponding SHA-256 sidecar:

| Province | Annex key | Bytes | Local SHA-256 |
|----------|-----------|------:|---------------|
| BC | `MD5E-s129429057--69128cb1e6ba4fd87447cfda23c251a9.zip` | 129,429,057 | `9ae6fb8069a46c4a745571871bf068bdd9d978da745001fd0f8462bfb3b82842` |
| AB | (per annex keystore) | 254,938,403 | `0dfd3afc922f12b870a231bddd359d3430a5b66e04e283131c614f0b38aacf9a` |
| SK | (per annex keystore) | 153,989,918 | `f0a2bc98341db02ed55af6a79b4a437bc68c6243a7963824fdccd1c66857018a` |
| MB | (per annex keystore) | 44,372,783 | `d7dcda5a93202f26defd78207bf2a730b6968c5cb0e18d5cf4860a495948185c` |
| ON | (per annex keystore) | 507,430,394 | `a9f4e1f418d31c3a682d5d9224c8994cefd4c33e9c7b5e453af9d86bb77760d7` |
| QC | (per annex keystore) | 402,694,935 | `7175fa54a9846ec6d365f7e1674c1a78ec0bde8e44f0d786f7a5974b18c81552` |
| NB | (per annex keystore) | 66,437,628 | `af185c70ec70b8744090d49cd2db96f7e2d4234026535d0ac01435780afe8ace` |
| NS | (per annex keystore) | 129,980,403 | `5139dd2000922582c27ef7ef9c93edeac463346e874f6541d3e01e3ff77ffb98` |
| PE | (per annex keystore) | 14,227,278 | `58280c57970735050884a2baa13c20f048c10351ad6c154b4611c2d180e6694a` |
| NL | (per annex keystore) | 23,858,147 | `5250ddf9e017ea0f3caa6e2eff11c382cad4ff021875ae1a4ecad169ef946270` |
| YT | (per annex keystore) | 6,367,064 | `2b428a089059b686ba1c453b6b38dee3ca45053f9b54d236071f3b4f053f0b29` |
| NT | (per annex keystore) | 10,413,272 | `bbef9d3970a1dae37b53bcf3b02f48535882a902d85df3922e7f404d375c8d1b` |
| NU | (per annex keystore) | 4,063,764 | `5d0e8c03fa5b73bf11e2be9dd04fadcc8be66fb3437ae13b03003a0c4bedc3a6` |

ZIPs are released as: ZIP wrapper containing 2 GeoPackage members (the English `NRN_*_GPKG_en.gpkg` release and the French `RRN_*_GPKG_fr.gpkg` release). Inner sizes are surfaced in `PROVENANCE.csv` but the GeoPackage files are not extracted to disk.

## Predecessor notes

Batch 1 (2026-08-10) acquired BC. Batch 2 (this session, 2026-08-10) acquired the remaining 12 provinces. Source-inventory row 48 (`nrn_vectors`) is now satisfied in full; row 49 (`nrn_rrn_other_formats`) remains a future-work placeholder for GML FR/EN and KML where applicable.

## Acknowledgements / citation

> Statistics Canada / Natural Resources Canada. *National Road Network
> (NRN) — GeoBase Series.* Open Government Licence — Canada. Retrieved
> 2026-08-10 from the Open Canada portal
> <https://open.canada.ca/data/en/dataset/3d282116-e556-400c-9306-ca1a3cada77f>.
