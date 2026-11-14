# NFI Photo Plot Documentation — Acquisition Record — 2026-11-14

## Identity

| Field | Value |
|-------|-------|
| Publisher | National Forest Inventory Canada (Natural Resources Canada / Canadian Forest Service) |
| Collection | NFI photo-plot interpretation documentation (data dictionaries, land-cover classification, compilation procedures, interpretation examples) |
| Licence / notice | NFI copyright and non-commercial reproduction notice: https://nfi.nfis.org/en/notices — material may be reproduced for personal/public non-commercial use with attribution; commercial redistribution requires written permission. |
| Data access | **Plot data itself was NOT downloaded.** NFI photo-plot data require the NFI Data Request Form and a signed Data Use Agreement (DUA), plus any applicable agreements. |
| Acquisition date | 2026-11-14 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage of documentation | National (NFI photo-plot program) |
| Format | PDF, HTML snapshots; one linked XLSX not archived |

## Important access note: the specified page is broken

`https://nfi.nfis.org/en/photo_plot` was requested on 2026-11-14. The server returned **HTTP 200** but the response body is the NFI site's **"404 error — Page not found"** shell (23,418 bytes). The page is linked from the site navigation but has no photo-plot content. The error body was archived as `photo_plot_page.html`; it was **not** treated as documentation.

The photo-plot documents were instead located on the NFI documentation index at `https://nfi.nfis.org/en/documentation` (HTTP 200, 29,234 bytes, archived as `nfi_documentation_page.html`). The index's photo-plot section links the five PDFs below. This is recorded as a documented source-page failure, not silently substituted.

## Source URLs and HTTP responses

HEAD probes run 2026-11-14 18:13 UTC for the PDFs; GET snapshots for the HTML pages.

| Local filename | URL | HTTP | Content-Type | Content-Length (bytes) | Last-Modified | Pages |
|----------------|-----|-----:|--------------|----------------------:|---------------|------:|
| `PP_Data_Dictionary_6.1.pdf` | `https://nfi.nfis.org/resources/photoplot/PP_Data_Dictionary_6.1.pdf` | 200 | `application/pdf` | 1,912,721 | 2025-07-21 | 118 |
| `Pp_data_dictionary_5.2.pdf` | `https://nfi.nfis.org/resources/photoplot/Pp_data_dictionary_5.2.pdf` | 200 | `application/pdf` | 2,115,017 | 2018-04-05 | 114 |
| `Pp_data_dictionary_4.2.4.pdf` | `https://nfi.nfis.org/resources/photoplot/Pp_data_dictionary_4.2.4.pdf` | 200 | `application/pdf` | 303,061 | 2016-04-18 | 30 |
| `Land_cover_classification_v4.0.1.pdf` | `https://nfi.nfis.org/resources/photoplot/Land_cover_classification_v4.0.1.pdf` | 200 | `application/pdf` | 211,954 | 2016-04-18 | 19 |
| `Pp_compilation_v1.4.pdf` | `https://nfi.nfis.org/resources/photoplot/Pp_compilation_v1.4.pdf` | 200 | `application/pdf` | 174,306 | 2016-04-18 | 14 |
| `photo_plot_page.html` | `https://nfi.nfis.org/en/photo_plot` | 200 (404 body) | `text/html; charset=UTF-8` | 23,418 | — | — |
| `nfi_documentation_page.html` | `https://nfi.nfis.org/en/documentation` | 200 | `text/html; charset=UTF-8` | 29,234 | — | — |
| `datarequest_page.html` | `https://nfi.nfis.org/en/datarequest` | 200 | `text/html; charset=UTF-8` | 21,620 | — | — |

## Retrieved files

