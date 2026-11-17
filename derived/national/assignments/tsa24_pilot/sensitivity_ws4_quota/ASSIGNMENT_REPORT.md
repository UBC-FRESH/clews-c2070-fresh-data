# TSA24/BC Stage A Facility Assignment Pilot

> **Diagnostic pilot.** The supply area is `306,047 ha`, a
> contract/data-shape test, not a TSA24 supply estimate. Assortment sorts are
> dimension-only; no BC official grade equivalence is claimed. MKRF is not used.
> This version uses the real NRN BC road graph for facilities with a snapped
> road path and keeps the parsed FFCM TL graph as a flagged fallback elsewhere.
> It adds facility coordinate provenance and routes all capacity conversions
> through `units.py`.
> **Period-scale sensitivity.** This run uses the ws4 quota area `306,047 ha/period`. It is not an annual supply forecast and its volume must not be compared directly with annual facility nameplate without a period normalization.

This version uses the real NRN BC road graph for facilities with a snapped road path (118 facilities) and keeps the parsed FFCM TL graph as a flagged fallback for 11 facilities without a real path.
- Real NRN road paths: 118 facilities (196 grade links).
- FFCM TL fallback: 11 facilities (14 grade links); first 20: BC-BIO-4007, BC-SAW-1031, BC-SAW-1707, BC-SAW-1714, BC-SAW-1725, BC-SAW-1732, BC-SAW-2013, BC-SAW-551, BC-SAW-708, BC-SAW-711, BC-SAW-730.

## 1. Scope and Stage A/B split

Stage A consumes the TSA24 assortment matrix, parsed FFCM BC facility lines,
the real NRN BC road graph plus flagged FFCM TL fallback, and diagnostic
contracts, then solves a
profit-maximising transportation/allocation LP. It emits facility assignment,
utilization, contract, unassigned-supply, objective, and validation tables.
Stage B (`fresh_fibre.graph` / `fresh_fibre.lp`) consumes the Stage B
`supply_offer`, `technology`, and `transport_link` subset written alongside this
report; Stage A does not invent Stage B demand or market rows.

- Scenario: `tsa24_bc_stage_a_pilot_ws4_quota`
- Period: `2026`
- Supply offers: 53
- Facilities: 161 screened; 129 with a transport link
- Transport links: 210
- Contracts: 161 (`contract_source=diagnostic_absent`)
- Total supply: 95,364,339 m3 green
- Solver: PULP_CBC_CMD 2.9.0 (Optimal)

## 2. BC facilities (coordinate coverage, sources, missing)

One row per BC facility is written to `facilities_bc.csv`. Coordinates are
resolved from the recovered Mills DB 2015 crosswalk (`mills_db_2015`), then an
FFCM TL/water hub anchor, then `missing`.  Exact facility codes are only a
candidate: the 2015 and 2018 code systems collide, so every code match must be
corroborated by name, city, or coordinate evidence.  The hub anchor is the
median coordinate of geocoded facilities directly attached to the same
TL/water node; it is a low-confidence proxy, not a Euclidean guess.

| coord_source | All BC facilities | Stage A scope | Expected confidence |
| --- | --- | --- | --- |
| mills_db_2015 | 98 | 88 | high/medium |
| suppliers_dbf | 0 | 0 | high |
| tl_anchor_proxy | 65 | 58 | low |
| missing | 16 | 15 | missing |

15 Stage A facilities have no coordinate; 16 of all BC facilities are missing. Missing coordinates are not replaced with Euclidean guesses.

Mills DB 2015 recovery method (code matches are corroborated; collisions rejected):

| Match method | Facilities |
| --- | --- |
| company_city_class | 47 |
| coordinate_corroborated | 5 |
| coordinate_named | 1 |
| mill_name_class | 45 |

Recovery confidence:

| Match confidence | Facilities |
| --- | --- |
| high | 55 |
| low | 1 |
| medium | 42 |

Missing Stage A coordinates: `BC-SAW-1735`, `BC-SAW-163`, `BC-SAW-308`, `BC-SAW-609`, `BC-SAW-935`, `BC-SAW-992`, `BC-SAW-994`, `BC-SAW-1022`, `BC-SAW-1472`, `BC-SAW-1698`, `BC-SAW-1700`, `BC-SAW-1705`, `BC-SAW-1710`, `BC-SAW-1728`, `BC-SAW-1730`

