# Sustainable WS4 cases on the share-based operable landbase

**Artifact:** `ws4_operable_cases` **Version:** 1.0.0

**Status:** pass. The 100, 119, and 150 Mm3/yr cases were rerun
on a share-based operable proxy of the national 990 m WS4 estate. The strict
all-province cases are not sustained; the maximum schedule-only levels on the
covered operable provinces are reported below.

**Labels:** `model_estimate=true`, `observed=false`, `policy_grade=false`,
`national_claim=false`, `ws4_derived=true`, `sustainable_schedule=true`,
`share_based_operable_proxy=true`, `legal_thlb=false`, `slope_screen=false`,
`official_osecan_changed=false`, `chain_v51_unchanged=true`.

## 1. Operable screen

Screen case `screen_core30`: SCANFI median age >= 30 years, NBAC 2020 burned
pixels excluded, block centre within 10 km of a public NRN road. The mask is a
deterministic area-share proxy: within each province, blocks are ranked by
`blake2b(province:block_id)` and taken whole until the selected forest area
matches `operable_share_of_treed * WS4 province forest area`.

| Province | Coverage | Published share | Published area Mha | WS4 forest Mha | Share target Mha | Selected Mha | Selected blocks |
|---|---|---|---|---|---|---|---|
| BC | yes | 33.6629% | 22.422 | 65.698 | 22.116 | 22.116 | 164,442 |
| AB | yes | 28.5791% | 10.959 | 37.550 | 10.732 | 10.731 | 47,774 |
| SK | yes | 11.2245% | 2.936 | 23.593 | 2.648 | 2.648 | 12,040 |
| MB | yes | 6.8898% | 2.326 | 31.879 | 2.196 | 2.146 | 9,272 |
| ON | yes | 33.4358% | 22.909 | 66.682 | 22.296 | 22.317 | 71,707 |
| QC | yes | 12.8963% | 10.532 | 81.424 | 10.501 | 10.501 | 45,146 |
| NB | yes | 26.4599% | 1.771 | 6.605 | 1.748 | 1.748 | 7,685 |
| NS | yes | 18.1834% | 0.860 | 4.674 | 0.850 | 0.850 | 3,311 |
| PE | no | n/a | n/a | 0.269 | 0.000 | 0.000 | 0 |
| NL | yes | 2.8825% | 0.678 | 23.342 | 0.673 | 0.673 | 2,660 |
| YT | yes | 5.6880% | 1.474 | 25.809 | 1.468 | 1.468 | 6,025 |
| NT | yes | 0.4234% | 0.184 | 42.370 | 0.179 | 0.177 | 690 |
| NU | no | n/a | n/a | 1.355 | 0.000 | 0.000 | 0 |

National selected area: 75.374
Mha across 370,752 blocks.
Published absolute screen area:
77.050
Mha. The difference is the WS4 block-forest denominator versus the SCANFI treed
denominator; the share is preserved.

**No legal THLB, national slope DEM, or spatial road overlay is available.**
The screen is an area-share proxy, not legal THLB, slope, or spatial road
screening. NU and PE have no 2016 tenure coverage and therefore no operable
blocks.

## 2. Case results

| Case | Target Mm3/yr | Sustained | Covered sustained | Annual min Mm3/yr | Annual max Mm3/yr | Annual mean Mm3/yr | Period shortfall Mm3 | Province shortfall Mm3 | Blocks | Treated area Mha | Max nominal Mm3/yr | Max operable Mm3/yr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100m | 100.0000 | False | False | 94.4141 | 105.4949 | 98.6880 | 160.4216 | 259.6635 | 310,750 | 68.234 | 68.4570 | 69.3438 |
| 119m | 118.9773 | False | False | 97.9475 | 123.0149 | 113.1749 | 623.2648 | 752.8481 | 352,262 | 76.783 | 67.8543 | 69.2302 |
| 150m | 150.0000 | False | False | 111.6734 | 154.4895 | 132.6875 | 1774.8825 | 1896.9787 | 410,086 | 89.775 | 61.4868 | 62.7054 |

## 3. Full-forest versus operable

| Case | Full-forest Mm3/yr | Full-forest sustained | Operable Mm3/yr | Operable sustained | Max nominal Mm3/yr | Shortfall provinces |
|---|---:|---|---:|---|---:|---|
| 100m | 101.1050 | True | 98.6880 | False | 68.4570 | QC|NB|NL|PE|NS |
| 119m | 119.8839 | True | 113.1749 | False | 67.8543 | QC|NB|NL|SK|PE|NS |
| 150m | 151.2477 | True | 132.6875 | False | 61.4868 | QC|SK|NS|NL|NB|PE |

