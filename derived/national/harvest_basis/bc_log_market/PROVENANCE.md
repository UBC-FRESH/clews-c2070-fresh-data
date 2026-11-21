# Provenance: BC public log-market price extraction

## 1. Scope and source boundary

This dataset extracts the **published average prices** in the BC Ministry of
Forests' public Coast and Interior log-market reports. It uses only public PDFs
linked from the two government index pages. It does **not** use, request, or
bypass access controls for ILCR or CCTMCS microdata, and it does not log in to
any system.

- Coast index:
  <https://www2.gov.bc.ca/gov/content/industry/forestry/competitive-forest-industry/timber-pricing/coast-timber-pricing/coast-log-market-reports>
- Interior index:
  <https://www2.gov.bc.ca/gov/content/industry/forestry/competitive-forest-industry/timber-pricing/interior-timber-pricing/interior-log-market-reports>
- Publisher: BC Timber Pricing Branch, Ministry of Forests.
- Copyright: BC Crown copyright. The PDFs state that the material is for
  private study/research and that commercial reproduction or redistribution
  requires a licence from the Province.

## 2. Discovery

Retrieval window: **2026-11-21 20:30–20:32 UTC**.

1. Fetched both current index pages with an ordinary HTTP GET and a descriptive
   user agent. No authentication, cookies, or paywall bypass was used.
2. Extracted the yearly "historical versions" links for 2019–2025 from each
   index page.
3. Fetched those 14 archive pages and enumerated every `*.pdf` link.
4. De-duplicated 502 archive links by URL and downloaded each PDF.
5. Also downloaded the three current-index PDFs not present in the archive
   inventory: `1mc_jan_26.pdf`, `1m2gc_jan_26.pdf`, `1mi_sept_26.pdf`.
6. Every response was HTTP 200 and began with a PDF header; no HTML error page
   was accepted as a PDF.

All 16 discovery pages (2 current + 14 archive) and 505 PDFs are hash-recorded
in `manifest.json` (`discovery.index_and_archive_pages` and `inputs`).
Per-PDF URL, timestamp, size, and SHA-256 are also in
`bc_log_market_sources.json`.

| Discovery page | SHA-256 |
|---|---|
| Coast current index | `fac48fc930e4d998621ce4963cc42160988d8a4e170fdca7fab5c59c701c418b` |
| Interior current index | `921a6443f19644ba2b54bc96d85a1b4d29b0434499a6c5c92e9e6348c462576e` |
| 14 yearly archive pages | See `manifest.json` |

Corpus digest (SHA-256 of sorted `filename:sha256` lines over all 505 PDFs):

```
bc8ef0c5623d5d5ea4ee137d95458f18239340f18a8fdb6a815a7d6933d01b38
```

Downloaded corpus size: **55,882,938 bytes** across **505 PDFs**.

### Series inventory

| Region | Basis | Log class | PDFs |
|---|---|---|---:|
| Coast | 1-month | old growth | 85 |
| Coast | 1-month | second growth | 84 |
| Coast | 3-month | old growth | 84 |
| Coast | 3-month | second growth | 83 |
| Interior | 1-month | not reported | 85 |
| Interior | 3-month | not reported | 84 |
| **Total** | | | **505** |

## 3. Extraction method

For each PDF:

```bash
pdftotext -layout report.pdf report.txt
pdftotext -tsv report.pdf report.tsv
```

Poppler version 24.02.0. The TSV word boxes are used for column assignment;
the layout text is used for dates, titles, and manual cross-checks.

### Coast table

- Header row contains `Grade` and ten species columns: Alder, Birch, Cedar,
  Cottonwood, Cypress, Fir, Hembal, Maple, Pine, Spruce.
- Grade rows B–Z each carry an `AMV` price row and a `%` volume-share row.
- The grade table ends at the first footer row (`Volume(m3)`, `Volume`,
  `Species %`, or `Total volume`). That row and every row below it are excluded
  from grade cells, so the footer species volumes and the footer `Species %`
  shares cannot overwrite the last grade's share cells.
- Numeric cells are assigned to the species column whose header-left boundary
  interval contains the cell's **right edge**. This is necessary because the
  published table right-aligns values while headers are not consistently
  centred; naive nearest-header matching shifts the last columns.
- Example of the alignment trap: in `1mc_jan_26.pdf`, grade H prints
  `92.85` at x-right 883.0, inside the Pine header interval (840.0–903.4),
  not the Spruce interval (903.4+). The parser keeps it as Pine; Spruce is
  blank for that grade.

### Interior table

- Header row contains `SPF`, `Df-Larch`, `Hem-Bal`, `Cedar`, `White Pine`,
  `Yellow Pine`, `Deciduous`, `Other`, `Total/Avg`.
- Volume block and average-price block each have six product rows: Sawlog,
  Peelers, Poles/House, Minor Products, Pulpwood, Other; plus `Total` (volume)
  and `Wtd. Average` (price).
- `Total/Avg` column is an aggregate and is not emitted as a species.
- `Total` volume row is used only as a report-level check; it is not emitted.
- `Wtd. Average` rows **are emitted** as species-level `weighted_average` rows
  with `is_aggregate=true`. They are report-level checks and must not be added
  to or averaged with the product cells.
- `-` means not reported, not zero.

