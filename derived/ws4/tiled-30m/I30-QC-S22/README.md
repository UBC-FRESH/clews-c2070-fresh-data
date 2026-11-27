# WS4 tiled 30-m dataset — I30|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|QC|S22` (parent `I30|QC`)
- Tile / row / col: `I30` / 2 / 2
- Province: `QC`
- Centroid: 51.943458, -63.193918
- Allocated harvest: 7324.247508 m3
- Productive subcell area: 32443.584640 ha
- Committed geometry area: 42382.499526 ha
- Clipped inventory geometry: 42382.499526 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 361422
- Blocks: 176567
- Forest area: 32527.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17425
- Scheduled area: 3264.03 ha
- Eligible blocks (age class >= 40): 174242
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.68 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 5.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
