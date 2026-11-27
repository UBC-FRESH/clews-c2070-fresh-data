# WS4 tiled 30-m dataset — H32|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H32|QC|S32` (parent `H32|QC`)
- Tile / row / col: `H32` / 3 / 2
- Province: `QC`
- Centroid: 50.241202, -60.253610
- Allocated harvest: 1128.484735 m3
- Productive subcell area: 4021.580601 ha
- Committed geometry area: 7464.936768 ha
- Clipped inventory geometry: 7464.936768 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 17036
- Blocks: 10189
- Forest area: 1533.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 778
- Scheduled area: 120.96 ha
- Eligible blocks (age class >= 40): 7779
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.40 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
