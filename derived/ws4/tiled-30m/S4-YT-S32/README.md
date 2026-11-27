# WS4 tiled 30-m dataset — S4|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S4|YT|S32` (parent `S4|YT`)
- Tile / row / col: `S4` / 3 / 2
- Province: `YT`
- Centroid: 65.187947, -138.802923
- Allocated harvest: 112.993599 m3
- Productive subcell area: 94174.546119 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 841371
- Blocks: 416100
- Forest area: 75723.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26439
- Scheduled area: 4254.39 ha
- Eligible blocks (age class >= 40): 264385
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.96 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 12.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
