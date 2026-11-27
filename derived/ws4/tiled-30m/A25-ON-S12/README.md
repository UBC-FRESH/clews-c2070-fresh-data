# WS4 tiled 30-m dataset — A25|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A25|ON|S12` (parent `A25|ON`)
- Tile / row / col: `A25` / 1 / 2
- Province: `ON`
- Centroid: 44.147124, -78.748514
- Allocated harvest: 44155.719864 m3
- Productive subcell area: 156899.309954 ha
- Committed geometry area: 249026.890135 ha
- Clipped inventory geometry: 249026.890135 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1029847
- Blocks: 461967
- Forest area: 92686.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34170
- Scheduled area: 7140.33 ha
- Eligible blocks (age class >= 40): 341696
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.02 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 14.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
