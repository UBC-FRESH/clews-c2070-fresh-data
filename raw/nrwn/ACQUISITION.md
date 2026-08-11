# NRWN (National Railway Network) — multi-format per-province acquisition — 2026-08-10/11

## Identity

| Field | Value |
|-------|-------|
| Publisher | Natural Resources Canada — Canada Centre for Mapping and Earth Observation |
| Title | National Railway Network (NRWN) — GeoBase series — v2.0 |
| Catalogue record | https://open.canada.ca/data/en/dataset/ac26807e-a1e8-49fa-87bf-451175a859b8 |
| Source mirror (verified live) | `https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/` (HTTPS directory listing per `<prov>/`) |
| Licence | Open Government Licence — Canada |
| Batch 1 (BC SHP) acquired | 2026-08-10 (commit `54fec20`) |
| Batch 3 (per-province GML/KML) acquired | 2026-08-11 (commits `85317fb` + `66ff56c`) |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | 11 of 13 jurisdictions (BC, AB, SK, MB, ON, QC, NB, NS, NL, NT, YT). PE and NU deferred (see below). |
| Vintage | 2019-07-25 (server timestamps); BC KML updated 2020-10-02 |
| CRS | NRWN v2.0 (Statistics Canada Lambert conformal conic, EPSG:3347 family) |
| Format (per-province) | Three flavours hosted per jurisdiction: SHP (ESRI), GML (Geography Markup Language — English & French), KML/KMZ (Google Earth — English `.kmz`) |

## Provenance pipeline

The NRWN per-province archives follow a regular upstream naming pattern:

```
https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/<prov>/
    nrwn_rfn_<prov>_shp_en.zip   ← ESRI Shapefile bundle (English)
    nrwn_rfn_<prov>_shp_fr.zip   ← ESRI Shapefile bundle (French, where present)
    nrwn_rfn_<prov>_gml_en.zip   ← GML 3.x bundle (English)
    nrwn_rfn_<prov>_gml_fr.zip   ← GML 3.x bundle (French)
    nrwn_rfn_<prov>_kml_en.kmz   ← KML/KMZ Google Earth bundle (English)
    nrwn_rfn_<prov>_kml_fr.kmz   ← KML/KMZ Google Earth bundle (French, where present)
```

`git-annex` tracks each `.zip`/`.kmz` blob as an annex object stored on the
`arbutus-s3` DataLad special remote; co-located `.sha256` files are kept as
plain git-tracked manifest text for end-to-end verification.

## Archived files — batch-3 per-province expansion (commit `85317fb`)

A total of **33 archives** were downloaded and uploaded to `arbutus-s3` across
11 jurisdictions and 3 format/lang slots. Aggregate footprint: **114,610,941
bytes (~109 MB)**.

### Per-province × format matrix (bytes)

| Prov | GML EN (`.zip`) | GML FR (`.zip`) | KML EN (`.kmz`) | Subtotal |
|:----:|---------------:|---------------:|----------------:|---------:|
| BC   | 5,014,595      | 5,109,152      | 6,327,950       | 16,451,697 |
| AB   | 4,235,231      | 4,296,594      | 6,200,805       | 14,732,630 |
| SK   | 3,693,881      | 3,765,671      | 5,489,811       | 12,949,363 |
| MB   | 2,575,035      | 2,618,879      | 3,840,303       |  9,034,217 |
| ON   | 9,325,425      | 9,461,565      | 14,211,673      | 32,998,663 |
| QC   | 6,041,272      | 6,126,590      | 9,110,347       | 21,278,209 |
| NB   | 1,045,569      | 1,066,040      | 1,550,318       |  3,661,927 |
| NS   | 792,176        | 805,440        | 1,179,306       |  2,776,922 |
| NL   | 133,680        | 136,010        | 173,075         |    442,765 |
| NT   | 58,277         | 58,867         | 55,346          |    172,490 |
| YT   | 39,593         | 39,984         | 32,481          |    112,058 |
| **Total** | **32,954,734** | **33,484,792** | **48,171,415** | **114,610,941** |

