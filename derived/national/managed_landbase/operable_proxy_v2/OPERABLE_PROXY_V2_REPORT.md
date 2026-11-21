# National Operable Landbase Proxy v2

**Status: screening proxy. This is not a legal timber harvesting landbase (THLB), not an AAC landbase, and not an operability model.**

Generated: 2026-11-21T20:32:35+00:00  
Runtime: 281.6 s  
Grid: 30 m SCANFI pixels aggregated to 990 m blocks.

## Method

1. Start from the v1 operable proxy: SCANFI treed classes 5/6/7, merchantability >= 5 m height, >= 20 Mg/ha biomass, >= 10% closure, and the v1 managed share.
2. Add SCANFI median-age screens at >= 20 and >= 30 years, excluding younger stands.
3. Add an NBAC 2020 annual fire screen; burned merchantable pixels are excluded.
4. Add NRN nearest-public-road distance classes at 5, 10, and 20 km and a 20 km access screen.
5. Report each screen alone and two combined cores. No slope/operability screen is applied because no national DEM is present.

Age, burn, and road screens are applied to the v1 merchantable surface. The managed share is not re-intersected with tenure; it remains a uniform province-ecoprovince share.

## Screens and thresholds

| Screen | Threshold | Treatment |
|---|---|---|
| Age | >= 20 years | exclude younger stands |
| Age | >= 30 years | exclude younger stands |
| Fire | NBAC 2020 perimeter | exclude burned pixels |
| Road | <= 5 km | access sensitivity |
| Road | <= 10 km | access sensitivity |
| Road | <= 20 km | access screen |
| Slope | no national DEM | gap; no filter |

NBAC 2020 contains only YEAR=2020 polygons. The 2010 and 2015 disturbance sensitivity cases are recorded as gaps, not zero-disturbance assumptions.

## National area results

| Case | Age | Disturbance | Road | Screened merchantable (Mha) | Share of base | Operable proxy (Mha) | Excluded (Mha) |
|---|---:|---|---:|---:|---:|---:|---:|
| base |  | none |  | 332.60 | 100.0% | 144.69 | 0.00 |
| age_ge_20 | >= 20 yr | none |  | 311.52 | 93.7% | 134.56 | 21.08 |
| age_ge_30 | >= 30 yr | none |  | 294.67 | 88.6% | 127.37 | 37.93 |
| disturb_2020_excluded |  | NBAC 2020 |  | 332.54 | 100.0% | 144.67 | 0.06 |
| road_le_5km |  | none | <= 5 km | 121.58 | 36.6% | 69.60 | 211.01 |
| road_le_10km |  | none | <= 10 km | 156.50 | 47.1% | 87.97 | 176.10 |
| road_le_20km |  | none | <= 20 km | 197.61 | 59.4% | 107.20 | 134.99 |
| screen_age20_disturb | >= 20 yr | NBAC 2020 |  | 311.49 | 93.7% | 134.55 | 21.11 |
| screen_age30_disturb | >= 30 yr | NBAC 2020 |  | 294.64 | 88.6% | 127.36 | 37.96 |
| screen_core20 | >= 20 yr | NBAC 2020 | <= 20 km | 184.33 | 55.4% | 99.87 | 148.27 |
| screen_core30 | >= 30 yr | NBAC 2020 | <= 10 km | 137.63 | 41.4% | 77.05 | 194.97 |

v1 base operable proxy: **144.69 Mha**.
v2 base operable proxy: **144.69 Mha**.

## Base case by province/territory

| Province | SCANFI treed (Mha) | Base merchantable (Mha) | Managed proxy (Mha) | Base operable (Mha) | Managed share |
|---|---:|---:|---:|---:|---:|
| QC | 81.66 | 72.18 | 28.27 | 26.16 | 34.6% |
| BC | 66.61 | 60.43 | 54.37 | 49.26 | 81.6% |
| ON | 68.52 | 53.48 | 33.81 | 30.01 | 49.3% |
| AB | 38.35 | 32.03 | 21.79 | 18.40 | 56.8% |
| NT | 43.46 | 24.53 | 0.82 | 0.64 | 1.9% |
| MB | 33.75 | 23.87 | 6.90 | 5.49 | 20.5% |
| NL | 23.53 | 21.43 | 1.11 | 0.88 | 4.7% |
| YT | 25.91 | 17.73 | 8.07 | 5.76 | 31.2% |
| SK | 26.16 | 14.51 | 7.49 | 4.93 | 28.6% |
| NB | 6.69 | 5.62 | 2.56 | 2.14 | 38.2% |
| NS | 4.73 | 4.41 | 1.10 | 1.02 | 23.2% |
| NU | 2.83 | 2.11 | missing | missing | missing |
| PE | 0.27 | 0.25 | missing | missing | missing |

## Age sensitivity

| Case | National operable (Mha) | Change vs base |
|---|---:|---:|
| age_ge_20 | 134.56 | -10.13 Mha |
| age_ge_30 | 127.37 | -17.32 Mha |

Stands below 20 years: **21.08 Mha** (6.3% of base merchantable).
Stands below 30 years: **37.93 Mha** (11.4% of base merchantable).
Age-missing base pixels: **0.0000 Mha**.

## Disturbance sensitivity

