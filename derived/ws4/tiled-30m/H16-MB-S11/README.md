# WS4 tiled 30-m dataset — H16|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H16|MB|S11` (parent `H16|MB`)
- Tile / row / col: `H16` / 1 / 1
- Province: `MB`
- Centroid: 55.109146, -96.372579
- Allocated harvest: 5853.763982 m3
- Productive subcell area: 184419.845316 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2037383
- Blocks: 614961
- Forest area: 183364.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54347
- Scheduled area: 11537.82 ha
- Eligible blocks (age class >= 40): 543468
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.52 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 23.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
