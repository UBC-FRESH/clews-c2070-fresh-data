# WS4 tiled 30-m dataset — D30|NB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D30|NB|S31` (parent `D30|NB`)
- Tile / row / col: `D30` / 3 / 1
- Province: `NB`
- Centroid: 46.764262, -67.759346
- Allocated harvest: 5220.128378 m3
- Productive subcell area: 5408.830441 ha
- Committed geometry area: 6181.593137 ha
- Clipped inventory geometry: 6181.593137 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 52001
- Blocks: 20158
- Forest area: 4680.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1681
- Scheduled area: 342.18 ha
- Eligible blocks (age class >= 40): 16801
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.88 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
