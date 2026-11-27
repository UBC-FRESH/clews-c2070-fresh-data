# WS4 tiled 30-m dataset — F32|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F32|QC|S33` (parent `F32|QC`)
- Tile / row / col: `F32` / 3 / 3
- Province: `QC`
- Centroid: 47.277592, -61.699122
- Allocated harvest: 1839.978545 m3
- Productive subcell area: 5330.614164 ha
- Committed geometry area: 12571.041174 ha
- Clipped inventory geometry: 12571.041174 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 47849
- Blocks: 26847
- Forest area: 4306.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1819
- Scheduled area: 306.36 ha
- Eligible blocks (age class >= 40): 18190
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.96 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
