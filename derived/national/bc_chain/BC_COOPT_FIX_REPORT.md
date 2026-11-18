# BC residue co-optimisation: review-fix report

Date: 2026-11-18. Period: 2028. Scope: the four material review findings and
the report guard. Diagnostic only; not an operating plan.

## 1. Harvest supply source

- Before: harvest sources were built only from the Stage A **assigned**
  `RESIDUE` grade, so the LP could not re-home recoverable residue that Stage A
  left unassigned.
- After: harvest sources are the period-specific `residue_recoverable_odt`
  offers in `bc_supply_by_zone.csv`, grouped by zone (`HARVEST::B1`,
  `HARVEST::B2`). Stage A log assignment remains fixed. Stage A-assigned
  residue is carried as `stage_a_assigned_odt` for reporting only.
- Current data after the 2026-11-18 FFCM-implied basis rebuild: recoverable
  **2,352,639 odt** (B1 194,891; B2 2,157,748), Stage A assigned
  **2,352,639 odt**, Stage A unassigned **0.004 odt**, co-opt assigned
  **2,352,639 odt** (100.00% of recoverable). The previous 1,935,673 odt case
  held B2 recovery at 0.583931; the adopted B2 recovery is 0.723799.
- The review cited 2,176,721 odt (B1 198,637; B2 1,978,084). That total is the
  pre-refinement `bc_supply_by_zone.csv` at data commit `3a76984`; the current
  regenerated file at `8473cac`/`f6e824a` sums to 1,935,673 odt. The code now
  reads the file directly, so a restored 2,176,721 odt supply would enter the
  LP in full rather than being truncated to Stage A-assigned volume.
- Added tests: recoverable-vs-assigned source construction, recoverable
  conservation, and fail-closed Stage A assignment above recoverable.

## 2. Route provenance and fallback links

- Before: `ffcm_route_fallback_road` links were accepted and missing
  provenance silently defaulted to `real_road_network`. The materialised
  assignment sent hogfuel to BC-BIO-4007 on a fallback link.
- After: `CooptLink` carries `path_confidence`, `evidence`,
  `ferry_distance_km`, and `ferry_cost_cad_m3`. Default accepted provenance is
  only `real_road_network`. Fallback links are excluded and reported in
  `excluded_pairs` with reason `non_nrn_fallback`; they enter only with
  explicit `allow_fallback_links=True` / `--allow-fallback-links`. Missing,
  NaN, or empty provenance fails closed.
- Current default run: **51** fallback pairs excluded, covering at most
  **710,678 odt** of source supply; **10** pairs have no transport link.
  Net contribution is CAD 957,802,389 on the adopted 2,352,639 odt harvest
  basis.
- Previous sensitivity (`allow_fallback_links=True`, written to a temporary
  directory, not published, on the 1,935,673 odt case): 10 fallback
  allocations, **80,304 odt**, net contribution CAD 947,920,764 versus
  CAD 947,142,387 default. Total assigned residue was effectively unchanged
  (8,841,757 odt); the fallback sensitivity only changed routing and net
  contribution. It was not rerun on the adopted basis.
- Validation now checks every allocation against the accepted arc set and its
  accepted provenance, with no defaulting.

## 3. Ferry costing and edge metadata

- Before: the graph kept the shortest edge for a node pair but the ferry
  lookup kept the longest ferry length for the same pair. Stage B charged the
  road rate on ferry kilometres; `bc_chain.py` inherited the same pair logic.
- After: the winning edge is selected with its own mode, length, and
  provenance (`edge_mode`, `edge_provenance`). Ferry arrays are rebuilt from
  winning ferry edges only, so a road edge cannot inherit another edge's ferry
  distance. Same-node published fallback snaps are rejected. Duplicate ferry
  pairs fail closed in `ferry_pair_lookup`.
- Stage A and Stage B both use `road_ferry_cost(...)`:
  `road_rate * (distance_km - ferry_km) + 0.03 * ferry_km`, with the Stage A
  `BC_residue_truck` rate and the same ferry placeholder. Both preserve
  `ferry_distance_km`, `ferry_cost_cad_m3`, `path_confidence`, and `evidence`.
- Stage A links: unchanged (64 ferry links, 10,078.6 ferry km; zero distance
  or cost changes), because no ferry edge in this graph lost to a shorter road
  edge.
- Stage B links: **530** links carry ferry distance, **30,060.3 ferry km**.
  Link-table transport cost falls from CAD 46,259.88 to CAD 45,759.93 per m3
  summed over all links. Stage B transport cost falls from CAD 278,936,925 to
  CAD 274,769,703; net contribution rises from CAD 865,961,449 to
  CAD 870,128,671. Stage B assigned volume is unchanged at 6,856,004 odt.
- Added tests: parallel road/ferry edge selection with mode/provenance,
  duplicate-ferry rejection, path decomposition, and Stage A/Stage B shared
  helper identity. The real Stage A link table still reconciles exactly to the
  same distance and cost.

## 4. Report guard

- All shares and utilization values use `_share()`; a zero or non-finite
  denominator emits `n/a` in Markdown and `null` in JSON instead of raising or
  writing NaN. Zero-capacity utilization rows are guarded.

## Re-run result (2028)

| metric | before | after |
|---|---:|---:|
| generated odt | 8,841,756.841 | 8,841,756.852 |
| assigned odt | 8,841,756.807 | 8,841,756.848 |
| unassigned odt | 0.034 | 0.004 |
| BIO odt | 2,118,365.973 | 2,118,365.996 |
| product revenue CAD | 2,085,149,279.53 | 2,085,149,286.17 |
| transport cost CAD | 330,282,746.67 | 326,876,053.65 |
| processing cost CAD | 811,130,843.19 | 811,130,845.64 |
| net contribution CAD | 943,735,689.67 | 947,142,386.88 |
| excluded pairs | 16 (all no-link) | 61 (10 no-link, 51 fallback) |
| capacity double-booking avoided odt | 1,309,342.575 | 1,309,343 |

The default solution contains 199 allocations; 58 of them use a path with
positive ferry distance (3,458.4 ferry km).

## Verification

- Focused tests pass: `test_residue_coopt.py`, `test_bc_chain.py`,
  `test_road_network.py`, and `test_stage_b.py` (42 passed); the full
  `workflows/national/assignments/tests` suite passes (92 passed).
- `ruff check` passes on every changed Python file.
- `bc_chain` and the co-opt were re-run from source; Stage B was re-run because
  its transport costs changed.

## Remaining independent-review items (next fix pass)

These were explicitly out of scope for this pass:

1. Alias-area leakage / `NO_ECOPROVINCE` handling in
   `workflows/national/assortments/bc_area_weights.py`.
2. NaN coercion in the supply and demand parsers.
3. Period alignment between supply, Stage A, and Stage B tables.
4. Stage B validation should be fatal rather than reporting a soft status.
5. Add a negative-margin service test at the shared-capacity boundary.
