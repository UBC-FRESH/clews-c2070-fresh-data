# Quebec BMMB delivered-to-destination auction results

**Status:** extracted public snapshot, 2026-11-21. `policy_grade=false`;
this is an observed auction sample, not a provincial delivered-price deck.

**Source:** Bureau de mise en marché des bois (BMMB), Ministère des
Ressources naturelles et des Forêts du Québec, archived auction results:
<https://bmmb.gouv.qc.ca/Auction/Auctions/Archive> and the bulk export
<https://bmmb.gouv.qc.ca/Auction/Auctions/Export?IsArchive=True>.

**Bottom line.** The public archive contains 18 `Livré à destination`
(delivered to destination) sales, all ending in 2011, 2012, 2014, or 2015.
Thirteen were awarded and have an observed total sale value. Eleven of those
have a computable CAD/m3 rate; the two 2012 awards are partial awards, so only
a lower bound is published.

**Crown vs non-Crown.** Only nine of the eleven computable sales are Crown
public-forest sales. They cover 74,550 m3 and give a volume-weighted
**35.7547 CAD/m3** at 57.3% pulpwood. The other two are
`Forêt d'enseignement et recherche` lots (15,350 m3, 75.6% sawlog,
**50.6266 CAD/m3**). Pooling all eleven sales gives **38.2940 CAD/m3**, which
the two non-Crown lots raise by **+2.54 CAD/m3**; the 38.2940 figure is not a
Crown benchmark unless this split is shown.

The archive does not publish a species- or grade-specific price for these
lots. The prices are nominal CAD and must not be treated as stumpage or as a
confirmed mill-gate log price.

## Files

| File | Rows | Purpose |
|---|---:|---|
| `bmmb_delivered_sales.csv` | 18 | One row per delivered sale, including unsold offers and the observed aggregate price. |
| `bmmb_delivered_species_volume.csv` | 156 | Supporting unpriced species x product volume lines for the same sales. Sums to the sale volume; carries **no** allocated price. |
| `bmmb_sale_type_summary.csv` | 46 | Sale counts, offered volume, awarded volume, observed value, rate, and `currency_basis=CAD_nominal` by sale type and year. Delivered, `Récolté`, and both standing types are separate rows; notes record that result-PDF checks cover delivered sales only. |
| `manifest.json` | — | Machine-readable source URLs, HTTP metadata, hashes, counts, `rate_breakdown`, `reoffer_links`, validation, and output hashes. |
| `PROVENANCE.md` | — | Human-readable retrieval and field-provenance record. |

## Coverage

| Dimension | Observed delivered subset |
|---|---|
| Sales offered | 18 |
| Sales awarded | 13 |
| Sales with an observed price | 13 |
| Sales with a computable full rate | 11 |
| Sales with a partial-award lower bound only | 2 |
| Years | 2011, 2012, 2014, 2015 |
| BMMB sales regions | Sud-Est (11), Centre-Sud (4), Sud-Ouest (3) |
| UAs | 01151, 01152, 01251, 01252, 01253, 01254, 031050, 04151, 07151, 07251 |
| Tenure/provenance | `Forêt publique` (16), `Forêt d'enseignement et recherche` (2) |
| Species groups with volume | 14 (see `bmmb_delivered_species_volume.csv`) |
| Quality/grade | **not reported** (`quality=NA`) |
| Offered volume | 159,850 m3 (137,650 m3 excluding 22,200 m3 re-offer overlap) |
| Awarded volume | 108,750 m3 (100,450 m3 excluding 8,300 m3 awarded re-offer) |
| Observed sale value | 3,878,958.50 CAD nominal |
| Value with a computable rate | 3,442,633.50 CAD over 89,900 m3 |
| Volume-weighted computable rate, all 11 sales | 38.2940 CAD/m3 |
| Volume-weighted computable rate, Crown only (9 sales) | 35.7547 CAD/m3 |

