# WS4 tiled 30-m dataset — H30|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H30|QC|S12` (parent `H30|QC`)
- Tile / row / col: `H30` / 1 / 2
- Province: `QC`
- Centroid: 50.543409, -64.575996
- Allocated harvest: 47860.132653 m3
- Productive subcell area: 193254.336037 ha
- Committed geometry area: 242626.830907 ha
- Clipped inventory geometry: 242626.830907 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2389811
- Blocks: 896546
- Forest area: 215082.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85631
- Scheduled area: 21334.68 ha
- Eligible blocks (age class >= 40): 856309
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.05 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 31.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
