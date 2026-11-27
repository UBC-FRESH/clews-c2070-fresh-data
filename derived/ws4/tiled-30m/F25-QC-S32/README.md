# WS4 tiled 30-m dataset — F25|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F25|QC|S32` (parent `F25|QC`)
- Tile / row / col: `F25` / 3 / 2
- Province: `QC`
- Centroid: 51.456222, -75.628337
- Allocated harvest: 29746.222024 m3
- Productive subcell area: 159257.145725 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1775246
- Blocks: 539498
- Forest area: 159772.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32194
- Scheduled area: 7312.95 ha
- Eligible blocks (age class >= 40): 321933
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.78 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 20.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
