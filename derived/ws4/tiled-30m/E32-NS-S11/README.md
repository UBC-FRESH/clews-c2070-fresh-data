# WS4 tiled 30-m dataset — E32|NS|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|NS|S11` (parent `E32|NS`)
- Tile / row / col: `E32` / 1 / 1
- Province: `NS`
- Centroid: 45.807909, -64.214752
- Allocated harvest: 23012.312411 m3
- Productive subcell area: 49078.283630 ha
- Committed geometry area: 60656.732488 ha
- Clipped inventory geometry: 60656.732488 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 474052
- Blocks: 160948
- Forest area: 42664.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12088
- Scheduled area: 2677.05 ha
- Eligible blocks (age class >= 40): 120874
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.30 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 6.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