TL/water hub proxies used by `coord_source=tl_anchor_proxy`:

| Hub | Lat | Lon | Geocoded anchors | Anchor facilities |
| --- | --- | --- | --- | --- |
| TL12 | 49.2000 | -122.8600 | 13 | BC-PLY-1404;BC-SAW-1031;BC-SAW-1064;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| TL13 | 51.6150 | -120.7980 | 52 | BC-BIO-4007;BC-BIO-4008;BC-BIO-4009;BC-BIO-4010;BC-BIO-4011;BC-BIO-4018;BC-BIO-4024;BC-OSB-2;BC-PAP-179;BC-PAP-511;BC-PAP-679;BC-PEL-1650;BC-PEL-1652;BC-PEL-1655;BC-PEL-1657;BC-PEL-1659;BC-PLY-1013;BC-PLY-1434;BC-PLY-1693;BC-PLY-410;BC-PLY-44;BC-PLY-473;BC-PLY-514;BC-SAW-1011;BC-SAW-1014;BC-SAW-1021;BC-SAW-1253;BC-SAW-131;BC-SAW-1316;BC-SAW-132;BC-SAW-1335;BC-SAW-1377;BC-SAW-1386;BC-SAW-1389;BC-SAW-1394;BC-SAW-1437;BC-SAW-167;BC-SAW-1740;BC-SAW-178;BC-SAW-352;BC-SAW-397;BC-SAW-418;BC-SAW-5;BC-SAW-506;BC-SAW-611;BC-SAW-66;BC-SAW-680;BC-SAW-682;BC-SAW-74;BC-SAW-979;BC-SAW-981;BC-SAW-987 |
| TL14 | 50.2300 | -119.6600 | 23 | BC-BIO-4007;BC-BIO-4009;BC-BIO-4024;BC-PAP-179;BC-PAP-511;BC-PEL-1652;BC-PEL-1659;BC-PLY-1693;BC-PLY-44;BC-PLY-473;BC-PLY-514;BC-SAW-1064;BC-SAW-1316;BC-SAW-1335;BC-SAW-1377;BC-SAW-1389;BC-SAW-1394;BC-SAW-167;BC-SAW-178;BC-SAW-418;BC-SAW-66;BC-SAW-718;BC-SAW-987 |
| TL15 | 49.1750 | -122.4300 | 2 | BC-SAW-1064;BC-SAW-718 |
| TL17 | 49.2100 | -122.8000 | 14 | BC-PLY-1404;BC-PLY-473;BC-SAW-1031;BC-SAW-1064;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-66;BC-SAW-697;BC-SAW-904 |
| TL19 | 54.2300 | -124.3300 | 15 | BC-BIO-4015;BC-BIO-4023;BC-PEL-1141;BC-PEL-1653;BC-PEL-1654;BC-PEL-1658;BC-SAW-1171;BC-SAW-1383;BC-SAW-1387;BC-SAW-1740;BC-SAW-275;BC-SAW-379;BC-SAW-381;BC-SAW-389;BC-SAW-488 |
| TL20 | 54.0100 | -122.7300 | 46 | BC-BIO-4010;BC-BIO-4011;BC-BIO-4015;BC-BIO-4018;BC-BIO-4022;BC-BIO-4023;BC-OSB-2;BC-OSB-382;BC-PAP-1319;BC-PAP-679;BC-PEL-1141;BC-PEL-1650;BC-PEL-1653;BC-PEL-1654;BC-PEL-1655;BC-PEL-1657;BC-PEL-1658;BC-PLY-1013;BC-PLY-1434;BC-SAW-1011;BC-SAW-1171;BC-SAW-1253;BC-SAW-131;BC-SAW-132;BC-SAW-1377;BC-SAW-1383;BC-SAW-1386;BC-SAW-1387;BC-SAW-1437;BC-SAW-1740;BC-SAW-208;BC-SAW-210;BC-SAW-275;BC-SAW-379;BC-SAW-381;BC-SAW-383;BC-SAW-389;BC-SAW-488;BC-SAW-5;BC-SAW-506;BC-SAW-611;BC-SAW-680;BC-SAW-682;BC-SAW-74;BC-SAW-979;BC-SAW-981 |
| TL26 | 54.3500 | -124.0100 | 19 | BC-BIO-4015;BC-BIO-4022;BC-OSB-382;BC-PAP-1319;BC-PEL-1141;BC-PEL-1653;BC-PEL-1654;BC-PEL-1658;BC-SAW-1171;BC-SAW-1377;BC-SAW-1383;BC-SAW-1387;BC-SAW-1740;BC-SAW-208;BC-SAW-210;BC-SAW-275;BC-SAW-383;BC-SAW-389;BC-SAW-488 |
| TL27 | 50.6300 | -116.0900 | 7 | BC-BIO-4008;BC-PAP-1163;BC-PLY-410;BC-SAW-1014;BC-SAW-1021;BC-SAW-352;BC-SAW-397 |
| TL3 | 49.3900 | -116.9800 | 9 | BC-BIO-4008;BC-PAP-1163;BC-PAP-179;BC-PLY-410;BC-SAW-1014;BC-SAW-1335;BC-SAW-178;BC-SAW-352;BC-SAW-397 |
| W11 | 49.2050 | -122.8000 | 12 | BC-PLY-1404;BC-SAW-1064;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W12 | 49.1900 | -122.7000 | 7 | BC-SAW-1064;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W13 | 49.1850 | -122.6750 | 6 | BC-SAW-1064;BC-SAW-1287;BC-SAW-1288;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W16 | 49.2650 | -123.0900 | 4 | BC-PLY-1404;BC-SAW-114;BC-SAW-1467;BC-SAW-242 |
| W17 | 49.1900 | -122.7200 | 8 | BC-PLY-1404;BC-SAW-1064;BC-SAW-1276;BC-SAW-1287;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W18 | 49.1950 | -122.5400 | 4 | BC-SAW-1064;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W19 | 49.1800 | -122.4300 | 3 | BC-SAW-1064;BC-SAW-697;BC-SAW-718 |
| W20 | 49.1800 | -122.4300 | 3 | BC-SAW-1064;BC-SAW-697;BC-SAW-718 |
| W23 | 49.1900 | -122.7000 | 7 | BC-SAW-1064;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W25 | 49.2100 | -122.8900 | 10 | BC-PLY-1404;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-697;BC-SAW-904 |
| W27 | 49.2150 | -123.0700 | 6 | BC-PLY-1404;BC-SAW-114;BC-SAW-1276;BC-SAW-1467;BC-SAW-242;BC-SAW-281 |
| W28 | 49.2050 | -122.8000 | 12 | BC-PLY-1404;BC-SAW-1064;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W29 | 49.2050 | -122.8000 | 12 | BC-PLY-1404;BC-SAW-1064;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W3 | 49.4500 | -123.7100 | 1 | BC-SAW-1153 |
| W30 | 49.1900 | -122.7300 | 9 | BC-PLY-1404;BC-SAW-1064;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W31 | 49.1900 | -122.7300 | 9 | BC-PLY-1404;BC-SAW-1064;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W32 | 49.2100 | -122.9200 | 9 | BC-PLY-1404;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-904 |
| W33 | 49.2650 | -123.0900 | 4 | BC-PLY-1404;BC-SAW-114;BC-SAW-1467;BC-SAW-242 |
| W34 | 49.1800 | -122.7000 | 5 | BC-SAW-1064;BC-SAW-1287;BC-SAW-1288;BC-SAW-718;BC-SAW-904 |
| W4 | 49.2050 | -122.8000 | 12 | BC-PLY-1404;BC-SAW-1064;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-697;BC-SAW-718;BC-SAW-904 |
| W7 | 49.8400 | -124.5200 | 1 | BC-PAP-591 |
| W8 | 49.2100 | -122.8600 | 11 | BC-PLY-1404;BC-SAW-1064;BC-SAW-114;BC-SAW-1276;BC-SAW-1287;BC-SAW-1288;BC-SAW-1467;BC-SAW-242;BC-SAW-281;BC-SAW-697;BC-SAW-904 |

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
- Real NRN road links: 196 grade links across 118 facilities (`path_confidence=real_road_network`).
- FFCM fallback links: 14 grade links across 11 facilities (`status=linked_ffcm_fallback_no_real_road_path`).
- TSA24 anchor: `TSA24_AU23000` with
  anchor proxy `BC-SAW-506`.
  Access TL nodes:
  TL13, TL20.
