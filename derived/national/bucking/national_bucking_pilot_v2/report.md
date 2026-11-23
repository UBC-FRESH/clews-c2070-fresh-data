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
| Rule set | Trees | Logs | Recovered m3 (expanded) | Residue m3 | Residue odt | Sawlog share | Pulpwood share | Other share | Solid share | Residue odt/m3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BC interior TIPSY | 347 | 621 | 146115.503 | 36955.338 | 13776.656 | 0.913 | 0.000 | 0.087 | 1.000 | 0.0943 |
| National pilot sorts | 347 | 1238 | 165127.417 | 17506.417 | 6700.357 | 0.695 | 0.295 | 0.010 | 0.705 | 0.0406 |

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
| BC_V2_MEASURED_TIPSY_SORTS | 0.913 | 1.000 | 0.0943 | 1.451 | 1.237 | outside_20pct |
| BC_V2_MEASURED_NATIONAL_SORTS | 0.695 | 0.705 | 0.0406 | 1.023 | 0.532 | outside_20pct |
| BC_FACILITY_FEEDSTOCK | 0.592 | 0.689 | 0.0762 | 1.000 | 1.000 | reference |

Facility feedstock shares are mill receipts from `facility_product_chain_v1`, not TIPSY dimension classes.  The TIPSY rule set classifies nearly all conifer logs with a 12.5 cm top as sawlog, so its solid share is not expected to equal the facility sawlog + panel feedstock share.  The comparison is screening, not calibration.

## Expansion-weighted population check
| Metric | v0 full population | v2 TIPSY | TIPSY/v0 | v2 national | National/v0 |
|---|---:|---:|---:|---:|---:|
| taper_total_m3_expanded | 185575.651 | 183070.841 | 0.9865 | 182633.834 | 0.9841 |
| recovered_gross_m3_expanded | 147547.444 | 146115.503 | 0.9903 | 165127.417 | 1.1191 |
| residue_m3_expanded | 38028.207 | 36955.338 | 0.9718 | 17506.417 | 0.4604 |
| residue_odt_expanded | 14116.451 | 13776.656 | 0.9759 | 6700.357 | 0.4746 |

## Checks
- `bc_empirical_provenance`: **PASS** — 347 BC tree rows carry measured FAIB PSP provenance
- `bc_expansion_preserved`: **PASS** — BC PHF total 1188462.589136 preserved
- `thirteen_jurisdictions`: **PASS** — 13 jurisdictions present
- `bc_empirical_count`: **PASS** — BC tree count 347 equals measured list
- `other_provinces_unchanged`: **PASS** — AB=10; SK=10; MB=10; ON=10; QC=10; NB=10; NS=10; PE=10; NL=10; YT=10; NT=10; NU=10
- `volume_balance`: **PASS** — national v2 balance error 0 m3
- `net_defect_balance`: **PASS** — national v2 net+defect error 0 m3
- `bc_tipsy_conservation`: **PASS** — 347 BC TIPSY stems balance
- `no_nan`: **PASS** — numeric columns contain no NaN
- `no_negative`: **PASS** — numeric columns are non-negative except explicit delta columns
- `grade_not_assigned`: **PASS** — 1426 national and 621 BC TIPSY log rows grade=not_assigned
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
- No national, operational, policy-grade, AAC, or investment claim is made.
- No UI or public OSeCAN surface was changed.

No UI, public OSeCAN surface, policy grade, AAC, or national supply claim is made.
