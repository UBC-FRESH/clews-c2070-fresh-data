# WS4 tiled 30-m dataset — U6|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|NT|S11` (parent `U6|NT`)
- Tile / row / col: `U6` / 1 / 1
- Province: `NT`
- Centroid: 68.043802, -136.411243
- Allocated harvest: 1.074501 m3
- Productive subcell area: 906.582393 ha
- Committed geometry area: 3904.749520 ha
- Clipped inventory geometry: 3904.749520 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 154
- Blocks: 143
- Forest area: 13.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41
- Scheduled area: 4.05 ha
- Eligible blocks (age class >= 40): 41
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
