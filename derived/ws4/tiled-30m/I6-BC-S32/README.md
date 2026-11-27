# WS4 tiled 30-m dataset — I6|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|BC|S32` (parent `I6|BC`)
- Tile / row / col: `I6` / 3 / 2
- Province: `BC`
- Centroid: 54.618340, -120.121560
- Allocated harvest: 33670.836494 m3
- Productive subcell area: 53698.864942 ha
- Committed geometry area: 70843.624246 ha
- Clipped inventory geometry: 70843.624246 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 772570
- Blocks: 326705
- Forest area: 69531.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30960
- Scheduled area: 5629.32 ha
- Eligible blocks (age class >= 40): 309593
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.50 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 10.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