- Anchor basis: `tsa24_prince_george_geocoded_mill_proxy;facility=BC-SAW-506;source=mills_db_2015;note=no_TSA24_FMU_exists_in_FFCM_graph;legacy_BC-SAW-488_was_a_code_collision_with_Canfor_Houston`.
- 210 links have `capacity=None`; `capacity_source=absent`; route capacity table=`absent`.

No accepted link uses `access_leg_plus_graph`: the anchor is attached through
parsed route edges from `BC-SAW-506`. That label is reserved for a future
non-route access leg.

| Path confidence | Facilities |
| --- | --- |
| direct_route | 5 |
| graph_shortest_path | 6 |
| real_road_network | 118 |

| Mode | Facilities |
| --- | --- |
| COMBINATION | 3 |
| ROAD | 126 |

| Distance set | Distribution (km) |
| --- | --- |
| New FFCM graph | n=129; min=14.1; p25=193.0; median=616.2; p75=857.3; max=2,277.9; mean=554.0 |
| Previous 150 km diagnostic | n=129; min=151.0; p25=175.4; median=266.9; p75=360.0; max=651.9; mean=289.9 |
| Delta new - old | n=129; min=-136.9; p25=-136.9; median=386.2; p75=681.7; max=1,791.3; mean=264.1 |
| Ratio new / old | n=129; min=0.09; p25=0.59; median=1.89; p75=4.35; max=6.00; mean=2.28 |

