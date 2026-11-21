# BC public log-market average prices

Standalone extraction of **observed mill-delivered log prices** from the public
BC Timber Pricing Branch Coast and Interior log-market reports. This dataset is
not merged into `forest_cost_revenue.csv`, the national ledger, or any UI.

- **Price basis:** `mill_delivered`
- **Currency basis:** `CAD_nominal` — nominal Canadian dollars of each report
  period; no inflation or deflation adjustment
- **Observation type:** `reported_market_average` — published averages, not
  transaction-level records
- **Geography:** `coast` and `interior` (British Columbia)
- **Period:** reports covering January 2019 through September 2026, as published
- **Units:** CAD per cubic metre (`price_cad_m3`), cubic metres (`volume_m3`),
  percent of report volume (`volume_share_pct`)
- **Status:** 505 public PDFs parsed; 15,705 reported price cells; no negative
  or NaN prices

## Files

| File | Rows | Purpose |
|---|---:|---|
| `bc_log_market_prices.csv` | 15,705 | Tidy observed price cells (one row per report × species × grade/sort × end use) |
| `bc_log_market_coverage.csv` | 505 | One row per source PDF: dates, reported/blank cells, totals status, source hash |
| `bc_log_market_sources.json` | 505 | Source URL, retrieval timestamp, SHA-256, size, region, basis, period |
| `manifest.json` | — | Inputs, discovery pages, outputs, validation summary, assumptions |
| `PROVENANCE.md` | — | Discovery, download, extraction, and spot-check audit trail |
| `README.md` | — | This file |

The full PDFs are not committed. `manifest.json` and
`bc_log_market_sources.json` retain the URL, retrieval timestamp, and SHA-256 of
every downloaded PDF so the corpus can be re-fetched and checked.

## Schema: `bc_log_market_prices.csv`

| Column | Meaning |
|---|---|
| `report_id` | Stable key: `{region}_{basis}_{log_class}_{period_end YYYY-MM}` |
| `region` | `coast` or `interior` |
| `report_basis` | `1_month` or `3_month` |
| `period_start`, `period_end` | Published reporting period; three-month reports use the printed date range |
| `log_class` | Coast: `old_growth` or `second_growth`; Interior: `not_reported` |
| `species` | Coast common species name; Interior species group (`SPF`, `Df-Larch`, `Hem-Bal`, `Cedar`, `White Pine`, `Yellow Pine`, `Deciduous`, `Other`) |
| `grade` | Coast grade letter (B–Z); blank for Interior product cells |
| `end_use` | Interior log product/end use (`sawlog`, `peelers`, `poles_house`, `minor_products`, `pulpwood`, `other`, `weighted_average`); blank for Coast |
| `price_cad_m3` | Published average market value (AMV) or average price, CAD/m³ |
| `currency_basis` | Always `CAD_nominal`; values are not inflation-adjusted |
| `price_basis` | Always `mill_delivered` |
| `observation_type` | Always `reported_market_average` |
| `is_aggregate` | Lowercase `true` only for Interior `weighted_average` rows; `false` otherwise. Exclude these aggregates when summing product cells |
| `price_status` | `reported` for every emitted row; blank cells are counted in coverage, not emitted as zero |
| `price_plausibility` | `ok`, `zero_cad_m3`, `below_1_cad_m3`, or `above_1000_cad_m3` |
| `volume_m3` | Directly reported volume for Interior product × species cells; blank for Coast grade cells |
| `volume_status` | `reported`, `blank_cell`, `not_reported_by_grade` (Coast), or `not_applicable` (Interior `weighted_average` row, which is price-only) |
| `volume_share_pct` | Coast published percent share for the grade × species cell; blank when not printed. The Interior schema has no share column |
| `volume_share_status` | `reported` or `blank_cell` for Coast; `not_applicable` for Interior |
| `report_total_volume_m3` | Report-level total volume, when published and internally consistent |
| `report_total_value_cad` | Report-level total value, when published and internally consistent |
| `report_avg_price_cad_m3` | Report-level average price |
| `report_totals_status` | `consistent`, `reported` (Interior), `inconsistent`, `not_reported_or_unparseable`, or `not_reported` |
| `source_document`, `source_url`, `source_sha256`, `retrieved_utc` | Source audit fields |

### Missing-value policy

A blank price cell is **not** a zero and is not emitted as a price row. It is
counted in `bc_log_market_coverage.csv`:

- `table_cells_possible` — grid cells implied by the report's grades/products ×
  species columns;
- `price_cells_reported` — cells with a printed numeric price;
- `price_cells_blank` — difference between the two.

Coast grade-level volume is not published. The Coast PDFs print only a species
volume total, and only for some species; those partial totals are not attached
to grade rows. Coast `volume_status` is therefore
`not_reported_by_grade`. Interior product × species volumes are published and
are recorded directly.

### Non-additivity rules

The published prices are averages over different samples and vintages. Apply
these rules before any aggregation:

1. **Never sum or average across `report_basis`.** A `1_month` report and a
   `3_month` report are independently published vintages, not components of one
   another. Their prices cannot be added or averaged.
2. **Never sum or average overlapping `3_month` reports.** Consecutive
   three-month windows share two months of transactions, so summing them
   double-counts volume and prices.
3. **Never reconstruct one basis from the other.** Do not sum `1_month` reports
   to reproduce a `3_month` report, or difference `3_month` reports to recover a
   `1_month` report; late and revised submissions are not reconciled.
