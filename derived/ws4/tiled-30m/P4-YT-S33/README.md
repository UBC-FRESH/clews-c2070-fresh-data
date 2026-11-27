# WS4 tiled 30-m dataset — P4|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P4|YT|S33` (parent `P4|YT`)
- Tile / row / col: `P4` / 3 / 3
- Province: `YT`
- Centroid: 62.115691, -132.382377
- Allocated harvest: 236.260843 m3
- Productive subcell area: 170296.639153 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2289437
- Blocks: 757768
- Forest area: 206049.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65401
- Scheduled area: 17602.74 ha
- Eligible blocks (age class >= 40): 654006
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.85 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 27.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