| Grade | New graph CAD/m3 | Previous diagnostic CAD/m3 | Delta CAD/m3 |
| --- | --- | --- | --- |
| SAWLOG | n=105; min=5.36; p25=16.13; median=39.71; p75=57.28; max=66.63; mean=37.36 | n=105; min=8.48; p25=9.82; median=14.50; p75=19.98; max=36.63; mean=15.95 | n=105; min=-3.12; p25=-3.12; median=26.28; p75=47.45; max=52.79; mean=21.41 |
| RESIDUE | n=24; min=5.45; p25=11.24; median=17.55; p75=34.06; max=44.94; mean=21.11 | n=24; min=7.33; p25=11.73; median=13.70; p75=17.96; max=26.76; mean=14.76 | n=24; min=-1.88; p25=-1.88; median=-1.88; p75=22.51; max=25.06; mean=6.36 |

Distance/cost outliers versus the previous diagnostic (top 10 by delta):

| Facility | Class | Old km | New km | Delta km | Ratio | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| BC-PAP-1163 | PAP | 486.6 | 2,277.9 | 1,791.3 | 4.68 | graph_shortest_path |
| BC-SAW-352 | SAW | 400.5 | 1,527.1 | 1,126.6 | 3.81 | direct_route |
| BC-SAW-397 | SAW | 413.9 | 1,506.0 | 1,092.1 | 3.64 | direct_route |
| BC-SAW-1736 | SAW | 437.4 | 1,252.9 | 815.5 | 2.86 | direct_route |
| BC-SAW-1014 | SAW | 422.3 | 1,231.6 | 809.3 | 2.92 | direct_route |
| BC-SAW-940 | SAW | 159.5 | 922.6 | 763.1 | 5.78 | graph_shortest_path |
| BC-SAW-1467 | SAW | 181.7 | 939.8 | 758.1 | 5.17 | graph_shortest_path |
| BC-SAW-114 | SAW | 251.2 | 1,009.3 | 758.1 | 4.02 | graph_shortest_path |
| BC-PAP-938 | PAP | 181.1 | 938.0 | 756.9 | 5.18 | graph_shortest_path |
| BC-SAW-1026 | SAW | 177.5 | 934.4 | 756.9 | 5.26 | graph_shortest_path |


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
| OTHER_LOG | other | 8 | 6,449,761 | 2,479,731 | 6,449,761 | 0 | 100.0% | 61.74-61.74 |
| PULP | pulpwood | 2 | 183,208 | 67,066 | 183,208 | 0 | 100.0% | 52.99-52.99 |
| RESIDUE | residue | 7 | 21,687,883 | 9,759,547 | 12,965,591 | 8,722,292 | 59.8% | 0.00-0.00 |
| SAWLOG | sawlog | 36 | 67,043,487 | 24,432,498 | 57,863,404 | 9,180,083 | 86.3% | 105.98-128.19 |

### 5.2 Facility utilization by class

