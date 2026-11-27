# WS4 tiled 30-m dataset — P6|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P6|NT|S23` (parent `P6|NT`)
- Tile / row / col: `P6` / 2 / 3
- Province: `NT`
- Centroid: 63.154849, -126.699224
- Allocated harvest: 28.727976 m3
- Productive subcell area: 57516.706047 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 775601
- Blocks: 357570
- Forest area: 69804.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26135
- Scheduled area: 5075.73 ha
- Eligible blocks (age class >= 40): 261343
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.91 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 11.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
