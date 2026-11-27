# WS4 tiled 30-m dataset — U6|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|NT|S22` (parent `U6|NT`)
- Tile / row / col: `U6` / 2 / 2
- Province: `NT`
- Centroid: 68.706297, -136.334346
- Allocated harvest: 7.119574 m3
- Productive subcell area: 6006.957323 ha
- Committed geometry area: 25872.622171 ha
- Clipped inventory geometry: 25872.622171 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 15959
- Blocks: 10939
- Forest area: 1436.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 626
- Scheduled area: 74.88 ha
- Eligible blocks (age class >= 40): 6255
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.39 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
