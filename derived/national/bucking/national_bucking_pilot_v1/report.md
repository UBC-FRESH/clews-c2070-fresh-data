# National bucking pilot v1 — 13 jurisdictions
**Scope: representative synthetic pilot.**  Not inventory, not a national supply estimate, not an official grade.  Every row is `model_estimate=true`, `synthetic=true`, `observed=false`, `policy_grade=false`, `national_claim=false`.
## Method
- Ten representative trees per province.  Species shares use NFI ecodistrict coverage where available; AB/ON/NS/NU use documented composition assumptions.  DBH uses NFI national p05/p50/p95 with an 8 cm merchantable lower bound; height uses the NFI national H = 1.3 + exp(a) * DBH^b fit.  Trees are deterministic synthetic draws, not inventory.
- Taper dispatch is explicit: QC uses Schneider (2013), BC uses Kozak (2004), and the other provinces use a labelled donor taper.  Donor BEC anchors are BC anchors, not local BEC zones.
- Products use one national dimension-only pilot sort set.  `grade=not_assigned`; defect, sweep, knot and rot are not represented.
- Residue is taper total minus recovered gross log volume per stem; density, moisture, chip and hog yields are labelled assumptions.
## Taper coverage
| Province | Trees | Local taper | Donor taper | Taper status |
|---|---:|---:|---:|---|
| BC | 10 | 10 | 0 | local_published |
| AB | 10 | 0 | 10 | donor_published |
| SK | 10 | 0 | 10 | donor_published |
| MB | 10 | 0 | 10 | donor_published |
| ON | 10 | 0 | 10 | donor_published |
| QC | 10 | 10 | 0 | local_published |
| NB | 10 | 0 | 10 | donor_published |
| NS | 10 | 0 | 10 | donor_published |
| PE | 10 | 0 | 10 | donor_published |
| NL | 10 | 0 | 10 | donor_published |
| YT | 10 | 0 | 10 | donor_published |
| NT | 10 | 0 | 10 | donor_published |
| NU | 10 | 0 | 10 | donor_published |

## Logs and residue by province
| Province | Trees | Logs | Recovered m3 | Sawlog m3 | Pulpwood m3 | Other m3 | Residue m3 | Residue odt | Balance error m3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | 10 | 23 | 5.1584 | 4.8521 | 0.2765 | 0.0298 | 0.2084 | 0.0817 | 0 |
| AB | 10 | 20 | 1.6755 | 0.7458 | 0.8859 | 0.0439 | 0.2325 | 0.0860 | 0 |
| SK | 10 | 22 | 1.8127 | 0.7458 | 1.0231 | 0.0439 | 0.2079 | 0.0764 | 0 |
| MB | 10 | 18 | 1.3183 | 0.2673 | 1.0339 | 0.0170 | 0.2505 | 0.1027 | 0 |
| ON | 10 | 14 | 0.6416 | 0.2347 | 0.3758 | 0.0310 | 0.2366 | 0.0895 | 0 |
| QC | 10 | 14 | 0.9048 | 0.2347 | 0.6544 | 0.0157 | 0.2446 | 0.0965 | 0 |
| NB | 10 | 10 | 0.4671 | 0.1387 | 0.3130 | 0.0153 | 0.2663 | 0.0965 | 0 |
| NS | 10 | 14 | 0.6416 | 0.2347 | 0.3758 | 0.0310 | 0.2314 | 0.0843 | 0 |
| PE | 10 | 14 | 1.2546 | 0.9284 | 0.3109 | 0.0153 | 0.2369 | 0.0937 | 0 |
| NL | 10 | 10 | 0.5301 | 0.2347 | 0.2800 | 0.0153 | 0.2445 | 0.0941 | 0 |
| YT | 10 | 20 | 1.7899 | 1.2218 | 0.5383 | 0.0298 | 0.2229 | 0.0871 | 0 |
| NT | 10 | 17 | 1.6928 | 0.7458 | 0.9299 | 0.0170 | 0.2525 | 0.1045 | 0 |
| NU | 10 | 15 | 1.1458 | 0.7458 | 0.3531 | 0.0469 | 0.2175 | 0.0836 | 0 |

## Facility coefficient comparison
| Province | Model solid share | Facility solid share | Model residue odt/m3 | Facility harvest residue odt/m3 | Status | Dominant factor |
|---|---:|---:|---:|---:|---|---|
| BC | 0.946 | 0.689 | 0.0158 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;local_taper |
| AB | 0.471 | 0.689 | 0.0513 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| SK | 0.436 | 0.689 | 0.0422 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| MB | 0.216 | 0.689 | 0.0779 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| ON | 0.414 | 0.689 | 0.1394 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| QC | 0.277 | 0.689 | 0.1067 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;local_taper |
| NB | 0.330 | 0.689 | 0.2067 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| NS | 0.414 | 0.689 | 0.1314 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| PE | 0.752 | 0.689 | 0.0747 | 0.0762 | within_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| NL | 0.472 | 0.689 | 0.1774 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| YT | 0.699 | 0.689 | 0.0486 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| NT | 0.451 | 0.689 | 0.0618 | 0.0762 | outside_20pct | synthetic_tree_list;dimension_sort_assumption;donor_taper |
| NU | 0.692 | 0.000 | 0.0730 | 0.0000 | not_comparable_zero_harvest | synthetic_tree_list;dimension_sort_assumption;donor_taper |

## Checks
- `thirteen_jurisdictions`: **PASS** — 13 jurisdictions present
- `ten_trees_per_province`: **PASS** — BC=10; AB=10; SK=10; MB=10; ON=10; QC=10; NB=10; NS=10; PE=10; NL=10; YT=10; NT=10; NU=10
- `volume_balance`: **PASS** — national balance error 0 m3
- `net_defect_balance`: **PASS** — national net+defect error 3.55e-15 m3
- `no_nan`: **PASS** — numeric columns contain no NaN
- `no_negative`: **PASS** — numeric columns are non-negative
- `grade_not_assigned`: **PASS** — 211 log rows grade=not_assigned
- `taper_evidence`: **PASS** — all taper rows are published_table
- `taper_dispatch`: **PASS** — local=['BC', 'QC']; donor=['AB', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'SK', 'YT']
- `provenance`: **PASS** — every tree carries representative_synthetic_v1 provenance and a basis label
- `coefficient_comparison`: **PASS** — 13 province comparison rows
- `labels`: **PASS** — model_estimate/synthetic/observed=false/policy_grade=false/national_claim=false
- `repository_hygiene`: **PASS** — no unexpected D in parent or data git status before run

## Limitations
- Tree lists are representative synthetic draws, not inventory, PSP data, or an NFI expansion.
- AB/ON/NS/NU species composition is a documented assumption because the open NFI coverage table has no provincial rows for them.
- Non-QC/BC trees use a cross-jurisdiction donor taper; donor BEC anchors are BC anchors, not local BEC zones.
- Dimension-only pilot sorts are not official federal or provincial log grades; grade=not_assigned.
- Prices, density, moisture, chip and hog yields are pilot assumptions.
- Facility coefficient comparison is screening only; harvest residue and facility process residue are different streams.
- No national, operational, policy-grade, AAC, or investment claim is made.
- No UI or public OSeCAN surface was changed.

No UI, public OSeCAN surface, policy grade, AAC, or national supply claim is made.
