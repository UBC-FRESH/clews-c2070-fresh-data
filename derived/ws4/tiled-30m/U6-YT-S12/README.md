# WS4 tiled 30-m dataset — U6|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|YT|S12` (parent `U6|YT`)
- Tile / row / col: `U6` / 1 / 2
- Province: `YT`
- Centroid: 68.358774, -136.665478
- Allocated harvest: 9.555883 m3
- Productive subcell area: 5154.360289 ha
- Committed geometry area: 60009.438325 ha
- Clipped inventory geometry: 60009.438325 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 16755
- Blocks: 13059
- Forest area: 1507.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 574
- Scheduled area: 61.74 ha
- Eligible blocks (age class >= 40): 5739
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.43 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
