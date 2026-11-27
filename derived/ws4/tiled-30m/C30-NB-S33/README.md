# WS4 tiled 30-m dataset — C30|NB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C30|NB|S33` (parent `C30|NB`)
- Tile / row / col: `C30` / 3 / 3
- Province: `NB`
- Centroid: 45.209701, -67.399609
- Allocated harvest: 4510.615865 m3
- Productive subcell area: 3973.481801 ha
- Committed geometry area: 4429.080669 ha
- Clipped inventory geometry: 4429.080669 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 47262
- Blocks: 19953
- Forest area: 4253.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1862
- Scheduled area: 339.30 ha
- Eligible blocks (age class >= 40): 18612
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.84 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
