# WS4 tiled 30-m dataset — B22|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B22|ON|S13` (parent `B22|ON`)
- Tile / row / col: `B22` / 1 / 3
- Province: `ON`
- Centroid: 46.320296, -83.193311
- Allocated harvest: 34422.291730 m3
- Productive subcell area: 117509.031802 ha
- Committed geometry area: 130546.472776 ha
- Clipped inventory geometry: 130546.472776 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1134677
- Blocks: 367000
- Forest area: 102120.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34628
- Scheduled area: 9895.86 ha
- Eligible blocks (age class >= 40): 346278
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.88 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 14.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
