# TSA24/BC Stage A Facility Assignment Pilot

> **Diagnostic pilot.** The supply area is `1,000 ha`, a
> contract/data-shape test, not a TSA24 supply estimate. Assortment sorts are
> dimension-only; no BC official grade equivalence is claimed. MKRF is not used.
> This version replaces the flat 150 km access leg with the parsed FFCM TL graph,
> adds facility coordinate provenance, and routes all capacity conversions
> through `units.py`.

## 1. Scope and Stage A/B split

Stage A consumes the TSA24 assortment matrix, parsed FFCM BC facility lines,
the FFCM TL transport graph, and diagnostic contracts, then solves a
profit-maximising transportation/allocation LP. It emits facility assignment,
utilization, contract, unassigned-supply, objective, and validation tables.
Stage B (`fresh_fibre.graph` / `fresh_fibre.lp`) consumes the Stage B
`supply_offer`, `technology`, and `transport_link` subset written alongside this
report; Stage A does not invent Stage B demand or market rows.

- Scenario: `tsa24_bc_stage_a_pilot`
- Period: `2026`
- Supply offers: 53
- Facilities: 161 screened; 129 with a transport link
- Transport links: 210
- Contracts: 161 (`contract_source=diagnostic_absent`)
- Total supply: 311,600 m3 green
- Solver: PULP_CBC_CMD 2.9.0 (Optimal)

## 2. BC facilities (coordinate coverage, sources, missing)

One row per BC facility is written to `facilities_bc.csv`. Coordinates are
resolved in this order: Mills DB, CFS `suppliers.dbf`, an FFCM TL/water hub
anchor, then `missing`. The hub anchor is the median coordinate of geocoded
facilities directly attached to the same TL/water node; it is a low-confidence
proxy, not a Euclidean guess.

| coord_source | All BC facilities | Stage A scope | Expected confidence |
| --- | --- | --- | --- |
| mills_db | 8 | 7 | high |
| suppliers_dbf | 0 | 0 | high |
| tl_anchor_proxy | 126 | 113 | low |
| missing | 45 | 41 | missing |

41 Stage A facilities have no coordinate; 45 of all BC facilities are missing. Missing coordinates are not replaced with Euclidean guesses.

Missing Stage A coordinates: `BC-SAW-281`, `BC-SAW-1735`, `BC-SAW-114`, `BC-SAW-163`, `BC-SAW-200`, `BC-SAW-242`, `BC-SAW-284`, `BC-SAW-363`, `BC-SAW-456`, `BC-SAW-609`, `BC-SAW-697`, `BC-SAW-810`, `BC-SAW-904`, `BC-SAW-905`, `BC-SAW-915`, `BC-SAW-916`, `BC-SAW-920`, `BC-SAW-935`, `BC-SAW-940`, `BC-SAW-992`, `BC-SAW-994`, `BC-SAW-1022`, `BC-SAW-1026`, `BC-SAW-1152`, `BC-SAW-1153` ...

TL/water hub proxies used by `coord_source=tl_anchor_proxy`:

| Hub | Lat | Lon | Geocoded anchors | Anchor facilities |
| --- | --- | --- | --- | --- |
| TL13 | 50.8750 | -119.5050 | 2 | BC-PLY-410;BC-SAW-418 |
| TL14 | 50.9900 | -118.2000 | 1 | BC-SAW-418 |
| TL19 | 50.1500 | -120.7800 | 3 | BC-SAW-384;BC-SAW-389;BC-SAW-488 |
| TL20 | 50.1250 | -121.7350 | 4 | BC-SAW-383;BC-SAW-384;BC-SAW-389;BC-SAW-488 |
| TL26 | 50.1500 | -122.6900 | 3 | BC-SAW-383;BC-SAW-389;BC-SAW-488 |
| TL27 | 50.7600 | -120.8100 | 1 | BC-PLY-410 |
| TL3 | 50.7600 | -120.8100 | 1 | BC-PLY-410 |
| W7 | 49.1800 | -116.5600 | 1 | BC-SAW-309 |

Zero/blank-capacity facilities: None; every BC facility has a positive normalized nameplate.


