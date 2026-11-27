# WS4 tiled 30-m dataset — D30|NB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D30|NB|S22` (parent `D30|NB`)
- Tile / row / col: `D30` / 2 / 2
- Province: `NB`
- Centroid: 46.086601, -67.638751
- Allocated harvest: 95716.446829 m3
- Productive subcell area: 99176.494103 ha
- Committed geometry area: 113345.896491 ha
- Clipped inventory geometry: 113345.896491 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 977038
- Blocks: 408762
- Forest area: 87933.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33940
- Scheduled area: 6044.76 ha
- Eligible blocks (age class >= 40): 339391
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.76 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 13.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
