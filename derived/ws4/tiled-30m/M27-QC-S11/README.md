# WS4 tiled 30-m dataset — M27|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S11` (parent `M27|QC`)
- Tile / row / col: `M27` / 1 / 1
- Province: `QC`
- Centroid: 58.644120, -66.210925
- Allocated harvest: 1953.080584 m3
- Productive subcell area: 10661.856765 ha
- Committed geometry area: 136622.329724 ha
- Clipped inventory geometry: 136622.329724 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 143774
- Blocks: 96407
- Forest area: 12939.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5224
- Scheduled area: 616.95 ha
- Eligible blocks (age class >= 40): 52238
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.04 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
