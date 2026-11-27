# WS4 tiled 30-m dataset — N11|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N11|NT|S23` (parent `N11|NT`)
- Tile / row / col: `N11` / 2 / 3
- Province: `NT`
- Centroid: 63.062803, -110.152350
- Allocated harvest: 42.605610 m3
- Productive subcell area: 75817.363283 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 605407
- Blocks: 333427
- Forest area: 54486.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18699
- Scheduled area: 2783.70 ha
- Eligible blocks (age class >= 40): 186984
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.21 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 9.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
