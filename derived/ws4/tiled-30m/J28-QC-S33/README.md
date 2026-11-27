# WS4 tiled 30-m dataset — J28|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|QC|S33` (parent `J28|QC`)
- Tile / row / col: `J28` / 3 / 3
- Province: `QC`
- Centroid: 54.925848, -65.218297
- Allocated harvest: 8727.073865 m3
- Productive subcell area: 61879.763128 ha
- Committed geometry area: 101666.134030 ha
- Clipped inventory geometry: 101666.134030 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 810416
- Blocks: 473546
- Forest area: 72937.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44324
- Scheduled area: 6604.56 ha
- Eligible blocks (age class >= 40): 443238
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.43 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 12.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
