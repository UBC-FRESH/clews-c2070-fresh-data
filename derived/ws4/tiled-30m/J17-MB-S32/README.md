# WS4 tiled 30-m dataset — J17|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J17|MB|S32` (parent `J17|MB`)
- Tile / row / col: `J17` / 3 / 2
- Province: `MB`
- Centroid: 58.650068, -93.285439
- Allocated harvest: 99.557308 m3
- Productive subcell area: 7543.798302 ha
- Committed geometry area: 33830.825576 ha
- Clipped inventory geometry: 33830.825576 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5130
- Blocks: 2938
- Forest area: 461.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1143
- Scheduled area: 239.67 ha
- Eligible blocks (age class >= 40): 1143
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.16 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
