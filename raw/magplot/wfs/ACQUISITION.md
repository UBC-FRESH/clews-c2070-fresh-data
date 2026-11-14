# MAGPlot WFS Supplement — Acquisition Record — 2026-11-14

## Purpose

The open MAGPlot v1.2 ZIP package (`../MAGPlot_latest_data_package.zip`) omits
Prince Edward Island, contains only 171 Saskatchewan sites, and does not match
the live WFS site population for Newfoundland and Labrador. This supplement
captures the province-level site summaries and the tree-measurement layers for
Saskatchewan, Prince Edward Island, and Newfoundland and Labrador from the
public NFIS MAGPlot WFS.

The WFS is a live service. The payloads here are a dated snapshot, not a
versioned release.

## Identity

| Field | Value |
|-------|-------|
| Publisher | National Forest Inventory Canada / Natural Resources Canada |
| Service | `https://ca.nfis.org/mapserver/cgi-bin/magplot_trees_eng.cgi` |
| Service title | MAGPlot Sites and Trees |
| WFS version | 2.0.0 |
| Default CRS | `urn:ogc:def:crs:EPSG::3978` (NAD83 / Alberta 10-TM Forest) |
| Licence | Open Government Licence — Canada (`ca-ogl-lgo`) |
| Retrieval date | 2026-11-14, 18:37–18:44 UTC |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Access tier | Tier 1 open WFS. Published geometry is the same approximate-location product as the open MAGPlot release. |

Capabilities snapshot: `wfs_capabilities.xml` (92,714 bytes, SHA-256
`c2e457524e5e0214e6c86458a5480959db851aa4a288a28fd26dc548f8a35e0d`).

## Feature types

The capabilities document advertises 39 feature types: one `Sites_Summary`
layer, 22 BC tree layers, 2 NB layers, 1 NFM layer, 2 NL layers, 1 PEI layer,
6 QC layers, 3 SK layers, and 1 YT layer. Only the following layers were
retrieved for this supplement.

| Layer | Title | Measurement coverage |
|-------|-------|----------------------|
| `ms:Sites_Summary` | Site Summaries | All provinces |
| `ms:SK_Trees_Measure_Num_0` | SK Trees Measurement 0 | SK meas 0 |
| `ms:SK_Trees_Measure_Num_1` | SK Trees Measurement 1 | SK meas 1 |
| `ms:SK_Trees_Measure_Num_2_8` | SK Trees Measurement 2–8 | SK meas 2–8 |
| `ms:PEI_Trees_Measure_Num_0_11` | PEI Trees Measurement 0–11 | PEI meas 0–11 |
| `ms:NL_Trees_Measure_Num_0_2` | NL Trees Measurement 0–2 | NL meas 0–2 |
| `ms:NL_Trees_Measure_Num_3_9` | NL Trees Measurement 3–9 | NL meas 3–9 |

## Retrieval method

WFS 2.0 `GetFeature` requests with `outputFormat=text/csv`.

- `Sites_Summary` returned all 41,840 features in one request (`count=50000`).
- The tree layers are capped by MapServer at 100,000 features per request.
  They were paged with `count=100000&startIndex=N` and
  `sortBy=magp_web_key`. The sort key is required: unsorted paging produced
  identical rows duplicated across page boundaries (717 duplicates in the
  first SK layer attempt). With `sortBy=magp_web_key`, all pages were disjoint
  and every layer returned exactly the `numberMatched` count from
  `resultType=hits`.
- Each page's repeated CSV header was removed before concatenation.
- CSV geometry is WKT in EPSG:3978.

Base request template:

```text
https://ca.nfis.org/mapserver/cgi-bin/magplot_trees_eng.cgi
  ?service=WFS&version=2.0.0&request=GetFeature
  &typeNames=ms:<layer>
  &outputFormat=text/csv
  &count=100000&startIndex=<offset>&sortBy=magp_web_key
```

## Retrieved files

All CSV payloads are gzipped with `gzip -9 -n` so that git-annex stores them as
binary objects. `feature_count` is the WFS `numberMatched` value and the
verified CSV data-row count.