The full-forest cases are the existing sustainable 100/119/150 Mm3 artifacts.
The operable cases restrict eligibility to the mask and disable the
cross-province fallback; provincial targets are otherwise the frozen case
shares. The operable cases fail because QC, NB, NS, SK, NL, and PE cannot meet
their allocated targets on the screened area; the binding province sets the
maximum sustainable level.

## 4. Chain comparison against frozen v5.1 full-forest totals

| Case | Metric | Unit | v5.1 full-forest | Operable primary | Delta % | Operable achieved | Delta % |
|---|---|---|---:|---:|---:|---:|---:|
| 100m | harvest_m3 | m3 | 100,000,000.100000 | 102,538,416.376373 | +2.5384 | 98,688,038.668833 | -1.3120 |
| 100m | solid_product_m3 | m3 | 31,692,807.151334 | 32,338,131.012287 | +2.0362 | 31,341,215.312687 | -1.1094 |
| 100m | pulp_product_odt | odt | 10,136,702.863917 | 10,448,990.662907 | +3.0808 | 9,970,253.391789 | -1.6420 |
| 100m | process_residue_pj | PJ | 419.238018 | 429.783127 | +2.5153 | 413.715371 | -1.3173 |
| 100m | harvest_residue_gross_pj | PJ | 373.243923 | 383.181241 | +2.6624 | 368.707692 | -1.2154 |
| 100m | harvest_residue_recoverable_r060_pj | PJ | 223.946354 | 229.908745 | +2.6624 | 221.224615 | -1.2154 |
| 100m | total_residue_gross_pj | PJ | 792.481942 | 812.964369 | +2.5846 | 782.423063 | -1.2693 |
| 119m | harvest_m3 | m3 | 118,977,339.100000 | 119,145,039.011526 | +0.1410 | 113,174,872.830592 | -4.8770 |
| 119m | solid_product_m3 | m3 | 37,673,626.761068 | 37,753,282.564585 | +0.2114 | 36,488,810.460976 | -3.1449 |
| 119m | pulp_product_odt | odt | 12,066,311.269557 | 12,071,929.346576 | +0.0466 | 11,277,577.630878 | -6.5367 |
| 119m | process_residue_pj | PJ | 498.750917 | 499.461625 | +0.1425 | 475.061816 | -4.7497 |
| 119m | harvest_residue_gross_pj | PJ | 444.410766 | 445.142894 | +0.1647 | 417.473157 | -6.0614 |
| 119m | harvest_residue_recoverable_r060_pj | PJ | 266.646460 | 267.085736 | +0.1647 | 250.483894 | -6.0614 |
| 119m | total_residue_gross_pj | PJ | 943.161683 | 944.604519 | +0.1530 | 892.534973 | -5.3678 |
| 150m | harvest_m3 | m3 | 150,000,000.200000 | 150,096,161.415197 | +0.0641 | 132,687,525.202585 | -11.5416 |
| 150m | solid_product_m3 | m3 | 46,136,665.718213 | 46,205,915.906538 | +0.1501 | 42,859,441.424691 | -7.1033 |
| 150m | pulp_product_odt | odt | 15,550,881.011045 | 15,546,309.670058 | -0.0294 | 13,228,147.127068 | -14.9363 |
| 150m | process_residue_pj | PJ | 626.865219 | 627.301909 | +0.0697 | 557.140748 | -11.1227 |
| 150m | harvest_residue_gross_pj | PJ | 573.125413 | 573.564662 | +0.0766 | 481.526667 | -15.9823 |
| 150m | harvest_residue_recoverable_r060_pj | PJ | 343.875248 | 344.138797 | +0.0766 | 288.916000 | -15.9823 |
| 150m | total_residue_gross_pj | PJ | 1,199.990632 | 1,200.866571 | +0.0730 | 1,038.667415 | -13.4437 |

The primary operable basis is the first-period annual average; the achieved
basis is the 100-year average. Both are unscaled and use frozen v5.1
per-province coefficients. The reference is the frozen full-forest v5.1 case
total for each scenario.

## 5. OSeCAN handoff

Rebuilt from the operable sustainable WS4 case chains on the origin-province basis using the frozen handoff-v10 zone weights. Frozen v5.1 21/21 positions match handoff v10; 100m primary 6/7, achieved 7/7; 119m primary 7/7, achieved 6/7; 150m primary 7/7, achieved 6/7. Official OSeCAN is unchanged.

## 6. Gaps and limitations

- No legal THLB boundary.
- No national slope/elevation DEM; no slope screen.
- Road distance is public-NRN Euclidean distance at 990 m, not a spatial road
  overlay; resource and industrial roads are absent.
- NBAC 2020 only; 2010/2015 disturbance cases are gaps.
- SCANFI age is a prediction surface.
- Managed share is uniform inside each province-ecoprovince.
- The mask is not spatially intersected with the tenure, burn, road, or slope
  rasters.
- Max-sustainable levels are schedule-only diagnostics; they are not
  WS4-simulated or policy-tested.
