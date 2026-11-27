# WS4 tiled 30-m dataset — O2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O2|BC|S23` (parent `O2|BC`)
- Tile / row / col: `O2` / 2 / 3
- Province: `BC`
- Centroid: 59.165097, -134.581708
- Allocated harvest: 859.792324 m3
- Productive subcell area: 4145.577678 ha
- Committed geometry area: 20891.915944 ha
- Clipped inventory geometry: 20891.915944 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 28
- Blocks: 21
- Forest area: 2.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 0
- Scheduled area: 0.00 ha
- Eligible blocks (age class >= 40): 0
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.06 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