| File | Layer | Features | Gzip bytes | SHA-256 (gzip) |
|------|-------|---------:|-----------:|----------------|
| `sites_summary.csv.gz` | `ms:Sites_Summary` | 41,840 | 1,643,267 | `20c9dacb4cfebc56f806dac8145e630ec666f041bea00a87ed837b5cb40cbde6` |
| `sk_trees_measure_num_0.csv.gz` | `ms:SK_Trees_Measure_Num_0` | 403,953 | 4,763,464 | `2d4b94b2e91ae744b2dd348de229e3be8b14551e0b7c927b2b1ee2e955bad2c1` |
| `sk_trees_measure_num_1.csv.gz` | `ms:SK_Trees_Measure_Num_1` | 269,189 | 3,322,350 | `f0083c31053da0a9f53d3ee2b9e0a9ca70612fcac0d35c751ae1f0d033be5dbf` |
| `sk_trees_measure_num_2_8.csv.gz` | `ms:SK_Trees_Measure_Num_2_8` | 339,429 | 4,243,245 | `14d37cacdc34cf63db61e32ca31dedcdd07376abba7f503523ccbed1b67f8b11` |
| `pei_trees_measure_num_0_11.csv.gz` | `ms:PEI_Trees_Measure_Num_0_11` | 275,204 | 3,368,887 | `c9625884a36426d2a52aee553399dd0426c89cc266528080cc5f598034f5808f` |
| `nl_trees_measure_num_0_2.csv.gz` | `ms:NL_Trees_Measure_Num_0_2` | 313,531 | 4,116,727 | `9715ed6d49df996cf1468215ac7b7898a4442ed8af512a96652725e2dc64bb79` |
| `nl_trees_measure_num_3_9.csv.gz` | `ms:NL_Trees_Measure_Num_3_9` | 298,786 | 3,924,513 | `21ce361fcfd7cd113964abd752729acc3275591a3bb73e817d9fe7ef2f0cb56b` |

Total tree-measurement features: **1,900,092**.

## Site-count reconciliation

The ZIP counts below were recomputed from `magp_sites.csv` inside
`../MAGPlot_latest_data_package.zip`; they match the counts in
`../MAGPlot_CONTENTS.md`.

| Province | ZIP `magp_sites` | WFS `Sites_Summary` | Difference | Common IDs | ZIP-only | WFS-only |
|----------|-----------------:|--------------------:|-----------:|-----------:|---------:|---------:|
| BC | 16,517 | 16,517 | 0 | 16,517 | 0 | 0 |
| QC | 12,892 | 12,892 | 0 | 12,892 | 0 | 0 |
| NB | 7,609 | 7,609 | 0 | 7,609 | 0 | 0 |
| NL | 1,350 | 1,321 | **−29** | 1,282 | 68 | 39 |
| YT | 327 | 327 | 0 | 327 | 0 | 0 |
| NT | 262 | 262 | 0 | 262 | 0 | 0 |
| SK | 171 | 2,219 | **+2,048** | 171 | 0 | 2,048 |
| MB | 2 | 2 | 0 | 2 | 0 | 0 |
| PE | 0 | 691 | **+691** | 0 | 0 | 691 |
| **Total** | **39,130** | **41,840** | **+2,710** | **39,062** | **68** | **2,778** |

The WFS is not a strict superset of the ZIP for NL. Only 1,282 of 1,350 ZIP NL
site IDs are present in the WFS summary; 68 ZIP NL IDs are absent and 39
different NL IDs appear. The net NL change is −29. The WFS supplement therefore
adds 2,048 SK sites, 691 PE sites, and 39 NL site IDs, while 68 ZIP NL site IDs
remain available only through the ZIP.

## Tree-layer coverage

Distinct site counts are computed from `magp_site_id`. Year ranges are from
`meas_year`. ``Plot types`` counts distinct `plot_type_id` values in the layer.

| Layer | Features | Distinct sites | Plot types | Measurement years |
|-------|---------:|---------------:|-----------:|-------------------|
| SK meas 0 | 403,953 | 2,046 | 3 | 1949–1999 |
| SK meas 1 | 269,189 | 1,433 | 3 | 1954–2019 |
| SK meas 2–8 | 339,429 | 983 | 3 | 1959–2019 |
| **SK union** | **1,012,571** | **2,046** | — | **1949–2019** |
| PEI meas 0–11 | 275,204 | 687 | 1 | 1976–2018 |
| NL meas 0–2 | 313,531 | 1,297 | 1 | 1985–2022 |
| NL meas 3–9 | 298,786 | 1,220 | 1 | 1985–2022 |
| **NL union** | **612,317** | **1,297** | — | **1985–2022** |

