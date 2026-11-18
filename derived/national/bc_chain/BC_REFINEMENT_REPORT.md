# BC chain refinement: ferry connectivity and species alias recovery

Generated 2026-11-18.  This report covers the refinement of the all-BC
B1/B2 chain in `data/derived/national/bc_chain/` and the area-weight inputs in
`data/derived/national/assortments/bc_area_weights/`.  It is a diagnostic
chain, not an operational plan.

## Ferries

### Layer and treatment

- Source layer: `NRN_BC_14_0_FERRYSEG` in `data/raw/nrn/nrn_bc_gpkg.zip`
  (NRN 2.0, EPSG:4617 source; projected to EPSG:3005 for routing).
- NRN ferry features read: **56**.  Usable NRN segments connected to the road
  graph: **53**.  Rejected terminal snaps: **3** (`263585`, 14.9 km;
  `263587`, 5.1 km; `263624`, 13.5 km from the nearest road node).  They are
  listed in `bc_stage_a_summary.json` under
  `transport_summary.ferry_graph_summary.rejected`.
- Ferry edges added: **54** = 53 NRN segments plus one documented fallback
  route, Comox-Powell River, whose NRN terminal snap was more than the 3 km
  route-dedup tolerance from the published terminal pair.  The other five
  documented major routes were already covered by NRN segments and were not
  double-counted: Tsawwassen-Swartz Bay, Horseshoe Bay-Departure Bay,
  Horseshoe Bay-Langdale, Port Hardy-Prince Rupert, Skidegate-Prince Rupert.
- Ferry network length: **1,951.95 km**.  Crossing time is
  `length / 33 km/h` (18 kn); no sailing schedule, queue, or seasonal capacity
  is modelled.
- Ferry cost: **0.03 CAD/m3/km placeholder**, flagged
  `placeholder_not_a_bc_ferries_tariff`.  This is not a BC Ferries tariff and
  must not be cited as one.  It produces a maximum link charge of
  **27.74 CAD/m3** on the longest island path and a mean of **1.01 CAD/m3**
  across all 298 links (including zero-ferry links).
- Terminal snapping uses the same nearest-road-node method as facilities,
  with a documented 5 km tolerance.  The B1 zone centroid now snaps
  **86.5 km** from the main road component (B2: 4.0 km); this is a large
  zone-proxy access gap and is recorded in `origin_snap_m`.

### Newly connected B1 island/coastal facilities

Twelve facilities that previously had `no_graph_path` now have a real
zone-to-facility path.  Eleven received Stage A volume; the twelfth
(Catalyst-Powell River) is connected but not selected.

| Facility | Class | Location | Assigned m3 |
|---|---|---|---:|
| Catalyst-Crofton | PAP | Crofton, Vancouver Island | 3,004,902 |
| Nanaimo-Harmac | PAP | Nanaimo, Vancouver Island | 2,402,236 |
| Catalyst-Port Alberni | PAP | Port Alberni, Vancouver Island | 651,743 |
| Catalyst-Powell River | PAP | Powell River, mainland coast | 0 |
| Western Forest Products-Chemainus | SAW | Chemainus, Vancouver Island | 445,995 |
| Western Forest Products-Duke Point | SAW | Nanaimo, Vancouver Island | 600,377 |
| Western Forest Products-Somass | SAW | Port Alberni, Vancouver Island | 600,377 |
| Western Forest Products-Alberni Pacific | SAW | Port Alberni, Vancouver Island | 572,932 |
| Franklin Forest Products | SAW | Port Alberni, Vancouver Island | 65,870 |
| Errington Cedar Products | SAW | Errington, Vancouver Island | 55,303 |
| Suncoast Lumber & Milling | SAW | Sechelt, mainland coast | 39,694 |
| Abfam Enterprises | SAW | Port Clements, Haida Gwaii | 31,288 |

Total assigned to these facilities: **8,470,715 m3**, all in B1.

## Species aliases

### Rules

Exact CASFRI crosswalk targets always win.  Aliases are applied only where the
CASFRI target has no RSYC species.  Every area row now carries
`alias_source`, `alias_rule`, and `alias_confidence`; the full long-form table
is `bc_species_alias_table.csv`.

