# WS4 tiled 30-m dataset — P5|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P5|NT|S13` (parent `P5|NT`)
- Tile / row / col: `P5` / 1 / 3
- Province: `NT`
- Centroid: 62.180065, -128.715462
- Allocated harvest: 23.346076 m3
- Productive subcell area: 39526.219041 ha
- Committed geometry area: 106034.398120 ha
- Clipped inventory geometry: 106034.398120 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 399036
- Blocks: 197377
- Forest area: 35913.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14478
- Scheduled area: 2654.73 ha
- Eligible blocks (age class >= 40): 144773
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.29 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 6.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
