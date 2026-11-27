# WS4 tiled 30-m dataset — D16|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|ON|S23` (parent `D16|ON`)
- Tile / row / col: `D16` / 2 / 3
- Province: `ON`
- Centroid: 50.116730, -94.805263
- Allocated harvest: 37654.175362 m3
- Productive subcell area: 182407.860351 ha
- Committed geometry area: 245657.309354 ha
- Clipped inventory geometry: 245657.309354 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1745464
- Blocks: 783205
- Forest area: 157091.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72067
- Scheduled area: 13665.60 ha
- Eligible blocks (age class >= 40): 720664
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.42 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 24.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
