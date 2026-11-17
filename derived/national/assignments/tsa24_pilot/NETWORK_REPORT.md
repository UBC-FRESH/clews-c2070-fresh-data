# BC Road-Network Transport Pilot (NRN)

## 1. Network

- **Layer:** `NRN_BC_14_0_ROADSEG` from
  `data/raw/nrn/nrn_bc_gpkg.zip` (English GeoPackage member
  `NRN_BC_14_0_GPKG_en.gpkg`; NRN 2.0 `SPECVERS`, archive
  member dated `2018-10-25`).
- **CRS:** source `EPSG:4617`; metric routing
  and lengths in `EPSG:3005`.
- **Clip:** No clip: the full BC NRN road layer was processed (bounds (-136.854, 48.3266, -114.218, 60.0018)).
- **Graph:** 203,511 nodes and 242,059 undirected edges
  after minimum length per unordered endpoint pair; 197 connected
  components, largest 157,089 nodes
  (77.2%).
- **Build:** total 10.9 s (read 2.1 s,
  project 0.7 s, graph 7.0 s); peak RSS
  581 MB. Timebox 780 s;
  within timebox.
- **Node snap:** segment endpoints snapped to a
  1.0 m grid before deduplication.
- **Facility snap:** nearest graph node within
  5000 m.
- **One-way:** `TRAFFICDIR` values
  {'Unknown': 263584}; all edges treated as bidirectional.
- **Class filter:** kept 244,224 of
  263,584 segments. Pedestrian classes
  present: none.

| ROADCLASS | Segments | Treatment |
|---|---|---|
| Arterial | 18923 | included |
| Collector | 30309 | included |
| Expressway / Highway | 9741 | included |
| Freeway | 1843 | included |
| Local / Strata | 15179 | included |
| Local / Street | 157655 | included |
| Local / Unknown | 3701 | included |
| Resource / Recreation | 6873 | included |
| Alleyway / Lane | 12084 | excluded |
| Ramp | 3686 | excluded |
| Service Lane | 3590 | excluded |

## 2. Snapping

Anchor `BC-SAW-506` snapped to a node 812.4 m
away (status `snapped`); it is on the graph and was used
as the shortest-path source. Across all 179 facilities,
163 carry coordinates: 156 snapped within
5000 m, 7 were
`too_far`, and 16 were `missing_coord` (never snapped).

| coord_source | Total | With coord | Snapped | Too far | Missing coord | In scope | In-scope snapped |
|---|---|---|---|---|---|---|---|
| mills_db_2015 | 98 | 98 | 98 | 0 | 0 | 88 | 88 |
| missing | 16 | 0 | 0 | 0 | 16 | 15 | 0 |
| tl_anchor_proxy | 65 | 65 | 58 | 7 | 0 | 58 | 51 |

Real paths were available for **134**
of the 163 coordinate-bearing facilities. Facilities on a
different connected component from the anchor are marked `no_path` rather than
given a Euclidean guess. One island facility (`BC-SAW-383`) snaps to a separate
Vancouver Island component; no ferry link is added in this pass.

## 3. Distances and costs

Matched real/FFCM facilities: 117.

| Distance set | Distribution (km) |
|---|---|
| Real NRN road | n=117, min 12.0, p25 139.3, median 375.1, p75 725.9, max 1118.9 |
| FFCM TL graph (same facilities) | n=117, min 316.0, p25 483.0, median 911.2, p75 1161.4, max 2582.4 |
| Real - FFCM | n=117, min -1563.7, p25 -477.4, median -351.0, p75 -304.6, max -258.3 |
| Real / FFCM | n=117, min 0.02, p25 0.31, median 0.46, p75 0.62, max 0.77 |
| 150 km diagnostic (same facilities) | n=117, min 151.0, p25 175.4, median 267.6, p75 361.3, max 651.9 |
| Real on old-diagnostic match | n=117, min 12.0, p25 139.3, median 375.1, p75 725.9, max 1118.9 |

Outliers (|real - FFCM| > 100 km or ratio outside 0.67-1.5): 
109. Top 20:

| Facility | Real km | FFCM km | Delta km | Ratio |
|---|---|---|---|---|
| BC-PAP-1163 | 1018.7 | 2582.4 | -1563.7 | 0.39 |
| BC-SAW-1704 | 375.1 | 1274.3 | -899.2 | 0.29 |
| BC-SAW-762 | 375.1 | 1122.6 | -747.4 | 0.33 |
| BC-PEL-383 | 12.0 | 738.8 | -726.8 | 0.02 |
| BC-SAW-352 | 1118.9 | 1831.6 | -712.7 | 0.61 |
| BC-SAW-397 | 1100.7 | 1810.5 | -709.8 | 0.61 |
| BC-SAW-1020 | 375.1 | 1031.4 | -656.2 | 0.36 |
| BC-SAW-114 | 657.9 | 1313.8 | -655.9 | 0.50 |
| BC-SAW-1289 | 375.1 | 1018.1 | -642.9 | 0.37 |
| BC-SAW-1736 | 929.7 | 1557.4 | -627.7 | 0.60 |
| BC-SAW-535 | 375.1 | 982.6 | -607.5 | 0.38 |
| BC-SAW-1014 | 929.7 | 1536.1 | -606.4 | 0.61 |
| BC-PEL-210 | 12.0 | 612.1 | -600.1 | 0.02 |
| BC-SAW-1706 | 375.1 | 967.9 | -592.7 | 0.39 |
| BC-PEL-1651 | 375.1 | 948.1 | -572.9 | 0.40 |
| BC-SAW-754 | 375.1 | 943.6 | -568.5 | 0.40 |
| BC-PEL-4100 | 375.1 | 942.6 | -567.5 | 0.40 |
| BC-SAW-23 | 375.1 | 942.0 | -566.9 | 0.40 |
| BC-SAW-1731 | 375.1 | 938.6 | -563.5 | 0.40 |
| BC-SAW-1737 | 375.1 | 922.6 | -547.4 | 0.41 |

