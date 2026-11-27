# WS4 tiled 30-m dataset — L1|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L1|BC|S12` (parent `L1|BC`)
- Tile / row / col: `L1` / 1 / 2
- Province: `BC`
- Centroid: 54.054800, -132.847310
- Allocated harvest: 52761.681280 m3
- Productive subcell area: 68638.531459 ha
- Committed geometry area: 72928.617852 ha
- Clipped inventory geometry: 72928.617852 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 780303
- Blocks: 357621
- Forest area: 70227.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35461
- Scheduled area: 6864.30 ha
- Eligible blocks (age class >= 40): 354610
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.87 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 11.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
