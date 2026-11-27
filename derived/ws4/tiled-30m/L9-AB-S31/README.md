# WS4 tiled 30-m dataset — L9|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|AB|S31` (parent `L9|AB`)
- Tile / row / col: `L9` / 3 / 1
- Province: `AB`
- Centroid: 59.783181, -116.211142
- Allocated harvest: 91653.235165 m3
- Productive subcell area: 183500.061415 ha
- Committed geometry area: 233748.953373 ha
- Clipped inventory geometry: 233748.953373 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1962466
- Blocks: 598671
- Forest area: 176621.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52441
- Scheduled area: 11722.41 ha
- Eligible blocks (age class >= 40): 524404
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.40 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 22.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