| Class | All BC rows | Stage A rows | Stage A nameplate m3/y | Linked |
| --- | --- | --- | --- | --- |
| SAW | 121 | 121 | 45,178,430 | 94 |
| PAP | 15 | 15 | 30,774,260 | 11 |
| PEL | 13 | 13 | 6,859,300 | 13 |
| BIO | 12 | 12 | 8,326,259 | 11 |
| PLY | 15 | 0 | 0 | 0 |
| OSB | 2 | 0 | 0 | 0 |
| NSP | 1 | 0 | 0 | 0 |

### 2.1 Capacity normalization

Capacity is normalized to green m3/y through `units.py`: `m3/y` directly,
`odt/y` and `bdmt/y` at the declared 0.45 ODT/m3 density, `admt/y` only with a
declared air-dry moisture, `mbf/y` only with a declared recovery factor, and
energy units never to volume. Facility nameplate is the sum of the maximum
normalized capacity per primary product. Rejected processing lines (first 15):

No processing line was rejected by the unit contract.

### 2.2 Transport screening

Facilities without a defensible TL path are excluded rather than given a
fabricated distance. Rejected facilities (first 20):

| Facility | Status | Reason |
| --- | --- | --- |
| BC-BIO-4017 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-PAP-589 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-PAP-590 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-PAP-591 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-PAP-731 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1022 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1152 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1153 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1472 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-163 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1698 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1700 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1705 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1710 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1728 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1730 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-1735 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-200 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-308 | missing_no_tl_route | no_TL_route_in_routes_csv |
| BC-SAW-309 | missing_no_tl_route | no_TL_route_in_routes_csv |

## 3. Transport (paths, modes, distance/cost vs 150 km, confidence)

- Accepted links: 210 across
  129 facilities.
- TSA24 anchor: `TSA24_AU23000` with
  anchor proxy `BC-SAW-488`.
  Access TL nodes:
  TL19, TL20, TL26.
- Anchor basis: `tsa24_prince_george_geocoded_mill_proxy;facility=BC-SAW-488;source=mills_db;note=no_TSA24_FMU_exists_in_FFCM_graph`.
- 210 links have `capacity=None`; `capacity_source=absent`; route capacity table=`absent`.

No accepted link uses `access_leg_plus_graph`: the anchor is attached through
parsed route edges from `BC-SAW-488`. That label is reserved for a future
non-route access leg.

| Path confidence | Facilities |
| --- | --- |
| direct_route | 61 |
| graph_shortest_path | 68 |

| Mode | Facilities |
| --- | --- |
| COMBINATION | 24 |
| ROAD | 105 |

| Distance set | Distribution (km) |
| --- | --- |
| New FFCM graph | n=129; min=316.0; p25=494.4; median=920.6; p75=1,161.8; max=2,582.4; mean=846.3 |
| Previous 150 km diagnostic | n=129; min=151.0; p25=175.4; median=261.2; p75=357.4; max=651.9; mean=287.6 |
| Delta new - old | n=129; min=165.0; p25=165.0; median=690.7; p75=986.1; max=2,095.8; mean=558.7 |
| Ratio new / old | n=129; min=1.25; p25=1.60; median=2.21; p75=5.27; max=8.02; mean=3.48 |

| Grade | New graph CAD/m3 | Previous diagnostic CAD/m3 | Delta CAD/m3 |
| --- | --- | --- | --- |
| SAWLOG | n=105; min=22.33; p25=32.47; median=61.39; p75=78.96; max=88.31; mean=56.27 | n=105; min=8.48; p25=9.73; median=14.23; p75=19.48; max=36.63; mean=15.79 | n=105; min=13.84; p25=13.84; median=47.96; p75=69.13; max=74.47; mean=40.48 |
| RESIDUE | n=24; min=19.53; p25=25.31; median=31.63; p75=52.75; max=63.64; mean=36.73 | n=24; min=7.33; p25=11.73; median=13.70; p75=17.96; max=26.76; mean=14.76 | n=24; min=12.19; p25=12.19; median=12.19; p75=41.21; max=43.76; mean=21.97 |

Distance/cost outliers versus the previous diagnostic (top 10 by delta):

