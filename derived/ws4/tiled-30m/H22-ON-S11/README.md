# WS4 tiled 30-m dataset — H22|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H22|ON|S11` (parent `H22|ON`)
- Tile / row / col: `H22` / 1 / 1
- Province: `ON`
- Centroid: 54.396450, -82.464835
- Allocated harvest: 786.795231 m3
- Productive subcell area: 14173.379728 ha
- Committed geometry area: 56368.755782 ha
- Clipped inventory geometry: 56368.755782 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 211640
- Blocks: 66531
- Forest area: 19047.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4199
- Scheduled area: 1286.73 ha
- Eligible blocks (age class >= 40): 41982
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.93 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 2.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
