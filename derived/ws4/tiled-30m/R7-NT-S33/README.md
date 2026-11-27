# WS4 tiled 30-m dataset — R7|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R7|NT|S33` (parent `R7|NT`)
- Tile / row / col: `R7` / 3 / 3
- Province: `NT`
- Centroid: 66.659590, -127.527427
- Allocated harvest: 153.981434 m3
- Productive subcell area: 167855.244665 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2058196
- Blocks: 828408
- Forest area: 185237.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69406
- Scheduled area: 14953.23 ha
- Eligible blocks (age class >= 40): 694053
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.82 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 26.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
