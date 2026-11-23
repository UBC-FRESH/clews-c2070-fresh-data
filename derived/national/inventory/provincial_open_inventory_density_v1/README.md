# Provincial open inventory density v1

Small committed density evidence tables for E2 v3.  No request,
DUA, restricted data or official OSeCAN input is used.

| Province | Target stems/ha | Evidence | Basis |
|---|---:|---|---|
| AB | 1000.00 | proxy | proxy_default |
| SK | 2033.65 | open_inventory | area_weighted_median |
| MB | 2050.00 | donor | donor_median_plot_density |
| NS | 1409.82 | open_inventory | area_weighted_median |
| PE | 802.84 | open_inventory | area_weighted_median |
| ON | 1000.00 | proxy | proxy_default |
| NL | 1000.00 | proxy | proxy_default |
| NT | 1000.00 | proxy | proxy_default |
| NU | 1000.00 | proxy | proxy_default |

SK uses BA/QMD-implied total stem density with MSTEMS as a
merchantable-stem cross-check.  NS uses TOTBA/AVDI-implied total
stem density with TOTMRVOL as the volume check.  PE uses EFI2020
merchantable trees/ha with gtv as the volume check.

AB AVI publishes density and structure classes, not stems/ha, so the
AB target is a labelled 1,000 stems/ha proxy.  MB uses the median
measured donor plot density.  ON, NL, NT and NU retain the labelled
1,000 stems/ha proxy.

Full AB, NS, SK and PE layers are not redistributed; only the small
evidence tables and source hashes are committed.
