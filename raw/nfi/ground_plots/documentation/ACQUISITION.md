# NFI Ground Plot Documentation — Acquisition Record — 2026-11-14

## Identity

| Field | Value |
|-------|-------|
| Publisher | National Forest Inventory Canada (Natural Resources Canada / Canadian Forest Service) |
| Collection | NFI Ground Plot documentation (data dictionary, sampling guidelines, compilation procedures) |
| Licence / notice | NFI copyright and non-commercial reproduction notice: https://nfi.nfis.org/en/notices — material may be reproduced for personal/public non-commercial use with attribution; commercial redistribution requires written permission. |
| Data access | **Plot data itself was NOT downloaded.** NFI ground plot data require the NFI Data Request Form and a signed Data Use Agreement (DUA), plus any applicable jurisdictional agreements. |
| Acquisition date | 2026-11-14 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage of documentation | National (NFI ground plot program) |
| Format | PDF |

## Source URLs and HTTP responses

HEAD probes run 2026-11-14 18:11 UTC. All three PDFs returned HTTP 200 with `Content-Type: application/pdf`; none returned HTML or an error payload.

| Local filename | URL | HTTP | Content-Type | Content-Length (bytes) | Last-Modified | Pages |
|----------------|-----|-----:|--------------|----------------------:|---------------|------:|
| `4a-GPDataDictionary5.2.pdf` | `https://nfi.nfis.org/resources/groundplot/4a-GPDataDictionary5.2.pdf` | 200 | `application/pdf` | 3,676,384 | 2021-04-20 | 180 |
| `Gp_guidelines_v5.0.pdf` | `https://nfi.nfis.org/resources/groundplot/Gp_guidelines_v5.0.pdf` | 200 | `application/pdf` | 3,737,514 | 2016-03-30 | 274 |
| `GP_compilation_procedures_2.4.pdf` | `https://nfi.nfis.org/resources/groundplot/GP_compilation_procedures_2.4.pdf` | 200 | `application/pdf` | 1,586,599 | 2021-11-01 | 92 |

Raw response headers are retained in `http_headers.txt` (1,944 bytes).

## Retrieved files

| Local filename | Bytes | SHA-256 | Status |
|----------------|------:|---------|--------|
| `4a-GPDataDictionary5.2.pdf` | 3,676,384 | `70d00a78200428bb931822069f59511bdceda4232da1946ca89ec1e18ee944d8` | downloaded, PDF 1.5, 180 pages |
| `Gp_guidelines_v5.0.pdf` | 3,737,514 | `6adfc5c6573861b323748f044496ded8ca99a222d894605026e6b059eec4b106` | downloaded, PDF 1.5, 274 pages |
| `GP_compilation_procedures_2.4.pdf` | 1,586,599 | `28b1cacf3f97a35fb96dc087417f061360ecf727cb25f3dd127301cba61f3f99` | downloaded, PDF 1.5, 92 pages |
| `http_headers.txt` | 5,069 | `8134f7c80b5ccc803e3633fe9f1f888c2d269e82ac12a08a12e2b98f54d46dd8` | supporting HTTP header transcript |

Total archived documentation: 9,002,441 bytes (8.59 MiB).

## What was NOT downloaded

The NFI ground plot **data** payload — tree measurements, site attributes, remeasurement tables, and reference pixels — is not openly downloadable. It requires a formal request and a DUA. No data payload was fetched, and no placeholder or synthetic data was written.

## Exact request route

1. Request form: **https://nfi.nfis.org/en/datarequestform**
   - The page embeds the actual NFI Data Request form from `https://nfi.nfis.org/NFIDataRequest/User_Form.jsp?lang=en`.
2. Explanatory page: **https://nfi.nfis.org/en/datarequest**
3. Contact: `nfisupport@nfis.org` (National Forest Inventory Projects Office).
4. The request is subject to NFI approval; the team will be contacted by the NFI Projects Office to complete the required documentation, including the MAGPlot/NFI Data User Agreement and any jurisdictional agreements.

The existing pre-submission DUA package is at `metadata/license-determinations/nfi-targeted-request.md` in the **parent repository** (not inside the `data` submodule). Its placeholder contact lines are intentionally left unchanged. This documentation archive does not execute or alter that request.

## Version note

The NFI documentation index (https://nfi.nfis.org/en/documentation, observed 2026-11-14) also lists newer ground plot data dictionaries (`4a-GPDataDictionary5.2.3.pdf`, version 5.2.3, and `4a-GPDataDictionary5.3.2.pdf`, version 5.3.2). This acquisition archives the three documents named in the task specification (5.2, guidelines 5.0, compilation procedures 2.4). A future refresh should pin the newer dictionary version before schema work begins.

## Reproduction

```bash
mkdir -p data/raw/nfi/ground_plots/documentation
cd data/raw/nfi/ground_plots/documentation
curl -fL --retry 3 -O https://nfi.nfis.org/resources/groundplot/4a-GPDataDictionary5.2.pdf
curl -fL --retry 3 -O https://nfi.nfis.org/resources/groundplot/Gp_guidelines_v5.0.pdf
curl -fL --retry 3 -O https://nfi.nfis.org/resources/groundplot/GP_compilation_procedures_2.4.pdf
sha256sum *.pdf
```
