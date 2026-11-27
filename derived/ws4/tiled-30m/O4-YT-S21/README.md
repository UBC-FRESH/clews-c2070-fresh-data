# WS4 tiled 30-m dataset — O4|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|YT|S21` (parent `O4|YT`)
- Tile / row / col: `O4` / 2 / 1
- Province: `YT`
- Centroid: 60.139163, -131.879381
- Allocated harvest: 201.402867 m3
- Productive subcell area: 123806.486047 ha
- Committed geometry area: 165891.264117 ha
- Clipped inventory geometry: 165891.264117 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1473825
- Blocks: 754910
- Forest area: 132644.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72251
- Scheduled area: 12940.02 ha
- Eligible blocks (age class >= 40): 722504
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.23 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 22.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
