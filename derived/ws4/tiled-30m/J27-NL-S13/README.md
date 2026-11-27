# WS4 tiled 30-m dataset — J27|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J27|NL|S13` (parent `J27|NL`)
- Tile / row / col: `J27` / 1 / 3
- Province: `NL`
- Centroid: 54.433708, -67.707420
- Allocated harvest: 73.590143 m3
- Productive subcell area: 2086.903741 ha
- Committed geometry area: 4049.685150 ha
- Clipped inventory geometry: 4049.685150 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 27876
- Blocks: 10014
- Forest area: 2508.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 935
- Scheduled area: 202.68 ha
- Eligible blocks (age class >= 40): 9344
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.48 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
