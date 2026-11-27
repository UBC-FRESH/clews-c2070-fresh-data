# WS4 tiled 30-m dataset — P8|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P8|NT|S22` (parent `P8|NT`)
- Tile / row / col: `P8` / 2 / 2
- Province: `NT`
- Centroid: 64.186022, -122.034928
- Allocated harvest: 81.527466 m3
- Productive subcell area: 142920.379368 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1432481
- Blocks: 560190
- Forest area: 128923.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34159
- Scheduled area: 6292.44 ha
- Eligible blocks (age class >= 40): 341587
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.88 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 18.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