### Non-additivity and nominal currency

- Every `price_cad_m3` value is nominal Canadian dollars of its published report
  period (`currency_basis=CAD_nominal`). No deflator is applied.
- `1_month` and `3_month` reports are independent vintages. Never sum or average
  prices across `report_basis`.
- Consecutive `3_month` windows overlap by two months. Never sum or average
  overlapping three-month reports.
- Do not reconstruct a `3_month` report by summing `1_month` reports, or a
  `1_month` report by differencing `3_month` reports.
- Never add Interior `weighted_average` rows to product rows, and never sum
  Coast `volume_share_pct` across grades or species.

### Dates and classes

- Coast period is parsed from `For the {1,3} month period ending: ...`.
- Interior period is parsed from `Report for the month of ...` or
  `Report for the 3 month period of ... to ...`.
- Three-month periods use the printed start and end dates, including the
  occasional printed end date of the 30th.
- Coast old-growth PDFs carry the published note that the series is a blend of
  old and mixed growth transactions under ministry policy. The dataset labels
  the series `old_growth` but does not claim a pure old-growth sample.
- Coast reports published from April 2023 onward print Note (2): *"April 2023,
  new and additional participants to the Vancouver Log Market data set."* This
  is a participant-expansion structural break. Published levels before and after
  the break are not directly comparable; the dataset preserves the reports as
  published and makes no adjustment.

## 4. Manual spot checks

All checks compare the printed PDF line with the parsed CSV row.

| # | PDF | Printed value | Parsed value | Result |
|---|---|---|---|---|
| 1 | `1mc_jan_19.pdf`, grade H, old growth | Cedar 327.36 (22.39%); Cypress 194.92 (22.05%); Fir 210.19 (18.43%); Hembal 97.69 (10.69%); Pine 53.11 (6.36%); Spruce 150.61 (20.07%) | Same six species, prices and shares | PASS |
| 2 | `1m2gc_jan_26.pdf`, grade H, second growth | Cedar 477.59 (15.10%); Fir 172.44 (6.97%); Hembal 141.24 (10.19%); Spruce 70.38 (21.94%) | Same four species, prices and shares | PASS |
| 3 | `1mi_jan_21.pdf`, Sawlog | SPF 100.23 / 1,284,117 m³; Df-Larch 109.98 / 333,513 m³; Hem-Bal 93.32 / 61,062 m³; Cedar 181.55 / 45,261 m³ | Same prices and volumes | PASS |
| 4 | `3mi_dec_19.pdf`, Sawlog | SPF 85.60 / 1,826,621 m³; Df-Larch 92.35 / 490,200 m³; Hem-Bal 81.86 / 93,884 m³; Cedar 149.31 / 102,297 m³ | Same prices and volumes | PASS |
| 5 | `1m2gc_sept_23.pdf`, grade Y, second growth | Fir 51.83 (0.14%); footer `Species %` row prints the Fir species volume 125,344.26 | Fir price 51.83 and share 0.14; footer row excluded from grade cells | PASS |

Additional independent checks over all 169 Interior reports:

- Sum of parsed product × species volumes equals the printed `Total/Avg`
  volume within **2 m³** (rounding).
- Volume-weighted parsed prices reproduce the printed `Wtd. Average` within
  **CAD 0.01/m³**.

## 5. Missing reports and blank cells

- Coast 1-month second growth: archive page does not list **2023-10**.
- Coast 3-month second growth: archive page does not list **2021-03**.
- Interior 1-month: current page lists **2026-09**; archive pages end at 2025-12,
  so 2026-01 through 2026-08 are not present.
- All other monthly sequences are complete for the published ranges.

Blank price cells are counted in `bc_log_market_coverage.csv`. They are not
zero-filled, interpolated, or carried forward. Coast grade-level volumes are
not published; only partial species volume totals are printed, so no coast
grade volume is inferred.

Six Coast 1-month second-growth PDFs (`2023-09`, `2023-11`, `2023-12`, `2024-01`,
`2024-02`, `2024-03`) print the footer labels one text row above their values.
The grade table still parses, but the printed report totals cannot be assigned
unambiguously. These reports are kept with
`report_totals_status=not_reported_or_unparseable`; the totals are not
reconstructed from shifted labels.

## 6. Build and verification

- Builder: `scripts/national/build_bc_log_market.py`
- Tests: `tests/test_bc_log_market.py` with TSV/text fixtures copied from
  `1mc_jan_26`, `1m2gc_sept_23`, and `1mi_sept_26`
- Ruff: `ruff check` and `ruff format --check` pass on the builder and tests
- Validation in the builder: hard-fails on negative, NaN, or >2,000 CAD/m³
  prices; Coast volume shares outside `0–100`; duplicate observation keys;
  missing/unknown report layout; or a filename/document basis mismatch
- Build result: **505 reports parsed, 0 failures, 15,705 emitted price rows**
- No ledger, model, or UI file was modified.

## 7. Reproduction

```bash
python scripts/national/build_bc_log_market.py \
  --raw-dir tmp/bc_log_market_raw \
  --out-dir data/derived/national/harvest_basis/bc_log_market
```

The raw corpus is not committed; re-fetching the hashed URLs listed in
`bc_log_market_sources.json` reproduces the inputs. `pdftotext` is the only
non-Python tool required.
