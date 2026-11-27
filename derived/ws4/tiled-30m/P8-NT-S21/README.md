# WS4 tiled 30-m dataset — P8|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P8|NT|S21` (parent `P8|NT`)
- Tile / row / col: `P8` / 2 / 1
- Province: `NT`
- Centroid: 63.992067, -122.994929
- Allocated harvest: 81.527466 m3
- Productive subcell area: 142920.379368 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2001564
- Blocks: 642436
- Forest area: 180140.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49383
- Scheduled area: 11371.86 ha
- Eligible blocks (age class >= 40): 493824
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.62 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 23.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