| Class | Facilities | With link | Nameplate m3/y | Assigned m3 | Utilization | Binding | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BIO | 12 | 11 | 8,326,259 | 7,726,990 | 92.8% | 11 | 44 |
| PAP | 15 | 11 | 30,774,260 | 23,962,264 | 77.9% | 11 | 33 |
| PEL | 13 | 13 | 6,859,300 | 6,859,300 | 100.0% | 13 | 39 |
| SAW | 121 | 94 | 45,178,430 | 38,913,410 | 86.1% | 94 | 94 |

### 5.3 Capacity binding

| Facility | Class | Assigned m3 | Nameplate m3/y | Utilization |
| --- | --- | --- | --- | --- |
| BC-BIO-4007 | BIO | 646,892 | 646,892 | 100.0% |
| BC-BIO-4008 | BIO | 15,875 | 15,875 | 100.0% |
| BC-BIO-4009 | BIO | 43,655 | 43,655 | 100.0% |
| BC-BIO-4010 | BIO | 829,451 | 829,451 | 100.0% |
| BC-BIO-4011 | BIO | 2,162,923 | 2,162,923 | 100.0% |
| BC-BIO-4015 | BIO | 380,992 | 380,992 | 100.0% |
| BC-BIO-4016 | BIO | 289,713 | 289,713 | 100.0% |
| BC-BIO-4018 | BIO | 682,610 | 682,610 | 100.0% |
| BC-BIO-4022 | BIO | 380,992 | 380,992 | 100.0% |
| BC-BIO-4023 | BIO | 1,146,944 | 1,146,944 | 100.0% |

### 5.4 Largest assignments

| Facility | Class | Assigned m3 | Nameplate m3/y | Utilization |
| --- | --- | --- | --- | --- |
| BC-PAP-511 | PAP | 3,498,280 | 3,498,280 | 100.0% |
| BC-PAP-963 | PAP | 3,436,332 | 3,436,332 | 100.0% |
| BC-PAP-957 | PAP | 3,228,260 | 3,228,260 | 100.0% |
| BC-PAP-179 | PAP | 3,168,385 | 3,168,386 | 100.0% |
| BC-PAP-938 | PAP | 2,465,880 | 2,465,880 | 100.0% |
| BC-BIO-4011 | BIO | 2,162,923 | 2,162,923 | 100.0% |
| BC-PAP-1007 | PAP | 1,862,947 | 1,862,947 | 100.0% |
| BC-SAW-1387 | SAW | 1,822,248 | 1,822,248 | 100.0% |
| BC-SAW-1253 | SAW | 1,811,424 | 1,811,424 | 100.0% |
| BC-PAP-964 | PAP | 1,730,006 | 1,730,006 | 100.0% |

### 5.5 Delivered cost per m3

| Component | CAD/m3 | Notes |
| --- | --- | --- |
| product revenue | 133.02 | assigned volume weighted |
| supply (roadside proxy) | 90.14 | assigned volume weighted |
| transport (real NRN road + FFCM fallback) | 20.15 | assigned volume weighted; fallback links may include transload |
| gate | 0.00 | assigned volume weighted |
| processing | 39.91 | assigned volume weighted |
| delivered cost | 150.21 | supply + transport + gate + processing |
| net contribution | -17.18 | revenue - delivered cost |

### 5.6 Objective decomposition

| Component | Value CAD | Unit | Notes |
| --- | --- | --- | --- |
| product_revenue | 10,304,132,953.04 | CAD | assigned volume x facility product revenue |
| supply_cost | -6,982,693,802.07 | CAD | assigned volume x roadside cost proxy |
| transport_cost | -1,560,728,768.67 | CAD | assigned volume x transport cost |
| gate_cost | -0.00 | CAD | assigned volume x contract gate cost |
| processing_cost | -3,091,844,777.69 | CAD | assigned volume x line processing cost |
| unassigned_penalty | -17,902,374,720.00 | CAD | unassigned volume x diagnostic penalty |
| net_objective | -19,233,509,115.39 | CAD | solver objective -19233509115.389965 |

### 5.7 Class mix versus FFCM BC subset and previous pilot

| Class | Pilot assigned m3 | Pilot share | Previous pilot share | FFCM BC nameplate share | FFCM BC facility-count share |
| --- | --- | --- | --- | --- | --- |
| SAW | 38,913,410 | 50.2% | 51.1% | 49.6% | 75.2% |
| PAP | 23,962,264 | 30.9% | 30.4% | 33.8% | 9.3% |
| PEL | 6,859,300 | 8.9% | 8.7% | 7.5% | 8.1% |
| BIO | 7,726,990 | 10.0% | 9.8% | 9.1% | 7.5% |

