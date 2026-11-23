# National bucking pilot v2 — measured BC list
**Scope: pilot.  Not inventory, not a national supply estimate, not an official grade.**  BC tree geometry is measured FAIB PSP TSA24 data; the other 12 jurisdictions are representative synthetic lists.  BC logs and residue are model estimates (`observed=false`, `policy_grade=false`, `national_claim=false`).
## BC empirical tree list
- Source: 59,397 buckable live TSA24 PSP stems from `selected_trees.csv`; 1,563 v0-skipped stems excluded (unsupported taper species or reference bucker balance failure).
- Selection: one measured PHF-weighted median stem per species x BEC zone x 2.5 cm DBH stratum; 347 retained stems in 347 strata.
- Expansion: source PHF 1,188,462.589; selected PHF 1,188,462.589; relative error 0.  DBH and height are the measured retained values; no synthetic geometry.
| Species | Source stems | Selected stems |
|---|---:|---:|
| AC | 132 | 18 |
| AT | 4474 | 26 |
| BL | 16548 | 67 |
| CW | 154 | 11 |
| EP | 3343 | 27 |
| FD | 3743 | 29 |
| HM | 1 | 1 |
| HW | 769 | 30 |
| PL | 6163 | 52 |
| SB | 257 | 10 |
| SE | 533 | 19 |
| SW | 23280 | 57 |

## BC bucking results
| Rule set | Trees | Logs | Recovered m3 (expanded) | Stem residue m3 | Stem residue odt | Branch odt | Foliage odt | Gross total odt | Gross odt/m3 | Recoverable odt/m3 (0.60) | Sawlog share | Pulpwood share | Other share | Solid share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BC interior TIPSY | 347 | 613 | 145725.588 | 37345.253 | 13922.853 | 12643.576 | 7344.286 | 33910.715 | 0.2327 | 0.1396 | 0.916 | 0.000 | 0.084 | 1.000 |
| National pilot sorts | 347 | 1238 | 165127.417 | 17506.417 | 6700.357 | 12643.576 | 7344.286 | 26688.219 | 0.1616 | 0.0970 | 0.695 | 0.295 | 0.010 | 0.705 |

Total harvest residue = stem taper residue + branch ODT + foliage ODT.  The recoverable column applies the existing pilot 0.60 recovery factor to the gross total; it is not calibrated to the facility coefficient.

## BC branch and foliage allometry
- Source: CFS Biomass and Nutrients Calculator tree-level DBH + height table; licence Open Government Licence - Canada.
- Equations: Lambert, Ung and Raulier (2005) Can. J. For. Res. 35:1996-2018; Ung, Bernier and Guo (2008) Can. J. For. Res. 38:1123-1132.  Branch and foliage are model estimates (`published_table`), not measured slash.
- Gross and recoverable residue are reported separately.  The facility gross coefficient is 0.076226 ODT/m3; the prior stem-only model result is 0.040577 ODT/m3.
| Variant | Residue definition | Residue odt/m3 | Ratio to facility | Gap vs facility | Gap vs prior stem |
|---|---|---:|---:|---:|---:|
| BC_V2_MEASURED_NATIONAL_SORTS_STEM_ONLY_PRIOR | stem_only | 0.040577 | 0.5323 | -46.77% | +0.00% |
| BC_V2_MEASURED_NATIONAL_SORTS_GROSS_TOTAL | gross_total | 0.161622 | 2.1203 | +112.03% | +298.31% |
| BC_V2_MEASURED_NATIONAL_SORTS_RECOVERABLE_TOTAL | recoverable_total | 0.096973 | 1.2722 | +27.22% | +138.99% |
| BC_V2_MEASURED_TIPSY_STEM_ONLY | stem_only | 0.095542 | 1.2534 | +25.34% | +135.46% |
| BC_V2_MEASURED_TIPSY_GROSS_TOTAL | gross_total | 0.232703 | 3.0528 | +205.28% | +473.49% |
| BC_V2_MEASURED_TIPSY_RECOVERABLE_TOTAL | recoverable_total | 0.139622 | 1.8317 | +83.17% | +244.09% |
| BC_FACILITY_HARVEST_RESIDUE_GROSS | facility_gross | 0.076226 | 1.0000 | +0.00% | +87.85% |
| BC_FACILITY_HARVEST_RESIDUE_RECOVERABLE | facility_recoverable | 0.054245 | 0.7116 | -28.84% | +33.68% |

The facility reference is a gross harvest-residue coefficient from `facility_product_chain_v1`.  The model gross total includes all live branch and foliage biomass and is therefore expected to exceed a roadside-recoverable facility coefficient.  The 0.60-recoverable row is the existing pilot default, not a calibrated recovery estimate.

## v1→v2 comparison
| Scope | v1 trees | v2 trees | v1 logs/tree | v2 logs/tree | v1 residue m3/m3 | v2 residue m3/m3 | v1 solid share | v2 solid share | Solid delta |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | 10 | 347 | 2.300 | 3.568 | 0.0404 | 0.1060 | 0.946 | 0.705 | -0.241 |
| NATIONAL_MACRO | 130 | 467 | 1.623 | 3.054 | 0.2437 | 0.2487 | 0.505 | 0.487 | -0.019 |
| NATIONAL_MIXED_EXPANDED | 130 | 467 | 1.623 | 3.054 | 0.1604 | 0.1060 | 0.614 | 0.705 | +0.091 |

Only BC changes; the other 12 province rows are the v1 trees and sort rules.  Absolute v1 and v2 volumes are not directly comparable because the BC row changes from a 10-tree unweighted sample to an expansion-weighted measured aggregate.  Shares and per-tree metrics are the comparison basis.  National rows are macro or mixed-basis, never a national supply estimate.

