# WS4 tiled 30-m dataset — K24|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K24|QC|S33` (parent `K24|QC`)
- Tile / row / col: `K24` / 3 / 3
- Province: `QC`
- Centroid: 58.255263, -73.364265
- Allocated harvest: 5416.048368 m3
- Productive subcell area: 47377.969135 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 68781
- Blocks: 48291
- Forest area: 6190.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 595
- Scheduled area: 71.19 ha
- Eligible blocks (age class >= 40): 5944
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.48 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