FFCM BC nameplate/facility shares come from the 161 in-scope BC SAW/PAP/PEL/BIO facilities in `facilities.csv`. The directional FFCM `fmu -> facility` variable-family shares are SAW 85.8%, PAP 4.1%, PEL 7.0%, BIO 3.0%; that comparison is secondary and not a calibration target.

## 6. Contracts and capacity gaps

161 of 161 diagnostic contracts satisfy both bounds.
Contract sources in this run: `diagnostic_absent`.
The BC Fibre Database diagnostic table contributes real TSA-level 2018
apportionment volumes (no facility identifier) and dimensionless residue
allocation shares (no volume).  It does **not** contribute a facility-level
contract volume, so Stage A keeps `min=0`, `max=nameplate` and
`contract_source=diagnostic_absent` for every facility.  These are diagnostic
and project-legacy bounds, not real supply agreements.  Transport links carry
`capacity=None` and `capacity_source=absent`; route and transload capacities
are not present in the parsed tables. These are data gaps, not modelled
constraints.

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
| scope | TSA24/BC Stage A pilot supply area is a diagnostic scale, not a TSA supply estimate. | 306047.3 | ha | diagnostic |
| supply | Assortment matrix rows are per-hectare values; the pilot multiplies by the diagnostic area. | 311.6 | m3/ha | derived_tsa24_assortment_matrix |
| supply | Roadside cost is the assortment matrix price_cad_m3 proxy, not a harvest/stumpage cost. |  | CAD/m3 | derived_tsa24_assortment_matrix |
| residue | Residue volume uses the ledger 0.45 ODT/m3 basic density and 0.45 wet-basis moisture. | 0.45 | ODT/m3 | tsa24_residue_ledger_assumption |
| facility_capacity | m3/y infeed is used directly; odt/y and bdmt/y infeed use the declared 0.45 ODT/m3 density; admt/y is rejected without a declared air-dry moisture; mbf/y is rejected without a declared recovery factor; energy units cannot become volume. | 2.2222222222222223 | m3/ODT | units.py;archive_parsed_processing_lines;ledger_density |
| facility_capacity | Facility nameplate is the sum of the maximum normalized capacity per primary product; feedstock alternatives are not additive. |  | m3/y | archive_parsed_processing_lines |
| coordinate | Coordinates use a corroborated Mills DB 2015 crosswalk, then an FFCM TL/water hub proxy, then missing; exact codes alone are not trusted because the 2015 and 2018 code systems collide. | mills_db_2015=98;suppliers_dbf=0;tl_anchor_proxy=65;missing=16 | facility_count | facilities_bc_recovered.csv;bc_facility_match_conflicts.csv;routes.csv |
| coordinate | Stage A scope coordinate coverage is tracked separately from all BC facilities. | mills_db_2015=88;suppliers_dbf=0;tl_anchor_proxy=58;missing=15 | facility_count | facilities_bc_recovered.csv;routes.csv |
| transport | The TSA24 supply anchor is a geocoded Prince George mill proxy because no TSA24 FMU exists in the FFCM graph. | BC-SAW-506 | facility_id | facility_geocoding.csv;routes.csv |
| transport | Distances are FFCM route-graph shortest paths from the anchor through TL nodes, not Euclidean distances. | 616.1618973962001 | km | archive_parsed_routes |
| transport | Road and rail costs use BC transporters with archive fuel and operating rates and material capacities; transload costs are added at each TL node. |  | CAD/m3 | archive_parsed_transporters;transporter_materials;transload_costs |
| transport | FFCM route capacity is absent from the parsed route table; every transport link is uncapped. |  | m3 | diagnostic |
| contracts | Contracts are diagnostic: min=0 and max=facility nameplate. The BC Fibre Database contributes TSA apportionment volumes without facility IDs and residue shares without volumes, so no facility-level contract volume is inferred. |  | m3 | diagnostic_absent;bc_fibre_db_2018_diagnostic |
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
- Extend real-road coverage beyond the NRN BC 2018 layer and 5 km facility snap
  tolerance; facilities without a real path still use flagged FFCM TL fallback.
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
