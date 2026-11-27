# WS4 tiled 30-m dataset — N11|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N11|NT|S33` (parent `N11|NT`)
- Tile / row / col: `N11` / 3 / 3
- Province: `NT`
- Centroid: 63.512162, -110.396801
- Allocated harvest: 42.605610 m3
- Productive subcell area: 75817.363283 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 144312
- Blocks: 113280
- Forest area: 12988.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3932
- Scheduled area: 405.81 ha
- Eligible blocks (age class >= 40): 39314
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.35 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 3.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
