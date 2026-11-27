# WS4 tiled 30-m dataset — P6|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P6|NT|S11` (parent `P6|NT`)
- Tile / row / col: `P6` / 1 / 1
- Province: `NT`
- Centroid: 62.300424, -127.969775
- Allocated harvest: 28.727976 m3
- Productive subcell area: 57516.706047 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 922125
- Blocks: 411702
- Forest area: 82991.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34747
- Scheduled area: 6862.41 ha
- Eligible blocks (age class >= 40): 347463
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.47 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 12.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
