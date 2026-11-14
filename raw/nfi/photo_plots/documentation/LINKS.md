# NFI Photo Plot — Links and Archive Status

Observed 2026-11-14 from `https://nfi.nfis.org/en/documentation` (archived as `nfi_documentation_page.html`). The nominal photo-plot landing page `https://nfi.nfis.org/en/photo_plot` returns an HTTP 200 response whose body is the site's "404 error — Page not found" shell (archived as `photo_plot_page.html`); it contains no photo-plot links.

## Photo-plot documentation links

| Title (from index) | Version | URL | HTTP | Bytes | Archived locally |
|--------------------|---------|-----|-----:|------:|------------------|
| Photo Plot Data Dictionary | 6.1 | `https://nfi.nfis.org/resources/photoplot/PP_Data_Dictionary_6.1.pdf` | 200 | 1,912,721 | `PP_Data_Dictionary_6.1.pdf` |
| Photo Plot Data Dictionary | 5.2 | `https://nfi.nfis.org/resources/photoplot/Pp_data_dictionary_5.2.pdf` | 200 | 2,115,017 | `Pp_data_dictionary_5.2.pdf` |
| Photo Plot Data Dictionary | 4.2.4 | `https://nfi.nfis.org/resources/photoplot/Pp_data_dictionary_4.2.4.pdf` | 200 | 303,061 | `Pp_data_dictionary_4.2.4.pdf` |
| Land Cover Classification | 4.0.1 | `https://nfi.nfis.org/resources/photoplot/Land_cover_classification_v4.0.1.pdf` | 200 | 211,954 | `Land_cover_classification_v4.0.1.pdf` |
| Photo Plot Compilation Procedures | 1.4 | `https://nfi.nfis.org/resources/photoplot/Pp_compilation_v1.4.pdf` | 200 | 174,306 | `Pp_compilation_v1.4.pdf` |
| Photo Plot Interpretation Examples (English) | — | `https://nfi.nfis.org/resources/photoplot/Photoplot_interpretation_examples_English_version.xlsx` | 200 | 239,672,490 | **No** — link only; large binary workbook |

## Page and access links

| Purpose | URL | HTTP | Archived locally |
|---------|-----|-----:|------------------|
| Nominal photo-plot page (broken) | `https://nfi.nfis.org/en/photo_plot` | 200 (404 body) | `photo_plot_page.html` |
| Documentation index (source of links) | `https://nfi.nfis.org/en/documentation` | 200 | `nfi_documentation_page.html` |
| NFI data request explanation | `https://nfi.nfis.org/en/datarequest` | 200 | `datarequest_page.html` |
| NFI data request form | `https://nfi.nfis.org/en/datarequestform` | 200 | Not archived as HTML; the form is embedded from `https://nfi.nfis.org/NFIDataRequest/User_Form.jsp?lang=en` |
| NFI notices (copyright / reproduction) | `https://nfi.nfis.org/en/notices` | 200 | Not archived |
| French photo-plot page | `https://nfi.nfis.org/fr/photo-plot` | Not checked | Not archived |

## Request route (photo plot data)

Photo-plot data are not openly downloadable. Use the NFI Data Request Form at `https://nfi.nfis.org/en/datarequestform`, complete the follow-up documentation and DUA, and state the photo-plot product required. Contact: `nfisupport@nfis.org`. The existing pre-submission DUA package is `metadata/license-determinations/nfi-targeted-request.md` in the parent repository; its placeholder contact lines are unchanged.

## Notes

- The documentation index also hosts ground-plot and general NFI documents; only the photo-plot section is reproduced here.
- The 239.7 MB interpretation-example workbook is recorded but not archived. If it becomes necessary for interpreter training or QA, download it separately and add a row to `PROVENANCE.csv`.
- The broken `/en/photo_plot` page is a source-side defect. The archive intentionally retains the error body as evidence rather than presenting it as documentation.
