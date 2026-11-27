# WS4 tiled 30-m dataset — O7|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O7|NT|S11` (parent `O7|NT`)
- Tile / row / col: `O7` / 1 / 1
- Province: `NT`
- Centroid: 61.723294, -123.979116
- Allocated harvest: 178.486937 m3
- Productive subcell area: 176484.661366 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1591838
- Blocks: 636334
- Forest area: 143265.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46098
- Scheduled area: 8699.58 ha
- Eligible blocks (age class >= 40): 460971
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.41 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 20.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
