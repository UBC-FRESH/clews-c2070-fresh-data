# WS4 tiled 30-m dataset — N4|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N4|YT|S33` (parent `N4|YT`)
- Tile / row / col: `N4` / 3 / 3
- Province: `YT`
- Centroid: 60.029583, -129.240399
- Allocated harvest: 24.025198 m3
- Productive subcell area: 8889.833171 ha
- Committed geometry area: 10277.429584 ha
- Clipped inventory geometry: 10277.429584 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 108477
- Blocks: 63497
- Forest area: 9762.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6305
- Scheduled area: 940.59 ha
- Eligible blocks (age class >= 40): 63044
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.19 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 2.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
