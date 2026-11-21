# Provenance: BC public appraisal cost allowances

## 1. Scope and source boundary

This dataset extracts **published appraisal cost allowances** from three public
BC Government sources:

1. Interior Appraisal Manual (IAM), effective **2026-07-01**.
2. Coast Appraisal Manual (CAM), effective **2026-01-01**.
3. Interior Basic Silviculture Costs, quarterly sheets effective **2026-10-01**
   and **2026-07-01**.

Only public PDFs linked from the BC Timber Pricing Branch pages were used. No
ILCR, CCTMCS, bidder-level, licence-level, or other restricted microdata were
requested, downloaded, or used. No login, cookie, paywall bypass, or access
control circumvention was used.

- IAM page: <https://www2.gov.bc.ca/gov/content/industry/forestry/competitive-forest-industry/timber-pricing/interior-timber-pricing/interior-appraisal-manual>
- CAM page: <https://www2.gov.bc.ca/gov/content/industry/forestry/competitive-forest-industry/timber-pricing/coast-timber-pricing/coast-appraisal-manual-and-amendments>
- Interior basic silviculture page: <https://www2.gov.bc.ca/gov/content/industry/forestry/competitive-forest-industry/timber-pricing/interior-timber-pricing/interior-basic-silviculture-costs>
- Publisher: BC Timber Pricing Branch, Ministry of Forests.
- Copyright: BC Crown copyright. The documents are public; commercial
  reproduction or redistribution may require a licence from the Province.

## 2. Discovery

Retrieval window: **2026-11-21 20:46 UTC**.

1. Fetched the three current index pages with ordinary HTTP GET requests and a
   descriptive user agent.
2. Extracted all public PDF links. The IAM page linked
   `iam_2026_master_b.pdf` (effective 2026-07-01). The CAM page linked
   `cam_2026_master.pdf` (effective 2026-01-01). The silviculture page linked
   the quarterly series; the current sheet was `basic_silv_costs_oct_26.pdf`
   (effective 2026-10-01), with the prior quarter `basic_silv_costs_jul_26.pdf`
   (effective 2026-07-01).
3. Downloaded the three current PDFs plus the prior-quarter silviculture sheet
   for a consecutive-quarter comparison.
4. Every response was HTTP 200 and began with a PDF header. Page counts and
   hashes were checked after download.

### Discovery pages

| File | URL | Bytes | SHA-256 | Retrieved (UTC) |
|---|---|---:|---|---|
| `iam.html` | IAM index | 333,676 | `2b70efd4f2922196deba79843914bd8543693e66e869c8dd9d8f9337e2112f7d` | 2026-11-21T20:46:19+00:00 |
| `cam.html` | CAM index | 334,999 | `f12b961d2b5746fea6955cce3923231216f703276efd83853551e58c0dd011dc` | 2026-11-21T20:46:19+00:00 |
| `silv.html` | Silviculture index | 319,077 | `5d4508ae5f8aa011e573c08086504a221f125fed63d268656d3690ac662cbc9c` | 2026-11-21T20:46:20+00:00 |

## 3. Downloaded PDFs

| File | Manual/series | Effective date | Pages | Bytes | SHA-256 | Retrieved (UTC) |
|---|---|---|---:|---:|---|---|
| `iam_2026_master_b.pdf` | IAM 2026 | 2026-07-01 | 172 | 3,389,829 | `45b2bdb8f035f5032297420c6031d0aee1092838f2e257298884c9dab989fc22` | 2026-11-21T20:46:29+00:00 |
| `cam_2026_master.pdf` | CAM 2026 | 2026-01-01 | 145 | 2,455,492 | `dc88a581a4cc47e016d36b0eaeda2d714f20507ca8e0d845a4868af166e73824` | 2026-11-21T20:46:29+00:00 |
| `basic_silv_costs_oct_26.pdf` | Interior basic silviculture | 2026-10-01 | 1 | 190,228 | `35402ad60ce4e20f39c2d9e3de5f2c5e00771a957da22c869dbc34922146c882` | 2026-11-21T20:46:30+00:00 |
| `basic_silv_costs_jul_26.pdf` | Interior basic silviculture | 2026-07-01 | 1 | 197,650 | `bc8f38e8966296ee90b0fc325dc3473c28270191763859b8fb51de1a179342b9` | 2026-11-21T20:46:30+00:00 |

