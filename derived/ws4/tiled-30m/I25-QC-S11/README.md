# WS4 tiled 30-m dataset — I25|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I25|QC|S11` (parent `I25|QC`)
- Tile / row / col: `I25` / 1 / 1
- Province: `QC`
- Centroid: 54.630780, -74.725466
- Allocated harvest: 15858.451832 m3
- Productive subcell area: 122379.864931 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1303108
- Blocks: 461084
- Forest area: 117279.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39140
- Scheduled area: 9722.70 ha
- Eligible blocks (age class >= 40): 391397
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.92 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 16.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