### Per-archive SHA-256 + URL ledger

| File | Bytes | SHA-256 (full) | Source URL | Status |
|------|------:|----------------|------------|--------|
| `nrwn_rfn_bc_gml_en.zip`  | 5,014,595  | `59df5c9260c463544b42d1c1f6a45d3d9185ffecf9a9987e782975690bfe7532` | `…bc/nrwn_rfn_bc_gml_en.zip` | Archived |
| `nrwn_rfn_bc_gml_fr.zip`  | 5,109,152  | `025981184e0811887043a1b77c563569d3b20b2c69ce50818cf54050617b829e` | `…bc/nrwn_rfn_bc_gml_fr.zip` | Archived |
| `nrwn_rfn_bc_kml_en.kmz`  | 6,327,950  | `f16f9df8d06459e03c800be612a7e0dccfd18e20a4b45ce56549632173268644` | `…bc/nrwn_rfn_bc_kml_en.kmz` | Archived |
| `nrwn_rfn_ab_gml_en.zip`  | 4,235,231  | `4621784916288b52e7ef95b4d64a0420da548ea48981aaabfd7f5d21ae51d93d` | `…ab/nrwn_rfn_ab_gml_en.zip` | Archived |
| `nrwn_rfn_ab_gml_fr.zip`  | 4,296,594  | `e6304af23a0007b1a2206d5f5d678adaea73a511b21db355d8c0b12963aa7872` | `…ab/nrwn_rfn_ab_gml_fr.zip` | Archived |
| `nrwn_rfn_ab_kml_en.kmz`  | 6,200,805  | `f72d56c84a7c803c1902e549a792137f422c63e92fd5c0d32830c256cf42527d` | `…ab/nrwn_rfn_ab_kml_en.kmz` | Archived |
| `nrwn_rfn_sk_gml_en.zip`  | 3,693,881  | `2c8fda4dba44686c46f94a58f392f6da24bd9cff782610e8bfd4fe21ab0c7d48` | `…sk/nrwn_rfn_sk_gml_en.zip` | Archived |
| `nrwn_rfn_sk_gml_fr.zip`  | 3,765,671  | `d79248fd536090bbff2c13e5381dbc016192238e1b4a92d851252c89aba78dc9` | `…sk/nrwn_rfn_sk_gml_fr.zip` | Archived |
| `nrwn_rfn_sk_kml_en.kmz`  | 5,489,811  | `5462007ba4e6c610bb86a474ada1ce3f7d020949b907d6463bbb3114187a5ec2` | `…sk/nrwn_rfn_sk_kml_en.kmz` | Archived |
| `nrwn_rfn_mb_gml_en.zip`  | 2,575,035  | `bfaf04c6c0089aa4a3c6239100c7a60618dd77277480c506e1020a11af5b6597` | `…mb/nrwn_rfn_mb_gml_en.zip` | Archived |
| `nrwn_rfn_mb_gml_fr.zip`  | 2,618,879  | `fb9fd05d4a95ccad4a9411dc03f1c28a86bf65a9d623117d13508380bbabda7e` | `…mb/nrwn_rfn_mb_gml_fr.zip` | Archived |
| `nrwn_rfn_mb_kml_en.kmz`  | 3,840,303  | `195ee2b40df5e59be9d50e3fec8d1149bc1a27c555b17bb9cb59d6de8ecc9ffc` | `…mb/nrwn_rfn_mb_kml_en.kmz` | Archived |
| `nrwn_rfn_on_gml_en.zip`  | 9,325,425  | `4cae81d3afc774993d3ca9648bafcee0bbf893b5f557796f91b5820b960185d8` | `…on/nrwn_rfn_on_gml_en.zip` | Archived |
| `nrwn_rfn_on_gml_fr.zip`  | 9,461,565  | `ba6db470b1f1a3b57b866f574a18b18d1b6fa1033fbfdc1877ad3362cf4544dc` | `…on/nrwn_rfn_on_gml_fr.zip` | Archived |
| `nrwn_rfn_on_kml_en.kmz`  | 14,211,673 | `835c2f30f453cd554d6462845085f99594e51000851bb81f1dbdaaabdc87da6a` | `…on/nrwn_rfn_on_kml_en.kmz` | Archived |
| `nrwn_rfn_qc_gml_en.zip`  | 6,041,272  | `b749acabac5814b078284cebbe7a840a21c4b99c17de9f5a4acd41440a464ebe` | `…qc/nrwn_rfn_qc_gml_en.zip` | Archived |
| `nrwn_rfn_qc_gml_fr.zip`  | 6,126,590  | `7f5d7bb1eeec944229ecd6e3480cdb30d914f8d351e65c0c5d564b95dda1f7b3` | `…qc/nrwn_rfn_qc_gml_fr.zip` | Archived |
| `nrwn_rfn_qc_kml_en.kmz`  | 9,110,347  | `ce219abc37fbd27e113a4f44f20f618ef09e9ca5c81806b5403d3782b5dba39e` | `…qc/nrwn_rfn_qc_kml_en.kmz` | Archived |
| `nrwn_rfn_nb_gml_en.zip`  | 1,045,569  | `996707260a36dac37d438965ff1e348047a97080d0e507d1c215a3418c288420` | `…nb/nrwn_rfn_nb_gml_en.zip` | Archived |
| `nrwn_rfn_nb_gml_fr.zip`  | 1,066,040  | `af95cbbda320d9d540483f39b9070a3a8a7b528ab1ba400ab073e741ad5bf410` | `…nb/nrwn_rfn_nb_gml_fr.zip` | Archived |
| `nrwn_rfn_nb_kml_en.kmz`  | 1,550,318  | `df4c7e4fc4f5e55bee93ac5d530b3326bffccfb27bf920708b57bddf15c70a46` | `…nb/nrwn_rfn_nb_kml_en.kmz` | Archived |
| `nrwn_rfn_ns_gml_en.zip`  | 792,176    | `abc1619834d0ece8b4873489732d5ad567b5a556310bea6c1621c6cdc7358aa9` | `…ns/nrwn_rfn_ns_gml_en.zip` | Archived |
| `nrwn_rfn_ns_gml_fr.zip`  | 805,440    | `d0d91b9e011ac403a2decd5df9f6b7855a7ac4fa9fdda93036383da3ae50b89d` | `…ns/nrwn_rfn_ns_gml_fr.zip` | Archived |
| `nrwn_rfn_ns_kml_en.kmz`  | 1,179,306  | `1cb4232ad680449f0edba301205f85ba44809838ce5c592ab2551f0942ba833d` | `…ns/nrwn_rfn_ns_kml_en.kmz` | Archived |
| `nrwn_rfn_nl_gml_en.zip`  | 133,680    | `cdf4fc630d6d45c8c1a558d0ea249ffa2f7bcb8516823496462ff2eb4d29467d` | `…nl/nrwn_rfn_nl_gml_en.zip` | Archived |
| `nrwn_rfn_nl_gml_fr.zip`  | 136,010    | `c8b7d201df54a84983a4592d1d6b59ad112af7d9fbe877c9eadd268f2384ae99` | `…nl/nrwn_rfn_nl_gml_fr.zip` | Archived |
| `nrwn_rfn_nl_kml_en.kmz`  | 173,075    | `9d538f258662bdefae8042dd77e7eaa9f141397c1d01dca627974ddde140958f` | `…nl/nrwn_rfn_nl_kml_en.kmz` | Archived |
| `nrwn_rfn_nt_gml_en.zip`  | 58,277     | `5b484a07f6314be9eb8d3abd602ac93ec33a6ddb0d05d006e11903b48e645bf6` | `…nt/nrwn_rfn_nt_gml_en.zip` | Archived |
| `nrwn_rfn_nt_gml_fr.zip`  | 58,867     | `0ef495e7a7446e470a4230d4b1f2c60afdbe657e843480b07abd54993caf8eee` | `…nt/nrwn_rfn_nt_gml_fr.zip` | Archived |
| `nrwn_rfn_nt_kml_en.kmz`  | 55,346     | `b461049473296077e5dc884d0addbce34eb2f6c54375e08290becd703616eb5a` | `…nt/nrwn_rfn_nt_kml_en.kmz` | Archived |
| `nrwn_rfn_yt_gml_en.zip`  | 39,593     | `e19d25e02054658b151fa609d2ca3ca8cc4a19bcc2d6196abe8901b1b5a19a26` | `…yt/nrwn_rfn_yt_gml_en.zip` | Archived |
| `nrwn_rfn_yt_gml_fr.zip`  | 39,984     | `90f9390cbdaf4f6639db1e7b9cf408ceb65977b0a54c7f77312ea989ae8e6887` | `…yt/nrwn_rfn_yt_gml_fr.zip` | Archived |
| `nrwn_rfn_yt_kml_en.kmz`  | 32,481     | `b8ad7ec5bef113ce0f4f5506099d085ed5573a35735565a472b808ff276b387f` | `…yt/nrwn_rfn_yt_kml_en.kmz` | Archived |

