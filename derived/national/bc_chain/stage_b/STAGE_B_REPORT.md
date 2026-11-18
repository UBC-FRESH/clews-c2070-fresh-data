# Stage B sawmill-residue and bioenergy allocation pilot (TSA24/BC)

## Scope and status

This is a diagnostic Stage B pilot for the TSA24/BC Stage A run
`stage_a_run`.  It uses the Stage A sawmill log assignments, FFCM
processing-line outfeed ratios, the real NRN BC road graph, and FFCM commodity
prices.  It is not a mill-level fibre supply estimate and it does not claim that
proxy-located sawmills are at their proxy coordinates.

- Period: `2028`
- Stage A run: `stage_a_run`
- Sawmill sources: **51** (51 corroborated, 0 TL-hub proxy, 0 missing)
- Solver status: **Optimal**
- Validation: **PASS**
- Objective mode: `profit_max` (all included recipient classes have FFCM prices)
- Residue generated: **6826610.313 ODT** (15170245.140 m3 green equivalent)
- Residue assigned: **6145980.960 ODT**
- Residue unassigned: **680629.353 ODT**
- Bioenergy (BIO) share of generated residue: **10.18%**
- Bioenergy share of assigned residue: **11.30%**
- Electricity from allocated hogfuel: **514488.647 MWh**
- Capacity-binding recipient facilities: **14 of 24**

## Residue supply (Stage A sawmill log volume x FFCM outfeed ratio)

Every ratio is `outfeed rate / infeed rate` from `processing_line_flows.csv`.
The declared outfeed is oven-dry, so ODT is the primary quantity.  Green m3 is
`ODT / 0.45` from the Stage A residue-ledger basic density.  The conversion is
recorded line by line in `residue_conversions.csv`.

| type | generated ODT | generated m3 | assigned ODT | unassigned ODT | assigned share | unassigned reasons |
|---|---|---|---|---|---|---|
| chips | 4181690.850 | 9292646.334 | 4050914.468 | 130776.382 | 96.87% | capacity_exhausted |
| sawdust/shavings | 1433623.013 | 3185828.918 | 1400446.975 | 33176.038 | 97.69% | capacity_exhausted |
| hogfuel/bark | 710678.360 | 1579285.244 | 694619.517 | 16058.843 | 97.74% | capacity_exhausted |
| other (internally used woodfuel) | 500618.090 | 1112484.644 | 0.000 | 500618.090 | 0.00% | no_consumer_class |
| all residue | 6826610.313 | 15170245.140 | 6145980.960 | 680629.353 | 90.03% |  |

### Sawmill outfeed ratio coverage

| type | sources screened | sources with ratio | sources excluded | min ratio | max ratio |
|---|---|---|---|---|---|
| chips | 51 | 51 | 0 | 0.158990938 | 0.158990938 |
| sawdust/shavings | 51 | 51 | 0 | 0.054507393 | 0.054507393 |
| hogfuel/bark | 51 | 51 | 0 | 0.027020510 | 0.027020510 |
| other (internally used woodfuel) | 51 | 51 | 0 | 0.019033865 | 0.019033865 |

Missing ratios are excluded and listed in `residue_supply_coverage.csv`; no
ratio was replaced by an assumption.  The full `204` source/type
rows are in `residue_supply_coverage.csv`; `204` supply rows are in
`residue_supply.csv`.  `residue_balance.csv` reports unassigned ODT as the
exact supply residual, so every row closes; `unassigned_residue.csv` lists the
material leftovers with reasons.  Sub-`1e-7` solver-tolerance residuals are
folded into the balance residual rather than given a false reason.
`internally_used_woodfuel` is reported as `other` and is not allocatable in this
pilot.

## Recipients (PAP/PEL/BIO)

Only BC facilities with a corroborated Mills DB coordinate and a real (or
explicitly flagged FFCM road-fallback) path are included.  Recipient capacity is
the FFCM line `infeed_rate` normalised to ODT; no capacity was added or scaled.
Products and prices come from `commodities.csv`; `markets.csv` defines feedstock
markets only and carries no product price.  A missing price would put the run in
cost-min mode; the `price_status` column records availability.

