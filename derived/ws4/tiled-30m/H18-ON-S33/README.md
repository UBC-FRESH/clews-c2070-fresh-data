# WS4 tiled 30-m dataset — H18|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|ON|S33` (parent `H18|ON`)
- Tile / row / col: `H18` / 3 / 3
- Province: `ON`
- Centroid: 55.914552, -89.857535
- Allocated harvest: 10369.748452 m3
- Productive subcell area: 129646.606750 ha
- Committed geometry area: 246060.459644 ha
- Clipped inventory geometry: 246060.459644 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1763952
- Blocks: 605278
- Forest area: 158755.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47251
- Scheduled area: 12743.01 ha
- Eligible blocks (age class >= 40): 472506
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.98 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 21.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