The computable individual sale rates range from 30.1042 to 51.3995 CAD/m3
(median 36.6668; unweighted mean 38.3490). The 2012 partial awards have
lower bounds of 10.6588 and 39.0211 CAD/m3 using total offered volume; these
are not full rates.

## Crown vs non-Crown rate

| Segment | Sales | Volume | Value (CAD nominal) | Weighted rate | Product mix |
|---|---:|---:|---:|---:|---|
| Crown public forest (`Forêt publique`) | 9 | 74,550 m3 | 2,665,515.50 | **35.7547 CAD/m3** | 57.3% pulpwood / 42.7% sawlog |
| Teaching/research (`Forêt d'enseignement et recherche`) | 2 | 15,350 m3 | 777,118.00 | **50.6266 CAD/m3** | 24.4% pulpwood / 75.6% sawlog |
| All computable sales | 11 | 89,900 m3 | 3,442,633.50 | 38.2940 CAD/m3 | 51.7% pulpwood / 48.3% sawlog |

The all-sale rate is **+2.54 CAD/m3** above the Crown-only rate because the two
non-Crown teaching/research lots are sawlog-rich and priced higher. Use
35.7547 CAD/m3 for a Crown delivered-price benchmark. The manifest publishes
the same split under `rate_breakdown`.

## Re-offers and volume overlap

Two 2012-07-20 sales re-offer unsold timber from 2012-06-27 sales at the same
sector coordinates:

| Later sale | Re-offers | Overlap | Status of later sale |
|---|---|---:|---|
| `CS201207001` | `CS201206004` (Hackett Ouest, 10,550 m3, partial award) | 8,300 m3 | Awarded, partial award |
| `SO201207001` | `SO201206009` (Lac à l'Ours, 16,650 m3, unsold) | 13,900 m3 | Unsold |

The repeated timber is 8,300 + 13,900 = **22,200 m3**. The sales file carries
`reoffer_of_sale_id` on the two later sales and a reverse
`reoffered_by_sale_id` note on the two earlier sales. Do not add `volume_m3`
across a linked pair: the unique offered volume is 159,850 - 22,200 =
137,650 m3, and the unique offered volume on awarded rows is 108,750 - 8,300 =
100,450 m3. Both re-offer rows are excluded from the computable rate (one
partial award, one unsold), so the 11-sale rate itself is not duplicated.

## Sale-type separation

The archive export reports exactly four sale types. They are never collapsed:

| Source label | Family in this dataset | Treatment |
|---|---|---|
| `Livré à destination` | `delivered_to_destination` | Delivered sale total; the only rows eligible for a delivered price observation. |
| `Récolté` | `harvested_recolte_unspecified` | Separate. Basis is not documented as delivered; not used as a delivered price. |
| `Sur pied selon mesurage` | `standing_measured` | Separate. Standing/stumpage sale; **not** delivered. |
| `Sur pied selon inventaire` | `standing_inventory` | Separate. Standing/inventory sale; **not** delivered. |

`bmmb_sale_type_summary.csv` records `is_delivered=1` only for
`Livré à destination`; all other types have `is_delivered=0` and a
`value_semantics` beginning with `standing_` or `recolte_`. Every summary row
also carries an explicit `rate_unit_basis`; only delivered rows use
`CAD_per_m3_delivered_destination`.

## Method

1. Download the public archive export and archive page; record status,
   content type, byte count, SHA-256, and retrieval time in `manifest.json`
   and `PROVENANCE.md`.
2. Read the legacy `.xls` export (`Sheet0`, 3,796 data rows, 142 columns)
   with `xlrd`. The parser fails if the export hash, row count, column set, or
   sale-type vocabulary changes.
3. Filter the sale type **exactly** to `Livré à destination`. No fuzzy match;
   `Récolté` and standing sales are excluded from the delivered table.
4. Parse one sale per row. `Prix de vente` is the total lot value, not a
   per-m3 price. Compute the rate only when the offered and awarded volumes
   are the same.
5. For two awarded 2012 sales the export has a blank `Prix de vente`; read
   the linked public result PDFs, verify their SHA-256, and use the published
   total. Parse the printed phrase
   `*Certains volumes de bois offerts sont non-adjugés.` to set
   `partial_award=1`; do not infer the flag from the mere presence of a PDF.
6. Parse the species/product volume columns into the supporting unpriced
   table. Verify that the species volumes sum to the sale volume. Do not
   allocate the sale price across species or products.
7. Cross-check the export price against the result text on the public detail
   page for all 11 priced sales that do not use a result PDF. A missing page
   fails extraction, and `detail_prices_match_export` is recorded only when
   all 11 checks cover the expected sale IDs.
8. Validate no negative or non-finite volume/price, no duplicate sale IDs,
   sale-type separation, year consistency, species-volume reconciliation,
   summary reconciliation to the export, the two re-offer links, the
   Crown/non-Crown rate split, and full coverage of all 3,796 source rows.

## Field notes

`bmmb_delivered_sales.csv`:

| Field | Meaning |
|---|---|
| `sale_id` | BMMB call-for-tenders number. |
| `sale_year` | Year encoded in `sale_id`; `auction_end_year` is the date field. Both are recorded. |
| `region_bmmb`, `ua` | Source sales region and unité d'aménagement; no external administrative-region mapping is inferred. |
| `tenure` | Source `Provenance` value. |
| `volume_m3` | Mandatory offered volume. `volume_optional_m3` is separate and is zero for all delivered rows. |
| `total_cad` | Observed total sale value for awarded sales; blank for unsold offers. |
| `price_cad_m3` | `total_cad / volume_m3` only when the full offered volume was awarded. |
| `price_cad_m3_lower_bound` | For partial awards only: `total_cad / volume_m3`, a lower bound because some offered volume was not awarded. |
| `price_unit_basis` | `CAD_per_m3_delivered_destination` or `not_computable_partial_award_volume`. |
| `observed` | 1 only when an awarded sale has a published total price. |
| `observation_type` | `observed_sale_price`, `offer_estimate_only`, or `not_awarded_no_price`. |
| `price_source` | `archive_export:Prix_de_vente` or `result_pdf:Prix_de_vente`. |
| `estimated_total_cad`, `estimated_cad_m3` | Pre-auction `Prix estimé`; never treated as observed. |
| `product_scope` | `sawlog_and_pulpwood` for all delivered lots. |
| `species_scope`, `quality`, `aggregation_level` | `ALL_SPECIES_MIXED`, `NA`, `sale_total`. |
| `partial_award` | 1 when the result PDF prints `*Certains volumes de bois offerts sont non-adjugés.` |
| `reoffer_of_sale_id` | Prior sale whose unsold timber this row re-offers; blank unless the sale is one of the two linked 2012-07-20 re-offers. |
| `notes` | Machine-readable flags, including `service_bundle_not_published=1`, `destination_not_reported=1`, `not_stumpage=1`, and `not_mill_gate_confirmed=1`. Re-offer rows also carry `reoffer_overlap_m3`, and the prior rows carry `reoffered_by_sale_id`. |

`bmmb_delivered_species_volume.csv` carries observed volume only. Its
`price_cad_m3` and `total_cad` fields are intentionally blank; `quality=NA`.
It must not be joined to the sale price as if the price were a species rate.

## Validation

All checks in `manifest.json` pass:

- source row count 3,796 and delivered row count 18;
- delivered table contains only `Livré à destination`;
- no duplicate sale IDs;
- no negative or non-finite volume or price;
- every awarded delivered sale has an observed total;
- every unsold delivered sale has no price;
- partial-award rows have no full rate and do have a labelled lower bound;
- sale year equals auction end year for the delivered subset;
- species volume lines reconcile exactly to each sale's mandatory volume;
- the sale-type summary reconciles to the full export for row count and volume,
  and every summary row records `currency_basis=CAD_nominal`;
- the two re-offer links reconcile to their declared 22,200 m3 overlap;
- the Crown/non-Crown rate split reproduces 35.7547 and 50.6266 CAD/m3;
- all 11 non-PDF priced sales are covered by detail-page price checks when
  detail pages are supplied; `detail_prices_match_export` is recorded only
  then.

## Limitations

- **Only 18 delivered sales exist; the newest ends in 2015.** This is not a
  current price deck and not a representative sample of Quebec Crown harvest.
- **No grade and no species price.** All delivered prices are lot totals. The
  species table is unpriced. Do not assign DER/F1-F4 or another grade.
- **Destination is not published.** The detail page does not publish a
  delivery destination field; the `Destination :` input is only a Google Maps
  directions box. Delivery terms are inside the unparsed tender documents.
  The price point is "delivered to destination", not a confirmed mill gate.
- **Service bundle is not published.** The sale type implies delivered wood;
  the archive does not state whether harvest, haul, or both are included.
- **Two 2012 awards are partial.** Both result PDFs print
  `*Certains volumes de bois offerts sont non-adjugés.`; that phrase sets
  `partial_award=1`. No awarded volume is published, so the lower bounds are
  not full rates and are excluded from the volume-weighted rate.
- **The 38.2940 CAD/m3 all-sale rate is not Crown-only.** Two non-Crown
  teaching/research lots raise it by 2.54 CAD/m3 over the Crown-only
  35.7547 CAD/m3. Always show the split above before comparing with Crown
  benchmarks.
- **Nominal CAD only.** Years 2011, 2012, 2014, and 2015 are not deflated.
  Do not mix them with 2023-dollar MERIS model inputs without a documented
  deflator.
- **Auctioned volume only.** BMMB volume is a sample of Crown volume, not the
  provincial harvest population.
- **Two sales are on a teaching/research forest.** `CS201408201` and
  `CS201506201` carry `Forêt d'enseignement et recherche`, not
  `Forêt publique`. They are retained, flagged in `tenure` and `notes`, and
  reported as a separate rate segment.
- **Two 2012-07-20 sales re-offer earlier unsold timber.** `CS201207001` and
  `SO201207001` repeat 22,200 m3 from `CS201206004` and `SO201206009`; use
  the unique-volume totals above rather than summing all 18 rows.

## Merge recommendation

**Do not merge this file into `forest_cost_revenue.csv` in v2b.** These rows
are a useful observed benchmark, but the current ledger grain requires a
species/product/quality price, and this source only supports one aggregate
sale total.

If a future ledger extension accepts sale-level delivered observations:

- `source=qc_bmmb_sales`
- `component=delivered_log_revenue`
- `species=ALL`, `product=mixed_log`, `quality=NA`
- `aggregation_level=sale_total`
- `value_basis=observed_sale:mill_gate` **only if** the destination is
  separately confirmed as a mill; otherwise the current enum cannot represent
  "delivered to unspecified destination" and the row should remain a
  benchmark, not a ledger row.
- For a Crown comparison, use the nine `Forêt publique` computable sales
  (35.7547 CAD/m3); keep the two teaching/research lots in a separate
  non-Crown segment.
- `confidence=medium` for full-rate rows, `low` for partial-award lower
  bounds.
- `volume_m3` is a sale weight, not a harvest observation.
- Keep `currency_basis=CAD_nominal` and deflate explicitly before comparison
  with MERIS `model_input` rows.

Never use `Récolté` or any `Sur pied` row as a delivered price. Never
allocate the aggregate sale price across the species volume lines.

## Reproduction

The raw files are not committed. Re-download them and run:

```bash
.venv/bin/python scripts/national/extract_bmmb_delivered.py \
  --export tmp/bmmb/export_archive.raw \
  --details-dir tmp/bmmb/details \
  --detail-meta tmp/bmmb/detail_meta.tsv \
  --pdf-dir tmp/bmmb
```

The parser fails closed if the export SHA-256 or byte count differs from the
snapshot recorded in `manifest.json`.