| Facility | Class | Old km | New km | Delta km | Ratio | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| BC-PAP-1163 | PAP | 486.6 | 2,582.4 | 2,095.8 | 5.31 | graph_shortest_path |
| BC-SAW-352 | SAW | 400.5 | 1,831.6 | 1,431.1 | 4.57 | graph_shortest_path |
| BC-SAW-397 | SAW | 413.9 | 1,810.5 | 1,396.6 | 4.37 | graph_shortest_path |
| BC-SAW-1736 | SAW | 437.4 | 1,557.4 | 1,120.0 | 3.56 | graph_shortest_path |
| BC-SAW-1014 | SAW | 422.3 | 1,536.1 | 1,113.8 | 3.64 | graph_shortest_path |
| BC-SAW-940 | SAW | 159.5 | 1,227.0 | 1,067.5 | 7.69 | graph_shortest_path |
| BC-SAW-1467 | SAW | 181.7 | 1,244.3 | 1,062.6 | 6.85 | graph_shortest_path |
| BC-SAW-114 | SAW | 251.2 | 1,313.8 | 1,062.6 | 5.23 | graph_shortest_path |
| BC-SAW-1026 | SAW | 177.5 | 1,238.9 | 1,061.4 | 6.98 | graph_shortest_path |
| BC-SAW-242 | SAW | 180.1 | 1,241.5 | 1,061.4 | 6.89 | graph_shortest_path |


## 4. Units (accepted/rejected, factors)

| Unit | Dimension | Accepted | Source |
| --- | --- | --- | --- |
| admt | dry_mass | yes | FFCM unit-registry.csv: air-dry metric tonne; requires a declared air-dry moisture |
| bdmt | dry_mass | yes | FFCM unit-registry.csv: bone-dry metric tonne; 1 bdmt = 1 odt dry-mass equivalence (candidate) |
| bf | board_volume | yes | FFCM unit-registry.csv: board foot |
| gj | energy | yes | SI energy unit: gigajoule |
| kwh | energy | yes | SI energy unit: kilowatt-hour |
| m3_green | volume | yes | Stage A model basis: green solid cubic metre |
| mbf | board_volume | yes | FFCM unit-registry.csv: thousand board feet; volume needs a declared recovery factor |
| mwh | energy | yes | SI energy unit: megawatt-hour |
| odt | dry_mass | yes | FFCM unit-registry.csv: oven-dry tonne |
| m3 | volume | alias_of_m3_green | Stage A green-volume alias; no separate meaning |
| t | dry_mass | conditional_archive_tonne | FFCM transload $/t may opt in as odt; otherwise rejected |
| m3_odt | ambiguous | no | mixed volume/mass basis; rejected |

Declared factors:

| Conversion | Factor | Condition/source |
| --- | --- | --- |
| m3_green -> odt | 0.45 | declared basic density; default ledger density |
| odt -> m3_green | 2.222... | 1 / 0.45; per-grade/species override allowed |
| bdmt -> odt | 1.0 | dry-mass equivalence; FFCM unit registry candidate |
| admt -> odt | 1 - moisture | requires declared air-dry moisture |
| mbf -> m3_green | recovery | requires declared m3 per mbf; rejected otherwise |
| kWh -> MWh | 0.001 | SI |
| MWh -> GJ | 3.6 | SI |
| energy -> volume/mass | rejected | no declared energy density |


## 5. Pilot results

### 5.1 Assigned versus unassigned by grade

| Grade | Product | Offers | Supply m3 | Supply ODT | Assigned m3 | Unassigned m3 | Assigned share | Roadside CAD/m3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HOGFUEL | hogfuel | 0 | 0 | 0 | 0 | 0 | 0.0% | 0.00-0.00 |
| OTHER_LOG | other | 8 | 21,074 | 8,102 | 21,074 | 0 | 100.0% | 61.74-61.74 |
| PULP | pulpwood | 2 | 599 | 219 | 599 | 0 | 100.0% | 52.99-52.99 |
| RESIDUE | residue | 7 | 70,864 | 31,889 | 70,864 | 0 | 100.0% | 0.00-0.00 |
| SAWLOG | sawlog | 36 | 219,062 | 79,832 | 219,063 | 0 | 100.0% | 105.98-128.19 |

### 5.2 Facility utilization by class

| Class | Facilities | With link | Nameplate m3/y | Assigned m3 | Utilization | Binding | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BIO | 12 | 11 | 8,326,259 | 0 | 0.0% | 0 | 44 |
| PAP | 15 | 11 | 30,774,260 | 21,673 | 0.1% | 0 | 33 |
| PEL | 13 | 13 | 6,859,300 | 70,864 | 1.0% | 0 | 39 |
| SAW | 121 | 94 | 45,178,430 | 219,063 | 0.5% | 0 | 94 |

