# WS4 tiled 30-m dataset — E16|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E16|MB|S23` (parent `E16|MB`)
- Tile / row / col: `E16` / 2 / 3
- Province: `MB`
- Centroid: 51.481585, -95.155675
- Allocated harvest: 64.526835 m3
- Productive subcell area: 1440.212669 ha
- Committed geometry area: 1908.573650 ha
- Clipped inventory geometry: 1908.573650 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 10615
- Blocks: 4722
- Forest area: 955.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4236
- Scheduled area: 741.24 ha
- Eligible blocks (age class >= 40): 4236
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.24 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