## Facility coefficient fit
| Variant | Sawlog share | Solid share | Residue odt/m3 | Solid/facility | Residue/facility | Status |
|---|---:|---:|---:|---:|---:|---|
| BC_V1_SYNTHETIC_NATIONAL_SORTS | 0.941 | 0.946 | 0.0158 | 1.373 | 0.208 | outside_20pct |
| BC_V2_MEASURED_TIPSY_SORTS | 0.916 | 1.000 | 0.0955 | 1.451 | 1.253 | outside_20pct |
| BC_V2_MEASURED_NATIONAL_SORTS | 0.695 | 0.705 | 0.0406 | 1.023 | 0.532 | outside_20pct |
| BC_FACILITY_FEEDSTOCK | 0.592 | 0.689 | 0.0762 | 1.000 | 1.000 | reference |

Facility feedstock shares are mill receipts from `facility_product_chain_v1`, not TIPSY dimension classes.  The TIPSY rule set classifies nearly all conifer logs with a 12.5 cm top as sawlog, so its solid share is not expected to equal the facility sawlog + panel feedstock share.  The comparison is screening, not calibration.  The residue column in this table is **stem taper residue only**; the gross and 0.60-recoverable totals that include branch and foliage are reported in the preceding branch/foliage section and in `bc_residue_allometry_summary.csv`.

## Expansion-weighted population check
| Metric | v0 full population | v2 TIPSY | TIPSY/v0 | v2 national | National/v0 |
|---|---:|---:|---:|---:|---:|
| taper_total_m3_expanded | 185575.651 | 183070.841 | 0.9865 | 182633.834 | 0.9841 |
| recovered_gross_m3_expanded | 147547.444 | 145725.588 | 0.9877 | 165127.417 | 1.1191 |
| residue_m3_expanded | 38028.207 | 37345.253 | 0.9820 | 17506.417 | 0.4604 |
| residue_odt_expanded | 14116.451 | 13922.853 | 0.9863 | 6700.357 | 0.4746 |

## Checks
- `bc_empirical_provenance`: **PASS** — 347 BC tree rows carry measured FAIB PSP provenance
- `bc_expansion_preserved`: **PASS** — BC PHF total 1188462.589136 preserved
- `thirteen_jurisdictions`: **PASS** — 13 jurisdictions present
- `bc_empirical_count`: **PASS** — BC tree count 347 equals measured list
- `other_provinces_unchanged`: **PASS** — AB=10; SK=10; MB=10; ON=10; QC=10; NB=10; NS=10; PE=10; NL=10; YT=10; NT=10; NU=10
- `volume_balance`: **PASS** — national v2 balance error 0 m3
- `net_defect_balance`: **PASS** — national v2 net+defect error 0 m3
- `bc_tipsy_conservation`: **PASS** — 347 BC TIPSY stems balance
- `no_nan`: **PASS** — numeric core columns contain no NaN; optional branch/foliage fields are populated for every BC measured stem
- `no_negative`: **PASS** — numeric columns are non-negative except explicit delta columns
- `bc_allometry_complete`: **PASS** — 694 BC component rows for 347 stems across two sort rule sets; branch and foliage are positive
- `bc_allometry_conservation`: **PASS** — branch+foliage, stem+branch+foliage, 0.60 recoverable and expansion identities hold for every BC component row
- `bc_allometry_non_bc_not_estimated`: **PASS** — non-BC synthetic rows keep stem residue only and do not claim zero branch/foliage biomass
- `bc_allometry_labels`: **PASS** — BC branch/foliage estimates are model_estimate=true, observed=false, policy_grade=false, national_claim=false
- `bc_allometry_comparison`: **PASS** — gross total and 0.60-recoverable totals are reported separately against facility 0.076226 and prior stem-only 0.040577
- `grade_not_assigned`: **PASS** — 1426 national and 613 BC TIPSY log rows grade=not_assigned
- `taper_evidence`: **PASS** — all national v2 taper rows are published_table
- `comparison_rows`: **PASS** — 13 facility rows, 15 v1-v2 rows, 4 BC facility variants, 4 population metrics
- `labels`: **PASS** — BC tree rows measured; other trees synthetic; observed/policy_grade/national_claim false
- `national_claim`: **PASS** — no national claim on any row
- `repository_hygiene`: **PASS** — no unexpected D in parent or data git status before run

## Limitations
- The BC empirical list is a post-stratified measured aggregate, not the full PSP tree list and not an inventory expansion.
- The other 12 jurisdictions remain representative synthetic lists from pilot v1.
- Absolute volumes are not comparable between expansion-weighted BC and unit-weight synthetic provinces.
- BC TIPSY dimension sorts and national pilot sorts are different rule sets; both are reported.
- Dimension-only pilot sorts are not official federal or provincial log grades; grade=not_assigned.
- Prices, density, moisture, chip and hog yields are pilot assumptions.
- Facility coefficient comparison is screening only; harvest residue and facility process residue are different streams.
- BC branch and foliage biomass is a published allometric model estimate, not measured slash. It is added to stem taper residue for gross and recoverable totals but remains a separate component.
- Some BC source heights are DBH-estimated; branch and foliage inherit that height basis and the tree-list height evidence is not upgraded.
- Gross harvest residue and 0.60-recoverable residue are both reported; the 0.60 recovery factor is the existing pilot default and is not calibrated to the facility coefficient.
- Mountain hemlock (one stem) uses the published conifer group equation; black cottonwood uses the published red alder + black cottonwood group equation. Both are flagged as non-species-specific.
- No national, operational, policy-grade, AAC, or investment claim is made.
- No UI or public OSeCAN surface was changed.

No UI, public OSeCAN surface, policy grade, AAC, or national supply claim is made.