### 5.3 Capacity binding

No facility reached nameplate capacity in this run.

### 5.4 Largest assignments

| Facility | Class | Assigned m3 | Nameplate m3/y | Utilization |
| --- | --- | --- | --- | --- |
| BC-SAW-981 | SAW | 219,063 | 394,122 | 55.6% |
| BC-PEL-1650 | PEL | 70,864 | 1,004,500 | 7.1% |
| BC-PAP-964 | PAP | 21,673 | 1,730,006 | 1.3% |

### 5.5 Delivered cost per m3

| Component | CAD/m3 | Notes |
| --- | --- | --- |
| product revenue | 141.27 | assigned volume weighted |
| supply (roadside proxy) | 84.33 | assigned volume weighted |
| transport (FFCM TL graph) | 21.78 | assigned volume weighted; includes transload |
| gate | 0.00 | assigned volume weighted |
| processing | 40.38 | assigned volume weighted |
| delivered cost | 146.48 | supply + transport + gate + processing |
| net contribution | -5.21 | revenue - delivered cost |

### 5.6 Objective decomposition

| Component | Value CAD | Unit | Notes |
| --- | --- | --- | --- |
| product_revenue | 44,018,710.11 | CAD | assigned volume x facility product revenue |
| supply_cost | -26,275,684.72 | CAD | assigned volume x roadside cost proxy |
| transport_cost | -6,785,708.27 | CAD | assigned volume x FFCM TL-graph transport cost |
| gate_cost | -0.00 | CAD | assigned volume x contract gate cost |
| processing_cost | -12,581,427.77 | CAD | assigned volume x line processing cost |
| unassigned_penalty | 0.00 | CAD | unassigned volume x diagnostic penalty |
| net_objective | -1,624,110.64 | CAD | solver objective -1624110.644157 |

### 5.7 Class mix versus FFCM BC subset and previous pilot

| Class | Pilot assigned m3 | Pilot share | Previous pilot share | FFCM BC nameplate share | FFCM BC facility-count share |
| --- | --- | --- | --- | --- | --- |
| SAW | 219,063 | 70.3% | 70.3% | 49.6% | 75.2% |
| PAP | 21,673 | 7.0% | 7.0% | 33.8% | 9.3% |
| PEL | 70,864 | 22.7% | 22.7% | 7.5% | 8.1% |
| BIO | 0 | 0.0% | 0.0% | 9.1% | 7.5% |

FFCM BC nameplate/facility shares come from the 161 in-scope BC SAW/PAP/PEL/BIO facilities in `facilities.csv`. The directional FFCM `fmu -> facility` variable-family shares are SAW 85.8%, PAP 4.1%, PEL 7.0%, BIO 3.0%; that comparison is secondary and not a calibration target.

## 6. Contracts and capacity gaps

161 of 161 diagnostic contracts satisfy both bounds.
All contracts carry `contract_source=diagnostic_absent`; no populated real
contract minimum, maximum, or gate cost exists in the archive. Transport links
carry `capacity=None` and `capacity_source=absent`; route and transload
capacities are not present in the parsed tables. These are data gaps, not
modelled constraints.

## 7. Validation

| Check | Pass | Detail |
| --- | --- | --- |
| solver_status | yes | status=Optimal |
| volume_conservation | yes | assigned + unassigned equals supply for every offer |
| supply_reference_integrity | yes | all assignment rows reference a declared supply offer |
| grade_eligibility | yes | every assignment has a declared eligible grade and transport link |
| capacity | yes | no assignment exceeds a facility or grade capacity |
| facility_nameplate | yes | aggregate facility assignments stay within nameplate |
| contract_bounds | yes | all contracts satisfy min/max bounds |
| unassigned_reasons | yes | every unassigned row has a documented reason |
| moisture_blend | yes | facility moisture blends respect declared limits |
| unit_consistency | yes | all quantities use declared m3/odt conversions and every capacity basis is documented |
| transport_provenance | yes | every transport link declares path confidence, capacity source, and distance basis |
| contract_source | yes | diagnostic contracts declare diagnostic_absent |
| finite_values | yes | all assignment and slack values are finite |
| objective_reconciliation | yes | objective decomposition reconciles to the solver objective |
| utilization_reconciliation | yes | facility utilization rows reconcile to assignments |
| contract_report_completeness | yes | every contract has a compliance row |

