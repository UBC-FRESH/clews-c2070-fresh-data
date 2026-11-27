# WS4 tiled 30-m dataset — E23|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E23|ON|S22` (parent `E23|ON`)
- Tile / row / col: `E23` / 2 / 2
- Province: `ON`
- Centroid: 50.422566, -80.530112
- Allocated harvest: 24738.224058 m3
- Productive subcell area: 207196.269649 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2293719
- Blocks: 806712
- Forest area: 206434.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74746
- Scheduled area: 16906.59 ha
- Eligible blocks (age class >= 40): 747460
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.73 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 28.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
