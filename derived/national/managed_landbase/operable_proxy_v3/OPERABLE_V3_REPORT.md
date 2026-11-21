# National Operable Landbase Proxy v3

**Status: screening proxy. This is not a legal timber harvesting landbase (THLB), not an AAC landbase, and not an operability model.**

Generated: 2026-11-21T21:06:40+00:00  
Runtime: 0.3 s  
Inputs: published operable proxy v2 tables and the national 960 m MRDEM-30 slope screen. No new GIS raster is produced.

## Method and overlay assumption

v3 combines the three v2 cases (base, core20, core30) with three slope cases (none, >15%, >30%). For each province/ecoprovince the published forest-weighted treed slope share is applied to the v2 operable area:

```
lost_ha = v2_operable_ha * slope_share
remaining_ha = v2_operable_ha - lost_ha
```

This preserves the slope-screen overlay assumption: the v2 screens are assumed independent of slope inside a province/ecoprovince. It is **not** a pixel-exact intersection. The >30% base and core20 losses reconcile to the published slope overlay; core30 uses the same ecoprovince share because no core30 overlay was published.

## National areas by case

| v2 case | slope case | v2 operable (Mha) | Lost (Mha) | Remaining (Mha) | Lost share |
|---|---|---:|---:|---:|---:|
| base | none | 144.690 | 0.0000 | 144.690 | 0.000% |
| base | gt15 | 144.690 | 12.5245 | 132.165 | 8.656% |
| base | gt30 | 144.690 | 2.1919 | 142.498 | 1.515% |
| core20 | none | 99.870 | 0.0000 | 99.870 | 0.000% |
| core20 | gt15 | 99.870 | 8.2668 | 91.603 | 8.278% |
| core20 | gt30 | 99.870 | 1.4792 | 98.391 | 1.481% |
| core30 | none | 77.050 | 0.0000 | 77.050 | 0.000% |
| core30 | gt15 | 77.050 | 5.8681 | 71.182 | 7.616% |
| core30 | gt30 | 77.050 | 1.0384 | 76.012 | 1.348% |

## 150M implications

The 150,000,000 m3/yr path is an upper scenario bound, not a forecast or AAC. 119M is the v2 reference base path (118,977,339 m3/yr).

| v2 case | slope case | Post-slope operable (Mha) | 100M (m3/ha/yr) | 119M (m3/ha/yr) | 150M (m3/ha/yr) |
|---|---|---:|---:|---:|---:|
| base | none | 144.690 | 0.691 | 0.822 | 1.037 |
| base | gt15 | 132.165 | 0.757 | 0.900 | 1.135 |
| base | gt30 | 142.498 | 0.702 | 0.835 | 1.053 |
| core20 | none | 99.870 | 1.001 | 1.191 | 1.502 |
| core20 | gt15 | 91.603 | 1.092 | 1.299 | 1.637 |
| core20 | gt30 | 98.391 | 1.016 | 1.209 | 1.525 |
| core30 | none | 77.050 | 1.298 | 1.544 | 1.947 |
| core30 | gt15 | 71.182 | 1.405 | 1.671 | 2.107 |
| core30 | gt30 | 76.012 | 1.316 | 1.565 | 1.973 |

These are target volume divided by post-slope operable area. They are not growth/yield estimates and do not demonstrate sustainability.

## Province totals (remaining Mha)

| Province | base none | base >15% | base >30% | core20 none | core20 >15% | core20 >30% | core30 none | core30 >15% | core30 >30% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AB | 18.401 | 18.216 | 18.385 | 13.755 | 13.596 | 13.741 | 10.959 | 10.833 | 10.948 |
| BC | 49.258 | 37.435 | 47.090 | 31.317 | 23.432 | 29.855 | 22.422 | 16.817 | 21.397 |
| MB | 5.485 | 5.485 | 5.485 | 3.342 | 3.342 | 3.342 | 2.326 | 2.326 | 2.326 |
| NB | 2.136 | 2.136 | 2.136 | 1.965 | 1.965 | 1.965 | 1.771 | 1.771 | 1.771 |
| NL | 0.884 | 0.880 | 0.884 | 0.816 | 0.813 | 0.816 | 0.678 | 0.676 | 0.678 |
| NS | 1.024 | 1.023 | 1.024 | 0.960 | 0.960 | 0.960 | 0.860 | 0.859 | 0.860 |
| NT | 0.639 | 0.636 | 0.639 | 0.299 | 0.298 | 0.299 | 0.184 | 0.184 | 0.184 |
| NU | missing | missing | missing | missing | missing | missing | missing | missing | missing |
| ON | 30.011 | 30.011 | 30.011 | 26.720 | 26.720 | 26.720 | 22.909 | 22.909 | 22.909 |
| PE | missing | missing | missing | missing | missing | missing | missing | missing | missing |
| QC | 26.159 | 26.130 | 26.159 | 14.537 | 14.521 | 14.537 | 10.532 | 10.519 | 10.532 |
| SK | 4.933 | 4.933 | 4.933 | 3.703 | 3.703 | 3.703 | 2.936 | 2.936 | 2.936 |
| YT | 5.760 | 5.278 | 5.752 | 2.456 | 2.254 | 2.453 | 1.474 | 1.353 | 1.471 |

### Largest base >30% ecoprovince losses

