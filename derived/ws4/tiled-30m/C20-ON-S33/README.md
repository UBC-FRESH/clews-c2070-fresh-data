# WS4 tiled 30-m dataset — C20|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C20|ON|S33` (parent `C20|ON`)
- Tile / row / col: `C20` / 3 / 3
- Province: `ON`
- Centroid: 48.906583, -86.596256
- Allocated harvest: 43521.548070 m3
- Productive subcell area: 152784.452279 ha
- Committed geometry area: 181231.208686 ha
- Clipped inventory geometry: 181231.208686 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1878369
- Blocks: 636813
- Forest area: 169053.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60530
- Scheduled area: 15883.29 ha
- Eligible blocks (age class >= 40): 605298
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.77 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 23.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