| BC code | Target | Rule | Confidence | Recovered ha |
|---|---|---|---|---:|
| SX | PICE.GLA interior/boreal; PICE.SIT coast | `SX_hybrid_spruce_coast_SIT_interior_GLA` | medium | 7,740,081 |
| S | PICE.GLA interior/boreal; PICE.SIT coast | `S_spruce_coast_SIT_interior_GLA` | medium | 1,103,415 |
| YC | CONIFEROUS | `YC_yellow_cedar_no_rsyc_target_group_conifer` | low | 704,155 |
| H | TSUG.HET | `H_hemlock_to_western_hemlock` | high | 581,589 |
| B | ABIE.LAS | `B_balsam_to_subalpine_fir_ABIE_LAS` | medium | 459,529 |
| ACT | POPU.BAL | `ACT_black_cottonwood_to_balsam_poplar_Tacamahaca` | medium | 144,925 |
| PA | CONIFEROUS | `PA_whitebark_pine_no_rsyc_target_group_conifer` | low | 111,652 |
| **Total** | | | | **10,845,346** |

Two brief suggestions were deliberately not followed because the source code
set contradicts them:

- **B (balsam)**: the brief suggested `ABIE.BAL`.  `ABIE.BAL` is eastern balsam
  fir and is not a BC commercial species; CASFRI maps BC `B` to `ABIE_SPP`, and
  the BC balsam stream is subalpine fir (`ABIE.LAS`).  The alias uses
  `ABIE.LAS` and records the deviation.
- **PA**: the brief labelled `PA` as paper birch.  The CASFRI crosswalk and the
  BC VRI code set identify `PA` as whitebark pine (`PINU_ALB`), which has no
  RSYC target.  Paper birch is `EP`/`BETU.PAP` and is already an exact
  crosswalk.  `PA` is therefore carried as `CONIFEROUS`, flagged low
  confidence, rather than forcing 111,652 ha of whitebark pine into paper
  birch.

### Area recovery and conservation

- Forest area: **56,428,146 ha**; THLB: **18,653,774 ha** (unchanged).
- Alias-recovered area: **10,845,346 ha**.
- Residual unmapped: **161,971 ha (0.29% of forest area)**, down from
  **11,007,317 ha (19.5%)**.  The largest remaining codes are LA 52,011 ha,
  E 43,362 ha, PW 35,137 ha, L 11,129 ha, BG 7,040 ha.  They are kept
  explicit and are not folded into a group.
- Conservation: sum of area before and after aliasing is identical at
  56,428,146 ha; the 2,384-row area table sums to the same total.

Species totals changed only by the alias transfers:

| Species | Previous ha | New ha | Delta ha |
|---|---:|---:|---:|
| PICE.GLA | 1,473,917 | 10,158,991 | +8,685,074 |
| CONIFEROUS | 0 | 815,807 | +815,807 |
| TSUG.HET | 3,542,181 | 4,123,770 | +581,589 |
| ABIE.LAS | 8,418,010 | 8,877,540 | +459,529 |
| PICE.SIT | 267,753 | 426,176 | +158,423 |
| POPU.BAL | 492,595 | 637,520 | +144,925 |
| UNMAPPED_BC | 11,007,317 | 161,971 | -10,845,346 |

## Re-run

### Area and supply

The 2028 AAC is unchanged: B1 9,120,805 m3, B2 34,249,971 m3.  Harvest area
and residue change because the species mix now carries the recovered spruce,
hemlock, balsam, cottonwood, and yellow-cedar area.

| Zone | Year | AAC m3 | Harvest ha | Log m3 | Gross residue odt | Recoverable odt | Recoverable PJ |
|---|---|---:|---:|---:|---:|---:|---:|
| B1 | 2028 | 9,120,805 | 28,596 | 9,120,805 | 324,818 | 194,891 | 3.61 |
| B2 | 2028 | 34,249,971 | 193,405 | 34,249,971 | 2,981,142 | 1,740,782 | 32.20 |

### Stage A (2028)

| Metric | Previous | New | Change |
|---|---:|---:|---:|
| Total supply m3 | 48,207,935 | 47,672,271 | -535,664 (-1.1%) |
| Assigned m3 | 45,590,661 | 47,672,271 | +2,081,609 (+4.6%) |
| Unassigned m3 | 2,617,273 | 0 | -2,617,273 (-100%) |
| Assigned share | 94.6% | 100.0% | +5.4 pp |
| Solver objective CAD | 626,511,267 | 3,675,102,299 | +3,048,591,033 |
| Net before unassigned penalty CAD | 3,243,784,537 | 3,675,102,299 | +431,317,762 (+13.3%) |

