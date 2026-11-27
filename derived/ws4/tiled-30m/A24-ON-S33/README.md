# WS4 tiled 30-m dataset — A24|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S33` (parent `A24|ON`)
- Tile / row / col: `A24` / 3 / 3
- Province: `ON`
- Centroid: 45.219811, -79.641803
- Allocated harvest: 31093.757282 m3
- Productive subcell area: 119454.807257 ha
- Committed geometry area: 248968.372799 ha
- Clipped inventory geometry: 248968.372799 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2103060
- Blocks: 670164
- Forest area: 189275.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62639
- Scheduled area: 19420.47 ha
- Eligible blocks (age class >= 40): 626386
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.47 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 25.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
