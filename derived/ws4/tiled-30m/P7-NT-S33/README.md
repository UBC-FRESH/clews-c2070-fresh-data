# WS4 tiled 30-m dataset — P7|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P7|NT|S33` (parent `P7|NT`)
- Tile / row / col: `P7` / 3 / 3
- Province: `NT`
- Centroid: 64.206668, -124.408146
- Allocated harvest: 136.701997 m3
- Productive subcell area: 163584.010344 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2176491
- Blocks: 573749
- Forest area: 195884.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38816
- Scheduled area: 7356.60 ha
- Eligible blocks (age class >= 40): 388151
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.50 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 22.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
