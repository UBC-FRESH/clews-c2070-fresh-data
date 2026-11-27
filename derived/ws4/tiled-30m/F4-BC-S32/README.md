# WS4 tiled 30-m dataset — F4|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F4|BC|S32` (parent `F4|BC`)
- Tile / row / col: `F4` / 3 / 2
- Province: `BC`
- Centroid: 49.794989, -121.320280
- Allocated harvest: 187932.035561 m3
- Productive subcell area: 186912.489401 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2517806
- Blocks: 1290025
- Forest area: 226602.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 122113
- Scheduled area: 18643.41 ha
- Eligible blocks (age class >= 40): 1221129
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 36.01 MB
- Schedules: 1.48 MB
- Runs: 0.00 MB
- Total: 37.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
