# WS4 tiled 30-m dataset — E24|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E24|ON|S11` (parent `E24|ON`)
- Tile / row / col: `E24` / 1 / 1
- Province: `ON`
- Centroid: 49.772294, -79.600560
- Allocated harvest: 5125.948174 m3
- Productive subcell area: 47706.894507 ha
- Committed geometry area: 55973.937507 ha
- Clipped inventory geometry: 55973.937507 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 455502
- Blocks: 136389
- Forest area: 40995.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12768
- Scheduled area: 3767.49 ha
- Eligible blocks (age class >= 40): 127679
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.87 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 6.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