The solver objective is not comparable directly: the previous run charged a
2.617 billion CAD diagnostic unassigned penalty.  The before-penalty net
contribution is the comparable economic measure and rises 13.3%.

B1 SAWLOG is the key change: **assigned 6,153,900 -> 8,806,340 m3**, and
**unassigned 2,617,273 -> 0 m3**.

Facility class mix:

| Class | Previous assigned m3 | Previous util. | New assigned m3 | New util. | New binding |
|---|---:|---:|---:|---:|---:|
| BIO | 4,320,244 | 51.9% | 0 | 0.0% | 0 |
| PAP | 10,127,286 | 32.9% | 14,545,888 | 47.3% | 7 |
| PEL | 4,841,690 | 70.6% | 4,413,106 | 64.3% | 1 |
| SAW | 26,301,442 | 58.2% | 28,713,277 | 63.6% | 46 |

BIO receives no Stage A volume in the new run.  This is an economic model
outcome (BIO product revenue is low relative to PAP/PEL), not a policy
statement; it is flagged as a diagnostic gap.

### Stage B (sawmill residue)

| Metric | Previous | New | Change |
|---|---:|---:|---:|
| Generated odt | 6,826,610 | 7,452,609 | +625,998 (+9.2%) |
| Assigned odt | 6,145,981 | 6,856,004 | +710,023 (+11.6%) |
| Unassigned odt | 680,629 | 596,605 | -84,024 (-12.3%) |
| Bioenergy odt | 694,620 | 758,943 | +64,324 (+9.3%) |

Harvest residue recoverable falls from 2,176,721 to 1,935,673 odt because the
recovered species mix has a lower taper-residue fraction; sawmill residue
rises because more B1 sawlog is now assigned.  The two are different residue
streams and are not additive.

## Comparison to previous BC chain

| Dimension | Previous | New |
|---|---|---|
| Unmapped species area | 11,007,317 ha (19.5%) | 161,971 ha (0.29%) |
| Graph edges | 242,059 | 242,113 |
| Zone-facility-grade links | 258 | 298 |
| Facilities with no path | 50 | 10 |
| Ferry links | 0 | 64 |
| B1 SAWLOG unassigned | 2,617,273 m3 | 0 m3 |
| Stage A assigned share | 94.6% | 100.0% |
| Stage B generated | 6,826,610 odt | 7,452,609 odt |

The B1 zone node moved because the main road component now includes
Vancouver Island and coastal TSAs.  The B1 centroid snaps 86.5 km from the
main graph; the zone-to-node access leg is not costed.  This is the main
remaining spatial proxy gap.

## Tests, commits, publish, status

### Tests

- `pytest workflows/national/assignments/tests workflows/national/assortments/tests -q`:
  **119 passed**, 2 deprecation warnings.
- Added tests: ferry edge connectivity and component merge; NRN ferry layer
  presence and positive placeholder; alias rules (coast/interior split, exact
  crosswalk precedence, unknown code); alias area recovery/conservation; Stage A
  rerun volume and class-mix invariants.

### Commits and publish

- Data submodule and parent commit hashes, annex publication, and
  `git status --porcelain` are recorded in the operator response and in the
  parent commit message.  No changed files in this run are annex objects; the
  derived CSV/JSON/Markdown outputs are regular git blobs.  `git annex status`
  shows no modified annexed payload.
- The BC chain manifest (`manifest.json`) records input and output hashes.

## Gaps and next

- Three NRN ferry segments have terminal endpoints more than 5 km from the
  road graph; they are rejected rather than snapped to a wrong road.
- Ferry fare and crossing time are placeholders.  A real BC Ferries commercial
  tariff and schedule would change island delivered costs.
- The B1 zone centroid is a poor spatial proxy once island TSAs are included.
  A zone node on the main component, or separate island sub-nodes, would
  reduce the 86.5 km snap gap.
- BIO receives no Stage A volume; verify whether the FFCM BIO product revenue
  and capacity basis are intended to be economic or policy-constrained.
- Residual unmapped codes (LA, E, PW, L, BG, RA, EA, VB, W, QG, AX, BP, X)
  remain explicit.  They are small (161,971 ha total) and were not forced into
  a species or group.
- The pilot `NETWORK_REPORT.md` under `data/derived/national/assignments/tsa24_pilot/`
  was not regenerated in this pass; the code now adds ferries, so a pilot
  re-run would refresh it.
