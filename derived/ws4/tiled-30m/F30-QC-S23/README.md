# WS4 tiled 30-m dataset — F30|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|QC|S23` (parent `F30|QC`)
- Tile / row / col: `F30` / 2 / 3
- Province: `QC`
- Centroid: 48.324903, -65.523276
- Allocated harvest: 127246.717399 m3
- Productive subcell area: 236147.860088 ha
- Committed geometry area: 249991.305393 ha
- Clipped inventory geometry: 249991.305393 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2595298
- Blocks: 909075
- Forest area: 233576.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80894
- Scheduled area: 19310.13 ha
- Eligible blocks (age class >= 40): 808932
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.45 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 32.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