Coverage reconciliation:

- **SK**: the tree layers cover 2,046 of the 2,219 WFS SK site records. All 171
  ZIP SK site IDs are represented. 173 WFS SK site records have no tree rows.
- **PEI**: the tree layer covers 687 of the 691 WFS PEI site records; 4 site
  records have no tree rows. The ZIP has no PEI records.
- **NL**: the tree layers cover 1,297 distinct site IDs. Of these, 28 site IDs
  are absent from the WFS `Sites_Summary`, and 52 `Sites_Summary` NL site IDs
  have no tree rows. Only 1,258 of the 1,350 ZIP NL site IDs appear in the WFS
  tree layers; 92 ZIP NL site IDs are not represented.

## Schema differences from the ZIP tables

| Table | WFS columns | ZIP columns | Notes |
|-------|------------:|------------:|-------|
| Sites | 41 | 10 | WFS adds `WKT`, `source_plot`, full disturbance/treatment blocks, `leading_genus_by_stem_cnt`, `meas_years`, `num_measurements`, and `meas0_trees`…`meas12_trees`. WFS lacks ZIP `latitude`, `longitude`, and `flag_sites`. |
| Trees | 25 | 29 | WFS adds `WKT`, `magp_web_key`, `meas_year`, `meas_month`, `meas_plot_size`, `num_measurements`. WFS lacks ZIP `meas_num`, `tree_id_meas`, `tree_id_treemeas`, `species_gs`, and the six `flag_*` QA columns. |

Integration consequences:

- WFS tree records must be keyed on `magp_web_key`; the ZIP `meas_num` must be
  reconstructed from `meas_year`/`meas_month` or from the per-site measurement
  ordering.
- WFS tree layers carry no `flag_species`, `flag_status`, `flag_ts.vs.cc`,
  `flag_ts.vs.sc`, `flag_cc.vs.sc`, or `flag_count_trees`. QA flags from the
  ZIP cannot be applied to WFS-only records.
- WFS sites have no `flag_sites`; coordinate suppression status must be
  inferred from geometry validity or from the ZIP where the site ID matches.

## Known limitations

- **Live, unversioned service.** Feature counts and identifiers can change
  without notice. Re-run `resultType=hits` and re-hash before reuse.
- **Paging requires a sort key.** Unordered `startIndex` paging duplicates rows
  across page boundaries. Any refresh must use `sortBy=magp_web_key` or an
  equivalent stable order.
- **Site-ID mismatch for NL.** The WFS site summary and tree layers are not
  fully consistent with each other or with the ZIP. Do not assume that a WFS
  tree site has a WFS site-summary record, or vice versa.
- **No Alberta, Ontario, or Nova Scotia layers.** The WFS exposes the same
  provincial coverage gaps as the open MAGPlot release for those provinces.
- **Approximate or suppressed locations.** The service is the open product;
  exact plot coordinates still require the NFI Data Request Form and
  jurisdictional approvals.

## Reproduction

```bash
mkdir -p data/raw/magplot/wfs
cd data/raw/magplot/wfs
curl -fL -o wfs_capabilities.xml \
  'https://ca.nfis.org/mapserver/cgi-bin/magplot_trees_eng.cgi?service=WFS&request=GetCapabilities'

# Sites_Summary (single request)
curl -fL -G 'https://ca.nfis.org/mapserver/cgi-bin/magplot_trees_eng.cgi' \
  --data-urlencode 'service=WFS' --data-urlencode 'version=2.0.0' \
  --data-urlencode 'request=GetFeature' \
  --data-urlencode 'typeNames=ms:Sites_Summary' \
  --data-urlencode 'outputFormat=text/csv' \
  --data-urlencode 'count=50000' -o sites_summary.csv

# Tree layers: page with startIndex and sortBy=magp_web_key.
# See PROVENANCE.csv for the layer list; concatenate pages after removing
# repeated headers, then gzip -9 -n.
```

## Citation

National Forest Inventory Canada. 2026. MAGPlot Sites and Trees, WFS 2.0.0
service. `https://ca.nfis.org/mapserver/cgi-bin/magplot_trees_eng.cgi`
(accessed 2026-11-14).