| facility | class | line | accepts | capacity ODT/y | processing CAD/ODT-in | product | price | price status |
|---|---|---|---|---|---|---|---|---|
| BC-BIO-4007 | BIO | BC-BIO-4007-1 | hogfuel | 258757.0 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4008 | BIO | BC-BIO-4008-1 | hogfuel | 6349.8 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4009 | BIO | BC-BIO-4009-1 | hogfuel | 17462.1 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4010 | BIO | BC-BIO-4010-1 | hogfuel | 331780.4 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4011 | BIO | BC-BIO-4011-1 | hogfuel | 865169.0 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4015 | BIO | BC-BIO-4015-1 | hogfuel | 152396.7 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4018 | BIO | BC-BIO-4018-1 | hogfuel | 273044.1 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4022 | BIO | BC-BIO-4022-1 | hogfuel | 152396.7 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4023 | BIO | BC-BIO-4023-1 | hogfuel | 458777.6 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-BIO-4024 | BIO | BC-BIO-4024-1 | hogfuel | 458777.6 | 20.89 | electricity_bc | 100.00 $/mwh | available |
| BC-PAP-1163 | PAP | BC-PAP-1163-1 | chips | 567102.7 | 138.87 | kraft_softwood | 808.68 $/t | available |
| BC-PAP-1319 | PAP | BC-PAP-1319-1 | chips | 276704.7 | 283.43 | refiner_softwood | 469.31 $/t | available |
| BC-PAP-179 | PAP | BC-PAP-179-1 | chips | 1267354.2 | 123.33 | kraft_softwood | 808.68 $/t | available |
| BC-PAP-511 | PAP | BC-PAP-511-1 | chips | 1399311.8 | 50.55 | kraft_softwood | 808.68 $/t | available |
| BC-PAP-679 | PAP | BC-PAP-679-1 | chips | 540441.1 | 132.68 | kraft_softwood | 808.68 $/t | available |
| BC-PEL-1141 | PEL | BC-PEL-1141-1 | sawdust_shavings | 34440.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1650 | PEL | BC-PEL-1650-1 | sawdust_shavings | 401800.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1652 | PEL | BC-PEL-1652-1 | sawdust_shavings | 83804.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1653 | PEL | BC-PEL-1653-1 | sawdust_shavings | 502824.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1654 | PEL | BC-PEL-1654-1 | sawdust_shavings | 251412.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1655 | PEL | BC-PEL-1655-1 | sawdust_shavings | 265188.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1657 | PEL | BC-PEL-1657-1 | sawdust_shavings | 251412.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1658 | PEL | BC-PEL-1658-1 | sawdust_shavings | 229600.0 | 41.92 | pellet | 151.10 $/t | available |
| BC-PEL-1659 | PEL | BC-PEL-1659-1 | sawdust_shavings | 137760.0 | 41.92 | pellet | 151.10 $/t | available |

41 recipient candidates were screened; excluded rows and reasons are
in `stage_b_recipient_screen.csv`.  Stage A's own residue-consuming facilities
without corroborated coordinates are excluded here; their Stage A volumes still
appear in the Stage A tables.

## Transport

All links use the NRN BC 2018 road graph (EPSG:3005 shortest path) and the
Stage A `BC_residue_truck` rate (fuel + operating/speed).  There is no transload
for direct road.  Proxy-located sources share low-confidence TL-hub nodes, so
their NRN source-to-recipient distances are identical; source-level allocation
is degenerate for those links.  FFCM fallback links use the facility route
attachments and can differ by source.  3
source-recipient pairs share a road node (0 km) and are flagged
`zero_distance_shared_road_node` in the link evidence.

| path confidence | links | min km | median km | max km |
|---|---|---|---|---|
| ffcm_route_fallback_road | 51 | 29.50 | 448.13 | 1035.96 |
| real_road_network | 1173 | 0.00 | 539.17 | 1527.23 |

Largest source-recipient pairs by assigned ODT (first 15 of 161):

| source | recipient | assigned ODT | distance km | cost CAD/m3 | path confidence |
|---|---|---|---|---|---|
| BC-SAW-1387 | BC-PAP-511 | 289720.9 | 636.02 | 29.659 | real_road_network |
| BC-SAW-506 | BC-PAP-511 | 215170.9 | 530.33 | 24.730 | real_road_network |
| BC-SAW-389 | BC-PAP-511 | 190909.1 | 663.19 | 30.925 | real_road_network |
| BC-SAW-680 | BC-PAP-679 | 171750.5 | 9.29 | 0.433 | real_road_network |
| BC-SAW-383 | BC-PAP-1319 | 164544.5 | 12.06 | 0.563 | real_road_network |
| BC-SAW-611 | BC-PAP-511 | 144000.0 | 288.85 | 13.469 | real_road_network |
| BC-SAW-488 | BC-PAP-179 | 132709.3 | 1261.59 | 58.830 | real_road_network |
| BC-SAW-74 | BC-PAP-511 | 131354.0 | 594.18 | 27.708 | real_road_network |
| BC-SAW-1383 | BC-PAP-1163 | 130909.1 | 1103.06 | 51.437 | real_road_network |
| BC-SAW-1394 | BC-PAP-179 | 126196.4 | 352.97 | 16.459 | real_road_network |
| BC-SAW-210 | BC-PAP-679 | 119867.4 | 178.36 | 8.317 | real_road_network |
| BC-SAW-132 | BC-PAP-1163 | 113454.5 | 778.65 | 36.310 | real_road_network |
| BC-SAW-5 | BC-PAP-511 | 112296.6 | 200.61 | 9.355 | real_road_network |
| BC-SAW-208 | BC-PAP-1319 | 112160.1 | 123.27 | 5.748 | real_road_network |
| BC-SAW-178 | BC-PAP-179 | 110487.3 | 7.34 | 0.342 | real_road_network |

Full link evidence, snap distances, and components are in
`stage_b_transport_links.csv`.

## Stage B results

