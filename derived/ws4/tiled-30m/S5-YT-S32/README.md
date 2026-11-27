# WS4 tiled 30-m dataset — S5|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S5|YT|S32` (parent `S5|YT`)
- Tile / row / col: `S5` / 3 / 2
- Province: `YT`
- Centroid: 66.047357, -136.167488
- Allocated harvest: 200.402540 m3
- Productive subcell area: 134571.201402 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1547513
- Blocks: 585151
- Forest area: 139276.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43656
- Scheduled area: 10198.26 ha
- Eligible blocks (age class >= 40): 436558
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.12 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 19.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
