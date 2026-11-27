# WS4 tiled 30-m dataset — L12|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|NT|S11` (parent `L12|NT`)
- Tile / row / col: `L12` / 1 / 1
- Province: `NT`
- Centroid: 60.117063, -107.747309
- Allocated harvest: 30.740198 m3
- Productive subcell area: 68656.724948 ha
- Committed geometry area: 127166.154885 ha
- Clipped inventory geometry: 127166.154885 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 973167
- Blocks: 252043
- Forest area: 87585.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18140
- Scheduled area: 5329.71 ha
- Eligible blocks (age class >= 40): 181393
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.36 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 10.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