| facility | class | capacity ODT/y | received ODT | utilization | capacity binding |
|---|---|---|---|---|---|
| BC-BIO-4007 | BIO | 258757.0 | 64245.0 | 24.83% | no |
| BC-BIO-4008 | BIO | 6349.8 | 6349.8 | 100.00% | yes |
| BC-BIO-4009 | BIO | 17462.1 | 17462.1 | 100.00% | yes |
| BC-BIO-4010 | BIO | 331780.4 | 69774.8 | 21.03% | no |
| BC-BIO-4011 | BIO | 865169.0 | 72109.2 | 8.33% | no |
| BC-BIO-4015 | BIO | 152396.7 | 152396.7 | 100.00% | yes |
| BC-BIO-4018 | BIO | 273044.1 | 79548.9 | 29.13% | no |
| BC-BIO-4022 | BIO | 152396.7 | 79853.8 | 52.40% | no |
| BC-BIO-4023 | BIO | 458777.6 | 61098.8 | 13.32% | no |
| BC-BIO-4024 | BIO | 458777.6 | 91780.4 | 20.01% | no |
| BC-PAP-1163 | PAP | 567102.7 | 567102.7 | 100.00% | yes |
| BC-PAP-1319 | PAP | 276704.7 | 276704.7 | 100.00% | yes |
| BC-PAP-179 | PAP | 1267354.2 | 1267354.2 | 100.00% | yes |
| BC-PAP-511 | PAP | 1399311.8 | 1399311.8 | 100.00% | yes |
| BC-PAP-679 | PAP | 540441.1 | 540441.1 | 100.00% | yes |
| BC-PEL-1141 | PEL | 34440.0 | 34440.0 | 100.00% | yes |
| BC-PEL-1650 | PEL | 401800.0 | 401800.0 | 100.00% | yes |
| BC-PEL-1652 | PEL | 83804.0 | 83804.0 | 100.00% | yes |
| BC-PEL-1653 | PEL | 502824.0 | 76304.3 | 15.18% | no |
| BC-PEL-1654 | PEL | 251412.0 | 90331.7 | 35.93% | no |
| BC-PEL-1655 | PEL | 265188.0 | 94995.0 | 35.82% | no |
| BC-PEL-1657 | PEL | 251412.0 | 251412.0 | 100.00% | yes |
| BC-PEL-1658 | PEL | 229600.0 | 229600.0 | 100.00% | yes |
| BC-PEL-1659 | PEL | 137760.0 | 137760.0 | 100.00% | yes |

### Objective decomposition (CAD)

| component | value CAD | CAD per assigned ODT | sense |
|---|---|---|---|
| product_revenue | 1463766688.82 | 238.17 | positive |
| transport_cost | 231717691.67 | 37.70 | negative |
| processing_cost | 529148816.43 | 86.10 | negative |
| net_contribution | 702900180.72 | 114.37 | objective_profit_max |
| solver_objective | 702900180.72 | 114.37 | profit_max |

Reported objective: **CAD 702,900,180.72**
(`profit_max`); normalized objective: CAD
702,900,180.72; raw CBC objective: CAD
702,900,184.42.
The assignment-level components reproduce the normalized value; the raw CBC
delta is caused by the solver-tolerance allocation normalization and is
reported in `validation_summary.json`.

## Validation

| check | passed | detail |
|---|---|---|
| solver_status | yes | status=Optimal |
| residue_balance | yes | assigned + unassigned equals generated residue for every source/type |
| allocation_reference_integrity | yes | all allocations reference a declared supply row and recipient line |
| residue_type_eligibility | yes | every allocation uses an eligible residue type and recipient class |
| recipient_capacity | yes | no recipient line exceeds its FFCM infeed capacity |
| transport_link_existence | yes | every allocation has a finite, cost-consistent road or fallback link |
| unit_consistency | yes | volume/ODT, capacity, moisture, and mass-price bases reconcile |
| objective_reconciliation | yes | assignment components reproduce the normalised objective; raw CBC delta 3.695755 CAD |
| finite_nonnegative_values | yes | all allocation and slack values are finite and non-negative |

## Data gaps and next steps

- 0 of 51 Stage A sawmills
  carry `tl_anchor_proxy` coordinates.  NRN haul distances from those sources
  are identical within a proxy node and are the largest transport limitation.
- Residue-consuming facilities without corroborated coordinates are excluded
  as recipients.  Their Stage A primary-feedstock volumes are unchanged.
- FFCM sawmill outfeed ratios are applied as constant returns to the Stage A
  log volume; the FFCM base case is not a closed mill mass balance.
- `internally_used_woodfuel` is reported but not allocated; no consumer class
  is declared for it in this pilot.
- Road-only transport is modelled.  Island recipients without a road path are
  reported as unlinked; no water or rail residue route is assumed.
- FFCM commodity prices are used as product-price proxies; they may represent
  delivered market prices rather than mill-gate realizations.
- Next: corroborate SAW coordinates, add residue-specific density/moisture, and
  add water/rail residue options for disconnected coastal recipients.
