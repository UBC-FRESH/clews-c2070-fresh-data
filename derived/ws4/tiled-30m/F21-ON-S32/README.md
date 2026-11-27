# WS4 tiled 30-m dataset — F21|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F21|ON|S32` (parent `F21|ON`)
- Tile / row / col: `F21` / 3 / 2
- Province: `ON`
- Centroid: 52.738380, -84.239084
- Allocated harvest: 9105.239574 m3
- Productive subcell area: 122428.732512 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1041111
- Blocks: 403733
- Forest area: 93699.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36494
- Scheduled area: 8560.71 ha
- Eligible blocks (age class >= 40): 364939
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.26 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 13.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