### Deferred jurisdictions (404 — directory absent on mirror)

Two of the 13 jurisdictions have **no NRWN directory at all** on the FTP
mirror (`https://ftp.maps.canada.ca/pub/nrcan_rncan/vector/geobase_nrwn_rfn/<prov>/`
returns HTTP 404 even at the directory level, not just at archive level).

| Prov | gml_en | gml_fr | kml_en.kmz | Reason |
|:----:|:------:|:------:|:----------:|--------|
| PE   | 404 | 404 | 404 | No `pe/` directory on mirror |
| NU   | 404 | 404 | 404 | No `nu/` directory on mirror |

These are recorded in `PROVENANCE.csv` with `bytes=0` and a `DEFERRED` note
under the same `file,format,bytes,note` schema; the 6 expected file paths
remain documented and re-probed on any future acquisition pass.

## Batch-1 BC shapefile background (commit `54fec20`)

The BC shapefile was the seed for this corpus and remains the only SHP bundle
archived in the data submodule.

| Field | Value |
|-------|-------|
| Path | `data/raw/nrwn/nrwn_rfn_bc_shp_en.zip` |
| Bytes | 4,777,621 |
| Local SHA-256 | `2ed031b9bc319ef085356e2124e16c736e225db4466dacd1c5b5ca1b9b36097a` |
| Type | Zip archive carrying a v2.0 ESRI shapefile bundle — confirmed via `unzip -l` |