NBAC 2020 burned merchantable area: **0.0557 Mha** (0.02% of base merchantable).
NBAC 2020 burned area also age >= 20: **0.0290 Mha**.

The NBAC bundle is the 2020 annual vintage (710 polygons, all YEAR=2020). It does not contain 2010 or 2015 fire history, so those cases are not reported. The polygons are annual perimeters, not cumulative severity classes.

## Road proximity

| Distance class | Base merchantable (Mha) | Share of base |
|---|---:|---:|
| 0-5 km | 121.58 | 36.6% |
| 5-10 km | 34.92 | 10.5% |
| 10-20 km | 41.11 | 12.4% |
| > 20 km | 134.99 | 40.6% |

NRN public roads only. Resource, industrial, winter, and decommissioned roads are absent, so this is an optimistic access proxy.

## 150M implications

The 150,000,000 m3/yr path is an upper scenario bound, not a forecast or AAC.

| Case | Operable area (Mha) | Implied intensity (m3/ha/yr) | Relative to v1 base |
|---|---:|---:|---:|
| base | 144.69 | 1.037 | 1.00x |
| age_ge_20 | 134.56 | 1.115 | 1.08x |
| age_ge_30 | 127.37 | 1.178 | 1.14x |
| disturb_2020_excluded | 144.67 | 1.037 | 1.00x |
| road_le_20km | 107.20 | 1.399 | 1.35x |
| screen_age20_disturb | 134.55 | 1.115 | 1.08x |
| screen_core20 | 99.87 | 1.502 | 1.45x |
| screen_core30 | 77.05 | 1.947 | 1.88x |

The implied intensity is target volume divided by screened operable area. It is not a growth/yield estimate and does not demonstrate sustainability. Base-path intensity at 118,977,339 m3/yr is proportionally lower.

## Validation

- Strip-level pixel conservation: max residual **0** pixels.
- National treed area vs area-weights: **0.000 ha** difference.
- No NaN in area fields: **True**.
- No negative area fields: **True**.
- Base <= treed: **True**.
- Age 20 <= base and age 30 <= age 20: **True**.
- Age partition conserves base: **True**.
- Burn <= base: **True**.
- Road classes conserve base: **True**.
- Combined cores <= component screens: **True**.
- Operable <= screened where defined: **True**.
- Province sums equal ecoprovince sums for every case: **True**.
- v2 base equals v1 base: **True**.

## Gaps

- **legal_thlb_missing** (all): No legal timber harvesting landbase boundary is used. Tenure is a rights footprint, not a harvest-landbase determination. Effect: All areas are screening proxies and must not be labelled THLB or AAC.
- **slope_dem_missing** (all): No national DEM is present in the workspace, so no slope, elevation, operability, or site-degradation filter is applied. Effect: Steep and inoperable terrain remains in every v2 area.
- **nbac_2010_2015_missing** (all): The NBAC bundle is the 2020 annual vintage (YEAR=2020 for all 710 polygons). It contains no 2010 or 2015 fire history, so those sensitivity screens cannot be computed from this input. Effect: Only a 2020 fire screen is reported; the 2010 and 2015 cases are explicit gaps, not zero-disturbance assumptions.
- **nbac_annual_not_cumulative** (all): NBAC polygons are annual fire perimeters with YEAR/NFIREID and polygon attributes. They are not a cumulative severity or burn-class stack, so no cumulative class is interpreted. Effect: The disturbance screen is an annual 2020 burned/not-burned mask.
- **nrn_public_roads_only** (all): All 13 NRN province bundles were materialised and used. NRN is the public road network; resource, industrial, winter, and decommissioned roads are not represented, and road condition/seasonality is absent. Effect: Road distance is an optimistic public-road access proxy.
- **age_regeneration_assumption** (all): SCANFI median age is a stand-age prediction. Excluding stands below 20 or 30 years assumes they are not merchantable at the screen date, which is stricter than the v1 height/biomass/closure thresholds and ignores partial harvest, thinning, and regeneration delay. Effect: Age screens reduce area beyond merchantability alone.
- **managed_share_uniform** (all): The v1 managed share is uniform inside each province-ecoprovince. Tenure was not re-intersected with the age, burn, or road rasters. Effect: Spatial tenure pattern is not represented.
- **nfi_age_uncertainty** (all): SCANFI age is a 30 m prediction surface, not a provincial inventory or a time-since-disturbance record. Effect: Age thresholds are screening conventions, not statutory rules.

## Outputs

- `operable_proxy_v2_by_province.csv`: province x screen case.
- `operable_proxy_v2_by_ecoprovince.csv`: province x ecoprovince x screen case.
- `operable_proxy_v2_summary.json`: screens, national totals, sensitivity, 150M implications, validation, gaps.
- `road_distance_classes.csv`: base merchantable area by road distance class and province.
- `gaps.csv`: explicit gap register.
- `manifest.json`: input and output hashes, runtime, software, validation.

## Reproduction

```bash
.venv/bin/python scripts/national/build_operable_proxy_v2.py \
  --out-dir data/derived/national/managed_landbase/operable_proxy_v2
```

Raw SCANFI, NBAC, NRN, tenure, CPCAD, boundary, and RSYC payloads remain in the `data` submodule and are not committed to the parent repository.
