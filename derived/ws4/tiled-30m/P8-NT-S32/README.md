# WS4 tiled 30-m dataset — P8|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P8|NT|S32` (parent `P8|NT`)
- Tile / row / col: `P8` / 3 / 2
- Province: `NT`
- Centroid: 64.606821, -122.479218
- Allocated harvest: 81.527466 m3
- Productive subcell area: 142920.379368 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1400486
- Blocks: 662948
- Forest area: 126043.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53739
- Scheduled area: 10238.31 ha
- Eligible blocks (age class >= 40): 537383
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.54 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 20.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