### Layer summary (BC NRWN v2.0 shapefile bundle)

| ESRI layer | Geometry | Layer file size |
|------------|----------|----------------:|
| `NRWN_BC_2_0_TRACK` | PolyLineZ | 6,150,636 B (~24,000 km rail) |
| `NRWN_BC_2_0_MARKERPOST` | Point | 90,960 B |
| `NRWN_BC_2_0_CROSSING` | Point | 182,800 B |
| `NRWN_BC_2_0_JUNCTION` | Point | 219,004 B |
| `NRWN_BC_2_0_STATION` | Point | 16,452 B |
| `NRWN_BC_2_0_STRUCTURE_1` | PolyLine (bridges/tunnels extent) | 214,284 B |
| `NRWN_BC_2_0_STRUCTURE_0` | Point | 996 B |
| `RFN_BC_2_0_pna.xml` | FGDC metadata | 133,839 B |

## Acknowledgements / citation

> Natural Resources Canada. *National Railway Network (NRWN) — GeoBase Series
> — v2.0*. Open Government Licence — Canada. Retrieved 2026-08-10/11 from
> the Open Canada portal
> <https://open.canada.ca/data/en/dataset/ac26807e-a1e8-49fa-87bf-451175a859b8>
> via the NRCan GeoBase FTP mirror.
