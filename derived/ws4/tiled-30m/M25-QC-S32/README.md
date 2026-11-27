# WS4 tiled 30-m dataset — M25|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M25|QC|S32` (parent `M25|QC`)
- Tile / row / col: `M25` / 3 / 2
- Province: `QC`
- Centroid: 60.523078, -69.936886
- Allocated harvest: 3.077949 m3
- Productive subcell area: 24.050354 ha
- Committed geometry area: 130369.540046 ha
- Clipped inventory geometry: 130369.540046 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 275
- Blocks: 256
- Forest area: 24.75 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3
- Scheduled area: 0.27 ha
- Eligible blocks (age class >= 40): 3
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
