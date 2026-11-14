# Newfoundland and Labrador FAL Permanent Sample Plots — Acquisition Record — 2026-11-14

## Identity

| Field | Value |
|-------|-------|
| Publisher | Newfoundland and Labrador Department of Fisheries, Forestry and Agriculture (FAL) |
| Dataset | FAL Permanent Sample Plots |
| Service | `https://services8.arcgis.com/aCyQID5qQcyrJMm2/arcgis/rest/services/FAL_-_Permanent_Sample_Plots/FeatureServer` |
| ArcGIS item | `6672099533d34409b7c221cc0a5b803d` (service `currentVersion` 12) |
| Licence | Open Government Licence — Newfoundland and Labrador |
| Coverage | Newfoundland and Labrador; 412 mature + 968 immature plots |
| Temporal coverage | Visit dates 1985–2026; plot origin years 1680–2015 as recorded |
| Format | 2 point feature layers (GeoJSON) + 12 attribute tables (CSV), all gzipped |
| Access tier | Tier 1 open ArcGIS REST; no credentials, request form, or DSA |
| Acquisition date | 2026-11-14 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |

The FeatureServer has 14 layers: two point feature classes (`Mature`,
`Immature`) and twelve tables (`Age Group`, `Disturbance History`,
`Remeasurement`, `Immature Trees Remeasurement`,
`Immature Sample Trees Remeasurement`, `Immature Trees Permanent`,
`Mature Trees Permanent`, `Mature Trees Remeasurement`, `Plot Layout`,
`Plot Location Description`, `Remeasurement Crew Date`,
`Silviculture History`). All 14 were exported.

## Retrieval

Layer inventory and counts were read with `?f=json` and
`query?where=1%3D1&returnCountOnly=true&f=json`. Each layer was then paged:

```text
<layer>/query
  ?where=1%3D1
  &outFields=*
  &orderByFields=OBJECTID
  &resultOffset=<offset>
  &resultRecordCount=2000
  &returnGeometry=false
  &f=json
```

The two point layers used `f=geojson` with `outSR=4326` and
`returnGeometry=true`. `orderByFields=OBJECTID` stabilises paging. Each page's
feature count was compared with the layer `returnCountOnly` value; any
mismatch or duplicate OBJECTID aborts the export. Tables were written to CSV
with the layer's field order; points were written as a single GeoJSON
FeatureCollection. Every output was compressed with `gzip -9 -n`.

Observed layer `maxRecordCount` is 2,000 (service root reports 1,000).
`supportedQueryFormats` is `JSON, geoJSON, PBF`; `f=csv` is not supported, so
CSV was generated from the JSON attributes.

## Retrieved files

`features` is the verified row/feature count; every file matches its
`returnCountOnly` value.

| File | Layer | Features | Gzip bytes | SHA-256 (gzip) |
|------|-------|---------:|-----------:|----------------|
| `mature.geojson.gz` | Mature (points) | 412 | 41,687 | `84339e08814afcd7a060c90e23d01978657b7f905d6878ad20fca2cf9c2c8741` |
| `immature.geojson.gz` | Immature (points) | 968 | 95,737 | `33c4b9ad3b2b0a0c5b9419f7a86454b26bb33e60cd0aa4b42f69d76d31a01efb` |
| `age_group.csv.gz` | Age Group | 592 | 21,010 | `e90737d0fb60a40525959b2c2ffafe5ed8a39658553b59dfd981e8baebfc5865` |
| `disturbance_history.csv.gz` | Disturbance History | 470 | 15,273 | `481e25586af53aa1725fcaa29a166be5245d81e2a0682a1a0377d40bb25f1e3a` |
| `remeasurement.csv.gz` | Remeasurement | 7,660 | 331,393 | `f847eb2158a0fdcf831712e9a512c0567ec8f9e6d06ca8c3a95d1a5fac8c18f2` |
| `immature_trees_remeasurement.csv.gz` | Immature Trees Remeasurement | 588,865 | 18,999,350 | `85250c34d7fbea07cac908396fafbd63c0cbb349ebc0519af3683954289a143f` |
| `immature_sample_trees_remeasurement.csv.gz` | Immature Sample Trees Remeasurement | 52,651 | 1,688,351 | `a8423d0126cef1f1a7e994d9a78e465bdd469628f0b7f3f13b1901b6ec72ac6e` |
| `immature_trees_permanent.csv.gz` | Immature Trees Permanent | 107,785 | 3,102,163 | `6d2cd05907ece6ecfd637420e5d9bae78d463e5419e87c4097dc6c87ac808bde` |
| `mature_trees_permanent.csv.gz` | Mature Trees Permanent | 35,500 | 1,028,658 | `a644e058d9101950fe5fdc653c92834201106d2c0e2df615fd2b10826dd94807` |
| `mature_trees_remeasurement.csv.gz` | Mature Trees Remeasurement | 186,783 | 5,914,635 | `ed2fc488cf14c0e0c92e0bc41143ef80e8cc5e1bd7d62be854bf220f2e0b1975` |
| `plot_layout.csv.gz` | Plot Layout | 6,628 | 204,539 | `f6687abae595395010114fab9c3e4240945bcc49fbd7e7fa5b45a97d3c94c4bd` |
| `plot_location_description.csv.gz` | Plot Location Description | 1,351 | 104,717 | `ee8e1bf332c494b8e22e01fae899db3119632c3235413537b7d1731107d7f8dd` |
| `remeasurement_crew_date.csv.gz` | Remeasurement Crew Date | 7,659 | 233,971 | `b62aff40024091fc5d3b8ce5de45fb5e3f580c4ae49c2d10d1f1137cb68b6126` |
| `silviculture_history.csv.gz` | Silviculture History | 430 | 13,873 | `abdde0ca0347edfa404a3847f2dfc2eb44ece170781c1188b70897989801caec` |

