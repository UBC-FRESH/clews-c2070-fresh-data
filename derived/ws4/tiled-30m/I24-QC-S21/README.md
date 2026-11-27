# WS4 tiled 30-m dataset — I24|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I24|QC|S21` (parent `I24|QC`)
- Tile / row / col: `I24` / 2 / 1
- Province: `QC`
- Centroid: 55.477356, -76.771779
- Allocated harvest: 16833.077383 m3
- Productive subcell area: 107048.280011 ha
- Committed geometry area: 249999.994314 ha
- Clipped inventory geometry: 249999.994314 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1552008
- Blocks: 692496
- Forest area: 139680.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54559
- Scheduled area: 10912.23 ha
- Eligible blocks (age class >= 40): 545585
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.53 MB
- Schedules: 0.65 MB
- Runs: 0.00 MB
- Total: 21.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
