# WS4 tiled 30-m dataset — D16|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D16|ON|S33` (parent `D16|ON`)
- Tile / row / col: `D16` / 3 / 3
- Province: `ON`
- Centroid: 50.565496, -94.799165
- Allocated harvest: 38231.260450 m3
- Productive subcell area: 185203.429637 ha
- Committed geometry area: 249422.234986 ha
- Clipped inventory geometry: 249422.234986 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1005167
- Blocks: 405172
- Forest area: 90465.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23063
- Scheduled area: 4726.89 ha
- Eligible blocks (age class >= 40): 230630
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.58 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 12.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