| Local filename | Bytes | SHA-256 | Status |
|----------------|------:|---------|--------|
| `PP_Data_Dictionary_6.1.pdf` | 1,912,721 | `e540cdda33d41fdbefc54dbed0abe98b1a3551fa2755f6fb0839fe8af811fca6` | downloaded, PDF 1.7, 118 pages |
| `Pp_data_dictionary_5.2.pdf` | 2,115,017 | `66a01bda3c1702e303993aa24f01a7c31331f97ca41bdf0549e9470c4d28649d` | downloaded, PDF 1.5, 114 pages |
| `Pp_data_dictionary_4.2.4.pdf` | 303,061 | `7ae6078b37aa25242b52a55315f26f83ddbb5182b014a78d42c8688b58b04c90` | downloaded, PDF 1.4, 30 pages |
| `Land_cover_classification_v4.0.1.pdf` | 211,954 | `0fec07025da7835cb0fe9d062765a3430104e43ee07ecda9c47b79e1327f47c2` | downloaded, PDF 1.2, 19 pages |
| `Pp_compilation_v1.4.pdf` | 174,306 | `902618c3f1ce92aade5b5ee2f8f27cb3dbbc0f8e36c04e3c2f42d4376dfc0acd` | downloaded, PDF 1.2, 14 pages |
| `photo_plot_page.html` | 23,418 | `3eaf0d091caebd97915a9c71089c28fe5e77fada0eb3e1ee6fab552bdcd1168c` | archived 404-error body from the specified page |
| `nfi_documentation_page.html` | 29,234 | `a09ba9ef935e186a5fab9677bf7c6142eb4252773641ea3841e372e08bd3901b` | archived documentation index (source of the links) |
| `datarequest_page.html` | 21,620 | `9b3603b48cf49031649daa67630420e85b82069351e42ac3f4f35f0a40aaf700` | archived request explanation page |
| `http_headers.txt` | 5,069 | `81e57cc94fddb768ba6155e6a14f017efd39f2e8286677e8f307ead89212ec8a` | supporting HTTP header transcript |

Total archived files: 4,796,400 bytes (4.57 MiB).

## Linked but not archived

| Resource | URL | Size | Reason not archived |
|----------|-----|-----:|---------------------|
| `Photoplot_interpretation_examples_English_version.xlsx` | `https://nfi.nfis.org/resources/photoplot/Photoplot_interpretation_examples_English_version.xlsx` | 239,672,490 | Large binary interpretation-example workbook; link and size recorded in `LINKS.md`; not needed for schema/calibration work now. |

## Exact request route

1. Request form: **https://nfi.nfis.org/en/datarequestform**
   - Embeds `https://nfi.nfis.org/NFIDataRequest/User_Form.jsp?lang=en`.
2. Explanatory page: **https://nfi.nfis.org/en/datarequest** (archived as `datarequest_page.html`).
3. Contact: `nfisupport@nfis.org` (National Forest Inventory Projects Office).
4. Requests are subject to NFI approval and a signed DUA. The existing pre-submission package is `metadata/license-determinations/nfi-targeted-request.md` in the parent repository; its placeholder contact lines were not modified.

## What was NOT downloaded

No NFI photo-plot data payload (plot attributes, interpreted land-cover records, or reference pixels) was downloaded. Only public documentation and page snapshots are archived.

## Reproduction

```bash
mkdir -p data/raw/nfi/photo_plots/documentation
cd data/raw/nfi/photo_plots/documentation
curl -fL --retry 3 -O https://nfi.nfis.org/resources/photoplot/PP_Data_Dictionary_6.1.pdf
curl -fL --retry 3 -O https://nfi.nfis.org/resources/photoplot/Pp_data_dictionary_5.2.pdf
curl -fL --retry 3 -O https://nfi.nfis.org/resources/photoplot/Pp_data_dictionary_4.2.4.pdf
curl -fL --retry 3 -O https://nfi.nfis.org/resources/photoplot/Land_cover_classification_v4.0.1.pdf
curl -fL --retry 3 -O https://nfi.nfis.org/resources/photoplot/Pp_compilation_v1.4.pdf
sha256sum *.pdf
```