Direct URLs:

- IAM: <https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/forestry/timber-pricing/interior-timber-pricing/interior-appraisal-manual/iam_2026_master_b.pdf>
- CAM: <https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/forestry/timber-pricing/coast-timber-pricing/coast-appraisal-manual/cam_2026_master.pdf>
- October silviculture: <https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/forestry/timber-pricing/interior-timber-pricing/basic_silv_costs_oct_26.pdf>
- July silviculture: <https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/forestry/timber-pricing/interior-timber-pricing/basic_silv_costs_jul_26.pdf>

The PDFs were retained only in the local working directory
(`tmp/bc_appraisal_costs_raw/pdfs/`) and are not committed. The manifest retains
all URLs and hashes for re-fetch.

## 4. Extraction method

Tooling: Python 3.12, `pdfplumber` for positioned text/tables, `pdftotext` and
`pdfinfo` (Poppler 24.02.0) for independent page/text inspection. Parser:
`scripts/national/build_bc_appraisal_costs.py`.

The builder uses the following page map (PDF page numbers):

| Source | Table/section | PDF page |
|---|---|---:|
| IAM | Table 3-5 railway | 62 |
| IAM | Specified operations 3.3.1–3.3.2 | 61–63 |
| IAM | Table 4-1 FMA constants | 69 |
| IAM | 4.3.2.3 subgrade equations | 81 |
| IAM | 4.3.2.5 snow/ice roads | 82 |
| IAM | Table 4-3 culverts | 83 |
| IAM | Table 4-4 bridges | 84 |
| IAM | 4.3.4.1 stabilizing material | 87 |
| IAM | Table 4-6 road maintenance | 95 |
| IAM | 4.6 root disease control | 102 |
| IAM | Table 4-8 BEC silviculture | 104–105 |
| CAM | 4.4.1–4.4.4 specified operations | 54–55 |
| CAM | 4.4.5–4.4.6 long haul / HDC | 56 |
| CAM | 4.4.7 barging | 57 |
| CAM | Table 5-1 road costs | 74 |
| CAM | Table 5-2 log bridges | 76 |
| CAM | Table 5-3 permanent/portable bridges | 78 |
| CAM | Table 5-4 culverts | 79 |
| CAM | Table 5-6 BEC silviculture | 87 |
| CAM | 5.2/5.2.1 FPA and low volume | 62 |
| CAM | 5.4 road management | 82 |
| CAM | 5.7.1 root disease control | 88 |
| Basic silv. | October 2026 | 1 |
| Basic silv. | July 2026 | 1 |

Extraction rules:

- Text tables are parsed with anchored regexes and fixed expected row counts.
- Matrix tables (culverts, bridges, road costs) are parsed from positioned
  `pdfplumber` tables or from the printed row/column structure, then normalized.
- CAM bridge tables are published in **thousands of dollars**; values are
  multiplied by 1,000 and stored as `CAD/each`.
- IAM culvert Table 4-3 Part A is `CAD/each`; Part B is `CAD/m`. CAM Table 5-4
  Column A is installed `CAD/m`; Column B is materials-only `CAD/m`.
- No interpolation is performed. Published units and caps are retained.
- The builder fails closed on missing tables, unexpected row counts, duplicate
  keys, non-finite/negative values, or failed spot checks.

## 5. Spot checks against the PDFs

