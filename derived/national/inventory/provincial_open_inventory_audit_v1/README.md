# Provincial open forest-inventory audit v1

Retrieval date: 2026-11-23

This artifact audits open provincial/territorial forest inventories for the nine
E2 jurisdictions (AB, SK, MB, ON, NS, PE, NL, NT, NU). It records source,
licence, format, coverage, vintage and stand-vs-tree level, and verifies a small
sample of each directly accessible layer. It does **not** ingest full layers and
does **not** produce model inputs or synthetic stand attributes.

## Files

- `source_table.csv` / `source_table.json`: one row per source, including
  licence, access mode, URL, coverage, year, format and spatial level.
- `field_coverage.csv`: audited fields and their attribute role.
- `sample_stats.csv`: min/p25/median/p75/max/mean of numeric attributes in the
  checked-in samples. No values are imputed.
- `species_distribution.csv`: species or class counts in the samples.
- `gaps.csv`: licence, access, attribute and coverage gaps.
- `manifest.csv`: sample and full-artifact SHA-256 provenance.
- `samples/`: small (100-500 row) verified samples. Metadata-only samples are
  labelled in `source_table.csv`.

## Source and licence summary

- AB: AVI Crown, Open Government Licence - Alberta, direct FGDB download.
- SK: FRI Forest Stands, SK Standard Unrestricted Use Data Licence v2.0,
  ArcGIS REST.
- MB: Manitoba Forest Inventory 1970s, OpenMB Information and Data Use License,
  direct FGDB download.
- ON: FRI packaged products, Open Government Licence - Ontario; stand
  attributes require a LIDS account/order (metadata only in this audit).
- NS: Nova Scotia Forest Inventory, Open Government Licence - Nova Scotia,
  direct shapefile download.
- PE: Corporate Landuse Inventory 2010 and EFI2020, Open Government Licence -
  Prince Edward Island (EFI item licence metadata is blank; portal default).
- NL: FAL Land Cover - Newfoundland, Open Government Licence - Newfoundland and
  Labrador, ArcGIS REST.
- NT: ATLAS Wooded Areas, Open Government Licence - Northwest Territories,
  ArcGIS REST; community-scale broad class only.
- NU: no territorial forest inventory identified.

## Attribute coverage

Stand-level species, age and height are available for AB and MB (MB height is
absent); NS has species, height and volume but no age; SK has height and volume
but only a softwood/hardwood class; PE combines CLUI species/height with EFI
volume/height; NL and NT open layers lack the core attributes; ON stand
attributes are not directly open; NU has no inventory. See `gaps.csv` for the
consequence of each gap.

No request, DUA, restricted data, official OSeCAN change, UI change or model
change is involved. All samples are observations of published open layers; no
value is synthetic.