4. **Never add Interior `weighted_average` rows to product rows.** Those rows
   carry `is_aggregate=true` and are report-level checks.
5. **Never sum Coast `volume_share_pct` across grades or species.** Each share is
   relative to its own grade's reported volume.

## Coverage

| Series | Reports | Period range | Gaps |
|---|---:|---|---|
| Coast 1-month old growth | 85 | 2019-01 to 2026-01 | none |
| Coast 1-month second growth | 84 | 2019-01 to 2026-01 | 2023-10 not listed on the archive page |
| Coast 3-month old growth | 84 | 2019-01 to 2025-12 | none |
| Coast 3-month second growth | 83 | 2019-01 to 2025-12 | 2021-03 not listed on the archive page |
| Interior 1-month | 85 | 2019-01 to 2026-09 | 2026-01 through 2026-08 not listed; current page shows 2026-09 |
| Interior 3-month | 84 | 2019-01 to 2025-12 | none |

The two Coast gaps and the Interior 2026 monthly gap are **missing from the
public archive pages at retrieval time**, not parser failures. No report was
imputed or back-filled.

Six Coast 1-month second-growth PDFs (`2023-09`, `2023-11`, `2023-12`, `2024-01`,
`2024-02`, `2024-03`) print the footer labels one text row above their values.
Their grade prices and shares parse normally, but the printed report totals
cannot be assigned unambiguously. Those reports keep
`report_totals_status=not_reported_or_unparseable`; their totals are not
reconstructed from the shifted labels.

Blank-cell rates are high by construction because the PDFs print only cells with
enough participants. Coast: 13,128 priced cells out of 54,120 possible grade ×
species cells. Interior: 2,577 priced cells out of 9,464 possible product ×
species cells (including the species weighted-average row; `is_aggregate=true`).

## Validation

- No negative or NaN prices; hard range check `0 <= price <= 2000` CAD/m³.
- Coast volume shares are hard-checked against `0 <= volume_share_pct <= 100`;
  footer rows are excluded from the grade table so `Species %` and the species
  volume line cannot overwrite a grade share.
- 15,665 prices in the ordinary range, 16 exact zeros, 7 non-zero values below
  CAD 1/m³, and 17 above CAD 1,000/m³. The extremes are retained with
  `price_plausibility` flags rather than truncated.
- Unique key `(report_id, species, grade, end_use)`: 0 duplicates.
- Interior volume cross-check: for all 169 Interior reports, the sum of parsed
  product × species volumes equals the printed `Total/Avg` volume within 2 m³
  (rounding only).
- Interior price cross-check: volume-weighted parsed prices reproduce the printed
  `Wtd. Average` within CAD 0.01/m³ for all 169 reports.
- Five independent manual spot checks are recorded in `PROVENANCE.md`.

## Limitations

- **Averages, not transactions.** The PDFs publish average market values for
  domestic log sales. They cannot support transaction-level distributions,
  bidder-level analysis, or exact species/grade volumes where suppressed.
- **Coast old growth is a blend.** The Coast old-growth reports state that the
  reported value is a blend of old and mixed growth transactions under ministry
  policy. `log_class=old_growth` therefore means the published old-growth
  series, not a pure old-growth sample.
- **Nominal CAD.** `price_cad_m3` is nominal Canadian dollars for each report
  period (`currency_basis=CAD_nominal`). No CPI or other deflator is applied, so
  prices from different years are not real-dollar comparable without an external
  adjustment.
- **Publication lag and revisions.** Three-month totals may not equal the sum of
  previously published one-month totals because of late or revised submissions.
  The dataset preserves each PDF as published and does not reconcile vintages.
- **Coast participant-expansion break (April 2023).** Coast reports published
  from April 2023 onward carry Note (2): *"April 2023, new and additional
  participants to the Vancouver Log Market data set."* This is a
  participant-expansion structural break; published levels before and after the
  break are not directly comparable, and this dataset makes no adjustment.
- **Suppressed grades and volumes.** Blank cells mean “not printed”, not “zero”.
  Coast grade-level volumes are unavailable. Coast species volume totals are
  partial in some reports.
- **Interior product mix.** Interior prices are product/end-use specific
  (sawlog, peeler, poles/house, minor products, pulpwood, other).
  `weighted_average` rows are emitted as species-level aggregates with
  `is_aggregate=true`; they support report-level checks and must not be added to
  or averaged with product cells.
- **No quality adjustment.** Species and grade labels are those printed in the
  PDFs. No grade is inferred, split, or renamed beyond spelling normalization.
- **Coverage as published.** The public archive does not list every month for
  every series; see the gaps table. Absence is recorded, not filled.
- **Copyright.** The source PDFs are BC Crown copyright and carry a
  research/private-study restriction. This derived dataset retains the source
  attribution and should be used for research with the same caveat; commercial
  redistribution requires the Province's permission.

## Regeneration

```bash
python scripts/national/build_bc_log_market.py \
  --raw-dir tmp/bc_log_market_raw \
  --out-dir data/derived/national/harvest_basis/bc_log_market
```

The builder expects `pdfs/`, `tsv/`, `text/`, `pages/`, `download_log.json`, and
`extra_sources.json` under `--raw-dir`. It uses `pdftotext` (Poppler) and does
not require network access once the corpus is staged.

Tests:

```bash
.venv/bin/python -m pytest tests/test_bc_log_market.py -q
.venv/bin/ruff check scripts/national/build_bc_log_market.py tests/test_bc_log_market.py
```