| Source | Table/component | Selector | Expected | Found | Result |
|---|---|---|---:|---:|---|
| IAM 2026 | Table 4-1 FMA constant | Skeena | 16.71 | 16.71 | pass |
| IAM 2026 | Table 4-8 basic silviculture | ICHmw1 | 2,973 | 2,973 | pass |
| IAM 2026 | Table 4-3 installed culvert | diameter 0.3 m | 963 | 963 | pass |
| IAM 2026 | 4.3.2.3 subgrade base | road group 12 | 18,975 | 18,975 | pass |
| CAM 2026 | Table 5-1 road cost | OMLB soft/medium | 72,601 | 72,601 | pass |
| CAM 2026 | Table 5-2 log bridge | span 4 m, single log sill | 1,300 | 1,300 | pass |
| CAM 2026 | Table 5-3 permanent bridge | span 2 m, abutment 0 | 52,700 | 52,700 | pass |
| CAM 2026 | Table 5-4 culvert | 1.8 m installed | 996 | 996 | pass |
| CAM 2026 | Table 5-6 silviculture | CWH | 2,178 | 2,178 | pass |
| Basic silv. 2026-10 | all-species average | North Central Zone | 10.02 | 10.02 | pass |
| Basic silv. 2026-07 | all-species average | North Central Zone | 9.95 | 9.95 | pass |

Additional manual checks:

- IAM Table 4-3 Part B 0.3 m supply-only = **57 CAD/m**; Part A 20 m × 1.8 m =
  **23,890 CAD**.
- CAM Table 5-2 span 20 m, crib 5 = **155.5 thousand = 155,500 CAD**.
- CAM Table 5-3 span 25 m, abutment 4 = **349.2 thousand = 349,200 CAD**.
- CAM 5.2 FPA = **21.56 CAD/m³** (scale); CAM 5.4 road management =
  **4.73 CAD/m³** (scale).
- IAM 3.3 helicopter = **94.31 CAD/m³**; horse = **8.67 CAD/m³**; skyline =
  **3.25 CAD/m³**.
- IAM 4.6 root disease control base = **1,114 CAD/ha**, clamped to
  **1,200–1,469 CAD/ha**.

## 6. Outputs and checks

- `bc_appraisal_costs.csv`: 879 rows, 599 Interior / 280 Coast.
- `bc_appraisal_coverage.csv`: 28 table/section rows.
- Unique key: 0 duplicates.
- No negative, NaN, infinite, or zero values.
- Regional reconciliation: FMA 6/6; road maintenance 22/22; CAM road 20/20;
  IAM culverts 182/182; CAM log bridges 85/85; CAM permanent bridges 120/120;
  CAM culverts 24 + 1; CAM silviculture 15/15; quarterly 7 + 7.
- `observation_type` is `appraisal_allowance` on every cost row.

## 7. Deliberate exclusions

- Restricted ILCR and CCTMCS microdata were not used.
- No tree-to-truck or general logging $/m³ allowance was fabricated; the public
  manuals do not publish one.
- No general truck-haul $/m³ table was fabricated; only rail/water/barge
  specified operations and cycle-time policy exist.
- ECE equipment/labour rates (Appendix I) were not converted into a unit
  allowance; ECE project costs are site-specific.
- The quarterly Interior silviculture sheet is by forest zone, not BGC. No BGC
  split was imputed.
- IAM Table 4-7/4-9 and CAM Table 5-5/5-7 factors are policy parameters, not cost
  rows; they are noted in coverage/manifest.
- Expired/invalid BEC variants in IAM Table 4-8 were excluded from the cost
  rows and are recorded here: MSxk (2017), BWBSdk1, BWBSmw1, ESSFdk,
  ESSFwc1, ICHdw, ICHdw2, IDFdk, MSdk1, PPdh2 (2018-10-31), ESSFwm (2019),
  IDFmw1 (2021-10-31), CWHms1 and IDFww1 (2027-03-31), SBSmk and ESSFxc
  (invalid codes).

## 8. Rebuild

```bash
python scripts/national/build_bc_appraisal_costs.py \
  --pdf-dir tmp/bc_appraisal_costs_raw/pdfs \
  --out-dir data/derived/national/harvest_basis/bc_appraisal_costs
```

Tests:

```bash
python -m pytest -q tests/test_bc_appraisal_costs.py
python -m ruff check scripts/national/build_bc_appraisal_costs.py
```
