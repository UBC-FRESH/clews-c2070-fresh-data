# WS4 tiled 30-m dataset — O6|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|NT|S21` (parent `O6|NT`)
- Tile / row / col: `O6` / 2 / 1
- Province: `NT`
- Centroid: 61.531119, -126.944498
- Allocated harvest: 79.193527 m3
- Productive subcell area: 95561.696210 ha
- Committed geometry area: 194487.085276 ha
- Clipped inventory geometry: 194487.085276 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1116993
- Blocks: 382764
- Forest area: 100529.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32222
- Scheduled area: 7717.95 ha
- Eligible blocks (age class >= 40): 322220
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.26 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 13.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