**Cost formula.** No transload for direct road. For grade `g`:

`cost_cad_m3 = distance_km * (fuel_cost + operating_cost / cruising_speed) / capacity_m3`

where capacity is the Stage A transporter-material capacity converted to green
m3 at the grade density, and costs/rates come from
`metadata/ffcm-archive/parsed/transporters.csv` and
`transporter_materials.csv`. Route capacity is absent; every link records
`capacity_m3=None`, `capacity_source=absent`.

| Grade | Transporter | CAD/km | Capacity m3 | CAD/m3/km |
|---|---|---|---|---|
| HOGFUEL | BC_residue_truck | 2.5906 | 55.56 | 0.046631 |
| OTHER_LOG | BC_logging_truck | 2.5906 | 46.10 | 0.056196 |
| PULP | BC_logging_truck | 2.5906 | 46.10 | 0.056196 |
| RESIDUE | BC_residue_truck | 2.5906 | 55.56 | 0.046631 |
| SAWLOG | BC_logging_truck | 2.5906 | 46.10 | 0.056196 |

Matched real/FFCM cost comparison (same facility-grade pairs):

| Grade | Links | Real median CAD/m3 | FFCM median CAD/m3 | Delta median CAD/m3 |
|---|---|---|---|---|
| HOGFUEL | 10 | 9.93 | 28.77 | -19.01 |
| OTHER_LOG | 34 | 11.81 | 35.41 | -22.26 |
| PULP | 34 | 11.81 | 35.41 | -22.26 |
| RESIDUE | 23 | 11.16 | 30.22 | -19.01 |
| SAWLOG | 94 | 21.29 | 61.19 | -28.69 |

FFCM costs in this comparison include transload at TL nodes; real NRN costs are
direct road with no transload. The gap is therefore a combined distance and
transload difference, not a like-for-like rate comparison.

## 4. Stage A re-run

The base 1,000 ha and ws4-quota runs use real NRN links for facilities with a
real path and flagged FFCM fallback links elsewhere. Every fallback is recorded
in `transport_links_bc.csv` with status
`linked_ffcm_fallback_no_real_road_path`.

| Run | Assigned m3 | Unassigned m3 | Objective CAD | Delivered CAD/m3 | Transport CAD/m3 |
|---|---|---|---|---|---|
| Base 1,000 ha | 311,600 | 0 | 4,959,577 | 125.35 | 0.65 |
| ws4 quota | 77,461,964 | 17,902,375 | -19,233,509,115 | 150.21 | 20.15 |
| Previous run | 311,600 | 0 | 3,995,058 | 128.45 | 3.74 |
| Previous run ws4 quota | 77,254,230 | 18,110,109 | -20,478,028,147 | 163.58 | 33.60 |

Base assigned facilities: 6 total; 6 with a real NRN path (BC-PAP-964, BC-PEL-210, BC-PEL-383, BC-SAW-1009, BC-SAW-141, BC-SAW-977) and 0 on FFCM fallback (none).

ws4-quota assigned facilities: 129 total; 118 real and 11 fallback.

| Class | Base current | Base previous | ws4 current | ws4 previous | FFCM nameplate |
|---|---|---|---|---|---|
| BIO | 0.0% | 0.0% | 10.0% | 10.0% | 9.1% |
| PAP | 7.0% | 7.0% | 30.9% | 31.0% | 33.8% |
| PEL | 22.7% | 22.7% | 8.9% | 8.9% | 7.5% |
| SAW | 70.3% | 70.3% | 50.2% | 50.1% | 49.6% |

Real-road facility count in the current run:
118; FFCM
fallback facility count:
11.
The fallback list is in `road_network_summary.json` and the Stage A manifest.

## 5. Gaps and next

- NRN BC archive is the 2018 NRN 2.0 release; resource-road coverage is
  incomplete relative to current forest operations.
- `TRAFFICDIR` is `Unknown` for every segment, so one-way restrictions are not
  modelled.
- 7 coordinate-bearing facilities are more than
  5000 m from an NRN node; they keep a
  flagged FFCM fallback rather than a fabricated distance.
- The 5 km snap access leg is recorded as `snap_m` but is not added to the
  graph distance or cost; it remains an unmodelled access gap.
- Vancouver Island is disconnected from the mainland road component; ferry
  segments (NRN `FERRYSEG`) and ferry fares/times are not included.
- NRWN rail is not used in this pass; all links are road.
- Route and transload capacity remain absent; the LP cannot model congestion or
  mode-shift limits.
- Real and FFCM-fallback links have different cost bases; the Stage A objective
  is a mixed-basis diagnostic, not a production delivered-cost estimate.
