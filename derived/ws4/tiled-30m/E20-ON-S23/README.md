# WS4 tiled 30-m dataset — E20|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E20|ON|S23` (parent `E20|ON`)
- Tile / row / col: `E20` / 2 / 3
- Province: `ON`
- Centroid: 51.083156, -86.141028
- Allocated harvest: 29876.809935 m3
- Productive subcell area: 192198.875528 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2344676
- Blocks: 776830
- Forest area: 211020.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70358
- Scheduled area: 19909.26 ha
- Eligible blocks (age class >= 40): 703577
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.60 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 28.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
