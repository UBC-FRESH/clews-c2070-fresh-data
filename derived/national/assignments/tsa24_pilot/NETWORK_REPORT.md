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
- **Build:** total 11.5 s (read 2.0 s,
  project 0.6 s, graph 7.6 s); peak RSS
  579 MB. Timebox 780 s;
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

Anchor `BC-SAW-488` snapped to a node 812.4 m
away (status `snapped`); it is on the graph and was used
as the shortest-path source. Across all 179 facilities,
134 carry coordinates: 79 snapped within
5000 m, 55 were
`too_far`, and 45 were `missing_coord` (never snapped).

| coord_source | Total | With coord | Snapped | Too far | Missing coord | In scope | In-scope snapped |
|---|---|---|---|---|---|---|---|
| mills_db | 8 | 8 | 8 | 0 | 0 | 7 | 7 |
| missing | 45 | 0 | 0 | 0 | 45 | 41 | 0 |
| tl_anchor_proxy | 126 | 126 | 71 | 55 | 0 | 113 | 62 |

Real paths were available for **77**
of the 134 coordinate-bearing facilities. Facilities on a
different connected component from the anchor are marked `no_path` rather than
given a Euclidean guess. One island facility (`BC-SAW-383`) snaps to a separate
Vancouver Island component; no ferry link is added in this pass.

## 3. Distances and costs

Matched real/FFCM facilities: 62.

| Distance set | Distribution (km) |
|---|---|
| Real NRN road | n=62, min 485.8, p25 539.3, median 539.3, p75 678.4, max 990.1 |
| FFCM TL graph (same facilities) | n=62, min 466.8, p25 930.0, median 1023.2, p75 1163.4, max 2582.4 |
| Real - FFCM | n=62, min -2096.6, p25 -491.3, median -472.3, p75 -390.7, max 523.4 |
| Real / FFCM | n=62, min 0.19, p25 0.53, median 0.57, p75 0.59, max 2.12 |
| 150 km diagnostic (same facilities) | n=62, min 162.0, p25 176.2, median 267.5, p75 356.1, max 583.6 |
| Real on old-diagnostic match | n=62, min 485.8, p25 539.3, median 539.3, p75 678.4, max 990.1 |

Outliers (|real - FFCM| > 100 km or ratio outside 0.67-1.5): 
54. Top 20:

| Facility | Real km | FFCM km | Delta km | Ratio |
|---|---|---|---|---|
| BC-PAP-1163 | 485.8 | 2582.4 | -2096.6 | 0.19 |
| BC-SAW-352 | 485.8 | 1831.6 | -1345.8 | 0.27 |
| BC-SAW-397 | 485.8 | 1810.5 | -1324.7 | 0.27 |
| BC-SAW-1736 | 485.8 | 1557.4 | -1071.5 | 0.31 |
| BC-SAW-1014 | 485.8 | 1536.1 | -1050.3 | 0.32 |
| BC-SAW-1704 | 539.3 | 1274.3 | -735.0 | 0.42 |
| BC-SAW-1335 | 539.3 | 1267.5 | -728.2 | 0.43 |
| BC-SAW-178 | 539.3 | 1261.5 | -722.2 | 0.43 |
| BC-PAP-179 | 539.3 | 1260.4 | -721.1 | 0.43 |
| BC-BIO-4008 | 485.8 | 1171.7 | -685.9 | 0.41 |
| BC-SAW-762 | 539.3 | 1122.6 | -583.3 | 0.48 |
| BC-SAW-389 | 990.1 | 466.8 | 523.4 | 2.12 |
| BC-SAW-708 | 678.4 | 1193.1 | -514.7 | 0.57 |
| BC-SAW-711 | 678.4 | 1191.7 | -513.3 | 0.57 |
| BC-SAW-698 | 678.4 | 1184.6 | -506.1 | 0.57 |
| BC-SAW-696 | 678.4 | 1183.9 | -505.5 | 0.57 |
| BC-SAW-1020 | 539.3 | 1031.4 | -492.0 | 0.52 |
| BC-SAW-1021 | 539.3 | 1028.3 | -489.0 | 0.52 |
| BC-SAW-1707 | 678.4 | 1164.4 | -485.9 | 0.58 |
| BC-SAW-1732 | 678.4 | 1163.9 | -485.5 | 0.58 |

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

## 4. Stage A re-run

The base 1,000 ha and ws4-quota runs use real NRN links for facilities with a
real path and flagged FFCM fallback links elsewhere. Every fallback is recorded
in `transport_links_bc.csv` with status
`linked_ffcm_fallback_no_real_road_path`.

| Run | Assigned m3 | Unassigned m3 | Objective CAD | Delivered CAD/m3 | Transport CAD/m3 |
|---|---|---|---|---|---|
| Base 1,000 ha | 311,600 | 0 | -1,624,111 | 146.48 | 21.78 |
| ws4 quota | 79,479,094 | 15,885,245 | -18,448,503,043 | 165.15 | 34.63 |
| Previous TL-graph base | 311,600 | 0 | -1,624,111 | 146.48 | 21.78 |
| Previous TL-graph ws4 quota | 77,254,230 | 18,110,109 | -21,346,350,989 | 174.82 | 44.84 |

Base assigned facilities: 3 total; 0 with a real NRN path (none) and 3 on FFCM fallback (BC-PAP-964, BC-PEL-1650, BC-SAW-981).

ws4-quota assigned facilities: 134 total; 67 real and 67 fallback.

| Class | Base current | Base previous | ws4 current | ws4 previous | FFCM nameplate |
|---|---|---|---|---|---|
| BIO | 0.0% | 0.0% | 10.5% | 10.0% | 9.1% |
| PAP | 7.0% | 7.0% | 31.1% | 31.0% | 33.8% |
| PEL | 22.7% | 22.7% | 8.6% | 8.9% | 7.5% |
| SAW | 70.3% | 70.3% | 49.8% | 50.1% | 49.6% |

Real-road facility count in the current run:
67; FFCM
fallback facility count:
67.
The fallback list is in `road_network_summary.json` and the Stage A manifest.

## 5. Gaps and next

- NRN BC archive is the 2018 NRN 2.0 release; resource-road coverage is
  incomplete relative to current forest operations.
- `TRAFFICDIR` is `Unknown` for every segment, so one-way restrictions are not
  modelled.
- 55 coordinate-bearing facilities are more than
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
