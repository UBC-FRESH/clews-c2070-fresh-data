# WS4 tiled 30-m dataset — S4|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S4|YT|S33` (parent `S4|YT`)
- Tile / row / col: `S4` / 3 / 3
- Province: `YT`
- Centroid: 65.479448, -137.943545
- Allocated harvest: 112.993599 m3
- Productive subcell area: 94174.546119 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1428655
- Blocks: 625337
- Forest area: 128578.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43865
- Scheduled area: 7945.20 ha
- Eligible blocks (age class >= 40): 438645
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.11 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 19.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
