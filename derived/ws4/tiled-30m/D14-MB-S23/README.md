# WS4 tiled 30-m dataset — D14|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D14|MB|S23` (parent `D14|MB`)
- Tile / row / col: `D14` / 2 / 3
- Province: `MB`
- Centroid: 50.032734, -99.008712
- Allocated harvest: 1077.408846 m3
- Productive subcell area: 23255.748089 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 604422
- Blocks: 119371
- Forest area: 54397.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7872
- Scheduled area: 4760.73 ha
- Eligible blocks (age class >= 40): 78712
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.32 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 6.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