| Province | Ecoprovince | Base operable (Mha) | Lost >30% (Mha) | Lost share |
|---|---|---:|---:|---:|
| BC | Southern Coastal Mountains | 7.957 | 1.0107 | 12.702% |
| BC | Columbia Montane Cordillera | 7.139 | 0.6647 | 9.311% |
| BC | Northern Coastal Mountains | 0.627 | 0.1397 | 22.282% |
| BC | Southern Montane Cordillera | 3.527 | 0.1268 | 3.594% |
| BC | Southern Boreal Cordillera | 5.062 | 0.0818 | 1.615% |
| BC | Northern Montane Cordillera | 8.887 | 0.0747 | 0.841% |
| BC | Central Montane Cordillera | 5.776 | 0.0396 | 0.685% |
| BC | Georgia Depression | 1.190 | 0.0297 | 2.496% |
| AB | Columbia Montane Cordillera | 0.741 | 0.0160 | 2.166% |
| YT | Northern Boreal Cordillera | 3.756 | 0.0052 | 0.138% |

## The 13.27 Mha ecoprovince gap

The slope screen covers 409.20 Mha of SCANFI treed area. 13.27 Mha (3.14%) of SCANFI treed area lies outside the RSYC ecoprovince polygons and has no independent ecoprovince slope statistics. Operable proxy v2 assigns those blocks to the nearest ecoprovince; v3 inherits that attribution and applies the receiving ecoprovince's slope share. The gap remains explicit and is not zero-filled.

## Validation

- v3 none equals v2 for all three cases: **True** (max province residual 3.73e-09 ha).
- v3 >15% and >30% losses for base and core20 match the published slope overlay (max ecoprovince residual 8.40e-07 ha).
- Province rows equal the sum of ecoprovince rows: **True**.
- No NaN outside the NU/PE coverage gap: **True**.
- No negative areas; losses never exceed pre-slope area: **True**.
- Threshold ordering (remaining >15% <= >30% <= none): **True**.
- Case ordering (core30 <= core20 <= base): **True**.
- 150M arithmetic exact: **True**.
- 13.27 Mha slope coverage gap reconciled: **True**.
- All checks pass: **True**.

## Gaps

- **legal_thlb_missing** (open): No legal timber harvesting landbase boundary is used. Tenure is a rights footprint, not a harvest-landbase determination. Effect: All v3 areas are screening proxies and must not be labelled THLB or AAC.
- **slope_overlay_assumption** (open): Forest-weighted treed slope shares from the 960 m screen are applied to v2 operable area inside a province/ecoprovince. The v2 screens are assumed independent of slope; this is not a pixel-exact intersection. Effect: Steep-area losses are overlay estimates, not spatially resolved exclusions.
- **coarse_slope_not_operability** (open): Slope is computed from 960 m average elevation. Local 30 m slope can be much steeper; this layer cannot classify operability, harvest system, or site degradation. Effect: >15% and >30% losses are screening sensitivities, not operational or legal classifications.
- **dem_source_mix** (open): MRDEM-30 is a DTM mosaic of HRDEM lidar and Copernicus GLO-30. Non-lidar areas are modelled and may have larger vertical error; the public STAC item has no source legend. Effect: Slope accuracy is not uniform across the country.
- **treed_outside_rsyc_ecoprovince** (open): 13,272,017.76 ha of SCANFI treed area lies outside the RSYC ecoprovince polygons. v2 assigns those blocks to the nearest ecoprovince, but the slope screen has no independent ecoprovince slope statistics for them. Effect: v3 inherits the v2 nearest-ecoprovince attribution and applies the receiving ecoprovince's slope share to those blocks; the 13.27 Mha gap is not zero-filled or separately resolved.
- **core30_slope_no_published_overlay** (documented): The published slope overlay contains base and core20 only. v3 applies the same ecoprovince share to core30; there is no independent core30 overlay to reconcile against. Effect: core30 slope losses are internally consistent estimates.
- **slope_dem_missing** (resolved_in_v3): The v2 gap that no national DEM was present is superseded by the national 960 m MRDEM-30 slope screen used here. Effect: The residual limitations are captured in coarse_slope_not_operability, dem_source_mix, and slope_overlay_assumption.
- **nbac_2010_2015_missing** (open): The NBAC bundle is the 2020 annual vintage only; 2010 and 2015 fire-history screens cannot be computed. Effect: Only the 2020 fire screen is represented in v2/v3.
- **nrn_public_roads_only** (documented): NRN is the public road network; resource, industrial, winter, and decommissioned roads are absent. Effect: Road distance is an optimistic public-road access proxy.
- **age_regeneration_assumption** (documented): SCANFI median age is a stand-age prediction; excluding stands below 20 or 30 years is a screening convention. Effect: Age screens reduce area beyond merchantability alone.
- **managed_share_uniform** (documented): The v1 managed share is uniform inside each province-ecoprovince; tenure is not intersected spatially. Effect: Spatial tenure pattern is not represented.
- **nfi_age_uncertainty** (documented): SCANFI age is a 30 m prediction surface, not a provincial inventory or disturbance record. Effect: Age thresholds are screening conventions.
- **nu_pe_tenure_missing** (documented): NU and PE managed and operable values are blank because the 2016 tenure compilation has no coverage. Effect: Blank is not zero; national totals cover 11 provinces.

## Outputs

- `operable_v3_by_province.csv`: province x v2 case x slope case.
- `operable_v3_by_ecoprovince.csv`: province x ecoprovince x v2 case x slope case.
- `operable_v3_150m.csv`: 100M/119M/150M target-volume arithmetic.
- `summary.json`: national totals, 150M implications, validation, coverage gap, gaps.
- `manifest.json`: input/output hashes, runtime, software versions, validation.

## Reproduction

```bash
.venv/bin/python scripts/national/build_operable_proxy_v3.py \
  --out-dir data/derived/national/managed_landbase/operable_proxy_v3
```

Raw SCANFI, NBAC, NRN, tenure, CPCAD, boundary, and RSYC payloads remain in the `data` submodule and are not committed to the parent repository.