Total tree-measurement rows: **775,648** (mature 186,783 + immature
588,865). Total permanent-tree rows: **143,285**. Total gzipped payload:
32.9 MB (about 83.6 MB uncompressed).

Service and layer metadata are in `metadata/` (`service.json`, 14
`layer_XX_<name>.json` files, and `export_manifest.json`).

## What the package contains

- **Plot locations** — `mature` (412) and `immature` (968) point layers.
  Attributes include `PLOTKEY`, `DISTRICT`, `TYPEID`, `INTERPSPEC`,
  `INTERPAGE`, `INTERPHEIGHT`, `INTERPSITE`, `YEAROFORIGIN`,
  `STANDORIGIN`, `PLOTSTATUS`, topography, surficial geology, and comments.
- **Visits** — `remeasurement` (7,660 rows) records each plot visit with
  `REMEASUREMENT` number, actual species/age-class/height-class/crown-density/
  site class, stand status, plot length/width/size, and comments. There are
  1,242 remeasured plots and 138 single-visit plots. One row has a null
  `PLOTKEY` (OBJECTID 14105) and no usable measurements.
- **Tree measurements** — `mature_trees_remeasurement` (186,783) and
  `immature_trees_remeasurement` (588,865). DBH is in centimetres and
  height in metres. `TREESTATUS` is a state code, not a binary flag
  (mature: 0 live no defects, 1 dead standing, 2 dead leaning/down,
  3 live leaning, 4 live down, 5 dead broken, 6 live broken, 7 live dead top,
  8 live lateral takeover, 9 not located; immature: 0 live, 1 dead,
  9 missing/cut). Tree identity is `PLOTKEY` + `TREENUMBER`.
- **Permanent tree lists** — `mature_trees_permanent` (35,500) and
  `immature_trees_permanent` (107,785) carry `SPECIES` and, for mature plots,
  `AGEGROUP`. These are the species key for the remeasurement tables.
- **Age and height samples** — `age_group` (592 rows, all 412 mature plots;
  `SAMPLEAGE`, `DBH`, `TREEHEIGHT`) and
  `immature_sample_trees_remeasurement` (52,651 rows; `TREEAGE`,
  `CROWNHEIGHT`).
- **Disturbance and silviculture** — `disturbance_history` (470 rows on 361
  plots; type, year, severity) and `silviculture_history` (430 rows on 410
  plots; treatment type and year).
- **Plot layout and access** — `plot_layout` (6,628 rows on 1,326 plots;
  subplot direction/azimuth/distance) and `plot_location_description`
  (1,351 rows on 1,342 plots; free-text directions). 39 plots lack location
  text.

Detailed counts and profiling are in `CONTENTS.md`.

## Method notes and limitations

- **Live service, no version number.** Counts and attributes can change.
  Re-run `returnCountOnly` and re-hash before reuse. This snapshot includes
  the 2026 field season (latest visit 2026-11-04).
- **Dates are epoch milliseconds.** They are midnight in Newfoundland local
  time; converting in UTC shifts New Year's Day visits to the previous year.
  All years in `CONTENTS.md` use `America/St_Johns`.
- **One null visit record.** The `remeasurement` table has 7,660 rows but
  only 7,659 usable visits; OBJECTID 14105 has a null `PLOTKEY` and no plot
  measurements. The crew-date table has 7,659 rows and joins to every usable
  visit.
- **Species are simplified codes.** The permanent-tree lists carry 14 codes
  (`bF`, `bS`, `wB`, `wS`, `tL`, `OH`, `tA`, `rM`, `9`, `yB`, `jP`, `nS`,
  `wP`, `OP`), dominated by balsam fir and black spruce. The plot layers carry
  25 (mature) and 39 (immature) interpreted composition strings such as
  `bFbS`; these are not tree-level species.
- **DBH and height gaps.** Mature DBH is populated for 88.5% of rows and
  height for 20.2%; immature DBH for 86.4% and height for 75.8%. Height is
  much better on live trees (mature 26.5%, immature 90.2%) than on dead trees
  (mature 2.7%, immature 29.4%).
- **Sentinel and domain gaps.** A single mature dead-tree height is 99 (the
  maximum), which is not a credible metre value and should be treated as a
  sentinel. `PLOTSIZE` has no coded domain; recorded values are 2–100
  (interpreted as square metres, mature mode 40, immature 2–10).
  `CAUSEOFDEATH` includes lowercase `w`/`x` variants alongside `W`/`X`.
- **Plot origin years** range 1680–2010 for mature and 1880–2015 for
  immature as recorded; some are older than the visit record and should be
  checked before use.
- **No numeric site index.** Site productivity is represented by
  `INTERPSITE` (H/G/M/P), `ACTUALSITE` (H/G/M/P), and `DAMMONSITETYPE`;
  age is available from `age_group` and sample trees. A numeric site index
  must be derived.

## Citation

Newfoundland and Labrador Department of Fisheries, Forestry and Agriculture.
2026. *FAL Permanent Sample Plots* [FeatureServer]. ArcGIS Online.
https://services8.arcgis.com/aCyQID5qQcyrJMm2/arcgis/rest/services/FAL_-_Permanent_Sample_Plots/FeatureServer
(accessed 2026-11-14). Open Government Licence — Newfoundland and Labrador.
