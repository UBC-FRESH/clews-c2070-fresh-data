# WS4 tiled 30-m dataset — P7|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P7|NT|S12` (parent `P7|NT`)
- Tile / row / col: `P7` / 1 / 2
- Province: `NT`
- Centroid: 63.172161, -124.411122
- Allocated harvest: 136.701997 m3
- Productive subcell area: 163584.010344 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2275744
- Blocks: 703518
- Forest area: 204816.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55389
- Scheduled area: 10927.89 ha
- Eligible blocks (age class >= 40): 553884
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.02 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 25.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
