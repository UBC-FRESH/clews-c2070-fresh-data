# WS4 tiled 30-m dataset — D23|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D23|ON|S11` (parent `D23|ON`)
- Tile / row / col: `D23` / 1 / 1
- Province: `ON`
- Centroid: 48.759920, -81.805051
- Allocated harvest: 41681.944236 m3
- Productive subcell area: 223204.920138 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2611067
- Blocks: 989936
- Forest area: 234996.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 90534
- Scheduled area: 19785.78 ha
- Eligible blocks (age class >= 40): 905333
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.64 MB
- Schedules: 1.08 MB
- Runs: 0.00 MB
- Total: 33.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