Overall validation: **PASS**.

## 8. Assumptions and unit conversions

| Category | Assumption | Value | Unit | Evidence |
| --- | --- | --- | --- | --- |
| scope | TSA24/BC Stage A pilot supply area is a diagnostic scale, not a TSA supply estimate. | 1000.0 | ha | diagnostic |
| supply | Assortment matrix rows are per-hectare values; the pilot multiplies by the diagnostic area. | 311.6 | m3/ha | derived_tsa24_assortment_matrix |
| supply | Roadside cost is the assortment matrix price_cad_m3 proxy, not a harvest/stumpage cost. |  | CAD/m3 | derived_tsa24_assortment_matrix |
| residue | Residue volume uses the ledger 0.45 ODT/m3 basic density and 0.45 wet-basis moisture. | 0.45 | ODT/m3 | tsa24_residue_ledger_assumption |
| facility_capacity | m3/y infeed is used directly; odt/y and bdmt/y infeed use the declared 0.45 ODT/m3 density; admt/y is rejected without a declared air-dry moisture; mbf/y is rejected without a declared recovery factor; energy units cannot become volume. | 2.2222222222222223 | m3/ODT | units.py;archive_parsed_processing_lines;ledger_density |
| facility_capacity | Facility nameplate is the sum of the maximum normalized capacity per primary product; feedstock alternatives are not additive. |  | m3/y | archive_parsed_processing_lines |
| coordinate | Coordinates use Mills DB first, CFS suppliers.dbf second, an FFCM TL/water hub proxy third, and missing last; no Euclidean guesses are used. | mills_db=8;suppliers_dbf=0;tl_anchor_proxy=126;missing=45 | facility_count | facility_geocoding.csv;routes.csv |
| coordinate | Stage A scope coordinate coverage is tracked separately from all BC facilities. | mills_db=7;suppliers_dbf=0;tl_anchor_proxy=113;missing=41 | facility_count | facility_geocoding.csv;routes.csv |
| transport | The TSA24 supply anchor is a geocoded Prince George mill proxy because no TSA24 FMU exists in the FFCM graph. | BC-SAW-488 | facility_id | facility_geocoding.csv;routes.csv |
| transport | Distances are FFCM route-graph shortest paths from the anchor through TL nodes, not Euclidean distances. | 920.6438935022001 | km | archive_parsed_routes |
| transport | Road and rail costs use BC transporters with archive fuel and operating rates and material capacities; transload costs are added at each TL node. |  | CAD/m3 | archive_parsed_transporters;transporter_materials;transload_costs |
| transport | FFCM route capacity is absent from the parsed route table; every transport link is uncapped. |  | m3 | diagnostic |
| contracts | Contracts are diagnostic: min=0 and max=facility nameplate; no populated real contract table exists. |  | m3 | diagnostic_absent |
| objective | Unassigned supply carries a diagnostic penalty so that feasible supply is not silently dropped. | 1000.0 | CAD/m3 | diagnostic |
| grade | Assortment sorts are dimension-only; no BC official grade equivalence is claimed. |  | grade | derived_tsa24_assortment_matrix |
| scope | MKRF is not used anywhere in this pilot. |  | n/a | scope_rule |

The full assumption list, including rejected lines and rejected transport
links, is written to `assumptions.csv`, `line_screen.csv`, and
`transport_screen.csv`.

## 9. Gaps and next steps

- Replace the Prince George mill proxy with a real TSA24 supply-node or FMU
  anchor once the AU-to-FMU crosswalk exists. The current anchor is documented
  and low-confidence, not a production route.
- Replace the FFCM synthetic TL distances with an accepted BC road/rail network
  or a validated haul-distance model; the graph is sparse and produces long
  TL-TL paths.
- Populate route and transload capacity before interpreting congestion or
  mode-shift limits.
- Populate real contract minima, maxima, and gate costs.
- Normalize `admt/y` and `mbf/y` capacity only with declared moisture/recovery
  factors; the current pilot rejects them rather than guessing.
- Add mill-residue supply (sawdust/woodchips/hogfuel) if Stage A scope expands
  beyond logging residue.
- Add multi-period inventory, demand/market clearing, and line-level `y`
  variables only when the data support them.
- Do not interpret the 1,000 ha result as a TSA24 supply estimate. The optional
  ws4-quota sensitivity is a period-scale diagnostic and must be labeled as
  such.
